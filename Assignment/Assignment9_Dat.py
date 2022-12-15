# Name: Dat , ID: 100886108

import string

def getStringInfo(*args):
    for j in args:
        Words = len(j.split(" "))
        Chars = len([i for i in j])
        CharsWithoutWhitespace = len([i for i in j if not i.isspace()])
        Letters = len([i for i in j if i.isalpha()])
        Numbers = len([i for i in j if i.isnumeric()])
        Puntuations = len([i for i in j if i in string.punctuation])
        IsNumber = j.isnumeric()
        UppercaseChars = len([i for i in j if i.isupper()])
        LowercaseChars = len([i for i in j if i.islower()])
        Uppercase = j.upper()
        Lowercase = j.lower()
        ReversedCase = j.swapcase()
        NoSpaces = j.replace(" ", "")
        Title = j.title()
        Reversed = j[::-1]
        print("{:23} - {}".format("# of Words", Words))
        print("{:23} - {}".format("# of Chars", Chars))
        print("{:23} - {}".format("# of Chars (Excl. w/s)", CharsWithoutWhitespace))
        print("{:23} - {}".format("# of letters", Letters))
        print("{:23} - {}".format("# of numbers", Numbers))
        print("{:23} - {}".format("# of punctuations", Puntuations))
        print("{:23} - {}".format("Is number", IsNumber))
        print("{:23} - {}".format("# of Uppercase Chars", UppercaseChars))
        print("{:23} - {}".format("# of Lowercase Chars", LowercaseChars))
        print("{:23} - {}".format("Uppercase", Uppercase))
        print("{:23} - {}".format("Lowercase", Lowercase))
        print("{:23} - {}".format("Reversed Case", ReversedCase))
        print("{:23} - {}".format("No Spaces", NoSpaces))
        print("{:23} - {}".format("Title", Title))
        print("{:23} - {}".format("Reversed", Reversed))
        print("\n", "#" * 100)
        print()


getStringInfo("HeLlO wOrLd!!11", "Did you hear about the one-eyed one-horned Flying Purple People Eater?")