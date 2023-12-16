import os

import openai
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


PROMPT1 = r"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
"""

# Boie is a real company, the product name is not real.
response1 = get_completion(PROMPT1)
print(response1)
