# FILE 011: independent fact-check

Checked 2026-11-08 against the local sources in /home/claude/src/dl and /home/claude/src/pg, the doc crops in /home/claude/src/img/doc, the DVIDS API descriptions (all 11 IDs), and the live pages from NARA, NOAA, Burlison, EarthSky and CBS. I also pulled frames from every b-roll clip at the times the script uses.

Line numbers are 1-based indexes into LINES, the same numbering META shorts use.

**Verdicts**
- **OK**: verified.
- **FIX**: must change. The replacement wording and the source are given.
- **NOTE**: acceptable as written, or an optional improvement.

## Systemic finding: the Tremonton clip (dv1023402s) goes black

I measured luma in both files with ffmpeg signalstats:
- **Original DVIDS 1023402:** the NARA slate "341.PBB.345 / Source: 16mm RSK (P Copy)" runs from about 3 to 5 s, not in the first second as research.md says. The "45" leader and a white flash run from about 6 to 8 s. The sky footage with points of light runs from about 9 to 24.5 s. **From about 25 s to 54.5 s the print is essentially black** (YAVG ≈ 23, YMAX ≈ 35–60). The sewing footage starts at 55 s.
- **Slowed file dv1023402s (64.4 s long):**
  - 0–2.5 s: NARA slate.
  - About 3–6 s: leader "45" and a white flash.
  - **About 7.5–26.9 s: usable sky footage.** The points of light are clearest at about 19–23 s.
  - **About 27–64.4 s: near-black.**

That affects lines 6, 19, 21, 24, 59, 68 and 70 below. Only lines 6 (partly) and 75 sit inside the usable stretch.

## Line-by-line

