import os
import subprocess

class SongLoader:
    
    def __init__(self, music_dir):
        self.music_dir = os.path.join(os.getcwd(), music_dir)
        self.silentsh = subprocess.Popen("/bin/bash -i".split(), stdout=subprocess.DEVNULL)
        self.silentsh.stdin.write(f"cd {self.music_dir}".encode())
        print(f"Initialized SongLoader into directory {self.music_dir}")
        

    def __del__(self):
        self.silentsh.terminate()

    def loadsong(self, filename, ext, ytID):
        print(f"Loading song into {self.music_dir}")
        cmd = f"youtube-dl --extract-audio --audio-format {ext} https://www.youtube.com/watch?v={ytID}"
        self.silentsh.stdin.write(cmd.encode())
    
    

