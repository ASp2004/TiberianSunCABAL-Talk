from sounddevice import play
import datetime as dt

import getopt, sys
from os import path
from pathlib import PureWindowsPath
import yaml

import tibsuncabal_talk
from tibsuncabal_talk.tibsuncabal import TibSunCabal
from tibsuncabal_talk.cli_progress import CliProgress


def main():
    path_dirname_config = path.normpath(path.dirname(__file__))
    if path.sep == '\\':
        path_dirname_config = PureWindowsPath(path_dirname_config).as_posix()
    path_dirname_config = path.join(path_dirname_config,'config.yaml')
    config_yaml = yaml.load(open(path_dirname_config,'r'), Loader=yaml.Loader)
    
    ready = True
    mix_to_aud = {'speech02': ['00-i012.aud', '00-i014.aud', '00-i024.aud', '00-i062.aud', '00-i064.aud', '00-i106.aud', '00-i286.aud', '01-n024.aud', '01-n128.aud', '01-n130.aud'],
                'e01vox01': ['01-n400.aud'],
                'sidecd02': ['nod-02.aud', 'nod-07b.aud']}
    for mix_name, mix_directory in config_yaml.items():
        if mix_directory is None or not path.exists(mix_directory):
            print("Directory for files from " + mix_name + ".mix not found")
            ready = ready and False
        else:
            for aud_file in mix_to_aud[mix_name]:
                aud_directory = path.join(mix_directory, "/" + aud_file)
                if not path.exists(aud_directory):
                    print("File " + aud_file + " could not be found in " + mix_name + " directory")
                    ready = ready and False
        
    if not ready:
        print("Files not found, please consult the readme about how to setup the files")
        exit(0)
               
    cabal = TibSunCabal()
    progress = CliProgress()

    print("Type the text you would like CABAL to speak")
    print("Leave blank and press enter to exit")

    try:
        while True:
            text = input("> ")
            if len(text) == 0:
                exit(0)
            else:
                audio = cabal.load_text(text, progress.update_progress)
                audio.export("./" + text + str(dt.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".wav", format='wav')
                play(audio.get_array_of_samples(), audio.frame_rate)

    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()
