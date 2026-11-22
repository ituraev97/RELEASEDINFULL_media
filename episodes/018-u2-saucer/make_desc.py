#!/usr/bin/env python3
"""Writes youtube_description.txt for FILE 018 with chapters from timing.json."""
import json, importlib.util, os
ep = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("e", os.path.join(ep, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
T = json.load(open(os.path.join(ep, "timing.json")))
def mmss(t): t = int(t); return f"{t // 60}:{t % 60:02d}"
ch = ["0:00 The U-2 designer's \"saucer\""]
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter":
            ch.append(f"{mmss(T['starts'][i])} {s[2]['n']}. {s[2]['t']}")
desc = """Why did the man who designed the U-2 spy plane tell the Air Force he was "more firmly convinced than ever" that flying saucers exist? The Pentagon's eighth release of UFO files (Nov. 20, 2026) includes Kelly Johnson's 1953 report, his Lockheed test crew's statements, and the Air Force's answer on the index card: "lenticular cloud."
We read the Lockheed file line by line, then open the rest of PURSUE Release 08: 1952 CIA memos on flying saucers ("no shred of evidence"; keep CIA interest from "the press or public"), the 1957 Levelland, Texas reports of stalled engines, Senator Harry Reid's 2009 request for a special access program and the DIA's answer, a contractor's 2009 plan for an underground vault for "exotic material or tissue," a 2023 radar track that would be Mach 2.5 if it were one object, and three new CENTCOM videos.

Facts come from the released documents; witness accounts are attributed; the documents do not identify what Johnson saw, and neither do we.

Question for you: Johnson's test crew said it was not a cloud. The Air Force wrote "lenticular cloud." Who do you believe, and why? Tell us in the comments.

""" + "\n".join(ch) + """

SOURCES
• Department of War, PURSUE Release 08 (Nov. 20, 2026): https://www.war.gov/UFO/ — unmodified copies of the files used here: https://archive.org/details/pursue-uap-documents-2026 (folder Release_08)
  – DOW-UAP-D206, Lockheed reports on a "flying saucer," Dec. 16, 1953, with Air Force index card and cover letter
  – CIA-UAP-D024, D026, D027 (OSI briefing, Aug. 14, 1952), D028 (Oct. 13, 1952)
  – DOW-UAP-D191, Air Intelligence Information Report, Levelland, Texas (Nov. 1957); DOW-UAP-D193, White Sands (Nov. 1957); DOW-UAP-D207 and D209, Project 10073 record cards
  – DOW-UAP-D183, letter from Sen. Harry Reid (June 24, 2009); DOW-UAP-D184 and D187, DIA talking papers (2009); DOW-UAP-D185, DIA review of SAP request (Nov. 2009); DOW-UAP-D186, DIA information memo (Dec. 2010); DOW-UAP-D188, DIA Defense Warning Office review (Oct. 2009)
  – DOW-UAP-D172, BAASS Ten Month Report (July 2009), PDF pp. 9 and 496
  – DOW-UAP-D165, Unresolved Radar Detection, United States, 2023
  – Videos DOW-UAP-PR166, PR168, PR169 (CENTCOM): https://www.dvidshub.net/video/1030270 , https://www.dvidshub.net/video/1030274 , https://www.dvidshub.net/video/1030277
• CBS News (Nov. 20, 2026): https://www.cbsnews.com/news/ufo-files-pentagon-contractor/
• FOX Local / LiveNOW (Nov. 20, 2026): https://www.ktvu.com/news/pentagon-releases-eighth-batch-declassified-ufo-files
• Interesting Engineering (Nov. 20, 2026): https://interestingengineering.com/culture/pentagon-1953-dark-elliptical-ufo-lockheed-engineer
• History.com on the Robertson Panel: https://www.history.com/articles/ufo-sightings-cia-robertson-condon

FOOTAGE
Document pages: PURSUE Release 08 as released; black bars over private witnesses' names were added by us. Videos PR166, PR168 and PR169 as released. Photos and b-roll via DVIDS (public domain): U-2 at Beale Air Force Base, California (2014, 2023, 2024, 2026); Point Mugu, California, at sunset (2022); Las Vegas at night from Nellis AFB (2026); Lubbock, Texas (2020); the U.S. Capitol (2012). Modern images do not show the events described; every shot is labelled on screen with what it actually shows. Appearance of U.S. government visual information does not imply or constitute endorsement.

Music and sound effects are original.
Independent channel. Not affiliated with or endorsed by any U.S. government agency.

This video reports on official public records. Inclusion of a name in released records does not imply wrongdoing. Allegations are unproven unless stated otherwise.

#UFOFiles #KellyJohnson #FlyingSaucers #Declassified #UAP

FILE 018"""
open(os.path.join(ep, "youtube_description.txt"), "w").write(desc)
print(len(desc), "chars"); print("\n".join(ch))
