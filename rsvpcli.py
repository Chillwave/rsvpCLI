import time
import sys
import os
import select
import re
import pyperclip

# Obtain working directory (diagnostics)
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
print("Script directory:", script_directory)

def sanitize_text(text):
    # Remove special characters
    sanitized = re.sub(r'[^\x00-\x7F]+', ' ', text)
    
    # Remove URLs
    sanitized = re.sub(r'http\S+', '', sanitized)

    # Remove multiple spaces
    sanitized = ' '.join(sanitized.split())

    return sanitized

def extract_text(filename=None):
    if filename:
        with open(filename, 'r') as file:
            return file.read().split()
    elif not sys.stdin.isatty():
        return sys.stdin.read().split()
    else:
        return []

def display_text(words, wpm):
    word_count = len(words)
    interval = 60 / wpm
    idx = 0

    while idx < word_count:
        word = words[idx]
        middle = len(word) // 2
        formatted_word = word[:middle] + '\033[1m' + word[middle] + '\033[0m' + word[middle+1:]
        
        print(f"\r({idx}/{word_count} - {idx*100/word_count:.2f}%)      {formatted_word}      ", end="", flush=True)
        
        time.sleep(interval)
        
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            command = input().strip()
            if command == 'l':
                idx += 25
            elif command == 'k':
                idx = max(0, idx - 25)
            elif command == 'p':
                wpm += 25
                interval = 60 / wpm
            elif command == 'o':
                wpm = max(25, wpm - 25)
                interval = 60 / wpm
        else:
            idx += 1

    print("\rReading completed at "+str(wpm)+" wpm!                      ")

def main():
    text = []  # Initialize text to an empty list
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        text = extract_text(filename)
    else:
        content = pyperclip.paste()
        if content:
            text = sanitize_text(content).split()  # Convert the string to a list of words
        else:
            print("No text provided. Exiting.")
            sys.exit()
    
    wpm = 400  # default wpm

    while True:
        print("Do not forget to blink. [Dry eyes note]")
        print("Current WPM: "+str(wpm))
        print("COMMANDS:")
        print("s - set WPM")
        print("n - load new text file")
        print("[p + enter] - (increase speed), [o + enter] - (decrease speed)")
        print("[k + enter] (skip back 25 words), [l + enter] - (skip ahead 25 words)")

        command = input("Press Enter to begin reading the file. Press enter again to move a particular word to a new line.")

        if command == '':
            display_text(text, wpm)
        elif command == 'n':
            filename = input("Enter the name of the new text or PDF file: ")
            text = extract_text(filename)
        elif command == 's':
            wpm = int(input("Enter new WPM: "))

if __name__ == "__main__":
    main()
