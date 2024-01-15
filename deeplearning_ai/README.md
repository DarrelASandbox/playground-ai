```sh
# conda env setup
conda create --name dla pytorch torchvision -c pytorch
conda activate dla
pip install -r deeplearning_ai/requirements.txt

# langchain with openai 0.28
conda create --name lc -c conda-forge langchain openai==0.28 chromadb
conda activate lc
pip install -r deeplearning_ai/requirements2.txt
```
