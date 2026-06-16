import io
from os import path
import numpy as np
import random
import warnings
from pydub import AudioSegment
from typing import List, Tuple, Callable, Literal

from morshutalk.g2p import G2pProgress

import yaml

g2p = G2pProgress()

config_yaml = yaml.load(open('../config.yaml','r'))

filepath = path.join(config_yaml['speech02'], '00-i012.aud')
battle_control_offline = AudioSegment.from_file(filepath)

morshu_wav_fp = path.join(path.dirname(__file__), 'morshu.wav')
morshu_wav = AudioSegment.from_wav(morshu_wav_fp)

# typos in comments are intentional

# Record that contains each recognizable phoneme in the morshu audio file,
# along with the time that phoneme ends in milliseconds, and the priority (how the phoneme sounds compared to others).
battle_control_offline_rec = np.rec.array([
    ('B', 41, 2), ('AE', 205, 1), ('L', 351, 2), #BA'L
    ('K', 393, 2), ('AA', 470, 0), ('CH', 596, 1), ('R', 664, 1), ('AO', 840, 1), ('L', 959, 0), #COCHROL , AA should be AX if it were in cmu phoneme set
    ('O', 1150, 2), ('F', 1281, 1), ('L', 1327, 1), ('N', 1758, 1), #OFFLINE
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['speech02'], '00-i064.aud')
unable_to_comply_building_in_progress = AudioSegment.from_file(filepath)

unable_to_comply_building_in_progress_rec = np.rec.array([
    ('AH', 95, 0), ('N', 198, 2), ('EY', 368, 1), ('B', 466, 1), ('L', 590, 1), #UNABLE
    ('T', 627, 2), ('UW', 723, 1), #TO
    ('K', 756, 1), ('AA', 841, 0), ('M', 920, 0), ('P', 1026, 1), ('L', 1047, 0), ('AY', 1455, 2), #COMPLY
    ('B', 1485, 1), ('IH', 1538, 2), ('L', 1688, 0), ('D', 1800, 0), ('IH', 1839, 0), ('N', 1855, 0), #BUILDING
    ('IH', 1904, 0), ('N', 2068, 0), #IN
    ('P', 2137, 2), ('R', 2168, 1), ('AA', 2305, 2), ('G', 2424, 1), ('R', 2480, 0), ('EH', 2549, 2), ('S', 2777, 2), #PROGRESS
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['speech02'], '00-i106.aud')
qauternery_objective_achieved = AudioSegment.from_file(filepath)

qauternery_objective_achieved_rec = np.rec.array([
    ('K', 77, 2), ('W', 144, 2), ('AA', 272, 2), ('T', 371, 1), ('ER', 470, 1),('EH', 535, 2),('R', 569, 1),('IY', 718, 1), #QAUTER-ERY
    ('AA', 778, 0), ('', 795, 0), ('J', 871, 2), ('EH', 1081, 1), ('K', 1105, 1),('T', 1140, 2),('IH', 1204, 1),('V', 1300, 2), #OBJECTIVE
    ('AE', 1340, 1), ('CH', 1440, 2), ('IY', 1642, 2), ('V', 1872, 1), ('T', 1948, 1), #ACHIEVED
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['speech02'], '00-i024.aud')
low_power = AudioSegment.from_file(filepath)

low_power_rec = np.rec.array([
    ('L', 100, 2), ('0W', 347, 2),('', 390, 1), #LOW
    ('P', 455, 2), ('AW', 644, 2), ('W', 704, 1), ('ER', 843, 1), #POWER
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['sidecd02'], 'nod-02.aud')
nod02 = AudioSegment.from_file(filepath)

nod02_rec = np.rec.array([
    ('H', 37, 1), ('AH', 153, 0),('S', 279, 2),('AE', 519, 2),('N', 643, 2),('', 648, 0), #HASSAN
    ('C', 455, 2), ('AA', 737, 2), ('M', 830, 1), ('', 838, 1), ('UH', 946, 1), ('N', 976, 1), ('IH', 1081, 2), ('K', 1139, 2), ('EY', 1320, 2), ('T', 1326, 0), ('S', 1391, 1), #COMMUNICATES # there is a small Y between M and UH
    ('', 1412, 2),('T', 1458, 2), ('UW', 1559, 2), #TO
    ('DH', 1609, 2), ('UW', 1710, 1), #THE
    ('B', 1740, 2), ('R', 1752, 1), ('AH', 1883, 1), ('DH', 1914, 1), ('ER', 2018, 1), ('HH', 2048, 1), ('UH', 2061, 2), ('D', 2120, 1), #BROTHERHOOD
    ('TH', 2270, 1), ('R', 2325, 2), ('UW', 2361, 2), #THROUGH
    ('AH', 2423, 0),  #A
    ('N', 2538, 2), ('AH', 2688, 1),#NEAR
    ('B', 2753, 2), ('AY', 2928, 2), #BY
    ('', 2960, 1),
    ('T', 3026, 2), ('IY', 3170, 2),('V', 3258, 2), ('IY', 3367, 2), #TV
    ('S', 3500, 2),('T', 3565, 1),('EY', 3637, 2),('SH', 3794, 2),('AH', 3806, 2), ('N', 3923, 1), #STATION
    ('', 4297, 2),
    ('W', 4365, 2), ('IH', 4488, 2),('DH', 4634, 2), #WITH
    ('DH', 4701, 2), ('UW', 4767, 1), #THE
    ('B', 4779, 0), ('R', 4816, 1), ('AH', 4914, 1), ('DH', 4951, 2), ('ER', 5043, 1), ('HH', 5059, 1), ('UH', 5150, 2), ('D', 5180, 1), #BROTHERHOOD
    ('IH', 5242, 2), ('N', 5324, 1),('', 5336, 1), #IN
    ('K', 5431, 2), ('EY', 5561, 2),('', 5572, 0),('AA', 5736, 2),('S', 5895, 1), #CHAOS # SMALL Y BETWEEN EY AND AA
    ('', 6254, 1), #*BREATH*
    ('DH', 6325, 1),('UW', 6407, 1), ('AA', 6521, 1),('P', 6553, 1), #THE-OP
    ('P', 6610, 1),('AO', 6723, 1),('T', 6760, 1),('UH', 6951, 2),('N', 7041, 2),('IH', 7065, 2),('IY', 7202, 1), #-PORTUNI-Y
    ('', 1412, 2),('T', 1458, 2), ('UW', 1559, 2), #TO
    ('D', 7304, 1),('IH', 7381, 2),('V', 7450, 2),('AY', 7751, 2),('D', 7800, 2), #DIVIDE
    ('H', 7829, 1), ('AH', 7900, 1),('S', 8006, 2),('AE', 8119, 2),('N', 8215, 2), #HASSAN
    ('F', 8282, 1), ('R', 8322, 0), ('M', 8376, 2), #FR-M
    ('H', 8408, 1), ('I', 8412, 2), ('S', 8556, 2), #HIS
    ('F', 8594, 1), ('AH', 8679, 2), ('L', 8790, 1), ('OW', 8853, 2),('ER', 8902, 2), ('S', 8994, 1), #FOLLOWER
    ('', 9229, 1), #*BREATH*
    ('P', 9261, 1), ('R', 2292, 2),  ('EH', 9342, 2),  ('Z', 9417, 2),  ('EH', 9497, 2), ('N', 9579, 2), ('S', 9678, 2),('IH', 9716, 0), ('T', 9752, 1), #PRESEN-S IT-
    ('S', 9876, 1),('EH', 9919, 1), ('L', 10041, 2), ('F', 10190, 2), #-SELF
    ('', 10670, 1), #*PAUSE*
    ('K', 10712, 2), ('AE', 10935, 2), ('P', 10954, 2), ('CH', 11072, 2),('ER', 11173, 2), #CAPCHURE
    ('DH', 11201, 2), ('UW', 11293, 1), #THE
    ('', 11314, 1), #*PAUSE*
    ('T', 11370, 2), ('IY', 11466, 2),('V', 11560, 2), ('IY', 11664, 2), #TV
    ('S', 11794, 2),('T', 11820, 1),('EY', 11922, 2),('SH', 12080, 2),('AH', 12092, 2), ('N', 12197, 1), #STATION
    ('', 12322, 1), #*BREATH*
    ('AE', 12473, 1), ('N', 12510, 1), ('', 12527, 2), #AN- # D after N is not strong enough
    ('DH', 12568, 1), ('OW', 12752, 2), ('Z', 12814, 2), #THOSE
    ('W', 12568, 2), ('AA', 12994, 2), ('N', 13063, 2), ('S', 13190, 2), #ONCE
    ('L', 13292, 1), ('OY', 13480, 2), ('AE', 13506, 0), ('L', 13580, 2),('', 13596, 2), #LOYAL
    ('T', 13639, 2), ('UH', 13727, 0), ('', 13738, 0), #TO
    ('K', 13792, 2), ('EY', 13876, 2), ('N', 14017, 2), ('S', 14125, 2), #KANE'S
    ('T', 14154, 2), ('EH', 14235, 0), ('K', 14380, 0), #TECH
    ('T', 14154, 2), ('EH', 14235, 0), ('K', 14380, 0), #NOLOGY
], names=('phoneme', 'timing', 'priority'))



# substitutes to phonemes that morshu doesn't say (some of these are tentative
similar_phonemes = {
    'AW': ['AE', 'UW'],
    'DH': ['D'],
    'EY': ['EH', 'IY'],
    'JH': ['CH'],
    'SH': ['CH'],
    'TH': ['D'],
    'ZH': ['CH'],
}


class Morshu:
    def __init__(self):
        self.input_str = ""
        self.input_phonemes = []

        self.stop_chars = '.,?!:;()\n'
        """
        Characters that represent a stop in the audio. If any of these characters appear in the text, silence of length
        stop_length will be added.
        """

        self.space_length = 20
        self.stop_length = 100

        self.use_phoneme_priority = True

        self.out_audio = AudioSegment.empty()
        """The audio segment generated by load_audio()"""

        self.audio_segment_timings = np.rec.array((0, 0), names=('output', 'morshu'))
        """
        Record of segment timings in the output audio. Each entry represents the time that a new morshu segment begins.
        
        The first index in each entry (named 'output') is the time in milliseconds when a new morshu segment begins.
        The second index (named 'morshu') is the time when the segment starts in the morshu audio.
        
        Example: If this record contains the entry (2000, 1895), that means at 2 seconds into the output audio, the
        morshu segment that begins at 1.895 seconds will be played (when morshu says 'B' in 'bombs').
        """

        self.canceled = False

    def cancel(self):
        g2p.cancel()
        self.canceled = True

    def load_text(self, text: str = None, progress_callback: Callable[[int, int, int], None] = None) \
            -> AudioSegment | Literal[False]:
        """
        Generate audio from the given text. The input_str, input_phonemes, and audio_segment_timings variables are also
        updated.

        :param text: The text to use. If omitted, the input_str variable is used instead.

        :param progress_callback: An optional callback function to report progress for stitching the audio segments.
        The first argument is the current major step (0 = g2p, 1 = audio), the second argument is the current minor step
        (word or phoneme currently on), and the last argument is the total minor steps.

        :return: The generated audio. It's also stored in the out_audio variable.
        """
        self.canceled = False

        if progress_callback is None:
            # dummy function just so I don't have to check if progress_callback exists every time I call it
            progress_callback: Callable[[int, int, int], None] = lambda major_step, minor_step, minor_total: None

        if text is None:
            text = self.input_str
        self.input_str = text
        text = text.replace('\n', ',,,')

        phonemes = g2p.run_with_progress(text, lambda step, total: progress_callback(0, step, total))
        if g2p.cancelled:
            return False

        progress_step = 0
        progress_total = len(phonemes)

        # output audio
        output = AudioSegment.empty().set_frame_rate(morshu_wav.frame_rate)

        # milliseconds marking each time a new morshu audio segment is used
        audio_out_millis = []

        # milliseconds marking the beginning of each segment in from the morshu audio
        audio_morshu_millis = []

        # segment of multiple phonemes in one word (phonemes between pauses)
        phoneme_segment = []
        while len(phonemes) > 0:
            if self.canceled:
                return False

            progress_callback(1, progress_step, progress_total)
            progress_step += 1

            p = phonemes.pop(0)
            if p in g2p.phonemes:
                phoneme_segment.append(p)
            if p not in g2p.phonemes or len(phonemes) == 0:
                output = self.append_best_morshu_phoneme_segment(output, phoneme_segment, audio_out_millis,
                                                                 audio_morshu_millis)
                phoneme_segment = []
            if p == ' ':
                output = self.append_audio_segment(output, AudioSegment.silent(self.space_length), -1, audio_out_millis,
                                                   audio_morshu_millis)
            elif p in self.stop_chars:
                output = self.append_audio_segment(output, AudioSegment.silent(self.stop_length), -1, audio_out_millis,
                                                   audio_morshu_millis)

        if len(output) == 0:
            warnings.warn('returned audio segment is empty', UserWarning)
            self.audio_segment_timings = np.rec.array((0, 0), names=('output', 'morshu'))
        else:
            self.audio_segment_timings = np.rec.array(tuple(zip(audio_out_millis, audio_morshu_millis)),
                                                      names=('output', 'morshu'))

        progress_callback(1, progress_total, progress_total)

        self.out_audio = output
        return output

    def get_frame_idx_from_millis(self, millis: int) -> int:
        """
        Get the morshu frame from the given time in milliseconds
        :param millis: Time in the output audio in milliseconds.
        :return: The morshu frame index that occurs at that time in the generated audio. The morshu video is 10 fps.
        """
        if len(self.out_audio) == 0:
            return 0

        millis = int(millis)
        idx = np.argmin(self.audio_segment_timings['output'] <= millis) - 1

        output_segment_start, morshu_segment_start = self.audio_segment_timings[idx]
        if morshu_segment_start == -1:
            return -1

        morshu_frame = (morshu_segment_start + (millis - output_segment_start)) // 100  # 10 fps, 1 frame per 100 millis
        return morshu_frame

    @staticmethod
    def substitute_similar_phonemes(phonemes: List[str]):
        """
        Parse through a list of phonemes and replace them if necessary.

        The replacement phonemes are stored in the global similar_phonemes dictionary. These are phonemes that Morshu
        doesn't say in his two lines of dialog. These phonemes may sound slightly different than expected, and may be
        updated to be more accurate later.

        The emphasis number at the end of some vowel phonemes are removed to simplify things.

        :param phonemes: A list of phonemes to parse through.

        :return: A new list of phonemes.
        """
        i = 0
        while i < len(phonemes):
            # remove emphasis number
            if phonemes[i].endswith('0') or phonemes[i].endswith('1') or phonemes[i].endswith('2'):
                phonemes[i] = phonemes[i][:len(phonemes[i]) - 1]

            if phonemes[i] in similar_phonemes.keys():
                phonemes = phonemes[0:i] + similar_phonemes[phonemes[i]] + phonemes[i + 1:]
            i += 1
        return phonemes

    @staticmethod
    def append_audio_segment(audio_out: AudioSegment, audio_segment: AudioSegment, morshu_millis_start: int,
                             audio_out_millis: List[int], audio_morshu_millis: List[int]) -> AudioSegment:
        """
        Helper function to append one audio segment to another and update several variables at the same time.

        :param audio_out: The full audio to append to.

        :param audio_segment: The audio segment that will be appended.

        :param morshu_millis_start: The time in milliseconds that the audio segment begins in the morshu audio. Use -1
        if this audio doesn't appear in the Morshu audio (like if it's silence).

        :param audio_out_millis: A list of milliseconds representing when new segments begin in the output audio.

        :param audio_morshu_millis: A list of milliseconds representing when the segment begins in the morshu audio.

        :return: audio_out with audio_segment appended.
        """
        audio_out_millis.append(len(audio_out))
        audio_morshu_millis.append(morshu_millis_start)
        audio_out += audio_segment
        return audio_out

    @staticmethod
    def get_phoneme_sequence_occurrences(phonemes: List[str]) -> List[Tuple[int, int]]:
        """
        Get all occurrences of a given phoneme segment in the morshu audio.
        :return: List of tuples containing (start_millis, end_millis)
        """
        occurrences = []
        for i in range(len(morshu_rec) - len(phonemes)):
            if (morshu_rec['phoneme'][i:i + len(phonemes)] == phonemes).all():
                start = morshu_rec['timing'][i - 1]
                end = morshu_rec['timing'][i + len(phonemes) - 1]
                occurrences.append((start, end))
        return occurrences

    def get_best_morshu_single_phoneme(self, phoneme: str, preceding: str = "", succeeding: str = "") \
            -> Tuple[AudioSegment, int]:
        """
        Find the best morshu audio segment of the given phoneme.

        This compares the given surrounding phonemes with the phonemes in the morshu audio to determine the best one.
        Segments that match the same preceding or succeeding phoneme will be given the highest priority, and moderate
        priority is given if the phonemes both contain vowels. If two segments have the same priority, a random one is
        chosen.

        For example, if we're looking for the phoneme 'K' with nothing before it and 'IH' after it, the 'K' in either
        "can't" or "come" will be chosen instead of "credit", because the preceding phoneme matches (nothing) and the
        succeeding phoneme contains a vowel, so it's close enough.

        :param phoneme: The phoneme to search for.

        :param preceding: The phoneme that comes before the searching phoneme.

        :param succeeding: The phoneme that comes after the searching phoneme.

        :return: A tuple containing the audio segment and the time that the segment starts in the morshu audio
        """
        # list of phoneme indices of the highest priority
        best_indices = []
        phoneme_indices = np.where(morshu_rec['phoneme'] == phoneme)[0]
        if len(phoneme_indices) == 0:
            return AudioSegment.empty(), 0

        highest_priority = 0
        for i in phoneme_indices:
            # priorities for preceding and succeeding phonemes:
            # exact match: 10
            # compared phonemes both contain vowels: 5
            # no match: 0
            # starting priority is obtained from morshu_rec
            morshu_preceding = morshu_rec['phoneme'][i - 1]

            priority = morshu_rec['priority'][i] if self.use_phoneme_priority else 0
            if morshu_preceding == preceding:
                priority += 10
            # check both phonemes for any vowel
            elif any(c in morshu_preceding for c in "AEIOU") and any(c in preceding for c in "AEIOU"):
                priority += 5

            # check succeeding phonemes
            morshu_succeeding = morshu_rec['phoneme'][i + 1]
            if morshu_succeeding == succeeding:
                priority += 10
            # check both phonemes for any vowel
            elif any(c in morshu_succeeding for c in "AEIOU") and any(c in succeeding for c in "AEIOU"):
                priority += 1

            if priority < highest_priority:
                continue
            if priority > highest_priority:
                highest_priority = priority
                best_indices = []
            best_indices.append(i)

        index = random.choice(best_indices)
        segment = morshu_wav[morshu_rec['timing'][index - 1]: morshu_rec['timing'][index]]
        return segment, morshu_rec['timing'][index - 1]

    def append_best_morshu_phoneme_segment(self, output: AudioSegment, phonemes: List[str],
                                           audio_out_millis: List[int] = None,
                                           audio_morshu_millis: List[int] = None) -> AudioSegment:
        """
        Search for a phoneme segment that appears in the morshu audio, and append it to the given audio output. If a
        segment more than 1 length can't be found, get_best_morshu_single_phoneme will be used to find the best one.

        :param output: The audio to append the best segment to.

        :param phonemes: The phoneme segment to search for.

        :param audio_out_millis: A list of milliseconds representing when new segments begin in the output audio.

        :param audio_morshu_millis: A list of milliseconds representing when the segment begins in the morshu audio.

        :return: The audio segment with the new segment appended to it.
        """
        phonemes = Morshu.substitute_similar_phonemes(phonemes)
        if len(phonemes) == 1:
            segment, start = self.get_best_morshu_single_phoneme(phonemes[0])
            return Morshu.append_audio_segment(output, segment, start, audio_out_millis, audio_morshu_millis)

        # preceding and succeeding phonemes are used if we need to search for a single phoneme
        preceding = ""

        # full_segment = AudioSegment.empty()
        while len(phonemes) > 0:
            sequence_length = 1
            segment = AudioSegment.empty()

            start = 0
            while sequence_length <= len(phonemes):
                occurrences = Morshu.get_phoneme_sequence_occurrences(phonemes[:sequence_length])
                if len(occurrences) == 0:
                    break
                start, end = random.choice(occurrences)
                segment = morshu_wav[start:end]
                sequence_length += 1
            sequence_length -= 1

            # find the best single phoneme if a longer segment wasn't found
            if sequence_length == 1:
                if sequence_length + 1 < len(phonemes):
                    succeeding = phonemes[sequence_length + 1]
                else:
                    succeeding = ""
                segment, start = self.get_best_morshu_single_phoneme(phonemes[0], preceding, succeeding)

            output = Morshu.append_audio_segment(output, segment, start, audio_out_millis, audio_morshu_millis)

            preceding = phonemes[sequence_length - 1]
            del phonemes[:sequence_length]

        return output
