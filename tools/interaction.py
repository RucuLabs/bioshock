import os
import re

MONITORING_ROOT = "monitoring"

RESOLUTIONS_16_9 = {
    "360p": "640x360",
    "480p": "854x480",
    "540p": "960x540",
    "576p": "1024x576",
    "720p": "1280x720",
    "768p": "1366x768",
    "900p": "1600x900",
    "FullHD": "1920x1080",
    "1440p": "2560x1440",
    "4K": "3840x2160"
}

def is_valid_directory(directory_name):

    if ' ' in directory_name:
        return False

    if not re.match(r'^[a-zA-Z0-9_-]+$', directory_name):
        return False

    try:
        os.makedirs(os.path.join('/tmp', directory_name), exist_ok=True)
    except OSError as e:
        return False
    else:
        os.rmdir(os.path.join('/tmp', directory_name))
        return True

def ask_for_monitoring_name():
    if not os.path.exists(MONITORING_ROOT):
        os.mkdir(MONITORING_ROOT)
    while True:
        monitoring_name = input("Choose a name for your monitoring session: ")
        monitoring_path = f"{MONITORING_ROOT}/{monitoring_name}"
        if not os.path.exists(monitoring_path) and is_valid_directory(directory_name=monitoring_name):
            try:
                os.mkdir(monitoring_path)
                return monitoring_name, monitoring_path
            except:
                print("Couldn't create the monitoring session folder, try again.")
                continue
        print(f"{monitoring_name} already exists, choose another name.")

def ask_for_settings():
    while True:
        try:
            num_photos = int(input("Number of records: "))
            interval = int(input("Indica el intervalo (segundos): "))
            if num_photos >= 0 and interval >= 0:
                return num_photos, interval
        except:
            print("Input error, make sure to use numbers.")
            continue
        print("Input error, make sure to use numbers bigger than 0.")


def ask_for_resolution():
    while True:
        print("-- Resolution Options --")
        for name, resolution in RESOLUTIONS_16_9.items():
            print(f"{name}: {resolution}")
        user_choice = input("Enter the name of your desired resolution: ")

        if user_choice in RESOLUTIONS_16_9:
            selected_resolution = RESOLUTIONS_16_9[user_choice]
            print(f"You chose {user_choice}: {selected_resolution}")
            return selected_resolution
        else:
            print("Invalid resolution choice. Please select a valid option.")
            continue


            
