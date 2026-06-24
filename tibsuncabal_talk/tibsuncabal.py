import io
from os import path
import numpy as np
import random
import warnings
from pydub import AudioSegment
from typing import List, Tuple, Callable, Literal

from sounddevice import play #TODO remove testing element

from tibsuncabal_talk.g2p import G2pProgress

import yaml

g2p = G2pProgress()

path_dirname_config = path.normpath(path.join(path.dirname(__file__), '..'))
path_dirname_config = path.join(path_dirname_config,'config.yaml')
config_yaml = yaml.load(open(path_dirname_config,'r'))

filepath = path.join(config_yaml['speech02'], '00-i012.aud')
battle_control_offline = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

# morshu_wav_fp = path.join(path.dirname(__file__), 'morshu.wav')
# morshu_wav = AudioSegment.from_wav(morshu_wav_fp)

# typos in comments are intentional

# Record that contains each recognizable phoneme in the .aud audio files,
# along with the time that phoneme ends in milliseconds, and the priority (how the phoneme sounds compared to others).
battle_control_offline_rec = np.rec.array([
    ('B', 35, 2), ('AE', 173, 1), ('', 210, 0), ('L', 366, 2), #BA-L
    ('K', 381, 2), ('AH', 412, 0), ('N', 503, 2), ('CH', 596, 1), ('R', 635, 1), ('AO', 855, 1), ('', 959, 0), #CUHNCHRO- # LAST L DOES NOT SOUND GOOD AS ITS OWN PHONEME 
    ('O', 1134, 2), ('F', 1249, 1), ('L', 1309, 1),('AY', 1669, 1), ('', 1766, 1),('', 1771, 1), #OFFLI-
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['speech02'], '00-i064.aud')
unable_to_comply_building_in_progress = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

unable_to_comply_building_in_progress_rec = np.rec.array([
    ('AH', 95, 0), ('N', 198, 2), ('EY', 368, 1), ('B', 466, 1), ('L', 590, 1), #UNABLE
    ('T', 627, 2), ('UW', 723, 1), #TO
    ('K', 756, 1), ('AA', 841, 0), ('', 920, 0), ('P', 1026, 1), ('', 1047, 0), ('AY', 1455, 2), #CO-P-Y
    ('B', 1485, 1), ('IH', 1538, 2), ('', 1688, 0), ('', 1800, 0), ('IH', 1839, 0), ('', 1855, 0), #BUI-----
    ('IH', 1904, 0), ('', 2068, 0), #IN
    ('P', 2137, 2), ('R', 2168, 1), ('AA', 2305, 2), ('G', 2424, 1), ('', 2480, 0), ('EH', 2549, 2), ('S', 2777, 2),('', 2796, 1), #PROG-ESS
], names=('phoneme', 'timing', 'priority'))



filepath = path.join(config_yaml['speech02'], '00-i106.aud')
qauternery_objective_achieved = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

qauternery_objective_achieved_rec = np.rec.array([
    ('K', 61, 2), ('W', 119, 2), ('AA', 244, 2), ('T', 268, 1), ('', 353, 1),('EH', 506, 2),('R', 544, 1),('IY', 667, 1), #QAUTER-ERY
    ('AA', 689, 0), ('', 795, 0), ('JH', 866, 2), ('EH', 1040, 1),('', 1081, 1), ('K', 1105, 1),('T', 1140, 2),('IH', 1188, 1),('V', 1226, 2), #OBJECTIVE
    ('AH', 1306, 1), ('CH', 1436, 2), ('IY', 1766, 2), ('V', 1837, 1),('', 1873, 1), ('T', 1929, 1),('', 1947, 1), #UHCHIEVED
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['speech02'], '00-i024.aud')
low_power = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

low_power_rec = np.rec.array([
    ('L', 100, 2), ('0W', 347, 2),('', 390, 1), #LOW
    ('P', 455, 2), ('AW', 644, 2), ('W', 704, 1), ('ER', 843, 1),('', 846, 1), #POWER
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['speech02'], '00-i062.aud')
training = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

training_rec = np.rec.array([
    ('', 11, 1),('T', 104, 2), ('R', 144, 2),('EY', 341, 2),('', 391, 1),('NG', 613, 2),('', 633, 1), 
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['speech02'], '00-i014.aud')
building_infiltrated = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

building_infiltrated_rec = np.rec.array([
    ('', 14, 1),('B', 140, 2), ('IH', 202, 2),('L', 349, 2),('D', 391, 1),('IH', 518, 2),('NG', 701, 2), #BUILDING
    ('IH', 768, 1),('N', 897, 2), ('F', 988, 2),('AH', 1047, 2),('L', 1133, 1),('CH', 1227, 2),('', 1242, 0),('EY', 1325, 2),('T', 1403, 1),('ED', 1467, 1),('T', 1597, 1),('', 1622, 1), #INFILT-ATED
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['speech02'], '00-i286.aud')
you_have_lost = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

you_have_lost_rec = np.rec.array([
    ('Y', 93, 2), ('UW', 344, 2), #YOU
    ('HH', 402, 2), ('AE', 523, 2),('V', 601, 2), #HAVE
    ('L', 676, 2), ('AA', 973, 2), ('S', 1205, 2), ('T', 1345, 2),('', 1403, 1), #LOST
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['speech02'], '01-n024.aud')
destroy_the_remainder_of_hassans_guard = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

destroy_the_remainder_of_hassans_guard_rec = np.rec.array([
    ('D', 38, 2), ('EH', 95, 2),('S', 308, 2),('T', 346, 2),('R', 389, 2),('OY', 678, 2), #YOU
    ('DH', 689, 2), ('AH', 791, 2),('R', 801, 2),('AH', 886, 2),('M', 941, 2),('EY', 1060, 2),('N', 1179, 2), #THE REMAIN-
    ('D', 1197, 2), ('AH', 1365, 2),#DER
    ('AH', 1476, 2),  #O- # THE F SOUND ISN'T CLEAR OR USEFUL
    ('H', 1556, 2), ('AH', 1637, 2), ('S', 1755, 2), ('', 1904, 2), ('N', 1967, 2), ('Z', 2100, 2),#HASSANS # SECOND A DOES NOT FIT NEATLY INTO CMU
    ('G', 2144, 2), ('', 2481, 2), ('', 2552, 2), #G-RD # sound between g and d does not fit neatly into cmu, D is too quiet to be useful
    ('', 2602, 1), 
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['speech02'], '01-n024.aud')
tunnel_secure_mcv_en_route = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

tunnel_secure_mcv_en_route_rec = np.rec.array([
    ('T', 33, 2), ('AH', 151, 2),('N', 159, 2),('', 346, 2),('', 265, 2),#TUN-- # LAST TWO PHONEMES HERE HAVE A TONE THAT DOES NOT FIT WITH THE REST OF THE DIALOG
    ('', 360, 2), ('', 473, 2),('K', 515, 2),('', 538, 2),('Y', 575, 2),('AO', 844, 2), #S-CURE # EH HAS A TONE THAT STRECHES THEM BEYOND PURPOSE, there is a voiceless alveolar lateral fricative between K and Y
    ('EH', 962, 2), ('', 1024, 2), ('S', 1149, 2), ('IY', 1248, 2),('V', 1312, 2), ('IY', 1458, 2),#MCV # M sound is a bit ambigous
    ('AA', 1598, 2),('N', 1681, 2),  #EN
    ('R', 1721, 2), ('UH', 1918, 2), ('T', 2025, 2),#ROUTE
    ('', 2078, 1), 
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['speech02'], '01-n024.aud')
mutants_located = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

mutants_located_rec = np.rec.array([
    ('M', 52, 2),('Y', 127, 2), ('UW', 279, 2),('T', 341, 2),('AE', 374, 0),('N', 489, 2),('S', 607, 2),#TUN-- # LAST TWO PHONEMES HERE HAVE A TONE THAT DOES NOT FIT WITH THE REST OF THE DIALOG
    ('L', 690, 2), ('OW', 888, 2),('K', 984, 2),('EY', 1140, 2),('', 1176, 2),('', 1241, 2),('', 1364, 2), #S-CURE # EH HAS A TONE THAT STRECHES THEM BEYOND PURPOSE, there is a voiceless alveolar lateral fricative between K and Y
    ('', 1380, 1), 
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['e01vox01'], '01-n400.aud')
cabal_online = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

cabal_online_rec = np.rec.array([
    ('K', 44, 2),('AH', 161, 1), ('B', 262, 2),('AE', 594, 2),('L', 840, 0),('', 489, 2),#CABAL
    ('AA', 1119, 2), ('N', 1163, 2),('L', 1430, 2),('IY', 1607, 2),('', 1876, 2), #ONLI-
    ('', 1994, 1), 
], names=('phoneme', 'timing', 'priority'))

filepath = path.join(config_yaml['sidecd02'], 'nod-02.aud')
nod02 = AudioSegment.from_file(filepath, format="wsaud",codec="adpcm_ima_ws")

nod02_rec = np.rec.array([
    ('HH', 37, 1), ('AH', 153, 0),('S', 279, 2),('AE', 519, 2),('N', 643, 2),('', 648, 0), #HASSAN
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
    ('S', 3500, 2),('T', 3565, 1),('EY', 3637, 2),('SH', 3794, 2),('AH', 3806, 2), ('', 3923, 1), #STATION
    ('', 4297, 2),
    ('W', 4365, 2), ('IH', 4488, 2),('DH', 4634, 2), #WITH
    ('DH', 4701, 2), ('UW', 4767, 1), #THE
    ('', 4779, 0), ('R', 4816, 1), ('AH', 4914, 1), ('DH', 4951, 2), ('ER', 5043, 1), ('HH', 5059, 1), ('UH', 5150, 2), ('D', 5180, 1), #-ROTHERHOOD
    ('IH', 5242, 2), ('N', 5324, 1),('', 5336, 1), #IN
    ('K', 5431, 2), ('EY', 5561, 2),('', 5572, 0),('AA', 5736, 2),('S', 5895, 1), #CHAOS # SMALL Y BETWEEN EY AND AA
    ('BREATH', 6254, 1), #*BREATH*
    ('DH', 6325, 1),('UW', 6407, 1), ('AA', 6521, 1),('P', 6553, 1), #THE-OP
    ('P', 6610, 1),('AO', 6723, 1),('T', 6760, 1),('UH', 6951, 2),('N', 7041, 2),('IH', 7065, 2),('IY', 7202, 1), #-PORTUNI-Y
    ('', 1412, 2),('T', 1458, 2), ('UW', 1559, 2), #TO
    ('D', 7304, 1),('IH', 7381, 2),('V', 7450, 2),('AY', 7751, 2),('D', 7800, 2), #DIVIDE
    ('HH', 7829, 1), ('AH', 7900, 1),('S', 8006, 2),('AE', 8119, 2),('N', 8215, 2), #HASSAN
    ('F', 8282, 1), ('', 8322, 0), ('M', 8366, 2), #F--M
    ('HH', 8408, 1), ('I', 8412, 2), ('S', 8556, 2), #HIS
    ('F', 8594, 1), ('AH', 8679, 2), ('L', 8790, 1), ('OW', 8853, 2),('ER', 8902, 2), ('S', 8994, 1), #FOLLOWER
    ('BREATH', 9229, 1), #*BREATH*
    ('P', 9261, 1), ('R', 2292, 2),  ('EH', 9342, 2),  ('Z', 9417, 2),  ('EH', 9497, 2), ('N', 9579, 2), ('S', 9678, 2),('IH', 9716, 0), ('T', 9752, 1), #PRESEN-S IT-
    ('S', 9876, 1),('EH', 9919, 1), ('L', 10041, 2), ('', 10190, 0), #-SEL-
    ('', 10670, 1), #*PAUSE*
    ('K', 10712, 2), ('AE', 10935, 2), ('P', 10954, 2), ('CH', 11072, 2),('ER', 11173, 2), #CAPCHURE
    ('DH', 11201, 2), ('UW', 11293, 1), #THE
    ('', 11314, 1), #*PAUSE*
    ('T', 11370, 2), ('IY', 11466, 2),('V', 11560, 2), ('IY', 11664, 2), #TV
    ('S', 11794, 2),('T', 11820, 1),('EY', 11922, 2),('SH', 12080, 2),('AH', 12092, 2), ('N', 12197, 1), #STATION
    ('BREATH', 12322, 1), #*BREATH*
    ('AE', 12473, 1), ('N', 12510, 1), ('', 12527, 2), #AN- # D after N is not strong enough
    ('DH', 12568, 1), ('OW', 12752, 2), ('Z', 12814, 2), #THOSE
    ('W', 12568, 2), ('AA', 12994, 2), ('N', 13063, 2), ('S', 13190, 2), #ONCE
    ('L', 13292, 1), ('OY', 13480, 2), ('AE', 13506, 0), ('L', 13580, 2),('', 13596, 2), #LOYAL
    ('T', 13639, 2), ('UH', 13727, 0), ('', 13738, 0), #TO
    ('K', 13792, 2), ('EY', 13876, 2), ('N', 14017, 2), ('S', 14125, 2), #KANE'S
    ('T', 14154, 2), ('EH', 14235, 0), ('', 14380, 0), #TE--
    ('N', 14408, 2), ('AA', 14509, 0), ('', 14546, 0), ('IH', 14662, 1), ('JH', 14715, 2), ('IH', 14913, 0), #-NO-IHGIH # THE LAST IY MIXES WITH THE AA OF 'OF', WHOSE F IS ABSENT
    ('', 14963, 0), ('P', 15010, 2), ('IY', 15215, 0), ('', 15385, 0), #PEA--
    ('BREATH', 15590, 1), #*BREATH*
    ('W', 15633, 1), ('AH', 15705, 1), ('R', 15723, 2),('EH', 15852, 2), #WUH- RE # IH turned into AH, L IS ABSENT
    ('', 15869, 0), ('T', 15941, 2), ('ER', 16106, 2), ('N', 16202, 2), #-TURN
    ('T', 16231, 2), ('UH', 16296, 0),  #TO
    ('DH', 16329, 2), ('UW', 16403, 1), #THE
    ('F', 16477, 1), ('AA', 16804, 2),('', 16840, 0), ('D', 16901, 2), #FO-D # L is absent
    ('', 17286, 1), #*PAUSE*
    #AND AS FOR HASAN'S PATHETIC GUARD, CRUSH THEM (noticably different emotional tone until 20293)
], names=('phoneme', 'timing', 'priority'))

all_recordings = [battle_control_offline_rec, unable_to_comply_building_in_progress_rec, qauternery_objective_achieved_rec, building_infiltrated_rec, you_have_lost_rec, low_power_rec, training_rec, destroy_the_remainder_of_hassans_guard_rec, tunnel_secure_mcv_en_route_rec, mutants_located_rec, cabal_online_rec, nod02_rec]
all_aud = [battle_control_offline, unable_to_comply_building_in_progress, qauternery_objective_achieved, building_infiltrated, you_have_lost, low_power, training, destroy_the_remainder_of_hassans_guard, tunnel_secure_mcv_en_route, mutants_located, cabal_online, nod02]

# substitutes to phonemes that have yet to be identified (some of these are tentative
similar_phonemes = {
    'ZH': ['CH'],
}


class TibSunCabal:
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
        self.end_length = 800

        self.use_phoneme_priority = True

        self.out_audio = AudioSegment.empty()
        """The audio segment generated by load_audio()"""

        self.audio_segment_timings = np.rec.array((0, 0), names=('output_time', 'source_clip_index', 'source_time'))
        """
        Record of segment timings in the output audio. Each entry represents the time that a new source segment begins.
        
        The first index in each entry (named 'output_time') is the time in milliseconds when a new source segment begins.
        The second index (named 'source_time') is the time when the segment starts in the source audio.
        
        Example: If this record contains the entry (2000, 1, 590), that means at 2 seconds into the output audio, the
        segment of 'unable_to_comply' that begins at 590 seconds will be played (when CABAL says 'T' in 'to').
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
        output = AudioSegment.empty().set_frame_rate(all_aud[0].frame_rate) #rate is 22050Hz

        # milliseconds marking each time a new audio segment is used
        audio_out_millis = []

        # milliseconds marking the beginning of each segment in from the source audio
        audio_source_millis = []

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
                output = self.append_best_phoneme_segment(output, phoneme_segment, audio_out_millis,
                                                                 audio_source_millis)
                phoneme_segment = []
            if p == ' ':
                output = self.append_audio_segment(output, AudioSegment.silent(self.space_length), -1, audio_out_millis,
                                                   audio_source_millis)
            elif p in self.stop_chars:
                output = self.append_audio_segment(output, AudioSegment.silent(self.stop_length), -1, audio_out_millis,
                                                   audio_source_millis)

        if len(output) == 0:
            warnings.warn('returned audio segment is empty', UserWarning)
            self.audio_segment_timings = np.rec.array((0, 0), names=('output_time', 'source_clip_index', 'source_time'))
        else:
            self.audio_segment_timings = np.rec.array(tuple(zip(audio_out_millis, audio_source_millis)),
                                                      names=('output_time', 'source_clip_index', 'source_time'))

        progress_callback(1, progress_total, progress_total)
        output = self.append_audio_segment(output, AudioSegment.silent(self.end_length), -1, audio_out_millis,
                                           audio_source_millis)

        self.out_audio = output
        return output

    # Note CABAL does not have an easily available video source, this function will have no use
    # def get_frame_idx_from_millis(self, millis: int) -> int:
    #     """
    #     Get the morshu frame from the given time in milliseconds
    #     :param millis: Time in the output audio in milliseconds.
    #     :return: The morshu frame index that occurs at that time in the generated audio. The morshu video is 10 fps.
    #     """
    #     if len(self.out_audio) == 0:
    #         return 0

    #     millis = int(millis)
    #     idx = np.argmin(self.audio_segment_timings['output'] <= millis) - 1

    #     output_segment_start, morshu_segment_start = self.audio_segment_timings[idx]
    #     if morshu_segment_start == -1:
    #         return -1

    #     morshu_frame = (morshu_segment_start + (millis - output_segment_start)) // 100  # 10 fps, 1 frame per 100 millis
    #     return morshu_frame

    @staticmethod
    def substitute_similar_phonemes(phonemes: List[str]):
        """
        Parse through a list of phonemes and replace them if necessary.

        The replacement phonemes are stored in the global similar_phonemes dictionary. These are phonemes that have
        yet to be identified in CABAL dialog. These phonemes may sound slightly different than expected, and may be
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
    def append_audio_segment(audio_out: AudioSegment, audio_segment: AudioSegment, source_millis_start: int,
                             audio_out_millis: List[int], audio_source_millis: List[int]) -> AudioSegment:
        """
        Helper function to append one audio segment to another and update several variables at the same time.

        :param audio_out: The full audio to append to.

        :param audio_segment: The audio segment that will be appended.

        :param source_millis_start: The time in milliseconds that the audio segment begins in the source audio. Use -1
        if this audio doesn't appear in the source audio (like if it's silence).

        :param audio_out_millis: A list of milliseconds representing when new segments begin in the output audio.

        :param audio_source_millis: A list of milliseconds representing when the segment begins in the morshu audio.

        :return: audio_out with audio_segment appended.
        """
        audio_out_millis.append(len(audio_out))
        audio_source_millis.append(source_millis_start)
        audio_out += audio_segment
        return audio_out

    @staticmethod
    def get_phoneme_sequence_occurrences(phonemes: List[str]) -> List[Tuple[int, int]]:
        """
        Get all occurrences of a given phoneme segment in the source audio.
        :return: List of tuples containing (source_index, start_millis, end_millis)
        """
        occurrences = []
        for chosen_rec_index in range(len(all_recordings)):
            chosen_rec = all_recordings[chosen_rec_index]
            for i in range(len(chosen_rec) - len(phonemes)):
                if (chosen_rec['phoneme'][i:i + len(phonemes)] == phonemes).all():
                    start = chosen_rec['timing'][i - 1]
                    end = chosen_rec['timing'][i + len(phonemes) - 1]
                    occurrences.append((chosen_rec_index, start, end))
        return occurrences

    def get_best_single_phoneme(self, phoneme: str, preceding: str = "", succeeding: str = "") \
            -> Tuple[AudioSegment, int]:
        """
        Find the best audio segment of the given phoneme.

        This compares the given surrounding phonemes with the phonemes in the each audio to determine the best one.
        Segments that match the same preceding or succeeding phoneme will be given the highest priority, and moderate
        priority is given if the phonemes both contain vowels. If two segments have the same priority, a random one is
        chosen.

        :param phoneme: The phoneme to search for.

        :param preceding: The phoneme that comes before the searching phoneme.

        :param succeeding: The phoneme that comes after the searching phoneme.

        :return: A tuple containing the audio segment and the time that the segment starts in the chosen audio
        """
        # list of phoneme indices of the highest priority
        best_samples = []
        for chosen_rec_index in range(len(all_recordings)):
            chosen_rec = all_recordings[chosen_rec_index]
            phoneme_indices = np.where(chosen_rec['phoneme'] == phoneme)[0]
            if len(phoneme_indices) == 0:
                continue

            highest_priority = 0
            for i in phoneme_indices:
                # priorities for preceding and succeeding phonemes:
                # exact match: 10
                # compared phonemes both contain vowels: 5
                # no match: 0
                # starting priority is obtained from chosen_rec
                source_preceding = chosen_rec['phoneme'][i - 1]

                priority = chosen_rec['priority'][i] if self.use_phoneme_priority else 0
                if source_preceding == preceding:
                    priority += 10
                # check both phonemes for any vowel
                elif any(c in source_preceding for c in "AEIOU") and any(c in preceding for c in "AEIOU"):
                    priority += 5

                # check succeeding phonemes
                source_succeeding = chosen_rec['phoneme'][i + 1] #does this need protection from going out of bounds? TODO: check how empty phonemes are handled 
                if source_succeeding == succeeding:
                    priority += 10
                # check both phonemes for any vowel
                elif any(c in source_succeeding for c in "AEIOU") and any(c in succeeding for c in "AEIOU"):
                    priority += 1

                # TODO CABAL has more dialog than Morshu, so we could afford to vary which words are used to avoid fatigue
                if priority < highest_priority:
                    continue
                if priority > highest_priority:
                    highest_priority = priority
                    best_samples = []
                best_samples.append((chosen_rec_index, i))

        if len(best_samples) == 0:
            return AudioSegment.empty(), 0
        sample = random.choice(best_samples)
        source_rec = sample[0]
        phoneme_index = sample[1]
        chosen_rec = all_recordings[source_rec]
        chosen_aud = all_aud[source_rec]
        # play(chosen_aud.get_array_of_samples(), 22050, blocking=True)
        segment = chosen_aud[chosen_rec['timing'][phoneme_index - 1]: chosen_rec['timing'][phoneme_index]]
        # play(segment.get_array_of_samples(), 22050, blocking=True)
        return segment, chosen_rec['timing'][phoneme_index - 1]

    def append_best_phoneme_segment(self, output: AudioSegment, phonemes: List[str],
                                           audio_out_millis: List[int] = None,
                                           audio_source_millis: List[int] = None) -> AudioSegment:
        """
        Search for a phoneme segment that appears in the source audio, and append it to the given audio output. If a
        segment more than 1 length can't be found, get_best_single_phoneme will be used to find the best one.

        :param output: The audio to append the best segment to.

        :param phonemes: The phoneme segment to search for.

        :param audio_out_millis: A list of milliseconds representing when new segments begin in the output audio.

        :param audio_source_millis: A list of milliseconds representing when the segment begins in the source audio.

        :return: The audio segment with the new segment appended to it.
        """
        phonemes = TibSunCabal.substitute_similar_phonemes(phonemes)
        if len(phonemes) == 1:
            segment, start = self.get_best_single_phoneme(phonemes[0])
            return TibSunCabal.append_audio_segment(output, segment, start, audio_out_millis, audio_source_millis)

        # preceding and succeeding phonemes are used if we need to search for a single phoneme
        preceding = ""

        # full_segment = AudioSegment.empty()
        while len(phonemes) > 0:
            sequence_length = 1
            segment = AudioSegment.empty()

            start = 0
            while sequence_length <= len(phonemes):
                occurrences = TibSunCabal.get_phoneme_sequence_occurrences(phonemes[:sequence_length])
                if len(occurrences) == 0:
                    break
                chosen_rec_index, start, end = random.choice(occurrences)
                phonemes_sequence_print = ""
                for single_phoneme in phonemes[:sequence_length]:
                    phonemes_sequence_print += single_phoneme
                print("phoneme[:sequence_length]" + phonemes_sequence_print + " rec index: " + str(chosen_rec_index) + ", clip_start: " + str(start) + ", clip_end: " + str(end))
                chosen_aud = all_aud[chosen_rec_index]
                # play(chosen_aud.get_array_of_samples(), 22050, blocking=True)
                segment = chosen_aud[start:end]
                # play(segment.get_array_of_samples(), 22050, blocking=True)
                sequence_length += 1
            sequence_length -= 1

            # find the best single phoneme if a longer segment wasn't found
            if sequence_length == 1:
                if sequence_length + 1 < len(phonemes):
                    succeeding = phonemes[sequence_length + 1]
                else:
                    succeeding = ""
                segment, start = self.get_best_single_phoneme(phonemes[0], preceding, succeeding)
            
            output = TibSunCabal.append_audio_segment(output, segment, start, audio_out_millis, audio_source_millis)

            preceding = phonemes[sequence_length - 1]
            del phonemes[:sequence_length]

        return output
