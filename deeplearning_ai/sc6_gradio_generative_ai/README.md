&nbsp;

# About The Project

- [DeepLearning.AI Short Courses](https://learn.deeplearning.ai/)
- Building Generative AI Applications with Gradio
- Hugging Face

&nbsp;

# Introduction

- The course aims to teach how to showcase generative AI systems, like text summarization, name entity recognition, image captioning, image generation using diffusion models, and LLM-based chatbots, using Gradio.

&nbsp;

# NLP Tasks interface

## Small Specialist Model

- Designed for a specific task
- Similar performance as a general purpose LLM
- Cheaper and faster to run compared to a general purpose LLM

## BART Large CNN Model

- This model uses a process called distillation.
- Distillation uses the predictions of a large model to train a smaller model.
- We are using the [**shleifer/distibart-cnn-12-6**](https://huggingface.co/sshleifer/distilbart-cnn-12-6), a 306M parameter distilled model trained by Facebook.

## Bert Model

- Bert is a Machine Learning model for natural language processing.
- When parsing a text, it is useful to identify specific entities such as persons, companies, places, etc.
- To do so, we are using [**bert-base-NER**](https://huggingface.co/dslim/bert-base-NER), a 108M parameter fine-tuned BERT model that is ready to use for Named Entity Recognition (NER).
- **bert-base-NER** has been trained to recognize four types of entities: location (LOC), organizations (ORG), person (PER) and Miscellaneous (MISC).

&nbsp;

# Image Captioning App

- [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)

&nbsp;

# Image Generation App

## Diffusion Model

- Text-to-image model generates images from input text.
- We are using an open-source [**runwayml/stable-diffusion-v1-5**](https://huggingface.co/runwayml/stable-diffusion-v1-5) using the 🧨 diffusers library.

&nbsp;
