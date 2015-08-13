#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re, sys
import midifile

OUT_KAR_DIR = "./out-kars/"
OUT_LYRICS_DIR = "./out-lyrics/"

## make sure we're getting a kar file
inFileKar = ''
if len(sys.argv) > 1 and sys.argv[1].endswith(".kar"):
    inFileKar = sys.argv[1]
else:
    print "Please provide a .kar karaoke file"
    sys.exit(0)

## read it and make sure it's a valid kar file
myKar = midifile.midifile()
myKar.load_file(inFileKar)
if not myKar.karfile:
    print "This is not a valid karaoke file"
    sys.exit(0)

## get filename from file location
filename = os.path.basename(inFileKar)

## create directory for decomposed kar files
if not os.path.exists(OUT_KAR_DIR):
    os.makedirs(OUT_KAR_DIR)

## determine which tracks are being used for notes
candidateTracks = {}
for v in myKar.notes:
    candidateTracks[v[4]] = 'notes'

## write out one file per karaoke track
for n in candidateTracks:
    tracks2remove = [t for t in candidateTracks if t!=n and t!=myKar.kartrack]
    outFileKar = filename.replace(".kar", ".%s.kar"%(n))
    myKar.write_file(inFileKar, os.path.join(OUT_KAR_DIR, outFileKar), tracks2remove, None)


## create directory for decomposed lyrics files
if not os.path.exists(OUT_LYRICS_DIR):
    os.makedirs(OUT_LYRICS_DIR)

## clean up syllables, make lyrics string
lyrics = ""
for s in myKar.karsyl:
    s = re.sub('[\\\\/_]', ' ', s)
    s = re.sub('[,.;!?\"\']', '', s)
    lyrics += s

## write out lyrics one word per line
outFileLyrics = filename.replace(".kar", ".lyrics.txt")
with open(os.path.join(OUT_LYRICS_DIR, outFileLyrics), 'w') as lyricsFile:
    for w in lyrics.strip().split(" "):
        if w != "":
            lyricsFile.write("%s\n"%w.decode('iso-8859-1').lower().encode('utf-8'))

