# Functions for the various methods of changing the text in attempt to encode it


def de_encrypt_alphabetorder(alphabet, offset):
    alphabet_list = []  # To store a list of all the alphabet characters
    new_alphabet_list = []  # To store a list of all the new alphabet characters

    for char in alphabet:  # To loop through all the characters in the alphabet
        alphabet_list.append(char)  # To populate the original alphabet list

    if abs(offset) >= len(alphabet):  # While the offset is longer than the alphabet
        if offset > 0:  # For positive offsets (encryption)
            offset = offset - len(alphabet) + 1
        elif offset < 0:  # For negative offsets (decryption)
            offset = -(abs(offset) - len(alphabet) + 1)

    while len(new_alphabet_list) < len(alphabet):  # To repeat until the new alphabet is as long as the original
        temp_characters = []  # To store the characters in each loop
        i = 0  # Original index position
        while i < len(alphabet_list):  # To loop while the index is within the alphabet
            temp_characters.append(alphabet_list[i])  # Adds a character to the temp characters list
            i += abs(offset)  # To change the offset value

        for char in temp_characters:  # To loop through the characters in the temp characters list
            alphabet_list.remove(char)  # Removes each of these characters from the original alphabet
            new_alphabet_list.append(char)  # To add each character to the new alphabet list

    new_alphabet = ''.join(new_alphabet_list)  # To join the new alphabet list into a single string
    return new_alphabet


def de_encrypt_wordorder(text, offset):
    new_words = []  # To store the new word order in

    words = text.split()  # To split the text string into a list of words

    while abs(offset) >= len(words):  # While the offset is longer than the list
        if offset > 0:  # For positive offsets (encryption)
            offset = offset - len(words)
        elif offset < 0:  # For negative offsets (decryption)
            offset = -(abs(offset) - len(words))

    if len(words) > 1:  # Only do this is there is more than one word
        for i in range(len(words)):  # To loop through the indexes for each word
            new_i = i + offset  # The new index is the original plus an offset

            if new_i >= len(words):  # If the offset index is greater than the max list index
                new_i = i - (len(words)) + offset  # Index position will go back to fill in from the start

            new_words.append(words[new_i])  # To add the new word order back into a list

    else:  # If there is only 1 or none words
        new_words = words  # Make the new words the same as the old words

    new_text = ' '.join(new_words)  # To join all the words back into a list
    return new_text


def de_encrypt_letterorder(text, offset):
    new_characters = []  # To store the new word order in

    words = text.split()  # To split the text string into a list of words
    for word in words:  # To loop through each word
        word_offset = offset  # To set the initial offset for each word

        if len(word) > 1:  # Only if the word is longer than 1 character
            for i in range(len(word)):  # To loop through the index in each word

                while abs(word_offset) >= len(word):  # While the offset is longer than the list
                    if word_offset > 0:  # For positive offsets (encryption)
                        word_offset = word_offset - len(word)
                    elif word_offset < 0:  # For negative offsets (decryption)
                        word_offset = -(abs(word_offset) - len(word))

                new_i = i + word_offset  # The new index is the original plus an offset

                while new_i >= len(word):  # If the offset index is greater than the words max index
                    new_i = new_i - (len(word))  # Index position will go back to fill in from the start

                new_characters.append(word[new_i])  # To add all the characters to the new characters list

            new_characters.append(' ')  # To add spaces back in between the words

        else:  # If the word is only one letter long
            new_characters.append(word)  # New characters is just the one word
            new_characters.append(' ')  # Need to add space as above line too

    if len(new_characters) > 1:  # If there is more than one new character
        del new_characters[-1]  # To delete the trailing space from the list

    new_text = ''.join(new_characters)  # To join all the characters into a single text string
    return new_text


def de_encrypt_characterswap(text, alphabet, offset):
    new_characters = []  # To store the new letters in

    for character in text:  # To loop through all the characters in the text
        ini_i = alphabet.find(character)  # To find the index position of each character from the text in the alphabet

        if offset > 0:  # For positive offsets (encryption)
            new_i = ini_i + abs(offset)  # To make a new index position for each character
        elif offset < 0:  # For negative offsets (decryption)
            new_i = ini_i + -abs(offset)

        while abs(new_i) >= len(alphabet)-1:  # If the index position is greater than the max index in the alphabet
            if offset > 0:  # For positive offsets (encryption)
                new_i = new_i - len(alphabet)  # This will reset it back to zero and try again
            elif offset < 0:  # For negative offsets (decryption)
                new_i = new_i + len(alphabet)

        new_characters.append(alphabet[new_i])  # To put all the new letters in a list

    new_text = ''.join(new_characters)  # To make the list into a single string
    return new_text


def encrypt(text, offsets):
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789.?!,;:-()[]{}'@#$%&+*/"  # alphabet
    new_offsets = []  # List to store all the new offsets

    for offset in offsets:  # To iterate through all the offsets
        new_offsets.append(abs(offset))  # To append teh absolute values of each offset as the new offset

    new_alphabet = de_encrypt_alphabetorder(base_alphabet, new_offsets[0])  # creates the new alphabet
    new_wordorder = de_encrypt_wordorder(text, new_offsets[1])  # Changes the word order
    new_letterorder = de_encrypt_letterorder(new_wordorder, new_offsets[2])  # Changes the letter order
    new_text = de_encrypt_characterswap(new_letterorder, new_alphabet, new_offsets[3])  # Performs the letter swap
    return new_text


def decrypt(text, offsets):
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789.?!,;:-()[]{}'@#$%&+*/"  # alphabet
    new_offsets = []  # List to store all the new offsets

    for offset in offsets:  # To loop through all the offsets in the offset list
        new_offsets.append(-abs(offset))  # To make all the new offsets negative

    new_alphabet = de_encrypt_alphabetorder(base_alphabet, abs(new_offsets[0]))  # To find the new alphabet again
    new_characterswap = de_encrypt_characterswap(text, new_alphabet, new_offsets[3])  # To change the characters back
    new_letterorder = de_encrypt_letterorder(new_characterswap, new_offsets[2])  # To change the letter order back
    new_text = de_encrypt_wordorder(new_letterorder, new_offsets[1])  # To change the word order back
    return new_text
