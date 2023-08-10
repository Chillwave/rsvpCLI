# RSVP (Rapid Serial Visual Presentation) CLI

## RSVP CLI is a Python script designed to help users read text files and clipboard content at a rapid pace, word by word. The methodology employed is based on the RSVP method of speed reading, which presents words in quick succession to increase reading speed.

### Features

* Read text from files or directly from the clipboard.
* Control reading speed (words per minute).
* Navigation controls to skip ahead or go back.
* Display the current reading position and progress percentage.

### Prerequisites
To run the script, ensure you have the pyperclip package for clipboard access. 

* Install using pip:
* pip install pyperclip

### Usage

* Navigate to the directory containing the script.
* Run the script:

* python rsvpcli.py [filename]

Replace [filename] with the name of a text or PDF file you want to read. This argument is optional.
If no filename is provided, the script will prompt you to paste your clipboard contents for reading.
Follow on-screen instructions to control the reading process.


The variable on line 79 "wpm = 400" can be adjusted to set the default WPM to your preference.


### Commands

[Enter]: Begin reading the file. Press again to move a particular word to a new line.
n: Load a new text file.
s: Set words per minute (WPM).
[p + enter]: Increase reading speed.
[o + enter]: Decrease reading speed.
[k + enter]: Skip back 25 words.
[l + enter]: Skip ahead 25 words.

### In action

* Within Kubuntu, Scroll lock was used as a keybind to open a konsole session with the script. This reads clipboard contents and allows you to rapidly read a selected sum of text.
  
https://youtube.com/shorts/uiw-lePGQqU?feature=share

### License
This project is open-source. Feel free to modify, distribute, and use it as you see fit.
