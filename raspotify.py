import subprocess


def splashscreen(ver):
    print(f"=== Raspotify v{ver} ===")
    print("play - plays available queue")
    print("queue - lists queue")
    print("search - search for song to enqueue")
    print("exit - exit program")
    print("=========================")


def exit_raspotify():
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
        if(action.lower() == "search"):
            
            filename = "Kyoto"
            ytID = "cdaKIWr4wDU"

            if(ytID not in songset):
                cmd = f"youtube-dl -o {path}/{filename}{pre_ext} -f 140 https://www.youtube.com/watch?v={ytID}; ffmpeg -i {filename}{pre_ext} -c:v copy -c:a libmp3lame -q:a 4 {filename}{ref_ext}"
                print(cmd)
                subprocess.Popen(cmd.split())
                print("loading song")
            else:
                print("queueing cached song")

            queue.append(filename)
            songset.add(ytID)


        print(": ", end='')
        action = input()
    
    exit_raspotify()



if __name__ == '__main__':
    main()