
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

# to nie wiem czy się przyda, ale w badaniach by się przydało
zbiera dane o ludziach 
expName = 'stroop_feedback'  
expInfo = {'session': '01', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  
expInfo['date'] = data.getDateStr() 
expInfo['expName'] = expName


filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])


thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  

endExpNow = False  


# wygląd okna, można sb zmienić rozdzielczość, as u wish

win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')


expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0   #chyba?

# To są dane do routin pt "Start"
#TU jest napisany wstępik co to je stroop

startClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'Za chwil\u0119 przyst\u0105pisz do udzia\u0142u w tzw. te\u015bcie Stroopa!\n\nTest Ridleya Stroopa s\u0142u\u017cy do mierzenia funkcji poznawczych cz\u0142owieka, koncentracji i podzielno\u015bci uwagi.\n\nTwoim zadaniem b\u0119dzie okre\u015blenie koloru czcionki, kt\xf3r\u0105 zapisane jest s\u0142owo.\nJak b\u0119dziesz gotowy/a wci\u015bnij dowolny przycisk, aby zobaczy\u0107 intrukcje.',
    font='Times New Roman',
    pos=(0, -0.2), height=0.08, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1,
    depth=0.0);
image = visual.ImageStim(
    win=win, name='image',
    image='logokierunku.jpg', mask=None,
    ori=0, pos=(0, 0.7), size=(0.8, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# To są dane do instrukcji
#przed próbą
instructPracticeClock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text=u'Okej, no to najpierw ma\u0142a pr\xf3ba.\n\nWybierasz kolor liter, olewasz s\u0142owa.\n\nlewa strza\u0142ka - czerwony\ndolna strza\u0142ka - zielony\nprawa strza\u0142ka - niebieski\n\nNaci\u015bnij dowolony przycisk aby rozpocz\u0105\u0107',
    font='Times New Roman',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1,
    depth=0.0);

# A tu jest zadanie właściwe

trialClock = core.Clock()
word = visual.TextStim(win=win, name='word',
    text='default text',
    font='Times New Roman',
    pos=[0, 0], height=0.35, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text=u'\n\nlewa strza\u0142ka - czerwony\ndolna strza\u0142ka - zielony\nprawa strza\u0142ka - niebieski\n\n',
    font='Arial',
    pos=(0.5, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Dane to feedbacku który jest po kazdym trialu
feedbackClock = core.Clock()
msg=''
feedback_2 = visual.TextStim(win=win, name='feedback_2',
    text='default text',
    font='Times New Roman',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Intrukcje 2 - te są przed właściwym zadaniem

instructClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text=u'Ok, teraz zaczynamy naprawd\u0119,\npami\u0119taj:\n\nlewa strza\u0142ka - czerwony\ndolna strza\u0142ka - zielony\nprawa strza\u0142ka - niebieski\n\nNaci\u015bnij dowolony przycisk aby rozpocz\u0105\u0107\n',
    font='Times New Roman',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0);

#zadanie
trialClock = core.Clock()
word = visual.TextStim(win=win, name='word',
    text='default text',
    font='Times New Roman',
    pos=[0, 0], height=0.35, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text=u'\n\nlewa strza\u0142ka - czerwony\ndolna strza\u0142ka - zielony\nprawa strza\u0142ka - niebieski\n\n',
    font='Arial',
    pos=(0.5, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1,
    depth=-2.0);

#feedback
feedbackClock = core.Clock()
msg=''
feedback_2 = visual.TextStim(win=win, name='feedback_2',
    text='default text',
    font='Times New Roman',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1,
    depth=-1.0);

# dane to ostatniego "slajdu"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text=u'Ok, to ju\u017c koniec,\ndzi\u0119ki za udzia\u0142 w eksperymencie :)\n\n\nNaci\u015bnij esc aby wyj\u015b\u0107\n',
    font='Times New Roman',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1,
    depth=0.0);

globalClock = core.Clock()  
routineTimer = core.CountdownTimer()  



t = 0
startClock.reset()  
frameN = -1
continueRoutine = True

key_resp_2 = event.BuilderKeyResponse()

startComponents = [text, image, key_resp_2]
for thisComponent in startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#tu się zaczyna wszystko

while continueRoutine:
    
    t = startClock.getTime()
    frameN = frameN + 1 
    
    
    if t >= 0.0 and text.status == NOT_STARTED:
    
        text.tStart = t
        text.frameNStart = frameN 
        text.setAutoDraw(True)
    
   
    if t >= 0.0 and image.status == NOT_STARTED:
      
        image.tStart = t
        image.frameNStart = frameN  
        image.setAutoDraw(True)
    
    # *key_resp_2*
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructPractice"-------
t = 0
instructPracticeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ready1 = event.BuilderKeyResponse()
# keep track of which components have finished
instructPracticeComponents = [instr1, ready1]
for thisComponent in instructPracticeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructPractice"-------
while continueRoutine:
    # get current time
    t = instructPracticeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if t >= 0.0 and instr1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr1.tStart = t
        instr1.frameNStart = frameN  # exact frame index
        instr1.setAutoDraw(True)
    
    # *ready1* updates
    if t >= 0.0 and ready1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready1.tStart = t
        ready1.frameNStart = frameN  # exact frame index
        ready1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready1.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructPractice"-------
for thisComponent in instructPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.xlsx'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    word.setColor(letterColor, colorSpace='rgb')
    word.setText(text)
    resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [word, resp, text_2]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word* updates
        if t >= 0.5 and word.status == NOT_STARTED:
            # keep track of start time/frame for later
            word.tStart = t
            word.frameNStart = frameN  # exact frame index
            word.setAutoDraw(True)
        
        # *resp* updates
        if t >= 0.5 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'down', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1  # correct non-response
        else:
           resp.corr = 0  # failed to respond (incorrectly)
    # store data for practice (TrialHandler)
    practice.addData('resp.keys',resp.keys)
    practice.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        practice.addData('resp.rt', resp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if resp.corr:#stored on last run routine
      msg="Dobrze! czas reakcji=%.3f" %(resp.rt)
    else:
      msg="Ups, zla odpowiedz"
    feedback_2.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedback_2]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedback_2* updates
        if t >= 0.0 and feedback_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_2.tStart = t
            feedback_2.frameNStart = frameN  # exact frame index
            feedback_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback_2.status == STARTED and t >= frameRemains:
            feedback_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practice'

# get names of stimulus parameters
if practice.trialList in ([], [None], None):
    params = []
else:
    params = practice.trialList[0].keys()
# save data for this loop
practice.saveAsExcel(filename + '.xlsx', sheetName='practice',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instruct"-------
t = 0
instructClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ready = event.BuilderKeyResponse()
# keep track of which components have finished
instructComponents = [instrText, ready]
for thisComponent in instructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruct"-------
while continueRoutine:
    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if t >= 0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    
    # *ready* updates
    if t >= 0 and ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready.tStart = t
        ready.frameNStart = frameN  # exact frame index
        ready.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    word.setColor(letterColor, colorSpace='rgb')
    word.setText(text)
    resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [word, resp, text_2]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word* updates
        if t >= 0.5 and word.status == NOT_STARTED:
            # keep track of start time/frame for later
            word.tStart = t
            word.frameNStart = frameN  # exact frame index
            word.setAutoDraw(True)
        
        # *resp* updates
        if t >= 0.5 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'down', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1  # correct non-response
        else:
           resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if resp.corr:#stored on last run routine
      msg="Dobrze! czas reakcji=%.3f" %(resp.rt)
    else:
      msg="Ups, zla odpowiedz"
    feedback_2.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedback_2]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedback_2* updates
        if t >= 0.0 and feedback_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_2.tStart = t
            feedback_2.frameNStart = frameN  # exact frame index
            feedback_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback_2.status == STARTED and t >= frameRemains:
            feedback_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if t >= 0.0 and thanksText.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText.tStart = t
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
