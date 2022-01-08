import os
import asyncio
import subprocess

POLL_DELAY: int = 10

async def _execute(cmds: list):
    for cmd in cmds:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL)

def loadsong(music_dir, filename, pre_ext, ref_ext, ytID):
    cmds = []
    # Song download
    cmd = f"youtube-dl -o {music_dir}/{filename}{pre_ext} -f 140 https://www.youtube.com/watch?v={ytID}"
    cmds.append(cmd)
    
    # Song conversion
    cmd = f"ffmpeg -i {music_dir}/{filename}{pre_ext} -c:v copy -c:a libmp3lame -q:a 4 {music_dir}/{filename}{ref_ext}"
    cmds.append(cmd)

    # Presong deletion
    cmd = f"rm -rf {music_dir}/{filename}{pre_ext}"
    cmds.append(cmd)

    asyncio.run(_execute(cmds))