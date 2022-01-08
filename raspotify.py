import os
import subprocess


def splashscreen(ver):
    print("\n\n\n")
    print(f"=== Raspotify v{ver} ===")
    print("play - plays available queue")
    print("volume <factor> - adjust volume between factor of [1..0]")
    print("queue - lists queue")
    print("search - search for song to enqueue")
    print("exit - exit program")
    print("=========================")


def exit_raspotify(music_dir):

    if(os.path.isdir(f"./{music_dir}") and os.listdir(f"./{music_dir}")):
        cmd = f"rm -rf {os.getcwd()}/{music_dir}/*"
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL)
    print("Goodbye.")


def main():
    splashscreen("0.01")

    music_dir = "music"
    pre_ext = ".m4a"
    ref_ext = ".mp3"
    queue = []
    songset = set()
    volume = 0.05
    action = ""

    while(action.lower() != "exit"):
        print(action)

        # do stuff
        if(action == "play"):
            if(queue):
                song_path = f"{music_dir}/{queue[0]}{ref_ext}"
                if(os.path.isfile(song_path)):
                    cmd = f"play {song_path}"
                    subprocess.Popen(cmd, stdout=subprocess.DEVNULL)
                    queue.pop(0)
                    print(f"Playing queue: {queue[0]}")
                else:
                    print(f"{song_path} not yet loaded")
            else:
                print("No songs in queue")
        
        elif(action.split()[0] == "volume"):
            if(len(action.split()) > 1 and isinstance(action.split()[1], float)):
                volume = action.split()[1]
                print(f"Volume set to {volume}")
            else:
                print("Invalid volume")
        
        elif(action == "queue"):
            print(queue)

        elif(action == "search"):
            filename = "Kyoto"
            ytID = "cdaKIWr4wDU"

            if(ytID not in songset):
                cmd = f"youtube-dl -o {music_dir}/{filename}{pre_ext} -f 140 https://www.youtube.com/watch?v={ytID}; ffmpeg -i {music_dir}/{filename}{pre_ext} -c:v copy -c:a libmp3lame -q:a 4 {music_dir}/{filename}{ref_ext}; rm -rf {music_dir}/{filename}{pre_ext}"
                subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL)
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