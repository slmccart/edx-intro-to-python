# Secret Decoder Ring
#### Video Demo:  [CS 50 Final Project](https://youtu.be/LteiIYepv5I)
#### Description:
This program acts as a secret decoder ring to encode and decode the user's message using a simple [substitution cipher](https://en.wikipedia.org/wiki/Caesar_cipher). The program can be run in either `--encode` or `--decode` mode. The user is prompted for a phrase, that must only contain alpha characters or spaces, and a shift value. The program then either encodes or decodes the phrase and displays the original and coded text.

Error conditions:
If the user does not provide any command-line arguments, a usage message is printed, specifying that the user must past either the `--encode` or `--decode` flags. These options are mutually exclusive and one must be passed. If the user's phrase contains characters other than alpha characters or spaces, the program exits, instructing the user of the character requirements. If the user-provided shift value is not an integer, the program exits, instructing the user to enter an integer value.

Currently, the program only implements a Caesar cipher where letters are shifted left or right by a numerical value. The character shifting wraps around properly so that a `Z` shifted right by a value of `2` becomes `B`. However, the program was structured to allow for additional ciphers to be added easily as long as they adhere to a standard interface of `cipher.encode` and `cipher.decode`

Files:
* `project.py`: Main project file. Processes command-line flags, takes user input, configures cipher, encodes/decodes phrase
* `test_project.py`: Tests main project file
* `cipher.py`: Implements Caesar cipher with a simple, standardized interface allowing for future extension. `encode` and `decode` handle the substitution of letters in a word
* `test_cipher.py`: Tests the cipher implementation
