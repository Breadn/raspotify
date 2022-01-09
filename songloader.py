import os
import subprocess

def loadsong(music_dir, filename, ext, ytID):
    filepath = f"{music_dir}/{filename}.{ext}"
    cmd = f"youtube-dl -o {filepath} --extract-audio --audio-format {ext} https://www.youtube.com/watch?v={ytID}"
    subprocess.Popen(args=cmd.split(), stdout=subprocess.DEVNULL)

