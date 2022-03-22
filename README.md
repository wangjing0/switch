**An online gaming and pychophysics experiment that can collect various behavioral data 
(clicking, mouse tracking, eye gaze) upon consent of the experimentees.** [Try it yourself here!](https://run.pavlovia.org/jingwang.physics/switchbeta/html/?__pilotToken=3c59dc048e8850243be8079a5c74d079&__oauthToken=a651fabc8d3fd042327636d17a96e67d188f0e5caccb34034de68d20aeb500b7)

Interested in building one? Here is a mini tutorial.


* PsychoPy is a python based cross-platform package for running behavioral sciences
* Design backbone of experiment. *.psyexp in PsychoPy* 
 
  Flow> routines>components

  Details can be found in [Psychopy.org](https://psychopy.org/index.html)
* Test local python version of the experiment in the experiment runner. A new *_lastrun.py* is generated automatically at each run. Data and log will be saved locally in a data folder.
* Set a git project and sync with the repository on pavlovia.org
* Automatically compile to PsychoJS javascripts in the html folder, and run the JS version in any web browser in local debug mode. Keep all images or sound file in the same directory under /html/resources folder.
* Modify JS directly in code components, make sure python and JS in the code component were selected as both, not auto->JS. 
* Sync after every change made locally *.psyexp*. Two new *.js* will be automatically compiled, test run *.js* both locally and online
* Push it to your git repository, then run JS in Piloting or Running mode on pavlovia.org
* Data will be saved on the repository in the data folder. Pull back online data from the repository.
* Set the exp as Running mode in [pavlovia.org](https://pavlovia.org). Publish the task using generated [alias link](https://tinyurl.com/) for safety.

<p align="center">
  <img src="screenshot.png" height="500" >
</p>
