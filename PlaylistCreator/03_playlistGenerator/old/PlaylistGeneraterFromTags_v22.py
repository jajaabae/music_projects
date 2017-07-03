import os

#Generate playlistfiles from TagSystem.txt (ignore "#"-lines), but get startOfTag and EndOfTag.
path = 'storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator'
start='__{'
stop='}__'

os.chdir(path)
#print os.listdir(os.getcwd())

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
                    print name
f.close()
print '#tags in: '+start+' '+stop
print playlistNames

# generate playlistfiles in "playlists"-folder from "playlistNames"
newFolder= 'playlists'
if not os.path.isdir(newFolder):
    os.mkdir(newFolder)
os.chdir(newFolder)
playlistDir=os.getcwd()

for name in playlistNames:
    f=open(name, 'w')
    f.write('#EXTM3U\n')
    f.close()





    
#getTagsFromMusicFile
def getTags(path, filename):
    print 'Not implemented: getTags()'
    
#Get all playlist tags
def getAllPlaylistTags():
    print 'Not implemented: getAllPlaylistTags() '
    
#getTagFromPlaylistFile
def getTagFromPlaylistFile(playlistFile):
    print 'Not implemented: getTagFromPlaylistFile '
    
#add to playlistfile
def addToPlaylistfile():
    print 'Not implemented: addToPlaylistfile '
    
    
#what to do for each music file
def handleMusicFile( fileName,path,fileInPath ):
    print '-----------------'
    print fileName
    print path
    
    #for tag in TagSystem.txt (ignore "#"-lines): for playlistfiles: 
    
        #if filename contains tag (chase spesific): #If tag corresponds with playlistfile.tag:
            #Add filename and relative(/or full) dir
    #print '-----------------'
    
					
#all files, all dirs
def recDigger(path, leadZ):
    liste=[]
    maxDepth = 100
    try:
        liste=os.listdir(path)
    except:
        pass
    for d in liste:
        dpath= (path+'/'+d)
        if os.path.isdir(dpath):
            #if leadZ<maxDepth & len(liste)>0:
            if len(liste)>0:
                space = ( ('%'+str('%02d' % leadZ)+'d') % 0)
                #print dpath
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
print '-- Program: Digger --'
#musicDir='/storage'
#musicDir='/storage/sdcard1'
musicDir='/storage/sdcard1/music'
recDigger(musicDir, 1)

