import argparse

from langchain.chains import LLMChain
from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate

API_KEY = ""

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

llm = OpenAI(openai_api_key=API_KEY)

code_prompt = PromptTemplate(
    template="Write a short {language} function that will {task}",
    input_variables=["language", "task"],
)

code_chain = LLMChain(llm=llm, prompt=code_prompt)

result = code_chain({"language": args.language, "task": args.task})
print(result)
