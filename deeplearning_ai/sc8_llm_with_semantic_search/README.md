&nbsp;

# About The Project

- [DeepLearning.AI Short Courses](https://learn.deeplearning.ai/)
- Large Language Models with Semantic Search
- Cohere
- Jay Allamar & Luis Serrano

&nbsp;

# Course Outline

- **Keyword vs. Semantic Search**: Keyword search relies on matching documents with queries based on the frequency of words, while semantic search utilizes the actual semantic meaning of texts, focusing on the context and intent behind queries rather than just the words themselves.
- **Ranking Responses**: Responses are ranked by relevance in a process called re-ranking, which orders search results based on their significance to the query, enhancing the precision of keyword searches.
- **Embeddings**: Embeddings are a tool in natural language processing that associates texts with vectors of numbers, allowing for the representation of textual information in a numerical space, facilitating the measurement of semantic similarities between texts.
- **Dense Retrieval**: Dense retrieval improves upon keyword search by using embeddings to conduct searches based on the semantic meaning of texts. This approach retrieves documents that are semantically closest to the query in the space of embeddings, significantly enhancing the accuracy of search results.
- **Evaluation Methods**: The course details effective ways to evaluate search algorithms, ensuring their effectiveness in delivering relevant and accurate search results.
- **Search-Powered LLMs**: Large Language Models (LLMs) enhanced with search capabilities, especially through dense retrieval, exhibit vastly improved question-answering capabilities. They first search for and retrieve relevant documents based on semantic understanding and then generate answers from this retrieved information, leveraging the depth and accuracy of the search results.

&nbsp;

# Keyword Search

- Weaviate is an open source database. It has keyword search capabilities, but also vector search capabilities that rely on language models.
- **Query**: What color is the grass?

|                Responses                | Number of words in common |
| :-------------------------------------: | :-----------------------: |
|        Tomorrow **is** Saturday         |             1             |
|         **The grass is** green          |             3             |
| **The** capital of Canada **is** Ottawa |             2             |
|         **The** sky **is** blue         |             2             |
|         A whale **is** a mammal         |             1             |

![search_at_a_high_level](diagrams/search_at_a_high_level.png)

![keyword_search_internals](diagrams/keyword_search_internals.png)

![limitation_of_keyword_matching](diagrams/limitation_of_keyword_matching.png)

- Language models can improve both search stages

![improve_both_search_stages](diagrams/improve_both_search_stages.png)

&nbsp;

# Embeddings

- The Cohere library is an extensive library of functions that use large language models and they can be called via API calls.

![embeddings](diagrams/embeddings.png)

![word_embeddings](diagrams/word_embeddings.png)

![text_embeddings](diagrams/text_embeddings.png)

&nbsp;
