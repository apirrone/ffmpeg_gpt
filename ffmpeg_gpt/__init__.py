from ffmpeg_gpt.ffmpeg_gpt import get_bash_script, rerun
from ffmpeg_gpt.utils import yesno
import argparse
import subprocess


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("prompt", type=str, help="prompt")
    args = argparser.parse_args()

    run_again = True
    script = get_bash_script(args.prompt)

    while run_again:
        print("Generated script: ")
        print("===========")
        print(script)
        print("===========")

        if not yesno("Do you want to run this script?"):
            print("Cancelling")
            return

        with open(".tmp.sh", "w") as f:
            f.write(script)

        subprocess.run("bash .tmp.sh 2>&1 | tee .tmp.txt", shell=True)

        out = open(".tmp.txt", "r").read()

        if not yesno("Did it work ?"):
            if yesno("Do you want to iterate ?"):
                script = rerun(args.prompt, script, out)
        else:
            run_again = False
