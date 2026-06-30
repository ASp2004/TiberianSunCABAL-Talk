# Tiberian Sun CABAL - Talk

A currently unfinished fork of MorshuTalk intended to apply the logic proved in the original to CABAL from Tiberian Sun, played by Milton James.

This program works by converting the given text into phonemes with [g2p_en](https://pypi.org/project/g2p-en/), then
concatenates the segments of Morshu's audio where he speaks those phonemes.

## Requirements
Python 3.13+ (tested on Windows)
A copy of [Command & Conquer: Tiberian Sun](https://cnc-comm.com/tiberian-sun/downloads/the-game/installer) (released as freeware in 2010).
The [XCC Utilities](https://cnc-comm.com/command-and-conquer/downloads/modding-tools/XCC-utilities).

## Installation and Setup
### Python Package
Clone this repo and run the setup script:

    python setup.py install

This installs all the packages necessary for running MorshuTalk from the command-line. If you want to use the GUI, you
will also need to install PySide6. (It's not included by default because it's a slightly larger download.)

    pip install PySide6

### Linking Audio Files
Following the above link to install the XCC Utilities. Find XCC Mixer (not Mix Editor), use it to open TIBSUN.mix, and extract speech02.mix and sidecd02.mix. The file e01vox01.mix is also needed.

You will need to extract the following .aud files from each given archive to a corresponding folder:
#### speech02
* 00-i012.aud 
* 00-i014.aud
* 00-i024.aud
* 00-i062.aud
* 00-i064.aud
* 00-i106.aud
* 00-i286.aud
* 01-n024.aud
* 01-n128.aud
* 01-n130.aud

##### e01vox01
* 01-n400.aud

#### sidecd02
* nod-02.aud
* nod-07b.aud

## Running
### Python Package
Installing the package will add the command `tibsuncabal_talk`  to your command-line. If that command
don't work, you can run the modules with `python -m tibsuncabal_talk`.

Simply type whatever lines you want CABAL to speak, then he will talk. To exit, leave the line blank and hit enter.

## Building
1. Clone this repo.
2. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) and activate it.
3. Install the required packages with `pip install -r requirements.txt`
4. If you make changes to `mainwindow.ui`, update `ui_mainwindow.py` with:
```commandline
pyside6-uic morshutalkgui/ui/mainwindow.ui -o morshutalkgui/ui_mainwindow.py --from-imports
```
5. If you make changes to `res.qrc`, update `res_rc.py` with:
```commandline
pyside6-rcc morshutalkgui/res/res.qrc -o morshutalkgui/res_rc.py
```
6. Use `build` to create a distributable package:
    1. Install it with `pip install build`
    2. Run `python -m build`. A tar.gz and wheel package should be located in the `dist` folder.
7. Use cx_freeze to build an executable for Windows:
    1. Install it with `pip install cx_freeze`
    2. Run `python freeze_setup.py build`. The executable and many other files should be located in the `build` folder.
    3. Run `python clean_cx_freeze_build.py` to remove unnecessary files. (cx_freeze does a bad job at choosing what
       packages are necessary. This script removes 150+ MB of unused files.)

## License
[MIT License](LICENSE.txt)

This uses the following libraries:
* [g2p_en](https://pypi.org/project/g2p-en/)
* [NumPy](https://numpy.org/)
* [Pydub](http://pydub.com/)
* [sounddevice](https://pypi.org/project/sounddevice/)
* [PySide 6 (Qt for Python)](https://wiki.qt.io/Qt_for_Python)
