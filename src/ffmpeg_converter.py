import os
import subprocess

AVI_EXTENSION = "avi"
MP4_EXTENSION = "mp4"


def convert_avi_to_mp4(directory_name):
    """
    Convert .avi to mp4
    :param directory_name: The directory to convert .avi to .mp4 files
    :return:
    """
    full_file_names = os.listdir(directory_name)
    for full_file_name in full_file_names:
        print(full_file_name)
        file_name_and_extension = full_file_name.split('.')
        file_name = file_name_and_extension[:len(file_name_and_extension) - 1][0] if len(file_name_and_extension[:len(file_name_and_extension) - 1]) > 0 else ''
        extension = file_name_and_extension[len(file_name_and_extension) - 1:][0] if len(file_name_and_extension[len(file_name_and_extension) - 1:]) > 0 else ''
        print(extension)

        if file_name == '' or extension == '':
            print('Early break -- Empty file name/extension')
            continue

        if extension == AVI_EXTENSION:
            print("avi extension detected")
            print(f"{file_name}.{AVI_EXTENSION}")
            os.chdir(directory_name)

            print(f'{file_name}.{AVI_EXTENSION}')
            print(f'{file_name}.{MP4_EXTENSION}')

            # Use double quotes around file names in case there are spaces in the file name
            subprocess.call(f'ffmpeg -ss 00:00:00.0 -i "{file_name}.{AVI_EXTENSION}" -map 0 -b:v 50M -minrate 50M -maxrate 50M -bufsize 100M "{file_name}.{MP4_EXTENSION}"', shell=True)
        else:
            print(f"unknown extension: {extension}")
