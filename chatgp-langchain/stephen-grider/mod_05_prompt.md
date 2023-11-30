```sh
# Duplicate the data a few times if needed
python mod_04_facts.py

# Running with `langchain.debug = True`
python mod_05_prompt.py

# Output
[chain/start] [1:chain:RetrievalQA] Entering Chain run with input:
{
  "query": "What is an interesting fact about the English language?"
}
[chain/start] [1:chain:RetrievalQA > 3:chain:StuffDocumentsChain] Entering Chain run with input:
[inputs]
[chain/start] [1:chain:RetrievalQA > 3:chain:StuffDocumentsChain > 4:chain:LLMChain] Entering Chain run with input:
{
  "question": "What is an interesting fact about the English language?",
  "context": "1. \"Dreamt\" is the only English word that ends with the letters \"mt.\"\n2. An ostrich's eye is bigger than its brain.\n3. Honey is the only natural food that is made without destroying any kind of life.\n\n4. A snail can sleep for three years.\n5. The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis.'\n6. The elephant is the only mammal that can't jump.\n\n86. Broccoli and cauliflower are the only vegetables that are flowers.\n87. The dot over an 'i' or 'j' is called a tittle.\n88. A group of owls is called a parliament.\n\n118. The original Star-Spangled Banner was sewn in Baltimore.\n119. The average adult spends more time on the toilet than they do exercising."
}
[llm/start] [1:chain:RetrievalQA > 3:chain:StuffDocumentsChain > 4:chain:LLMChain > 5:llm:ChatOpenAI] Entering LLM run with input:
{
  "prompts": [
    "System: Use the following pieces of context to answer the user's question. \nIf you don't know the answer, just say that you don't know, don't try to make up an answer.\n----------------\n1. \"Dreamt\" is the only English word that ends with the letters \"mt.\"\n2. An ostrich's eye is bigger than its brain.\n3. Honey is the only natural food that is made without destroying any kind of life.\n\n4. A snail can sleep for three years.\n5. The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis.'\n6. The elephant is the only mammal that can't jump.\n\n86. Broccoli and cauliflower are the only vegetables that are flowers.\n87. The dot over an 'i' or 'j' is called a tittle.\n88. A group of owls is called a parliament.\n\n118. The original Star-Spangled Banner was sewn in Baltimore.\n119. The average adult spends more time on the toilet than they do exercising.\nHuman: What is an interesting fact about the English language?"
  ]
}
[llm/end] [1:chain:RetrievalQA > 3:chain:StuffDocumentsChain > 4:chain:LLMChain > 5:llm:ChatOpenAI] [3.07s] Exiting LLM run with output:
{
  "generations": [
    [
      {
        "text": "An interesting fact about the English language is that \"dreamt\" is the only English word that ends with the letters \"mt.\"",
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
            "content": "An interesting fact about the English language is that \"dreamt\" is the only English word that ends with the letters \"mt.\"",
            "additional_kwargs": {}
          }
        }
      }
    ]
  ],
  "llm_output": {
    "token_usage": {
      "prompt_tokens": 242,
      "completion_tokens": 26,
      "total_tokens": 268
    },
    "model_name": "gpt-3.5-turbo",
    "system_fingerprint": null
  },
  "run": null
}
[chain/end] [1:chain:RetrievalQA > 3:chain:StuffDocumentsChain > 4:chain:LLMChain] [3.07s] Exiting Chain run with output:
{
  "text": "An interesting fact about the English language is that \"dreamt\" is the only English word that ends with the letters \"mt.\""
}
[chain/end] [1:chain:RetrievalQA > 3:chain:StuffDocumentsChain] [3.07s] Exiting Chain run with output:
{
  "output_text": "An interesting fact about the English language is that \"dreamt\" is the only English word that ends with the letters \"mt.\""
}
[chain/end] [1:chain:RetrievalQA] [4.24s] Exiting Chain run with output:
{
  "result": "An interesting fact about the English language is that \"dreamt\" is the only English word that ends with the letters \"mt.\""
}
An interesting fact about the English language is that "dreamt" is the only English word that ends with the letters "mt."
```
