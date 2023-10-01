# Dhivehi-TTS
A simple concatenative Dhivehi Text-to-Speech program which uses provided phonemes to convert Dhivehi input sentence to speech.

## Dependencies
This project relies on Python 3.11 or later.

The required python packages are listed in the requirement.txt file, which are:
```
pydub==0.25.1
tqdm==4.66.1
```

## Installation
1. Make sure you have python installed.
2. Clone or download this repository to your local machine.
3. Open a terminal and navigate to the cloned directory.
4. Run: `pip install -r requirements.txt`
5. Read below instructions on how to use this program.

## How to use
* In terminal:
```
python main.py [path to phonemes] [output file]
```
* Example since some of the phonemes are already provided in /phonemes/ folder:
```
python main.py /phonemes/ /output/generated_sentence.wav
```
* The sound files for phonemes should be in wav format and should be named in Thaana for that sound.
* By default the program will convert the following sentence:
> "ބޮޑު ބާޒާރުގައި ހުންނަ މޮޅު ތަކެތީގައި ސިލްޖަހަންޏާ ޕޯސްޓް އޮފީހުގެ ވެރިޔަކު ވާނީ ދާށެވެ."
* If you want to change the input sentence, you can use -i in command line as shown below. It will prompt for an input sentence instead of using the default:
```
python main.py -i /phonemes/ /output/generated_sentence.wav
```
