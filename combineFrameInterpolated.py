import os
import shutil

def combinedFolder(source_frames_folder, interpolated_frames_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Get the list of files from the source folder
    frames = sorted([f for f in os.listdir(source_frames_folder) if f.startswith('frame_')])
    interpolated = sorted([f for f in os.listdir(interpolated_frames_folder) if f.startswith('frame_')])

    # Determine the number of frames and interpolated images
    num_frames = len(frames)
    num_interpolated = len(interpolated)

    # Calculate the number of images to process
    num_images = num_frames + num_interpolated
    print(f"Total number of frames {num_images}, i.e. original frames: {num_frames}, interpolated frames: {num_interpolated}")

    # Merge and rename the files
    i = 0
    j = 0
    while (i<num_frames):
        try:
            frame_new_filename = f'frame_{j+1:03d}.jpg'
            j+=1
            shutil.copy(os.path.join(source_frames_folder, frames[i]), os.path.join(destination_folder, frame_new_filename))
        except IndexError:
            pass

        try:
            interpolated_new_filename = f'frame_{j+1:03d}.jpg'
            j+=1
            shutil.copy(os.path.join(interpolated_frames_folder, interpolated[i]), os.path.join(destination_folder, interpolated_new_filename))
        except IndexError:
            pass
        i+=1

    print("Files have been successfully arranged and renamed.")
