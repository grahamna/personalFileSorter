# personalFileSorter

## python --version
 Python 3.9.7

 OS : Windows 10

## Prerequisites
 Python 3
 watchdog module (you can install it via pip: pip install watchdog)

## Usage
 Clone the repository or download the downloadSort.py file.
 Open the downloadSort.py file in a text editor.
 Edit the sourceDir, destMusic, destImg, and destPDF variables to reflect your own directory paths.
 Run the script in your terminal with the command python downloadSort.py, or use the included shell script.
 The script will run indefinitely until it is interrupted with a keyboard interrupt (CTRL + C).

## How It Works
 The OnMyWatch class sets up an observer to watch the sourceDir directory for any file creation or modification events. When an event occurs, the Handler class is triggered.

 The moverHandler class is then called and passed the path of the file that triggered the event. The class checks the file extension type and moves the file to its respective folder (specified by destMusic, destImg, or destPDF).

## Notes
 The script will not move itself (downloadSort.py) or any shell script (script.sh) that may be in the sourceDir.
 If the script encounters a file type that it does not recognize, it will print a message to the console and take no action.
