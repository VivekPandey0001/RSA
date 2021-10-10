# RSA
Cryptography Algorithm RSA Python Implementation

For encrypting and decrypting files.

# Modules
Endec.py:
  Base class Endec

En.py:
  class En, for encryption 
  Use enc_runner function to encrypt all files (except the three source files) present in the same folder into an [output] folder named 'endec' by default.
  encrypted files will have [postfix string] in the name '\_' by default.

Dec.py:
  class En, for decryption
  Use dec_runner function to decrypt all files (except the three source files) present in the same folder into an [output] folder named 'endec' by default.
  decrypted files will have [postfix string] in the name '\_' by default.

# Usage
Basic steps -
- move file to the folder whose content needs to be encrypted/decrypted. 
- run the code, give appropriate keys (n, k)
- files will be encrypted/decrypted and stored in an output folder in the same directory

# Extra Features
output folder name can be given as input (default: 'endec')

output file names can be further diffrentiated with some postfix string (default: '\_')

Display stats such as - 
  time taken
  files processed
  speed Bytes/Second, etc

