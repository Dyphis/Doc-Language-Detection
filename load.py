import os
from docx import Document

def load_file_list(dir_path='.\\docs\\') -> list:
    file_list = []
    if not os.path.isdir(dir_path):
      return
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            file_list.append(os.path.join(dir_path, path))
    
    return file_list

def text_extraction(file_path: str) -> str:
    split_tup = os.path.splitext(file_path)
    if split_tup[1] == '.txt':
        return txt2text(file_path)
    elif split_tup[1] == '.docx':
        return docx2text(file_path)
    else:
        return 'unknown file'

def txt2text(file_path: str) -> str:
    with open(file_path, 'r') as file:
        text = ' '.join(file.readlines())
    return text

def docx2text(file_path: str) -> str:
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return ' '.join(text)



if __name__ == '__main__':
    for file in load_file_list():
        print(text_extraction(file))
    
        