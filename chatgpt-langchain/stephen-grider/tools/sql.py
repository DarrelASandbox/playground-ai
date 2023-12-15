"""
This module provides tools for interacting with an SQLite database using the langchain library. 
It includes functions to list tables in the database, execute SQL queries,
and describe the schemas of specific tables. 
These tools are designed to be used with the langchain's OpenAIFunctionsAgent
for natural language processing and database querying.

Functions:
- list_tables: Lists the names of all tables in the SQLite database.
- run_sqlite_query: Executes a given SQL query on the SQLite database and returns the results.
- describe_tables: Provides the schema for specified tables in the database.

Classes:
- RunQueryArgsSchema: Defines the schema for arguments to the 'run_sqlite_query' function.
- DescribeTablesArgsSchema: Defines the schema for arguments to the 'describe_tables' function.

Usage:
These functions are intended to be used as tools within the langchain framework, particularly
with OpenAIFunctionsAgent for processing natural language queries related to database operations.
"""
import sqlite3
from typing import List

from langchain.tools import Tool
from pydantic.v1 import BaseModel

# Connect to the SQLite database
conn = sqlite3.connect("db.sqlite")


def list_tables():
    """
    Retrieves a list of all table names in the SQLite database.

    Returns:
        str: A newline-separated string of table names.
    """
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = c.fetchall()
    return "\n".join(row[0] for row in rows if row[0] is not None)


def run_sqlite_query(query):
    """
    Executes a SQL query against the SQLite database.

    Args:
        query (str): The SQL query to be executed.

    Returns:
        list: The result of the SQL query execution, or an error message in case of failure.
    """
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return f"The following error occurred: {str(err)}"


class RunQueryArgsSchema(BaseModel):
    query: str


# Define a tool for running SQL queries
run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Run a sqlite query.",
    func=run_sqlite_query,
    args_schema=RunQueryArgsSchema,
)


def describe_tables(table_names):
    """
    Describes the schema of the specified tables in the SQLite database.

    Args:
        table_names (List[str]): A list of table names whose schema is to be retrieved.

    Returns:
        str: A newline-separated string containing the schema of each specified table.
    """
    c = conn.cursor()
    tables = ", ".join("'" + table + "'" for table in table_names)
    rows = c.execute(
        f"SELECT sql FROM sqlite_master WHERE type='table' and NAME IN ({tables});"
    )
    return "\n".join(row[0] for row in rows if row[0] is not None)


class DescribeTablesArgsSchema(BaseModel):
    table_names: List[str]


# Define a tool for describing table schemas
describe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, returns the schema of those tables",
    func=describe_tables,
    args_schema=DescribeTablesArgsSchema,
)
