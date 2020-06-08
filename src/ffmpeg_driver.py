from src import ffmpeg_converter

CONVERT_AVI_TO_MP4_MODE = 'avi to mp4'
CONVERT_MP4_TO_MP3_MODE = 'mp4 to mp3'


def main():
    print("Please input the mode you would like to use.")
    mode = input("Available Modes: 'AVI to MP4', 'MP4 to MP3'\n").lower()

    print("Ensure that ffmpeg.exe is located in the same directory as the directory inputted")
    if mode == CONVERT_AVI_TO_MP4_MODE:
        directory = input("Input directory to convert .avi to .mp4\n")
        ffmpeg_converter.convert_avi_to_mp4(directory)
    elif mode == CONVERT_MP4_TO_MP3_MODE:
        directory = input("Input directory to convert .mp4 to .mp3\n")

        file_names = []
        print("Input file names to convert -- Hit enter with nothing when finished")
        while True:
            file_name = input()

            if file_name:
                file_names.append(file_name)
            else:
                break
        ffmpeg_converter.convert_mp4_to_mp3(directory, file_names)
    else:
        print("Error, inputted mode not found")
    print("Done")


if __name__ == "__main__":
    main()