"""
Created by Farouk Bilesanmi
Date: 9/10/2019
Description:This script organizes downloaded files into separate folders depending
on the file type. This was made for windows systems.
Download directory should be the first command line argument
New file types can be added to the dictionary in the main method

"""

import os
import hashlib

#Creates folders for different file types
def makefolders(downloaddirectory, filetypes):
    """
    makefolders function
    """
    for filetype in filetypes.keys():
        directory = downloaddirectory + "\\" + filetype
        if not os.path.exists(directory):
            os.mkdir(directory)

#Moves file to its proper folder and delete any duplicates
def movefile(movefile, downloaddirectory, filetypes):
    """
    movefile function
    """
    #The file format is what is after the period in the file name
    if "." in movefile:
        temp = movefile.split(".")
        fileformat = temp[-1]
    else:
        return

    for filetype in filetypes.keys():
        if fileformat in filetypes[filetype]:
            srcpath = downloaddirectory + "\\" + movefile
            dstpath = downloaddirectory + "\\" + filetype + "\\" + movefile

            #If the file doesn't have a duplicate in the new folder, move it
            if not os.path.isfile(dstpath):
                os.rename(srcpath, dstpath)
            #If the file already exists with that name and has the same md5 sum
            elif os.path.isfile(dstpath) and \
                 checksum(srcpath) == checksum(dstpath):
                os.remove(srcpath)
                print("removed " + srcpath)
                return
#Get md5 checksum of a file. Chunk size is how much of the file to read at a time.
def checksum(filedir, chunksize=8192):
    """
    checksum function
    """
    md5 = hashlib.md5()
    file = open(filedir)
    while True:
        chunk = file.read(chunksize)
        #If the chunk is empty, reached end of file so stop
        if not chunk:
            break
        md5.update(chunk)
    file.close()
    return md5.hexdigest()

def main():
    """
    main function
    """
    #Dictionary contains file types as keys and lists of their corresponding file formats
    filetypes = {}
    filetypes["Images"] = ["jpg", "gif", "png", "jpeg", "bmp"]
    filetypes["Audio"] = ["mp3", "wav", "aiff", "flac", "aac"]
    filetypes["Video"] = ["m4v", "flv", "mpeg", "mov", "mpg", "mpe", "wmv",\
                          "MOV", "mp4", "mkv", "avi"]
    filetypes["Documents"] = ["doc", "docx", "txt", "ppt", "pptx", "pdf", "rtf", "xlsx",\
                              "xls", "csv"]
    filetypes["Exe"] = ["exe"]
    filetypes["Python files"] = ["py", "whl", "ipynb"]
    filetypes["Exe"] = ["exe"]
    filetypes["Compressed"] = ["zip", "tar", "7", "rar"]
    filetypes["Virtual_Machine_and_iso"] = ["vmdk", "ova", "iso"]
    filetypes["Torrents"] = ["torrent"]
    filetypes["Subtitles"] = ["srt"]

    #The second command line argument is the download directory
    downloaddirectory = input("Enter the folder directory:  ")
    downloadfiles = os.listdir(downloaddirectory)
    makefolders(downloaddirectory, filetypes)

    for filename in downloadfiles:
        movefile(filename, downloaddirectory, filetypes)
    print("Done!")

main()
