from sounddevice import play
import datetime as dt

from os import path
from pathlib import PureWindowsPath
import yaml

from tibsuncabal_talk.tibsuncabal import TibSunCabal
from tibsuncabal_talk.cli_progress import CliProgress

mix_to_aud = {'speech02': ['00-i012.aud', '00-i014.aud', '00-i024.aud', '00-i062.aud', '00-i064.aud', '00-i106.aud', '00-i286.aud', '01-n024.aud', '01-n128.aud', '01-n130.aud'],
            'e01vox01': ['01-n400.aud'],
            'sidecd02': ['nod-02.aud', 'nod-07b.aud']}


def main():
    path_dirname_config = path.normpath(path.dirname(__file__))
    if path.sep == '\\':
        path_dirname_config = PureWindowsPath(path_dirname_config).as_posix()
    path_dirname_config = path.join(path_dirname_config,'config.yaml')
    config_yaml = yaml.load(open(path_dirname_config,'r'), Loader=yaml.Loader)
    
    ready = True
    for mix_name, mix_directory in config_yaml.items():
        if mix_directory is None or not path.exists(mix_directory):
            print("Directory for files from " + mix_name + ".mix not found")
            ready = ready and False
        else:
            directory_str = PureWindowsPath(mix_directory).as_posix()
            for aud_file in mix_to_aud[mix_name]:
                supposed_path = path.join(directory_str, aud_file)
                ready = ready and path.exists(supposed_path)
                if not path.exists(supposed_path):
                    print("File " + aud_file + " could not be found in " + mix_name + " directory")
                    ready = ready and False
        
    if ready:
        print("Files were found successfully. Enter 'C' or 'configure' if you would like to configure directories again. Any other input will start TiberianSunCABAL_Talk.")
        
        configure_option = input("> ")
        configure_option = configure_option.lower()
        if configure_option == 'c' or configure_option[:3] == 'con':
            configure()
    else:
        print("Files not found, please consult the readme about how to setup the files")
        configure()
               
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


def configure():
    path_dirname_config = path.normpath(path.dirname(__file__))
    if path.sep == '\\':
        path_dirname_config = PureWindowsPath(path_dirname_config).as_posix()
    path_dirname_config = path.join(path_dirname_config,'config.yaml')
    config_yaml = yaml.load(open(path_dirname_config,'r'), Loader=yaml.Loader)
    for mix_name, aud_files_list in mix_to_aud.items():
        if not (config_yaml[mix_name] is None):
            if path.exists(config_yaml[mix_name]):
                print(mix_name + " currently points to " + config_yaml[mix_name])
            else:
                print("The directory that " + mix_name + " once pointed to no longer exists")
        
        print("Please enter the directory for " + mix_name + ". Entering nothing will cancel the configuration process with no changes saved.")
        ready = False
        while not ready:
            ready = False
            directory_str = input("> ")
            if len(directory_str) == 0:
                exit(0)
            try:
                if directory_str is None or not path.exists(directory_str):
                    print("Directory path does not exists.")
                else:
                    directory_str = PureWindowsPath(directory_str).as_posix()
                    ready = True
                    for aud_file in aud_files_list:
                        supposed_path = path.join(directory_str, aud_file)
                        ready = ready and path.exists(supposed_path)
                        if not path.exists(supposed_path):
                            print(supposed_path + " not found in directory path")
                            
                    if ready:
                        print("All files found")
                        config_yaml[mix_name] = directory_str
                        
            except:
                print("Invalid directory")
                
    yaml.dump(config_yaml, open(path_dirname_config,'w'))
            
            
        

if __name__ == '__main__':
    main()
