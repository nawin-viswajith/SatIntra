import os
import time
from combineFrameInterpolated import combinedFolder
from cropFolderImgs import process_images
from interpolation import process_and_save_interpolated_frames
from videoGen import create_video_from_images

def main():
    start_time = time.time()

    original_frame_path = input("Enter original frames directory: ").strip()
    base_directory = input("Enter directory to save files: ").strip()
    interpolation_factor = int(input("Enter the number of interpolation passes (interpolation factor = 2^pass): "))

    # Interpolation of frames
    for i in range(interpolation_factor):
        print(f"\nFrame generation: Pass {i}")

        interpolate_folder = os.path.join(base_directory, f'interpolated_{i}')
        combined_folder = os.path.join(base_directory, f'combined_{i}')
        
        process_and_save_interpolated_frames(original_frame_path, interpolate_folder)
        combinedFolder(original_frame_path, interpolate_folder, combined_folder)

        original_frame_path = combined_folder

    # Crop image folder
    print("\nCropping images")
    source_folder = original_frame_path
    destination_folder = os.path.join(base_directory, f'cropped')
    crop_coords = [0.0, 110, 1540.0, 1545.0]  
    process_images(source_folder, destination_folder, crop_coords)

    end_time = time.time()

    # Video Generation
    image_folder = destination_folder  
    output_video_file = os.path.join(base_directory, 'output.mp4')
    frame_rate = int(input('\nEnter frame rate: ')) 
    
    create_video_from_images(image_folder, output_video_file, frame_rate)
    
    video_gen_time = time.time()
    
    print(f"\nTime taken for image interpolation is {end_time-start_time}")
    print(f"Time taken for video generation is {video_gen_time-end_time}")

if __name__ == "__main__":
    main()