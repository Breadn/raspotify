import os
import subprocess

def _execute_cmd(cmd):
    silentsh = subprocess.Popen("/bin/bash -i".split(), stdin=subprocess.PIPE,
                            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    silentsh.stdin.write(cmd.decode())
    silentsh.kill()


def loadsong(music_dir, filename, ext, ytID):
    filepath = f"{music_dir}/{filename}{ext}"
    cmd = f"youtube-dl -o {filepath} --extract-audio --audio-format{ext} https://www.youtube.com/watch?v={ytID}"
    _execute_cmd(cmd)
    print(f"{filepath} loaded!")

