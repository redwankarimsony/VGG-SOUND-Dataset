import os
import pandas as pd
import subprocess

# Set the output directory
output_dir = "VGG-SOUND"
os.makedirs(output_dir, exist_ok=True)

# Path to the cookies file (Ensure this exists)
cookies_file = "cookies.txt"

# Load the dataframe (replace with actual file if reading from CSV)
data = pd.DataFrame({
    "video_id": ["---g-f_I2yQ", "--0PQM4-hqg", "--56QUhyDQM"],
    "start_time": [1, 30, 185],
    "end_time": [11, 40, 195],
    "action": ["people marching", "waterfall burbling", "playing tennis"],
    "split": ["test", "train", "train"],
    "idx": [1, 2, 3]
})

# Loop through each row and download the video clip
for _, row in data.iterrows():
    video_id = row["video_id"]
    start_time = row["start_time"]
    end_time = row["end_time"]

    # Define the output file path
    output_filename = f"V={video_id}_{start_time}_{end_time}.mkv"
    output_path = os.path.join(output_dir, output_filename)

    # Construct yt-dlp command with cookies
    command = [
        "yt-dlp",
        "--cookies", cookies_file,  # Include cookies file for authentication
        "-f", "bestvideo[height<=480]+bestaudio/best[height<=480]",
        f"https://youtube.com/watch?v={video_id}",
        "--output", f"{output_path}.%(ext)s",
        "--download-sections", f"*{start_time}-{end_time}"  # Ensure only the required segment is downloaded
    ]

    # Run the command
    print(f"Downloading: {output_path}")
    subprocess.run(command, check=True)

print("All downloads completed and saved in 'VGG-SOUND' folder.")
