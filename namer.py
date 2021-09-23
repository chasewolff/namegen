import random

def namer():
    num = random.randint(4, 20)
    ab = "abcdefghijklmnopqrstuvwxyz"
    vow1 = "aeiouy"
    vow2 = "aeiou"
    space = " "
    str = ""
    print(str)
    prevVowel = True
    prevSpace = True
    for i in range(num):
        # capper randomly determines if the letter to be added will be capitalized or not
        capper = random.randint(0,1)
        # if the previously generated value is a vowel, well then any letter can come after it.
        # otherwise, generate a vowel, but not a y vowel, or you get weird words.
        if(prevVowel):
            char = random.choice(ab)
            for vowel in vow1:
                if(char.upper() == vowel.upper()):
                    prevVowel = True
                else:
                    prevVowel = False
        else:
            char = random.choice(vow2)
            prevVowel = True

        if(capper == 1 and prevSpace):
            char = char.upper()
        str += char

        # Occasionally generate a space.
        if(random.randint(1,5) == 1 and not prevSpace):
            str += space
            prevSpace = True
        else:
            prevSpace = False

    print(str)



while True:
    namer()
