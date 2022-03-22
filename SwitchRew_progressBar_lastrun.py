#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.1),
    on Tue Mar 22 11:13:32 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.1'
expName = 'SwitchRew_progressBar'  # from the Builder filename that created this script
expInfo = {'MTurk_workerID': '', 'participant': '', 'gender': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jing/Google Drive/Switch_Bar/SwitchRew_progressBar_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 960], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "instructions1"
instructions1Clock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text='Move to the center dot\nWait till it turns to a square\nand move to your target\n\n\nClick to continue...',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instrMouse = event.Mouse(win=win)
x, y = [None, None]
instrMouse.mouseClock = core.Clock()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instruction_2 = visual.TextStim(win=win, name='instruction_2',
    text='Few practice trials first\nClick to Start...',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instrMouse_2 = event.Mouse(win=win)
x, y = [None, None]
instrMouse_2.mouseClock = core.Clock()

# Initialize components for Routine "Initialization"
InitializationClock = core.Clock()
Total_Ntrials = 750;
ITI_sec = 0.17
Nport = 6
targetDist = 0.33
stim_size = 0.1
minTargetDis = 0.05
maxWait_sec = 5.0

fixDuration = 0.5
Counter_TimeOut = 0
Counter_Complete = 0
Counter_Correct = 0
Counter_Error = 0
minNcorrect = 3;
maxNtrial_after = 7;
msg=""
progress_msg="0%"
codemsg = ""
feedbackOp = 1;
NewBlock= True
Ncorrect=0
Correct=0
SWITCH = 0
Ntrial_switch = 0
Nblock =0
reward_rate = 0
BarLength = 0
BarCenter = 0.1
perc_finish = 0;

Durations = np.arange(0.4, 0.5, .01)#np.arange(.25, 1.75, .01)
Ports = np.arange(Nport)
ID_port = np.random.randint(Nport)

ChoiceAngles = [p*2*pi/Nport for p in Ports]
xPos = [targetDist*np.cos(c) for c in ChoiceAngles]
yPos = [targetDist*np.sin(c) for c in ChoiceAngles]
start_session = visual.ShapeStim(
    win=win, name='start_session', vertices='cross',
    size=[1.0, 1.0],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=0, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_fix"
trial_fixClock = core.Clock()
Center = visual.ShapeStim(
    win=win, name='Center', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-1.0, interpolate=True)
Choice0 = visual.ShapeStim(
    win=win, name='Choice0', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
Choice1 = visual.ShapeStim(
    win=win, name='Choice1', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
Choice2 = visual.ShapeStim(
    win=win, name='Choice2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-4.0, interpolate=True)
Choice3 = visual.ShapeStim(
    win=win, name='Choice3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-5.0, interpolate=True)
Choice4 = visual.ShapeStim(
    win=win, name='Choice4', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-6.0, interpolate=True)
Choice5 = visual.ShapeStim(
    win=win, name='Choice5', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-7.0, interpolate=True)
mouse1 = event.Mouse(win=win)
x, y = [None, None]
mouse1.mouseClock = core.Clock()
progressBar_out1 = visual.Rect(
    win=win, name='progressBar_out1',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,0],
    opacity=1, depth=-9.0, interpolate=True)
progressBar_in1 = visual.Rect(
    win=win, name='progressBar_in1',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-10.0, interpolate=True)
progress_text1 = visual.TextStim(win=win, name='progress_text1',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "trial_choice"
trial_choiceClock = core.Clock()
CursorChoiceDistance=np.ones(Nport)
Choose = False
IDChoice = []
RT = np.nan
Center_2 = visual.Rect(
    win=win, name='Center_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-1.0, interpolate=True)
Choice0_2 = visual.ShapeStim(
    win=win, name='Choice0_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
Choice1_2 = visual.ShapeStim(
    win=win, name='Choice1_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
Choice2_2 = visual.ShapeStim(
    win=win, name='Choice2_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-4.0, interpolate=True)
Choice3_2 = visual.ShapeStim(
    win=win, name='Choice3_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-5.0, interpolate=True)
Choice4_2 = visual.ShapeStim(
    win=win, name='Choice4_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-6.0, interpolate=True)
Choice5_2 = visual.ShapeStim(
    win=win, name='Choice5_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-7.0, interpolate=True)
mouse2 = event.Mouse(win=win)
x, y = [None, None]
mouse2.mouseClock = core.Clock()
progressBar_out2 = visual.Rect(
    win=win, name='progressBar_out2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,0],
    opacity=1, depth=-9.0, interpolate=True)
progressBar_in2 = visual.Rect(
    win=win, name='progressBar_in2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-10.0, interpolate=True)
progress_text2 = visual.TextStim(win=win, name='progress_text2',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
Center_3 = visual.Rect(
    win=win, name='Center_3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-1.0, interpolate=True)
Choice0_3 = visual.ShapeStim(
    win=win, name='Choice0_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
Choice1_3 = visual.ShapeStim(
    win=win, name='Choice1_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
Choice2_3 = visual.ShapeStim(
    win=win, name='Choice2_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-4.0, interpolate=True)
Choice3_3 = visual.ShapeStim(
    win=win, name='Choice3_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-5.0, interpolate=True)
Choice4_3 = visual.ShapeStim(
    win=win, name='Choice4_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-6.0, interpolate=True)
Choice5_3 = visual.ShapeStim(
    win=win, name='Choice5_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-7.0, interpolate=True)
Chosen = visual.Rect(
    win=win, name='Chosen',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[0,0,0], fillColor='white',
    opacity=1.0, depth=-8.0, interpolate=True)
Message = visual.TextStim(win=win, name='Message',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-9.0);
progressBar_out3 = visual.Rect(
    win=win, name='progressBar_out3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,0],
    opacity=1, depth=-10.0, interpolate=True)
progressBar_in3 = visual.Rect(
    win=win, name='progressBar_in3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-11.0, interpolate=True)
progress_text3 = visual.TextStim(win=win, name='progress_text3',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
blank = visual.ShapeStim(
    win=win, name='blank', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=0, depth=0.0, interpolate=True)
progressBar_out4 = visual.Rect(
    win=win, name='progressBar_out4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,0],
    opacity=1, depth=-1.0, interpolate=True)
progressBar_in4 = visual.Rect(
    win=win, name='progressBar_in4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
progress_text4 = visual.TextStim(win=win, name='progress_text4',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instructions3"
instructions3Clock = core.Clock()
instruction_3 = visual.TextStim(win=win, name='instruction_3',
    text="Your goal is to gain as much 'Correct' as possible.\n\nReady? Click to Start\n\nOR press [esc] to quit, result will NOT be saved.",
    font='Arial',
    pos=(0, 0), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instrMouse_3 = event.Mouse(win=win)
x, y = [None, None]
instrMouse_3.mouseClock = core.Clock()

# Initialize components for Routine "trial_fix"
trial_fixClock = core.Clock()
Center = visual.ShapeStim(
    win=win, name='Center', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-1.0, interpolate=True)
Choice0 = visual.ShapeStim(
    win=win, name='Choice0', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
Choice1 = visual.ShapeStim(
    win=win, name='Choice1', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
Choice2 = visual.ShapeStim(
    win=win, name='Choice2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-4.0, interpolate=True)
Choice3 = visual.ShapeStim(
    win=win, name='Choice3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-5.0, interpolate=True)
Choice4 = visual.ShapeStim(
    win=win, name='Choice4', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-6.0, interpolate=True)
Choice5 = visual.ShapeStim(
    win=win, name='Choice5', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-7.0, interpolate=True)
mouse1 = event.Mouse(win=win)
x, y = [None, None]
mouse1.mouseClock = core.Clock()
progressBar_out1 = visual.Rect(
    win=win, name='progressBar_out1',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,0],
    opacity=1, depth=-9.0, interpolate=True)
progressBar_in1 = visual.Rect(
    win=win, name='progressBar_in1',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-10.0, interpolate=True)
progress_text1 = visual.TextStim(win=win, name='progress_text1',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "trial_choice"
trial_choiceClock = core.Clock()
CursorChoiceDistance=np.ones(Nport)
Choose = False
IDChoice = []
RT = np.nan
Center_2 = visual.Rect(
    win=win, name='Center_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-1.0, interpolate=True)
Choice0_2 = visual.ShapeStim(
    win=win, name='Choice0_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
Choice1_2 = visual.ShapeStim(
    win=win, name='Choice1_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
Choice2_2 = visual.ShapeStim(
    win=win, name='Choice2_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-4.0, interpolate=True)
Choice3_2 = visual.ShapeStim(
    win=win, name='Choice3_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-5.0, interpolate=True)
Choice4_2 = visual.ShapeStim(
    win=win, name='Choice4_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-6.0, interpolate=True)
Choice5_2 = visual.ShapeStim(
    win=win, name='Choice5_2', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-7.0, interpolate=True)
mouse2 = event.Mouse(win=win)
x, y = [None, None]
mouse2.mouseClock = core.Clock()
progressBar_out2 = visual.Rect(
    win=win, name='progressBar_out2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,0],
    opacity=1, depth=-9.0, interpolate=True)
progressBar_in2 = visual.Rect(
    win=win, name='progressBar_in2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-10.0, interpolate=True)
progress_text2 = visual.TextStim(win=win, name='progress_text2',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
Center_3 = visual.Rect(
    win=win, name='Center_3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-1.0, interpolate=True)
Choice0_3 = visual.ShapeStim(
    win=win, name='Choice0_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
Choice1_3 = visual.ShapeStim(
    win=win, name='Choice1_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
Choice2_3 = visual.ShapeStim(
    win=win, name='Choice2_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-4.0, interpolate=True)
Choice3_3 = visual.ShapeStim(
    win=win, name='Choice3_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-5.0, interpolate=True)
Choice4_3 = visual.ShapeStim(
    win=win, name='Choice4_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-6.0, interpolate=True)
Choice5_3 = visual.ShapeStim(
    win=win, name='Choice5_3', vertices=180,
    size=[1.0, 1.0],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-7.0, interpolate=True)
Chosen = visual.Rect(
    win=win, name='Chosen',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[0,0,0], fillColor='white',
    opacity=1.0, depth=-8.0, interpolate=True)
Message = visual.TextStim(win=win, name='Message',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-9.0);
progressBar_out3 = visual.Rect(
    win=win, name='progressBar_out3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,0],
    opacity=1, depth=-10.0, interpolate=True)
progressBar_in3 = visual.Rect(
    win=win, name='progressBar_in3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-11.0, interpolate=True)
progress_text3 = visual.TextStim(win=win, name='progress_text3',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
blank = visual.ShapeStim(
    win=win, name='blank', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=0, depth=0.0, interpolate=True)
progressBar_out4 = visual.Rect(
    win=win, name='progressBar_out4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,0],
    opacity=1, depth=-1.0, interpolate=True)
progressBar_in4 = visual.Rect(
    win=win, name='progressBar_in4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
progress_text4 = visual.TextStim(win=win, name='progress_text4',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "block_transition"
block_transitionClock = core.Clock()
savefilename = thisExp.dataFileName[:-5]

# Initialize components for Routine "end"
endClock = core.Clock()
mouse_end = event.Mouse(win=win)
x, y = [None, None]
mouse_end.mouseClock = core.Clock()
thank = visual.TextStim(win=win, name='thank',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text = visual.TextStim(win=win, name='text',
    text='Click to Save and Exit',
    font='Arial',
    pos=(0,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions1"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the instrMouse
instrMouse.x = []
instrMouse.y = []
instrMouse.leftButton = []
instrMouse.midButton = []
instrMouse.rightButton = []
instrMouse.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions1Components = [instruction, instrMouse]
for thisComponent in instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions1"-------
while continueRoutine:
    # get current time
    t = instructions1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction* updates
    if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction.frameNStart = frameN  # exact frame index
        instruction.tStart = t  # local t and not account for scr refresh
        instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        instruction.setAutoDraw(True)
    # *instrMouse* updates
    if instrMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrMouse.frameNStart = frameN  # exact frame index
        instrMouse.tStart = t  # local t and not account for scr refresh
        instrMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrMouse, 'tStartRefresh')  # time at next scr refresh
        instrMouse.status = STARTED
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if instrMouse.status == STARTED:  # only update if started and not finished!
        buttons = instrMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = instrMouse.getPos()
                instrMouse.x.append(x)
                instrMouse.y.append(y)
                buttons = instrMouse.getPressed()
                instrMouse.leftButton.append(buttons[0])
                instrMouse.midButton.append(buttons[1])
                instrMouse.rightButton.append(buttons[2])
                instrMouse.time.append(globalClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions1"-------
for thisComponent in instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('instrMouse.x', instrMouse.x)
thisExp.addData('instrMouse.y', instrMouse.y)
thisExp.addData('instrMouse.leftButton', instrMouse.leftButton)
thisExp.addData('instrMouse.midButton', instrMouse.midButton)
thisExp.addData('instrMouse.rightButton', instrMouse.rightButton)
thisExp.addData('instrMouse.time', instrMouse.time)
thisExp.nextEntry()
# the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the instrMouse_2
instrMouse_2.x = []
instrMouse_2.y = []
instrMouse_2.leftButton = []
instrMouse_2.midButton = []
instrMouse_2.rightButton = []
instrMouse_2.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions2Components = [instruction_2, instrMouse_2]
for thisComponent in instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_2* updates
    if instruction_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_2.frameNStart = frameN  # exact frame index
        instruction_2.tStart = t  # local t and not account for scr refresh
        instruction_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_2, 'tStartRefresh')  # time at next scr refresh
        instruction_2.setAutoDraw(True)
    # *instrMouse_2* updates
    if instrMouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrMouse_2.frameNStart = frameN  # exact frame index
        instrMouse_2.tStart = t  # local t and not account for scr refresh
        instrMouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrMouse_2, 'tStartRefresh')  # time at next scr refresh
        instrMouse_2.status = STARTED
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if instrMouse_2.status == STARTED:  # only update if started and not finished!
        buttons = instrMouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = instrMouse_2.getPos()
                instrMouse_2.x.append(x)
                instrMouse_2.y.append(y)
                buttons = instrMouse_2.getPressed()
                instrMouse_2.leftButton.append(buttons[0])
                instrMouse_2.midButton.append(buttons[1])
                instrMouse_2.rightButton.append(buttons[2])
                instrMouse_2.time.append(globalClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('instrMouse_2.x', instrMouse_2.x)
thisExp.addData('instrMouse_2.y', instrMouse_2.y)
thisExp.addData('instrMouse_2.leftButton', instrMouse_2.leftButton)
thisExp.addData('instrMouse_2.midButton', instrMouse_2.midButton)
thisExp.addData('instrMouse_2.rightButton', instrMouse_2.rightButton)
thisExp.addData('instrMouse_2.time', instrMouse_2.time)
thisExp.nextEntry()
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Initialization"-------
continueRoutine = True
routineTimer.add(0.200000)
# update component parameters for each repeat
start_session.setSize((0.1, 0.1))
# keep track of which components have finished
InitializationComponents = [start_session]
for thisComponent in InitializationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InitializationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Initialization"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InitializationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InitializationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_session* updates
    if start_session.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_session.frameNStart = frameN  # exact frame index
        start_session.tStart = t  # local t and not account for scr refresh
        start_session.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_session, 'tStartRefresh')  # time at next scr refresh
        start_session.setAutoDraw(True)
    if start_session.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > start_session.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            start_session.tStop = t  # not accounting for scr refresh
            start_session.frameNStop = frameN  # exact frame index
            win.timeOnFlip(start_session, 'tStopRefresh')  # time at next scr refresh
            start_session.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitializationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Initialization"-------
for thisComponent in InitializationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_session.started', start_session.tStartRefresh)
thisExp.addData('start_session.stopped', start_session.tStopRefresh)

# set up handler to look after randomisation of conditions etc
pracLoop = data.TrialHandler(nReps=7, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='pracLoop')
thisExp.addLoop(pracLoop)  # add the loop to the experiment
thisPracLoop = pracLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracLoop.rgb)
if thisPracLoop != None:
    for paramName in thisPracLoop:
        exec('{} = thisPracLoop[paramName]'.format(paramName))

for thisPracLoop in pracLoop:
    currentLoop = pracLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPracLoop.rgb)
    if thisPracLoop != None:
        for paramName in thisPracLoop:
            exec('{} = thisPracLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_fix"-------
    continueRoutine = True
    # update component parameters for each repeat
    fixDuration  = Durations[np.random.randint(Durations.size)] # Take one of the randomized durations
    #print("fix duration is ",fixDuration,'s')
    #print("target is ",ID_port)
    
    mouse1.pos=(0.0,0.0)
    centerOp = 0.25
    choiceOp = 0
    
    #EXIT = False
    Fixation = False
    TimeOut = True
    Correct = 0;
    timer0 = core.CountdownTimer(60)
    Center.setSize((0.1, 0.1))
    Choice0.setPos((xPos[0],yPos[0]))
    Choice0.setSize((0.1, 0.1))
    Choice1.setPos((xPos[1],yPos[1]))
    Choice1.setSize((0.1, 0.1))
    Choice2.setPos((xPos[2],yPos[2]))
    Choice2.setSize((0.1, 0.1))
    Choice3.setPos((xPos[3],yPos[3]))
    Choice3.setSize((0.1, 0.1))
    Choice4.setPos((xPos[4],yPos[4]))
    Choice4.setSize((0.1, 0.1))
    Choice5.setPos((xPos[5],yPos[5]))
    Choice5.setSize((0.1, 0.1))
    # setup some python lists for storing info about the mouse1
    mouse1.x = []
    mouse1.y = []
    mouse1.leftButton = []
    mouse1.midButton = []
    mouse1.rightButton = []
    mouse1.time = []
    gotValidClick = False  # until a click is received
    progressBar_out1.setPos((0.5, 0.2))
    progressBar_out1.setSize((0.02, 0.2))
    progressBar_in1.setPos((0.5, BarCenter))
    progressBar_in1.setSize((0.02, BarLength))
    progress_text1.setPos((.5,.35))
    progress_text1.setText(progress_msg)
    progress_text1.setHeight(0.05)
    # keep track of which components have finished
    trial_fixComponents = [Center, Choice0, Choice1, Choice2, Choice3, Choice4, Choice5, mouse1, progressBar_out1, progressBar_in1, progress_text1]
    for thisComponent in trial_fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_fix"-------
    while continueRoutine:
        # get current time
        t = trial_fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if timer0.getTime()>0:
            CursorCenterDistance = sqrt((mouse1.getPos()[0]- 0)**2 + (mouse1.getPos()[1]- 0)**2)
            if (CursorCenterDistance > minTargetDis):
                centerOp = .25
            else: 
                centerOp = 1
                
            if (CursorCenterDistance < minTargetDis) and (not(Fixation)):
                Fixation = True
                TimeOut= False
                timer1 = core.CountdownTimer(fixDuration)
            if (CursorCenterDistance < minTargetDis) and (timer1.getTime()<=0):
                Fixation = True
                TimeOut= False
                continueRoutine = False
                
                
        else:
            Fixation = False
            TimeOut = True
            continueRoutine = False
        
        # *Center* updates
        if Center.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Center.frameNStart = frameN  # exact frame index
            Center.tStart = t  # local t and not account for scr refresh
            Center.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Center, 'tStartRefresh')  # time at next scr refresh
            Center.setAutoDraw(True)
        if Center.status == STARTED:  # only update if drawing
            Center.setOpacity(centerOp, log=False)
        
        # *Choice0* updates
        if Choice0.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice0.frameNStart = frameN  # exact frame index
            Choice0.tStart = t  # local t and not account for scr refresh
            Choice0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice0, 'tStartRefresh')  # time at next scr refresh
            Choice0.setAutoDraw(True)
        
        # *Choice1* updates
        if Choice1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice1.frameNStart = frameN  # exact frame index
            Choice1.tStart = t  # local t and not account for scr refresh
            Choice1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice1, 'tStartRefresh')  # time at next scr refresh
            Choice1.setAutoDraw(True)
        
        # *Choice2* updates
        if Choice2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice2.frameNStart = frameN  # exact frame index
            Choice2.tStart = t  # local t and not account for scr refresh
            Choice2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice2, 'tStartRefresh')  # time at next scr refresh
            Choice2.setAutoDraw(True)
        
        # *Choice3* updates
        if Choice3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice3.frameNStart = frameN  # exact frame index
            Choice3.tStart = t  # local t and not account for scr refresh
            Choice3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice3, 'tStartRefresh')  # time at next scr refresh
            Choice3.setAutoDraw(True)
        
        # *Choice4* updates
        if Choice4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice4.frameNStart = frameN  # exact frame index
            Choice4.tStart = t  # local t and not account for scr refresh
            Choice4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice4, 'tStartRefresh')  # time at next scr refresh
            Choice4.setAutoDraw(True)
        
        # *Choice5* updates
        if Choice5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice5.frameNStart = frameN  # exact frame index
            Choice5.tStart = t  # local t and not account for scr refresh
            Choice5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice5, 'tStartRefresh')  # time at next scr refresh
            Choice5.setAutoDraw(True)
        # *mouse1* updates
        if mouse1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse1.frameNStart = frameN  # exact frame index
            mouse1.tStart = t  # local t and not account for scr refresh
            mouse1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse1, 'tStartRefresh')  # time at next scr refresh
            mouse1.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse1.status == STARTED:  # only update if started and not finished!
            x, y = mouse1.getPos()
            mouse1.x.append(x)
            mouse1.y.append(y)
            buttons = mouse1.getPressed()
            mouse1.leftButton.append(buttons[0])
            mouse1.midButton.append(buttons[1])
            mouse1.rightButton.append(buttons[2])
            mouse1.time.append(globalClock.getTime())
        
        # *progressBar_out1* updates
        if progressBar_out1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_out1.frameNStart = frameN  # exact frame index
            progressBar_out1.tStart = t  # local t and not account for scr refresh
            progressBar_out1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_out1, 'tStartRefresh')  # time at next scr refresh
            progressBar_out1.setAutoDraw(True)
        
        # *progressBar_in1* updates
        if progressBar_in1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_in1.frameNStart = frameN  # exact frame index
            progressBar_in1.tStart = t  # local t and not account for scr refresh
            progressBar_in1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_in1, 'tStartRefresh')  # time at next scr refresh
            progressBar_in1.setAutoDraw(True)
        
        # *progress_text1* updates
        if progress_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progress_text1.frameNStart = frameN  # exact frame index
            progress_text1.tStart = t  # local t and not account for scr refresh
            progress_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_text1, 'tStartRefresh')  # time at next scr refresh
            progress_text1.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_fix"-------
    for thisComponent in trial_fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    print("TimeOut=",TimeOut, "Fixation=",Fixation)
    pracLoop.addData('Center.started', Center.tStartRefresh)
    pracLoop.addData('Center.stopped', Center.tStopRefresh)
    # store data for pracLoop (TrialHandler)
    pracLoop.addData('mouse1.x', mouse1.x)
    pracLoop.addData('mouse1.y', mouse1.y)
    pracLoop.addData('mouse1.leftButton', mouse1.leftButton)
    pracLoop.addData('mouse1.midButton', mouse1.midButton)
    pracLoop.addData('mouse1.rightButton', mouse1.rightButton)
    pracLoop.addData('mouse1.time', mouse1.time)
    # the Routine "trial_fix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_choice"-------
    continueRoutine = True
    # update component parameters for each repeat
    Choose = False
    IDChoice = []
    RT= np.nan
    timer3 = core.CountdownTimer(maxWait_sec)
    
    if TimeOut:
        continueRoutine = False
    
    Center_2.setSize((0.1, 0.1))
    Choice0_2.setPos((xPos[0],yPos[0]))
    Choice0_2.setSize((0.1, 0.1))
    Choice1_2.setPos((xPos[1],yPos[1]))
    Choice1_2.setSize((0.1, 0.1))
    Choice2_2.setPos((xPos[2],yPos[2]))
    Choice2_2.setSize((0.1, 0.1))
    Choice3_2.setPos((xPos[3],yPos[3]))
    Choice3_2.setSize((0.1, 0.1))
    Choice4_2.setPos((xPos[4],yPos[4]))
    Choice4_2.setSize((0.1, 0.1))
    Choice5_2.setPos((xPos[5],yPos[5]))
    Choice5_2.setSize((0.1, 0.1))
    # setup some python lists for storing info about the mouse2
    mouse2.x = []
    mouse2.y = []
    mouse2.leftButton = []
    mouse2.midButton = []
    mouse2.rightButton = []
    mouse2.time = []
    gotValidClick = False  # until a click is received
    progressBar_out2.setPos((0.5, 0.2))
    progressBar_out2.setSize((0.02, 0.2))
    progressBar_in2.setPos((0.5, BarCenter))
    progressBar_in2.setSize((0.02, BarLength))
    progress_text2.setPos((.5,.35))
    progress_text2.setText(progress_msg)
    progress_text2.setHeight(0.05)
    # keep track of which components have finished
    trial_choiceComponents = [Center_2, Choice0_2, Choice1_2, Choice2_2, Choice3_2, Choice4_2, Choice5_2, mouse2, progressBar_out2, progressBar_in2, progress_text2]
    for thisComponent in trial_choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_choice"-------
    while continueRoutine:
        # get current time
        t = trial_choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_choiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if (timer3.getTime() > 0):
            for p in Ports:
                CursorChoiceDistance[p] = sqrt((mouse2.getPos()[0]-xPos[p])**2 + (mouse2.getPos()[1]-yPos[p])**2)
                if (CursorChoiceDistance[p] < minTargetDis):
                    Choose = True
                    IDChoice = p
                    RT = maxWait_sec - timer3.getTime()
                    continueRoutine = False
                    
        else:
             TimeOut = True
             continueRoutine = False
        
        # *Center_2* updates
        if Center_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Center_2.frameNStart = frameN  # exact frame index
            Center_2.tStart = t  # local t and not account for scr refresh
            Center_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Center_2, 'tStartRefresh')  # time at next scr refresh
            Center_2.setAutoDraw(True)
        if Center_2.status == STARTED:  # only update if drawing
            Center_2.setOpacity(centerOp, log=False)
        
        # *Choice0_2* updates
        if Choice0_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice0_2.frameNStart = frameN  # exact frame index
            Choice0_2.tStart = t  # local t and not account for scr refresh
            Choice0_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice0_2, 'tStartRefresh')  # time at next scr refresh
            Choice0_2.setAutoDraw(True)
        
        # *Choice1_2* updates
        if Choice1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice1_2.frameNStart = frameN  # exact frame index
            Choice1_2.tStart = t  # local t and not account for scr refresh
            Choice1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice1_2, 'tStartRefresh')  # time at next scr refresh
            Choice1_2.setAutoDraw(True)
        
        # *Choice2_2* updates
        if Choice2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice2_2.frameNStart = frameN  # exact frame index
            Choice2_2.tStart = t  # local t and not account for scr refresh
            Choice2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice2_2, 'tStartRefresh')  # time at next scr refresh
            Choice2_2.setAutoDraw(True)
        
        # *Choice3_2* updates
        if Choice3_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice3_2.frameNStart = frameN  # exact frame index
            Choice3_2.tStart = t  # local t and not account for scr refresh
            Choice3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice3_2, 'tStartRefresh')  # time at next scr refresh
            Choice3_2.setAutoDraw(True)
        
        # *Choice4_2* updates
        if Choice4_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice4_2.frameNStart = frameN  # exact frame index
            Choice4_2.tStart = t  # local t and not account for scr refresh
            Choice4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice4_2, 'tStartRefresh')  # time at next scr refresh
            Choice4_2.setAutoDraw(True)
        
        # *Choice5_2* updates
        if Choice5_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice5_2.frameNStart = frameN  # exact frame index
            Choice5_2.tStart = t  # local t and not account for scr refresh
            Choice5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice5_2, 'tStartRefresh')  # time at next scr refresh
            Choice5_2.setAutoDraw(True)
        # *mouse2* updates
        if mouse2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse2.frameNStart = frameN  # exact frame index
            mouse2.tStart = t  # local t and not account for scr refresh
            mouse2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse2, 'tStartRefresh')  # time at next scr refresh
            mouse2.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse2.status == STARTED:  # only update if started and not finished!
            x, y = mouse2.getPos()
            mouse2.x.append(x)
            mouse2.y.append(y)
            buttons = mouse2.getPressed()
            mouse2.leftButton.append(buttons[0])
            mouse2.midButton.append(buttons[1])
            mouse2.rightButton.append(buttons[2])
            mouse2.time.append(globalClock.getTime())
        
        # *progressBar_out2* updates
        if progressBar_out2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_out2.frameNStart = frameN  # exact frame index
            progressBar_out2.tStart = t  # local t and not account for scr refresh
            progressBar_out2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_out2, 'tStartRefresh')  # time at next scr refresh
            progressBar_out2.setAutoDraw(True)
        
        # *progressBar_in2* updates
        if progressBar_in2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_in2.frameNStart = frameN  # exact frame index
            progressBar_in2.tStart = t  # local t and not account for scr refresh
            progressBar_in2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_in2, 'tStartRefresh')  # time at next scr refresh
            progressBar_in2.setAutoDraw(True)
        
        # *progress_text2* updates
        if progress_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progress_text2.frameNStart = frameN  # exact frame index
            progress_text2.tStart = t  # local t and not account for scr refresh
            progress_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_text2, 'tStartRefresh')  # time at next scr refresh
            progress_text2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_choice"-------
    for thisComponent in trial_choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    print("target = ",ID_port," choice = ", IDChoice, "RT = ", RT)
    if Choose:
        choiceOp = 1
        choice_xPos=xPos[IDChoice]
        choice_yPos=yPos[IDChoice]
    else:
        choiceOp = 0
        choice_xPos=0
        choice_yPos=0
    # store data for pracLoop (TrialHandler)
    pracLoop.addData('mouse2.x', mouse2.x)
    pracLoop.addData('mouse2.y', mouse2.y)
    pracLoop.addData('mouse2.leftButton', mouse2.leftButton)
    pracLoop.addData('mouse2.midButton', mouse2.midButton)
    pracLoop.addData('mouse2.rightButton', mouse2.rightButton)
    pracLoop.addData('mouse2.time', mouse2.time)
    # the Routine "trial_choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    cR = 1; cG =1; cB=1; 
    msg=""; tone = "acquire.wav";
    
    if TimeOut:
        Counter_TimeOut = Counter_TimeOut+1;
        Correct=0;
        continueRotine = False
    else:
         if not(IDChoice==[]):
            Counter_Complete = Counter_Complete+1;
            if IDChoice==ID_port:
               Counter_Correct = Counter_Correct +1;
               cR=0; cG=1;cB=0;
               msg = "Correct!"
               Correct=1
               tone = "reward.wav"
               print(msg)
            else: 
               Counter_Error = Counter_Error +1;
               cR=1; cG=0;cB=0;
               msg = "Incorrect!"
               Correct=0
               tone = "failure.wav"
               print(msg)
            reward_rate = Counter_Correct/Counter_Complete;
            
         else:
            Correct=0
            continueRotine = False
    Center_3.setSize((0.1, 0.1))
    Choice0_3.setPos((xPos[0],yPos[0]))
    Choice0_3.setSize((0.1, 0.1))
    Choice1_3.setPos((xPos[1],yPos[1]))
    Choice1_3.setSize((0.1, 0.1))
    Choice2_3.setPos((xPos[2],yPos[2]))
    Choice2_3.setSize((0.1, 0.1))
    Choice3_3.setPos((xPos[3],yPos[3]))
    Choice3_3.setSize((0.1, 0.1))
    Choice4_3.setPos((xPos[4],yPos[4]))
    Choice4_3.setSize((0.1, 0.1))
    Choice5_3.setPos((xPos[5],yPos[5]))
    Choice5_3.setSize((0.1, 0.1))
    Chosen.setFillColor([cR,cG,cB])
    Chosen.setOpacity(choiceOp)
    Chosen.setPos((choice_xPos,choice_yPos))
    Chosen.setSize((0.1, 0.1))
    Message.setOpacity(feedbackOp)
    Message.setText(msg)
    progressBar_out3.setPos((0.5, 0.2))
    progressBar_out3.setSize((0.02, 0.2))
    progressBar_in3.setPos((0.5, BarCenter))
    progressBar_in3.setSize((0.02, BarLength))
    progress_text3.setPos((.5,.35))
    progress_text3.setText(progress_msg)
    progress_text3.setHeight(0.05)
    # keep track of which components have finished
    feedbackComponents = [Center_3, Choice0_3, Choice1_3, Choice2_3, Choice3_3, Choice4_3, Choice5_3, Chosen, Message, progressBar_out3, progressBar_in3, progress_text3]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Center_3* updates
        if Center_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Center_3.frameNStart = frameN  # exact frame index
            Center_3.tStart = t  # local t and not account for scr refresh
            Center_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Center_3, 'tStartRefresh')  # time at next scr refresh
            Center_3.setAutoDraw(True)
        if Center_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Center_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Center_3.tStop = t  # not accounting for scr refresh
                Center_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Center_3, 'tStopRefresh')  # time at next scr refresh
                Center_3.setAutoDraw(False)
        if Center_3.status == STARTED:  # only update if drawing
            Center_3.setOpacity(centerOp, log=False)
        
        # *Choice0_3* updates
        if Choice0_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice0_3.frameNStart = frameN  # exact frame index
            Choice0_3.tStart = t  # local t and not account for scr refresh
            Choice0_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice0_3, 'tStartRefresh')  # time at next scr refresh
            Choice0_3.setAutoDraw(True)
        if Choice0_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice0_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice0_3.tStop = t  # not accounting for scr refresh
                Choice0_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice0_3, 'tStopRefresh')  # time at next scr refresh
                Choice0_3.setAutoDraw(False)
        
        # *Choice1_3* updates
        if Choice1_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice1_3.frameNStart = frameN  # exact frame index
            Choice1_3.tStart = t  # local t and not account for scr refresh
            Choice1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice1_3, 'tStartRefresh')  # time at next scr refresh
            Choice1_3.setAutoDraw(True)
        if Choice1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice1_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice1_3.tStop = t  # not accounting for scr refresh
                Choice1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice1_3, 'tStopRefresh')  # time at next scr refresh
                Choice1_3.setAutoDraw(False)
        
        # *Choice2_3* updates
        if Choice2_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice2_3.frameNStart = frameN  # exact frame index
            Choice2_3.tStart = t  # local t and not account for scr refresh
            Choice2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice2_3, 'tStartRefresh')  # time at next scr refresh
            Choice2_3.setAutoDraw(True)
        if Choice2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice2_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice2_3.tStop = t  # not accounting for scr refresh
                Choice2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice2_3, 'tStopRefresh')  # time at next scr refresh
                Choice2_3.setAutoDraw(False)
        
        # *Choice3_3* updates
        if Choice3_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice3_3.frameNStart = frameN  # exact frame index
            Choice3_3.tStart = t  # local t and not account for scr refresh
            Choice3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice3_3, 'tStartRefresh')  # time at next scr refresh
            Choice3_3.setAutoDraw(True)
        if Choice3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice3_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice3_3.tStop = t  # not accounting for scr refresh
                Choice3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice3_3, 'tStopRefresh')  # time at next scr refresh
                Choice3_3.setAutoDraw(False)
        
        # *Choice4_3* updates
        if Choice4_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice4_3.frameNStart = frameN  # exact frame index
            Choice4_3.tStart = t  # local t and not account for scr refresh
            Choice4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice4_3, 'tStartRefresh')  # time at next scr refresh
            Choice4_3.setAutoDraw(True)
        if Choice4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice4_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice4_3.tStop = t  # not accounting for scr refresh
                Choice4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice4_3, 'tStopRefresh')  # time at next scr refresh
                Choice4_3.setAutoDraw(False)
        
        # *Choice5_3* updates
        if Choice5_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice5_3.frameNStart = frameN  # exact frame index
            Choice5_3.tStart = t  # local t and not account for scr refresh
            Choice5_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice5_3, 'tStartRefresh')  # time at next scr refresh
            Choice5_3.setAutoDraw(True)
        if Choice5_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice5_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice5_3.tStop = t  # not accounting for scr refresh
                Choice5_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice5_3, 'tStopRefresh')  # time at next scr refresh
                Choice5_3.setAutoDraw(False)
        
        # *Chosen* updates
        if Chosen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Chosen.frameNStart = frameN  # exact frame index
            Chosen.tStart = t  # local t and not account for scr refresh
            Chosen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Chosen, 'tStartRefresh')  # time at next scr refresh
            Chosen.setAutoDraw(True)
        if Chosen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Chosen.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Chosen.tStop = t  # not accounting for scr refresh
                Chosen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Chosen, 'tStopRefresh')  # time at next scr refresh
                Chosen.setAutoDraw(False)
        
        # *Message* updates
        if Message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Message.frameNStart = frameN  # exact frame index
            Message.tStart = t  # local t and not account for scr refresh
            Message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Message, 'tStartRefresh')  # time at next scr refresh
            Message.setAutoDraw(True)
        if Message.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Message.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Message.tStop = t  # not accounting for scr refresh
                Message.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Message, 'tStopRefresh')  # time at next scr refresh
                Message.setAutoDraw(False)
        
        # *progressBar_out3* updates
        if progressBar_out3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_out3.frameNStart = frameN  # exact frame index
            progressBar_out3.tStart = t  # local t and not account for scr refresh
            progressBar_out3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_out3, 'tStartRefresh')  # time at next scr refresh
            progressBar_out3.setAutoDraw(True)
        if progressBar_out3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progressBar_out3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                progressBar_out3.tStop = t  # not accounting for scr refresh
                progressBar_out3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progressBar_out3, 'tStopRefresh')  # time at next scr refresh
                progressBar_out3.setAutoDraw(False)
        
        # *progressBar_in3* updates
        if progressBar_in3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_in3.frameNStart = frameN  # exact frame index
            progressBar_in3.tStart = t  # local t and not account for scr refresh
            progressBar_in3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_in3, 'tStartRefresh')  # time at next scr refresh
            progressBar_in3.setAutoDraw(True)
        if progressBar_in3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progressBar_in3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                progressBar_in3.tStop = t  # not accounting for scr refresh
                progressBar_in3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progressBar_in3, 'tStopRefresh')  # time at next scr refresh
                progressBar_in3.setAutoDraw(False)
        
        # *progress_text3* updates
        if progress_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progress_text3.frameNStart = frameN  # exact frame index
            progress_text3.tStart = t  # local t and not account for scr refresh
            progress_text3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_text3, 'tStartRefresh')  # time at next scr refresh
            progress_text3.setAutoDraw(True)
        if progress_text3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progress_text3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                progress_text3.tStop = t  # not accounting for scr refresh
                progress_text3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progress_text3, 'tStopRefresh')  # time at next scr refresh
                progress_text3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pracLoop.addData('Chosen.started', Chosen.tStartRefresh)
    pracLoop.addData('Chosen.stopped', Chosen.tStopRefresh)
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    progressBar_out4.setPos((0.5, 0.2))
    progressBar_out4.setSize((0.02, 0.2))
    progressBar_in4.setPos((0.5, BarCenter))
    progressBar_in4.setSize((0.02, BarLength))
    progress_text4.setPos((.5,.35))
    progress_text4.setText(progress_msg)
    progress_text4.setHeight(0.05)
    # keep track of which components have finished
    ITIComponents = [blank, progressBar_out4, progressBar_in4, progress_text4]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + ITI_sec-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # *progressBar_out4* updates
        if progressBar_out4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_out4.frameNStart = frameN  # exact frame index
            progressBar_out4.tStart = t  # local t and not account for scr refresh
            progressBar_out4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_out4, 'tStartRefresh')  # time at next scr refresh
            progressBar_out4.setAutoDraw(True)
        if progressBar_out4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progressBar_out4.tStartRefresh + ITI_sec-frameTolerance:
                # keep track of stop time/frame for later
                progressBar_out4.tStop = t  # not accounting for scr refresh
                progressBar_out4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progressBar_out4, 'tStopRefresh')  # time at next scr refresh
                progressBar_out4.setAutoDraw(False)
        
        # *progressBar_in4* updates
        if progressBar_in4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_in4.frameNStart = frameN  # exact frame index
            progressBar_in4.tStart = t  # local t and not account for scr refresh
            progressBar_in4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_in4, 'tStartRefresh')  # time at next scr refresh
            progressBar_in4.setAutoDraw(True)
        if progressBar_in4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progressBar_in4.tStartRefresh + ITI_sec-frameTolerance:
                # keep track of stop time/frame for later
                progressBar_in4.tStop = t  # not accounting for scr refresh
                progressBar_in4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progressBar_in4, 'tStopRefresh')  # time at next scr refresh
                progressBar_in4.setAutoDraw(False)
        
        # *progress_text4* updates
        if progress_text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progress_text4.frameNStart = frameN  # exact frame index
            progress_text4.tStart = t  # local t and not account for scr refresh
            progress_text4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_text4, 'tStartRefresh')  # time at next scr refresh
            progress_text4.setAutoDraw(True)
        if progress_text4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progress_text4.tStartRefresh + ITI_sec-frameTolerance:
                # keep track of stop time/frame for later
                progress_text4.tStop = t  # not accounting for scr refresh
                progress_text4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progress_text4, 'tStopRefresh')  # time at next scr refresh
                progress_text4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pracLoop.addData('blank.started', blank.tStartRefresh)
    pracLoop.addData('blank.stopped', blank.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 7 repeats of 'pracLoop'


# ------Prepare to start Routine "instructions3"-------
continueRoutine = True
# update component parameters for each repeat
#ID_port = 0
ID_port = np.random.randint(Nport)
Ncorrect = 0;
Nblock = 1;
Counter_TimeOut = 0
Counter_Complete = 0
Counter_Correct = 0
Counter_Error = 0
msg=""
feedbackOp = 0;
# setup some python lists for storing info about the instrMouse_3
instrMouse_3.x = []
instrMouse_3.y = []
instrMouse_3.leftButton = []
instrMouse_3.midButton = []
instrMouse_3.rightButton = []
instrMouse_3.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions3Components = [instruction_3, instrMouse_3]
for thisComponent in instructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions3"-------
while continueRoutine:
    # get current time
    t = instructions3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_3* updates
    if instruction_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_3.frameNStart = frameN  # exact frame index
        instruction_3.tStart = t  # local t and not account for scr refresh
        instruction_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_3, 'tStartRefresh')  # time at next scr refresh
        instruction_3.setAutoDraw(True)
    # *instrMouse_3* updates
    if instrMouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrMouse_3.frameNStart = frameN  # exact frame index
        instrMouse_3.tStart = t  # local t and not account for scr refresh
        instrMouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrMouse_3, 'tStartRefresh')  # time at next scr refresh
        instrMouse_3.status = STARTED
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if instrMouse_3.status == STARTED:  # only update if started and not finished!
        buttons = instrMouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = instrMouse_3.getPos()
                instrMouse_3.x.append(x)
                instrMouse_3.y.append(y)
                buttons = instrMouse_3.getPressed()
                instrMouse_3.leftButton.append(buttons[0])
                instrMouse_3.midButton.append(buttons[1])
                instrMouse_3.rightButton.append(buttons[2])
                instrMouse_3.time.append(globalClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions3"-------
for thisComponent in instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('instrMouse_3.x', instrMouse_3.x)
thisExp.addData('instrMouse_3.y', instrMouse_3.y)
thisExp.addData('instrMouse_3.leftButton', instrMouse_3.leftButton)
thisExp.addData('instrMouse_3.midButton', instrMouse_3.midButton)
thisExp.addData('instrMouse_3.rightButton', instrMouse_3.rightButton)
thisExp.addData('instrMouse_3.time', instrMouse_3.time)
thisExp.nextEntry()
# the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mainLoop = data.TrialHandler(nReps=Total_Ntrials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='mainLoop')
thisExp.addLoop(mainLoop)  # add the loop to the experiment
thisMainLoop = mainLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
if thisMainLoop != None:
    for paramName in thisMainLoop:
        exec('{} = thisMainLoop[paramName]'.format(paramName))

for thisMainLoop in mainLoop:
    currentLoop = mainLoop
    # abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
    if thisMainLoop != None:
        for paramName in thisMainLoop:
            exec('{} = thisMainLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_fix"-------
    continueRoutine = True
    # update component parameters for each repeat
    fixDuration  = Durations[np.random.randint(Durations.size)] # Take one of the randomized durations
    #print("fix duration is ",fixDuration,'s')
    #print("target is ",ID_port)
    
    mouse1.pos=(0.0,0.0)
    centerOp = 0.25
    choiceOp = 0
    
    #EXIT = False
    Fixation = False
    TimeOut = True
    Correct = 0;
    timer0 = core.CountdownTimer(60)
    Center.setSize((0.1, 0.1))
    Choice0.setPos((xPos[0],yPos[0]))
    Choice0.setSize((0.1, 0.1))
    Choice1.setPos((xPos[1],yPos[1]))
    Choice1.setSize((0.1, 0.1))
    Choice2.setPos((xPos[2],yPos[2]))
    Choice2.setSize((0.1, 0.1))
    Choice3.setPos((xPos[3],yPos[3]))
    Choice3.setSize((0.1, 0.1))
    Choice4.setPos((xPos[4],yPos[4]))
    Choice4.setSize((0.1, 0.1))
    Choice5.setPos((xPos[5],yPos[5]))
    Choice5.setSize((0.1, 0.1))
    # setup some python lists for storing info about the mouse1
    mouse1.x = []
    mouse1.y = []
    mouse1.leftButton = []
    mouse1.midButton = []
    mouse1.rightButton = []
    mouse1.time = []
    gotValidClick = False  # until a click is received
    progressBar_out1.setPos((0.5, 0.2))
    progressBar_out1.setSize((0.02, 0.2))
    progressBar_in1.setPos((0.5, BarCenter))
    progressBar_in1.setSize((0.02, BarLength))
    progress_text1.setPos((.5,.35))
    progress_text1.setText(progress_msg)
    progress_text1.setHeight(0.05)
    # keep track of which components have finished
    trial_fixComponents = [Center, Choice0, Choice1, Choice2, Choice3, Choice4, Choice5, mouse1, progressBar_out1, progressBar_in1, progress_text1]
    for thisComponent in trial_fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_fix"-------
    while continueRoutine:
        # get current time
        t = trial_fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if timer0.getTime()>0:
            CursorCenterDistance = sqrt((mouse1.getPos()[0]- 0)**2 + (mouse1.getPos()[1]- 0)**2)
            if (CursorCenterDistance > minTargetDis):
                centerOp = .25
            else: 
                centerOp = 1
                
            if (CursorCenterDistance < minTargetDis) and (not(Fixation)):
                Fixation = True
                TimeOut= False
                timer1 = core.CountdownTimer(fixDuration)
            if (CursorCenterDistance < minTargetDis) and (timer1.getTime()<=0):
                Fixation = True
                TimeOut= False
                continueRoutine = False
                
                
        else:
            Fixation = False
            TimeOut = True
            continueRoutine = False
        
        # *Center* updates
        if Center.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Center.frameNStart = frameN  # exact frame index
            Center.tStart = t  # local t and not account for scr refresh
            Center.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Center, 'tStartRefresh')  # time at next scr refresh
            Center.setAutoDraw(True)
        if Center.status == STARTED:  # only update if drawing
            Center.setOpacity(centerOp, log=False)
        
        # *Choice0* updates
        if Choice0.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice0.frameNStart = frameN  # exact frame index
            Choice0.tStart = t  # local t and not account for scr refresh
            Choice0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice0, 'tStartRefresh')  # time at next scr refresh
            Choice0.setAutoDraw(True)
        
        # *Choice1* updates
        if Choice1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice1.frameNStart = frameN  # exact frame index
            Choice1.tStart = t  # local t and not account for scr refresh
            Choice1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice1, 'tStartRefresh')  # time at next scr refresh
            Choice1.setAutoDraw(True)
        
        # *Choice2* updates
        if Choice2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice2.frameNStart = frameN  # exact frame index
            Choice2.tStart = t  # local t and not account for scr refresh
            Choice2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice2, 'tStartRefresh')  # time at next scr refresh
            Choice2.setAutoDraw(True)
        
        # *Choice3* updates
        if Choice3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice3.frameNStart = frameN  # exact frame index
            Choice3.tStart = t  # local t and not account for scr refresh
            Choice3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice3, 'tStartRefresh')  # time at next scr refresh
            Choice3.setAutoDraw(True)
        
        # *Choice4* updates
        if Choice4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice4.frameNStart = frameN  # exact frame index
            Choice4.tStart = t  # local t and not account for scr refresh
            Choice4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice4, 'tStartRefresh')  # time at next scr refresh
            Choice4.setAutoDraw(True)
        
        # *Choice5* updates
        if Choice5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice5.frameNStart = frameN  # exact frame index
            Choice5.tStart = t  # local t and not account for scr refresh
            Choice5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice5, 'tStartRefresh')  # time at next scr refresh
            Choice5.setAutoDraw(True)
        # *mouse1* updates
        if mouse1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse1.frameNStart = frameN  # exact frame index
            mouse1.tStart = t  # local t and not account for scr refresh
            mouse1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse1, 'tStartRefresh')  # time at next scr refresh
            mouse1.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse1.status == STARTED:  # only update if started and not finished!
            x, y = mouse1.getPos()
            mouse1.x.append(x)
            mouse1.y.append(y)
            buttons = mouse1.getPressed()
            mouse1.leftButton.append(buttons[0])
            mouse1.midButton.append(buttons[1])
            mouse1.rightButton.append(buttons[2])
            mouse1.time.append(globalClock.getTime())
        
        # *progressBar_out1* updates
        if progressBar_out1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_out1.frameNStart = frameN  # exact frame index
            progressBar_out1.tStart = t  # local t and not account for scr refresh
            progressBar_out1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_out1, 'tStartRefresh')  # time at next scr refresh
            progressBar_out1.setAutoDraw(True)
        
        # *progressBar_in1* updates
        if progressBar_in1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_in1.frameNStart = frameN  # exact frame index
            progressBar_in1.tStart = t  # local t and not account for scr refresh
            progressBar_in1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_in1, 'tStartRefresh')  # time at next scr refresh
            progressBar_in1.setAutoDraw(True)
        
        # *progress_text1* updates
        if progress_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progress_text1.frameNStart = frameN  # exact frame index
            progress_text1.tStart = t  # local t and not account for scr refresh
            progress_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_text1, 'tStartRefresh')  # time at next scr refresh
            progress_text1.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_fix"-------
    for thisComponent in trial_fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    print("TimeOut=",TimeOut, "Fixation=",Fixation)
    mainLoop.addData('Center.started', Center.tStartRefresh)
    mainLoop.addData('Center.stopped', Center.tStopRefresh)
    # store data for mainLoop (TrialHandler)
    mainLoop.addData('mouse1.x', mouse1.x)
    mainLoop.addData('mouse1.y', mouse1.y)
    mainLoop.addData('mouse1.leftButton', mouse1.leftButton)
    mainLoop.addData('mouse1.midButton', mouse1.midButton)
    mainLoop.addData('mouse1.rightButton', mouse1.rightButton)
    mainLoop.addData('mouse1.time', mouse1.time)
    # the Routine "trial_fix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_choice"-------
    continueRoutine = True
    # update component parameters for each repeat
    Choose = False
    IDChoice = []
    RT= np.nan
    timer3 = core.CountdownTimer(maxWait_sec)
    
    if TimeOut:
        continueRoutine = False
    
    Center_2.setSize((0.1, 0.1))
    Choice0_2.setPos((xPos[0],yPos[0]))
    Choice0_2.setSize((0.1, 0.1))
    Choice1_2.setPos((xPos[1],yPos[1]))
    Choice1_2.setSize((0.1, 0.1))
    Choice2_2.setPos((xPos[2],yPos[2]))
    Choice2_2.setSize((0.1, 0.1))
    Choice3_2.setPos((xPos[3],yPos[3]))
    Choice3_2.setSize((0.1, 0.1))
    Choice4_2.setPos((xPos[4],yPos[4]))
    Choice4_2.setSize((0.1, 0.1))
    Choice5_2.setPos((xPos[5],yPos[5]))
    Choice5_2.setSize((0.1, 0.1))
    # setup some python lists for storing info about the mouse2
    mouse2.x = []
    mouse2.y = []
    mouse2.leftButton = []
    mouse2.midButton = []
    mouse2.rightButton = []
    mouse2.time = []
    gotValidClick = False  # until a click is received
    progressBar_out2.setPos((0.5, 0.2))
    progressBar_out2.setSize((0.02, 0.2))
    progressBar_in2.setPos((0.5, BarCenter))
    progressBar_in2.setSize((0.02, BarLength))
    progress_text2.setPos((.5,.35))
    progress_text2.setText(progress_msg)
    progress_text2.setHeight(0.05)
    # keep track of which components have finished
    trial_choiceComponents = [Center_2, Choice0_2, Choice1_2, Choice2_2, Choice3_2, Choice4_2, Choice5_2, mouse2, progressBar_out2, progressBar_in2, progress_text2]
    for thisComponent in trial_choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_choice"-------
    while continueRoutine:
        # get current time
        t = trial_choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_choiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if (timer3.getTime() > 0):
            for p in Ports:
                CursorChoiceDistance[p] = sqrt((mouse2.getPos()[0]-xPos[p])**2 + (mouse2.getPos()[1]-yPos[p])**2)
                if (CursorChoiceDistance[p] < minTargetDis):
                    Choose = True
                    IDChoice = p
                    RT = maxWait_sec - timer3.getTime()
                    continueRoutine = False
                    
        else:
             TimeOut = True
             continueRoutine = False
        
        # *Center_2* updates
        if Center_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Center_2.frameNStart = frameN  # exact frame index
            Center_2.tStart = t  # local t and not account for scr refresh
            Center_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Center_2, 'tStartRefresh')  # time at next scr refresh
            Center_2.setAutoDraw(True)
        if Center_2.status == STARTED:  # only update if drawing
            Center_2.setOpacity(centerOp, log=False)
        
        # *Choice0_2* updates
        if Choice0_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice0_2.frameNStart = frameN  # exact frame index
            Choice0_2.tStart = t  # local t and not account for scr refresh
            Choice0_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice0_2, 'tStartRefresh')  # time at next scr refresh
            Choice0_2.setAutoDraw(True)
        
        # *Choice1_2* updates
        if Choice1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice1_2.frameNStart = frameN  # exact frame index
            Choice1_2.tStart = t  # local t and not account for scr refresh
            Choice1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice1_2, 'tStartRefresh')  # time at next scr refresh
            Choice1_2.setAutoDraw(True)
        
        # *Choice2_2* updates
        if Choice2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice2_2.frameNStart = frameN  # exact frame index
            Choice2_2.tStart = t  # local t and not account for scr refresh
            Choice2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice2_2, 'tStartRefresh')  # time at next scr refresh
            Choice2_2.setAutoDraw(True)
        
        # *Choice3_2* updates
        if Choice3_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice3_2.frameNStart = frameN  # exact frame index
            Choice3_2.tStart = t  # local t and not account for scr refresh
            Choice3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice3_2, 'tStartRefresh')  # time at next scr refresh
            Choice3_2.setAutoDraw(True)
        
        # *Choice4_2* updates
        if Choice4_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice4_2.frameNStart = frameN  # exact frame index
            Choice4_2.tStart = t  # local t and not account for scr refresh
            Choice4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice4_2, 'tStartRefresh')  # time at next scr refresh
            Choice4_2.setAutoDraw(True)
        
        # *Choice5_2* updates
        if Choice5_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice5_2.frameNStart = frameN  # exact frame index
            Choice5_2.tStart = t  # local t and not account for scr refresh
            Choice5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice5_2, 'tStartRefresh')  # time at next scr refresh
            Choice5_2.setAutoDraw(True)
        # *mouse2* updates
        if mouse2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse2.frameNStart = frameN  # exact frame index
            mouse2.tStart = t  # local t and not account for scr refresh
            mouse2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse2, 'tStartRefresh')  # time at next scr refresh
            mouse2.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse2.status == STARTED:  # only update if started and not finished!
            x, y = mouse2.getPos()
            mouse2.x.append(x)
            mouse2.y.append(y)
            buttons = mouse2.getPressed()
            mouse2.leftButton.append(buttons[0])
            mouse2.midButton.append(buttons[1])
            mouse2.rightButton.append(buttons[2])
            mouse2.time.append(globalClock.getTime())
        
        # *progressBar_out2* updates
        if progressBar_out2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_out2.frameNStart = frameN  # exact frame index
            progressBar_out2.tStart = t  # local t and not account for scr refresh
            progressBar_out2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_out2, 'tStartRefresh')  # time at next scr refresh
            progressBar_out2.setAutoDraw(True)
        
        # *progressBar_in2* updates
        if progressBar_in2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_in2.frameNStart = frameN  # exact frame index
            progressBar_in2.tStart = t  # local t and not account for scr refresh
            progressBar_in2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_in2, 'tStartRefresh')  # time at next scr refresh
            progressBar_in2.setAutoDraw(True)
        
        # *progress_text2* updates
        if progress_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progress_text2.frameNStart = frameN  # exact frame index
            progress_text2.tStart = t  # local t and not account for scr refresh
            progress_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_text2, 'tStartRefresh')  # time at next scr refresh
            progress_text2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_choice"-------
    for thisComponent in trial_choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    print("target = ",ID_port," choice = ", IDChoice, "RT = ", RT)
    if Choose:
        choiceOp = 1
        choice_xPos=xPos[IDChoice]
        choice_yPos=yPos[IDChoice]
    else:
        choiceOp = 0
        choice_xPos=0
        choice_yPos=0
    # store data for mainLoop (TrialHandler)
    mainLoop.addData('mouse2.x', mouse2.x)
    mainLoop.addData('mouse2.y', mouse2.y)
    mainLoop.addData('mouse2.leftButton', mouse2.leftButton)
    mainLoop.addData('mouse2.midButton', mouse2.midButton)
    mainLoop.addData('mouse2.rightButton', mouse2.rightButton)
    mainLoop.addData('mouse2.time', mouse2.time)
    # the Routine "trial_choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    cR = 1; cG =1; cB=1; 
    msg=""; tone = "acquire.wav";
    
    if TimeOut:
        Counter_TimeOut = Counter_TimeOut+1;
        Correct=0;
        continueRotine = False
    else:
         if not(IDChoice==[]):
            Counter_Complete = Counter_Complete+1;
            if IDChoice==ID_port:
               Counter_Correct = Counter_Correct +1;
               cR=0; cG=1;cB=0;
               msg = "Correct!"
               Correct=1
               tone = "reward.wav"
               print(msg)
            else: 
               Counter_Error = Counter_Error +1;
               cR=1; cG=0;cB=0;
               msg = "Incorrect!"
               Correct=0
               tone = "failure.wav"
               print(msg)
            reward_rate = Counter_Correct/Counter_Complete;
            
         else:
            Correct=0
            continueRotine = False
    Center_3.setSize((0.1, 0.1))
    Choice0_3.setPos((xPos[0],yPos[0]))
    Choice0_3.setSize((0.1, 0.1))
    Choice1_3.setPos((xPos[1],yPos[1]))
    Choice1_3.setSize((0.1, 0.1))
    Choice2_3.setPos((xPos[2],yPos[2]))
    Choice2_3.setSize((0.1, 0.1))
    Choice3_3.setPos((xPos[3],yPos[3]))
    Choice3_3.setSize((0.1, 0.1))
    Choice4_3.setPos((xPos[4],yPos[4]))
    Choice4_3.setSize((0.1, 0.1))
    Choice5_3.setPos((xPos[5],yPos[5]))
    Choice5_3.setSize((0.1, 0.1))
    Chosen.setFillColor([cR,cG,cB])
    Chosen.setOpacity(choiceOp)
    Chosen.setPos((choice_xPos,choice_yPos))
    Chosen.setSize((0.1, 0.1))
    Message.setOpacity(feedbackOp)
    Message.setText(msg)
    progressBar_out3.setPos((0.5, 0.2))
    progressBar_out3.setSize((0.02, 0.2))
    progressBar_in3.setPos((0.5, BarCenter))
    progressBar_in3.setSize((0.02, BarLength))
    progress_text3.setPos((.5,.35))
    progress_text3.setText(progress_msg)
    progress_text3.setHeight(0.05)
    # keep track of which components have finished
    feedbackComponents = [Center_3, Choice0_3, Choice1_3, Choice2_3, Choice3_3, Choice4_3, Choice5_3, Chosen, Message, progressBar_out3, progressBar_in3, progress_text3]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Center_3* updates
        if Center_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Center_3.frameNStart = frameN  # exact frame index
            Center_3.tStart = t  # local t and not account for scr refresh
            Center_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Center_3, 'tStartRefresh')  # time at next scr refresh
            Center_3.setAutoDraw(True)
        if Center_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Center_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Center_3.tStop = t  # not accounting for scr refresh
                Center_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Center_3, 'tStopRefresh')  # time at next scr refresh
                Center_3.setAutoDraw(False)
        if Center_3.status == STARTED:  # only update if drawing
            Center_3.setOpacity(centerOp, log=False)
        
        # *Choice0_3* updates
        if Choice0_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice0_3.frameNStart = frameN  # exact frame index
            Choice0_3.tStart = t  # local t and not account for scr refresh
            Choice0_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice0_3, 'tStartRefresh')  # time at next scr refresh
            Choice0_3.setAutoDraw(True)
        if Choice0_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice0_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice0_3.tStop = t  # not accounting for scr refresh
                Choice0_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice0_3, 'tStopRefresh')  # time at next scr refresh
                Choice0_3.setAutoDraw(False)
        
        # *Choice1_3* updates
        if Choice1_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice1_3.frameNStart = frameN  # exact frame index
            Choice1_3.tStart = t  # local t and not account for scr refresh
            Choice1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice1_3, 'tStartRefresh')  # time at next scr refresh
            Choice1_3.setAutoDraw(True)
        if Choice1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice1_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice1_3.tStop = t  # not accounting for scr refresh
                Choice1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice1_3, 'tStopRefresh')  # time at next scr refresh
                Choice1_3.setAutoDraw(False)
        
        # *Choice2_3* updates
        if Choice2_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice2_3.frameNStart = frameN  # exact frame index
            Choice2_3.tStart = t  # local t and not account for scr refresh
            Choice2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice2_3, 'tStartRefresh')  # time at next scr refresh
            Choice2_3.setAutoDraw(True)
        if Choice2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice2_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice2_3.tStop = t  # not accounting for scr refresh
                Choice2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice2_3, 'tStopRefresh')  # time at next scr refresh
                Choice2_3.setAutoDraw(False)
        
        # *Choice3_3* updates
        if Choice3_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice3_3.frameNStart = frameN  # exact frame index
            Choice3_3.tStart = t  # local t and not account for scr refresh
            Choice3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice3_3, 'tStartRefresh')  # time at next scr refresh
            Choice3_3.setAutoDraw(True)
        if Choice3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice3_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice3_3.tStop = t  # not accounting for scr refresh
                Choice3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice3_3, 'tStopRefresh')  # time at next scr refresh
                Choice3_3.setAutoDraw(False)
        
        # *Choice4_3* updates
        if Choice4_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice4_3.frameNStart = frameN  # exact frame index
            Choice4_3.tStart = t  # local t and not account for scr refresh
            Choice4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice4_3, 'tStartRefresh')  # time at next scr refresh
            Choice4_3.setAutoDraw(True)
        if Choice4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice4_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice4_3.tStop = t  # not accounting for scr refresh
                Choice4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice4_3, 'tStopRefresh')  # time at next scr refresh
                Choice4_3.setAutoDraw(False)
        
        # *Choice5_3* updates
        if Choice5_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Choice5_3.frameNStart = frameN  # exact frame index
            Choice5_3.tStart = t  # local t and not account for scr refresh
            Choice5_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice5_3, 'tStartRefresh')  # time at next scr refresh
            Choice5_3.setAutoDraw(True)
        if Choice5_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice5_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Choice5_3.tStop = t  # not accounting for scr refresh
                Choice5_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice5_3, 'tStopRefresh')  # time at next scr refresh
                Choice5_3.setAutoDraw(False)
        
        # *Chosen* updates
        if Chosen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Chosen.frameNStart = frameN  # exact frame index
            Chosen.tStart = t  # local t and not account for scr refresh
            Chosen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Chosen, 'tStartRefresh')  # time at next scr refresh
            Chosen.setAutoDraw(True)
        if Chosen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Chosen.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Chosen.tStop = t  # not accounting for scr refresh
                Chosen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Chosen, 'tStopRefresh')  # time at next scr refresh
                Chosen.setAutoDraw(False)
        
        # *Message* updates
        if Message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Message.frameNStart = frameN  # exact frame index
            Message.tStart = t  # local t and not account for scr refresh
            Message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Message, 'tStartRefresh')  # time at next scr refresh
            Message.setAutoDraw(True)
        if Message.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Message.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Message.tStop = t  # not accounting for scr refresh
                Message.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Message, 'tStopRefresh')  # time at next scr refresh
                Message.setAutoDraw(False)
        
        # *progressBar_out3* updates
        if progressBar_out3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_out3.frameNStart = frameN  # exact frame index
            progressBar_out3.tStart = t  # local t and not account for scr refresh
            progressBar_out3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_out3, 'tStartRefresh')  # time at next scr refresh
            progressBar_out3.setAutoDraw(True)
        if progressBar_out3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progressBar_out3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                progressBar_out3.tStop = t  # not accounting for scr refresh
                progressBar_out3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progressBar_out3, 'tStopRefresh')  # time at next scr refresh
                progressBar_out3.setAutoDraw(False)
        
        # *progressBar_in3* updates
        if progressBar_in3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_in3.frameNStart = frameN  # exact frame index
            progressBar_in3.tStart = t  # local t and not account for scr refresh
            progressBar_in3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_in3, 'tStartRefresh')  # time at next scr refresh
            progressBar_in3.setAutoDraw(True)
        if progressBar_in3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progressBar_in3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                progressBar_in3.tStop = t  # not accounting for scr refresh
                progressBar_in3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progressBar_in3, 'tStopRefresh')  # time at next scr refresh
                progressBar_in3.setAutoDraw(False)
        
        # *progress_text3* updates
        if progress_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progress_text3.frameNStart = frameN  # exact frame index
            progress_text3.tStart = t  # local t and not account for scr refresh
            progress_text3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_text3, 'tStartRefresh')  # time at next scr refresh
            progress_text3.setAutoDraw(True)
        if progress_text3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progress_text3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                progress_text3.tStop = t  # not accounting for scr refresh
                progress_text3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progress_text3, 'tStopRefresh')  # time at next scr refresh
                progress_text3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mainLoop.addData('Chosen.started', Chosen.tStartRefresh)
    mainLoop.addData('Chosen.stopped', Chosen.tStopRefresh)
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    progressBar_out4.setPos((0.5, 0.2))
    progressBar_out4.setSize((0.02, 0.2))
    progressBar_in4.setPos((0.5, BarCenter))
    progressBar_in4.setSize((0.02, BarLength))
    progress_text4.setPos((.5,.35))
    progress_text4.setText(progress_msg)
    progress_text4.setHeight(0.05)
    # keep track of which components have finished
    ITIComponents = [blank, progressBar_out4, progressBar_in4, progress_text4]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + ITI_sec-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # *progressBar_out4* updates
        if progressBar_out4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_out4.frameNStart = frameN  # exact frame index
            progressBar_out4.tStart = t  # local t and not account for scr refresh
            progressBar_out4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_out4, 'tStartRefresh')  # time at next scr refresh
            progressBar_out4.setAutoDraw(True)
        if progressBar_out4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progressBar_out4.tStartRefresh + ITI_sec-frameTolerance:
                # keep track of stop time/frame for later
                progressBar_out4.tStop = t  # not accounting for scr refresh
                progressBar_out4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progressBar_out4, 'tStopRefresh')  # time at next scr refresh
                progressBar_out4.setAutoDraw(False)
        
        # *progressBar_in4* updates
        if progressBar_in4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            progressBar_in4.frameNStart = frameN  # exact frame index
            progressBar_in4.tStart = t  # local t and not account for scr refresh
            progressBar_in4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progressBar_in4, 'tStartRefresh')  # time at next scr refresh
            progressBar_in4.setAutoDraw(True)
        if progressBar_in4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progressBar_in4.tStartRefresh + ITI_sec-frameTolerance:
                # keep track of stop time/frame for later
                progressBar_in4.tStop = t  # not accounting for scr refresh
                progressBar_in4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progressBar_in4, 'tStopRefresh')  # time at next scr refresh
                progressBar_in4.setAutoDraw(False)
        
        # *progress_text4* updates
        if progress_text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progress_text4.frameNStart = frameN  # exact frame index
            progress_text4.tStart = t  # local t and not account for scr refresh
            progress_text4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_text4, 'tStartRefresh')  # time at next scr refresh
            progress_text4.setAutoDraw(True)
        if progress_text4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > progress_text4.tStartRefresh + ITI_sec-frameTolerance:
                # keep track of stop time/frame for later
                progress_text4.tStop = t  # not accounting for scr refresh
                progress_text4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progress_text4, 'tStopRefresh')  # time at next scr refresh
                progress_text4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mainLoop.addData('blank.started', blank.tStartRefresh)
    mainLoop.addData('blank.stopped', blank.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "block_transition"-------
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData("fixDuration", fixDuration)
    thisExp.addData("Correct", Correct)
    thisExp.addData("SWITCH", SWITCH)
    thisExp.addData("ID_port", ID_port)
    thisExp.addData("IDChoice", IDChoice)
    thisExp.addData("RT", RT)
    thisExp.addData("Nblock", Nblock)
    thisExp.addData("Counter_Complete", Counter_Complete)
    thisExp.addData("Counter_Correct", Counter_Correct)
    thisExp.addData("Counter_Error", Counter_Error)
    print("#trial = ",Counter_Complete,",#trial_switch = ",Ntrial_switch)
    print("Ncorrect =",Ncorrect)
    print("============================")
    # keep track of which components have finished
    block_transitionComponents = []
    for thisComponent in block_transitionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block_transitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block_transition"-------
    while continueRoutine:
        # get current time
        t = block_transitionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block_transitionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_transitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_transition"-------
    for thisComponent in block_transitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SWITCH = 0
    if not(Correct):
        Ncorrect=0
    else:
        Ncorrect= Ncorrect + Correct
        if (Ncorrect==minNcorrect) and (NewBlock):
           Ntrial_switch = Counter_Complete + np.random.randint(maxNtrial_after)+1
           NewBlock=False
           SWITCH = 1
    
    if (Counter_Complete  == Ntrial_switch) and not(NewBlock):
        Nblock = Nblock+1;
        ID_port = (ID_port + np.random.randint(Nport-1) +1)%Nport
        NewBlock = True
        print("****New Block****")
        thisExp.saveAsWideText(savefilename +'.csv',fileCollisionMethod='overwrite')
        thisExp.saveAsPickle(savefilename,fileCollisionMethod='overwrite')
    
    perc_finish = np.ceil(100*mainLoop.thisRepN/Total_Ntrials);
    BarLength = 0.2*perc_finish/100;
    BarCenter = 0.1 + BarLength/2;
    progress_msg = str(perc_finish) + "%";
    # the Routine "block_transition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed Total_Ntrials repeats of 'mainLoop'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
reward_rate = np.round(reward_rate*100)
codemsg = "SurveyCode: " + str(int(reward_rate))
# setup some python lists for storing info about the mouse_end
gotValidClick = False  # until a click is received
thank.setText(codemsg)
# keep track of which components have finished
endComponents = [mouse_end, thank, text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *mouse_end* updates
    if mouse_end.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_end.frameNStart = frameN  # exact frame index
        mouse_end.tStart = t  # local t and not account for scr refresh
        mouse_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_end, 'tStartRefresh')  # time at next scr refresh
        mouse_end.status = STARTED
        prevButtonState = mouse_end.getPressed()  # if button is down already this ISN'T a new click
    if mouse_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mouse_end.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            mouse_end.tStop = t  # not accounting for scr refresh
            mouse_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mouse_end, 'tStopRefresh')  # time at next scr refresh
            mouse_end.status = FINISHED
    if mouse_end.status == STARTED:  # only update if started and not finished!
        buttons = mouse_end.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # *thank* updates
    if thank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank.frameNStart = frameN  # exact frame index
        thank.tStart = t  # local t and not account for scr refresh
        thank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank, 'tStartRefresh')  # time at next scr refresh
        thank.setAutoDraw(True)
    if thank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            thank.tStop = t  # not accounting for scr refresh
            thank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thank, 'tStopRefresh')  # time at next scr refresh
            thank.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_end.getPos()
buttons = mouse_end.getPressed()
thisExp.addData('mouse_end.x', x)
thisExp.addData('mouse_end.y', y)
thisExp.addData('mouse_end.leftButton', buttons[0])
thisExp.addData('mouse_end.midButton', buttons[1])
thisExp.addData('mouse_end.rightButton', buttons[2])
thisExp.addData('mouse_end.started', mouse_end.tStart)
thisExp.addData('mouse_end.stopped', mouse_end.tStop)
thisExp.nextEntry()
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
