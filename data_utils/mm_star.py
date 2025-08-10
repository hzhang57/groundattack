from data_utils.utils import save_image_to_folder
from data_utils.utils import split_question_into_query_and_options_0
from data_utils.utils import split_question_into_query_and_options_1
from data_utils.utils import split_question_into_query_and_options_2
from data_utils.utils import split_question_into_query_and_options_3
from data_utils.utils import remap_options_to_indices

class format_mmstar_dataset:

    def __init__(self, dataset, output_file, output_images_folder):
        self.dataset = dataset
        self.output_file = output_file
        self.output_images_folder = output_images_folder

    def split_question(self, question):
        options_dict = {}
        try:
             only_question, options_dict = split_question_into_query_and_options_0(question)
        except:
            print("[ERROR 0] in F0, options_dict is {}".format(options_dict.keys()))

        ## Not parse success by split_..._0
        if len(options_dict) == 0:
            try:
                only_question, options_dict = split_question_into_query_and_options_1(question)
            except:
                print("[ERROR 1]")

        ## Not success by split_..._0 and _1
        if len(options_dict) == 0:
            try:
                only_question, options_dict = split_question_into_query_and_options_2(question)
            except:
                print("ERROR 2")
        ## Not success by split_..._0 and _1 and _2
        if len(options_dict) == 0:
            try:
                only_question, options_dict = split_question_into_query_and_options_3(question)
            except:
                print("ERROR 3")
        #print(question)

        options_dict = remap_options_to_indices(options_dict)
        return only_question, options_dict

    def format_options_and_answer(self, options_dict, answer):
        index2ans = {}
        all_choices = []
        gt_answer = None
        opt_concat_str = "Select from options:\n"
        print(options_dict)

        for opt_key in options_dict.keys():
            opt_key_str  = "({})".format(opt_key)
            opt_full_str = "({}) {}".format(opt_key, options_dict[opt_key])
            index2ans[opt_key_str] = opt_full_str
            all_choices.append(opt_key_str)
            opt_concat_str += "{}\n".format(opt_full_str)
        gt_answer = index2ans["({})".format(answer)]
        ## 测试
        #print("index2ans {}".format(index2ans))
        #print("all_choices {}".format(all_choices))
        #print("gt_answer {}".format(gt_answer))
        #print("opt_concat_str {}".format(opt_concat_str))
        return index2ans, all_choices, gt_answer, opt_concat_str

    def format_a_sample(self, a_sample):
        index    = a_sample["index"]
        question = a_sample["question"]
        image    = a_sample["image"]
        quest_type = a_sample["category"]
        quest_type_l2 = a_sample["l2_category"]
        answer   = a_sample["answer"]
        answer =  ord(answer) - ord('A')# remapt A,B,C to 0, 1, 2 ..
        # split quesiton into question and options
        only_question, options_dict = self.split_question(question)
        ## remove original <image 1>
        only_question = only_question.replace('<image 1>', '')
        only_answer  = options_dict[answer]



        index2ans, all_choices, gt_answer, opt_concat_str = self.format_options_and_answer(options_dict, answer)

        new_question = "<image>\n" + only_question.strip() + "\n{}".format(opt_concat_str) ## Question, format <image>\n+text
        #print("**"*7)
        #print(question)
        #print(new_question)
        #print("**"*7)

        # save image into folder
        file_name = save_image_to_folder(image, self.output_images_folder, index)

        ## pack all indexes, question, options, answer, quest_type into a new dict
        new_sample = {}
        new_sample['id'] = index
        new_sample['quest_type'] = quest_type
        new_sample['quest_type_l2'] = quest_type_l2
        new_sample['index2ans'] = index2ans
        new_sample['all_choices'] = all_choices
        new_sample['image'] = file_name
        new_sample['only_question'] = only_question
        new_sample['only_answer'] = only_answer
        new_sample['conversations'] = [
            {
                'from': "human",
                'value': new_question
            },
            {
                'from': "gpt",
                'value': gt_answer
            }
        ]

        #print(new_sample)
        #print("**"*8)
        #print(new_question)
        #print(gt_answer)
        #print(new_sample)

        return new_sample

    def format(self):
        new_dataset = []
        n_vals = len(self.dataset)
        for ii in range(n_vals):
            a_sample = self.dataset[ii]
            a_new_sample = self.format_a_sample(a_sample)
            new_dataset.append(a_new_sample)
            #print(a_new_sample)

        ## save json
        return new_dataset

