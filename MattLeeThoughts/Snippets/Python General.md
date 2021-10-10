```python
# Region marker		 | Syntax		 | Name of snippet
#region SHORTSNIPPET | source.python | file-header
"""
$TM_FILENAME : ${1:Description}
"""

__author__ = "Matt Lee"
__copyright__ = "Copyright 2021, crazoter"
__license__ = "GPL 3.0"
__version__ = "1.0.0"
```

Basic Template
```python
# Region marker		 | Syntax		 | Name of snippet
#region SHORTSNIPPET | source.python | basic-body
if __name__ == "__main__":
	${1:Body}
```

Regex match
```Python
# This is an automatically generated template for Sublime Text snippets. For more information, see https://sublime-text-unofficial-documentation.readthedocs.io/en/stable/extensibility/snippets.html
# Fields: ${1:this} is a ${2:snippet}
# Context: $SELECTION
# File is saved using tabTrigger name.

#region SNIPPET
<snippet>
<content>
<![CDATA[
# https://stackoverflow.com/questions/1327369/extract-part-of-a-regex-match
# ${1:import re}
regex_search = re.search('<title>(.*)</title>', html, re.IGNORECASE)
if regex_search:
    title = regex_search.group(1)
]]></content>
<tabTrigger>regex-group</tabTrigger>
<scope>source.python</scope>
</snippet>
#endregion
```

Enums
```Python
#region SNIPPET
<snippet><content><![CDATA[
# https://docs.python.org/3/library/enum.html
# # e.g. Color.RED
from enum import Enum
class ${1:ClassName}(Enum):
	${2:ENUM_NAME} = ${3:1}
]]></content><tabTrigger>enums</tabTrigger>
<scope>source.python</scope></snippet>
#endregion
```

Command line execution
```python
# Region marker		 | Syntax		 | Name of snippet
#region SHORTSNIPPET | source.python | cmd

# src: https://stackoverflow.com/questions/89228/how-to-execute-a-program-or-call-a-system-command
${1:import subprocess}
subprocess.run(['ls', '-l'])
```

Quick python script dependency setup
```python
# Region marker		 | Syntax		 | Name of snippet
#region SHORTSNIPPET | source.python | dependencies-setup
# Install required dependencies if not already installed
# https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t
import sys
import subprocess
import pkg_resources

required = {"${1:pkg1}"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print("Installing missing required dependencies...")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
```

.env file
```python
# Region marker		 | Syntax		 | Name of snippet
#region SHORTSNIPPET | source.python | dotenv
# Load variables from environment file
# Requires python-dotenv
# https://stackoverflow.com/questions/40216311/reading-in-environment-variables-from-an-environment-file
import os
from dotenv import load_dotenv
# .env file contains MY_ENV_VAR="This is my env var content."
load_dotenv()
${1:MY_ENV_VAR} = os.getenv("${1:MY_ENV_VAR}")
ENV = {
	"${1:MY_ENV_VAR}" = os.getenv("${1:MY_ENV_VAR}"),
}
for key in ENV:
	if ENV[key] == None:
		print(f"Error: {key} is not defined (is there a .env file in the directory?)")
		print(f"The .env file should contain '{key} = someValue,SeeDocumentation'")
		input("Press Enter to continue...")
		exit()

```

Press any key to continue
```python
# Region marker		 | Syntax		 | Name of snippet
#region SHORTSNIPPET | source.python | press-enter-to-exit
input("Press Enter to continue...")
```