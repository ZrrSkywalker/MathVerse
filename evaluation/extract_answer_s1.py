import os
import copy
import argparse
from tqdm import tqdm
from collections import defaultdict
from utils import *

# OpenAI
import openai

from prompts import demo_prompt_extract


def verify_extraction(extraction):
    extraction = extraction.strip()
    if extraction == "" or extraction == None:
        return False
    return True


def create_test_prompt(demo_prompt, response, inst):
    demo_prompt = demo_prompt.strip()
    test_prompt = f"Model response: '{response}'\nExtracted Answer: "
    full_prompt = f"{demo_prompt}\n\n{test_prompt}"
    return full_prompt


def extract_answer(response, inst, api_key):
    # general extraction
    try:
        full_prompt = create_test_prompt(demo_prompt_extract, response, inst)
        extraction = get_chat_response(full_prompt, api_key)
        return extraction
    except Exception as e:
        print(e)
        print(f"Error in extracting answer for {response}")
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
    parser.add_argument('--model_output_file', type=str, default='output.json')
    parser.add_argument('--save_file', type=str, default='answer.json')
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
    result_file = args.model_output_file
    print(f"Reading {result_file}...")
    results = read_json(result_file)

    os.makedirs(os.path.dirname(args.save_file), exist_ok=True)
    if os.path.exists(args.save_file):
        save_results = json.load(open(args.save_file))
    else:
        save_results = []

    score_dict = defaultdict(lambda: defaultdict(list))
    score_dict_record = defaultdict(list)
    score_version_dict = defaultdict(list)

    # enumerate results
    for i, inst in enumerate(tqdm(results)):
        save_inst = save_results[i] if i < len(save_results) else copy.deepcopy(inst)
        if args.cache and 'extraction' in save_inst:
            pass
        else:
            if 'model_answer' in save_inst:
                response = save_inst['model_answer']  
            else:
                response = ''
                print(save_inst)
                print("######### NO MODEL ANSWER ###########")  # some model may output nothing due to safety
            response = trunk_response(response, args.trunk_response)

            extraction  = extract_answer(response, save_inst, args.api_key)
            save_inst['extraction'] = extraction.replace('Extracted Answer: ', '').strip()  # sometimes gpt will repeat
            save_results.append(save_inst)

        if i % args.save_every == 0 or i == len(results) - 1:
            print(f"Saving results to {args.save_file}...")
            save_json(save_results, args.save_file)
            print(f"Results saved.")