| # | Verdict | Finding / replacement (source) |
|---|---|---|
| 1 | OK | Haines p. 68: "On 19 and 20 July, radar scopes at Washington National Airport and Andrews Air Force Base tracked mysterious blips." The haines_dc crop shows this text. dv503512 80.6 shows the radar room and scope at RAF Lakenheath, so the label is accurate. |
| 2 | NOTE | 19/20 to 27 July is about one week, so OK. "They found nothing" is the CIA history's claim (Haines p. 68), carried over from the attribution in line 1. Acceptable, but other accounts dispute it. If wanted: "According to that history, they found nothing." Footage: F-22 cockpit over D.C. 2026 matches the label. dv431279 13.2 shows the RAPCON scope, but from 18.05 s it cuts to a talking-head interview, so keep this shot short. |
| 3 | OK | Haines dates the return to 27 July and the press conference was 29 July (CIA memo of 14 Aug 1952), so "two days after that" holds. The chart crop shows the label "AF PRESS CONFERENCE ON UNIDENTIFIED FLYING OBJECTS". |
| 4 | OK | The chart (Status Report 8, Appendix I) has the three labels "PUBLICIZED INCIDENT AT WASHINGTON D.C.", "HIGHLY PUBLICIZED INCIDENT AT WASHINGTON D.C." and "AF PRESS CONFERENCE ON UNIDENTIFIED FLYING OBJECTS", all at the late-July spike. |
| 5 | OK | Chadwell memo (Sept 24), para 1: "To determine: (a) whether or not there are national security implications in the problem of 'unidentified flying objects'". sep24_head shows "SEP 24 1952 … SUBJECT: Flying Saucers". |
| 6 | FIX (timing) / NOTE | Text OK. "Prevented a conclusive resolution" in the DVIDS PR159 description supports "still has no conclusive answer". "Pentagon" is fair: CBS writes "The Pentagon on Friday released its sixth batch", and EarthSky uses Pentagon and Department of War interchangeably. **Footage:** the clip starts at 22.0, and the film goes black at about 26.9, so the end of the line plays over black. Start at **19.0**. |
| 7–8 | OK | No factual content. |
| 9 | OK | March to July is four months. |
| 10 | OK | DVIDS 1023407 describes "a March 1952 presentation by Captain Edward J. Ruppelt, outlining the U.S. Air Force's reorganized investigation into unidentified flying objects". The DVIDS date is 1952-03-26, location Boston. NOTE on footage: dv934516a from 4.0 to about 7 s shows a modern F-15 in flight, not the museum. Either start at **7.0** (aerial view of the museum) or accept it. |
| 11 | FIX (minor, doc card) | Narration OK. Burlison press release, May 8, 2026: "an identified reel-to-reel recording", "identified as "AF-ATIC-FILM, 03/52" and labeled "flying saucer talk"", "lists former Air Force officer Edward J. Ruppelt as the briefer". The release does not say "AF-ATIC-FILM, 03/52" is label text; it says the recording is *identified as* that. Change the card title from `"The label"` to `"How it is identified"`, and change the source line to `SOURCE: OFFICE OF REP. ERIC BURLISON, PRESS RELEASE, MAY 8, 2026 · TEXT AS QUOTED, RECREATED`. |
| 12 | OK | DVIDS 1023407 was published 2026-09-18. The narration does not claim this is the same item as the Burlison tape. Good. |
| 13 | OK | DVIDS 1023407: "out of approximately 800 historical cases reviewed by the Air Force, approximately 20% remained unexplained after technical analysis." The stat card is OK. |
| 14 | FIX | **(a) Wording.** The description says Ruppelt "highlights geographic report concentrations around sensitive national security and nuclear weapons installations (including Los Alamos, Albuquerque, and Oak Ridge…)". "Many [of those reports] were concentrated" adds a quantity the source does not give, and it ties the clusters to the unexplained subset. Replace the second sentence with: **"He also pointed to clusters of reports around nuclear weapons sites, like Los Alamos and Oak Ridge."** (DVIDS 1023407.) **(b) Label.** dv934516b from 10.0 shows an F-86 and a MiG-15, then from about 18 s a propeller-driven F-82 Twin Mustang. Change MUSJ to `"B-ROLL · KOREAN WAR-ERA AIRCRAFT ON DISPLAY, NATIONAL MUSEUM OF THE USAF, 2024"`. |
| 15 | FIX | **(a) Wording.** The source says "radar detections indicating unconfirmed air speeds between 1,000 and 3,500 miles per hour". "Never confirmed" is stronger than "unconfirmed". Replace the second sentence with: **"Speeds that, the description notes, were unconfirmed."** (DVIDS 1023407.) **(b) Footage.** dv503512 from 83.0 has cuts at 85.19 and 86.95. From 86.95 it is a talking-head interview in front of the control tower, which does not match the "RADAR APPROACH CONTROL" label, and this line runs about 8 s. Start at **78.3**, where the 78.24–85.2 stretch is the radar room and scope only. |
| 16 | FIX | **(a) Attribution.** NARA: "Air Force Director of Intelligence Maj. Gen. Charles P. Cabell ordered Project Blue Book in March 1952." Haines p. 68 says Cabell "ordered a new UFO project in 1952". Line 36 then calls Samford "the Air Force's Director of Intelligence" four months later. Other histories put Samford in that post from 1951 and date Cabell's order to the 1951 reorganisation. Keep the claim, but attribute it: **"That same month, according to the National Archives, the Air Force's Director of Intelligence, Major General Charles Cabell, ordered a new project."** The other two sentences are OK (Haines p. 68: "increased Cold War tensions, the Korean war"). **(b) Footage.** dv934516b from 18.0 cuts at about 27.5 s to a yellow bomb-bay exhibit with a child, which is not Korean War-era aircraft. This line runs about 10 s. Start at **10.0** (line 14 then needs another in-point), or keep the shot under 9 s. |
| 17 | OK | Rhetorical. The status report supports "buried": over 440 in July. |
| 18 | FIX | "The first big case of that summer" is an unsupported superlative; the Robertson report only says it "was considered significant". Replace with: **"One of that summer's most closely studied cases came on July second."** (Robertson panel meeting report, PDF p. 13, printed p. 11.) |
| 19 | FIX | **(a) Witness attribution.** DVIDS PR159: Newhouse "reported observing and filming a group of bright airborne objects". Replace the first sentence with: **"Near Tremonton, Utah, a Navy Chief Warrant Officer named Delbert C Newhouse reported seeing a group of bright objects in the sky."** "Handheld camera, in color" is OK: a handheld Bell & Howell with Kodachrome. **(b) Footage.** At 4.0 the slowed clip shows the handwritten "45" leader and a white flash; sky footage starts at about 7.5. Start at **8.0**. |
| 20 | OK | Robertson PDF p. 13: "Kodachrome motion picture films (about 1600 frames)". The rb_trem crop shows this. DVIDS: "shortly thereafter submitted the footage to the U.S. Air Force." |
| 21 | FIX (footage) | Text OK. **At 26.0 the clip goes black at about 26.9**, so viewers would hear "the objects are the small white points of light" over a black screen. Start at **19.0**; points of light are visible from about 19 to 23 s. |
| 22 | OK | Robertson p. 12 (rb_pil): "(at Air Force request) approximately 1000 man-hours of professional and sub-professional time in the preparation of graph plots of individual frames of the film, showing apparent and relative motion of objects and variation in their light intensity." The page image reads 1000, confirmed. |
| 23 | OK | The quote is verbatim with correct ellipses: "were not birds, balloons or aircraft, were "not reflections because there was no blinking while passing through 60° of arc" and were, therefore, "self-luminous"." The narration frames it as the lab's opinion. |
| 24 | FIX (footage) | Text OK. July 2, 1952 to Jan 14–17, 1953 is about 6.5 months, and the report is stamped SECRET. **The clip at 44.0 is black.** Use **12.0–17.0**, or another point inside 7.5–26.5. |
| 25 | OK | 2 to 19 July is 17 days, about 2.4 weeks. |
| 26 | OK | Haines p. 68. Footage: RAPCON (NJ) at 102.5 and the Lakenheath room at 78.4; both labels are accurate. |
| 27 | NOTE | Haines p. 68 gives "On 27 July". EarthSky dates the second wave to July 26; it ran overnight 26–27. The tag "JULY 27, 1952" matches the cited source. "JULY 26-27, 1952" would be more precise if you want it; the timeline in line 72 would need the same change. The shot ends before the 86.95 cut. |
| 28 | OK | Attributed to Haines. dv503512 38.6 is a night F-15 afterburner takeoff (cut 40.21), so the label is accurate if the shot stays under 3.6 s. |
| 29 | OK | Haines: "caused headlines across the country." |
| 30 | OK | Status Report 8 (st_peak): "reached a peak on 28 Jul 52 when 43 reports were received (see Appendix I)." |
| 31 | OK | st_status: "For the month of Jul 52, the total was over 440 reports." The stat card is OK. |
| 32 | OK | st_status: "During the period 1 Jun 52 to 31 Oct 52 … 886 reports … 149 more reports than had been received during the previous five-year period". |
| 33 | FIX (minor) | Source (st_staff): "In Jul 52 … the number of personnel was increased to a total of four officers, two airmen, and two secretaries." "By July" implies the staff was already at that level. Replace with: **"In July, the staff was increased to four officers, two airmen and two secretaries. \| For forty-five days, a weather officer was brought in to help."** |
| 34 | OK | Haines: "The White House wanted to know what was happening". |
| 35 | OK | 14 Aug 1952 memo, verbatim: "Requests for information have poured in on the Air Force, including an official query from the White House." The crop shows it. |
| 36 | OK / NOTE | The memo gives July 29 and "General Samford". Haines p. 71 titles him "Director of Air Force Intelligence". See the note on line 16. b-roll: the PENN label is not confirmed by DVIDS (see LABELS below). |
| 37 | OK | The quote is verbatim from the memo. Role: "as summarized by the CIA" is correct. |
| 38 | OK | Memo: "recent Washington sightings were possibly due to "temperature inversions"". The crop at focus 0.6 shows it. |
| 39 | OK | NOAA JetStream: "air temperature increasing with height instead of the typical decreasing with height"; "Superrefraction is where the radar beam is bent greater than normal back toward the Earth"; "more likely when a strong low-level inversion is in place"; "False echoes are known as anomalous propagation". Weather-balloon frames at 21 and 41 match the label. NOTE: DVIDS says "U.S. Marines with 1st Intelligence Battalion … Camp Pendleton". "Weather team" is fair; `"…BY U.S. MARINES, CAMP PENDLETON, CALIF., 2022"` would be more exact. |
| 40 | OK | Memo, verbatim: "He emphatically stated that the unexplained sightings could not have resulted from any experiments or tests conducted by the United States." The crop at 0.8 shows it. |
| 41 | FIX (image) | Text OK (Haines p. 68). **The haines_dc crop ends at "…the radar blips might"**, so the CAA sentence the narrator is reading is not on screen. Re-crop haines_dc from haines.pdf p. 68 so it runs through "…Later, a Civil Aeronautics Administration investigation confirmed that such radar blips were quite common and were caused by temperature inversions." Alternatively, add a second crop haines_caa for this line. |
| 42 | FIX | "Case closed" overstates the record. Samford said "possibly", and the same memo says "instrumentation would be emphasized henceforth in the Air Force study". Replace with: **"That was the public answer. \| Inside the C I A, it was just getting started."** (CIA memo, 14 Aug 1952.) |
| 43 | OK | Haines p. 68: "monitored UFO reports for at least three years". |
| 44 | OK | Haines p. 68. |
| 45 | OK / NOTE | Haines pp. 68–69. Tauss was "acting chief of OSI's Weapons and Equipment Division". The full phrase is "in view of their probable alarmist tendencies" *to accept such interest as confirming the existence of UFOs*. The narration truncates it, but the sense holds. |
| 46 | OK | Haines p. 69: "The Air Force claimed that 90 percent … The other 10 percent were characterized as "a number of incredible reports from credible observers."" The quote is verbatim. |
| 47 | OK | Haines p. 69, verbatim: "there was only one chance in 10,000 that the phenomenon posed a threat to the security of the country, but even that chance could not be taken." The ellipsis is correct. |
| 48 | OK | The diary crop shows "Monday, 18 August 1952 … At the Deputies' meeting, announced that we would have a briefing on flying saucers at 11 A.M. Wednesday in the Director's conference room … this briefing would take 20 minutes." |
| 49 | OK | sep24_head and the signature block: "H. Marshall Chadwell, Assistant Director, Scientific Intelligence". |
| 50 | OK | Para 3 (sep24_july): "approximately 1500 official reports … Air Force carries 20 percent as unexplained … January through July 1952 it carries 28 percent unexplained." The memo says ATIC, which is part of the Air Force, so OK. |
| 51 | OK | Para 6 gives "two elements of danger" and "a. Psychological". The "incredible" passage is verbatim. |
| 52 | OK | Para 6a, verbatim in substance. Para 4: the CIA "checked the Soviet press". |
| 53 | OK | Para 6b is headed "Air Vulnerability". The quote "we cannot, on an instant basis, distinguish hardware from phantom" is verbatim. |
| 54 | OK | Paraphrase of 6b: "as tension mounts we will run … the even greater danger of falsely identifying the real as phantom." |
| 55 | OK | Haines p. 70 (December 1952 briefing). F-22 b-roll is labelled. |
| 56 | OK | — |
| 57 | OK | Haines p. 71: "met from 14 to 17 January 1953". Robertson is described as "a noted physicist from the California Institute of Technology". rp_head shows "17 January 1953". |
| 58 | OK | Haines p. 71: "after spending 12 hours studying the phenomena, declared that reasonable explanations could be suggested for most, if not all, sightings." Capitol b-roll is labelled. |
| 59 | FIX (footage) | Text OK. Robertson PDF pp. 3–4 list "Tremonton, Utah (2 July 1952)" and "Washington, D.C. area (19 July 1952)". **The clip at 34.0 is black.** Use a point between **9.0 and 26.0**. |
| 60 | OK | rb_gulls: "impressed by the evident enthusiasm, industry and extent of effort of the P.I.L. team, they could not accept the conclusions reached." The "plots … were displayed" sentence is on rb_pil, bottom. |
| 61 | OK | "A semi-spherical object can readily produce a reflection of sunlight without "blinking"". The crop at 0.3 shows it. |
| 62 | OK | "the apparent motions, sizes and brightnesses of the objects were considered strongly to suggest birds, particularly after the Panel viewed a short film showing high reflectivity of seagulls in bright sunlight." |
| 63 | FIX (minor, image) | Text verbatim, OK. The rp_strip focus of [0.5, 0.2] frames para 1 ("evaluate any possible threat"). The conclusion sentence sits at about y = 0.48. Use `focus=[0.5, 0.48]`. |
| 64 | OK | The quote matches the rp_strip page verbatim, including the capitals "Unidentified Flying Objects". |
| 65 | FIX (image) | Text OK (Report of the Scientific Panel, 17 Jan 1953). **The rp_strip crop ends at "…unfortunately acquired."** The "integrated program designed to reassure the public of the total lack of evidence of inimical forces" sentence is not in the crop. Extend the rp_strip crop down, or add a crop rp_reassure from 0005516125.pdf. |
| 66 | OK | March 1952 to Dec 17, 1969 is 17 years 9 months (NARA). |
| 67 | FIX (stat card) | Narration OK. USAF Fact Sheet 95-03: "From 1947 to 1969, the Air Force investigated … Of a total of 12,618 sightings reported to Project Blue Book, 701 remained "unidentified."" The 12,618 total covers 1947–1969, not 1952–1969. Change the stat key to **`"PROJECT BLUE BOOK · 1947-1969"`**, or `"USAF UFO INVESTIGATIONS · 1947-1969"`. |
| 68 | FIX | "Published the Tremonton film again" implies an earlier Pentagon release that no source supports, and it reads oddly after line 6. Replace with: **"On September eighteenth, twenty twenty-six, the Pentagon published a digitized print of the Tremonton film, in its sixth batch of U A P files."** (DVIDS 1023402: "a digitization of a 16mm print"; CBS: "sixth batch"; EarthSky and CBS give Sept 18, 2026.) **Footage:** 50.0 is black, so use **20.0**. |
| 69 | OK | The quote is verbatim from DVIDS PR159. |
| 70 | FIX | **(a) Wording.** The source says "unrelated footage appearing to show a demonstration of sewing equipment". Replace the second sentence with: **"From the fifty-five second mark, the surviving print switches to unrelated footage that appears to show a demonstration of sewing equipment."** The third sentence is OK: "the available record does not establish how or when the materials came to be combined". **(b) Footage.** At 56.0 the clip is black, and a line of about 13 s would run past the end of the 64.4 s file. Use a point inside **7.5–26.5**, or show the actual sewing segment from the unslowed original (55 s onward) with a label such as `"ACTUAL FILM · DOW-UAP-PR159 · UNRELATED SEWING FOOTAGE FROM 0:55"`. |
| 71 | FIX (footage) / OK (text) | Text OK. Both items were published 2026-09-18 (DVIDS). EarthSky: "Social media posts claimed the talk included the famous 1952 Washington disk sightings". **Footage:** dv934516b from 24.0 cuts at about 27.5 s to the yellow bomb-bay interior, which the MUSJ label does not describe. Start at **19.0**, or use the generic label `"B-ROLL · NATIONAL MUSEUM OF THE U.S. AIR FORCE, 2024"`. |
| 72 | OK / NOTE | Ruppelt spoke on March 26, 1952 (DVIDS date). The timeline is correct per Haines and the memo. See line 27 on July 27 vs. 26–27. |
| 73 | FIX | "The Air Force's answer was the weather" drops the hedge in both sources: the memo has "possibly due to", and Haines has "might be the result of". Replace the second sentence with: **"The Air Force's answer was, possibly, the weather: temperature inversions."** The third sentence is OK: Haines repeats it and adds the CAA finding. NOTE: dv431279 from 15.0 cuts to the airman interview at 18.05, so keep it under 3 s or use 102.8. |
| 74 | OK | A fair summary: the CIA study group, then the panel's "strip … the aura of mystery". |
| 75 | FIX | "Every secret has a release date. For the film from Tremonton, it came seventy-four years after it was shot" implies the film stayed secret until 2026. NARA says the Blue Book records were "made available for public research" in 1976. The panel discussed the film in 1953, and EarthSky calls it "famous" and long debated. No source supports 2026 as its first release. Replace with: **"Every secret has a release date. \| For this print of the Tremonton film, the Pentagon's release came seventy-four years after it was shot."** Or, more neutral: **"Some files take decades to surface. \| This print of the Tremonton film was published seventy-four years after it was shot."** 1952 to 2026 = 74 years, OK. Footage at 12.0 is OK. |
| 76 | OK | F-22 at 40.5 is labelled. |
| 77 | NOTE | Teaser for the next episode; check it in that episode. Commonly dated 1972–1995 (about 23 years); "for more than two decades" is OK. |

