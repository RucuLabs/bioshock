import sys, time, csv, os
import tools.cameras
import tools.interaction
import tools.monitoring
from tools.art import BANNER

print(BANNER)

# detect cameras
cams = cameras.detect()
if not cams:
    print("Exiting")
    sys.exit(1)

# user interaction
monitoring_name, monitoring_path = interaction.ask_for_monitoring_name()
num_photos, interval = interaction.ask_for_settings()
resolution = interaction.ask_for_resolution()

# start monitoring
monitoring.start_monitoring(monitoring_path=monitoring_path, monitoring_name=monitoring_name, cams=cams, resolution=resolution, num_photos=num_photos, interval=interval)

sys.exit(0)
