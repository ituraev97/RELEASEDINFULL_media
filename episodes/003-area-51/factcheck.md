# FILE 003 — Area 51 · Independent fact-check

Date: 2026-10-31
Checker: independent (did not write the script)

## Sources actually opened
Primary (local):
- 1998 redacted CIA history, Pedlow & Welzenbach, "The CIA and the U-2 Program, 1954–1974": OCR /home/claude/dl/u2_1998.txt (full text read for all passages cited below); page scans /home/claude/fc/n66, p56, p56b, p57, p71, p72a, p72u, p73, title (viewed).
- Haines, "CIA's Role in the Study of UFOs, 1947–90" (CIA doc C00242525): page 73 scan /home/claude/fc/hi-07.jpg plus crops h07, h07q (viewed); OCR /home/claude/dl/haines_raw.txt.
- DVIDS footage frames pulled with ffmpeg from /home/claude/src/dv478042, dv402699, dv396020, dv507037, dv908150, dv995792 (.mp4), at every timestamp the script uses; still dvimg749221.jpg viewed.
- Asset check, /home/claude/src/img: ciamap.jpg and usgs1968.jpg are **not images**. Each is a saved "Wikimedia Error" HTML page. a12.jpg and landsat.jpg **do not exist**.

Online (WebFetch/WebSearch):
- https://nsarchive2.gwu.edu/NSAEBB/NSAEBB434/ (EBB 434 landing page)
- https://nsarchive2.gwu.edu/NSAEBB/NSAEBB434/docs/U2%20-%20Chapter%202.pdf (2013 release, ch. 2. The OCR is partly garbled around the AEC/Area 51 sentences.)
- https://nsarchive2.gwu.edu/NSAEBB/NSAEBB434/docs/U2%20-%20Chapter%203.pdf (2013 release, ch. 3)
- https://www.cia.gov/resources/csi/static/b45f5f8f5e4937963d9e9931313d84a4/Archangel-CIAs-Supersonic-A-12-Reconnaissance-Aircraft.pdf (Robarge, Archangel)
- https://lasvegassun.com/news/2013/aug/15/government-acknowledges-area-51-declassified-spy-p/
- https://foreignpolicy.com/2013/08/15/declassified-the-cias-secret-history-of-area-51/
- https://www.bangordailynews.com/2013/08/17/news/cia-acknowledges-its-mysterious-area-51-test-site-for-first-time/
- https://www.kunc.org/npr-news/2013-08-16/did-you-know-area-51-nearly-killed-4-important-visitors
- https://migflug.com/afterburner/u-2-dragon-lady-reprieve-fy2027-congress-blocks-retirement-2026/ (June 15, 2026, modified Oct 2, 2026) and https://theaviationist.com/2026/03/18/u-2-ads-updates/ (current status of the U-2)
- WebSearch result for the af.mil biography "Major General OSMOND J. RITLAND": https://www.af.mil/About-Us/Biographies/Display/Article/105825/major-general-osmond-j-ritland/
- Blocked or not answered: https://en.wikipedia.org/wiki/Area_51 (permission timeout)

---

## Verdicts by script line

**1. OK.** p56 crop is page 56 of the 1998 release. Label correct.

**2. NOTE.** The spoken heading "Preparations for testing the U-2" is real (1998, p. 55–56). But neither p56 nor p56b shows the heading on screen: p56 starts at "As work progressed…" and p56b is the lower half of the page. Optional: use a crop that includes the heading line.

**3. OK.** p57 (1998) is almost entirely blacked out.

**4. FIX (asset).** /home/claude/src/img/ciamap.jpg is a Wikimedia error HTML page, not the map. As it stands, nothing would render, or the wrong thing would. Replacement: obtain the actual image ("The CIA's declassified map of Groom Lake/Area 51", NSArchive EBB 434 or Commons "CIA declassified map of Groom Lake and Area 51.jpg"), check it, then keep the label. NOTE: the 2013 OCR confirms a map and an "Area 51" caption, but I could not confirm the map sits on p. 57 specifically. A safer line is "In two thousand thirteen, the same history came back with fewer redactions. Behind the black boxes were a map. And a name."

**5. FIX (asset).** Same missing ciamap.jpg as line 4.

**6. OK.** B-roll frames at 158 s and 336 s show a U-2 in flight (DVIDS 908150). Label OK. "Most famous secret base" is framing, not a factual claim.

**7. OK.** **8. OK.** **9. OK.**

**10. OK.** Haines p. 73: atomic bomb summer 1949, hydrogen bomb August 1953. B-roll dv507037 at 75 s and 100 s shows a U-2 pilot in a pressure suit. Label OK. Location (Beale) and year (2017) are per rights.json and research; I did not independently confirm them.

