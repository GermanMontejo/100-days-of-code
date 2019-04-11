import time
from datetime import datetime, timedelta

def pomodoro_timer():
    pomodoro_tracker = 0

    # flip is going to be used to switch the end time to 25 mins or 5 mins
    # when the ctr resets to 0.
    flip = 0
    print('Begin...')

    end = datetime.now() + timedelta(minutes=25)
    while True:
        ctr = (end-datetime.now()) + timedelta(seconds=1)

        print(str(ctr).split('.')[0])

        if ctr.seconds == 0:
            pomodoro_tracker += 1
            flip += 1

            if pomodoro_tracker > 4:
                # after 4 pomodoro, take longer breaks, i.e. 20 mins
                end = datetime.now() + timedelta(minutes=20)
                pomodoro_tracker = 0
                print('long break countdown...')

            else:
                # this means we're back to 25 mins pomodoro countdown
                if flip % 2 == 0:
                    end = datetime.now() + timedelta(minutes=25)
                    print('pomodoro countdown...')
                else:
                    # else, countdown is on short break
                    end = datetime.now() + timedelta(minutes=5)
                    print('short break countdown...')

        time.sleep(1)

try:
    pomodoro_timer()
except KeyboardInterrupt:
    print('Exiting program...')
    exit()