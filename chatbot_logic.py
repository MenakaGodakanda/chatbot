from transformers import AutoModelForCausalLM, AutoTokenizer

class Chatbot:
    def __init__(self, model_name="gpt2"):
        # Load the tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_response(self, user_input):
        # Encode user input and generate response
        input_ids = self.tokenizer.encode(user_input, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=50, num_return_sequences=1, pad_token_id=self.tokenizer.eos_token_id)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
