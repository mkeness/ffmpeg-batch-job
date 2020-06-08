import os
import subprocess

AVI_EXTENSION = ".avi"
MP3_EXTENSION = ".mp3"
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
            subprocess.call(f'ffmpeg -ss 00:00:00.0 -i "{file_name}{AVI_EXTENSION}" \
                -map 0 -b:v 50M -minrate 50M -maxrate 50M -bufsize 100M \
                "{file_name}{MP4_EXTENSION}"', shell=True)
        else:
            print(f"unknown extension: {extension}")
    # TODO: Return number of files converted/processed


def convert_mp4_to_mp3(directory_name, file_names):
    """
    Convert .mp4 files to .mp3 files
    :param directory_name: Directory to search for file names (will search through folders)
    :param file_names: List of strings (file names)
    :return:
    """
    if not directory_name or not file_names:
        return

    os.chdir(directory_name)

    for root, dirs, files in os.walk(directory_name):
        for file_name_with_extension in files:
            file_name_no_extension = os.path.splitext(file_name_with_extension)[0]
            if file_name_no_extension in file_names or file_name_with_extension in file_names:
                print(f'Input File: {file_name_no_extension}{MP4_EXTENSION}')
                print(f'Output File: {file_name_no_extension}{MP3_EXTENSION}')
                print(os.path.join(root, file_name_with_extension))

                # Use double quotes around file names in case there are spaces in the file name
                # ffmpeg cmd source: https://askubuntu.com/questions/84584/converting-mp4-to-mp3
                subprocess.call(f'ffmpeg -i "{file_name_no_extension}{MP4_EXTENSION}" -vn -sn -dn \
                    -acodec libmp3lame -ac 2 -ab 190k -ar 48000 \
                    "{file_name_no_extension}{MP3_EXTENSION}"', shell=True)
    # TODO: Return number of files converted/processed
