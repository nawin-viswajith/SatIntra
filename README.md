# SaiIntra - SaiHackFest'24 (Frame Interpolation and Video Generation Project)

This project implements a pipeline for frame interpolation and video generation from a sequence of images. The pipeline includes frame interpolation, image cropping, and video creation. It is designed to handle large sequences of images, such as satellite images captured at regular intervals.

### Project Structure

The project consists of several Python scripts:

1. **`main.py`**: The main script to run the entire pipeline. It handles frame interpolation, image cropping, and video generation.
2. **`combinedFrameInterpolated.py`**: Contains the function to combine original frames with interpolated frames and rename them sequentially.
3. **`cropFolderImgs.py`**: Handles the cropping of images based on specified coordinates.
4. **`interpolation.py`**: Contains functions for interpolating frames between two consecutive images.
5. **`videoGen.py`**: Generates a video from a sequence of images.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `Pillow`
  - `numpy`
  - `opencv-python`

You can install the required packages using `pip`:

```bash
pip install pillow numpy opencv-python
```

## Usage
1. Run the Main Script

Execute **'main.py'** to start the pipeline. It will prompt you for the following inputs:
- **Original frames directory:** Path to the directory containing the original frames.
- **Directory to save files:** Path to the base directory where intermediate and final results will be saved.
- **Number of interpolation passes:** Number of times the interpolation process should be applied. Each pass doubles the number of interpolated frames.


2. Process Images

The script will:
- Perform frame interpolation based on the specified number of passes.
- Combine the original and interpolated frames.
- Crop the images based on the specified coordinates.
- Generate a video from the cropped images.
During execution, you will also be asked to input:
- Frame rate: Frame rate for the output video.


3. Output

The script will output:
- Interpolated frames: Saved in the base directory with the prefix **'interpolated_{pass}'**.
- Combined frames: Saved in the base directory with the prefix **'combined_{pass}'**.
- Cropped images: Saved in the base directory under the folder **'cropped'**.
- Video file: Saved as **'output.mp4'** in the base directory.


## Example
To run the project, use:
```
python main.py
```

Provide the necessary inputs when prompted, and the pipeline will process the images and generate the video accordingly.

## Notes
Ensure that the image filenames follow the pattern **'frame_XXX.jpg'** where 'XXX' is a zero-padded number.
The cropping coordinates are set to [0.0, 110, 1540.0, 1545.0]. Adjust these coordinates as needed for your specific images.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to fork the repository and submit pull requests. Issues and feature requests can be reported in the GitHub issues section.
