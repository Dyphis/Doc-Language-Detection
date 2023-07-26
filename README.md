# Doc Language Detection Tool
This document language detection tool is based on `xlm-roberta-base` model [1]. The model is fine-tuned on [`STSb Multi MT`](https://huggingface.co/datasets/stsb_multi_mt) dataset.
Currently, it supports detecting .txt and .docx files. Available languages are: de, en, es, fr, it, nl, pl, pt, ru, zh. It can support more languages by fine-tuning on datasets with other languages.
# Get Started
## 1. Initialization
```bash
cd DOC-LANGUAGE-DETECTION
```
Windows Powershell:
```bash
./initialzation.bat
```
Linux:
```bash
./initialization.sh
```

## 2. Get the Fine-tuned Checkpoint
Donwload the model checkpoint from the [GoogleDrive](https://drive.google.com/drive/folders/1NTiiN78QQ-S3dZHvt4EfmsTZqAC9I_Gy?usp=sharing) and put them into the `pt_save_pretrained` folder.

Or run the script file (`fine-tuning.bat` or `fine-tuning.sh`) corresponding to your OS.

## 3. Start Detecting
Window Powershell:
```bash
./run.bat
```
Linux:
```bash
./run.sh
```
and following the instruction.

# Example
```
Virtual environment folder found. Activating...
Virtual environment activated.
Please enter a path for a file path or a folder. 
You can either put copies of docs into the 'docs' folder and press enter to continue.

Detected 4 files in the folder.

Document names                           Language
doc1.txt                                   en
doc2.docx                                  en

2 unrecognized files cannot be detected:
doc3.pdf
doc4.doc
Continue detection for other docs? (y/n): n
Exiting program..
```

# Reference
[1] Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020. Unsupervised Cross-lingual Representation Learning at Scale. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 8440–8451, Online. Association for Computational Linguistics.