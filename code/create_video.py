import moviepy.video.io.ImageSequenceClip	
import os
import re

image_folder = './figures/'
video_name = "sheepherding.mp4"
 

fps=10


# List images
image_files = [os.path.join(image_folder,img)
               for img in os.listdir(image_folder)
               if img.endswith(".png")]
# Sort by number
image_files.sort(key=lambda x: int(re.sub(r'./figures/(\d+)\.png', r'\1', x)))

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile(video_name)