import sys, time, csv, os
import tools.cameras as cameras
import tools.interaction as interaction
import tools.monitoring as monitoring
from tools.art import BANNER

print(BANNER)

# detect cameras
_, working_ports, _ = cameras.list_ports()
if not working_ports:
    print("Exiting")
    sys.exit(1)

# user interaction
monitoring_name, monitoring_path = interaction.ask_for_monitoring_name()
num_photos, interval = interaction.ask_for_settings()
resolution = interaction.ask_for_resolution()

# start monitoring
monitoring.start_monitoring(monitoring_path=monitoring_path, working_ports=working_ports, interval = interval)

sys.exit(0)
