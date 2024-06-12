# Secret Decoder Ring
#### Video Demo:  [CS 50 Final Project](https://youtu.be/LteiIYepv5I)
#### Description:
This program acts as a secret decoder ring to encode and decode the user's message using a simple [substitution cipher](https://en.wikipedia.org/wiki/Caesar_cipher). The program can be run in either `--encode` or `--decode` mode. The user is prompted for a phrase, that must only contain alpha characters or spaces, and a shift value. The program then either encodes or decodes the phrase and displays the original and coded text.

Currently, the program only implements a Caesar cipher where letters are shifted left or right by a numerical value. However, the program was structured to allow for additional ciphers to be added easily as long as they adhere to a standard interface of `cipher.encode` and `cipher.decode`

Files:
* `project.py`: Main project file. Processes command-line flags, takes user input, configures cipher, encodes/decodes phrase
* `test_project.py`: Tests main project file
* `cipher.py`: Implements Caesar cipher with a simple, standardized interface allowing for future extension. `encode` and `decode` handle the substitution of letters in a word
* `test_cipher.py`: Tests the cipher implementation