**11. FIX.** "higher than Soviet fighters and missiles could reach" overstates. The history says the plane "had to fly above 70,000 feet to be safe from interception" (1998, p. ~16), and ch. 3 p. 93 says "beyond the reach" of Soviet "antiaircraft weapons and interceptors". A Soviet missile brought one down in 1960 (line 46), so the line contradicts the episode itself.
Replacement: "The answer they backed was a plane that could fly higher than Soviet fighters and anti-aircraft guns could reach. Around seventy thousand feet."
B-roll 478042 at 36 s: view from a U-2 cockpit over the wing at altitude. Label OK.

**12. OK.** Eisenhower approval in the first half of November 1954 (ch. 1, Killian meeting). CIA runs it with Air Force assistance; Lockheed builds. Timeline dates OK.

**13. OK.** "would be flying by August 1955, just eight months after he proposed to start construction" (ch. 1). "About eight months after construction began" is close enough for spoken narration.

**14. OK.**

**15. OK.**

**16. FIX (spelling, for captions, subtitles and description).** The official USAF biography spells the name "Osmond J. Ritland". The CIA history is inconsistent: "Osmund" on p. 56 and the photo caption, "Osmond" on p. 70. The audio is unaffected, but all written text should read "Osmond". Replacement: "…Bissell, Air Force Colonel Osmond Ritland, and Kelly Johnson flew over Nevada in a small Beechcraft, piloted by Lockheed's chief test pilot, Tony LeVier."
Checked and OK: 12 April, the four names, "small Beechcraft plane piloted by Lockheed's chief test pilot, Tony LeVier" (1998 p. 56, visible on screen). The map graphic is labelled approximate. OK.

**17. OK.** On-screen quote matches the 2013 text as quoted by the Las Vegas Sun and NPR, word for word: "…by a salt flat known as Groom Lake, near the northeast corner of the Atomic Energy Commission's (AEC) Nevada Proving Ground." The leading ellipsis covers the skipped words.

**18. FIX (minor overstatement).** The history says the plane "would probably have nosed over when the wheels sank into the loose soil". It does not say "flipped".
Replacement: "LeVier set the plane down on the lakebed instead. Good call. According to the history, the old strip had turned into ankle-deep dust. Had he landed on it, the plane would probably have nosed over, killing or injuring all of the key figures in the U two project."
The p56b image (1998) shows exactly this passage. OK.

**19. FIX.** It is not verifiable that Bissell himself asked the AEC. The 1998 text breaks off at "Bissell discovered that [redacted]", and the 2013 OCR for this sentence is garbled ("After … Commission to add the Groom … AEC Chairman Adm. …"). The press accounts disagree: the Las Vegas Sun says the group ("They agreed … and asked the AEC to add it to its real estate holdings in Nevada"), while Bangor Daily News paraphrases it as Bissell.
Replacement: "Bissell's group asked the Atomic Energy Commission to add the site to its land in Nevada. And according to the history, President Eisenhower approved the addition of this strip of wasteland, known by its map designation as Area fifty-one, to the Nevada Test Site."
On-screen doc: the text "President Eisenhower also approved the addition of this strip of wasteland, known by its map designation as Area 51, to the Nevada Test Site." matches word for word (Las Vegas Sun; Bangor Daily News, as two fragments). It is labelled "EXCERPT, RECREATED". OK.

**20. FIX (asset).** Same missing ciamap.jpg. The spoken line is OK.

**21. FIX.** "Later, the base picked up another unofficial name, Watertown Strip" misstates the source. The 2013 ch. 2 text ties the name to floods ("…when rainwater runoff … (at such times the base acquired yet another unofficial name, Watertown Strip)"), not to a later period.
Replacement: "To make the place sound more attractive to his workers, Kelly Johnson called it the Paradise Ranch. That was soon shortened to the Ranch. And when rain flooded the lakebed, the base picked up another unofficial name: Watertown Strip."
ALSO an asset problem: /home/claude/src/img/usgs1968.jpg is a Wikimedia error HTML page, so the label "USGS AERIAL PHOTO · GROOM LAKE, NEV., AUG. 28, 1968" cannot be checked. Obtain and verify the image, or cut it.

**22. OK.** "By July 1955 the base was ready, and Agency, Air Force, and Lockheed personnel began moving in" (2013 ch. 2). Monday-morning and Friday-evening flights; James Cunningham "dubbed this activity 'Bissell's Narrow-Gauge Airline'" (1998 p. 72, the p72a crop on screen). NOTE: the nickname went with the regular MATS C-54 service, which started 3 Oct 1955. Calling Cunningham "one project officer" is acceptable.

