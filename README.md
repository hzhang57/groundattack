# GroundAttack

GroundAttack contains 3 modules: captioner, distractor, and selector.

## Captioner

The captioner relies on VLM to generate detailed captions for videos and images, which serves the later stage of negative option generation.

We implement `captioner_video.py` and `captioner_image.py` to extract captions from video frames and images in PIL format.

For processing videos in a folder, we use `main_capt_video.py` and `main_capt_image.py`.

### Loop Wrapper

#### Caption Video

#### Caption Image



# GroundAttack
GroundAttack contains 3 modules: captioner, distractor and selector.

## Captioner
Captioner relies on VLM to generate detailed captions for video and images, which serves for the later stage negative option generation.

We implement Captioner_Video.py and Captioner_Image.py to extract captions given video_frames, and images (PIL) format.
For processing videos under a folder, we use main_capt_video.py and main_capt_image.py to process.

Loop Wrapper
#### Caption Video


#### Caption Image