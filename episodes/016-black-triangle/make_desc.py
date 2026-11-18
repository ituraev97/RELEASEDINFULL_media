#!/usr/bin/env python3
"""Writes youtube_description.txt for FILE 016 with chapters from timing.json."""
import json, importlib.util, os
ep = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("e", os.path.join(ep, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
T = json.load(open(os.path.join(ep, "timing.json")))
def mmss(t): t = int(t); return f"{t // 60}:{t % 60:02d}"
ch = ["0:00 Two agents, one silent triangle"]
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter":
            ch.append(f"{mmss(T['starts'][i])} {s[2]['n']}. {s[2]['t']}")
desc = f"""What did two federal agents see over a ridge in 2026? In its seventh release of UFO files (Oct. 23, 2026), the Pentagon published an AARO memo and an FBI report about a silent, matte-black triangle that climbed, hovered and dropped into a canyon. The two official accounts don't agree on how long it lasted.
We read the black triangle UFO files line by line, then open the rest of PURSUE Release 07: three Boy Scouts on Catalina Island in 1952, a B-52 gunner's radar contact over Saudi Arabia during Operation Power Flite (1957), a Swedish airline pilot's "unmanned robot" (1953), a 1963 memo on who collects fallen space hardware ("use NASA for a 'cover'," in a NASA official's view), and the "Skinwalker" ranch report's DNA results.

Facts come from the released documents; witness accounts are attributed; the documents themselves do not identify the object, and neither do we.

Question for you: two official reports describe the same evening, about thirty seconds versus three. Which account do you trust more, and why? Tell us in the comments.

""" + "\n".join(ch) + """

SOURCES
• Department of War, PURSUE Release 07 (Oct. 23, 2026): https://www.war.gov/UFO/ — unmodified copies of the files used here: https://archive.org/details/pursue-uap-documents-2026 (folder Release_07)
  – DOW-UAP-D176, AARO Memorandum for Record, triangular UAP (2026)
  – FBI-UAP-D043, FD-302 with co-signed statement and nine depiction images (2026)
  – DOW-UAP-D179 / D177, Santa Catalina reports (1952, 1955); DOW-UAP-D164, Atterbury AFB report, Indiana (1954)
  – DOW-UAP-D155, Air Intelligence Information Report, Saudi Arabia (1957)
  – DOW-UAP-D163, air attaché report, Stockholm (1954); DOW-UAP-D160, French Morocco (1953); DOW-UAP-D162, Alaska (1953)
  – EOP-UAP-D002, memo on recovery of foreign materiel (May 29, 1963); USG-UAP-D002, space-fragment correspondence (1962–64, LBJ Library)
  – DOW-UAP-D174, BAASS "Utah Ranch Investigation" (April 2010), incl. lab report and analysis
• EarthSky, "Pentagon UAP files part 7" (Oct. 2026): https://earthsky.org/human-world/pentagon-uap-files-ufos-batch-7
• Anadolu Agency (Oct. 23, 2026): https://www.aa.com.tr/en/americas/pentagon-releases-7th-batch-of-ufo-files/4098640
• The National Desk / KMPH (Oct. 23, 2026): https://kmph.com/newsletter-daily/federal-agents-reported-seeing-silent-black-triangle-in-latest-ufo-file-release-defense-department-presidential-unsealing-reporting-system-uap-encounters-fbi-extraterrestrial-activity
• Air Force Global Strike Command, "Year of the B-52: B-52s make historic nonstop around-the-world flights": https://www.afgsc.af.mil/News/Article-Display/Article/454903/year-of-the-b-52-b-52s-make-historic-nonstop-around-the-world-flights/

FOOTAGE
Document pages: PURSUE Release 07 as released. The images of the triangle are depictions attached to the FBI report (a black shape placed into the same landscape), not photographs of the object. Black bars over names in the 1953 Swedish report were added by us. B-roll via DVIDS (public domain): dusk over the San Gabriel Mountains from Mt. Wilson, California (2026); B-52 takeoff and B-52 refuelling from a KC-135 (2026); a C-47 takeoff (2024); Santa Catalina Island (2019); a thermal imaging camera (2020); Canyon Lake Gorge, Texas (2026); a C-17 refuelling over the Grand Canyon (2021); Armed Forces DNA Identification Laboratory (2015); the U.S. Capitol (2012). Modern footage does not show the events described; every shot is labelled on screen with what it actually shows. Appearance of U.S. government visual information does not imply or constitute endorsement.

Music and sound effects are original.
Independent channel. Not affiliated with or endorsed by any U.S. government agency.

This video reports on official public records. Inclusion of a name in released records does not imply wrongdoing. Allegations are unproven unless stated otherwise.

#UFOFiles #BlackTriangle #UAP #Declassified #SkinwalkerRanch

FILE 016"""
open(os.path.join(ep, "youtube_description.txt"), "w").write(desc)
print(desc[:400]); print("\n".join(ch)); print(len(desc), "chars")
