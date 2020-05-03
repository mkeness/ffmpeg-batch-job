import os
import subprocess

AVI_EXTENSION = ".avi"
MP4_EXTENSION = ".mp4"


def convert_avi_to_mp4(directory_name):
    """
    Convert .avi to mp4
    :param directory_name: The directory to convert .avi to .mp4 files
    :return:
    """
    os.chdir(directory_name)
    full_file_names = [file for file in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), file))]

    for full_file_name in full_file_names:
        file_name = os.path.splitext(full_file_name)[0]
        extension = os.path.splitext(full_file_name)[1]

        print(file_name)
        print(extension)

        if file_name == '' or extension == '':
            print('Early break -- Empty file name/extension')
            continue

        if extension == AVI_EXTENSION:
            print("avi extension detected")
            print(f'Input File: {file_name}{AVI_EXTENSION}')
            print(f'Output File: {file_name}{MP4_EXTENSION}')

            # Use double quotes around file names in case there are spaces in the file name
            subprocess.call(f'ffmpeg -ss 00:00:00.0 -i "{file_name}{AVI_EXTENSION}" -map 0 -b:v 50M -minrate 50M -maxrate 50M -bufsize 100M "{file_name}{MP4_EXTENSION}"', shell=True)
        else:
            print(f"unknown extension: {extension}")
