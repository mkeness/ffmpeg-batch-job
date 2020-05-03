# ffmpeg-batch-job
Cooked up some quick scripts to use ffmpeg to perform batch jobs on videos

Had a ton of old .avi files and wanted to convert them into smaller files (h264)

Further development could involve allowing the user to determine length of videos, 
specific bit rates, multiple input directories/files, multiple output directories/files
and more.

## Usage
1. Ensure ffmpeg.exe (that would normally be used in CLI) is located in the same directory
as the raw video files
2. Run ffmpeg_driver.py
3. Input into the console the directory to convert .avi files into .mp4 
(.avi files will NOT be overwritten)
