# pip install psutil
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent >= 30:
 
    # pip install py-notifier
    # pip install win10toast
    from pynotifier import Notification

    Notification(
        title="Battery Low",
        description=f"{str(percent)}% Battery remain!!",
        duration=5,
        urgency=Notification.URGENCY_CRITICAL,
    ).send()
