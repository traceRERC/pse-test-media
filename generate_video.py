import cv2
import os
import csv
import argparse
from utils.json_utils import merge_with_config

def read_csv(file_path):
    csv_dir = os.path.dirname(file_path)
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [os.path.join(csv_dir, row['image_path']) for row in reader]

def generate_video(json_file, padding_frames=None):
    # Load the JSON data
    data = merge_with_config(json_file)


    # Get JSON file's basename
    basename = os.path.basename(json_file).split('.')[0]
    
    # Set default CSV location if not specified in the JSON
    csv_path = os.path.join(os.path.dirname(json_file), f"{basename}_src/framelist.csv")
    
    # Read the CSV file containing frame paths
    frame_paths = read_csv(csv_path)
    
    # Print the read frame paths for debugging
    print("Read frame paths:")
    for frame_path in frame_paths:
        print(frame_path)
    
    # Extract video properties from JSON
    framerate = data.get('framerate', 30)
    codec = data.get('codec', 'ffv1')
    video_extension = data.get('video_extension', 'avi')
    
    # Extract padding from JSON, if specified
    json_padding = data.get('padding', 0)
    
    # Resolve padding: Use command line padding if provided, else use JSON padding
    if padding_frames is None:
        padding_frames = json_padding
    elif padding_frames != json_padding:
        print(f"Warning: Padding specified in JSON ({json_padding}) is overridden by command line option ({padding_frames}).")
    
    # Make 'videos/' subdirectory
    save_dir = os.path.join(os.path.dirname(json_file), "videos") 
    os.makedirs(save_dir, exist_ok=True)

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*codec)
    output_video = os.path.join(save_dir, f"{basename}.{video_extension}")
    
    # Print the first frame path for debugging
    first_frame_path = frame_paths[0]
    print(f"Reading first frame from: {first_frame_path}")

    # Read the first frame
    first_frame = cv2.imread(first_frame_path)
    if first_frame is None:
        raise FileNotFoundError(f"Cannot read the first frame from path: {first_frame_path}")
    
    height, width, _ = first_frame.shape
    video_writer = cv2.VideoWriter(output_video, fourcc, framerate, (width, height))
    
    # Add padding frames by repeating the first frame
    for _ in range(padding_frames):
        video_writer.write(first_frame)
    
    # Add each frame to the video writer
    for frame_path in frame_paths:
        frame = cv2.imread(frame_path)
        if frame is None:
            print(f"Warning: Cannot read frame from path: {frame_path}")
            continue
        video_writer.write(frame)
    
    # Release the video writer
    video_writer.release()
    print(f"Video saved to {output_video}")

# Command line execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a video as specified in a JSON (that references CSV file listing of frames).')
    parser.add_argument('json_file', help='Path to the JSON file.')
    parser.add_argument('--padding', type=int, help='Number of padding frames to add at the start.')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call the function with parsed arguments
    generate_video(args.json_file, args.padding)
