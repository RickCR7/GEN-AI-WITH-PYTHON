import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temparature...")
        time.sleep(2)

threading.Thread(target=monitor_tea_temp).start()

print("Main program done")