from sounddevice import play
import datetime as dt

from tibsuncabal_talk.tibsuncabal import TibSunCabal
from tibsuncabal_talk.cli_progress import CliProgress


def main():
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
