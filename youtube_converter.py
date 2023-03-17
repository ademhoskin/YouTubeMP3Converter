# uses youtube_dl for downloading audio and re for title sanitation
import yt_dlp
import re


# our class the YouTube Converter
class YoutubeConverter(object):
    # this will use user input to create an object
    def __init__(self, url, output_dir):
        self.url = url
        self.output_dir = output_dir
        self.format = None
        self.clean_title = None

    def download_audio(self, output_format):
        self.format = output_format

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.output_dir}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': output_format,
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.url, download=True)
            title = info_dict.get('title', None)
            if title is not None:
                self.clean_title = re.sub('[^0-9a-zA-Z]+', '_', title)
