# uses pytube to get video from youtube, subprocess to run ffmpeg commands, and re for title sanitation
from pytube import YouTube
import subprocess
import re


# our class the YouTube Converter
class YoutubeConverter(object):
    # this will use user input to create an object, will also initialize the clean_title attribute for conversion method
    def __init__(self, url, output_dir):
        self.url = url
        self.output_dir = output_dir
        self.clean_title = None

    # uses the url and output_dir to validate and download audio in mp4 (I hate pytube)
    def download_audio(self):
        # Download the YouTube video using pytube
        yt = YouTube(self.url)
        title = yt.title
        self.clean_title = re.sub('[^0-9a-zA-Z]+', '_', title)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path=self.output_dir, filename=self.clean_title)

    # ffmpeg conversion method, will take the user's requested output format to convert the mp4 to (wav or mp3)
    def convert_audio(self, output_format):
        input_file = self.clean_title
        if output_format == 'mp3':
            output_file = f'{self.output_dir}/{self.clean_title}.mp3'
            command = ["ffmpeg", "-i", input_file, "-vn", "-ar", "44100", "-ac", "2", "-b:a", "192k", output_file]
        elif output_format == 'wav':
            output_file = f'{self.output_dir}/{self.clean_title}.wav'
            command = ["ffmpeg", "-i", input_file, "-vn", "-acodec", "pcm_s16le", "-ac", "2", "-ar", "44100", output_file]
        else:
            print('Invalid output format!')
            return

        subprocess.call(command)
