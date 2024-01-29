import weaviate
import weaviate.classes as wvc
from utils import get_dataset
from peft import LoraConfig, PeftModel, prepare_model_for_kbit_training, get_peft_model

peft_config = LoraConfig(
        r=16,
        lora_alpha=16,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj","gate_proj"]
)

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