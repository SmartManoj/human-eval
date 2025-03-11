import json

from pymsgbox import *
from human_eval.data import write_jsonl, read_problems

problems = read_problems()

import litellm
from dotenv import load_dotenv
import os
load_dotenv()

model = "Qwen/Qwen2.5-Coder-32B-Instruct"
base_url = os.getenv('base_url')
api_key = os.getenv('api_key')

def without_chat(prompt):
    import openai

    openai.api_key = api_key
    openai.base_url = base_url
    try:
        response = openai.completions.create(
            model=model,
            prompt=prompt,
            seed=42,
            temperature=0.0,
            top_p=1,
            max_tokens=1000,
        )
        return response.choices[0].text
    except Exception as e:
        print(f"Error during API call: {e}")
        return None

task_ids='''HumanEval/145'''.splitlines()

if 1:
    # system_prompt = """'Complete the following function according to its docstring. Do not include any explanations or additional text.' """
    # system_prompt = "# Don't add any test functions. Only complete this function and nothing else.\n"
    system_prompt = '"Don\'t add any test functions. Only complete this function and nothing else."\n\n'
    for task_id in task_ids:
        if task_id not in problems:
            continue
        prompt = (system_prompt + problems[task_id]["prompt"])
        print(f"\nTask: {task_id}")
        print(prompt)

        print(problems[task_id]["canonical_solution"])
        print(problems[task_id]["test"])
        print('-'*100)
        exit()