"""
Use helper functions:
    1)get_story_string() that returns the encrypted version of the story as a string.
      Create a CiphertextMessage object using the story string and use
    2)decrypt_message to return the appropriate shift value and unencrypted story string.

"""

def decrypt_story():
    encryptedStory = CiphertextMessage(get_story_string())
    decryptedStory = encryptedStory.decrypt_message()
    return decryptedStory
