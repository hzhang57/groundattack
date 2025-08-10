
### Prompt to convert video into detailed captions
caption_prompt = """
You are an expert video captioning assistant with exceptional observational and descriptive skills. Carefully analyze the provided video frames and generate captions and detailed descriptions that vividly and accurately convey the content. Structure your response clearly, covering the following points:
1. Overall Summary: Briefly summarize the central theme, context, and primary setting of the video in a concise and engaging manner.
2. Key Visual Details: Clearly describe the main characters, significant objects, and notable locations shown in the video. Highlight distinct visual features that help viewers visualize the scenes vividly.
3. Action Breakdown: Provide a sequential, step-by-step breakdown of the key actions and events occurring in the video, ensuring clarity in the order of occurrence.
4. Atmosphere and Mood: Describe the emotional tone, atmosphere, and any stylistic elements present. Identify aspects such as lighting, music, pacing, and visual style that contribute to the video's overall mood.
5. Text and Dialogue (if applicable): Include accurate transcriptions or summaries of important on-screen text or clearly audible dialogue, noting any critical details relevant to understanding the video’s context.
Ensure your response is articulate, engaging, and structured in a way that enables someone unfamiliar with the video to clearly visualize and comprehend its content.

"""

image_caption_prompt = """
You are an expert image captioner. Analyze the image and produce a description that includes:

1. objects: A comprehensive list of at least 6 distinct items seen.
2. attributes: For each object, list its color, size, and texture.
3. actions: Any motions or interactions happening.
4. spatial_relations: For each key pair, describe relative positions (e.g., “cup on table”).
5. scene: A single sentence summarizing the setting (e.g., “A cozy café interior at dusk”).

Use vivid, precise language and output a description.
"""



negative_prompt = """
You are an expert in generating challenging distractors for video-based questions. Given a video description, a question, and its correct answer, create 4 confusing yet incorrect answer options. Follow these guidelines strictly:
1. Grounded in the video: Each negative option must accurately describe events, actions, or details actually depicted in the video.
2. Specifically Incorrect: Ensure each negative option does not correctly answer the provided question.
3. Plausibly Confusing: Craft options that could appear correct to a model lacking deeper reasoning about temporal order, causality, object references, intentions, or relationships.
4. Deceptively Similar: Structure options to closely resemble the correct answer in terms of content, sequence, or entities involved, challenging superficial matching strategies.
5. Relevance: Avoid introducing details or actions not present in the video or clearly irrelevant to the scenario described.
An Example like this:
[Question]: what does the white dog do after going to the cushion?
[Correct Answer]: Smell the black dog
[Negative Options]:
(0) Lie down on the pet bed.
(1) Walk towards the black dog.
(2) Explore the the pet bed.
(3) Watchthe black dog.

"""

negative_prompt_10 = """
You are an expert in generating challenging distractors for video-based questions. Given a video description, a question, and its correct answer, create 10 confusing yet incorrect answer options. Follow these guidelines strictly:
1. Grounded in the video: Each negative option must accurately describe events, actions, or details actually depicted in the video.
2. Specifically Incorrect: Ensure each negative option does not correctly answer the provided question.
3. Plausibly Confusing: Craft options that could appear correct to a model lacking deeper reasoning about temporal order, causality, object references, intentions, or relationships.
4. Deceptively Similar: Structure options to closely resemble the correct answer in terms of content, sequence, or entities involved, challenging superficial matching strategies.
5. Relevance: Avoid introducing details or actions not present in the video or clearly irrelevant to the scenario described.
An Example like this:
[Question]: what does the white dog do after going to the cushion?
[Correct Answer]: Smell the black dog
[Negative Options]:
(0) Lie down on the pet bed.
(1) Walk towards the black dog.
(2) Explore the the pet bed.
(3) Watchthe black dog.
...
"""

negative_prompt_50 = """
You are an expert in generating challenging distractors for video-based questions. Given a video description, a question, and its correct answer, create 50 confusing yet incorrect answer options. Follow these guidelines strictly:
1. Grounded in the video: Each negative option must accurately describe events, actions, or details actually depicted in the video.
2. Specifically Incorrect: Ensure each negative option does not correctly answer the provided question.
3. Plausibly Confusing: Craft options that could appear correct to a model lacking deeper reasoning about temporal order, causality, object references, intentions, or relationships.
4. Deceptively Similar: Structure options to closely resemble the correct answer in terms of content, sequence, or entities involved, challenging superficial matching strategies.
5. Relevance: Avoid introducing details or actions not present in the video or clearly irrelevant to the scenario described.
An Example like this:
[Question]: what does the white dog do after going to the cushion?
[Correct Answer]: Smell the black dog
[Negative Options]:
(0) Lie down on the pet bed.
(1) Walk towards the black dog.
(2) Explore the the pet bed.
(3) Watchthe black dog.
...
"""

negative_prompt_100 = """
You are an expert in generating challenging distractors for video-based questions. Given a video description, a question, and its correct answer, create 100 confusing yet incorrect answer options. Follow these guidelines strictly:
1. Grounded in the video: Each negative option must accurately describe events, actions, or details actually depicted in the video.
2. Specifically Incorrect: Ensure each negative option does not correctly answer the provided question.
3. Plausibly Confusing: Craft options that could appear correct to a model lacking deeper reasoning about temporal order, causality, object references, intentions, or relationships.
4. Deceptively Similar: Structure options to closely resemble the correct answer in terms of content, sequence, or entities involved, challenging superficial matching strategies.
5. Relevance: Avoid introducing details or actions not present in the video or clearly irrelevant to the scenario described.
An Example like this:
[Question]: what does the white dog do after going to the cushion?
[Correct Answer]: Smell the black dog
[Negative Options]:
(0) Lie down on the pet bed.
(1) Walk towards the black dog.
(2) Explore the the pet bed.
(3) Watchthe black dog.
...
"""

format_option_prompt = """
You are given a list of options that:
May be inconsistently formatted (different capitalization, punctuation, etc.).
Vary greatly in length and style.
Your task is to:
1. Rephrase each option so they all have similar length (use concise but clear language).
2. Ensure each option has consistent capitalization and punctuation.
3. Present each option in a neatly formatted list with number.
4. Maintain the original meaning of each option.
5. keep word count in each option the same length.
Instructions:
1. Retain the essence of each option’s text but normalize length and correct spelling/grammar as needed.
2. Use the same overall format for every option (e.g., sentence case with a period at the end).
3. Return only the final, uniformly styled list.
Desired Output:
A neatly formatted list of consistently styled, similarly worded options, with minimal length variations.
[Example Options Format]:
(0) Lie down on the pet bed.
(1) Walk towards the black dog.
(2) Explore the the pet bed.
(3) Watchthe black dog.
...
Here is the list of options: 

"""

print("**"*10 + "Caption Prompt")
print(caption_prompt)
print("**"*10 + "Negative Prompt")
print(negative_prompt)
print("**"*10 + "Format Option Prompt")
print(format_option_prompt)
