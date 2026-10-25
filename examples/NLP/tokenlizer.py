from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "bert-base-uncased"
)
text  = "Hello, I love pytorch!"

inputs = tokenizer(
    text, 
    return_tensors = "pt"
) 