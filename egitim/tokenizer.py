import json

class Tokenizer:
    def __init__(self, vocab_file):
        with open(vocab_file, 'r', encoding='utf-8') as f:
            self.vocab = json.load(f)
            self.revers_vocab = {v: k for k, v in self.vocab.items()}