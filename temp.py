import time

print(" Enter to start, Ctrl + C to stop")


while True:
    try:
        input()
        startTime = time.time()
        print("start now!")
        while True:
            print("time elapsed: ", round(time.time() - startTime, 0), "secs", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stoped")
        endTime = time.time()
        print("total Time: ", round(endTime - startTime, 2), 'secs')
        break








