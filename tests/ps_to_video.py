"""
ps_to_video.py

Convert a folder of PostScript (.ps) frames into an MP4 video.
No command-line arguments — just edit the config section below.

Requires:
    pip install pillow imageio imageio-ffmpeg numpy

On Windows, Ghostscript must be installed for Pillow to read .ps files:
    https://ghostscript.com/releases/
"""

import os
import glob
import numpy as np
from PIL import Image
import imageio.v2 as imageio
import time

INPUT_DIR = "frames_ps"           # Folder containing .ps frames
PATTERN = "frame_*.ps"            # Frame file naming pattern
OUTPUT_VIDEO = "output/orbit.mp4" # Where to save the video

FPS = 60                         # Frames per second
WIDTH = 1920                      # Output video width
HEIGHT = 1080                     # Output video height

CODEC = "libx264"                 # Video codec (imageio-ffmpeg)
QUALITY = 8                       # 0–10 (higher = better; default 8)


def main():
    # Find frames
    frame_paths = sorted(glob.glob(os.path.join(INPUT_DIR, PATTERN)))
    if not frame_paths:
        raise SystemExit(f"No .ps files found in {INPUT_DIR}/{PATTERN}")

    # Ensure output directory exists
    out_dir = os.path.dirname(OUTPUT_VIDEO)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    print(f"Found {len(frame_paths)} frame(s).")
    print(f"Saving video to: {OUTPUT_VIDEO}")
    print(f"Resolution: {WIDTH}x{HEIGHT} @ {FPS} FPS")

    writer = imageio.get_writer(
        OUTPUT_VIDEO,
        fps=FPS,
        codec=CODEC,
        quality=QUALITY,
        macro_block_size=1,
    )

    try:
        for idx, ps_path in enumerate(frame_paths, start=1):
            startTime = time.time()
            # Open PS file using Pillow (Ghostscript required)
            with Image.open(ps_path) as img:
                
                img = img.convert("RGBA")
                arr = np.array(img)
                
                white_mask = (arr[:, :, 0] > 240) & (arr[:, :, 1] > 240) & (arr[:, :, 2] > 240)
                arr[white_mask] = [0, 0, 0, 255]  # Set white pixels to black
                #bg = Image.new("RGBA", img.size, (0, 0, 0, 255))  # Black background
                #img = Image.alpha_composite(bg, img)
                img = Image.fromarray(arr, mode="RGBA")
                img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)

                frame = np.array(img)
                writer.append_data(frame)
            
            try:
                os.remove(ps_path)
            except OSError as e:
                print(f"Warning: could not delete {ps_path}: {e}")

            if idx % 25 == 0 or idx == len(frame_paths):
                print(f" time left: {(time.time() - startTime)*(len(frame_paths)-idx)/60:.1f} min")
                print(f"  Processed {idx}/{len(frame_paths)} frames")

    finally:
        writer.close()

    print("exported video successfully.")


if __name__ == "__main__":
    main()