**23. FIX (graphic label).** The spoken line is supported. Foreign Policy quotes the history: "whose fallout was expected to contaminate the Groom Lake facility". The 1998 text has "In June 1957, the [redacted] entire facility had to be evacuated"; personnel went to Edwards AFB, and the CIA was back by 1959. The problem is the reused map graphic: it still carries the kicker "APRIL 1955 · The search for a test site", which does not describe this line.
Replacement graphic text: kicker "1957", title "A nuclear neighbor" (same map). Suggested spoken precision: replace "Later," with "In June nineteen fifty-seven,".

**24. OK.** MATS (USAF C-54) flight bound for the site crashed on 17 November 1955: "killing all 14 persons aboard … the greatest single loss of life in the entire U-2 program" (1998 p. 72, on screen).

**25. OK.** Second taxi trial on 1 August 1955, on the lakebed. "…as I had no intentions whatsoever of flying" (1998 p. 69). B-roll 995792 at 63 s shows a U-2 low over the runway, consistent with landing. 908150 at 255 s shows a U-2 on the runway. Labels OK.

**26. OK.** First planned flight 4 Aug 1955. "Official" first flight 8 Aug 1955 with Bissell present. "Kelly Johnson had met his eight-month deadline."

**27. OK.** "altitudes never before attained in sustained flight"; 8 September, 65,600 feet (p71 crop on screen).

**28. OK.**

**29. OK.** The section heading in the source is "U-2s, UFOs, AND OPERATION BLUE BOOK".

**30. OK.** Matches 1998 p. 72. NOTE: the graphic draws the military-jets band from 20,000 to 40,000 ft, while the source only says "below 40,000 feet". The graphic is labelled "ILLUSTRATION, NOT TO SCALE", so this is acceptable.

**31. FIX (b-roll).** At 145 s, dv478042 shows Earth from orbit (a deep black-space limb), not a view from a U-2. 103 s is a U-2 cockpit at altitude: OK. The label "MODERN U-2 AT HIGH ALTITUDE" is false for 145 s.
Replacement: dv478042 @28.0s, a U-2 cockpit at dusk with the sunlit horizon, which matches the narration. Keep the label.

**32. OK.** The quote matches 1998 p. 72 word for word, and the ellipsis is correct. NOTE: the source line says "2013 RELEASE". The same text is in the 1998 edition, and its page numbering (p. 72) was checked against 1998. Optionally label it "(1998 AND 2013 RELEASES)".

**33. OK.** Haines p. 73: "The early U-2s were silver (they were later painted black)". B-roll 375 s: U-2 in flight. OK.

**34. FIX (attribution).** "it adds" now reads as Haines, the subject of line 33. The sentence actually comes from the U-2 history (p. 72): "no one believed manned flight was possible above 60,000 feet, so no one expected to see an object so high in the sky."
Replacement: "And at the time, the history adds, no one believed manned flight was possible above sixty thousand feet. So no one expected to see an object that high in the sky."
B-roll 112 s shows a U-2 filmed from another aircraft at altitude. OK.

**35. OK.** Airline pilots and "ground-based observers also wrote letters to the Air Force unit at Wright Air Development Command … led to the Air Force's Operation BLUE BOOK. Based at Wright-Patterson, the operation collected all reports" (p. 73). This compression is acceptable.

**36. OK.** "regularly called on the Agency's Project Staff in Washington to check reported UFO sightings against U-2 flight logs … eliminate the majority … could not reveal to the letter writers the true cause" (p. 73).

**37. FIX (misleading framing).** The quote is word for word (p. 73). But this sentence was not newly declassified in 2013: it is fully legible in the 1998 release (p. 73, the same page shown in lines 35–36). The narration implies 2013 brought it out.
Replacement: "Then comes the line that made headlines in two thousand thirteen, even though it had been public since the nineteen ninety-eight version. U two and later OXCART flights accounted for more than one-half of all UFO reports, during the late nineteen-fifties and most of the nineteen-sixties."

**38. OK.** Haines p. 73: "According to later estimates from CIA officials who worked on the U-2 project and the OXCART (SR-71, or Blackbird) project, over half of all UFO reports…". The h07 crop shows exactly this.

**39. OK.** The on-screen quote matches Haines p. 73 word for word: "This led the Air Force to make misleading and deceptive statements to the public in order to allay public fears and to protect an extraordinarily sensitive national security project." Attributed to Haines.

