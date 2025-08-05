# GroundAttack

GroundAttack contains 3 modules: Captioner, Distractor, and Selector.

## Captioner

The captioner relies on VLM to generate detailed captions for videos and images, which serves the later stage of negative option generation.

We implement `captioner_video.py` and `captioner_image.py` to extract captions from video frames and images in PIL format.

For processing videos or images under a folder, we use `main_capt_video.py` and `main_capt_image.py`.
