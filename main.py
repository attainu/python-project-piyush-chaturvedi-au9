# File Organizer
import os
import shutil


audio = [".mp3",".wma",".aac",".aif",".cda",".mid",".midi",".ogg",".wav",".wpl"]
video = [".mp4",".wmv",".avi",".mkv"]
docs = [".docx",".pdf",".pptx",".xlsx",".rtf",".txt"]
software = [".exe",".apk"]
zips = [".zip",".rar",".7z",".arj",".deb",".pkg",".rpm",".tar.gz",".z",".deb"]
image = [".ai",".bmp",".gif",".jpeg",".png",".tif"]
path = os.getcwd()
files = os.listdir(path)
# print (files)

os.mkdir(path+"\\"+"audio")
os.mkdir(path+"\\"+"image")
os.mkdir(path+"\\"+"video")
os.mkdir(path+"\\"+"docs")
os.mkdir(path+"\\"+"software")
os.mkdir(path+"\\"+"zips")
os.mkdir(path+"\\"+"unknown")

for file in files:
    extension = os.path.splitext(file)[1]
    # print(extension)
    if extension == "":
        files1 = os.listdir(path + "\\" + file)
        for file1 in files1:
            ext = os.path.splitext(file1)[1]
            newpath = path+"\\"+file+"\\"
            if ext in audio:
                shutil.move(newpath + file1,path+"\\"+"audio")
            elif ext in video:
                shutil.move(newpath + file1,path+"\\"+"video")
            elif ext in image:
                shutil.move(newpath + file1,path+"\\"+"image")
            elif ext in docs:
                shutil.move(newpath + file1,path+"\\"+"docs")
            elif ext in software:
                shutil.move(newpath + file1,path+"\\"+"software")
            elif ext in zips:
                shutil.move(newpath + file1,path+"\\"+"zips")
            else:
                shutil.move(newpath + file1,path+"\\"+"unknown")

    elif extension in audio:
                shutil.move(path +"\\" + file,path +"\\"+ "audio")
    elif extension in video:
                shutil.move(path +"\\" + file,path +"\\"+ "video")
    elif extension in image:
                shutil.move(path +"\\" + file,path +"\\"+"image")
    elif extension in docs:
                shutil.move(path +"\\" + file,path +"\\"+ "docs")
    elif extension in software:
                shutil.move(path +"\\" + file,path +"\\"+ "software")
    elif  extension in zips:
                shutil.move(path +"\\" + file,path +"\\"+ "zips")
    else:
                shutil.move(path +"\\" + file,path +"\\"+ "unknown")
