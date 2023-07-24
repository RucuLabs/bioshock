import os
import imageio

def list_monitorings():
    monitorings = os.listdir("monitorings")
    print("Available monitorings:")
    for idx, monitoring in enumerate(monitorings, start=1):
        print(f"{idx}. {monitoring}")
    return monitorings

def create_timelapse(chosen_monitoring, cams):
    monitoring_path = os.path.join("monitorings", chosen_monitoring)
    for cam in cams:
        cam_path = os.path.join(monitoring_path, cam)
        pictures = [filei for filei in os.listdir(cam_path) if filei.endswith(".jpg")]
        pictures.sort()

        if not pictures:
            print(f"No pictures found on '{camara}' of '{chosen_monitoring}'.")
            continue

        complete_pictures = [os.path.join(cam_path, picture) for picture in pictures]

        video_name = f"timelapse_{chosen_monitoring}_{cam}.mp4"
        video_path = os.path.join("timelapses", video_name)

        with imageio.get_writer(video_path, format="mp4", mode="I", fps=30) as writer:
            for picture in complete_pictures:
                frame = imageio.imread(picture)
                writer.append_data(frame)

        print(f"Timelapse '{video_name}' has been created at 'timelapses'.")

def main():
    if not os.path.exists("timelapses"):
        os.mkdir("timelapses")

    monitorings = list_monitorings()
    if not monitorings:
        print("No monitorings have been found.")
        return

    while True:
        try:
            option = int(input("Choose your monitoring (number): "))
            if 1 <= option <= len(monitorings):
                chosen_monitoring = monitorings[option - 1]
                break
            else:
                print("Error, chose a valid option.")
        except ValueError:
            print("Error, choose a valid option.")

    monitoring_path = os.path.join("monitorings", chosen_monitoring)
    cams = [cam for cam in os.listdir(monitoring_path) if os.path.isdir(os.path.join(monitoring_path, cam))]

    if not cams:
        print(f"No cameras have been found at '{chosen_monitoring}'.")
        return

    create_timelapse(chosen_monitoring, cams)

if __name__ == "__main__":
    main()
