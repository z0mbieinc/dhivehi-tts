import dhitts
import os
from argparse import ArgumentParser, Namespace


parser = ArgumentParser()
parser.add_argument("phonemes", help="Path to phonemes")
parser.add_argument("output", help="Output file and path")
parser.add_argument("-i", "--input", help="Prompt for input instead of using default sentence",
                    action="store_true")
args: Namespace = parser.parse_args()

text_input = ""
PHONEMES_PATH = os.path.dirname(__file__) + args.phonemes
OUTPUT_FILE = os.path.dirname(__file__) + args.output

if args.input:
    inp = input("Write a sentence in Dhivehi to convert to speech:")
    text_input = inp
else:
    text_input = ".ބޮޑު ބާޒާރުގައި ހުންނަ މޮޅު ތަކެތީގައި ސިލްޖަހަންޏާ ޕޯސްޓް އޮފީހުގެ ވެރިޔަކު ވާނީ ދާށެވެ"

dhitts.thaana_to_speech(text_input, PHONEMES_PATH, OUTPUT_FILE)