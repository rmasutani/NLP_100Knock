import sys

def split_word(sent):
    sent = sent.replace(",", " ,")
    sent = sent.replace(".", " .")
    sent = sent.split()
    return sent


def word_ngram(words, n):
    return [words[i:i+n] for i in range(len(words)-n+1)]


def letter_ngram(sent, n):
    return [sent[i:i+n] for i in range(len(sent)-n+1)]


def main():
    sent = sys.stdin.readline()
    words = split_word(sent)
    print(word_ngram(words, 2))
    print(letter_ngram(sent, 2))
    return


if __name__ == '__main__':
    main()
    