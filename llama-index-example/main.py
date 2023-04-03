# NOTE: 環境変数 OPENAI_API_KEY を設定すること

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

response = index.query("What did the author do growing up?")
print(response)

# save to disk
index.save_to_disk('index.json')
# load from disk
# index = GPTSimpleVectorIndex.load_from_disk('index.json')
