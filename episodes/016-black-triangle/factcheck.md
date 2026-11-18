# FILE 016 — The Black Triangle — independent fact-check

**Date:** 2026-11-18
**Checker:** independent (did not write the script)
**Scope:** all 96 LINES (1-indexed) of `episode.py`, on-screen labels, graphics, tags, META title, shorts/yshorts hooks, and all of `packaging.md`.

## Sources used

Primary (Department of War PURSUE Release 07, Oct. 23, 2026, unmodified mirror archive.org/details/pursue-uap-documents-2026, folder Release_07):
- DOW-UAP-D176 AARO Memorandum for Record (3 pp., text layer)
- FBI-UAP-D043 FD-302 + co-signed statement (11 pp.: 2 text pages, read visually from `/home/claude/src/pg/FBI-UAP-D043_p1-01.jpg`, `_p2-02.jpg`, plus 9 image pages = fbi1–fbi9.jpg, inspected visually)
- DOW-UAP-D155 Saudi Arabia 1957 (p.1 read visually), D164 Indiana 1954, D179 Catalina 1952 (p.2 read visually), D177 Catalina 1955, D163 Sweden 1953, D160 Morocco 1953, D161/D162 Alaska 1953
- EOP-UAP-D002 memo for Dr. Welsh, May 29, 1963; USG-UAP-D002 space-fragment correspondence (djvu text)
- DOW-UAP-D174 BAASS Utah Ranch Investigation Report (PDF pp. 1, 5, 8, 9, 37, 38; pp. 37–38 read visually)
- Release 07 file list (archive.org metadata API): 28 PDFs

Secondary:
- EarthSky, "pentagon-uap-files-ufos-batch-7" — Oct. 23, 2026 date; 28 files; Parnell: "the Department will release additional files on a rolling basis."
- Sinclair / KMPH, "Federal agents reported seeing silent black triangle in latest UFO file release" — Oct. 23, 2026; files labeled "unresolved" because investigators lacked enough information for a definitive identification, "not because the phenomena have been linked to extraterrestrial activity."
- AFGSC, "Year of the B-52: B-52s make historic nonstop around-the-world flights" — five B-52Bs left Castle AFB two days after the Jan. 14, 1957 briefing; three "completed the 24,325 mile flight in 45 hours and 19 minutes," landing at March AFB.
- BAASS / DIA AAWSAP contract: The Debrief ("Defense Intelligence Agency paid $22 million…"), Black Vault DIA FOIA material.
- Edward C. Welsh (NASC executive secretary 1961–69) and Arnold Frutkin (NASA director of international programs): Wikipedia, NASA History, JFK Library oral history. EOP letterhead in USG-UAP-D002 confirms NASC sat in the Executive Office of the President.

## Notes before the table

- **Another difference the script leaves out:** the FBI statement gives the time as "approximately **1923** hours" (the scan clearly reads 1923). The AARO memo says **2023L**. Line 9 credits 8:23 pm to the memo, so it is not wrong. But it is a second difference between the two accounts, and a viewer could catch it. Consider adding it to the Chapter III list.
- **FBI images:** the PDF has 11 pages, and pages 3–11 are the nine images, with no captions or text. All nine use **the exact same background photo**: the same dusk ridge landscape, the same light disc, the same foreground. The only change is a flat black shape pasted into the sky. In images 1–3 it is a thin dark sliver at about ridge height, in 4–5 a triangle above the ridge, and in 6–9 a triangle lower down, moving into the valley. Calling them **"depictions, not photographs" is reasonable and supported**: a pasted silhouette moving across one fixed frame is a reconstruction, not a photo sequence. One wording problem: in images 1–3 the shape is a sliver, not clearly a triangle (see line 26).
- **Ranch "dogs":** on PDF p.38 the control dog and the fence are both on a *redacted* property. The redaction code is 1843(a)(2), a personal-name exemption, and the text says "property near where the 'creature' was spotted". That is the witness's property, not the "Utah Ranch". The raccoon hair came from a rock "found on the ranch… on the mesa during the January deployment".
- **Ranch label pages:** the lab report is on **PDF p.37** (printed page 36). The BAASS interpretation (dog and raccoon) is on **PDF p.38** (printed 37). The label prefix "PDF P." is wrong for crops `dna`, `dog` and `rac`.

