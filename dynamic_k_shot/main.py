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

if reports.__len__() == 0:
        dataset = get_dataset()
        reports.data.insert_many(dataset)

query = "This is a test"
response = reports.query.near_text(query=query, limit=3)
print(response.objects)