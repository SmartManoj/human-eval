import json
import os
from pymsgbox import *
from human_eval.data import write_jsonl, read_problems
from dotenv import load_dotenv
import openai

load_dotenv()

problems = read_problems()

model = os.getenv('model')
base_url = os.getenv('base_url')
api_key = os.getenv('api_key')

openai.api_key = api_key
openai.base_url = base_url

def completion(prompt):
    response = openai.completions.create(
        model=model,
        prompt=prompt,
        seed=42,
        temperature=0.0,
        max_tokens=1000,
        stop=[ '```', '<stop>'],
    )
    return response.choices[0].text, response.choices[0].finish_reason

task_ids=problems.keys()
# task_ids='''HumanEval/132'''.splitlines()
problems={task_id:problems[task_id] for task_id in task_ids}
total_tasks=len(problems)
one_task=0
if 1:
    initial_prompt = '"Don\'t add any test functions. Only complete this function and nothing else."\n\n'
    initial_prompt = '"Don\'t add any test functions. Complete this function very carefully based on the docstring and add <stop>. Don\'t make any mistakes. Don\'t add any other texts."\n\n'
    initial_prompt = '"Reason step by step carefully. Make sure the logic applies to all cases. Then complete the function and add <stop>."\n\n'
    for k,task_id in enumerate(problems):
        print(f"{k}/{total_tasks}")
        prompt = (initial_prompt + problems[task_id]["prompt"]).replace('even digits', 'single even digit integers')
        print(task_id)
        print(prompt)
        completion_result, stop_reason = completion(prompt)
        data = {
            "task_id": task_id,
            "prompt": prompt,
            "completion": completion_result,
            "stop_reason": stop_reason
        }
        print(completion_result)
        print(f"Stop reason: {stop_reason}")
        if not one_task:
            with open("results.jsonl", "a") as file:
                file.write(json.dumps(data) + "\n")
            # break
        else:
            exit()
if not one_task:
    alert("done")