# Check environment - Validate rediness 
import torch
print(f"PyTorch: {torch.__version__}")
print(f"CUDA: {torch.cuda.is_available()}")

import transformers
print(f"Transformers: {transformers.__version__}")

from sklearn.ensemble import RandomForestRegressor
print("✅ Scikit-learn OK")

from datasets import load_dataset
dataset = load_dataset("flytech/python-codes-25k", split="train[:10]")
print("✅ Datasets OK")

print (" Environment Ready!!!!")



##########################################################################################

# Load dataset, and perform intial train 

import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True,max_split_size_mb:32"
import torch
torch.cuda.empty_cache()

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, TaskType

# Smaller model + dataset
model_name = "microsoft/DialoGPT-small"
dataset = load_dataset("flytech/python-codes-25k", split="train[:200]")  # Direct split

tokenizer = AutoTokenizer.from_pretrained(model_name)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Load model CRITICALLY with gradients enabled
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,
    trust_remote_code=True
)

# CRITICAL: Enable training mode + gradients
model.train()
model.enable_input_require_grads()
for param in model.parameters():
    param.requires_grad = True

# Apply LoRA AFTER enabling gradients
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=4,
    lora_alpha=8,
    lora_dropout=0.1,
    target_modules=["c_attn", "c_proj"]
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()  # Verify trainable params

# Fixed tokenization (dynamic padding)
def tokenize_function(examples):
    texts = [f"### Instruction: {inst}\n### Input: {inp}\n### Response: {out}" 
             for inst, inp, out in zip(examples['instruction'], examples['input'], examples['output'])]
    tokenized = tokenizer(texts, truncation=True, max_length=128)
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized

tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=dataset.column_names)

# Ultra-safe TrainingArguments
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=32,
    gradient_checkpointing=True,
    fp16=True,
    max_steps=50,  # Very small for testing
    logging_steps=5,
    dataloader_num_workers=0,
    report_to=None,
    optim="adamw_torch",
    learning_rate=2e-4
)

# Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=None  # Let trainer handle
)

print("Starting training...")
trainer.train()
print("Training completed!")


##########################################################################################

# Training - Iteration2

import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True,max_split_size_mb:32"
import torch
torch.cuda.empty_cache()

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForLanguageModeling
from peft import LoraConfig, get_peft_model, TaskType

# Production model + larger dataset
model_name = "microsoft/DialoGPT-small"
dataset = load_dataset("flytech/python-codes-25k", split="train[:5000]")

tokenizer = AutoTokenizer.from_pretrained(model_name)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Load model with gradients enabled
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,
    trust_remote_code=True
)

# Enable training mode + gradients
model.train()
model.enable_input_require_grads()
for param in model.parameters():
    param.requires_grad = True

# Production LoRA config
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,
    lora_alpha=16,
    lora_dropout=0.1,
    target_modules=["c_attn", "c_proj"]
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# tokenization with padding=True
def tokenize_function(examples):
    texts = [f"### Instruction: {inst}\n### Input: {inp}\n### Response: {out}" 
             for inst, inp, out in zip(examples['instruction'], examples['input'], examples['output'])]
    tokenized = tokenizer(
        texts, 
        truncation=True, 
        padding=True, 
        max_length=128,
        return_tensors=None
    )
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized

tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=dataset.column_names)

# PRODUCTION TrainingArguments
training_args = TrainingArguments(
    output_dir="./python-code-llm",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=16,
    gradient_checkpointing=True,
    fp16=True,
    num_train_epochs=3,
    max_steps=2000,
    logging_steps=50,
    save_steps=500,
    save_total_limit=3,
    dataloader_num_workers=0,
    report_to=None,
    optim="adamw_torch",
    learning_rate=5e-5,
    warmup_steps=100,
    weight_decay=0.01,
    lr_scheduler_type="cosine"
)

# Use proper data collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator 
)

print("Starting PRODUCTION training...")
print("Monitor with: watch nvidia-smi -l 1")
trainer.train()

# Save final model
trainer.save_model("./my-python-code-llm-final")
print("✅ Training completed! Model saved to ./my-python-code-llm-final")


##########################################################################################

# Inference test

# Load your trained model
from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForCausalLM

base_model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small", torch_dtype=torch.float16)
model = PeftModel.from_pretrained(base_model, "./my-python-code-llm-final")
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")

def generate_code(prompt):
    inputs = tokenizer(f"### Instruction: {prompt}\n### Response:", return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.7, do_sample=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Test it!
print(generate_code("Write a Python function to reverse a string"))


##########################################################################################
#web front end

import gradio as gr
# Your inference code above + this:
demo = gr.Interface(fn=generate_code, inputs="text", outputs="text", title="🐍 My Python SLM")
demo.launch(share=False)  # http://localhost:7860
pip install gradio  # If needed

##########################################################################################

