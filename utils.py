from fastai.text import BaseTokenizer

class CustomTokenizer(BaseTokenizer):
    def __init__(self, max_seq_len=None, **kwargs):
        self.max_seq_len = max_seq_len
    
    def tokenizer(self, t):
        token_list = t.split()
        if self.max_seq_len:
            token_list[:self.max_seq_len]
        
        return token_list + ['xxeos']
    
    def __call__(self, *args, **kwargs): 
        return self

def lowercase_everything(x):
    res = []
    for t in x:
        if t.isupper() and len(t) > 1: res.append(t.lower())
        else: res.append(t)
    return res

def remove_duplicates(x):
    return list(dict.fromkeys(x))