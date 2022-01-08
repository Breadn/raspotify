import os
import asyncio
import subprocess

POLL_DELAY: int = 10

async def loadsong(music_dir, filename, pre_ext, ref_ext, ytID):
    song_file = f"{music_dir}/{filename}"

    # Song download
    cmd = f"youtube-dl -o {music_dir}/{filename}{pre_ext} -f 140 https://www.youtube.com/watch?v={ytID}"
    subprocess.call(cmd.split(), stdout=subprocess.DEVNULL)

    while(not os.path.isfile(song_file+pre_ext)):
        asyncio.sleep(POLL_DELAY)
    
    # Song conversion
    cmd = f"ffmpeg -i {music_dir}/{filename}{pre_ext} -c:v copy -c:a libmp3lame -q:a 4 {music_dir}/{filename}{ref_ext}"
    subprocess.call(cmd.split(), stdout=subprocess.DEVNULL)

    while(not os.path.isfile(song_file+ref_ext)):
        asyncio.sleep(POLL_DELAY)

    # Presong deletion
    cmd = f"rm -rf {music_dir}/{filename}{pre_ext}"
    subprocess.call(cmd.split(), stdout=subprocess.DEVNULL)