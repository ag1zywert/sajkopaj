from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np 
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  
import sys  


_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)


expName = 'FIRST ONE' 
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit() 
expInfo['date'] = data.getDateStr() 
expInfo['expName'] = expName


filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])


thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  

endExpNow = False  

# Jak wygląda okno, które się wyświetla
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)

expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0 

# To jest pierwszy "routine" i są to instrukcje, wyświetlają się na samym początku
instrukcjeClock = core.Clock()
intrukcjetekstowe = visual.TextStim(win=win, name='intrukcjetekstowe',
    text=u'Pami\u0119taj!\nWybierasz kolor liter, olewasz s\u0142owa.\n\nlewa strza\u0142ka - czerwony\ndolna strza\u0142ka - zielony\nprawa strza\u0142ka - niebieski',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
# To jest routine o nazwie trial i jest tu target, czyli to co nas obchodzi w stroopie 
# trial ma w sb 6 zmiennych, zapętlone to jest 5 razy
# isntrukcjewtrakcie to ten sam tekst co intrukcje wyświetla się w prawym górnym rogu
# pokazuje jakie szczałki som od czego

trialClock = core.Clock()
target = visual.TextStim(win=win, name='target',
    text='default text',
    font=u'Times New Roman',
    pos=(0, 0), height=0.7, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);
instrukcjewtrakcie = visual.TextStim(win=win, name='instrukcjewtrakcie',
    text=u'\nlewa strza\u0142ka - czerwony\ndolna strza\u0142ka - zielony\nprawa strza\u0142ka - niebieski',
    font=u'Arial',
    pos=(0.5, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0);


globalClock = core.Clock() 
routineTimer = core.CountdownTimer()  

#tu się zaczynają instrukcje
t = 0
instrukcjeClock.reset()  
frameN = -1
continueRoutine = True

key_resp_2 = event.BuilderKeyResponse()

instrukcjeComponents = [intrukcjetekstowe, key_resp_2]
for thisComponent in instrukcjeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

while continueRoutine:
   
    t = instrukcjeClock.getTime()
    frameN = frameN + 1 

    if t >= 0.0 and intrukcjetekstowe.status == NOT_STARTED:
       
        intrukcjetekstowe.tStart = t
        intrukcjetekstowe.frameNStart = frameN  # exact frame index
        intrukcjetekstowe.setAutoDraw(True)
    
   
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN 
        key_resp_2.status = STARTED
       
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
      
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  
            continueRoutine = False
    
  
    if not continueRoutine: 
        break
    continueRoutine = False 
    for thisComponent in instrukcjeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break 
   # jak chcesz wyjść to wciśnij escape i chuj
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
# odświeżanie
    if continueRoutine:  
        win.flip()


for thisComponent in instrukcjeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

routineTimer.reset()


trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('warunki.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials) 
thisTrial = trials.trialList[0]  

if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
   
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
   #tu się zaczyna stroop
    t = 0
    trialClock.reset()  
    frameN = -1
    continueRoutine = True
    
    target.setColor(color, colorSpace='rgb')
    target.setText(word)
    response = event.BuilderKeyResponse()

    trialComponents = [target, response, instrukcjewtrakcie]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
  
    while continueRoutine:
      
        t = trialClock.getTime()
        frameN = frameN + 1 
        if t >= 0.5 and target.status == NOT_STARTED:
         
            target.tStart = t
            target.frameNStart = frameN 
            target.setAutoDraw(True)
        frameRemains = 0.5 + 4- win.monitorFramePeriod * 0.75  
        if target.status == STARTED and t >= frameRemains:
            target.setAutoDraw(False)
        
       
        if t >= 0.5 and response.status == NOT_STARTED:
           
            response.tStart = t
            response.frameNStart = frameN  
            response.status = STARTED
          
            win.callOnFlip(response.clock.reset) 
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', 'down'])
            
          
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  
                response.keys = theseKeys[-1] 
                response.rt = response.clock.getTime()
             
                if (response.keys == str(odpowiedz)) or (response.keys == odpowiedz):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
      
        if t >= 0.0 and instrukcjewtrakcie.status == NOT_STARTED:
          
            instrukcjewtrakcie.tStart = t
            instrukcjewtrakcie.frameNStart = frameN  
            instrukcjewtrakcie.setAutoDraw(True)
        
     
        if not continueRoutine: 
        break
        continueRoutine = False  
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  
        
      
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
       
        if continueRoutine: 
            win.flip()
    
#koniec
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]: 
        response.keys=None
       
        if str(odpowiedz).lower() == 'none':
           response.corr = 1  
        else:
           response.corr = 0
    trials.addData('response.keys',response.keys)
    trials.addData('response.corr', response.corr)
    if response.keys != None:  #to jest odpowiedz
        trials.addData('response.rt', response.rt)
   #to zapisuje odpowiedzi a przynajmniej powinno xD
    routineTimer.reset()
    thisExp.nextEntry()
    

thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()

thisExp.abort()  
win.close()
core.quit()
