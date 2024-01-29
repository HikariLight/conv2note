import weaviate
import weaviate.classes as wvc
from utils import get_dataset

client = weaviate.connect_to_local()

if client.collections.exists("reports"):
    reports = client.collections.get("reports")
else:
    reports = client.collections.create(
        name="reports",
        vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_transformers()
    )

dataset = get_dataset()
# print(dataset[0])

# reports.data.insert_many(dataset)

response = reports.query.near_text(query="", limit=3)
print(response)

# def get_k_similar(k):
    # response = reports.query.near_text(query="", limit=3)