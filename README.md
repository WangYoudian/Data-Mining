# Data-Mining
This is the assignment for Data Mining Project
### 2018/6/7
Today I solved the problem about [py2exe/cx_Freeze/pyinstaller](https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python "How to genetate exe file in python stuff……"). Before solving it finally, I tried different methods and websites, they are:
1.[py2exe](http://www.py2exe.org/index.cgi/Tutorial "Tutorial in using py2exe to distribute an exe.")
It needs to bundle some *dll files* with you exe. I'll take it as [liscence](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en "Microsoft.VC90.CRT and stuff"), apparently, with good luck, you can draw you foot on it somewhere [in your computer](#abc "Just type the version number you are fetching, such as 9.0.21022.8"). 'Cause the microsoft liscence is [prevailing](#abc "And it purchase github from June 4th, 2018")
One thing I need to warn, py2exe packages is not so friendly to the newst version for python, see [SorceForge](https://sourceforge.net/projects/py2exe/?source=directory "Py2exe.exe download"). There is only 2.7 version available. Therefore, there is a guy in the first [website](https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python) suggested using Cpython to get a better experience in deving.
2.[pyinstaller](https://pyinstaller.readthedocs.io/en/stable/index.html "How to generate an exe file in pyinstaller?")
And when you want to run you result. You need to go to [*dist* directory](#abc "Meanwhile there is a build directory")(which means distributable and contains the supporting files) to find the .exe.
3.[cx_Freeze](https://stackoverflow.com/questions/17798128/how-to--exe-file-in-python-using-cx-freeze "Go to this website and it's clear for all")
The good thing about this package is that when you run the setup.py, better put the script itself in the same directory with python.exe.
I don't know why, but it seems to be explained on stack-over-flow
The project's name, will just be the same as **name** below  
```python
setup(
    name = "hello",
    options = options,
    version = "0.0",
    description = 'This trail I hope it will work!',
    executables = executables
)

```
Actually, myself got this traceback:
```python
*** WARNING *** unable to create version resource
install pywin32 extensions first
writing zip file build\exe.win-amd64-3.6\lib\library.zip
执行python setup.py build程序的报错。
```
The second time when I run the PowerShell *using Shift+Right Click*,  it went away!
