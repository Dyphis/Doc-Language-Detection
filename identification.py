import torch
from transformers import pipeline


def detection(text_list):
    device = 0 if torch.cuda.is_available() else -1
    model_ckpt = "papluca/xlm-roberta-base-language-detection"
    pipe = pipeline("text-classification", model=model_ckpt, device=device)

    model_preds = [s['label'] for s in pipe(text_list, truncation=True, max_length=128)]
    return model_preds


if __name__ == '__main__':

    test_doc = ['Een man zingt en speelt gitaar.', 'De technologisch geplaatste Nasdaq Composite I', 
                'Es muy resistente la parte trasera rígida y', '这是一条用于测试的中文语句。', 'これはテスト用の日本語の文章です。']
    print(detection(test_doc))