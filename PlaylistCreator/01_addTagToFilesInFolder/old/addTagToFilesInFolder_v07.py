import os



start='_{'
stop='}_'


##general functions
printing=1 #Print in finished program
def p(val): 
    if printing == 1:
        print val
testprint = 1 #Print for testing 
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


def testing(theFile):
    pl('######### Testing! ######### ')
    fileHasOkTagSetup(theFile)

        
def fileHasOkTagSetup( theFile ):
    pl('not implemented')
    if (start in theFile) & (stop in theFile):
        tag = theFile.split(start)
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
    return ['bad']
           

    
def tmp():
    pl('not implemented')
    
def tmp():
    pl('not implemented')
    
def tmp():
    pl('not implemented')
       


theFile='gfuijg_{FMCiDz}_ghkhfgj.mp3'
testing(theFile)
theFile='gfuijgFMCiDz}_ghkhfgj.mp3'
testing(theFile)
theFile='gfuijg_{FMCiDzghkhfgj.mp3'
testing(theFile)
theFile='gfuijgFMCiDzghkhfgj.mp3'
testing(theFile)
theFile='gfuijg_{FMCiDz}_ghk}_hfgj.mp3'
testing(theFile)