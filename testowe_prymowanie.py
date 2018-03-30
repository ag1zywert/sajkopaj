#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

expName = 'untitled.py'
expInfo = {'session': '001', 'participant': ''}
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


win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)

expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  


trialClock = core.Clock()
negatywne_prymowanie = visual.TextStim(win=win, name='negatywne_prymowanie',
    text='default text',
    font=u'Calibri',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color=u'blue', colorSpace='rgb', opacity=1,
    depth=0.0);


odpowiedzClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'Witaj,\njak si\u0119 dzisiaj czujesz?\n\nDobrze - wci\u015bnij strza\u0142ke w g\xf3r\u0119\n\u0179le - wci\u015bnij strza\u0142k\u0119 w d\xf3\u0142\nSam nie wiem- wci\u015bnij strza\u0142k\u0119 w lewo\nA co ci\u0119 to? - wci\u015bnij strza\u0142k\u0119 w prawo',
    font=u'Calibri',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);


globalClock = core.Clock()  
routineTimer = core.CountdownTimer()  


trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'warunkidoprymowania.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  #to zapętla
thisTrial = trials.trialList[0] 

if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
   
    t = 0
    trialClock.reset() 
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.100000)
  
    negatywne_prymowanie.setText(word)
    
    trialComponents = [negatywne_prymowanie]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #to rozpoczyna tę pętle
    while continueRoutine and routineTimer.getTime() > 0:
       
        t = trialClock.getTime()
        frameN = frameN + 1  
        
        # *negatywne_prymowanie*
        if t >= 0.0 and negatywne_prymowanie.status == NOT_STARTED:
            
            negatywne_prymowanie.tStart = t
            negatywne_prymowanie.frameNStart = frameN 
            negatywne_prymowanie.setAutoDraw(True)
        frameRemains = 0.0 + 0.1- win.monitorFramePeriod * 0.75 
        if negatywne_prymowanie.status == STARTED and t >= frameRemains:
            negatywne_prymowanie.setAutoDraw(False)
        
       
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
    
   
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
#to jest powtórzone 2 razy



trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'keyrespdoprymowania.xlsx'), #to jest po to, żeby potem można zebrać dane co oznacza jakiś przycisk?
    seed=None, name='trials_2')
thisExp.addLoop(trials_2) 
thisTrial_2 = trials_2.trialList[0]  

if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
  
    t = 0
    odpowiedzClock.reset() 
    frameN = -1
    continueRoutine = True
    
    key_resp_2 = event.BuilderKeyResponse()
    
    odpowiedzComponents = [text, key_resp_2]
    for thisComponent in odpowiedzComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #tu jest 'odpowiedz' czyli pytanie o nastroj i mozliwa odpowiedz od ziomka co wyplenia w postaci 'keybord'
    while continueRoutine:
       
        t = odpowiedzClock.getTime()
        frameN = frameN + 1  
        
        if t >= 0.0 and text.status == NOT_STARTED:
            
            text.tStart = t
            text.frameNStart = frameN  
            text.setAutoDraw(True)
        
        # *key_resp_2* 
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
           
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  
            key_resp_2.status = STARTED
            
            win.callOnFlip(key_resp_2.clock.reset)  
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['up', 'down', 'left', 'right'])
            
          
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # trzeba wciśnij przynajmniej 1 z podanych przycisków
                key_resp_2.keys = theseKeys[-1]  
                key_resp_2.rt = key_resp_2.clock.getTime()
                #odpowiedz, w sensie klikniecie danego przycisku konczy ten routine
                continueRoutine = False
        
       
        if not continueRoutine:  
            break
        continueRoutine = False 
        for thisComponent in odpowiedzComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  
                
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        if continueRoutine:  
            win.flip()
    
    
    for thisComponent in odpowiedzComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
   
    if key_resp_2.keys in ['', [], None]:  #to jest wersja, ze ktos w ogole nie odpowiedzial
        key_resp_2.keys=None
    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  #tu jest odpowiedz chyba, ktora mozna zapisac
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    
    routineTimer.reset()
    thisExp.nextEntry()
    


#TO POWINNO ZAPISYWAĆ ODPOWIEDZI
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()

thisExp.abort() 
win.close()
core.quit()
