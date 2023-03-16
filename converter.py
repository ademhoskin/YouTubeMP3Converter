# i will need pytube to get the audio mp4  and use ffmpeg to convert mp4 to mp3/wav, use regex to validate url
from pytube import Youtube
import subprocess
import re


# our custom exception: the invalid url
class InvalidURL(Exception):
    def __init__(self, message="Error: Invalid Youtube URL"):
        self.message = message

    def __str__(self):
        return self.message


# our class the YouTube Converter
class YoutubeConverter(object):
    # this will use user input to create an object
    def __init__(self, url, output_dir):
        self.url = url
        self.output_dir = output_dir

    # uses the url and output_dir to validate and download audio in mp4 (i hate pytube)
    def download_audio(self):
        # regex validation/exception implementation
        url_pattern = re.compile(r'https?://(www\.)?youtube\.com/watch\?v=\w+')
        if not url_pattern.match(self.url):
            raise InvalidURL()

        # Download the YouTube video using pytube
        yt = Youtube(self.url)
        title = yt.title
        clean_title = re.sub('[^0-9a-zA-Z]+', '_', title)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path=self.output_dir, filename='audio')

    # ffmpeg conversion method, will take the user's requested output format to convert the mp4 to (wav or mp3)
    def convert_audio(self, output_format):
        input_file = self.output_dir + ''







