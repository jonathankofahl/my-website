import shutil
import sys, os
from datetime import date
########## Script to copy images from photo-database to website images folder

# helper methots to print to txt file
def writeToTXTLog(text):
 mypath = os.path.dirname(os.path.abspath(__file__))
 print("writeToTXTLog: " + str(mypath))
 with open(str(mypath)+'/log.txt', 'a') as f:
    f.write(str(text+"\n"))

def deleteLogTXT():
  with open('log.txt', 'w') as f:
    f.write("\n")

#0. prepare log txt
#deleteLogTXT()
#writeToTXTLog("START NOW AT TIME " + str(date.today()))
#writeToTXTLog("PYTHON VERSION:")
#writeToTXTLog(sys.version)
#1. remove all files from images folder in website
path = os.getcwd()
writeToTXTLog(path)
 
# prints parent directory
writeToTXTLog(os.path.abspath(os.path.join(path, os.pardir)))
parentDirectory = os.path.abspath(os.path.join(path, os.pardir))
parentDirectory = str(parentDirectory) + "/jonathp"
targetDirectory = str(parentDirectory) + "/public_html/imgPhotos"

print("######### parentDirectory " + str(parentDirectory))
print("######### targetDirectory " + str(targetDirectory))
writeToTXTLog("######### parentDirectory " + str(parentDirectory))
writeToTXTLog("######### targetDirectory " + str(targetDirectory))

for image in os.listdir(targetDirectory):
    os.remove(os.path.join(targetDirectory, image))

print("######### .. removed all pictures")
writeToTXTLog("######### .. removed all pictures" + str(targetDirectory))

#2. read in the actual counter
counter = "0"
with open(str(parentDirectory) + "/scripts/" + "folderCounter.txt") as f:
    counter = f.readline()

print("######### Actual Counter read from file: " + str(counter))
writeToTXTLog("######### Actual Counter read from file: " + str(counter))

#3. check if a folder with this counter exists, else set counter to 0
newSourceImageDirectoryPath = str(parentDirectory) + "/photo-database/" + str(counter)

print("######### newSourceImageDirectoryPath " + str(newSourceImageDirectoryPath))
writeToTXTLog("######### newSourceImageDirectoryPath " + str(newSourceImageDirectoryPath))

if os.path.isdir(str(newSourceImageDirectoryPath)): 
    print("######### counter" + "directory exists")
    writeToTXTLog("######### counter" + "directory exists")
else :
    print("######### " + str(newSourceImageDirectoryPath) + " directory does not exists")
    writeToTXTLog("######### " + str(newSourceImageDirectoryPath) + " directory does not exists") 
    counter = "0"
    newSourceImageDirectoryPath = str(parentDirectory) + "/photo-database/" + str(counter)

#4. copy images from counter folder to images folder
print("Start copy from: " + str(newSourceImageDirectoryPath))
writeToTXTLog("Start copy from: " + str(newSourceImageDirectoryPath))
src_files = os.listdir(newSourceImageDirectoryPath)
for file_name in src_files:
    full_file_name = os.path.join(newSourceImageDirectoryPath, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, targetDirectory)
       

#5. give all the new files a new filename with a counter so that the website can interpret it with hardcoded image-url
fileNameCounter = 0
target_files = os.listdir(targetDirectory)
print("######### TARGET FILES" + str(target_files)) 
writeToTXTLog("######### TARGET FILES" + str(target_files))
valid_images = [".jpg",".JPG",".HEIC",".HEIF", ".jpeg"]
for file_name in target_files:
        ## rename file to a counter
        fileExtension = os.path.splitext(file_name)[1]
        if fileExtension not in valid_images:
            continue
        print("######## rename " + file_name + " to " + str(fileNameCounter) + fileExtension)
        os.rename(str(targetDirectory) + "/" + file_name, str(targetDirectory) + "/" + str(fileNameCounter) + ".JPG")
        fileNameCounter = fileNameCounter + 1

#6. increment counter and write counter to folderCounter.txt
counter = int(counter) + 1
with open(parentDirectory + "/scripts/" + "folderCounter.txt", "w") as f:
    f.write(str(counter))

writeToTXTLog("######### END ###############")
print("######### END ###############")

########## SECOND PART: WRITE EXIFS OF IMAGES IN TXT FILE
# TODO extract exifs and combine it to two strings 
# year
# country
# image exif data
# custom tag analog/digital

