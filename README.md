# YouTube Converter

This is a simple YouTube to WAV/MP3 converter written in Python. It uses the PyTube and FFmpeg libraries to download YouTube videos and convert them to the desired format.
Requirements

To use this converter, you will need to have the following software installed:

    Python 3.x
    PyTube library (pip install pytube)
    FFmpeg library (sudo apt-get install ffmpeg or brew install ffmpeg)

## Usage

    Clone or download the repository to your local machine.

    Open a terminal or command prompt and navigate to the repository directory.

    Run the following command to start the converter:

    python converter.py

    Follow the prompts to enter the YouTube video URL, output directory, and output format (WAV or MP3).

    The converter will download the audio in MP4 format using PyTube and convert it to the desired format using FFmpeg.

    The converted audio file will be saved in the specified output directory with a filename based on the title of the YouTube video.

## Notes

    This converter currently only supports YouTube video URLs in the format https://www.youtube.com/watch?v=<video_id>. Other URL formats may not work.
    If the download or conversion fails, the converter will print an error message and exit. Please check your internet connection and make sure that the output directory is valid.
