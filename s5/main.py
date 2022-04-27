import time


def bonjour(t):
    print("\n")
    for x in range(5):
        print("bonjour")
        time.sleep(t)


bonjour(0.3)
bonjour(0.5)
bonjour(1.3)
