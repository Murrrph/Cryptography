## Caesar Cipher Decryption


import cryptoFunctions as cfns


##__MAIN__##

## Determine shift value
print '\nPlease enter the shift value: '

shift = int(raw_input())    ## Amount plaintext characters were shifted

## Enter the message to decrypt
print '\nEnter the message to decrypt: '

cipherText = raw_input()    ## Encrypted message

message = ""    ## Initialize decrypted text

## Shift each character
for char in cipherText:

	newChar = cfns.shiftChar(26 - shift, char)
	message += newChar


print '\nDecrypted message:'
print message
print "\n"

