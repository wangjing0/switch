# switch
An online gaming and pychophysics experiment, that can collect various behavior data 
(clicking, mouse tracking, eye gaze tracking) upon consent of the experimentees.

[Try it yourself here!]<https://run.pavlovia.org/jingwang.physics/switchbeta/html/?__pilotToken=3c59dc048e8850243be8079a5c74d079&__oauthToken=a651fabc8d3fd042327636d17a96e67d188f0e5caccb34034de68d20aeb500b7>

Here is a mini tutorial

Design backbone of experiment. *.psyexp in PsychoPy
  Flow> routines>components, 
Run local python version of the experiment in the experiment runner. A new *_lastrun.py is generated automatically at each run. Data and log saved locally in a data folder
Set a git project and sync with the repository on pavlovia.org
Automatically compile to PsychoJS javascripts in the html folder, and run the JS version in any web browser in local debug mode. Keep all images or sound file in the same directory under /html/resources folder
Modify JS directly in code components, make sure python and JS in the code component were selected as both, not auto->JS. 
Sync after every change made locally *.psyexp. Two new *.js will be automatically compiled, test run *.js both locally and online
Push to your git repository, then run JS in Piloting or Running mode on pavlovia.org
Data will be saved on the repository in the data folder. Pull online data from the repository.
Set the exp as running mode in pavlovia.org. Publish the task using generated alias link at https://tinyurl.com/
