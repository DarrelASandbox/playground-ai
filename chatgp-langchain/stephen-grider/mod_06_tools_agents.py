from dotenv import load_dotenv
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import SystemMessage
from tools.sql import describe_tables_tool, list_tables, run_query_tool

load_dotenv()

chat = ChatOpenAI()

# [('users',), ('addresses',), ('products',), ('carts',), ('orders',), ('order_products',)]
TABLES = list_tables()
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(
            content=f"You are an AI that has access to SQLITE database.\n{TABLES}"
        ),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

tools = [run_query_tool, describe_tables_tool]

agent = OpenAIFunctionsAgent(llm=chat, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, verbose=True, tools=tools)
agent_executor("How many users have provided a shipping address?")
