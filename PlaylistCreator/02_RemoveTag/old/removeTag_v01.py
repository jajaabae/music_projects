#
PSEUDOCODE:

remTag='...'
if ok filename and contains remTag:
    tmp = filename
    tmp = tmp.split(start)
    tmp = tmp.split(stop)
    #len(tmp)==3
    newTag=tmp[1].split(remTag)
    newTag=newTag[0]+newTag[1]
    newFileName=tmp[0]+start+newTag+stop+tmp[2]
    