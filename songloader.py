import os
import subprocess

POLL_DELAY: int = 10


def loadsong(music_dir, filename, pre_ext, ref_ext, ytID):
    presong_file = f"{music_dir}/{filename}{pre_ext}"
    refsong_file = f"{music_dir}/{filename}{ref_ext}"

    silentsh = subprocess.Popen("/bin/bash -i".split(), 
                            stdin=subprocess.PIPE,
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.PIPE)

    # Song download
    cmd = f"youtube-dl -o {presong_file} -f 140 https://www.youtube.com/watch?v={ytID}\n"
    silentsh.stdin.write(cmd.encode())

    # Song conversion
    cmd = f"ffmpeg -i {presong_file} -c:v copy -c:a libmp3lame -q:a 4 {refsong_file}\n"
    silentsh.stdin.write(cmd.encode())

    # Presong deletion
    os.remove(presong_file)
