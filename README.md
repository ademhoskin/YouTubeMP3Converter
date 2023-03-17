# Youtube to MP3/WAV Converter

This is a user-friendly script that allows the user to download .mp3 or .wav files

## Custom Modules Implemented

### Invalid URL Exception Module

This custom module defines the `InvalidURL` exception class, which is used to handle invalid YouTube URL errors.

#### Class

##### `InvalidURL(message="Error: Invalid Youtube URL")`

- **Parameters:** `message` (string) - The error message to be displayed when the exception is raised (default: "Error: Invalid Youtube URL").
- **Methods:** `__str__()` - Returns the error message as a string.

#### Usage

You can use this module in your Python project by importing and raising the `InvalidURL` exception:

```python
from invalid_url import InvalidURL

# Your code here...

raise InvalidURL("Custom error message")
```

### URL Validation Module

This custom module provides functionality to validate YouTube URLs using regular expressions.

#### Functions

##### `validate_url(url)`

- **Parameters:** `url` (string) - The URL to be validated
- **Returns:** `True` if the URL is a valid YouTube URL, otherwise raises an `InvalidURL` exception.

#### Dependencies

- `re` (Python standard library)
- `InvalidURL` (custom exception class)

### URL Validation Module

This custom module provides functionality to validate YouTube URLs using regular expressions.

#### Functions

##### `validate_url(url)`

- **Parameters:** `url` (string) - The URL to be validated
- **Returns:** `True` if the URL is a valid YouTube URL, otherwise raises an `InvalidURL` exception.

#### Dependencies

- `re` (Python standard library)
- `InvalidURL` (custom exception class)

#### Usage

You can use this module in your Python project by importing and calling the `validate_url` function:

```python
from url_validation import validate_url

url = "https://www.youtube.com/watch?v=example"
try:
    is_valid = validate_url(url)
    print("Valid URL")
except InvalidURL:
    print("Invalid URL")
```
### YouTube Converter Module

This custom module provides functionality to download audio from YouTube videos using the `yt-dlp` library and sanitize the title using regular expressions.

#### Class

##### `YoutubeConverter(url, output_dir)`

- **Parameters:**
  - `url` (string) - The URL of the YouTube video to download audio from.
  - `output_dir` (string) - The directory where the audio file will be saved.

- **Methods:**
  - `download_audio(output_format)` - Downloads the audio from the YouTube video and saves it in the specified format.

#### Dependencies

- `yt-dlp` - A Python library for downloading videos and audio from YouTube and other video platforms.
- `re` (Python standard library)

#### Usage

You can use this module in your Python project by importing the `YoutubeConverter` class and creating an instance with the desired YouTube URL and output directory:

```python
from youtube_converter import YoutubeConverter

url = "https://www.youtube.com/watch?v=example"
output_dir = "/path/to/output/directory"

converter = YoutubeConverter(url, output_dir)
converter.download_audio("mp3")
```

## Main Script (The GUI Converter)
This script uses `PySimpleGUI` to create a simple graphical user interface for downloading audio from YouTube videos. It utilizes the custom modules `url_validation`, `youtube_converter`, and `invalid_url` to perform URL validation and audio downloading.

### Functions

#### `download_audio(url, output_dir, output_format)`

- **Parameters:**
  - `url` (string) - The YouTube URL to download audio from.
  - `output_dir` (string) - The directory where the audio file will be saved.
  - `output_format` (string) - The audio format to save the file in ("mp3" or "wav").
- **Functionality:** Validates the provided URL, downloads the audio using the `YoutubeConverter` class, and displays success or error messages using `PySimpleGUI` popups.

#### `get_output_directory()`

- **Functionality:** Opens a file dialog for the user to select an output directory and returns the selected directory as a string.

#### `main()`

- **Functionality:** Creates the main window of the application using `PySimpleGUI`, defines the layout, and handles button events for downloading audio, browsing the output directory, and exiting the application.

### Dependencies

- `tkinter` (Python standard library)
- `filedialog` (from `tkinter`)
- `PySimpleGUI`
- `url_validation` (custom module)
- `youtube_converter` (custom module)
- `invalid_url` (custom module)

## Usage

### Method 1
Open the "YoutubeAudioConverter" executable in the 'dist' folder. (due to pyinstaller, you may have to turn your antivirus 
off for the file)

### Method 2 (using the script )
Run the script using the following command on your terminal:

```bash
python __main__.py
```
## Notes:
Make sure when downloading, you have permissions on the directory, 
otherwise you will get an error popup. (Errno 13- Permission Denied)
### Known Issues:
When program successfully downloads, the popup window is not visible.
The program will still work, just close the window through your taskbar.
I will figure a fix for it :).