## Labels (lab=)

| Label | Verdict | Finding |
|---|---|---|
| TREM | OK | DVIDS 1023402: Tremonton, Utah, July 2, 1952; "SLOWED TO 80%" is disclosed. See the systemic finding for in-points. |
| RADAR15 | OK | DVIDS 431279, "RAPCON", Joint Base McGuire-Dix-Lakehurst (New Jersey), 2015-10-27. Air Force personnel are in the frame. |
| RADAR16 | OK | DVIDS 503512, 48th Fighter Wing (RAF Lakenheath), Suffolk UK, published 2016-12-29. The DVIDS date field is a 1970 placeholder, so 2016 is the publication year. Avoid frames after 86.95 (interview at the tower). |
| F15 | OK | 503512 at 38.6–40.2 is an F-15 night takeoff at Lakenheath. |
| F22 | OK | DVIDS 1026930: F-22 demonstration over Washington, D.C., July 3, 2026, with a cockpit camera. |
| WH / CAP / TREAS | NOTE | DVIDS 346124 / 346026 / 346120 are U.S. Department of State b-roll; the DVIDS date field is 2012-08-02. The foliage in 346119 is autumnal, so "2012" may be an ingest date. A safer form is `"… · U.S. DEPARTMENT OF STATE VIA DVIDS"` with no year. |
| PENN | FIX (minor) | DVIDS 346119 is titled only "B-Roll Footage Around Washington, D.C. Capitol 2". The frames show a tree-lined avenue toward the Capitol dome, which is plausibly Pennsylvania Ave NW, but the source does not name the street. Use `"B-ROLL · AVENUE LEADING TO THE U.S. CAPITOL, WASHINGTON, D.C."`. |
| MUS | NOTE | DVIDS 934516: National Museum of the USAF at Wright-Patterson AFB near Dayton, Ohio, 2024-06-03, so the label is correct. Frames 4.0 to about 7 show a modern F-15 in flight and 12–17 show the museum crest overlay; see line 10. |
| MUSJ | FIX | Covered by lines 14, 16 and 71: an F-82 propeller aircraft and the bomb-bay interior are not "jets". |
| BAL | OK / NOTE | See line 39. |
| TOWER16 | NOTE | Defined but not used. |

