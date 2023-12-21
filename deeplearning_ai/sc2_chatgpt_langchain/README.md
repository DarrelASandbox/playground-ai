- [About The Project](#about-the-project)
- [Introduction](#introduction)
  - [Overview](#overview)
  - [Components](#components)
- [Models, Prompts and Output Parsers](#models-prompts-and-output-parsers)

&nbsp;

# About The Project

- [DeepLearning.AI Short Courses](https://learn.deeplearning.ai/)
- LangChain for LLM Application Development
- Harrison Chase

&nbsp;

# Introduction

## Overview

- Open-source development framework for LLM applications
- Python and JavaScript (TypeScript) packages
- Focused on composition and modularity
- Key value adds:
  - Modular components
  - Use cases: Common ways to combine components

## Components

- **Models**
  - LLMs: 20+ integrations
  - Chat Models
  - Text Embedding Models: 10+ integrations
- **Prompts**
  - Prompt Templates
  - Output Parsers: 5+ implementations
    - Retry/fixing logic
  - Example Selectors: 5+ implementations
- **Indexes**
  - Document Loaders: 50+ implementations
  - Text Splitters: 10+ implementations
  - Vector stores: 10+ integrations
  - Retrievers: 5+ integrations/implementations
- **Chains**
  - Prompt + LLM + Output parsing
  - Can be used as building blocks for longer chains
  - More application specific chains: 20+ types
- **Agents**
  - Agent Types: 5+ types
    - Algorithms for getting LLMs to use tools
  - Agent Toolkit: 10+ implementations
    - Agents armed with specific tools for a specific application

&nbsp;

# Models, Prompts and Output Parsers

- Direct API calls to OpenAI
- API calls through LangChain:
  - Prompts
  - Models
  - Output parsers
- **Why use prompt templates?**
  - Prompts can be long and detailed.
  - Reuse good with templates
  - LangChain also provides prompts for common operations.
- LangChain output parsing works with prompt templates
  - The library functions parse the LLM's output assuming that it will sue certain keywords.
  - Example here uses Thought, Action, Observation as keywords for Chain-of-Thought Reasoning. (ReAct)

```py
EXAMPLES = ["""
Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?

Thought: need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.

Action: Search [Colorado orogeny]

Observation: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas.

Thought: It does not mention the eastern sector. So I need to look up eastern sector.
Action: Lookup(eastern sector)
...

Thought: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.

Action: Finish[1,800 to 7,000 ft]""",
]
```

&nbsp;
