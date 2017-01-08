## Module containing functions for cryptographic algorithms
##
## Written by David Shaw
##
## Created:     December 30, 2016
## Last edit:   December 30, 2016



## Function to shift a letter by a given amount
## Currently used in caesarEncrypt.py, caesarDecrypt.py
def shiftChar(shift, char):

        ## Case 1 - lowercase letter
        if char.islower():
                newChar = chr(ord('a') + (ord(char) - ord('a') + shift) % 26)

        ## Case 2 - uppercase letter
        elif char.isupper():
                newChar = chr(ord('A') + (ord(char) - ord('A') + shift) % 26)

        ## Case 3 - anything else
        else:
                newChar = char

        return newChar


