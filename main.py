import time


def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{}:{}".format(mins, secs)
        print(timer)
        time.sleep(1)
        t-=1
countdown_timer(10)