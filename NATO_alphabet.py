
""" Script that turns a word into separate NATO words."""
NATO = {
    'A': 'Alfa', 
    'B': 'Bravo', 
    'C': 'Charlie', 
    'D': 'Delta', 
    'E': 'Echo', 
    'F': 'Foxtrot', 
    'G': 'Golf', 
    'H': 'Hotel', 
    'I': 'India', 
    'J': 'Juliet', 
    'K': 'Kilo', 
    'L': 'Lima', 
    'M': 'Mike', 
    'N': 'November', 
    'O': 'Oscar', 
    'P': 'Papa', 
    'Q': 'Quebec', 
    'R': 'Romeo', 
    'S': 'Sierra', 
    'T': 'Tango', 
    'U': 'Uniform', 
    'V': 'Victor', 
    'W': 'Whiskey', 
    'X': 'X-ray', 
    'Y': 'Yankee', 
    'Z': 'Zulu'
}
def code_func():
    sentence = input("Enter a word: ").upper()
    try:
        code_list = [NATO[letter] for letter in sentence]
        
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        code_func()
    else:
        print(code_list)
        go_again = input("\nDo you want to add another word? 'y' or 'n': ").lower()
        if go_again == "y":
            code_func()
        else:
            print("Goodbye.")
     



print("Welcome to the NATO Alphabet utility\n")
code_func()