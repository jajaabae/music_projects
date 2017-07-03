import os

#Generate playlistfiles from TagSystem.txt (ignore "#"-lines)
path='storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator'
path='storage/sdcard0/'
path = 'storage/sdcard0/com.hipipal.qpyplus/scripts/PyIOFolder'
path = 'storage/sdcard0/com.hipipal.qpyplus/scripts/PlaylistCreator'

os.chdir(path)
print os.listdir(os.getcwd())

f=open('TagSystem.txt','r')
for line in f:
    line =str(line.strip())
    if len(line)>0:
        if not line[0]=='#':
            print '-------------'
            print bool(str(line[0:10])=='TagStart: ')
            print (len(line)>10 & bool(str(line[0:10])=='TagStart: '))
            print 1<0 & 2>1
            a= (len(line)>10)
            b= (bool(str(line[0:10])=='TagStart: '))
            c= (len(line)>10 & bool(str(line[0:10])=='TagStart: '))
            d= ( (len(line)>10) & (bool(str(line[0:10])=='TagStart: ')) )
            print 'a'
            print a
            print 'b'
            print b
            print 'c'
            print c
            print 'd'
            print d
            print '-------------'
            
            if ( (len(line)>10) & bool(str(line[0:10])=='TagStart: ')):
                print 'arrr: '+line[0:10]
            elif len(line)>9 & bool(str(line[0:10])=='TagStop: '):
                print 'b: '+line[0:9]
            print 'l: '+line
f.close()

 #For files all dirs:
 	#for tag in TagSystem.txt (ignore "#"-lines): #for playlistfiles: 
 		#if filename contains tag (chase spesific): #If tag corresponds with playlistfile.tag:
					#Add filename and relative(/or full) dir
					
					