- [About The Project](#about-the-project)
- [Links](#links)
- [CLI](#cli)
- [env](#env)
  - [langchainenv](#langchainenv)
  - [pdf-dist](#pdf-dist)
    - [IMPORTANT](#important)
    - [Questions for tests](#questions-for-tests)
- [LangChain](#langchain)
- [Pinecone](#pinecone)
- [LangFuse](#langfuse)
- [Models](#models)
- [Semantic Search \& Embeddings](#semantic-search--embeddings)

&nbsp;

# About The Project

- ChatGPT and LangChain: The Complete Developer's Masterclass
- Intensive masterclass on ChatGPT, LangChain, and Python. Make production-ready apps focused on real-world AI integration
- [Stephen Grider](https://github.com/StephenGrider)

&nbsp;

# Links

- [pdf.ai](https://pdf.ai/)
- [langchain](https://github.com/langchain-ai/langchain)
- [python.langchain docs](https://python.langchain.com/docs/get_started/quickstart)
- [openai api key](https://platform.openai.com/api-keys)
- [chromaDB](https://github.com/chroma-core/chroma)

# CLI

```sh
conda create --name langchainenv -c conda-forge langchain openai python-dotenv tiktoken chromadb
conda activate langchainenv
pip install pyboxen
conda list


# Parsing Command Line Argument
python mod_01_pycode.py
python mod_01_pycode.py --language javascript --task 'print hello world'
python mod_01_pycode.py --language javascript --task 'return a list of numbers'

# Chat Chain
python mod_02_tchat.py
What is 1+1?
and 3 more?

# Document Loaders
python mod_04_facts.py

# Custom Retriever in Action
python mod_05_prompt

# For `scores.ipynb`
conda install ipykernel

# ChatGPT Functions
python mod_06_tools_agents.py

# pdf-dist initial setup
# Refer to README in pdf-dist
cd chatgp-langchain/stephen-grider/
conda create --name pdf-dist pip
conda activate pdf-dist
pip install -r pdf-dist/requirements.txt
cd pdf-dist
flask --app app.web init-db

# local-do-files setup
cd chatgp-langchain/stephen-grider
conda activate pdf-dist
pip install -r local-do-files/requirements.txt

# Running the servers
redis-server
inv dev        # pdf-dist
inv devworker  # pdf-dist
python app.py  # local-do-files

# Redis
redis-cli
HGETALL llm_score_values
HGETALL llm_score_counts
```

# env

## langchainenv

```sh
# packages in environment at /opt/homebrew/Caskroom/miniconda/base/envs/langchainenv:
#
# Name                    Version                   Build  Channel
aiohttp                   3.9.1           py311h05b510d_0    conda-forge
aiosignal                 1.3.1              pyhd8ed1ab_0    conda-forge
annotated-types           0.6.0              pyhd8ed1ab_0    conda-forge
anyio                     3.7.1              pyhd8ed1ab_0    conda-forge
appdirs                   1.4.4              pyh9f0ad1d_0    conda-forge
appnope                   0.1.2           py311hca03da5_1001
asgiref                   3.7.2              pyhd8ed1ab_0    conda-forge
asttokens                 2.0.5              pyhd3eb1b0_0
async-timeout             4.0.3              pyhd8ed1ab_0    conda-forge
attrs                     23.1.0             pyh71513ae_1    conda-forge
backcall                  0.2.0              pyhd3eb1b0_0
backoff                   1.11.1             pyhd8ed1ab_0    conda-forge
bcrypt                    4.1.0           py311h94f323b_0    conda-forge
blinker                   1.7.0              pyhd8ed1ab_0    conda-forge
brotli                    1.1.0                hb547adb_1    conda-forge
brotli-bin                1.1.0                hb547adb_1    conda-forge
brotli-python             1.1.0           py311ha891d26_1    conda-forge
bzip2                     1.0.8                h93a5062_5    conda-forge
c-ares                    1.22.1               h93a5062_0    conda-forge
ca-certificates           2023.11.17           hf0a4a13_0    conda-forge
cachetools                5.3.2              pyhd8ed1ab_0    conda-forge
certifi                   2023.11.17      py311hca03da5_0
cffi                      1.16.0          py311h4a08483_0    conda-forge
charset-normalizer        3.3.2              pyhd8ed1ab_0    conda-forge
chroma-hnswlib            0.7.3           py311hddbb800_1    conda-forge
chromadb                  0.4.18          py311h267d04e_0    conda-forge
click                     8.1.7           unix_pyh707e725_0    conda-forge
colorama                  0.4.6              pyhd8ed1ab_0    conda-forge
coloredlogs               15.0.1             pyhd8ed1ab_3    conda-forge
comm                      0.1.2           py311hca03da5_0
contourpy                 1.2.0           py311hd03642b_0    conda-forge
cryptography              41.0.7          py311h71175c2_0    conda-forge
cycler                    0.12.1             pyhd8ed1ab_0    conda-forge
dataclasses-json          0.6.3              pyhd8ed1ab_0    conda-forge
debugpy                   1.6.7           py311h313beb8_0
decorator                 5.1.1              pyhd3eb1b0_0
deprecated                1.2.14             pyh1a96a4e_0    conda-forge
docker-pycreds            0.4.0                      py_0    conda-forge
et_xmlfile                1.1.0              pyhd8ed1ab_0    conda-forge
exceptiongroup            1.2.0              pyhd8ed1ab_0    conda-forge
executing                 0.8.3              pyhd3eb1b0_0
fastapi                   0.104.1            pyhd8ed1ab_0    conda-forge
filelock                  3.13.1             pyhd8ed1ab_0    conda-forge
fonttools                 4.45.1          py311h05b510d_0    conda-forge
freetype                  2.12.1               hadb7bae_2    conda-forge
frozenlist                1.4.0           py311heffc1b2_1    conda-forge
fsspec                    2023.10.0          pyhca7485f_0    conda-forge
gitdb                     4.0.11             pyhd8ed1ab_0    conda-forge
gitpython                 3.1.40             pyhd8ed1ab_0    conda-forge
gmp                       6.3.0                h965bd2d_0    conda-forge
gmpy2                     2.1.2           py311h2ba9262_1    conda-forge
google-api-core           2.14.0             pyhd8ed1ab_0    conda-forge
google-auth               2.23.4             pyhca7485f_0    conda-forge
googleapis-common-protos  1.61.0             pyhd8ed1ab_0    conda-forge
greenlet                  3.0.1           py311hbaf5611_0    conda-forge
grpcio                    1.59.3          py311h79dd126_0    conda-forge
h11                       0.14.0             pyhd8ed1ab_0    conda-forge
huggingface_hub           0.16.4             pyhd8ed1ab_0    conda-forge
humanfriendly             10.0               pyhd8ed1ab_6    conda-forge
idna                      3.6                pyhd8ed1ab_0    conda-forge
importlib-metadata        6.0.0              pyha770c72_0    conda-forge
importlib-resources       6.1.1              pyhd8ed1ab_0    conda-forge
importlib_resources       6.1.1              pyhd8ed1ab_0    conda-forge
iniconfig                 2.0.0              pyhd8ed1ab_0    conda-forge
ipykernel                 6.25.0          py311hb6e6a13_0
ipython                   8.15.0          py311hca03da5_0
jedi                      0.18.1          py311hca03da5_1
joblib                    1.3.2              pyhd8ed1ab_0    conda-forge
jsonpatch                 1.33               pyhd8ed1ab_0    conda-forge
jsonpointer               2.4             py311h267d04e_3    conda-forge
jupyter_client            8.6.0           py311hca03da5_0
jupyter_core              5.5.0           py311hca03da5_0
kiwisolver                1.4.5           py311he4fd1f5_1    conda-forge
krb5                      1.21.2               h92f50d5_0    conda-forge
langchain                 0.0.340            pyhd8ed1ab_0    conda-forge
langsmith                 0.0.67             pyhd8ed1ab_0    conda-forge
lcms2                     2.15                 hf2736f0_3    conda-forge
lerc                      4.0.0                h9a09cb3_0    conda-forge
libabseil                 20230802.1      cxx17_h13dd4ca_0    conda-forge
libblas                   3.9.0           20_osxarm64_openblas    conda-forge
libbrotlicommon           1.1.0                hb547adb_1    conda-forge
libbrotlidec              1.1.0                hb547adb_1    conda-forge
libbrotlienc              1.1.0                hb547adb_1    conda-forge
libcblas                  3.9.0           20_osxarm64_openblas    conda-forge
libcurl                   8.4.0                h2d989ff_0    conda-forge
libcxx                    16.0.6               h4653b0c_0    conda-forge
libdeflate                1.19                 hb547adb_0    conda-forge
libedit                   3.1.20191231         hc8eb9b7_2    conda-forge
libev                     4.33                 h642e427_1    conda-forge
libexpat                  2.5.0                hb7217d7_1    conda-forge
libffi                    3.4.2                h3422bc3_5    conda-forge
libgfortran               5.0.0           13_2_0_hd922786_1    conda-forge
libgfortran5              13.2.0               hf226fd6_1    conda-forge
libgrpc                   1.59.3               hbcf6334_0    conda-forge
libjpeg-turbo             3.0.0                hb547adb_1    conda-forge
liblapack                 3.9.0           20_osxarm64_openblas    conda-forge
libnghttp2                1.58.0               ha4dd798_0    conda-forge
libopenblas               0.3.25          openmp_h6c19121_0    conda-forge
libpng                    1.6.39               h76d750c_0    conda-forge
libprotobuf               4.24.4               hc9861d8_0    conda-forge
libpulsar                 3.2.0                h25ec3c2_6    conda-forge
libre2-11                 2023.06.02           h1753957_0    conda-forge
libsodium                 1.0.18               h1a28f6b_0
libsqlite                 3.44.2               h091b4b1_0    conda-forge
libssh2                   1.11.0               h7a5bd25_0    conda-forge
libtiff                   4.6.0                ha8a6c65_2    conda-forge
libwebp-base              1.3.2                hb547adb_0    conda-forge
libxcb                    1.15                 hf346824_0    conda-forge
libzlib                   1.2.13               h53f4e23_5    conda-forge
llvm-openmp               17.0.5               hcd81f8e_0    conda-forge
markdown-it-py            3.0.0              pyhd8ed1ab_0    conda-forge
marshmallow               3.20.1             pyhd8ed1ab_0    conda-forge
matplotlib-base           3.8.2           py311hfdba5f6_0    conda-forge
matplotlib-inline         0.1.6           py311hca03da5_0
mdurl                     0.1.0              pyhd8ed1ab_0    conda-forge
mmh3                      4.0.1           py311hbaf5611_2    conda-forge
monotonic                 1.5                        py_0    conda-forge
mpc                       1.3.1                h91ba8db_0    conda-forge
mpfr                      4.2.1                h9546428_0    conda-forge
mpmath                    1.3.0              pyhd8ed1ab_0    conda-forge
multidict                 6.0.4           py311he2be06e_1    conda-forge
munkres                   1.1.4              pyh9f0ad1d_0    conda-forge
mypy_extensions           1.0.0              pyha770c72_0    conda-forge
ncurses                   6.4                  h463b476_2    conda-forge
nest-asyncio              1.5.6           py311hca03da5_0
numexpr                   2.8.7           py311h6e08293_4    conda-forge
numpy                     1.26.2          py311h6d074dd_0    conda-forge
oauthlib                  3.2.2              pyhd8ed1ab_0    conda-forge
onnxruntime               1.16.3          py311h76957bc_0_cpu    conda-forge
openai                    0.28.1             pyhd8ed1ab_0    conda-forge
openapi-schema-pydantic   1.2.4              pyhd8ed1ab_0    conda-forge
openjpeg                  2.5.0                h4c1507b_3    conda-forge
openpyxl                  3.1.2           py311heffc1b2_0    conda-forge
openssl                   3.2.0                h0d3ecfb_1    conda-forge
opentelemetry-api         1.21.0             pyhd8ed1ab_0    conda-forge
opentelemetry-exporter-otlp-proto-common 1.21.0             pyhd8ed1ab_0    conda-forge
opentelemetry-exporter-otlp-proto-grpc 1.21.0             pyhd8ed1ab_0    conda-forge
opentelemetry-instrumentation 0.42b0             pyhd8ed1ab_0    conda-forge
opentelemetry-instrumentation-asgi 0.42b0             pyhd8ed1ab_0    conda-forge
opentelemetry-instrumentation-fastapi 0.42b0             pyhd8ed1ab_0    conda-forge
opentelemetry-proto       1.21.0             pyhd8ed1ab_0    conda-forge
opentelemetry-sdk         1.21.0             pyhd8ed1ab_0    conda-forge
opentelemetry-semantic-conventions 0.42b0             pyhd8ed1ab_0    conda-forge
opentelemetry-util-http   0.42b0             pyhd8ed1ab_0    conda-forge
overrides                 7.4.0              pyhd8ed1ab_0    conda-forge
packaging                 23.2               pyhd8ed1ab_0    conda-forge
pandas                    2.1.3           py311h6e08293_0    conda-forge
pandas-stubs              2.1.1.230928       pyhd8ed1ab_1    conda-forge
parso                     0.8.3              pyhd3eb1b0_0
pathtools                 0.1.2                      py_1    conda-forge
pexpect                   4.8.0              pyhd3eb1b0_3
pickleshare               0.7.5           pyhd3eb1b0_1003
pillow                    10.1.0          py311hb9c5795_0    conda-forge
pip                       23.3.1             pyhd8ed1ab_0    conda-forge
platformdirs              3.10.0          py311hca03da5_0
plotly                    5.18.0             pyhd8ed1ab_0    conda-forge
pluggy                    1.3.0              pyhd8ed1ab_0    conda-forge
posthog                   3.0.2              pyhd8ed1ab_0    conda-forge
prompt-toolkit            3.0.36          py311hca03da5_0
protobuf                  4.24.4          py311h4d1eceb_0    conda-forge
psutil                    5.9.5           py311heffc1b2_1    conda-forge
pthread-stubs             0.4               h27ca646_1001    conda-forge
ptyprocess                0.7.0              pyhd3eb1b0_2
pulsar-client             3.3.0           py311ha891d26_1    conda-forge
pure_eval                 0.2.2              pyhd3eb1b0_0
pyasn1                    0.5.0              pyhd8ed1ab_0    conda-forge
pyasn1-modules            0.3.0              pyhd8ed1ab_0    conda-forge
pyboxen                   1.2.0                    pypi_0    pypi
pycparser                 2.21               pyhd8ed1ab_0    conda-forge
pydantic                  2.5.2              pyhd8ed1ab_0    conda-forge
pydantic-core             2.14.5          py311h94f323b_0    conda-forge
pygments                  2.17.2             pyhd8ed1ab_0    conda-forge
pyjwt                     2.8.0              pyhd8ed1ab_0    conda-forge
pyopenssl                 23.3.0             pyhd8ed1ab_0    conda-forge
pyparsing                 3.1.1              pyhd8ed1ab_0    conda-forge
pypika                    0.48.9             pyhd8ed1ab_0    conda-forge
pysocks                   1.7.1              pyha2e5f31_6    conda-forge
pytest                    7.4.3              pyhd8ed1ab_0    conda-forge
pytest-subtests           0.11.0             pyhd8ed1ab_0    conda-forge
python                    3.11.6          h47c9636_0_cpython    conda-forge
python-dateutil           2.8.2              pyhd8ed1ab_0    conda-forge
python-dotenv             1.0.0              pyhd8ed1ab_1    conda-forge
python-flatbuffers        23.5.26            pyhd8ed1ab_0    conda-forge
python-kubernetes         28.1.0             pyhd8ed1ab_0    conda-forge
python-tzdata             2023.3             pyhd8ed1ab_0    conda-forge
python_abi                3.11                    4_cp311    conda-forge
pytz                      2023.3.post1       pyhd8ed1ab_0    conda-forge
pyu2f                     0.1.5              pyhd8ed1ab_0    conda-forge
pyyaml                    6.0.1           py311heffc1b2_1    conda-forge
pyzmq                     25.1.0          py311h313beb8_0
re2                       2023.06.02           h6135d0a_0    conda-forge
readline                  8.2                  h92ec313_1    conda-forge
regex                     2023.10.3       py311heffc1b2_0    conda-forge
requests                  2.31.0             pyhd8ed1ab_0    conda-forge
requests-oauthlib         1.3.1              pyhd8ed1ab_0    conda-forge
rich                      13.7.0             pyhd8ed1ab_0    conda-forge
rsa                       4.9                pyhd8ed1ab_0    conda-forge
scikit-learn              1.3.2           py311ha25ca4d_1    conda-forge
scipy                     1.11.4          py311h2b215a9_0    conda-forge
sentry-sdk                1.37.1             pyhd8ed1ab_0    conda-forge
setproctitle              1.3.3           py311heffc1b2_0    conda-forge
setuptools                68.2.2             pyhd8ed1ab_0    conda-forge
shellingham               1.5.4              pyhd8ed1ab_0    conda-forge
six                       1.16.0             pyh6c4a22f_0    conda-forge
smmap                     5.0.0              pyhd8ed1ab_0    conda-forge
snappy                    1.1.10               h17c5cce_0    conda-forge
sniffio                   1.3.0              pyhd8ed1ab_0    conda-forge
sqlalchemy                2.0.23          py311h05b510d_0    conda-forge
stack_data                0.2.0              pyhd3eb1b0_0
starlette                 0.27.0             pyhd8ed1ab_0    conda-forge
sympy                     1.12            pypyh9d50eac_103    conda-forge
tenacity                  8.2.3              pyhd8ed1ab_0    conda-forge
threadpoolctl             3.2.0              pyha21a80b_0    conda-forge
tiktoken                  0.5.1           py311h12f791a_1    conda-forge
tk                        8.6.13               h5083fa2_1    conda-forge
tokenizers                0.15.0          py311hd6c2c79_0    conda-forge
tomli                     2.0.1              pyhd8ed1ab_0    conda-forge
tornado                   6.3.3           py311h80987f9_0
tqdm                      4.66.1             pyhd8ed1ab_0    conda-forge
traitlets                 5.7.1           py311hca03da5_0
typer                     0.9.0              pyhd8ed1ab_0    conda-forge
types-pytz                2023.3.1.1         pyhd8ed1ab_0    conda-forge
typing-extensions         4.8.0                hd8ed1ab_0    conda-forge
typing_extensions         4.8.0              pyha770c72_0    conda-forge
typing_inspect            0.9.0              pyhd8ed1ab_0    conda-forge
typing_utils              0.1.0              pyhd8ed1ab_0    conda-forge
tzdata                    2023c                h71feb2d_0    conda-forge
urllib3                   1.26.18            pyhd8ed1ab_0    conda-forge
uvicorn                   0.24.0          py311h267d04e_0    conda-forge
wandb                     0.15.12            pyhd8ed1ab_0    conda-forge
wcwidth                   0.2.5              pyhd3eb1b0_0
websocket-client          1.6.4              pyhd8ed1ab_0    conda-forge
wheel                     0.42.0             pyhd8ed1ab_0    conda-forge
wrapt                     1.16.0          py311h05b510d_0    conda-forge
xorg-libxau               1.0.11               hb547adb_0    conda-forge
xorg-libxdmcp             1.1.3                h27ca646_0    conda-forge
xz                        5.2.6                h57fd34a_0    conda-forge
yaml                      0.2.5                h3422bc3_2    conda-forge
yarl                      1.9.2           py311h05b510d_1    conda-forge
zeromq                    4.3.4                hc377ac9_0
zipp                      3.17.0             pyhd8ed1ab_0    conda-forge
zstd                      1.5.5                h4f39d0f_0    conda-forge
```

## pdf-dist

```sh
# packages in environment at /opt/homebrew/Caskroom/miniconda/base/envs/pdf-dist:
#
# Name                    Version                   Build  Channel
aiohttp                   3.9.1                    pypi_0    pypi
aiosignal                 1.3.1                    pypi_0    pypi
amqp                      5.2.0                    pypi_0    pypi
anyio                     4.1.0                    pypi_0    pypi
attrs                     23.1.0                   pypi_0    pypi
backoff                   2.2.1                    pypi_0    pypi
billiard                  4.2.0                    pypi_0    pypi
blinker                   1.7.0                    pypi_0    pypi
boto3                     1.26.122                 pypi_0    pypi
botocore                  1.29.122                 pypi_0    pypi
bzip2                     1.0.8                h620ffc9_4
ca-certificates           2023.08.22           hca03da5_0
celery                    5.3.1                    pypi_0    pypi
certifi                   2023.11.17               pypi_0    pypi
charset-normalizer        3.3.2                    pypi_0    pypi
click                     8.1.7                    pypi_0    pypi
click-didyoumean          0.3.0                    pypi_0    pypi
click-plugins             1.1.1                    pypi_0    pypi
click-repl                0.3.0                    pypi_0    pypi
dataclasses-json          0.5.14                   pypi_0    pypi
dnspython                 2.4.2                    pypi_0    pypi
flask                     3.0.0                    pypi_0    pypi
flask-cors                4.0.0                    pypi_0    pypi
flask-sqlalchemy          3.0.3                    pypi_0    pypi
frozenlist                1.4.0                    pypi_0    pypi
h11                       0.14.0                   pypi_0    pypi
httpcore                  0.17.3                   pypi_0    pypi
httpx                     0.24.1                   pypi_0    pypi
idna                      3.6                      pypi_0    pypi
invoke                    2.2.0                    pypi_0    pypi
itsdangerous              2.1.2                    pypi_0    pypi
jinja2                    3.1.2                    pypi_0    pypi
jmespath                  1.0.1                    pypi_0    pypi
kombu                     5.3.4                    pypi_0    pypi
langchain                 0.0.252                  pypi_0    pypi
langfuse                  1.0.18                   pypi_0    pypi
langsmith                 0.0.69                   pypi_0    pypi
libffi                    3.4.4                hca03da5_0
loguru                    0.7.2                    pypi_0    pypi
markupsafe                2.1.3                    pypi_0    pypi
marshmallow               3.20.1                   pypi_0    pypi
multidict                 6.0.4                    pypi_0    pypi
mypy-extensions           1.0.0                    pypi_0    pypi
ncurses                   6.4                  h313beb8_0
numexpr                   2.8.7                    pypi_0    pypi
numpy                     1.26.2                   pypi_0    pypi
openai                    0.27.8                   pypi_0    pypi
openapi-schema-pydantic   1.2.4                    pypi_0    pypi
openssl                   3.0.12               h1a28f6b_0
packaging                 23.2                     pypi_0    pypi
pinecone-client           2.2.2                    pypi_0    pypi
pip                       23.3.1          py311hca03da5_0
prompt-toolkit            3.0.41                   pypi_0    pypi
pydantic                  1.10.13                  pypi_0    pypi
pypdf                     3.15.4                   pypi_0    pypi
python                    3.11.5               hb885b13_0
python-dateutil           2.8.2                    pypi_0    pypi
python-dotenv             1.0.0                    pypi_0    pypi
pytz                      2023.3.post1             pypi_0    pypi
pyyaml                    6.0.1                    pypi_0    pypi
readline                  8.2                  h1a28f6b_0
redis                     5.0.0                    pypi_0    pypi
regex                     2023.10.3                pypi_0    pypi
requests                  2.31.0                   pypi_0    pypi
s3transfer                0.6.2                    pypi_0    pypi
setuptools                68.0.0          py311hca03da5_0
six                       1.16.0                   pypi_0    pypi
sniffio                   1.3.0                    pypi_0    pypi
sqlalchemy                2.0.23                   pypi_0    pypi
sqlite                    3.41.2               h80987f9_0
tenacity                  8.2.3                    pypi_0    pypi
tiktoken                  0.4.0                    pypi_0    pypi
tk                        8.6.12               hb8d0fd4_0
tqdm                      4.66.1                   pypi_0    pypi
typing-extensions         4.8.0                    pypi_0    pypi
typing-inspect            0.9.0                    pypi_0    pypi
tzdata                    2023.3                   pypi_0    pypi
urllib3                   1.26.18                  pypi_0    pypi
uuid                      1.30                     pypi_0    pypi
vine                      5.1.0                    pypi_0    pypi
watchdog                  3.0.0                    pypi_0    pypi
wcwidth                   0.2.12                   pypi_0    pypi
werkzeug                  3.0.1                    pypi_0    pypi
wheel                     0.41.2          py311hca03da5_0
xz                        5.4.5                h80987f9_0
yarl                      1.9.3                    pypi_0    pypi
zlib                      1.2.13               h5a0b063_0
```

### IMPORTANT

- **Open the `pdf-dist` directory directly in a new VS Code window instead of navigating into the directory from `playground-ai`.**
- **This is so that pylint doesn't highlight errors when you are using the `pdf-dist` conda environment.**

### Questions for tests

- **Testing the chain to use context** (Without streaming)
  - What country produces the most spice?
  - How much did they produce in metric tonnes?
- **Testing the streaming setup**
  - What country produces the most spice?
  - What country is second?

&nbsp;

# LangChain

LangChain is a library and framework designed to facilitate the development of applications that leverage Large Language Models (LLMs) like GPT-3 or GPT-4. It's particularly focused on making it easier to build applications that use these models for language understanding and generation tasks. Here are some key aspects of LangChain:

1. **Purpose and Functionality**:

   - LangChain is intended to streamline the process of integrating LLMs into various applications.
   - It provides tools and abstractions that simplify common tasks such as generating text, processing language inputs, and managing interactions with language models.

2. **Components and Features**:

   - **Chain-of-Thought Prompting**: LangChain supports advanced prompting techniques like chain-of-thought prompting, where the model is guided to "think out loud" to reach a conclusion. This can improve the quality of responses for complex queries.
   - **Modular Design**: The framework is designed to be modular, allowing developers to plug in different components or models as needed. This flexibility is crucial for tailoring applications to specific requirements.
   - **Context Management**: Effective management of context in conversations or language tasks is a key feature, enabling more coherent and relevant interactions with the model.

3. **Applications**:

   - LangChain can be used in a variety of applications, from chatbots and virtual assistants to more complex language understanding systems in various domains like education, customer service, and content creation.

4. **Developer-Friendly**:

   - It's designed to be developer-friendly, reducing the barrier to entry for creating sophisticated language-based applications.

5. **Community and Support**:
   - As with many open-source projects, LangChain benefits from community contributions and support. This can include new features, bug fixes, and improvements based on real-world use cases.

In summary, LangChain is a valuable tool for developers looking to harness the power of Large Language Models in their applications. Its focus on ease of use, modularity, and advanced language processing capabilities makes it a noteworthy addition to the toolkit of any developer working in the AI and language domains.

&nbsp;

---

&nbsp;

Before tools like LangChain, developers and researchers working with Large Language Models (LLMs) like GPT-3 or GPT-4 had to handle several challenges and tasks manually or through custom solutions. Here's an overview of what they typically did:

1. **Manual Integration of Language Models**:

   - Developers had to manually integrate LLMs into their applications, which involved directly interfacing with the APIs provided by model providers like OpenAI. This required a good understanding of the API specifications and handling various aspects like request formats, response parsing, and error handling.

2. **Custom Prompt Engineering**:

   - Crafting effective prompts to elicit the desired response from an LLM is a nuanced task. Without frameworks like LangChain, developers had to manually experiment with and refine their prompts, a process that can be time-consuming and requires a deep understanding of how these models respond to different inputs.

3. **Context Management**:

   - For applications involving conversations or extended interactions, managing context effectively is crucial. Without specialized tools, developers had to devise their own methods for maintaining context across multiple exchanges, which could be complex and error-prone.

4. **Handling Model Limitations**:

   - Developers had to devise their own strategies to handle limitations of LLMs, such as biases in the model, handling off-topic responses, or ensuring the relevance and accuracy of the generated content.

5. **Building Custom Workflows**:

   - Integrating LLMs into broader application workflows (like using an LLM in conjunction with a database or other AI services) required custom development work. This included handling the logic for when and how to call the LLM, process its outputs, and integrate those outputs into the application's workflow.

6. **Performance Optimization**:

   - Optimizing the performance of applications using LLMs, in terms of response time and resource usage, often required custom solutions and fine-tuning.

7. **Experimentation and Research**:

   - Researchers and developers had to conduct their own experiments to understand the capabilities and limitations of LLMs in various applications, which could be a resource-intensive process.

In essence, without tools like LangChain, the process of integrating and effectively utilizing LLMs in applications was more manual, required deeper expertise in the workings of these models, and often involved developing custom solutions for various aspects of the integration. LangChain and similar frameworks aim to simplify and streamline these processes, making it easier for a broader range of developers to leverage the power of LLMs in their applications.

&nbsp;

# Pinecone

- [Pinecone](https://app.pinecone.io/)
- **Create new index**
  - **Name**: docs
  - **Dimensions**: 1536 (OpenAI)

&nbsp;

# LangFuse

- [Self-hosted by Stephen](prod-langfuse.fly.dev)
- [langfuse](langfuse.com)

&nbsp;

# Models

1. **Completion Model**:

   - **Function**: The completion model is designed to generate text that logically and coherently follows from a given prompt. It's like finishing a sentence or a thought based on the initial input it receives.
   - **Applications**: This model is widely used in scenarios like auto-completing sentences in email or text editors, generating content for articles, coding assistance, and more.
   - **Mechanism**: It relies on patterns and structures it has learned during training. When given a prompt, it predicts the next most likely sequence of words based on its training.
   - **Challenges**: Ensuring relevance and accuracy can be challenging, especially for longer completions or more complex topics.

2. **Chat Model**:

   - **Function**: The chat model is specialized for conversational interactions. It's designed to not just complete a prompt but to engage in a back-and-forth dialogue, maintaining context and coherence over multiple turns of conversation.
   - **Applications**: These models are used in chatbots, virtual assistants, customer service automation, and interactive educational tools.
   - **Mechanism**: Chat models are trained to understand the flow of a conversation, including nuances, questions, and responses. They maintain context over a conversation and can handle a wide range of topics.
   - **Challenges**: Maintaining context accurately over long conversations and handling ambiguous or complex queries are common challenges.

Both models share a common foundation in terms of their underlying technology (like neural networks and machine learning algorithms), but they are optimized for different use cases. The completion model is more about generating relevant and coherent text based on a given start, while the chat model is about engaging in a dynamic, context-aware conversation.

&nbsp;

# Semantic Search & Embeddings

Semantic search and embeddings are concepts closely related to the fields of natural language processing (NLP) and machine learning, particularly relevant in the context of information retrieval and understanding human language.

1. **Semantic Search**

   - **Definition**: Semantic search refers to search algorithms that go beyond the traditional keyword-based approaches. Instead of relying solely on the exact match of keywords, semantic search tries to understand the intent and contextual meaning of the search query.
   - **How it Works**: It uses various NLP techniques to comprehend the query's semantics - the meaning behind the words. For instance, it understands synonyms, variations in language, and even the context within which words are used. This leads to more intuitive and relevant search results.
   - **Applications**:
     - **Web Search Engines**: Google and other search engines use semantic search principles to provide results that match the searcher's intent, not just their exact query.
     - **E-commerce**: Product searches that understand user intent and preferences.
     - **Information Retrieval Systems**: In libraries, databases, and other knowledge repositories.

2. **Embeddings**

   - **Definition**: In machine learning, especially in the domain of NLP, embeddings are a type of representation where words, phrases, sentences, or even entire documents are mapped to vectors of real numbers. This process effectively translates text into a form that computers can understand and process.
   - **Characteristics**:
     - **Dimensionality Reduction**: Embeddings condense the vast information in words into a lower-dimensional space.
     - **Contextual Meaning**: They capture semantic and syntactic meanings of words. Words with similar meanings tend to have closer embeddings.
   - **Types**:
     - **Word Embeddings**: Examples include Word2Vec, GloVe. They represent individual words in vector space.
     - **Sentence/Document Embeddings**: Examples include BERT, Doc2Vec. They extend the concept to larger units of text.
   - **Applications**:
     - **Semantic Analysis**: Understanding the sentiment or topic of a text.
     - **Machine Translation**: Translating text between languages while preserving meaning.
     - **Information Retrieval**: Enhancing search algorithms to fetch contextually relevant documents.

3. **Intersection of Semantic Search and Embeddings**

   - Semantic search often utilizes embeddings to understand the context and semantics of queries and documents. By converting words and sentences into vector representations, a semantic search system can measure the similarity between the query and potential search results more effectively than traditional keyword matching.
   - There are practical applications of these concepts in various NLP libraries and frameworks, which are extensively used for developing intelligent search systems, chatbots, recommendation systems, and more.

&nbsp;
