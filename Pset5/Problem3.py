"""
The methods you should fill in are:

    1)__init__(self, text): Use the parent class constructor to make your code more concise.
    2)decrypt_message(self): You may find the helper function is_word(wordlist, word) 
      and the string method split() useful. Note that is_word will ignore punctuation and other 
      special characters when considering whether a word is valid.
    
"""

class CiphertextMessage(Message):
    def __init__(self, text):
        """
        Initializes a CiphertextMessage object
        text (string): the message's text
        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        
        Message.__init__(self, text)
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        """
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.
        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return
        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        """
        
        wordList = load_words(WORDLIST_FILENAME)
        shift = 0
        total = 0
        maxShift = (0, 0)
        while shift <= 26:
            currentTotal = 0
            decryptedMessage = self.apply_shift(-shift)
            cryptedWords = decryptedMessage.split()
            for word in cryptedWords:
                if is_word(wordList, word):
                    currentTotal += 1
            if currentTotal > total:
                total = currentTotal
                maxShift = (26 - shift, decryptedMessage)
            shift += 1
        return maxShift
