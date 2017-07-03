import os
start='__{' #initialize (not suposed to be used!!!)
stop='}__' #initialize (not suposed to be used!!!)
spc=', ' #initialize (not suposed to be used!!!)
playlistContainsPathsForFiles=0

excludeTag='Ex'

##general functions
printing=0 #Print in finished program
def p(val): 
    if printing == 1:
        print val
testprint = 0 #Print for testing 
def pt(val) :
    if testprint == 1:
        print val
progressprint = 0 #Print for progress while programming
def pp(val) :
    if progressprint == 1:
        print val
printbar = 0 #Print a bar to show where I am working
def pb() :
    if printbar == 1:
        print '###################'
printlimitations = 0 #Print limitations in the code/methods
def pl(val) :
    if printlimitations == 1:
        print 'Limitation: '+str(val)
        

#Generate playlistfiles from TagSystem.txt (ignore "#"-lines), but get startOfTag and EndOfTag.
def firstTask():
    q = os.getcwd()
    print q
    print os.listdir(q)
    global start
    global stop
    playlistNames = []
    f=open('TagSystem.txt','r')
    for line in f:
        line =str(line.strip())
        if len(line)>0:
            if not line[0]=='#':
                #print '-------------'
                if ( (len(line)>10) & bool(str(line[0:10])=='TagStart: ')):
                    #print 'a: '+line[0:10]
                    start = line[10:len(line)]
                elif (len(line)>9) & bool(str(line[0:9])=='TagStop: '):
                    #print 'b: '+line[0:9]
                    stop = line[9:len(line)]
                else:
                    parts = line.split("\t")
                    if len(parts)>1:
                        #print parts[1]+': ('+parts[0]+')'
                        name= parts[0]+' '+parts[1]+'.m3u'
                        playlistNames = playlistNames+[name]
                        pp( name)
    f.close()
    p( '#tags in: '+start+' '+stop)
    p( 'Playlists:')
    p(playlistNames)
    
    # generate playlistfiles in "playlists"-folder from "playlistNames"
    newFolder= 'playlists'
    if not os.path.isdir(newFolder):
        os.mkdir(newFolder)
    os.chdir(newFolder)
    playlistDir=os.getcwd()
    
    for name in playlistNames:
##        pb()
        pt(os.getcwd())
        pt('--'+name)
##        pt(os.listdir(os.getcwd()))
        f=open(name, 'w')
        f.write('#EXTM3U\n')
        f.close()
##        pb()
        
    pb()





    
#getTagsFromMusicFile
def getTags(filename):
    pp( 'getTags()')
    tag=''
    if start in filename:
        tag = filename.split(start)
        pl('DANGER! Check for good tag?')
        tag = tag[1].split(stop)[0]
        #print tag
    return [tag]


#Get all playlist tags
def REDUNDANTgetAllPlaylistTags():
    AllTags=[]
    pp('getAllPlaylistTags() ')
    #! assumes playlist dir.
    filesAndFoldes=os.listdir(os.getcwd())
    #print filesAndFoldes
    for item in filesAndFoldes:
        if os.path.isfile(item):
            #print 'file: '+str(item)
            tag=item.split()
            tag=tag[0]
            AllTags = AllTags+[tag]
            #print tag
    #print AllTags
    pp('##Should return tag-array and playlistName-array')
    return AllTags


#Get all playlists with/for this tag
def getAllPlaylistWithTheseTags(mTags):
    AllPlaylistsWithTags=[]
    pp( 'MESSY, NOT OPTIMAL: getAllPlaylistWithThisTag(mTag): ')
    pp( '## Shoult take list of playlists and their tags')
    #! assumes playlist dir.
    filesAndFoldes=os.listdir(os.getcwd())
    for item in filesAndFoldes:
        if os.path.isfile(item):
            tag = getTagFromPlaylistFile(item)
            #tag=item.split()
            #tag=tag[0]
            pp( item)
            if tag in mTags:
                if excludeTag not in mTags:
                    AllPlaylistsWithTags= AllPlaylistsWithTags+[str(item)]
                    #print mTags+spc+tag+spc+item
    pp( 'NOT OPTIMAL END')
    return AllPlaylistsWithTags

    
#getTagFromPlaylistFile
def getTagFromPlaylistFile(playlistFile):
##    pp( 'Compleated: getTagFromPlaylistFile ')
    tag=playlistFile.split()
    tag=tag[0]
    return tag    
    
#add to playlistfile
def addToPlaylistfile(path,fileName,playlist):
    pl('Assumes playlist dir')
    pb()
    pp( 'Not compleated: addToPlaylistfile ')
    pt(path)
    pt(fileName)
    pt(playlist)
    f=open(playlist,'a')
    pathAndFile = path+'/'+fileName
    pt(pathAndFile)
    if playlistContainsPathsForFiles==1:
        output= pathAndFile+'\n'
    else:
        output= fileName+'\n'
    print '###################################################'
    print fileName
    print playlist
    f.write(output)
    #f.write(pathAndFile+'\n')
    f.close()
    pb()
    
    
#what to do for each music file
def handleMusicFile( fileName,path,fileInPath ):
    p( '-----------------')
    p( fileName)
    p( path)
    #getTagsFromMusicFile
    musicFilesTags = getTags(fileName)
    #for tags in filename
    for mTags in musicFilesTags:
        #get all playlists for tag
        playlists = getAllPlaylistWithTheseTags(mTags)
        p( '-----------------')
        p( '-----------------')
        p(musicFilesTags)
        p( playlists)
        p( '-----------------')
        p( '-----------------')
        p( '-----------------')
        for eachPlaylist in playlists:
            addToPlaylistfile(path,fileName,eachPlaylist)
    
    ##getTaglist
    #AllTags = getAllPlaylistTags()
    #print AllTags
        ##for tag in TagSystem.txt (ignore "#"-lines): for playlistfiles: 
        ##if filename contains tag (chase spesific): #If tag corresponds with playlistfile.tag:
            ##Add filename and relative(/or full) dir
    #print '-----------------'
    
					
					
					
#digg all files in all dirs (recursive)
def recDigger(path, leadZ):
    print path
    liste=[]
    maxDepth = 100
    try:
        liste=os.listdir(path)
        print liste
    except:
        pass
    for d in liste:
        dpath= (path+'/'+d)
        if os.path.isdir(dpath):
            #if leadZ<maxDepth & len(liste)>0:
            if len(liste)>0:
                space = ( ('%'+str('%02d' % leadZ)+'d') % 0)
##                print dpath
                p= (path+'/'+d)
                l= (leadZ+1)
                recDigger(p,l)
            #else:
            #    print "end"
        elif os.path.isfile(dpath):
            #print d
            #print dpath
            #----------------
            #methods for each song
            handleMusicFile(d,path,dpath)
            #----------------

def runProg(mDir):
    firstTask()
    p('-- Program: Directory Digger --')
    musicDir=mDir
    #musicDir='/storage/sdcard1/music'
    recDigger(musicDir, 1)