# Problem Statement:
# ------------------
# Display notifications on a timely manner.
# Notification to display the ETA.
# Alert for battery status.
# Break notifications after every 20 minutes.

# Flow:
# -----
# Schedule function to run every after particular time.
# Need to have a mechanism which will subtract time to display ETA.
# Event based triggering.

import os
import time


def show_toast(title, message):
    title = title.replace("'", "")
    message = message.replace("'", "")
    os.system(f"notify-send '{title}' '{message}'")


while True:
    show_toast("Drink Water", "Please gtfo and drink some water!!!")
    # time.sleep(3.0)
