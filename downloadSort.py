import os
from shutil import move

def main():
    moverHandler()
   
        
def moverHandler():
    sourceDir = "C:\\Users\\natea\\Downloads\\keep"
    destMusic = "C:\\Users\\natea\\Music"
    destImg = "C:\\Users\\natea\\OneDrive\\Pictures\\temp"
    destPDF = "C:\\Users\\natea\\OneDrive\\Textbooks\\temp"
    with os.scandir(sourceDir) as files:
        for file in files:
            fileName = file.name
            dest = sourceDir
            theFile = dest +"\\"+ file.name
            if  fileName.endswith(".png") or fileName.endswith(".jpg") or fileName.endswith(".jpeg"):
                dest = destImg
                move(theFile, dest)
            elif fileName.endswith(".mp3") or fileName.endswith(".wav"):
                dest = destMusic
                move(theFile, dest)
            elif fileName.endswith(".pdf"):
                dest = destPDF
                move(theFile, dest)
            print(fileName +" move to " + dest +" from " + sourceDir)


if __name__ == '__main__':
    main()