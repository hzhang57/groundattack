## 用于图片描述的prompt
image_caption_prompt = """
You are an expert image captioner. Analyze the image and produce a description that includes:

1. objects: A comprehensive list of at least 6 distinct items seen.
2. attributes: For each object, list its color, size, and texture.
3. actions: Any motions or interactions happening.
4. spatial_relations: For each key pair, describe relative positions (e.g., “cup on table”).
5. scene: A single sentence summarizing the setting (e.g., “A cozy café interior at dusk”).

Use vivid, precise language and output a description.
"""


