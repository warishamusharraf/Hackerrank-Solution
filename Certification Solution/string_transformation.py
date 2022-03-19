def transformation(sentence):
    sentence.split()
    words=''
    for i in sentence:
            words+=i
    if words[1:].upper():
          print(words.replace(words[1:],words[1:].lower()))
    if words[1:].lower():
          print(words.replace(words[1:],words[1:].upper()))
    

sentence=input("type word")
transformation(sentence) 