## Shorts and post titles

| Item | Verdict | Finding / replacement |
|---|---|---|
| s1 hook "THE NAVY SAID [NOT BIRDS]" | FIX | It was the representatives of the USN Photo Interpretation Laboratory, not "the Navy". Use **`A NAVY LAB SAID<br>[NOT BIRDS]`**. The cut (lines 18–24) gives only the lab's view; line 24 says it was "argued over", but the panel's bird conclusion is not in the cut. Recommend an end card: *"Jan. 1953: a CIA scientific panel rejected this; it said the objects strongly suggested birds."* (Robertson meeting report, p. 12.) |
| s2 hook | OK | Haines p. 68. |
| s3 hook "THE AIR FORCE SAID [IT WAS WEATHER]" | FIX | Samford said "possibly due to temperature inversions" (CIA memo, 14 Aug 1952), and Haines says the explanation was that the blips "might be the result of". Use **`THE AIR FORCE SAID<br>[MAYBE THE WEATHER]`**. |
| s4 hook | OK | Verbatim fragment. |
| y1 lines [21, 23] + hook | FIX | Hook OK: it is attributed. The cut ends on "self-luminous" with no counterpoint, and line 21's footage at 26.0 is black. Extend to **[21, 24]** at minimum and add the panel end card above. Also re-time line 21 to 19.0. |
| y2 | OK | — |
| y3 [53, 56] | OK | — |
| TikTok "In 1952 a Navy lab said a UFO film showed no birds" | FIX | The lab said the objects "were not birds", not that the film showed no birds, and its analysis was presented in January 1953. Use **"A Navy lab said the objects in this 1952 film were 'not birds'"**. |
| TikTok "Radar tracked blips over Washington in July 1952" | OK | Haines p. 68. |
| TikTok "The Air Force blamed the 1952 Washington blips on weather" | FIX | Use **"The Air Force said the 1952 Washington blips were possibly weather"**. |
| TikTok "A 1952 CIA memo: we can't tell hardware from phantom" | FIX | Dropping "on an instant basis" changes the meaning. Use **"A 1952 CIA memo: we can't instantly tell 'hardware from phantom'"**. |
| YT "A Navy Lab Called This 1952 Film 'Self-Luminous'" | FIX | The lab called the *objects* self-luminous. Use **"A Navy Lab Called the Objects in This 1952 Film 'Self-Luminous'"**. |
| YT "Radar Saw Blips Over Washington in July 1952" | OK | — |
| YT "1952 CIA Memo: We Can't Tell 'Hardware From Phantom'" | FIX | Use **"1952 CIA Memo: We Can't Instantly Tell 'Hardware From Phantom'"**. |
| Long title "The 1952 Washington UFOs: What Did Radar See?" | OK | — |
| META title "Saucers Over the Capitol" | NOTE | The sources describe radar blips at National Airport and Andrews and an "incident at Washington"; none places them over the Capitol building. Consider "Saucers Over the Capital". "Flying saucers" is the documents' own term, so it is fine. |
| META credit | OK / NOTE | Accurate. Optionally add "USAF Fact Sheet 95-03; NOAA". |
| DISPLAY map | OK | All number and name mappings match the narration. Order is safe: "C I A's" before "C I A", and "July nineteenth and twentieth" before "July nineteenth". |
| S_RPF "P. 12" | OK | The quote continues onto printed p. 12; rb_trem is printed p. 11. |

