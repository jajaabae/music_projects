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
    pl('testing!')
    fileHasOkTagSetup(theFile)
    if (start in theFile) & (stop in theFile):
        okTag
    elif start or stop:
        badTag()
    else:
        noTag()
        
def fileHasOkTagSetup( theFile ):
    pl('not implemented')
    
           

    
def tmp():
    pl('not implemented')
    
def tmp():
    pl('not implemented')
    
def tmp():
    pl('not implemented')
       

theFile='gfuijg_{FMCiDz}_ghkhfgj.mp3'
testing(theFile)