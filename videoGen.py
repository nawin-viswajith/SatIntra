import cv2
import os

def create_video_from_images(image_folder, output_video_file, frame_rate):
    # Get a list of image files in the directory
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    image_files.sort()  # Sort images to maintain sequence

    # Check if there are images in the folder
    
    if not image_files:
        raise ValueError("No images found in the specified folder.")

    # Read the first image to get the dimensions
    first_image_path = os.path.join(image_folder, image_files[0])
    first_image = cv2.imread(first_image_path)
    height, width, layers = first_image.shape

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 file
    video_writer = cv2.VideoWriter(output_video_file, fourcc, frame_rate, (width, height))

    # Calculate video duration based on frame rate and number of images
    total_frames = len(image_files)
    video_duration = total_frames / frame_rate  # Duration in seconds

    # Print out the duration for verification
    print(f"Total frames: {total_frames}")
    print(f"Video duration: {video_duration} seconds")

    # Iterate through the images and write them to the video
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)
        video_writer.write(image)  # Write the frame

    # Release the VideoWriter object
    video_writer.release()
    print(f"Video saved!")
   