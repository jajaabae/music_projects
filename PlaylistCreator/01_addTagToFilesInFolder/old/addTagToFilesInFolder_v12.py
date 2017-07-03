import os

writeFilenames=1
theNewTag='MDj'
#musicDir='/storage/sdcard1/music'
path = 'storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator/musicForTagging/jive'
os.chdir(path)

theAlowedFileExtention='mp3'
allFileExtentionsAlowed=0

start='_{'
stop='}_'


##general functions
printing=1 #Print in finished program
def p(val): 
    if printing == 1:
        print val
testprint = 0 #Print for testing 
def pt(val) :
    if testprint == 1:
        print val
progressprint = 1 #Print for progress while programming
def pp(val) :
    if progressprint == 1:
        print val
printbar = 1 #Print a bar to show where I am working
def pb() :
    if printbar == 1:
        print '###################'
printlimitations = 1 #Print limitations in the code/methods
def pl(val) :
    if printlimitations == 1:
        print 'Limitation: '+str(val)





def okTag():
    p('OK tag')

def badTag():
    p('Bad tag')

def noTag():
    p('No tag')


#def testing(theFile):
#    pl('######### Testing! ######### ')
#    #splitTagIfOkTagSetup(theFile)
#    newTag='HeNCaKr'
#    addTagToFileName(theFile, newTag)

def testing(theFile,newTag):
    pl('######### Testing! ######### ')
    pb()
    addTagToFileName(theFile, newTag)

def initializeTag(theFile):
    pp('Init. tag')
    pp('old filename: '+theFile)
    newFilename=start+stop+theFile
    pp('new filename: '+newFilename)
    hasExtention = '.' in theFile
    if hasExtention:
       pt('has extention')
       a=allFileExtentionsAlowed==1
       pt(theFile)
       #pb()
       #pb()
       tmp=theFile.split('.')
       length = len(tmp)
       #p(tmp[length-1])
       b=tmp[length-1]==theAlowedFileExtention
       #p(length)
       #p(b)
       #pb()
       if a or b:
           pt('Alowed file extention')
           if writeFilenames==1:
               p('Renamed')
               os.rename(theFile,newFilename)
        
def splitTagIfOkTagSetup( theFile ):
    p(theFile)
    a= not (start in theFile)
    b= not (stop in theFile)
    if a&b:
        initializeTag(theFile)
    tag = theFile.split(start)
    if (start in theFile) & (stop in theFile):
        pt('step2')
        e=len(tag)==2
        a=(stop not in tag[0])
        b=(stop in tag[1])
        c=(start not in tag[0])
        d=(start not in tag[1])
        if e&a&b&c&d:
            pt('step3')
            tag=[tag[0]]+tag[1].split(stop)
            #pt(tag)
            a=not (start in tag[0]+tag[1]+tag[2])
            b=not (stop in tag[0]+tag[1]+tag[2])
            c=len(tag)==3
            if a&b&c:
                okTag()
                return tag
            else:
                badTag()
        else:
            badTag()
    elif (start in theFile) or (stop in theFile) :
        badTag()
    else:
        noTag()
    pt('bad tag: '+str(tag))
    return ['bad']
           

    
def addTagToFileName(fileName, newTag):
    separatedFilename = splitTagIfOkTagSetup(fileName)
    if len( separatedFilename )==3:
        changeFilename( fileName, newTag, separatedFilename )
    else:
        pt('bad')
        
    
def changeFilename( fileName, newTag, separatedFilename ):
    p('new tag: '+newTag)
    #p('old filename: '+fileName)
    s=separatedFilename
    if not (newTag in s[1]):
       newFilename = s[0]+start+s[1]+newTag+stop+s[2]
       p('newFilename: '+newFilename)
       if writeFilenames==1:
          pl('not compleated')
          os.rename(fileName,newFilename)
       else:
          p(' writeFilenames is turned off ')
    else:
        p('!!Allready contains tag')
    
def forAllFiles(newTag):
    pl('not implemented')
    items=os.listdir(os.getcwd())
    for item in items:
        if os.path.isfile(item):
            theFile=item
            pb()
            addTagToFileName(theFile, newTag)
    
       
def runTests():
    newTag='HeNCaKr'
    theFile='gfuijg_{FMCiDz}_ghkhfgj.mp3'
    testing(theFile,newTag)
    theFile='gfuijgFMCiDz}_ghkhfgj.mp3'
    testing(theFile,newTag )
    theFile='gfuijg_{FMCiDzghkhfgj.mp3'
    testing(theFile,newTag )
    theFile='gfuijgFMCiDzghkhfgj.mp3'
    testing(theFile,newTag )
    theFile='gfuijg_{FMCiDz}_ghk}_hfgj.mp3'
    testing(theFile,newTag )


#runTests()
forAllFiles(theNewTag)