**40. FIX (image mismatch).** The spoken quote is accurate ("While perhaps justified, this deception added fuel to the later conspiracy theories [and the coverup controversy of the 1970s]"). But the h07q crop does not show it: it shows the pull-quote "BLUE BOOK investigators were able to attribute many UFO sightings to U-2 flights" and the "fiery objects / BLUE BOOK" paragraph.
Replacement: re-crop hi-07.jpg, right column, from "This led the Air Force to" through "…coverup controversy of the 1970s."

**41. OK.** Haines p. 73 (checked on the scan): "fell to 5.9 percent in 1955 and to 4 percent in 1956." The stat graphic is correct and not presented as a quote.

**42. FIX (minor overstatement).** Haines says the estimate came from "CIA officials who worked on the U-2 project and the OXCART … project". It does not say they "ran the programs". The rest of the line is fair.
Replacement: "One caution. More than half is, according to Haines, a later estimate by C I A officials who worked on the programs. The released history doesn't list which reports, or show the math. And it doesn't claim to explain every sighting."
B-roll 218 s: U-2 in flight. OK.

**43. OK.**

**44. FIX (wording and b-roll).**
(a) The history (p. 104–105) says the 4 July flight (mission 2013) targeted Leningrad, and the 5 July flight (2014) went "more than 200 kilometers past Moscow". It was "the only U-2 photographs of Moscow". Bissell told Dulles on 5 July, not "later", that "they had overflown both Moscow and Leningrad". "The first two missions had passed over both" suggests each mission passed over both cities.
Replacement: "On July fourth, nineteen fifty-six, a U two made the first overflight of the Soviet Union, over Leningrad. The next day, a second flight passed Moscow. According to the history, when Allen Dulles asked, Bissell told him they had overflown both Moscow and Leningrad."
(b) B-roll dv478042 at 41 s is orbital footage (the Moon over Earth's limb, black space), not from a U-2. The label is false. Replacement: dv478042 @20.0s (U-2 cockpit over the curving horizon). Keep the label. 26 s (U-2 cockpit at dusk) is OK.

**45. OK, with a NOTE.** Soviets "did detect the aircraft and made several very unsuccessful attempts at interception" (p. 106). The photos showed MiG-15s and MiG-17s "in various pursuit and attack attitudes: climbing, flipping over, and falling toward Earth" and proved they "could not bring down a U-2 at operational altitude" (p. 108). The 10 July note called it a "twin-engine medium bomber of the United States Air Force" (p. 109), six days after 4 July. Optional tighter wording: "Mission photos showed Soviet MiGs below it, climbing, flipping over, and falling back toward Earth." B-roll 170 s: U-2. OK.

**46. OK.** Powers was "brought down by a near miss of a Soviet surface-to-air missile" from the "Sverdlovsk SA-2 battery" (ch. 4). July 1956 to May 1960 fits "almost four years". Timeline OK.

**47. OK.** Eisenhower's order ended overflights. OXCART was a "proposed successor" (ch. 4). B-roll 505 s: a U-2 on the ramp. OK.

**48. OK.**

**49. FIX (asset).** The figures check out against Robarge p. 11 ("Mach 3.2, or 2,150 miles per hour … mid-range altitude of 91,000 feet"). But /home/claude/src/img/a12.jpg does not exist, so the label "U.S. AIR FORCE PHOTO · CIA A-12 (OXCART) IN FLIGHT, 1960s" cannot be checked. Obtain and verify the image (Commons "A12-flying.jpg", DVIC DF-SC-82-10542), or substitute a verified one.

**50. OK.** "over 90 percent of the A-12's airframe out of a titanium alloy" (Robarge p. 12). SR-71 museum b-roll is labelled as such. OK.

**51. FIX (asset).** The spoken line is OK: Schalk's first lift-off on 25 April 1962 and the official flight on 30 April at "the Nevada facility" (Robarge pp. 16–17). But /home/claude/src/img/landsat.jpg does not exist. Obtain and verify the image, or cut it.

**52. OK, with NOTEs.** The White House statement of 29 Feb 1964 said "The A-11 aircraft now at Edwards Air Force Base are undergoing extensive tests". The aircraft surfaced was the YF-12A interceptor (Robarge p. 27). NOTE 1: Robarge says none were actually at Edwards, so "two had to be rushed from the test site". Optional: "…a plane called the A eleven, which it said was testing at Edwards Air Force Base." NOTE 2: Robarge's figure is "the 15 OXCART aircraft CIA and the Air Force had ordered" (p. 22). "Fifteen OXCART aircraft" is closer to the source than "fifteen of them". Image dvimg749221 shows YF-12A 60935 and a second Blackbird marked NASA. Label OK.

**53. OK.** BLACK SHIELD; first mission 31 May 1967 over North Vietnam, from Kadena (Okinawa) (Robarge pp. 30, 34). B-roll 402699 at 69 s and 95 s is archival Blackbird flight film, honestly labelled SR-71.

**54. FIX (b-roll).** The spoken line is OK: Pueblo seized 23 Jan 1968; an A-12 photographed it on 26 Jan (Robarge pp. 37–38). But dv402699 at 105 s lands on a museum curator interview (a man in a suit), not "SR-71 BLACKBIRD IN FLIGHT". Replacement: dv402699 @114.0s (Blackbird in flight over a coastline). Keep the label.

**55. OK.** The last operational A-12 mission was 6 May 1968 (Robarge p. 37), and the SR-71 was the Air Force's "OXCART reconnaissance variant" (p. 41). "Two-seat" is not in Robarge but is standard (pilot plus reconnaissance systems officer). Museum b-roll labelled. OK.

**56. OK, with a NOTE.** The U-2 is still in service as of 2026. It flies daily ISR missions (The Aviationist, Mar 18, 2026), and Migflug (June 15, 2026, updated Oct 2, 2026) says it "remains in service in 2026", with the first retirement in Dec 2025 and Congress capping retirements. Recheck at publish date. Optional: "…is still flying today, though the Air Force has begun retiring it." B-roll 146 s (Blackbird over clouds) and 908150 at 440 s (U-2 on runway): OK.

**57. OK.**

**58. FIX (asset).** Same missing ciamap.jpg. The spoken line is OK: the site was picked from the air on 12 April 1955, the name comes from the map designation, and it was a CIA test site for the U-2.

**59. OK.**

**60. OK.** EBB 434: written 1992 ("published in classified channels in 1992"); "heavily redacted version" published 1998; "2005 Freedom of Information Act request"; posted August 15, 2013.

**61. FIX (asset).** The spoken line is OK (the history covers 1954–1974), and it labels theories as theories. But landsat.jpg is missing (see line 51).

**62. FIX (misleading).** 1955 to 2013 is 58 years, so the arithmetic is fine. But the name itself was not secret all that time: the 2013 history says "The outlines of Area 51 are shown on current unclassified maps as a small rectangular area adjoining the northeast corner of the much larger Nevada Test Site." What took 58 years was the CIA confirming the story.
Replacement: "Every secret has a release date. For the C I A to put that name on the record, it took fifty-eight years."

**63. NOTE.** "We read every one" is a channel promise, not a documentary claim. Keep it only if true.

**64. OK.** Not a factual claim for this episode.

Rule checks across the script: the words "alien" and "debunked" do not appear. Witness and person statements are attributed (LeVier, Bissell, Haines). "Conspiracy theories" appears only inside Haines's attributed words, and line 61 labels theories as theories. The one recreated document (line 19) is labelled RECREATED.

FIXES: 21

---
## Applied by the producer (2026-10-31)
All 21 FIXes applied before the final render:
- Commons images (CIA map, USGS 1968, Landsat, A-12 photo) could not be downloaded (HTTP 429) — all removed. L4 now shows the redacted p. 57 with "Behind the black boxes were a map. And a name."; L5 is a text card ("AREA 51 · the name under the black boxes", source NSArchive EBB 434); L20/L58 use the map graphic; L21 uses the verbatim "Paradise Ranch" quote card; L49 uses the NASA YF-12 photo (labelled as YF-12, based on the A-12); L51/L61 use labelled DVIDS footage.
- L11 "fighters and anti-aircraft guns"; L16 "Osmond"; L18 "would probably have nosed over"; L19 "Bissell's group asked"; L21 Watertown tied to flooding; L23 "In June 1957" + map retitled "JUNE 1957 · A nuclear neighbor"; L34 "the history adds"; L37 "even though it had been public since the 1998 version"; L40 crop now shows "While perhaps justified…"; L42 "according to Haines, a later estimate by CIA officials who worked on the programs"; L44 Leningrad (July 4) / Moscow (July 5) / Bissell told Dulles; L62 "For the CIA to put that name on the record, it took fifty-eight years."
- Footage: every clip from DVIDS 478042, 402699 and 507037 removed (24→30 pull-down judder found with mpdecimate). Replaced with native-frame-rate DVIDS 1017843 (U-2 at altitude, 2026), 940701 (U-2 training flight, 2024), 640384 (SR-71 display, Beale, 2017), 396020, 995792, 908150. Each replacement checked on contact sheets; the one shot that landed on an interview was replaced.
