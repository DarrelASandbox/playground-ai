from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from dotenv import load_dotenv

from tools.sql import run_query_tool

load_dotenv()

chat = ChatOpenAI()
prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

tools = [run_query_tool]

agent = OpenAIFunctionsAgent(llm=chat, prompt=prompt, tools=[run_query_tool])
agent_executor = AgentExecutor(agent=agent, verbose=True, tools=tools)
# agent_executor("How many users are in the database?")

# Invoking: `run_sqlite_query` with `SELECT COUNT(DISTINCT user_id) FROM users
# WHERE address IS NOT NULL`
# The following error occurred: no such column: user_id
# Invoking: `run_sqlite_query` with `SELECT COUNT(DISTINCT user_id) FROM orders
# WHERE shipping_address IS NOT NULL
# The following error occurred: no such column: shipping_address
# I apologize for the confusion. It seems that the column names I used in the query are incorrect.
# Could you please provide me with the correct column names for the user table
# and the shipping address column?
agent_executor("How many users have provided a shipping address?")
