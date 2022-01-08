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

    queue = []
    action = ""

    while(action.lower() != "exit"):
        print(action)

        # do stuff
        if(action.lower() == "search"):
            cmd = "youtube-dl -o music/%(title)s.%(ext)s -f 140 https://www.youtube.com/watch?v=cdaKIWr4wDU"
            subprocess.Popen(cmd.split())

        print(": ", end='')
        action = input()
    
    exit_raspotify()



if __name__ == '__main__':
    main()