#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pdf_downloader.py: Read urls and download them as PDF.
"""

__author__ = "Matt Lee"
__copyright__ = "Copyright 2021, crazoter"
__license__ = "GPL 3.0"
__version__ = "1.0.1"

import os

scriptdir = os.path.dirname(os.path.abspath(__file__))
youtube_embed_format = '<iframe width="560" height="315" src="https://www.youtube.com/embed/{0}?start={1}&end={2}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

def mmss_to_ss(mmss):
    parts = mmss.split(':')
    val = 0
    multiplier = 1
    for i in reversed(parts):
        val += int(i.strip()) * multiplier
        multiplier *= 60
    return val


if __name__ == "__main__":
    file = os.path.join(scriptdir, "./YoutubeAnnotator.md")
    # Writing to file
    outfp = None
    youtube_id = None
    try:     
        # Read file w/ for loop
        with open(file, 'r') as fp:
            for line in fp:
                line = line.strip();
                if len(line) <= 0:
                    continue
                # Skip comments
                if line.strip()[0] == '#':
                    continue
                if not outfp:
                    # Open and write, create if not exist
                    outfp = open(os.path.join(scriptdir,line), 'w+')
                    continue
                if not youtube_id:
                    youtube_id = line
                    outfp.write(f'#### URL: https://www.youtube.com/watch?v={line}\n\n')
                    continue

                if line.strip()[0] == '$':
                    outfp.write(line[1:] + "\n")
                else:
                    # timestamp
                    parts = line.split('-')
                    ss1 = mmss_to_ss(parts[0])
                    ss2 = mmss_to_ss(parts[1])
                    duration = int(ss2) - int(ss1)
                    outfp.write(f'{youtube_embed_format.format(youtube_id, ss1, ss2)}\n\n*<span style="color:lightgray">{parts[0]} - {parts[1]} ({duration}s)</span>* \n\n')
    except Exception as e:
        print(e)
    finally:
        if outfp:
            outfp.close()