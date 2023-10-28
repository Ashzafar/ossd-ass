def vowels_and_consonants(string):
    i = 0
    vowels = 0
    consonants = 0
    while i < len(string):
        if (
            string[i] == "a"
            or string[i] == "A"
            or string[i] == "e"
            or string[i] == "E"
            or string[i] == "i"
            or string[i] == "I"
            or string[i] == "o"
            or string[i] == "O"
            or string[i] == "u"
            or string[i] == "U"
        ):
            vowels += 1
        elif string[i] == " ":
            pass
        else:
            consonants += 1
        i+=1
    print('vowels: ' + str(vowels))
    print('consonants: ' + str(consonants))
    
vowels_and_consonants('University of Management and Technology')