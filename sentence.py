
sentence = ""

while True:
    new_word = raw_input("Enter a world (. ! or ? to end):") 
    if new_word == "." or new_word == "!" or new_word == "?":
        print sentence + new_word
        break
    else:
        sentence += new_word
        sentence += " "
    