import os
import copy
import argparse
from tqdm import tqdm
from collections import defaultdict
from utils import *

# OpenAI
import openai

from prompts import demo_prompt_score


# load demo prompt
def verify_extraction(extraction):
    extraction = extraction.strip()
    if extraction == "" or extraction == None:
        return False
    return True


def create_test_prompt(demo_prompt, inst):
    demo_prompt = demo_prompt.strip()
    full_prompt = demo_prompt.format(question = inst['question'], gt=inst['answer'], extraction=inst['extraction'])
    return full_prompt


def match_answer(inst, api_key, quick_match=False):
    # quick match
    if quick_match:
        return '1' if inst['answer'] == inst['extraction'] else '0'
    # general extraction
    try:
        full_prompt = create_test_prompt(demo_prompt_score, inst)
        extraction = get_chat_response(full_prompt, api_key)
        return extraction.replace("Judgement:", "").strip()
    except Exception as e:
        print(e)
        print(f"Error in matching answer")

    return ""


def trunk_response(response, trunk_length):
    if trunk_length <= 0:
        return response
    else:
        return_res = ' '.join(response.split(' ')[-trunk_length:])
        return return_res

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    # input
    parser.add_argument('--answer_extraction_file', type=str, default='answer.json')
    parser.add_argument('--save_file', type=str, default='answer.json')
    # match
    parser.add_argument('--quick_match', action='store_true', help='use rules to match answer for some problems')
    # output
    parser.add_argument('--save_every', type=int, default=10, help='save every n problems')
    parser.add_argument('--cache', action='store_true', help='cache results')
    parser.add_argument('--trunk_response', type=int, default=-1, help='trunk response to the last n words')
    parser.add_argument('--api_key', type=str, help='api key for openai')
    # args
    args = parser.parse_args()

    # set api key
    openai.api_key = args.api_key

    # read results
    result_file = args.answer_extraction_file
    print(f"Reading {result_file}...")
    results = read_json(result_file)

    os.makedirs(os.path.dirname(args.save_file), exist_ok=True)
    if os.path.exists(args.save_file):
        save_results = json.load(open(args.save_file))
    else:
        save_results = []

    score_dict = defaultdict(lambda: defaultdict(list))
    score_version_dict = defaultdict(list)
    # tqdm, enumerate results
    for i, inst in enumerate(tqdm(results)):
        save_inst = save_results[i] if i < len(save_results) else copy.deepcopy(inst)
        if args.cache and 'judgement' in save_inst:
            pass
        else:
            judgement = match_answer(save_inst, args.api_key, args.quick_match)
            while True:
                if judgement.strip() not in ['0', '1']:
                    print('Wrong return format: ', judgement)
                    judgement = match_answer(save_inst, args.api_key, args.quick_match)
                else:
                    save_inst['judgement'] = int(judgement)
                    break

            save_results.append(save_inst)

        score_dict[save_inst['category']['subject']][save_inst['category']['subfield']].append(save_inst['judgement'])
        score_version_dict[save_inst['problem_version']].append(save_inst['judgement'])

        if i % args.save_every == 0 or i == len(results)-1:
            print(f"Saving results to {args.save_file}...")
            save_json(save_results, args.save_file)
            print(f"Results saved.")
    
    # subject level acc
    total_cnt, right_cnt = 0, 0
    for subject in score_dict:
        subject_total_cnt, subject_right_cnt = 0, 0
        for subfield in score_dict[subject]:
            subfield_total_cnt = len(score_dict[subject][subfield])
            subfield_right_cnt = len([inst for inst in score_dict[subject][subfield] if inst == 1])
            subject_total_cnt += subfield_total_cnt
            subject_right_cnt += subfield_right_cnt
            print(f"{subject}-{subfield} Acc: {(subfield_right_cnt/subfield_total_cnt):.3f}")
        print(f"{subject} Acc: {(subject_right_cnt/subject_total_cnt):.3f}")
        total_cnt += subject_total_cnt
        right_cnt += subject_right_cnt
    print(f"Total Acc: {(right_cnt/total_cnt):.3f}")

    # version level acc
    total_cnt, right_cnt = 0, 0
    for version in score_version_dict:
        version_total_cnt = len(score_version_dict[version])
        version_right_cnt = len([inst for inst in score_version_dict[version] if inst == 1])
        total_cnt += version_total_cnt
        right_cnt += version_right_cnt
        print(f"{version} Acc: {(version_right_cnt/version_total_cnt):.3f}")
        print(version_total_cnt)

    print(f"Acc: {(right_cnt/total_cnt):.3f}")     