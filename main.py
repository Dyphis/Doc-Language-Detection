import os

from load import *
from identification import *

flag = 1
while flag:
    path = input("Please enter a path for a file path or a folder. \nYou can either put copies of docs into the 'docs' folder and press enter to continue.\n")
    if os.path.isfile(path):
            text = text_extraction(path)
            if text == 'unknown file':
                print("Unrecognized file type (only support txt, docx, doc), please try other documents.\n")
            else:
                predictions = detection([text])
                print('{:<40} {:>4}'.format('Document names', 'Language'))
                print('{:<40} {:>4}'.format(os.path.basename(path), predictions[0]))
    else:
        if path == "":
            path = './docs'
        file_list = load_file_list(path)
        if file_list:
            print('Detected {} files in the folder.\n'.format(len(file_list)))
            valid = []
            texts = []
            invalid = []
            for file_path in file_list:
                text = text_extraction(file_path)
                if text == 'unknown file':
                    invalid.append(os.path.basename(file_path))
                else:
                    valid.append(os.path.basename(file_path))
                    texts.append(text)
            
            if valid:
                predictions = detection(texts)
                if predictions == 'error':
                    break
                print('{:<40} {:>4}'.format('Document names', 'Language'))
                for doc_name, lang in zip(valid, predictions):
                    print('{:<40} {:>4}'.format(doc_name, lang))

            print('\n{} unrecognized files cannot be detected:'.format(len(invalid)))
            for file_name in invalid:
                print(file_name)
        else:
            print('No files in this directory or invalid file path.\n')
    
    flag = 0
    command = input("Continue detection for other docs? (y/n): ")
    if command == 'y' or command == 'Y' or command == 'Yes' or command == 'YES':
        flag = 1
        
print('Exiting program..')

    
    