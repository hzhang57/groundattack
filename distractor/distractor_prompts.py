
negative_prompt_128 = """
You are an expert in generating challenging distractors for image-based questions and answering. Given an image description, a question, and its correct answer, create 128 confusing yet incorrect answer options. Follow these guidelines strictly:
1. Grounded in the image: Each negative option must accurately describe events, actions, or details actually depicted in the image description.
2. Specifically Incorrect: Ensure each negative option does not correctly answer the provided question.
3. Plausibly Confusing: Craft options that could appear correct to a model lacking deeper reasoning about temporal order, causality, object references, intentions, or relationships.
4. Deceptively Similar: Structure options to closely resemble the correct answer in terms of content, sequence, or entities involved, challenging superficial matching strategies.
5. Relevance: Avoid introducing details or actions not present in the video or clearly irrelevant to the scenario described.
An Example like this:
[Image Description]: A white dog is lying on a pet bed...
[Question]: what does the white dog do after going to the cushion?
[Correct Answer]: Smell the black dog
[Negative Options]:
(0) Lie down on the pet bed.
(1) Walk towards the black dog.
(2) Explore the the pet bed.
(3) Watchthe black dog.
...
"""