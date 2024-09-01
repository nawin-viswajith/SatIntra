import os
from PIL import Image

def resize_image(image, target_width, target_height):
    """Resize the image to fit within target dimensions while maintaining aspect ratio."""
    image.thumbnail((target_width, target_height), Image.LANCZOS)
    return image

def calculate_crop_coords(original_size, crop_coords, target_size):
    """Calculate crop coordinates based on the ratio of the original size to the target size."""
    orig_width, orig_height = original_size
    crop_x1, crop_y1, crop_x2, crop_y2 = crop_coords
    target_width, target_height = target_size

    # Calculate crop box coordinates based on the target size
    ratio_width = target_width / orig_width
    ratio_height = target_height / orig_height

    crop_x1 = int(crop_x1 * ratio_width)
    crop_y1 = int(crop_y1 * ratio_height)
    crop_x2 = int(crop_x2 * ratio_width)
    crop_y2 = int(crop_y2 * ratio_height)

    return crop_x1, crop_y1, crop_x2, crop_y2

def process_images(source_folder, destination_folder, crop_coords):
    """Process images in the source folder and save cropped images to the destination folder."""
    # Ensure destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Loop through all images in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            file_path = os.path.join(source_folder, filename)
            image = Image.open(file_path)
            
            # Calculate new crop coordinates
            crop_coords_new = calculate_crop_coords(image.size, crop_coords, (1540, 1545))

            # Crop the image
            cropped_image = image.crop(crop_coords_new)

            # Save the cropped image
            save_path = os.path.join(destination_folder, filename)
            cropped_image.save(save_path)
    print("Cropping done!")
