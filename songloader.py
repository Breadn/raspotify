import os
import subprocess

class SongLoader:
    
    def __init__(self, music_dir):
        self.music_dir = os.path.join(os.getcwd(), music_dir)
        self.silentsh = subprocess.Popen("/bin/bash -i".split(), stdin=subprocess.PIPE, 
                                    stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        self.silentsh.stdin.write(f"cd {self.music_dir}".encode())
        print(f"Initialized SongLoader into directory {self.music_dir}")
        

    def __del__(self):
        self.silentsh.terminate()

    def loadsong(self, filename, ext, ytID):
        filepath = f"{self.music_dir}/{filename}.{ext}"
        print(f"Loading song into {filepath}")
        cmd = f"youtube-dl -o {filepath} --extract-audio --audio-format {ext} https://www.youtube.com/watch?v={ytID}"
        self.silentsh.stdin.write(cmd.encode())
    
    

