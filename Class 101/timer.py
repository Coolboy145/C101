import time

second = int(input("Please enter the amount of seconds."))


def countdown_timer(second):
    while second > 0:
        mins  = int(second/60)
        secs = int(second%60)
        timer = f'{mins}:{secs}'
        print(timer)
        time.sleep(1)
        second-=1
    
    print("times up!")

countdown_timer(int(second))    