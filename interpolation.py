import os
from PIL import Image
import numpy as np
import glob

def load_images_in_order(folder_path):
    # Load all image paths, sorted by filename
    image_paths = sorted(glob.glob(os.path.join(folder_path, "*.jpg")))
    images = [Image.open(img_path) for img_path in image_paths]
    return images, image_paths

def create_interpolated_frame(frame1, frame2):
    # Convert frames to numpy arrays
    frame1_np = np.array(frame1)
    frame2_np = np.array(frame2)
    
    # Average the frames to create an interpolated frame
    interpolated_frame_np = (frame1_np.astype(np.float32) + frame2_np.astype(np.float32)) / 2.0
    interpolated_frame_np = interpolated_frame_np.astype(np.uint8)
    
    # Convert back to image
    interpolated_frame = Image.fromarray(interpolated_frame_np)
    return interpolated_frame

def process_and_save_interpolated_frames(folder_path, save_folder):
    images, image_paths = load_images_in_order(folder_path)
    
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    for i in range(len(images) - 1):
        frame1 = images[i]
        frame2 = images[i + 1]
        interpolated_frame = create_interpolated_frame(frame1, frame2)

        # Save the interpolated frame with a unique name
        save_path = os.path.join(save_folder, f"frame_{i+1:04d}.jpg")
        interpolated_frame.save(save_path)
    print(f"Generated {i+1} interpolated frames")
