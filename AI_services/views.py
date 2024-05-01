from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
import json
import torch
from peft import PeftModel, PeftConfig
from transformers import AutoModelForSeq2SeqLM


"""
Next word prediction model endpoint

This endpoint takes a prompt as input and 
generates the next word prediction based on the 
provided prompt using a pretrained language model.

Example usage:
POST /generate/next-word/
{
    "prompt": "Once upon a time"
}

Returns:
{
    "generated_text": "there"
}
"""

# Load tokenizer and model
next_word_tokenizer = AutoTokenizer.from_pretrained("mohammedRiad/Next_Word_Pred_Model")
next_word_model = AutoModelForCausalLM.from_pretrained("mohammedRiad/Next_Word_Pred_Model")

@csrf_exempt
def predict_next_word(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('prompt', '')
        # Tokenize the prompt
        input_ids = next_word_tokenizer.encode(prompt, return_tensors="pt")
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

        max_length = len(input_ids[0]) + 10 
        # Generate text
        output = next_word_model.generate(input_ids,pad_token_id=next_word_tokenizer.pad_token_id,max_length=max_length, attention_mask=attention_mask, num_return_sequences=1, temperature=0.5,do_sample=True)
        # Decode the generated output
        generated_text = next_word_tokenizer.decode(output[0], skip_special_tokens=True)
        return JsonResponse({'generated_text': generated_text})
    else:
        return JsonResponse({'error': 'POST method required'})



"""
    Summarizarion model
"""

config = PeftConfig.from_pretrained("mohammedRiad/flanT5_summary_withPEFT")
base_model = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForSeq2SeqLM.from_pretrained(base_model)
summary_model = PeftModel.from_pretrained(model, config=config, model_id="mohammedRiad/flanT5_summary_withPEFT")



@csrf_exempt
def summarize(request):
    if request.method == 'POST':
        try:
            # Extract the input text from the POST request
            data = json.loads(request.body)
            input_text = data.get('long_text', '')

            # Tokenize the input text
            inputs = tokenizer(input_text, return_tensors="pt")

            # Generate text using the PEFT model
            with torch.no_grad():
                outputs = summary_model.generate(input_ids=inputs["input_ids"], max_length=100)
                generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Return the generated text as JSON response
            return JsonResponse({'summarized_text': generated_text})

        except Exception as e:
            return JsonResponse({'error': str(e)})

    else:
        return JsonResponse({'error': 'POST method required'})





"""
Question and Answer model endpoint

This endpoint takes a prompt as input and generates the question and answer based on the provided prompt using a pretrained question answering model.

Example usage:
POST /generate/QA/
{
    "prompt": "Who is the president of the United States?"
}

Returns:
{
    "generated_text": "The president of the United States is Joe Biden."
}

"""

QA_tokenizer = AutoTokenizer.from_pretrained("mohammedRiad/QAModel")
QA_model = AutoModelForCausalLM.from_pretrained("mohammedRiad/QAModel")


@csrf_exempt
def send_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('prompt', '')
        # Tokenize the prompt
        input_ids = next_word_tokenizer.encode(prompt, return_tensors="pt")
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

        max_length = len(input_ids[0]) + 100 
        # Generate text
        output = next_word_model.generate(input_ids,pad_token_id=next_word_tokenizer.pad_token_id,max_length=max_length, attention_mask=attention_mask, num_return_sequences=1, temperature=0.5,do_sample=True)
        # Decode the generated output
        generated_text = next_word_tokenizer.decode(output[0], skip_special_tokens=True)
        # Remove duplucated question tokens
        end_index = generated_text.index(prompt) + len(prompt)
        remaining_text = ''.join(generated_text[end_index:]).strip()
        remaining_text = remaining_text.replace('"', '')
        remaining_text = remaining_text.replace("?", "")
        return JsonResponse({'generated_text': remaining_text})
    else:
        return JsonResponse({'error': 'POST method required'})
    

