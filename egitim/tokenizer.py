import json

class Tokenizer:
    def __init__(self, vocab_file):
        with open(vocab_file, 'r', encoding='utf-8') as f:
            self.vocab = json.load(f)
            self.revers_vocab = {v: k for k, v in self.vocab.items()}

    def encode(self, text):
        tokens = []

        for word in text.split():
            i = 0
            while i < len(word):
                found_match = False
                for j in range(len(word), i, -1):
                    sub_word = word[i:j]
                    if sub_word in self.vocab:
                        tokens.append(self.vocab[sub_word])
                        i=j
                        found_match= True
                        break
                if not found_match:
                    tokens.append(self.vocab["<unk>"])
                    i +=1
                tokens.append(self.vocab[" "])

            tokens.pop()
            return tokens

    def decode(self, ids):
        text = " "
        for id in ids:
            text += self.revers_vocab[id]
        return text

    