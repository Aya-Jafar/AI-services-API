from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import AutoTokenizer, AutoModelForCausalLM
import json
import torch


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

# summary_tokenizer = AutoTokenizer.from_pretrained("mohammedRiad/flanT5_summary_withPEFT")
# summary_model = AutoModelForCausalLM.from_pretrained("mohammedRiad/flanT5_summary_withPEFT")

# def summarize(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         prompt = data.get('prompt', '')
#         # Tokenize the prompt
#         input_ids = next_word_tokenizer.encode(prompt, return_tensors="pt")
#         attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

#         max_length = len(input_ids[0]) + 10 
#         # Generate text
#         output = next_word_model.generate(input_ids,pad_token_id=next_word_tokenizer.pad_token_id,max_length=max_length, attention_mask=attention_mask, num_return_sequences=1, temperature=0.5,do_sample=True)
#         # Decode the generated output
#         generated_text = next_word_tokenizer.decode(output[0], skip_special_tokens=True)
#         print(generated_text)
#         return JsonResponse({'generated_text': generated_text})
#     else:
#         return JsonResponse({'error': 'POST method required'})



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
        output = next_word_model.generate(input_ids,pad_token_id=next_word_tokenizer.pad_token_id,max_length=max_length, attention_mask=attention_mask, num_return_sequences=1, temperature=0.5)
        # Decode the generated output
        generated_text = next_word_tokenizer.decode(output[0], skip_special_tokens=True)
        return JsonResponse({'generated_text': generated_text})
    else:
        return JsonResponse({'error': 'POST method required'})
    


