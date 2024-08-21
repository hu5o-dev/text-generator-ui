import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from datetime import datetime
import os
import logging
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkTextbox
from tkinter import messagebox


logging.basicConfig(filename='text_generation.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
logging.info(f"Using device: {device}")


model_name = 'gpt2-medium'
model = GPT2LMHeadModel.from_pretrained(model_name).to(device)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)


def generate_text(prompt, max_length=100, temperature=0.7, top_k=50, top_p=0.9):
    logging.info(f"Generating text with prompt: {prompt}")
    
    
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
    
   
    attention_mask = torch.ones(input_ids.shape, device=device)
    
    
    with torch.no_grad():
        outputs = model.generate(
            input_ids, 
            attention_mask=attention_mask,
            max_length=max_length,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            no_repeat_ngram_size=2,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
   
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    logging.info("Text generation completed.")
    return generated_text


def on_generate_click():
    prompt = prompt_entry.get()
    if not prompt.strip():
        messagebox.showwarning("Input Error", "Please enter a prompt.")
        return
    
    generated_text = generate_text(prompt, max_length=150)
    
    output_textbox.delete(1.0, "end")
    output_textbox.insert("end", generated_text)
    

    output_dir = "generated_texts"
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"generated_text_{timestamp}.txt")
    
    with open(output_file, 'w') as f:
        f.write(generated_text)
    
    logging.info(f"Generated text saved to {output_file}")
    messagebox.showinfo("Success", f"Generated text saved to {output_file}")


def create_ui():
    global prompt_entry, output_textbox
    app = CTk()
    app.title("Text Generator")
    app.geometry("600x400")


    prompt_label = CTkLabel(app, text="Enter your prompt:")
    prompt_label.pack(pady=10)


    prompt_entry = CTkEntry(app, width=500)
    prompt_entry.pack(pady=10)


    generate_button = CTkButton(app, text="Generate Text", command=on_generate_click)
    generate_button.pack(pady=10)

    output_textbox = CTkTextbox(app, width=550, height=200)
    output_textbox.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    try:
        create_ui()
    except Exception as e:
        logging.error(f"Failed to start the UI: {e}")
        messagebox.showerror("Error", f"Failed to start the UI: {e}")
