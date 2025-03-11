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

def completion(prompt):
    
    import openai

    openai.api_key = api_key
    openai.base_url = base_url

    response = openai.completions.create(
        model=model,
        prompt=prompt,
        seed=42,
        temperature=0.0,
        max_tokens=1000,
    )
    return response.choices[0].text




if 1:
    system_prompt = '"Don\'t add any test functions. Only complete this function and nothing else."\n\n'
    system_prompt = ''


    prompt = 'What is the length of a closed interval [a, b]?'
    prompt = (system_prompt + prompt)
    completion_result = completion(prompt)
    print(completion_result)
    