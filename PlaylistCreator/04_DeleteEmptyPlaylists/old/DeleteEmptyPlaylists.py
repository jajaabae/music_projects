import os

os.chdir('/storage/sdcard0/com.hipipal.qpyplus')

def deleteEmptyPlaylists():
    
    direc = os.getcwd()
    files = os.listdir(direc)
    print files
    for file in files:
        if os.path.isfile(file):
            #If "one line long"
                #if #EXIFM3U? in line1
                    print file
                    #print length of file
                    #os.delete(file)
deleteEmptyPlaylists()