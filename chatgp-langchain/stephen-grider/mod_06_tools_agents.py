"""
This script integrates various components from the langchain library to create an 
AI agent capable of interacting with an SQLite database. 
It demonstrates how to set up a chat-based agent that can understand and 
respond to queries about the database, utilizing custom tools for 
running SQL queries and describing table schemas.

The script utilizes the OpenAIFunctionsAgent from langchain, 
along with custom tools for database interaction. 
The agent is configured with a specific prompt template and 
is capable of executing SQL queries and describing database tables.

Functions:
- list_tables: Retrieves the list of table names from the SQLite database.
- run_sqlite_query: Executes an SQL query against the SQLite database and returns the results.
- describe_tables: Provides the schema of specified tables in the SQLite database.

Classes:
- RunQueryArgsSchema: Pydantic schema for the 'run_sqlite_query' function arguments.
- DescribeTablesArgsSchema: Pydantic schema for the 'describe_tables' function arguments.

Usage:
The script is designed to be executed as a standalone module. 
Upon running, it initializes an agent capable of processing natural language queries
related to the database and executing corresponding SQL commands.
"""
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import SystemMessage
from tools.report import write_report_tool
from tools.sql import describe_tables_tool, list_tables, run_query_tool

load_dotenv()

chat = ChatOpenAI()

# Retrieve the list of tables in the SQLite database
TABLES = list_tables()

# Define the chat prompt template with a system message
# and placeholders for user input and agent scratchpad
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(
            content=(
                "You are an AI that has access to SQLITE database.\n"
                f"The database has tables of: {TABLES}"
                "Do not make any assumptions about what tables exist "
                "or what columns exists. Instead, use the 'describe_tables' function"
            )
        ),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# Define tools for running SQL queries and describing table schemas
tools = [run_query_tool, describe_tables_tool, write_report_tool]

# Create an OpenAIFunctionsAgent with the defined prompt and tools
agent = OpenAIFunctionsAgent(llm=chat, prompt=prompt, tools=tools)

# Create an AgentExecutor to execute the agent with verbose logging
agent_executor = AgentExecutor(agent=agent, verbose=True, tools=tools)

# Execute the agent to answer a query
# agent_executor("How many users have provided a shipping address?")
agent_executor(
    "Summarize the top 5 most popular products. Write the results to a report file."
)
