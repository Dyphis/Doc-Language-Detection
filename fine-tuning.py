import numpy as np
import torch
import evaluate

from datasets import load_dataset, Dataset
from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification, 
    TrainingArguments, 
    Trainer, 
    DataCollatorWithPadding
    )

LABELS = ['en', 'de', 'es', 'fr', 'it', 'nl', 'pl', 'pt', 'ru', 'zh']
DEVICE =  0 if torch.cuda.is_available() else -1

#create dataset & apply label to id
def generator(split_name):
  for idx, lang in enumerate(LABELS):
    temp_dataset = load_dataset("stsb_multi_mt", name=lang, split=split_name)
    for sample in temp_dataset:
      yield {'sentence': sample['sentence1'], 'label': idx}

train_set = Dataset.from_generator(generator('train')).shuffle(seed=42)
valid_set = Dataset.from_generator(generator('valid')).shuffle(seed=42)
test_set = Dataset.from_generator(generator('test')).shuffle(seed=42)

#define label2id and id2label function
label2id = {lang: idx for idx, lang in enumerate(LABELS)}
id2label = {idx: lang for idx, lang in enumerate(LABELS)}

#tokenization
tokenizer = AutoTokenizer.from_pretrained("xlm-roberta-base")

def tokenization(sample):
    return tokenizer(sample['sentence'], max_length=128, truncation=True)

tokenized_train_set = train_set.map(tokenization, batched=True)
tokenized_valid_set = valid_set.map(tokenization, batched=True)
tokenized_test_set = test_set.map(tokenization, batched=True)

#training
model = AutoModelForSequenceClassification.from_pretrained(
    "xlm-roberta-base", 
    num_labels=len(LABELS), 
    id2label=id2label, 
    label2id=label2id
    )

epoch = 2
learning_rate = 2e-5
batch_size = 64
logging_steps = len(tokenized_train_set) // batch_size

training_args = TrainingArguments(
    output_dir="model",
    evaluation_strategy="epoch",
    num_train_epochs=epoch,
    learning_rate=learning_rate,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    logging_steps=logging_steps
    )

metric = evaluate.load("accuracy")
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_set,
    eval_dataset=tokenized_valid_set,
    compute_metrics=compute_metrics,
    tokenizer=tokenizer,
    data_collator=data_collator
    )

trainer.train()

#save model and tokenizer
pt_save_directory = "./pt_save_pretrained"
tokenizer.save_pretrained(pt_save_directory)
model.save_pretrained(pt_save_directory)