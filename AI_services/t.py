from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
import torch

config = PeftConfig.from_pretrained("ybelkada/opt-350m-lora")
base_model = "facebook/opt-350m"
tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForCausalLM.from_pretrained(base_model)
peft_model = PeftModel.from_pretrained(model, config=config, model_id="ybelkada/opt-350m-lora")



inputs = tokenizer("Preheat the oven to 350 degrees and place the cookie dough", return_tensors="pt")
input_ids = inputs["input_ids"]  

with torch.no_grad():
    outputs = peft_model.generate(input_ids=input_ids, max_length=100)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(generated_text)
    

