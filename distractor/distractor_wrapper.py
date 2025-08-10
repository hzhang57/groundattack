from distractor.utils import remove_label
from distractor.utils import parse_numbered_strings_line_by_line
from distractor.utils import parse_numbered_list

class distractor_wrapper:
    def __init__(self, llm_name, llm_model, distractor_prompt, print_process=False):
        self.llm_name = llm_name
        self.llm = llm_model
        self.distractor_prompt = distractor_prompt
        self.print_process = print_process

    def generate_negatives(self, sample_caption, question, answer):

        answer = remove_label(answer)
        sample_template = 'Here is the Descrtion of my image, question, correct answer: \n[Image Description]:\n "{}"\n[Question]: {}\n[Correct Answer]: {}\n[Negative Options]:\n'.format(sample_caption, question, answer)
        text = "{}{}".format(self.distractor_prompt, sample_template)

        new_negatives = self.llm.text_predict(text)
        
        new_negatives_dict = {}
        if "gpt-oss" in self.llm_name:
            new_negatives_dict = parse_numbered_strings_line_by_line(new_negatives) ## For GPT-OSS-Parser
        elif "gpt-4o-mini" in self.llm_name:"
            new_negatives_dict = parse_numbered_list(new_negatives) ## For GPT-4O-Mini-Parser

        if self.print_process:
            print(text)
            print("New negatives:", new_negatives)
            print("New negatives dict:", new_negatives_dict)
        if len(new_negatives_dict) == 0:
            print("[WARNNING, distractor: No new negatives generated]")
        return new_negatives_dict
