#meta

Document Purpose
 ===
1. To serve as a note-taking repository for articles, papers and work.
2. To serve as a collaborative platform for like-minded individuals to share and unify ideas and notes.
3. To leverage on Obsidian's graph view, so as to better interconnect new ideas with old ones.


Scripts
 ===
 Embedded in this Obsidian vault is a bunch of python scripts that I use to further optimize my workflow. You may have to install some dependencies. 
 
annotations_to_md.py: This is a script for converting annotated PDFs into markdown. Combined with it are a few folders designed to keep it neat and tidy.
- See [[Motivations for annotations_to_md.py]]

url_to_pdf.py and [[links_to_download]]: This is for downloading multiple URLs. Modify the [[links_to_download]] markdown and then run the script.

YoutubeAnnotator.py and [[YoutubeAnnotator]]: 
- Sometimes you watch a good youtube video and you want to combine notes with snippets of the video (e.g. [[Video-Based Generative Patch Nearest Neighbours]]). 
- All you have to do is then update [[YoutubeAnnotator]] and then run the ```YoutubeAnnotator.py``` script to generate the markdown. 
- An example is shown at [[YoutubeAnnotator Example]]

snippet_extractor.py: 
- The motivation for this is quite simple: I wanted to contextualize my sublime text snippets using notes in Obsidian. 
	- It'll also make it easier for me to backup and manage my snippets
- First, I setup an Obsidian snippet to facilitate the ease of generating sublime text snippets. Setting this up and using it can be found via this link: [[Using text snippets]]
- Next, I setup the script `snippet_extractor.py` in the Scripts directory to use the correct `SUBLIME_TEXT_SNIPPET_DIR` and `ROOT` directories. `SUBLIME_TEXT_SNIPPET_DIR` can be found by going Tools > Developer > New Snippet... > Save and then getting the directory that Sublime Text attempts to save the snippet to. 
	- Currently it uses a rather rudimentary system of hardcoded file paths; I might extend it to just use a `.env` file instead to separate config and code. 
- I then intermingle my notes and my code. I have a few examples like [[Python IO]]. 
- Additional documentation on how the script works can be found in the script itself.

encryption_manager.py:
- While I want to use this system and back it up on the cloud / GitHub, there are some stuff that I may want to keep secret. The `encryption_manager.py` script is thus a way to encrypt / decrypt files in the vault. Automating the procedure with something like Husky require me to install node modules, which is incompatible with the way I'm backing this vault up in Google Cloud; thus I opted for a more manual method.

.env file:
- For some of the scripts to work properly, they rely on the existence of a .env file to define the environment variables. Save this file in the `Scripts` directory, modifying the variables as necessary.
- SUBLIME_TEXT_SNIPPET_DIR: Folder to store generated sublime text snippets.
- ROOT: Root folder. 
- SALT: Salt to combine with the password for encrypting data.
```
SUBLIME_TEXT_SNIPPET_DIR = D:\\DownloadsHDD\\sublime_text_build_4113_x64\\Data\\Packages\\User\\
ROOT = G:\\My Drive\\Obsidian\\MattLeeThoughts
SALT = SaltedChickenIsDelicious
```