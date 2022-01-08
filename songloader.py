import os
import subprocess


async def _execute_cmd(cmd):
    subprocess.call(cmd.split(), stdout=subprocess.DEVNULL)
    return

async def loadsong(music_dir, filename, pre_ext, ref_ext, ytID):
    presong_file = f"{music_dir}/{filename}{pre_ext}"
    refsong_file = f"{music_dir}/{filename}{ref_ext}"

    # Song download
    cmd = f"youtube-dl -o {presong_file} -f 140 https://www.youtube.com/watch?v={ytID}"
    print("Fetching song from YouTube...")
    await _execute_cmd(cmd)

    # Song conversion
    cmd = f"ffmpeg -i {presong_file} -q:a 4 {refsong_file}"
    print(f"Converting song {presong_file} to mp3...")
    await _execute_cmd(cmd)

    # Presong deletion
    os.remove(presong_file)
    print(f"{refsong_file} loaded!")
