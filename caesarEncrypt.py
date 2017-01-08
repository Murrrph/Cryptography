## Caesar Cipher Encryption


import cryptoFunctions as cfns


##__MAIN__##

## Determine shift value
print '\nPlease enter the shift value: '

shift = int(raw_input())    ## Amount to shift plaintext characters

## Enter the message to encrypt
print '\nEnter the message to encrypt: '

message = raw_input()    ## Plaintext message

cipherText = ""    ## Initialize encrypted text

## Shift each character
for char in message:

	newChar = cfns.shiftChar(shift, char)
	cipherText += newChar


print '\nEncrypted message:'
print cipherText
print "\n"

