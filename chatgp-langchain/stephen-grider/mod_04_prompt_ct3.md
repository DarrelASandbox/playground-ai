```sh
# Running with `langchain.debug = True`
python mod_04_prompt_ct3.py

# Output:
[chain/start] [1:chain:RetrievalQA] Entering Chain run with input:
{
  "query": "What is an interesting fact about the English language?"
}
[chain/start] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain] Entering Chain run with input:
[inputs]
/opt/homebrew/Caskroom/miniconda/base/envs/langchainenv2/lib/python3.11/site-packages/langchain/chains/llm.py:349: UserWarning: The apply_and_parse method is deprecated, instead pass an output parser directly to LLMChain.
  warnings.warn(
[chain/start] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain > 4:chain:LLMChain] Entering Chain run with input:
{
  "input_list": [
    {
      "context": "1. \"Dreamt\" is the only English word that ends with the letters \"mt.\"\n2. An ostrich's eye is bigger than its brain.\n3. Honey is the only natural food that is made without destroying any kind of life.",
      "question": "What is an interesting fact about the English language?"
    },
    {
      "context": "4. A snail can sleep for three years.\n5. The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis.'\n6. The elephant is the only mammal that can't jump.",
      "question": "What is an interesting fact about the English language?"
    },
    {
      "context": "86. Broccoli and cauliflower are the only vegetables that are flowers.\n87. The dot over an 'i' or 'j' is called a tittle.\n88. A group of owls is called a parliament.",
      "question": "What is an interesting fact about the English language?"
    },
    {
      "context": "118. The original Star-Spangled Banner was sewn in Baltimore.\n119. The average adult spends more time on the toilet than they do exercising.",
      "question": "What is an interesting fact about the English language?"
    }
  ]
}
[llm/start] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain > 4:chain:LLMChain > 5:llm:ChatOpenAI] Entering LLM run with input:
{
  "prompts": [
    "Human: Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\nIn addition to giving an answer, also return a score of how fully it answered the user's question. This should be in the following format:\n\nQuestion: [question here]\nHelpful Answer: [answer here]\nScore: [score between 0 and 100]\n\nHow to determine the score:\n- Higher is a better answer\n- Better responds fully to the asked question, with sufficient level of detail\n- If you do not know the answer based on the context, that should be a score of 0\n- Don't be overconfident!\n\nExample #1\n\nContext:\n---------\nApples are red\n---------\nQuestion: what color are apples?\nHelpful Answer: red\nScore: 100\n\nExample #2\n\nContext:\n---------\nit was night and the witness forgot his glasses. he was not sure if it was a sports car or an suv\n---------\nQuestion: what type was the car?\nHelpful Answer: a sports car or an suv\nScore: 60\n\nExample #3\n\nContext:\n---------\nPears are either red or orange\n---------\nQuestion: what color are apples?\nHelpful Answer: This document does not answer the question\nScore: 0\n\nBegin!\n\nContext:\n---------\n1. \"Dreamt\" is the only English word that ends with the letters \"mt.\"\n2. An ostrich's eye is bigger than its brain.\n3. Honey is the only natural food that is made without destroying any kind of life.\n---------\nQuestion: What is an interesting fact about the English language?\nHelpful Answer:"
  ]
}
[llm/start] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain > 4:chain:LLMChain > 6:llm:ChatOpenAI] Entering LLM run with input:
{
  "prompts": [
    "Human: Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\nIn addition to giving an answer, also return a score of how fully it answered the user's question. This should be in the following format:\n\nQuestion: [question here]\nHelpful Answer: [answer here]\nScore: [score between 0 and 100]\n\nHow to determine the score:\n- Higher is a better answer\n- Better responds fully to the asked question, with sufficient level of detail\n- If you do not know the answer based on the context, that should be a score of 0\n- Don't be overconfident!\n\nExample #1\n\nContext:\n---------\nApples are red\n---------\nQuestion: what color are apples?\nHelpful Answer: red\nScore: 100\n\nExample #2\n\nContext:\n---------\nit was night and the witness forgot his glasses. he was not sure if it was a sports car or an suv\n---------\nQuestion: what type was the car?\nHelpful Answer: a sports car or an suv\nScore: 60\n\nExample #3\n\nContext:\n---------\nPears are either red or orange\n---------\nQuestion: what color are apples?\nHelpful Answer: This document does not answer the question\nScore: 0\n\nBegin!\n\nContext:\n---------\n4. A snail can sleep for three years.\n5. The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis.'\n6. The elephant is the only mammal that can't jump.\n---------\nQuestion: What is an interesting fact about the English language?\nHelpful Answer:"
  ]
}
[llm/start] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain > 4:chain:LLMChain > 7:llm:ChatOpenAI] Entering LLM run with input:
{
  "prompts": [
    "Human: Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\nIn addition to giving an answer, also return a score of how fully it answered the user's question. This should be in the following format:\n\nQuestion: [question here]\nHelpful Answer: [answer here]\nScore: [score between 0 and 100]\n\nHow to determine the score:\n- Higher is a better answer\n- Better responds fully to the asked question, with sufficient level of detail\n- If you do not know the answer based on the context, that should be a score of 0\n- Don't be overconfident!\n\nExample #1\n\nContext:\n---------\nApples are red\n---------\nQuestion: what color are apples?\nHelpful Answer: red\nScore: 100\n\nExample #2\n\nContext:\n---------\nit was night and the witness forgot his glasses. he was not sure if it was a sports car or an suv\n---------\nQuestion: what type was the car?\nHelpful Answer: a sports car or an suv\nScore: 60\n\nExample #3\n\nContext:\n---------\nPears are either red or orange\n---------\nQuestion: what color are apples?\nHelpful Answer: This document does not answer the question\nScore: 0\n\nBegin!\n\nContext:\n---------\n86. Broccoli and cauliflower are the only vegetables that are flowers.\n87. The dot over an 'i' or 'j' is called a tittle.\n88. A group of owls is called a parliament.\n---------\nQuestion: What is an interesting fact about the English language?\nHelpful Answer:"
  ]
}
[llm/start] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain > 4:chain:LLMChain > 8:llm:ChatOpenAI] Entering LLM run with input:
{
  "prompts": [
    "Human: Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\nIn addition to giving an answer, also return a score of how fully it answered the user's question. This should be in the following format:\n\nQuestion: [question here]\nHelpful Answer: [answer here]\nScore: [score between 0 and 100]\n\nHow to determine the score:\n- Higher is a better answer\n- Better responds fully to the asked question, with sufficient level of detail\n- If you do not know the answer based on the context, that should be a score of 0\n- Don't be overconfident!\n\nExample #1\n\nContext:\n---------\nApples are red\n---------\nQuestion: what color are apples?\nHelpful Answer: red\nScore: 100\n\nExample #2\n\nContext:\n---------\nit was night and the witness forgot his glasses. he was not sure if it was a sports car or an suv\n---------\nQuestion: what type was the car?\nHelpful Answer: a sports car or an suv\nScore: 60\n\nExample #3\n\nContext:\n---------\nPears are either red or orange\n---------\nQuestion: what color are apples?\nHelpful Answer: This document does not answer the question\nScore: 0\n\nBegin!\n\nContext:\n---------\n118. The original Star-Spangled Banner was sewn in Baltimore.\n119. The average adult spends more time on the toilet than they do exercising.\n---------\nQuestion: What is an interesting fact about the English language?\nHelpful Answer:"
  ]
}
[llm/end] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain > 4:chain:LLMChain > 5:llm:ChatOpenAI] [12.68s] Exiting LLM run with output:
{
  "generations": [
    [
      {
        "text": "\"Dreamt\" is the only English word that ends with the letters \"mt.\"\nScore: 100",
        "generation_info": {
          "finish_reason": "stop"
        },
        "type": "ChatGeneration",
        "message": {
          "lc": 1,
          "type": "constructor",
          "id": [
            "langchain",
            "schema",
            "messages",
            "AIMessage"
          ],
          "kwargs": {
            "content": "\"Dreamt\" is the only English word that ends with the letters \"mt.\"\nScore: 100",
            "additional_kwargs": {}
          }
        }
      }
    ]
  ],
  "llm_output": {
    "token_usage": {
      "prompt_tokens": 359,
      "completion_tokens": 21,
      "total_tokens": 380
    },
    "model_name": "gpt-3.5-turbo",
    "system_fingerprint": ""
  },
  "run": null
}
[llm/end] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain > 4:chain:LLMChain > 6:llm:ChatOpenAI] [12.68s] Exiting LLM run with output:
{
  "generations": [
    [
      {
        "text": "The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis.'\nScore: 100",
        "generation_info": {
          "finish_reason": "stop"
        },
        "type": "ChatGeneration",
        "message": {
          "lc": 1,
          "type": "constructor",
          "id": [
            "langchain",
            "schema",
            "messages",
            "AIMessage"
          ],
          "kwargs": {
            "content": "The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis.'\nScore: 100",
            "additional_kwargs": {}
          }
        }
      }
    ]
  ],
  "llm_output": {
    "token_usage": {
      "prompt_tokens": 363,
      "completion_tokens": 31,
      "total_tokens": 394
    },
    "model_name": "gpt-3.5-turbo",
    "system_fingerprint": ""
  },
  "run": null
}
[llm/end] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain > 4:chain:LLMChain > 7:llm:ChatOpenAI] [12.68s] Exiting LLM run with output:
{
  "generations": [
    [
      {
        "text": "The dot over an 'i' or 'j' is called a tittle.\nScore: 100",
        "generation_info": {
          "finish_reason": "stop"
        },
        "type": "ChatGeneration",
        "message": {
          "lc": 1,
          "type": "constructor",
          "id": [
            "langchain",
            "schema",
            "messages",
            "AIMessage"
          ],
          "kwargs": {
            "content": "The dot over an 'i' or 'j' is called a tittle.\nScore: 100",
            "additional_kwargs": {}
          }
        }
      }
    ]
  ],
  "llm_output": {
    "token_usage": {
      "prompt_tokens": 354,
      "completion_tokens": 21,
      "total_tokens": 375
    },
    "model_name": "gpt-3.5-turbo",
    "system_fingerprint": ""
  },
  "run": null
}
[llm/end] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain > 4:chain:LLMChain > 8:llm:ChatOpenAI] [12.68s] Exiting LLM run with output:
{
  "generations": [
    [
      {
        "text": "This document does not answer the question\nScore: 0",
        "generation_info": {
          "finish_reason": "stop"
        },
        "type": "ChatGeneration",
        "message": {
          "lc": 1,
          "type": "constructor",
          "id": [
            "langchain",
            "schema",
            "messages",
            "AIMessage"
          ],
          "kwargs": {
            "content": "This document does not answer the question\nScore: 0",
            "additional_kwargs": {}
          }
        }
      }
    ]
  ],
  "llm_output": {
    "token_usage": {
      "prompt_tokens": 340,
      "completion_tokens": 12,
      "total_tokens": 352
    },
    "model_name": "gpt-3.5-turbo",
    "system_fingerprint": ""
  },
  "run": null
}
[chain/end] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain > 4:chain:LLMChain] [12.68s] Exiting Chain run with output:
{
  "outputs": [
    {
      "text": "\"Dreamt\" is the only English word that ends with the letters \"mt.\"\nScore: 100"
    },
    {
      "text": "The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis.'\nScore: 100"
    },
    {
      "text": "The dot over an 'i' or 'j' is called a tittle.\nScore: 100"
    },
    {
      "text": "This document does not answer the question\nScore: 0"
    }
  ]
}
[chain/end] [1:chain:RetrievalQA > 3:chain:MapRerankDocumentsChain] [12.68s] Exiting Chain run with output:
{
  "output_text": "\"Dreamt\" is the only English word that ends with the letters \"mt.\""
}
[chain/end] [1:chain:RetrievalQA] [13.63s] Exiting Chain run with output:
{
  "result": "\"Dreamt\" is the only English word that ends with the letters \"mt.\""
}
"Dreamt" is the only English word that ends with the letters "mt."
```
