a='results.jsonl_results.jsonl'
# a='results4.jsonl'
# a='results-final.jsonl_results.jsonl'
import json
ids= ['HumanEval/127']
with open(a, 'r') as f:
    for line in f:
        data = json.loads(line)
        if data['task_id'] in ids:
            continue
        if not data['passed']:
            print(data['task_id'])
            if 1:
                print(data['prompt'])
                print(data['completion'])
                print(data['result'])
                print('-'*100)
                # break

