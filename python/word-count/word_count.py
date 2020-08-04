import unicodedata
def word_count(phrase):
    phrase = phrase.replace('"', '').replace("'", '')
    count = {}
    for k in "".join(ch for ch in phrase if unicodedata.category(ch)[0]!="C").split(' '):
        if k in count.keys():
            count[k.lower()] += 1
        else:
            count[k.lower()] = 1
    print (count)

word_count('Praise "lo\trd" ke\tk!')