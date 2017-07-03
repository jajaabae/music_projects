import os

#Generate playlistfiles from TagSystem.txt (ignore "#"-lines), but get startOfTag and EndOfTag.
path = 'storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator'
start='__{'
stop='}__'

os.chdir(path)
#print os.listdir(os.getcwd())

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
                    print parts[1]+': ('+parts[0]+')'
f.close()
print '#tags in: '+start+' '+stop

 #For files all dirs:
 	#for tag in TagSystem.txt (ignore "#"-lines): for playlistfiles: 
 		#if filename contains tag (chase spesific): #If tag corresponds with playlistfile.tag:
					#Add filename and relative(/or full) dir
					
					