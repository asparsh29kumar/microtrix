import subprocess
import time

try:
    while True:  # Loop continuously
        # subprocess.call(['python', 'login.py', "140905116", "#Cannonballs1#"])
        print("Attempting login...")
        subprocess.call(['python', 'login.py', "140909620", "thebest1"])
        time.sleep(5)
except (KeyboardInterrupt, SystemExit):
    subprocess.call(['python', 'logout.py'])
