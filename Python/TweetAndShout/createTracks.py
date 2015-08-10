#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Song import Song

## make sure we're getting a kar file
inFileKar = ''
if len(sys.argv) > 1 and sys.argv[1].endswith(".kar"):
    inFileKar = sys.argv[1]
else:
    print "Please provide a .kar karaoke file"
    sys.exit(0)

## make sure we get a lyrics file
inFileLyrics = ''
if len(sys.argv) > 2:
    inFileLyrics = sys.argv[2]
else:
    print "Please provide a lyrics file"
    sys.exit(0)

## send to Song object to prepare the tracks
mySong = Song(inFileKar, inFileLyrics)
mySong.prepWordVoice()
