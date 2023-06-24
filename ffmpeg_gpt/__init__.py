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

        _stdout = ""
        # history = subprocess.run(script, shell=True)
        p = subprocess.Popen(
            script, shell=True, stdout=subprocess.PIPE
        )  # launch the process
        while p.poll() is None:  # check if the process is still alive
            out = p.stdout.readline()  # if it is still alive, grab the output
            print(out.decode("utf-8"))  # and print it
            _stdout += out.decode("utf-8")

        print("aaaaaaa")
        print(_stdout)
        print("=================================")
        exit()

        if not yesno("Did it work ?"):
            if yesno("Do you want to iterate ?"):
                script = rerun(args.prompt, script, _stdout)
        else:
            run_again = False
