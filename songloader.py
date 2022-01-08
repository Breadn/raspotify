import os
import asyncio
import subprocess

POLL_DELAY: int = 10

async def _loadsong_proc(cmds, presong_file, refsong_file):
    # Song download
    cmd = cmds[0]
    subprocess.call(cmd.split(), stdout=subprocess.DEVNULL)
    while(not os.path.isfile(presong_file)):
        asyncio.sleep(POLL_DELAY)
    
    # Song conversion
    cmd = cmds[1]
    subprocess.call(cmd.split(), stdout=subprocess.DEVNULL)
    while(not os.path.isfile(refsong_file)):
        asyncio.sleep(POLL_DELAY)

    # Presong deletion
    os.remove(presong_file)

async def loadsong(music_dir, filename, pre_ext, ref_ext, ytID):
    presong_file = f"{music_dir}/{filename}{pre_ext}"
    refsong_file = f"{music_dir}/{filename}{ref_ext}"
    cmds = (
        f"youtube-dl -o {presong_file} -f 140 https://www.youtube.com/watch?v={ytID}",
        f"ffmpeg -i {presong_file} -c:v copy -c:a libmp3lame -q:a 4 {refsong_file}"
    )
    asyncio.run(_loadsong_proc(cmds, presong_file, refsong_file))

