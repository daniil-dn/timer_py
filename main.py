import time


def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer)
        time.sleep(1)
        t-=1
    print('finished')
countdown_timer(3)