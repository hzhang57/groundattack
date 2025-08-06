
class caption_wrapper:
    def __init__(self, vlm_model, caption_prompt, print_process=False):
        self.vlm = vlm_model
        self.caption_prompt = caption_prompt
        self.print_process = print_process

    def generate_caption(self, images):
        # images是PIL文件列表
        num_images = len(images)
        image_placeholder = "<image>"*num_images

        text = "{}\n{}".format(image_placeholder, self.caption_prompt)

        captioned_text = self.vlm.predict(images, text)

        if self.print_process:
            print("Captioned Text:", captioned_text)

        return captioned_text
