"""
encrypt.py : Encrypt md files where the first line is '#encrypted'
https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/#installing-pycryptodome
"""

__author__ = "Matt Lee"
__copyright__ = "Copyright 2021, crazoter"
__license__ = "GPL 3.0"
__version__ = "1.0.0"

# Install required dependencies if not already installed
# https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t
import sys
import subprocess
import pkg_resources

required = {"python-dotenv", "pycryptodome"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print("Installing missing required dependencies...")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

# Load variables from environment file
# https://stackoverflow.com/questions/40216311/reading-in-environment-variables-from-an-environment-file
import os
from dotenv import load_dotenv
# .env file contains MY_ENV_VAR="This is my env var content."
load_dotenv(verbose=True)
ROOT = os.getenv("ROOT")
SALT = os.getenv("SALT")
if (not ROOT):
	print("Error: ROOT is not defined (is there a .env file in the directory?)")
	print("The .env file should contain 'ROOT = directoryOfObsidianVault'")
	input("Press Enter to continue...")
	exit()
if (not SALT):
	print("Error: SALT is not defined (is there a .env file in the directory?)")
	print("The .env file should contain 'SALT = aRandomSequenceOfCharacters'")
	input("Press Enter to continue...")
	exit()
# Convert to byte array format
SALT = SALT.encode()

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from pathlib import Path
import getpass


if __name__ == "__main__":
	encrypt = None
	while (encrypt == None):
		print("Choose action: Encrypt (E) or Decrypt (D): ")
		action = input()
		if (action.upper() == 'E'):
			encrypt = True
		elif (action.upper() == 'D'):
			encrypt = False
		else:
			print("Invalid choice; please input either 'E' or 'D'.")

	# print("Input your password: ")
	password = ""
	while len(password) <= 0:
		password = getpass.getpass("Input your password (length cannot be 0): ")
	key = PBKDF2(password, SALT, dkLen=32) # Your key that you can encrypt with

	if encrypt:
		# Req: Python 3.4+
		# https://stackoverflow.com/questions/18394147/recursive-sub-folder-search-and-return-files-in-a-list-python
		from pathlib import Path
		for filename in Path(ROOT).rglob("*.[mM][dD]"):
			encrypt_file = False
			# Check if we need to encrypt file
			with open(filename, 'r', errors='replace') as fp:
				if fp.readline().strip() == "#encrypted":
					encrypt_file = True
			if encrypt_file:
				output_file = str(filename).replace('.md', '-encrypted.bin')
				print(f"Encrypting {filename} as {output_file}")
				with open(filename, 'rb') as fp:
					data = bytearray(fp.read())

					cipher = AES.new(key, AES.MODE_CFB) # Create a AES cipher object with the key using the mode CBC
					ciphered_data = cipher.encrypt(data) # Pad the input data and then encrypt
					
					file_out = open(output_file, "wb") # Open file to write bytes
					file_out.write(cipher.iv) # Write the iv to the output file (will be required for decryption)
					file_out.write(ciphered_data) # Write the varying length ciphertext to the file (this is the encrypted data)
					file_out.close()
				os.remove(filename)
	else:
		# Req: Python 3.4+
		# https://stackoverflow.com/questions/18394147/recursive-sub-folder-search-and-return-files-in-a-list-python
		# Open up all -encrypted.bin files, which I assume to be encrypted
		for filename in Path(ROOT).rglob("*-encrypted.bin"):

			# Read the data from the file
			file_in = open(filename, 'rb')
			iv = file_in.read(16)
			ciphered_data = file_in.read()
			file_in.close()

			cipher = AES.new(key, AES.MODE_CFB, iv=iv)
			original_data = cipher.decrypt(ciphered_data) # No need to un-pad

			output_file = str(filename).replace("-encrypted.bin", ".md")
			print(f"Decrypting {filename} as {output_file}")
			file_out = open(output_file, "wb") # Open file to write bytes
			file_out.write(original_data)
			file_out.close()

	input("Press Enter to continue...")