"""
utils.py : Common utils used by my scripts
"""

__author__ = "Matt Lee"
__copyright__ = "Copyright 2021, crazoter"
__license__ = "GPL 3.0"
__version__ = "1.0.0"


def installMissingPackages(required):
	import sys
	import subprocess
	import pkg_resources
	# Install required dependencies if not already installed
	# https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t
	# required = {"pdfrw"}
	installed = {pkg.key for pkg in pkg_resources.working_set}
	missing = required - installed

	if missing:
	    print("Installing missing required dependencies...")
	    python = sys.executable
	    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

def load_env(env_varnames):
	import os
	from dotenv import load_dotenv
	# Load variables from environment file
	# Requires python-dotenv
	# https://stackoverflow.com/questions/40216311/reading-in-environment-variables-from-an-environment-file
	# .env file contains MY_ENV_VAR="This is my env var content."
	load_dotenv()
	ENV = {}
	for i in env_varnames:
		ENV[i] = os.getenv(i)
	for key in ENV:
		if ENV[key] == None:
			print(f"Error: {key} is not defined (is there a .env file in the directory?)")
			print(f"The .env file should contain '{key} = someValue,SeeDocumentation'")
			input("Press Enter to continue...")
			exit()
	return ENV