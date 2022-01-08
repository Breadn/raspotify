import os
import subprocess


def splashscreen(ver):
    print(f"=== Raspotify v{ver} ===")
    print("play - plays available queue")
    print("queue - lists queue")
    print("search - search for song to enqueue")
    print("exit - exit program")
    print("=========================")


def exit_raspotify():
    if(os.path.isdir("./music")):
        cmd = "rm -rf ./music/*"
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL)
    print("Goodbye.")


def main():
    splashscreen("0.01")

    path = "music"
    pre_ext = ".m4a"
    ref_ext = ".mp3"
    queue = []
    songset = set()
    action = ""

    while(action.lower() != "exit"):
        print(action)

        # do stuff
        if(action.lower() == "play"):
            song_path = f"{path}/{queue[0]}{ref_ext}"
            if(os.path.isfile(song_path)):
                cmd = f"play {song_path}"
                subprocess.Popen(cmd, stdout=subprocess.DEVNULL)
                queue.pop(0)
                print(f"Playing queue: {queue[0]}")
            else:
                print("No songs loaded in queue")
        
        elif(action.lower() == "queue"):
            print(queue)

        elif(action.lower() == "search"):
            filename = "Kyoto"
            ytID = "cdaKIWr4wDU"

            if(ytID not in songset):
                cmd = f"youtube-dl -o {path}/{filename}{pre_ext} -f 140 https://www.youtube.com/watch?v={ytID}; ffmpeg -i {path}/{filename}{pre_ext} -c:v copy -c:a libmp3lame -q:a 4 {path}/{filename}{ref_ext}; rm -rf {path}/{filename}{pre_ext}"
                subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL)
                songset.add(ytID)
                print("loading song")
            else:
                print("queueing cached song")
            queue.append(filename)


        print(": ", end='')
        action = input()
    
    exit_raspotify()



if __name__ == '__main__':
    main()