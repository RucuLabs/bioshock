import os
import imageio

def list_monitorings():
    monitorings = os.listdir("monitoring")
    print("Available monitorings:")
    for idx, monitoring in enumerate(monitorings, start=1):
        print(f"{idx}. {monitoring}")
    return monitorings

def obtain_chosen_monitoring(monitorings):
    while True:
        try:
            option = int(input("Choose your monitoring (number): "))
            if 1 <= option <= len(monitorings):
                return monitorings[option - 1]
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Invalid option. Try again.")

def create_timelapse(chosen_monitoring):
    monitoring_path = os.path.join("monitoring", chosen_monitoring)
    pictures = [filei for filei in os.listdir(monitoring_path) if filei.endswith(".jpg")]
    pictures.sort()

    if not pictures:
        print("No pictures on chosen monitoring.")
        return

    complete_pictures = [os.path.join(monitoring_path, picture) for picture in pictures]

    video_name = f"timelapse_{chosen_monitoring}.mp4"
    video_path = os.path.join("timelapses", video_name)

    with imageio.get_writer(video_path, format="mp4", mode="I", fps=30) as writer:
        for picture in complete_pictures:
            frame = imageio.imread(picture)
            writer.append_data(frame)

    print(f"'{nombre_video}' in 'timelapses' directory.")

def main():
    if not os.path.exists("timelapses"):
        os.mkdir("timelapses")

    monitorings = list_monitorings()
    if not monitorings:
        print("No monitorings have been found.")
        return

    chosen_monitoring = obtain_chosen_monitoring(monitorings)
    create_timelapse(chosen_monitoring)

if __name__ == "__main__":
    main()
