import subprocess


def splashscreen(ver):
    print(f"=== Raspotify v{ver} ===")
    print("play - plays available queue")
    print("queue - lists queue")
    print("search - search for song to enqueue")
    print("exit - exit program")
    print("=========================")
    print(":")


def exit_raspotify():
    print("asynch?")
    subprocess.run(["youtube-dl", "-f", "140", "https://www.youtube.com/watch?v=cdaKIWr4wDU"])
    print("yup")


def main():
    splashscreen("0.01")

    queue = []
    action = input()

    while(action != "exit"):
        print(action)

        print(":")
        action = input()
    
    exit_raspotify()



if __name__ == '__main__':
    main()