from ffmpeg_gpt.ffmpeg_gpt import get_bash_script
from ffmpeg_gpt.utils import yesno
import argparse


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("prompt", type=str, help="prompt")
    args = argparser.parse_args()

    script = get_bash_script(args.prompt)

    print("Generated script: ")
    print("===========")
    print(script)
    print("===========")

    if yesno("Do you want to run this script?"):
        import subprocess

        subprocess.run(script, shell=True)
