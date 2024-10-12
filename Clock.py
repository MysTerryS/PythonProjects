import time

def ClockStep():
    while True:
        print("\rCurrent time: %s" % time.strftime("%H:%M:%S"), end = "")
        time.sleep(1)

ClockStep()
