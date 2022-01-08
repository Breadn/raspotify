import os
import asyncio
import subprocess

POLL_DELAY: int = 10


async def loadsong(music_dir, filename, pre_ext, ref_ext, ytID):
    presong_file = f"{music_dir}/{filename}{pre_ext}"
    refsong_file = f"{music_dir}/{filename}{ref_ext}"

    # Song download
    cmd = f"youtube-dl -o {presong_file} -f 140 https://www.youtube.com/watch?v={ytID}"
    subprocess.call(cmd.split(), stdout=subprocess.DEVNULL)
    while(not os.path.isfile(presong_file)):
        asyncio.sleep(POLL_DELAY)
    
    # Song conversion
    cmd = f"ffmpeg -i {presong_file} -c:v copy -c:a libmp3lame -q:a 4 {refsong_file}"
    subprocess.call(cmd.split(), stdout=subprocess.DEVNULL)
    while(not os.path.isfile(refsong_file)):
        asyncio.sleep(POLL_DELAY)

    # Presong deletion
    os.remove(presong_file)
