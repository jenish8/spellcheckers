from spellchecker import SpellChecker
spell=SpellChecker()
while word!=99:
    word=word.lower()
    if word in spell:
        print("'{}' is spelled correctly!".format(word))
    else:
        correctwords=spell.correction(word)
        print("The best suggestion for '{}' is '{}' ".format(word,correctwords))
    word=input('enter the word:')