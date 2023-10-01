import os, re
from pydub import AudioSegment
from tqdm import tqdm
from pydub.effects import speedup
from pydub.silence import detect_leading_silence

trim_leading_silence = lambda x: x[detect_leading_silence(x) :]
trim_trailing_silence = lambda x: trim_leading_silence(x.reverse()).reverse()
strip_silence = lambda x: trim_trailing_silence(trim_leading_silence(x))


def get_voice_file(phoneme, path):
    fname = phoneme.decode("utf-8")
    return path + fname + ".wav"


def thaana_to_speech(text_input, phonemes, outfile):
    stripped = re.sub(r"[.(),\'\"?؟:;،]+", "", text_input)
    input = list(stripped)
    voice_files = os.listdir(phonemes)
    for i in range(len(voice_files)):
        voice_files[i] = voice_files[i].split(".", 1)[0].encode("utf-8")

    word = ""
    word_w_next = ""
    sound = ""
    clips = []
    twochar = 0
    for i in range(len(input)):
        if twochar == 0:
            word = word + input[i]
            try:
                word_w_next = word + input[i + 1] + input[i + 2]

            except:
                word_w_next = ""

            if input[i] == " ":
                word = "space"
                sound = word.encode("utf-8")
                clip = AudioSegment.from_file(get_voice_file(sound, phonemes))
                clip = speedup(clip, 1.5, 150)
                sound = ""
                word = ""
                clips.append(clip)
                continue

            sound = word.encode("utf-8")
            soundnext = word_w_next.encode("utf-8")
            clip = None
            if soundnext in voice_files:
                clip = AudioSegment.from_file(get_voice_file(soundnext, phonemes))
                clip = strip_silence(clip)
                soundnext = ""
                sound = ""
                word = ""
                twochar = 1
                clips.append(clip)
                continue
            if sound in voice_files:
                clip = AudioSegment.from_file(get_voice_file(sound, phonemes))
                clip = strip_silence(clip)
                sound = ""
                word = ""
                clips.append(clip)

        if twochar == 2:
            twochar = 0

        if twochar == 1:
            twochar = 2

    final_clip = clips[0]
    range_loop = tqdm(list(range(1, len(clips))), "Concatenating audio")
    for k in range_loop:
        final_clip = final_clip + clips[k]

    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    final_clip.export(outfile, format="wav")
