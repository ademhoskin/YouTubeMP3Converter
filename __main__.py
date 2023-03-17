import tkinter as tk
from tkinter import filedialog
import PySimpleGUI as sg
from url_validation import validate_url
from youtube_converter import YoutubeConverter
from invalid_url import InvalidURL

# Function to download audio from YouTube URL
def download_audio(url, output_dir, output_format):
    try:
        # Validate the URL
        if validate_url(url):
            # Download the audio using the YoutubeConverter class
            converter = YoutubeConverter(url, output_dir)
            converter.download_audio(output_format)
            # Display success message using PySimpleGUI popup
            sg.popup("Success", "Audio downloaded successfully!")
        else:
            # Raise an InvalidURL exception if URL is not valid
            raise InvalidURL()
    except InvalidURL as i:
        # Display error message using PySimpleGUI popup
        sg.popup_error("Error", str(i))
    except Exception as e:
        # Display error message using PySimpleGUI popup
        sg.popup_error("Error", str(e))

# Function to get output directory using a file dialog
def get_output_directory():
    root = tk.Tk()
    root.withdraw()
    # Open file dialog and get the selected directory
    output_dir = filedialog.askdirectory()
    root.destroy()
    return output_dir

# PySimpleGUI layout for the main window
def main():
    layout = [
        [sg.Text("YouTube URL:")],
        [sg.Input(key="url")],
        [sg.Text("Output directory:")],
        [sg.Input(key="output_dir"), sg.Button("Browse", key="browse_output_dir")],
        [sg.Text("Output format:")],
        [sg.Radio("mp3", "format", default=True, key="mp3"), sg.Radio("wav", "format", key="wav")],
        [sg.Button("Download Audio"), sg.Button("Exit")],
    ]

    # Create PySimpleGUI window with the layout
    window = sg.Window("Adem's YouTube to Audio Converter", layout)

    # Event loop for the window
    while True:
        event, values = window.read()

        # Close the window if the "Exit" button or close icon is clicked
        if event == sg.WIN_CLOSED or event == "Exit":
            break

        # Call the download_audio function if the "Download Audio" button is clicked
        if event == "Download Audio":
            url = values["url"]
            output_dir = values["output_dir"]
            output_format = "mp3" if values["mp3"] else "wav"
            download_audio(url, output_dir, output_format)

        # Call the get_output_directory function if the "Browse" button next to the output directory input is clicked
        if event == "browse_output_dir":
            output_dir = get_output_directory()
            window["output_dir"].update(value=output_dir)

    # Close the window at the end of the event loop
    window.close()

if __name__ == "__main__":
    main()
