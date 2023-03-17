# imports YoutuberConverter class, InvalidURL exception, os for directory validation and validate_url function

import os
from url_validation import validate_url
from youtube_converter import YoutubeConverter
from invalid_url import InvalidURL


def main():
    print("Welcome to Adem's YouTube to Audio Converter!")
    # runs validation on url input
    while True:
        try:
            url = input('Enter Youtube URl of video to convert: ')
            if validate_url(url):
                break
        except InvalidURL as i:
            print(i)
    # runs validation on directory input
    while True:
        output_dir = input('Enter directory where you want the file to be saved to: ')
        if os.path.isdir(output_dir):
            break
        else:
            print('Invalid directory. Enter a valid directory path.')
    # runs validation on output format
    while True:
        output_format = input('Enter output format (enter mp3 or wav): ')
        if output_format == 'mp3' or output_format == 'wav':
            break
        else:
            print('Invalid format. Enter mp3 or wav.')

    # Uses class methods
    try:
        converter = YoutubeConverter(url, output_dir)
        converter.download_audio(output_format)
    # exception to cover unforeseen stuff
    except Exception as e:
        print(e)


# this is the main script so duh will run
if __name__ == "__main__":
    main()
