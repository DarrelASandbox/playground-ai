from langchain.llms.openai import OpenAI

API_KEY = ""

llm = OpenAI(openai_api_key=API_KEY)

result = llm("Write a very short poem")
print(result)
