# countdown timer
# Jerica Hanna

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer) # end="\r (This gets rid of the numbers)"
        time.sleep(1)
        t -= 1

    print("Time completed!")

t = input('Enter the time in seconds: ')

countdown(int(t))

print(t)