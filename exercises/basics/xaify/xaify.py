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

# Notification to display the ETA.
# --------------------------------
# Shailesh:
# If we make hour = 0 as a counter and increment with every while loop then we
# can count the hour wrt opening time of laptop.

# Pranali:
# Time delta (difference/subtraction)


def show_toast(title: str, message: str, minutes: float) -> None:
    """Displays notification in timely manner."""
    title = title.replace("'", "")
    message = message.replace("'", "")
    time.sleep(minutes * 60.0)
    os.system(f"notify-send '{title}' '{message}'")


while True:
    show_toast("Take a break", "Get out from my sight!!!", 0.1)
    # show_toast("Drink Water", "Please gtfo and drink some water!!!", 0.1)
