from src import ffmpeg_converter


def main():
    # directory to use
    # 1st usage - convert .avi to .mp4

    print("Ensure that ffmpeg.exe is located in the same directory as the raw video files")
    directory = input("Input directory to convert .avi to .mp4\n")
    print(directory)

    ffmpeg_converter.convert_avi_to_mp4(directory)

    print("Done")


if __name__ == "__main__":
    main()