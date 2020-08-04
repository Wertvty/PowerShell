def is_pangram(sentence):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    result =  all(idk in sentence  for idk in alph)
    return result
