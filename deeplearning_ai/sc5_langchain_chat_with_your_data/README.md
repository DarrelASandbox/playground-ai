&nbsp;

# About The Project

- [DeepLearning.AI Short Courses](https://learn.deeplearning.ai/)
- LangChain Chat with Your Data
- Harrison Chase

&nbsp;

# Introduction

## Overview

- Open-source development framework for building LLM applications
- Python and TypeScript packages
- Focused on composition and modularity
- Key value adds:
  - Modular components (and implementations of those components)
  - Use cases: Common ways to combine components those components together

## Components

- **Prompts**
  - Prompt Templates
  - Output Parsers: 5+ implementations
    - Retry/fixing logic
  - Example Selectors: 5+ implementations
- **Models**
  - LLMs: 20+ integrations
  - Chat Models
  - Text Embedding Models: 10+ integrations
- **Indexes**
  - Document Loaders: 50+ implementations
  - Text Splitters: 10+ implementations
  - Vector stores: 10+ integrations
  - Retrievers: 5+ integrations/implementations
- **Chains**
  - Can be used as building blocks for other chains
  - More application specific chains: 20+ different types
- **Agents**
  - Agent Types: 5+ types
    - Algorithms for getting LLMs to use tools
  - Agent Toolkit: 10+ implementations
    - Agents armed with specific tools for a specific application

![retrieval_augmented_generation](diagrams/retrieval_augmented_generation.png)

&nbsp;

# Document Loading

## Loaders

- Loaders deal with the specifics of accessing and converting data
  - Accessing
    - Web Sites
    - Data Bases
    - YouTube
    - arXiv
    - ...
  - Data Types
    - PDF
    - HTML
    - JSON
    - Word, PowerPoint
- Returns a list of `Document` objects:

![document_objects](diagrams/document_objects.png)

![document_loaders](diagrams/document_loaders.png)

&nbsp;
