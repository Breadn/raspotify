import os
import subprocess

class SongLoader:
    
    songset = set()

    def __init__(self, music_dir):
        self.music_dir = os.path.join(os.getcwd(), music_dir)
        
        subprocess.call(f"cd {self.music_dir}".split(), shell=True)
        print(f"Initialized SongLoader into directory {self.music_dir}")

    def loadsong(self, ext, ytID):
        if(ytID not in self.songset):
            print(f"Loading song into {self.music_dir}")
            self.songset.add(ytID)
            cmd = f"youtube-dl --extract-audio --audio-format {ext} https://www.youtube.com/watch?v={ytID}"
            subprocess.Popen(args=cmd.split(), stdout=subprocess.DEVNULL)
        else:
            print("Song already cached!")
    
    