## Line-by-line table

| # / item | Claim | Source checked | Verdict | Fix (exact replacement) |
|---|---|---|---|---|
| 1 | Two agents watched matte-black triangle rise over ridge in silence, hover, dive into canyon at estimated fighter-jet speed | D176 p.1–3 | OK | — |
| 1 tag | LOCATION REDACTED · 2026 | D176 p.1 | OK | — |
| 1 labels | fbi4/5/8 "IMAGE n OF 9 … A DEPICTION, NOT A PHOTO" | FBI-UAP-D043 pp.3–11 (visual) | OK | — |
| 2 | Next-morning canyon search found no wreckage | D176 p.3 | OK | — |
| 3 | 2026 event; Pentagon published reports Oct. 23 | D176; EarthSky; KMPH | OK | — |
| 3 tag | WAR.GOV/UFO · RELEASE 07 · OCTOBER 23, 2026 | EarthSky | OK | — |
| 4 | Two reports, AARO and FBI, differ | D176; D043 | OK | — |
| 5 | "…and a lab test on hair from a creature called a Skinwalker" | D174 pp.5, 37–38 | FIX | The hair came from a fence where a witness *said* a Skinwalker ran. The script states as fact that it came from a creature. → "…and a lab test on hair from a fence where a witness said a Skinwalker had run?" |
| 5 label | MW b-roll "NOT THE SIGHTING SITE" | — | OK | — |
| 6–7 | Intro / title "THE BLACK TRIANGLE", sub "What the Seventh UFO Release Actually Says" | — | OK | — |
| 8 | "Start with the setting." | — | OK | — |
| 9 | Date and place blacked out; AARO; 2026, 8:23 pm local | D176 p.1 ("2023L"; date and place redacted) | OK | (See note: FBI says 1923 hours.) |
| 10 | Two federal law-enforcement agents on hilltop, primary observation post, routine observation support | D176 p.2 | OK | — |
| 11 | Sun just down; residual sunset gradient behind western ridge lines; valleys falling into shadow | D176 p.2 | OK | — |
| 12 | "Their cameras and their tripod-mounted thermal sensor were pointed east." | D176 p.2: "Primary optical and tripod-mounted sensor systems were initially oriented eastward" | FIX (minor) | The memo never says "cameras". → "Their main optical gear and their tripod-mounted sensors were pointed east. \| The thing came from the west." |
| 13 | Third witness at second post scanning west with long-range thermal; object over ridge line; radio call | D176 p.2 | OK | — |
| 14 | "ran across the peak… The heavy thermal camera stayed behind… a small handheld thermal monocular" | D176 p.2: "immediately relocated across the peak"; "Terrain conditions precluded quick relocation of the primary tripod-mounted thermal system"; "handheld thermal monocular" | FIX | The memo does not say "ran", "heavy" or "small". (The FBI statement does say "ran", but this line is attributed to the memo.) → "The two agents immediately moved across the peak to get a view to the west. \| The tripod-mounted thermal system couldn't be moved quickly, so it stayed behind. \| One agent had binoculars and a handheld thermal monocular." |
| 15 | He saw it with unaided eye first, dark shape against last western light | D176 p.2 | OK | — |
| 16 | "What happened next takes about half a minute to tell." | D176 (10 + 20 + 2–3 s) | FIX (minor) | "to tell" is ambiguous: it sounds like narration time. → "By the memo's account, what happened next lasted about half a minute. \| The memo splits it into three phases." |
| 17 | Phase I: straight up, slow, level; no tilt, sway, wobble; ~10 s | D176 p.1–2 | OK | — |
| 18 | Matte black, nonreflective; no rotors, rivets, panels, windows, canopy, exhaust | D176 p.2 ("rotating elements, rivets, panels, windows, canopy"; "exhaust plumes") | OK | — |
| 19 + stat | 13–15 ft wingspan, 6–9 ft long, 1–2 ft thick; "featureless" | D176 p.1 | OK | — |
| 20 | 1.4 to 3.2 miles by terrain estimates | D176 p.2 | OK | — |
| 21 | Phase II: 200–300 ft above ridge, instantly stopped, hovered ~20 s, no drift or oscillation | D176 p.2 | OK | — |
| 22 | Uniform thermal; no hot spots, engine heat, exhaust plume | D176 p.2–3 | OK | — |
| 23 | "…high-speed horizontal flight with no visible acceleration… the way a low-flying military aircraft hides behind hills" | D176 p.3: "without observable acceleration ramp"; "similar in appearance to low-altitude terrain-masking flight"; later "sudden acceleration" | FIX | The memo describes a *sudden* acceleration, not none. "Military" is the script's addition. → "Phase three. \| It went from hovering straight into high-speed horizontal flight, with no visible build-up of speed, \| banked, \| and dropped into a canyon, hugging the terrain, \| in a way the memo compares to low-altitude terrain-masking flight." |
| 24 | Last phase 2–3 s; agents compared speed to fighter jet; "no instrumented speed measurement was obtained" | D176 p.3 (verbatim) | OK | — |
| 25 | IR lost because object accelerated out of narrow field of view; absolute acoustic silence throughout | D176 p.1, p.3 | OK | — |
| 26 | Nine images; not photos; same dusk landscape; "a small black triangle placed in a different spot in each one" | D043 pp.3–11 (visual) | FIX (minor) | In images 1–3 the shape is a thin sliver, not a triangle. → "They show the same dusk landscape, with a small black shape placed in a different spot in each one, \| rising, \| hovering, \| and dropping toward the canyon." |
| 27 | Second account of same evening | D043 | OK | — |
| 28 | FD-302; statement "co-signed by two special agents, quoted word for word" | D043 p.1: "a written statement co-signed by [redacted] Special Agent [redacted]… provided verbatim"; p.2 "Co-signed SA [ ] and [ ]" | FIX | Only one co-signer is visibly titled "SA". The second co-signer's title is redacted or absent. → "Attached to it is a written statement co-signed by two agents, \| quoted word for word." |
| 29 | Quote: "almost immediately observed a substantial, nonreflective, dark black triangular object most resembling a delta wing drone" | D043 p.1 (verbatim) | OK | — |
| 30 | 9–15 ft wingspan; hotter than ambient; consistent thermal signature; no visible exhaust gases | D043 p.1 | OK | — |
| 31 | Ridge ~3.2 mi west; climbed ~200 ft; horizontal flight "at a very significant velocity, approaching our position", descended southeast | D043 pp.1–2 | OK | — |
| 32 | Lost sight ~1.5 miles away | D043 p.2 | OK | — |
| 33 | "total duration of the sighting was approximately three seconds" | D043 p.2 (verbatim) | OK | — |
| 34 + list graphic | AARO ~10 + 20 + 2–3 s, 13–15 ft, "unidentified craft"; FBI ~3 s, 9–15 ft, "most resembling a delta wing drone" | D176; D043 | OK | — |
| 35 | Documents don't explain gap; statement ends: neither detected auditory output from the unmanned aerial system | D043 p.2 | OK | — |
| 36 | "Unmanned aerial system" is the agents' description, not a finding; neither says what it was | D043 (FD-302 footer: no FBI conclusions); D176 | OK | — |
| 37 | Chapter IV | — | OK | — |
| 38 | No impact, smoke, dust; next-morning survey: no wreckage, scarring, plant damage | D176 p.3 | OK | — |
| 38 label | GORGE "NOT THE SIGHTING SITE" | — | OK | — |
| 39 | Collector note: extensive drone experience alongside government agencies and academic studies; regularly see conventional aircraft | D176 p.3 | OK | — |
| 40 | Small drone, quadcopter motor or helicopter at 1.4 mi clearly audible | D176 p.3 ("Group 1 drone, high-torque quadcopter motor, or rotary-wing aircraft") | OK | — |
| 41 | Judged size against trees on ridge | D176 p.3 | OK | — |
| 42 | "the memo rules out the strange extras… No nausea, no headaches, no lost time. No odd smells. No interference with any of their equipment." | D176 p.3: "There were no reports of…" | FIX (minor) | The memo records an absence of reports. It does not "rule out" anything. → "And the memo reports none of the strange extras that fill a lot of U F O stories. \| No nausea, no headaches, no lost time. \| No odd smells. \| No interference with any of their equipment." |
| 43 | "…should not be taken as a conclusive indication of what the object was or what it could do." | D176 p.1: "should not be interpreted as a conclusive indication of the presence or absence of any intrinsic object features or performance characteristics" | FIX | The caveat is about features and performance, not what the object *was*. → "This report, it says, reflects the reporter's interpretation at the time of the event, \| and its descriptions should not be taken as conclusive about the object's features or performance." |
| 44 | "Two trained observers… One object nobody could name. And no video of it." | D176; D043 | FIX | No document says no video exists. The release just contains none. → "Two experienced observers. \| Two documents. \| One object nobody could name. \| And no video of it in the release." |
| 45 | "The same words keep turning up, seventy years earlier." | D179 (1952) vs 2026 = 74 years; wording is similar, not identical | FIX | → "Here is the strange part of this release. \| The same ideas keep turning up, more than seventy years earlier." |
| 46 | "Most of its files are old Air Force reports, from California to Sweden, Morocco, Alaska and Saudi Arabia." | archive.org Release_07 listing: 28 PDFs; 14 are 1949–1957 Air Force sighting reports (D155–D164, D177–D179, D181); 9 are BAASS (2008–2010) | FIX | 14 of 28 is half, not "most". → "The seventh batch is not only about twenty twenty-six. \| About half of its twenty-eight files are old Air Force reports, from California to Sweden, Morocco, Alaska and Saudi Arabia." |
| 46 map | Point positions and years for Catalina 1952–55, Indiana 1954, Alaska 1953, Sweden 1953, Morocco 1953, Saudi 1957, Utah 2010 | respective files | OK | (Indiana sighting was Dec. 1953; "1954" is the report date. Acceptable.) |
| 47 + tag | June 25, 1952; Santa Catalina; three Boy Scouts, summer camp, hiking up a mountain | D179 p.2 (visual) | OK | — |
| 47 label | C52 "AUG. 28, 1952 · P. 2" | D179 p.2 | OK | — |
| 48 | Silver; faster than conventional jet; "There was no sound observed"; one climbing turn; "in the report's words, disappeared by disintegration" | D179 p.2: "its disappearance by disintegration" | FIX (minor) | Presented as a quote but not verbatim. → "It made one climbing turn, \| and then came what the report calls its disappearance by disintegration." |
| 49 | Officer's note: no estimate of reliability; experience "probably meager at best" | D179 p.2 (prepared by Lt Col E.D.H. Maddox, USAF) | OK | — |
| 50 + tag | 18 months later, Dec. 1953, couple driving near Seymour, Ind.; two objects; "complete level stability"; "incredible speed" | D164 p.1–4 | OK | — |
| 51 | "none to the ear, although observers stood outside of car to make sure" | D164 p.1 (verbatim) | OK | — |
| 52 | Circular ring of smoke; four brilliant points rotating slowly clockwise; no structure above or below | D164 p.1 | OK | — |
| 53 | "Silent. Hovering. Then gone, faster than a jet. The same three ideas, in reports written seventy years apart." | D164 ("incredible speed", not "faster than a jet"); D179; 1952 to 2026 = 74 years | FIX (minor) | → "Silent. \| Hovering. \| Then gone, at great speed. \| The same three ideas, in reports written more than seventy years apart." |
| 54 + tag | "what usually happens to cases like these"; Catalina Mar. 15, 1955; very bright round object, orange then red, fell straight down ~2 s | D177 pp.1–2 | FIX (minor) | "usually" generalizes from a handful of files. → "But the old files also show what can happen to cases like these." (rest unchanged) |
| 55 | Record card conclusion "probable meteor" | D177 p.1 (comments "Probable meteor."; "Probably Astronomical" box) | OK | — |
| 56 | File stamped Secret | D155 p.1 (visual) | OK | — |
| 57 + tag | Jan. 1957; B-52s flying around world nonstop, refuelling in air; Operation Power Flite; Jan. 16–18, 1957 | AFGSC; D155 (tanker rendezvous) | OK | (D155 spells it "Operation Powerflight"; the official spelling "Power Flite" is fine.) |
| 58 | 24,325 miles in 45 h 19 min, according to the Air Force | AFGSC | OK | — |
| 59 + tag | Over Saudi Arabia, night, 39,000 ft; B-52 no. 394; Lt Col J.H. Morris; about to meet tanker; 27°N 47°E | D155 p.1 (visual) | OK | — |
| 60 | Gunner's (A-3A gunnery) scope picked up unidentified aircraft just before rendezvous | D155 p.1 | OK | — |
| 61 | Drawing of scope; blip at 6,000-yard marker, center; 5–7 min | D155 pp.1–2 | OK | — |
| 62 | Banked left, blip slid off; turn may have caused it; seemed to disappear toward Baghdad Flight Identification Region | D155 p.1 | OK | — |
| 63 | Smaller return than a second B-52; "appeared on the scope where no aircraft were expected" | D155 p.1 (verbatim) | OK | — |
| 64 + tag | Sweden, Dec. 17, 1953; chief pilot of Swedish airline (Transair); DC-3; shining metal elliptical object passed below, opposite direction; near Hässleholm | D163 p.2 | OK | — |
| 65 | Visible 6–7 s; told newspaper "something absolutely new, possibly an unmanned robot"; U.S. air attaché translated and sent | D163 pp.1–2 | OK | — |
| 66 | Crew chief: "almost phosphorescent"; "could definitely not have been a meteor… no waste gases or condensation traces" | D163 p.2 | OK as quoted | **Omission:** D163 p.3 also says a source who knew him "personally doubts Christiernsson's story" and calls the pilot "most untrustworthy". To be fair, add after line 66: "But the attaché's report also notes that a source who had known the pilot all his life doubted his story." |
| 67 | French Morocco radar returns shaped V, W, M; anomalous propagation, ship-borne radar jamming, geese or storks | D160 p.1 | OK | — |
| 68 | Alaska light west of Gambell, St. Lawrence Island; possibly an unidentified ship in or near U.S. territorial waters | D162 p.1 | OK | — |
| 69 | "the question nobody in these files wants to answer in public" | EOP-UAP-D002 | FIX (minor) | Overgeneralizes from one memo. → "And then there is a question some officials in these files preferred not to answer in public: \| what if something comes down?" |
| 70 | 1962–63 NASC (part of EOP) meetings on who collects fallen satellite and rocket pieces | USG-UAP-D002 (EOP letterhead; Nov. 6, 1962 draft; Nov. 1963 meetings); EOP-UAP-D002 ("meetings held last year") | OK | — |
| 70 label | MAUI b-roll | — | OK | — |
| 71 | Draft guidelines: NASA responsible for receiving and identifying fragments "of space vehicles of all types"; foreign fragments, including whole vehicles, to DoD expeditiously for intelligence analysis | USG-UAP-D002 guidelines §1, §3 | OK | (Omits that DoD keeps sole responsibility for its own vehicles' fragments. Not misleading.) |
| 72 + tag | May 29, 1963 memo to NASC executive secretary Dr. Edward Welsh about meeting Arnold Frutkin, NASA director of international programs | EOP-UAP-D002; Welsh/Frutkin bios | OK | — |
| 73 | Frutkin "now very negative"; no public announcement needed; White House statement would scare people needlessly | EOP-UAP-D002 items 1–2 | OK | — |
| 74 | "point four: DoD and Air Force want to use NASA for a cover, but have no intention of letting NASA do anything but return some pieces" | EOP-UAP-D002 item 4: this is listed under "Frutkin seems to feel that", and "cover" is in quotation marks | FIX | It must stay attributed as Frutkin's view, not a statement by DoD. → "And point four, still Frutkin's view as the memo records it: \| the Defense Department and the Air Force want to use NASA for a cover, \| but have no intention of letting NASA do anything but return some pieces." |
| 75 | Memo about rockets and satellites, nothing about UFOs; "while foreign pieces went to the Defense Department for analysis" | EOP-UAP-D002; USG-UAP-D002 (drafts) | FIX (minor) | These were draft rules, so "went" states it as fact. → "But it shows officials talking about NASA as the public face, \| while foreign pieces would go to the Defense Department for analysis." |
| 76 | Chapter VIII | — | OK | — |
| 77 + tag | March–April 2010; BAASS; DIA program; ranch near Fort Duchesne, Utah | D174 PDF pp.1, 5 (Mar. 22–26, Apr. 19–23, 2010); DIA AAWSAP contract (The Debrief / DIA FOIA) | OK | — |
| 77 label | ranch_cover "PDF P. 1" | D174 PDF p.1 | OK | — |
| 78 | Witnesses reported balls of light at close range, dog-like creatures on two legs, little people, giant worm | D174 PDF pp.8–9 | OK | — |
| 78 label | ranch_abs "PDF P. 8" | D174 PDF p.8 | OK | (The crop shows the abstract's opening bullets, not the witness list further down the page. Consider re-cropping lower.) |
| 79 | Seven game cameras; witness saw what he believed was a Skinwalker a couple of days before arrival; dogs chased it; ran through barbed-wire fence | D174 PDF p.5 | OK | **Label FIX:** this text is on PDF p.5, but the line reuses `ranch_abs` labelled "PDF P. 8". Use a PDF p.5 crop labelled `UR + "5"`, or keep the image but change the label to `UR + "8"` only if the on-screen text matches. |
| 80 | Hair collected from fence; "control sample from one of the ranch's own dogs"; sent to lab for DNA | D174 PDF p.38: "Control hairs from one of the dogs on [redacted name] property"; fence "on [redacted] property near where the 'creature' was spotted" | FIX | The dog belongs to the witness's property, not the ranch. → "Hair was collected from the fence, \| along with a control sample from one of the dogs on that property, \| and sent to a laboratory for D N A testing." |
| 80–81 label | LAB b-roll "NOT THE LAB USED IN 2010" | — | OK | — |
| 82 | Fence hairs and dog's hair all showed same canine sequence, frequently found in domestic dogs | D174 PDF p.37 (SU-02/03/04 same HVI; "frequently found in domestic dogs") and p.38 (samples 2 = control, 3 and 4 = fence hairs) | OK | **Label FIX:** `dna` label `UR + "36"` should be `UR + "37"` (PDF page). |
| 83 | "The contractor's own scientist wrote… not 100 percent definitively… ranch dogs run at will on the property… strongly argues the hairs are from the same animal" | D174 PDF p.38 (email from "AAP Person 18", captioned "BAASS scientific interpretation of analysis"; "the dogs on [redacted] property run at will") | FIX | The author's role is redacted, and the dogs are not "ranch dogs". → "The contractor's own analysis says this suggests, though not one hundred percent definitively, the same canine individual. \| And because the dogs on that property run at will, it says the evidence strongly argues the hairs are from the same animal." **Label FIX:** `dog` → `UR + "38"`. |
| 84 | Fourth hair, embedded in red-stained rock: raccoon | D174 PDF pp.37–38 | OK | **Label FIX:** `rac` → `UR + "38"` (lines 84 and 85). |
| 85 | "Several people at the ranch had reported raccoons nearby, the scientist added… not out of the ordinary" | D174 PDF p.38 | FIX (minor) | Same authorship point as line 83. → "Several people at the ranch had reported raccoons nearby, the analysis added, \| so this finding would not be out of the ordinary." |
| 86 | Chapter IX | — | OK | — |
| 87 | News reports: officials call files unresolved, meaning not enough info to identify, not linked to anything from another world | KMPH / Sinclair | OK | — |
| 88 | Parnell: department will release additional files on a rolling basis | EarthSky | OK | — |
| 89 | "Look at the batch as a whole… A meteor. Storks on radar. A ship. A turning bomber. Dog hair and a raccoon. Again and again, a careful look turns up something ordinary." | D177, D160, D162, D155, D174 | FIX | Overstates. Most of these are possibilities, not findings. The bomber's turn explains only the blip vanishing, and the 1952 Catalina and 1957 B-52 files reach no conclusion. "Batch as a whole" also covers 28 files the script didn't review. → "Look at these files together and a pattern appears. \| A probable meteor. \| Possibly storks on radar. \| Possibly a ship. \| A bomber's turn that may explain a vanishing blip. \| Dog hair and a raccoon. \| Again and again, the files reach for something ordinary, even when they can't prove it." |
| 89 timeline | Title "What the files concluded"; 1952 "Catalina: no estimate"; 1953 "Morocco: maybe storks"; 1955 "Catalina: meteor"; 1957 "B-52: \"not expected\""; 2010 "Ranch: dog, raccoon"; 2026 "Triangle: open" | same | FIX | "no estimate" refers to reliability, not a conclusion. "meteor" should be "probable". "\"not expected\"" is not a verbatim fragment. → 1952 `"Catalina: no conclusion"`; 1955 `"Catalina: probable meteor"`; 1957 `"B-52: unidentified"`; others unchanged. |
| 90 | Two experienced observers; thermal reading; clear evening; terrain; next-morning search | D176 | OK | — |
| 91 | "in the government's own words, an unidentified craft" | D176 p.1 | OK | — |
| 92 | Maybe a drone they couldn't hear; documents don't say | — | OK | — |
| 92 label | GC b-roll | — | OK | — |
| 93 | "federal agents described something in the same words an Air Force officer used about three Boy Scouts in 1952. Silent. Faster than a jet. Gone." | D176 ("absolute acoustic silence", "as fast as a fighter jet") vs D179 ("no sound observed", "faster than a conventional Jet") | FIX (minor) | Similar terms, not the same words. → "What they do show is that in twenty twenty-six, federal agents described something in much the same terms an Air Force officer used about three Boy Scouts in nineteen fifty-two. \| Silent. Faster than a jet. Gone." |
| 94 | Date still blacked out | D176; D043 | OK | — |
| 95 | Two official reports, about 30 s vs 3 | D176; D043 | OK | — |
| 96 | Next file teaser | — | OK | — |
| DISPLAY | Subtitle spellings ("seventy years" → "70 years" etc.) | — | FIX (follow-on) | If lines 45/53 change, the DISPLAY entry ("seventy years", "70 years") still works ("more than 70 years"). Add ("twenty-eight", "28") for the line 46 fix. |
| Label FI | "A DEPICTION, NOT A PHOTO OF THE OBJECT" | D043 images (visual) | OK | — |
| Labels A_, FB, SA, IN, C52, C55, SW, MO, AK, EOP | Doc names, dates, page numbers | respective PDFs | OK | — |
| Label UR "PDF P." on dna/dog/rac | page numbers | D174 | FIX | dna → 37; dog → 38; rac → 38 |
| Credit | Documents from AARO, FBI, USAF, LBJ Library, contractor | release files | OK | — |
| META title | "The Silent Black Triangle Federal Agents Couldn't Identify" | D176 ("unidentified craft"); D043 (agents call it a UAS) | OK | (Defensible because AARO calls it unidentified. Note that the FBI statement itself calls it "the unmanned aerial system".) |
| shorts s1 hook | "B-52 RADAR: SOMETHING NOT EXPECTED" | D155 | OK | — |
| shorts s2 hook | "THE 'SKINWALKER' HAIR TEST" | D174 | OK | — |
| shorts s3 hook | "THE FBI'S VERSION: 3 SECONDS" | D043 | OK | — |
| shorts s4 hook | "'USE NASA FOR A COVER'" | EOP-UAP-D002 | OK as a quote | Must be paired with the corrected title (below). |
| yshorts y1 hook | "SILENT BLACK TRIANGLE" | D176 | OK | — |
| yshorts y2 hook | "'SKINWALKER' HAIR: DNA RESULT" | D174 | OK | — |
| yshorts y3 hook | "30 SECONDS OR 3?" | D176; D043 | OK | — |
| Thumb A | FBI depiction 5 labelled "FBI DEPICTION"; "matte black triangular shape"; "UNIDENTIFIED"; "RELEASED OCT. 2026"; "NO SOUND. NO WRECKAGE."; "STILL UNIDENTIFIED" | D176 p.1, p.3; D043 | OK | — |
| Thumb B | "WHAT / DID THEY / SEE?"; "RELEASED OCT. 2026" | — | OK | — |
| Thumb C | "dark black triangular object" highlight; "FBI FILE, 2026"; **FBI: "DARK BLACK TRIANGLE"**; "GONE IN 3 SECONDS" | D043 p.1–2 | FIX | The words in quotation marks are not verbatim. → `FBI: "DARK BLACK TRIANGULAR OBJECT"`, or drop the quotes: `FBI: DARK BLACK TRIANGLE` |
| y1 title | "Federal Agents Saw a Silent Black Triangle in 2026" | D176; KMPH ("reported seeing") | FIX | → "Federal Agents Reported a Silent Black Triangle in 2026" |
| y2 title | "What the 'Skinwalker' Hair DNA Test Actually Found" | D174 | OK | — |
| y3 title | "Two Official Reports, One Triangle: 30 Seconds or 3?" | — | OK | — |
| s1 title | "A B-52 Gunner's Radar Caught Something Over Saudi Arabia" | D155 | OK | — |
| s2 title | "The Government's 'Skinwalker' Hair Test Came Back… Dog" | D174 (test commissioned by contractor BAASS under a DIA contract) | FIX | → "A Pentagon Contractor's 'Skinwalker' Hair Test Came Back… Dog" |
| s3 title | "The FBI and the Pentagon Disagree About This Black Triangle" | D043 (agents' statement; FD-302 has "neither recommendations nor conclusions of the FBI") | FIX | Neither agency took an institutional position. → "An FBI File and a Pentagon Memo Tell Different Stories About This Black Triangle" |
| s4 title | "Why Officials Wanted to 'Use NASA for a Cover' in 1963" | EOP-UAP-D002 item 4 (Frutkin's view of DoD and AF intent) | FIX | → "1963 Memo: A NASA Official Said the Pentagon Wanted NASA as a 'Cover'" |
| Description hook | Seventh release Oct. 23, 2026; AARO memo + FBI report; silent matte-black triangle climbed, hovered, dropped into canyon; accounts disagree on duration | D176; D043; EarthSky | OK | — |

## Summary

- **Items checked:** 96 LINES plus about 45 labels, graphics, tags and packaging items.
- **FIX — spoken lines (21):** 5, 12, 14, 16, 23, 26, 28, 42, 43, 44, 45, 46, 48, 53, 54, 69, 74, 75, 80, 83, 85, plus line 89 and line 93 (**23 spoken-line fixes in total**). Line 66 has a recommended fairness addition.
- **FIX — on-screen and graphics (6):** timeline graphic (line 89); ranch labels dna/dog/rac page numbers; line 79 label/crop mismatch; DISPLAY additions.
- **FIX — packaging (5):** Thumb C quote, y1 title, s2 title, s3 title, s4 title.
- **Most important:** line 74 and the s4 title (the "cover" claim is Frutkin's view, not a DoD statement); line 89 and the timeline (overstated "ordinary" pattern); line 80/83 (the dogs are not "ranch dogs"); line 46 ("most" should be "about half" of 28); line 5 (hair "from a creature"); line 28 ("two special agents"); line 43 (caveat misparaphrased).
- **Everything else is OK.** All numbers check out: 13–15 ft, 9–15 ft, 6–9 ft, 1–2 ft, 1.4–3.2 mi, 200–300 ft, ~10/20/2–3 s, ~3 s, 1.5 mi, 39,000 ft, 6,000 yd, 5–7 min, 24,325 mi / 45 h 19 min, and all dates.
- **"Depictions, not photographs":** reasonable. All nine FBI images share one identical background frame with a pasted flat black silhouette.
- **Advisory:** the FBI statement's time (1923 hours) differs from AARO's 2023L by one hour. The script does not mention it.

## Applied (2026-11-18, before rendering)
All spoken-line FIX items applied verbatim or with equivalent wording (lines renumbered by +1 after line 66 because a Sweden caution line was added): 5, 12, 14, 16, 23, 26, 28, 42, 43, 44, 45, 46 (+ DISPLAY "28 files"), 48, 53, 54, 69 (legal reviewer's wording), 74, 75, 80, 83, 85, 89, 93; recommended Sweden caution line added (source doubted the pilot's story; Defense Staff kept investigating). FBI/AARO time difference (1923 vs 2023) added to line 32.
On-screen: timeline labels changed ("no conclusion", "probable meteor", "unidentified"); ranch labels now PDF p. 37/38; line 80 now shows a PDF p. 5 crop (ranch_exec).
Packaging: thumbnail C line 1 now "\"DARK BLACK TRIANGULAR\"" (verbatim words of the statement), line 2 "3 SECONDS OR 30?"; y1, s2, s3, s4 titles replaced with the suggested (or legal-review) wording.
