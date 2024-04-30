

def replace_word():
    str="hello guys ,alex here is greeting you "
    print(str)
    word_to_replace=input("enter the word you want to replace in the  above   ")
    wordReplacement=input("enter word replacement  " )
    # use of replace() method to replace
    print(str.replace(word_to_replace,wordReplacement))

replace_word()
