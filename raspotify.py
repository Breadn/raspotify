import os
import glob
import shutil
import subprocess

import songloader


def splashscreen(ver):
    print("\n\n\n")
    print(f"=== Raspotify v{ver} ===")
    print("play - plays available queue")
    print("volume <factor> - adjust volume between factor of [1..0]")
    print("queue - lists queue")
    print("search - search for song to enqueue")
    print("exit - exit program")
    print("========================")

def start_raspotify(music_dir):
    splashscreen("0.01")
    return songloader.SongLoader(music_dir)

def exit_raspotify(music_dir):
    path = f"{os.getcwd()}/{music_dir}"
    for item in glob.glob(os.path.join(path, '*')):
        if(os.path.isdir(item)):
            shutil.rmtree(item)
        else:
            os.remove(item)
    print("Goodbye.")


def main():
    music_dir = "music"
    ext = "mp3"
    queue = []
    songset = set()
    volume = 0.05
    action = ""

    sl = start_raspotify(music_dir)

    while(action.lower() != "exit"):

        if(action == "play"):
            if(queue):
                song_path = f"{music_dir}/{queue[0]}.{ext}"
                if(os.path.isfile(song_path)):
                    cmd = f"play -v {volume} {song_path}"
                    subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL)
                    print(f"Playing queue: {queue[0]}")
                    queue.pop(0)
                else:
                    print(f"{song_path} not yet loaded")
            else:
                print("No songs in queue")
        
        elif(action and action.split()[0] == "volume"):
            if(len(action.split()) > 1):
                try:
                    volume = float(action.split()[1])
                    print(f"Volume set to {volume}")
                except:
                    print("Invalid volume")
            else:
                print(f"volume: {volume}")
        
        elif(action == "queue"):
            print(queue)

        elif(action == "search"):
            filename = "Kyoto"
            ytID = "cdaKIWr4wDU"

            if(ytID not in songset):
                sl.loadsong(music_dir, filename, ext, ytID)
                songset.add(ytID)
                print("loading song")
            else:
                print("queueing cached song")
            queue.append(filename)


        print(": ", end='')
        action = input().lower()
    
    exit_raspotify(music_dir)



if __name__ == '__main__':
    main()