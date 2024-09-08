import json
from PIL import Image

import openai

from decouple import config

openai.api_key = config('OPEN_AI_KEY')
openai.organization = config('OPEN_AI_ORG')
# Function to query the language model
def query_llm(prompt, api_key, model="gpt-4o-mini"):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system",
             "content": "You are an assistant that checks if captions follow an agent-action-patient pattern."},
            {"role": "user", "content": prompt}
        ],
        #prompt=prompt,
        max_tokens=100,
        temperature=0.3
    )
    return response['choices'][0]['message']['content'].strip()

# Function to determine if a caption follows agent-action-patient pattern
def is_agent_action_patient(caption, api_key):
    prompt = f"Does the following caption follow the agent-action-patient pattern? Example of a valid pattern:" \
             f" 'The dog was stung by the bee' (True, agent: bee, action: sting, patient: dog).\n\nCaption: '{caption}'\n\nAnswer ONLY with True or False."
    return query_llm(prompt, api_key) == "True"

# Function to filter dataset based on agent-action-patient pattern
def filter_agent_action_patient(data, api_key):
    filtered_data = []
    relevant_ids = []

    for entry in data:
        if is_agent_action_patient(entry['caption_0'], api_key) or is_agent_action_patient(entry['caption_1'], api_key):
            filtered_data.append(entry)
            relevant_ids.append(entry['id'])

    return filtered_data, relevant_ids


# Example dataset (replace with your full dataset)
# data = [
#     {"id": 122, "caption_0": "big fish beside a small person", "caption_1": "small fish beside a big person"},
#     {"id": 123, "caption_0": "the train is moving fast while the person is still", "caption_1": "the train is still while the person is moving fast"},
#     {"id": 124, "caption_0": "they're enjoying hot water on a cold day", "caption_1": "they're enjoying cold water on a hot day"},
#     {"id": 126, "caption_0": "the bird eats a snake", "caption_1": "the snake eats a bird"},
#     # Add more captions here
# ]
datajsonl = "winoground.jsonl"

data = []
with open(datajsonl, 'r') as file:
    for line in file:
        entry = json.loads(line)
        data.append(entry)

#data = data[:10]
# Your OpenAI API key
api_key = openai.api_key

# Filter the dataset
filtered_data, relevant_ids = filter_agent_action_patient(data, api_key)

# Output the filtered dataset
for entry in filtered_data:
    print(f"ID: {entry['id']}, Caption 0: {entry['caption_0']}, Caption 1: {entry['caption_1']}")

print("Relevant IDs:", relevant_ids)