## Other checks (all OK)

- Nothing implies an extraterrestrial explanation.
- "Debunked" and "alien" are never used.
- The Burlison line does not claim the tape is the same item as PR160.
- "Pentagon" and "Department of War" phrasing is consistent with CBS and EarthSky.
- Every quote card was verified verbatim against the page images.
- "Almost eighteen years", "a week later", "two days after that", "two and a half weeks", "four months earlier" and "six months later" are all correct.

## Summary

**FIX items: 32.**
- **24 script lines:** 6, 11, 14, 15, 16, 18, 19, 21, 24, 33, 41, 42, 59, 63, 65, 67, 68, 70, 71, 73, 75, plus label fixes PENN, MUSJ and the line 15 footage. The MUSJ fix is handled inside lines 14, 16 and 71.
- **8 shorts and titles:** s1, s3, y1, TikTok 1, TikTok 3, TikTok 4, YT 1, YT 3.

The most important fixes are:
1. The black Tremonton footage (lines 21, 24, 59, 68, 70).
2. Line 75's implication that the film was secret until 2026.
3. Line 67's 1952–1969 stat key.
4. The hedge dropped in line 73, the s3 hook and TikTok 3.
5. The y1 Short presenting "self-luminous" with no counterpoint.
6. The witness attribution in line 19.

## Applied (2026-11-08, by the production run)
All 32 FIX items applied before the final render: wording changes on L11 (card title/source), L14, L15, L16, L18, L19, L33, L42, L68, L70, L73, L75; footage start points for every Tremonton shot moved into the usable sky window; museum/radar shots re-timed to avoid the bomb-bay exhibit and talking heads; MUSJ/PENN labels corrected, years dropped from the 2012 D.C. labels; haines_caa crop added for L41; rp_strip crop extended for L65; L63 focus; L67 stat key 1947-1969; s1/s3 hooks; y1 lines → [22, 24]; post titles per this report. Title card changed to "Saucers Over the Capital".
Later production change (QC): the Tremonton clip is now retimed to 30 fps at original speed with frame blending (the 80 % slow-down produced duplicated frames); L21 no longer says "we have slowed it", label reads "RETIMED TO 30 FPS". L73 now uses two radar shots (no talking head).
