# Input Data
text1 = "Hit me with your pet shark! The stranger officiates the meal. Now I need to ponder my existence and ask myself if I'm truly real He didn’t want to go to the dentist, yet he went anyway. A good example of a useful vegetable is medicinal rhubarb. Best friends are like old tomatoes and shoelaces. He put heat on the wound to see what would grow."
text2 = "The delicious aroma from the kitchen was ruined by cigarette smoke. Love is not like pizza-donuts!!!"
input_text = "Hello, this is Kanika!"
input_text1 = "I am Kanika Agimudie who recently returned to writing computer programs. It has been my obsession with becoming a Software Developer over ten (10) years ago and I decided to revisit programming once again. My ultimate goal is to leave my 9 to 5 job and pursue my passion for developing software specializing in Web Applications and working remotely. I am at the stage of deciding on what is my main language or framework to solidify my path. Currently, I am learning Python and enrolled in a web development Bootcamp on Udemy. My passion is programming, for several reasons, the main of which is the jubilation of having your ideas rendered into reality on the screen. Another is being able to provide solutions for improving existing and new business processes and even life. Another reason I am working diligently on becoming a successful Software Developer; is that I can make a significant contribution to my society both professionally and personally. Ultimately encouraged my peers and children to get into Information Technology (IT). As well as having the experience and influence to assist Governments and NGOs in improving the IT infrastructure of my country. I look forward to meeting IT personnel from various sectors and countries as part of my professional journey. For collaboration, cooperation, and innovation, thus providing each other with a wealth of information and knowledge. And in so doing making my career dreams come true."
# Set length of hash value
hashvaluesize = 100

# Values use to create hash values
code_dictionary = [2, 3, 1, 0, 3, 1, 1, 3, 2, 3, 1, 3, 0, 3, 2, 2, 3]
# Length of the dictionary
length_dictionary = len(code_dictionary)

def hash_function(character, code):

    """ 
    Return a hash value based on a defined formula
    character (char): character from the input text
    code (int): index for the code dictionary
    return: char value
    Convert character to the ASCII equivalent using built-in Python function ord(). 
    Find the results of the value in the code_dictionary located at the index defined raised to the power of 2
    using the built-in Python function pwr().
    Perform an arithmetic operation i.e. minus power result from ASCII value. 
    Convert the difference into a character using the built-in Python function chr()
    """ 
    return chr(ord(character) -  pow(code_dictionary[code],2))


def codex_start(textsize, character):
    
    """ 
    Return an index for the code_dictionary 
    textsize (int): length of the input size
    character (char): character from the input text
    return: integer value
    Sum textsize, the number 35, length of the code dictionary, the ASCII equivalent of the character entered. 
    Find the average of the sum numbers.
    Find the reminder result of the average divided by length of the code dictionary
    """ 
    return int((textsize + 35 + length_dictionary + ord(character))/4) % length_dictionary

def expand(text):
    """
    Return a hash value of 100 characters representing text entered 
    text (string): input to be converted
    Takes a string and access each character from it and converts them to another character.
    To ensure the hash value is 100 length, add additional characters. 
    """
    print("\nRan Expanded")
    # Length input text entered
    size = len(text)
    # Number of characters needed to make up a 100 length hash
    characters_needed = characters = int(hashvaluesize/size)
    # Get an index for starting to access code dictionary items
    codex_index = codex_start(size, text[0])
    # Initialize the hashvalue to an empty string
    hashvalue = ""
    
    # Get each index of the text entered
    for index in range(0, size):

        # Check how many more characters are needed to create the hash value of 100 length
        while characters_needed > 0:
            # Convert a character of the input text to a hash character
            hashvalue += hash_function(text[index], codex_index)
            # Decrease the number of characters needed 
            characters_needed -= 1
            # Get the next index of the code dictionary 
            codex_index += 1

            # If at last index start at index to
            if codex_index == length_dictionary-1:
                codex_index = 2
        
        # Reset index value
        codex_index = 0
        # Reset number of characters needed
        characters_needed = characters

    #print(f"Length of Hash: {len(hashvalue)}")

    # Check the length of the current hashvalue
    hashvaluelength = len(hashvalue)

    # If it less than 100 
    if hashvaluelength < hashvaluesize:
        # Get difference of the length and 100
        remaining = hashvaluesize - hashvaluelength
        # Initialize text index and code dictionary index to 0
        index = 0
        codex_index = 0

        # Check how many more characters to add to make 100 length hash
        while remaining > 0:
            # Convert a character of the input text to a hash character
            hashvalue += hash_function(text[index], codex_index)
            # Go to the next index
            index +=1
            codex_index += 1
            # Decrease the number of characters needed
            remaining -= 1
            
            # Reset the index when it is the last index
            if index == size -1:
                 index = 0
            
            # Reset the index for the code dictionary when it reaches last index
            if codex_index == length_dictionary-1:
                codex_index = codex_start(size, text[index])

    #print(f"Final Length of Hash: {len(hashvalue)}")
    return hashvalue

def compress(text):
    """
    Return a hash value of 100 characters representing text entered 
    text (string): input to be converted
    Takes a string and access each character combines the characters in groups, to get 100 individual combinations.
    Finds the sum of the ASCII code of each character in the group and sum them.
    Find the average of the sum and hash the character of the average. 
    """
    print("\nRan Compressed")
    # Length input text entered
    size = len(text)
    # Initialize the hashvalue to an empty string
    hashvalue = ""
    # Determine the number of character combinations to shrink input to to represent 100
    combinations = numofcombo = int(size / hashvaluesize)
    remaining = size % hashvaluesize
    # Initialize values for the sum of characters combination, the amount of the hash value, index for code dictionary and index of input
    combinations_sum = 0
    amount = hashvaluesize
    codex_index = codex_start(size, text[0])
    index = 0
       
    # Check if the number of hashes to be created is more than 0
    while amount > 0:
        
        # Check how many additional characters to add to combination
        if remaining > 0:
            combinations += 1
        
        # Check how many characters remaining in the combinations 
        while combinations > 0:
            # Add the ASCII code of each character in the input text
            combinations_sum +=  ord(text[index])
            # Go to the next index
            index += 1
            # Decrease the number of remaining combinations
            combinations -= 1
        
        # Decrease number of remaining characters and amount to make up 100
        remaining -= 1
        amount -= 1
        # Reset combination value to original
        combinations = numofcombo
        # Get hash value for each character combination
        hashvalue += hash_function(chr(int(combinations_sum/numofcombo)), codex_index)
        # Get next index of the code dictionary
        codex_index += 1
        # Reset combinations_sum to 0
        combinations_sum = 0
        
        # Reset the index for the code dictionary when it reaches last index
        if codex_index == length_dictionary-1:
            codex_index = codex_start(size, text[index])
        
    #print(f"Final Length of Hash: {len(hashvalue)}")
    return hashvalue

# Testing
print(f"Input Text: {input_text} \n\tof length {len(input_text)}")
print(f"{expand(input_text)}")
print(f"\nInput Text: {input_text1}  \n\tof length {len(input_text1)}")
print(f"{compress(input_text1)}")

# To create hash, first check if the text 
print(f"\nInput Text: {text1}  \n\tof length {len(text1)}")
if len(text1) > 100:
    print(compress(text1))
else:
    print(expand(text1))

print(f"\nInput Text: {text2}  \n\tof length {len(text2)}")
if len(text2) > 100:
    print(compress(text2))
else:
    print(expand(text2))

