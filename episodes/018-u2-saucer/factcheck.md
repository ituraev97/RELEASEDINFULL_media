# FILE 018 — Independent fact-check

Checked 2026-11-22 against the primary documents in /home/claude/src/r08 (Release 08 PDFs, text extraction, D172 OCR), page renders, the document crops in /home/claude/src/img/doc, frames taken from every b-roll clip at the timecodes in the script, the DVIDS API records for videos 1030270/1030274/1030277 and the b-roll and photo sources, CBS, FOX Local (KTVU), Interesting Engineering, and AARO's "Presidential UAP Transparency Initiative" page.

Line numbers are 1-indexed positions in `LINES`. "Page" means the PDF page, which is also the page the `lab=` suffix uses.

## Spoken lines and shots

| # | Claim | Source checked | Verdict | Replacement (FIX only) |
|---|---|---|---|---|
| 1 | The future U-2 engineer told the Air Force he had watched a flying saucer and was "more firmly convinced than ever that such devices exist" | D206 p.6–7 (statement addressed "To: Air Force Investigating Group on Flying Saucers"; "so-called 'saucer'"; p.7 quote). Crop j_believe = p.7. U2GOLD photo = DVIDS 8465347, Beale, June 3, 2024 | PASS | |
| 2 | Air Force card: lenticular cloud. Crew near 17,000 ft said it was not a cloud | D206 p.1 card; p.9 (Thoren "17,000 and 18,000 feet", "not a cloud"), p.11 (Wimmer), p.12 (Colman). Clip dv908150 @165 = U-2 at Beale, 2023 | PASS | |
| 3 | One of 40 documents published Friday, Nov. 20, in the eighth release, with 3 new videos | KTVU ("three videos and 40 documents"); Interesting Engineering (43 records = 40 + 3); Nov. 20, 2026 is a Friday. V168 label matches DVIDS PR168 | PASS | |
| 4 | CIA memos wanting no one to know of the agency's interest; Texas engines; vault for "exotic material or tissue" | D026 p.1, D027 p.2 ("outside knowledge of Agency interest ... must be avoided"); D191 p.5; D172 p.9. Crop labels correct | PASS | |
| 6 | Title card "THE U-2 DESIGNER'S SAUCER" | D206 p.6 (he calls it a "so-called 'saucer'"; the Air Force called it a cloud) | FIX | `t="THE U-2 DESIGNER'S \"SAUCER\""` (put SAUCER in quotes, matching how he wrote it) |
| 8 | Clarence "Kelly" Johnson, chief engineer, Lockheed California Division, Burbank | D206 p.2, p.3 letterhead, p.5 signature; p.10 "Kelly". j_cover = p.2 | PASS | |
| 9 | His engineers would build the U-2, and later the SR-71 | CBS ("later designed the U-2 and SR-71"); general record (U-2 first flew 1955). Clips: 908150 @176 = U-2; 1017843 @230 = view from a U-2 cockpit at altitude | PASS | |
| 10 | Wed. Dec. 16, 1953; ranch 3 mi W of Agoura; arrived about sundown | D206 p.6 ("went out to our ranch"; "drove" is a fair reading) | PASS | |
| 10 map | MAP_CA kicker, points, bounds | D206 p.6 (ranch, about 5 P.M., Point Mugu), p.10 (Thoren: "just off of Long Beach"); Burbank letterhead. All points are inside the bounds | FIX (title only) | `title="Two views, one sighting report"` ("Two views of one object" states as fact that both groups saw the same object. That is the witnesses' claim.) |
| 11 | About 5 o'clock, "within two minutes' accuracy"; plate-glass window; first thought a black cloud | D206 p.6; crop j_black = p.6 | PASS | |
| 12 | Western sky gold and red; why so dark with the sun behind it | D206 p.6 | PASS (but see the photo label FIX below) | |
| 13 | Smoke trail first; outline unchanged; thought lenticular cloud; no movement for 3 minutes | D206 p.6; j_hover = p.6 | PASS | |
| 14 | 8-power binoculars; recognized it as a "so-called saucer" | D206 p.6 | PASS | |
| 15 | Ran outside, moving fast roughly west (heading 240–260°); black, distinct, no detail | D206 p.6. U2PINK = DVIDS 8465345, Beale, 2024 | PASS | |
| 16 | Gone within 90 seconds, in a long shallow climb | D206 p.6; j_climb = p.6 | PASS | |
| 17 | Roughly over Point Mugu; an ellipse "about 7 or 10 to 1"; very large | D206 p.6 | PASS | |
| 19 | Back after about a week; chief flight test engineer came in with two senior engineers | D206 p.6–7 (Wassall, Asst. Chief Engineer; Haddon, Chief Project Engineer), p.10; th_kelly = p.10 | PASS | |
| 20 | "Kelly snapped this up immediately ... 5:05 ... off Point Mugu. This literally bowled me over" | D206 p.10 (light trim, meaning kept) | PASS | |
| 21 | Co-pilot on a Navy Super Constellation WV-2, took off at 4:29 p.m. | D206 p.9. E2 photo = DVIDS 7177846, E-2D, Point Mugu, Apr. 30, 2022 (label correct) | PASS | |
| 22 | Between 15,000 and 20,000 ft the pilot said "Look out, there's a flying saucer" | D206 p.9; th_saucer = p.9, names barred | PASS | |
| 23 | Turned toward it, expected to overtake it, about 5 min at about 225 mph, "never closed the gap" | D206 p.9: "we did not seem to be closing the gap" | FIX | `They turned straight toward it, expecting to overtake it. \| For about five minutes they flew at it, \| at some two hundred twenty-five miles an hour. \| They did not seem to close the gap.` |
| 24 | Sharp, definite edges; very large flying-wing airplane; silhouetted against red sky | D206 p.9 (OCR "flying wine" is "wing" in the scan); th_wing = p.9 | PASS | |
| 25 | Got smaller; in about a minute a "mere speck"; vanished almost due west | D206 p.9. Clip 908150 @386 = U-2 | PASS | |
| 26 | Pilot: at least 50 or 60 miles, possibly much farther; "not a cloud that dissolved" | D206 p.11 (Wimmer, Jan. 12, 1954). TU2 = DVIDS 5672066, Beale, Jan. 22, 2014 | PASS | |
| 27 | Chief aerodynamicist: the difference in positions showed too much depth to be a cloud | D206 p.12 (Colman: "sufficient depth to eliminate the possibility that it was a cloud phenomenon"); co_depth = p.12 | PASS | |
| 28 | "very skeptical ... what Kelly saw and what we saw appear to be identical ... not exactly an illusion" | D206 p.10 (the original says "what he saw"; "Kelly" swapped in, meaning kept); th_skept = p.10 | PASS | |
| 29 | Chapter / transition | none needed | PASS | |
| 30 | Covering letter Jan. 20, 1954, to ATIC, Wright-Patterson; "not been released to the press" | D206 p.5; j_press = p.5 | PASS | |
| 31 | Air Force officer, February: Johnson "most reluctant ... refused to forward it" | D206 p.2 (Lt., USAF, Feb. 15, 1954) | PASS | |
| 32 | Reason: those who profess to have seen saucers are not considered logical, hard-headed engineers | D206 p.2 | PASS | |
| 33 | "For at least five years I have definitely believed in the possibility..." | D206 p.7; j_believe = p.7 | PASS | |
| 34 | "the line he did not want read in public" | D206 p.2 says he would not forward the report, but p.5 shows he did send it to ATIC himself. Nothing says he wanted this line kept private. Quote graphic checked against p.7: verbatim, trailing "…" for "as of that date"; signed Dec. 18, 1953 | FIX (spoken lead-in only; quote graphic PASS) | `And then the line at the heart of his letter. \| Having seen this particular object, \| I am now more firmly convinced than ever that such devices exist, \| and I have some highly technical converts in this belief.` |
| 35 | Card: "Conclusion: other. Cloud. Lenticular cloud." | D206 p.1; j_card = p.1 | PASS | |
| 36 | Lenticular clouds: lens-shaped, form in airflow over mountains, can look stationary | standard meteorology (mountain-wave/standing lenticular clouds) | PASS | |
| 37 | Card summary "first appeared as black stationary cloud, then rapid movement in long shallow climb" | D206 p.1 | PASS | |
| 38 | "Almost seventy-three years later" released as "unresolved UAP report" | Dec. 16, 1953 → Nov. 20, 2026 = 72 years 11 months; file title DOW-UAP-D206 "Unresolved_UAP_Report". Clip 908150 @363 = U-2 | PASS | |
| 39 | "Go back one year" (to 1952) | D027, D026 | PASS | |
| 40 | OSI: phenomenal increase; requests poured in on the Air Force; official query from the White House | D027 p.1; c27_head = p.1 | PASS | |
| 41 | Aug. 14, 1952 briefing: about 1,500 official reports since 1947; 250 in July; 20% unexplained (stat graphic too) | D027 p.9 ("ATIC carries 20% as unexplained"; ATIC is the Air Force center) | PASS | |
| 42 | US weapon denied at the highest level; Russian: "absolutely no intelligence of such a technological advance" | D027 p.9–10; c27_russ = p.10 | PASS | |
| 43 | Man from Mars ... "no shred of evidence to support this theory at present" | D027 p.10 ("and that space travel is possible" trimmed, meaning kept); c27_mars = p.10 | PASS | |
| 44 | Another August memo: 1,000–2,000 reports; fewer than 100 credible ones still "unexplainable" | D026 p.1 (dated Aug. 1, 1952); c26_unexp = p.1 | PASS | |
| 45 | "interplanetary aspects and alien origin not being thoroughly excluded"; caution requires continued coverage | D026 p.1 | PASS | |
| 46 | "strongly urged ... no indication of CIA interest or concern reach the press or public ... probable alarmist tendencies" | D026 p.1 | PASS | |
| 47 | October secret memo: "might conceivably be an attack on the U.S."; enemy could use the confusion to launch "some air weapon" | D028 p.1 (SECRET, Oct. 13, 1952) | PASS | |
| 48 | Ad hoc panel of top-level scientists; about $5,000 | D024 p.2 (both crops on p.2) | PASS | |
| 49 | Panel named for its chairman, physicist Howard (H. P.) Robertson, met January 1953, 11 months before Dec. 16, 1953 | general record: Robertson Panel, Jan. 14–17, 1953. Clip 346026 @4 = U.S. Capitol, 2012 | PASS | |
| 50 | "Four years later, the reports came from the ground." | Johnson's 1953 sighting was also from the ground, so the contrast is wrong | FIX | `Four years later, the reports came from the roads of west Texas. \| And this time, there were engines involved.` |
| 51 | Night of Nov. 2, 1957; Levelland about 30 mi west of Lubbock | D191 p.3; straight-line distance ≈ 30.5 mi | PASS | |
| 51 map | MAP_TX | Levelland sub "ENGINES AND LIGHTS FAILED" states witness claims as fact. Albuquerque (lat 35.08) is outside `bounds` (top edge 34.9), so it will be clipped or drawn off-map | FIX | Levelland `sub="ENGINE FAILURES REPORTED"`; `bounds=[[-107.6, 32.3], [-100.9, 35.4]]` |
| 52 | Shortly after midnight, 19-year-old student, driving home from Lubbock on Hwy 116 | D191 p.5 (0005 CST, Nov. 3; Texas Tech freshman, 19) | PASS | |
| 53 | Ammeter to discharge; engine cut out as if not getting gas; then lights and radio out | D191 p.5 | PASS | |
| 54 | Got out, lifted hood, found nothing wrong, turned to look for help, saw object | D191 p.5 ("check for battery malfunction and, finding none") | PASS | |
| 55 | Oval, white with greenish tint, 75–100 ft; summary: two witnesses saw it hovering or resting on the ground 3–5 min | D191 p.5: the tint was "possibly caused by the tinted windshield". p.4 summary says two witnesses. p.21 comment 1a: "Only one observer (Part One) said an object hovered over or on the ground." The script leaves out both qualifiers | FIX | `Oval-shaped, he told the Air Force, white with a greenish tint, possibly from his tinted windshield, \| seventy-five to one hundred feet at its longest. \| The report's summary says two witnesses saw an object hovering or resting on the ground, \| though the officer's own comments say only this driver described that.` |
| 56 | After 4–5 min, rose virtually straight up; lights and radio came on; motor started "with no difficulty" | D191 p.5 (attributed: "he said"); lv_restart = p.5 | PASS | |
| 57 | Truck driver about 4 mi out of Levelland: big flame came over him; engine and lights out; lay on the ground | D191 p.8 and p.10 (statement). The officer wrote on p.21: "This observer's account of the sighting cannot be relied upon." The script leaves that out while repeating his account | FIX | `Earlier that night, about four miles outside Levelland, a man driving a truck said a big flame came over his position. \| His truck's engine and lights went out. \| Because of the heat and the speed, he said, he got out and lay down on the ground. \| The investigating officer wrote that his account could not be relied upon.` |
| 58 | Sheriff and highway patrolman went looking; only a streak or flash of light | D191 p.11 ("just a streak of light one time"), p.12 ("strange looking flash"). Clip 752141 @44 = Lubbock, 2020 | PASS | |
| 59 | Air Force T/Sgt and wife near Shallowater: lightning bolt; lights and radio out 1–3 s | D191 p.13–14; lv_bolt = p.14 | PASS | |
| 60 | "that was certainly a strong bolt of lightning to put out our lights and radio" | D191 p.14 verbatim | PASS | |
| 61 | List: air traffic negative; balloons not likely; power lines negative; drizzle, overcast 400 ft | D191 p.18 (Part Seven; contents p.3 calls it "Supplementary Investigative Efforts") | PASS | |
| 62 | Possibilities: St. Elmo's fire, ball lightning, excess burning gas reflected off very low cloud | D191 p.21; oil-field gas p.18; lv_poss = p.21 | PASS | |
| 63 | "something you rarely see in these files" plus the "insufficient knowledge ... forwarded as unresolved" quote | Quote verbatim, D191 p.21. "Rarely" is an unsupported generalization: the release itself is made up of "unresolved" files | FIX (lead-in only) | `And then he wrote something unusually candid. \| It is felt that insufficient knowledge of the above phenomena exists at this organization to completely resolve this sighting. \| Therefore, this sighting is forwarded as unresolved.` |
| 64 | Same weekend, more than 200 mi west, two Army MP patrols at White Sands Proving Ground | D193 p.3; Levelland → Trinity Site ≈ 235 mi | PASS | |
| 65 | About 2:30 a.m.: very bright object came down, hung motionless, egg-shaped. That evening, near Trinity Site (first atomic test), a light rose from the ground | D193 p.4 ("shaped like an egg"), p.5 (about 2000 hrs, Nov. 3, "leave the ground"); Trinity = July 16, 1945 test site; ws_egg = p.4 | PASS | |
| 66 | Verdict: first patrol mistook moonset, second merely witnessed Venus | D193 p.8 (preparing officer's opinion); ws_moon = p.8 | PASS | |
| 67 | "half a century" (1957 → 2008) | arithmetic | PASS | |
| 68 | 2008: Reid (NV) and Inouye (HI) sponsored a $10 million add | D186 p.1 (FY2008 Defense Supplemental); D184 (July 2008 supplemental); a_10m = p.1 | PASS | |
| 69 | Purpose: foreign advanced aerospace weapon threats, present out to 40 years | D186 p.1 | PASS | |
| 70 | 12 technical areas incl. lift, propulsion, armament, signature reduction, temporal translation | D186 p.1 | PASS | |
| 71 | Only one bid, BAASS, North Las Vegas; contract signed Sept. 22, 2008 | D186 p.1; D184 p.1 and D187 p.1 (22 September 2008). Clip 996238 @120 = Las Vegas from Nellis | PASS | |
| 72 | 26 reports delivered by Sept. 2009; release includes the title list | D186 p.1; D188 p.3; a_titles = p.3 | PASS | |
| 73 | Titles: invisibility cloaking, wormholes, antigravity, warp drives | D188 p.3 | PASS | |
| 74 | October DIA review: "all of the reviews of the reports were positive" | D188 p.1: only the highlighted reports were reviewed, and "all of the reviews were positive, some exceptionally so". The script's wording implies all 26 were reviewed | FIX | `An internal D I A review that October said all of the reviews it had received were positive, \| some exceptionally so.` |
| 75 | June 2009 Reid letter to the Deputy Secretary: "much progress ... several highly sensitive, unconventional aerospace-related findings" | D183 p.1 (June 24, 2009, to William Lynn III) | PASS | |
| 76 | Asked for parts in a restricted SAP with a tightly limited list | D183 p.1–2 ("specific portions"; "Bigoted Access List"). Clip 346026 @14 = Capitol | PASS | |
| 77 | Nov. 2009: "DIA cannot find adequate justification to establish a restricted SAP" | D185 p.1 (Nov. 13, 2009) verbatim | PASS | |
| 78 | "the contractor was already building out" | D172 p.9–10: plans drawn, buildings in escrow, nothing under construction. "Building out" sounds like construction, and line 89 then says there is no record the vault was built | FIX | `But by then, the contractor was already planning to expand.` |
| 79 | Ten-month report, July 2009, 538 pages; section "Progress on New BAASS Facilities" | D172 (538 PDF pages; p.3 "Ten Month Report"; p.9 heading "...: May-July 2009"). Clip 996238 @135 | PASS | |
| 80 | Vault need; recovered hardware and biological samples; corporate world, individuals, groups elsewhere incl. Brazil | D172 p.9; v_need = p.9 | PASS | |
| 81 | "no highly secure facility ... to store exotic material or tissue that the organization could obtain" (quote graphic) | D172 p.9 verbatim, including "at BAASS" | PASS | |
| 82 | North Las Vegas at Bigelow Aerospace; fencing, razor wire, cameras, 24-hour armed guards | D172 p.9; v_loc = p.9 | PASS | |
| 83 | 5,000 sq ft; 3-ft walls, ceiling, floor; tunnel; steel vault door; 15–20 ft of earth (stat graphic "BAASS PLAN · MAY 2009") | D172 p.9 (plans drawn in May) | PASS | |
| 84 | "Any surface structures protruding ... will be extensively camouflaged" | D172 p.9 verbatim | PASS | |
| 85 | Ready late 2009 or early 2010, subject to permits | D172 p.9 | PASS | |
| 86 | 2010 plan item "Launch search to obtain EBE tissue samples" | D172 p.478 ("BAASS STRATEGIC PLAN FOR 2010"), p.496 item f; v_ebe = p.496 | PASS | |
| 87 | Contractor quote "under the hypothesis that biological material of potentially non-human origin has been recovered ... lobby for access ... AFIP" | D172 p.496. The spoken version drops the "or ... biological or chemical agents of currently-unknown type" clause, but the crop shows the full sentence on screen. Acceptable trim | PASS | |
| 88 | The passage does not say any such material was found | D172 p.496 | PASS | |
| 89 | CBS: no public record the vault was built; later contractor reports do not mention it | CBS: "There's no public record that the vault was ever built. Subsequent BAASS reports the Pentagon has released make no mention of it." | FIX (minor precision) | `And was the vault ever built? \| CBS News, reporting on the release, says there is no public record that it was, \| and that later contractor reports released by the Pentagon do not mention it.` |
| 90 | "That November," Burgess and Lynn met Reid; reports of "limited value to DIA" | D186 p.2 (Nov. 2009). Burgess was DIA director 2009–12 and Lynn Deputy SecDef 2009–11. "That November" is ambiguous: the last dates spoken were 2010 (lines 85–86) | FIX | `In November twenty oh-nine, the D I A director, Lieutenant General Ronald Burgess, and Deputy Secretary of Defense William Lynn met with Senator Reid. \| By the director's own account, \| they determined the reports were of limited value to D I A.` |
| 91 | Per CBS, program ended 2012 | CBS ("ended in 2012") | PASS | |
| 93 | 2023 civil air-surveillance radar: 8 detections over 84 s, 55,000–70,000 ft | D165 | PASS (see TOWER label FIX below) | |
| 94 | 38.5 mi; if one object, minimum mean ground speed about 1,650 mph, about Mach 2.5 (stat graphic) | D165 | PASS | |
| 95 | 12-s sweep not sufficient to establish one object or a continuous track | D165 | PASS | |
| 96 | Three CENTCOM videos, Middle East. 2020: 20 s infrared, area of contrast enters from the right | DVIDS 1030270 (PR166) | PASS | |
| 97 | 2023: 13 s, sensor tracks an area of contrast | DVIDS 1030277 (PR169) | PASS | |
| 98 | 2026: 54 s, multiple areas of contrast, then two, intermittently loses contact | DVIDS 1030274 (PR168) | PASS | |
| 99 | Same warning: not an analytical judgment or investigative conclusion | DVIDS descriptions (all three), close paraphrase | PASS | |
| 101 | Timeline graphic | D206 card (lenticular cloud); D209 (Avalon/Catalina, Mar. 15, 1955, "Probable meteor"); D207 (Fontana & La Jolla, Aug. 22, 1956, "Was Aircraft"); D193 p.8; D191 p.21; D165. "Radar: not established" is unclear on its own | FIX (one event label) | `dict(y="2023", t="Radar: one object not established")` |
| 102 | Was aircraft / probable meteor / moonset and Venus / lenticular cloud | same as 101 | PASS | |
| 103 | Pentagon files them as unresolved; "unable to make a definitive determination" | AARO Presidential UAP Transparency Initiative page ("unresolved cases, meaning the government is unable to make a definitive determination"); Interesting Engineering | PASS | |
| 104 | "the witnesses were the people least likely to be fooled" | Editorial. It implies the Air Force answer was wrong, which the documents do not establish. "Trained to make accurate observations" is in D206 p.10 | FIX | `But sometimes the witnesses were people who watched the sky for a living. \| A man who designed airplanes. \| A test crew who, as one of them wrote, were trained to make accurate observations.` |
| 105 | Files do not say what he saw | — | PASS | |
| 106 | "a government that in 1952 wanted no one to know it was interested" | D026 and D027 are CIA. The Air Force studied the subject openly: D027 p.1 records General Samford's July 29, 1952 press conference. "Government" is wrong. Also "drew up a ... vault" should be "drew up plans for" | FIX | `What they do show is an intelligence agency that in nineteen fifty-two wanted the press and public kept from knowing it was interested, \| and a contractor that, in twenty oh-nine, drew up plans for a buried, camouflaged vault \| for exotic material or tissue it might one day obtain.` |
| 107 | Parnell: department and partners already working on the next release | Interesting Engineering quotes Parnell: "...actively working on the next release of UAP files"; KTVU: "additional files on a rolling basis" | PASS | |
| 108 | "Every secret has a release date. Johnson's waited almost seventy-three years." | D206 p.1: the card carries a NARA declassification stamp (Authority NND 923007, the Project Blue Book declassification). The file has not been secret until now: this release re-publishes it under a new heading. "Waited 73 years" is misleading | FIX | `Some files take a long road to a Pentagon release. \| Johnson's took almost seventy-three years.` |
| 109 | Crew said not a cloud; Air Force said it was; question to viewers | D206 p.1, p.9–12 | PASS | |
| 110 | Outro | — | PASS | |

## On-screen labels, constants, maps, DISPLAY, META

| Item | Claim | Source checked | Verdict | Replacement (FIX only) |
|---|---|---|---|---|
| J / JB labels | D206 pages 1, 5, 6, 7, 9, 10, 12 | page-by-page pdftotext and crops: every crop matches its page; black bars only on th_saucer/th_speck as labelled | PASS | |
| j_cover label | "AIR FORCE COVER LETTER (FEB. 1954) · P. 2" | D206 p.2, Feb. 15, 1954 | PASS | |
| C24 / C26 / C27 / C28 | pages and dates | D024 p.2; D026 p.1 (Aug. 1, 1952); D027 p.1 and p.10 (Aug. 14, 1952); D028 p.1 (Oct. 13, 1952) | PASS | |
| LV / WS | D191 p.4, 5, 8, 14, 21; D193 p.4, 8 | crops match | PASS | |
| R183 / R185 / R186 / R188 | dates and pages | D183 June 24, 2009; D185 Nov. 13, 2009; D186 p.1–2 (Dec. 2010, per file title); D188 Oct. 30, 2009, p.1 and p.3 | PASS | |
| BA | D172 PDF p.9 and p.496 | OCR and crops match | PASS | |
| RAD | "UNRESOLVED RADAR DETECTION, UNITED STATES, 2023 · DOW-UAP-D165" | slide title | PASS | |
| V166 / V168 / V169 | sensor type, year, CENTCOM, Middle East | DVIDS API | PASS | |
| U2, U2ALT, CAP, LUB, VEGAS | b-roll descriptions | frames at the scripted timecodes: U-2 at Beale (908150, Oct. 2023); U-2 cockpit view at altitude (1017843, 2026); Capitol (346026, 2012); Lubbock (752141, 2020, ≈30 mi from Levelland); Las Vegas skyline from Nellis (996238, Feb. 2026) | PASS | |
| TOWER (line 93) | "CONTROL TOWER AT NIGHT, NAS POINT MUGU, 2026" | DVIDS 996558: Navy air operations controllers' radar display during Bamboo Eagle (Feb. 13, 2026). The frame at 24 s is a radar scope, not a tower. It plays under narration about the 2023 radar, so viewers could take it for that radar. From about 27 s the clip shows a servicemember's face, and the episode rule is "no photos of people" | FIX | `TOWER = "B-ROLL · NAVY AIR-OPERATIONS RADAR DISPLAY, POINT MUGU, CALIFORNIA, 2026 · NOT THE 2023 RADAR DATA"`, and keep the shot inside 24–26.5 s of the clip |
| MUGU (lines 12, 17, 108) | "SUNSET AT POINT MUGU, CALIFORNIA, 2022" | mugu_sun = DVIDS 7177845, an MH-47 Chinook silhouetted at sunset, Point Mugu, Apr. 30, 2022. The helicopter dominates the frame and plays under narration about the 1953 object | FIX | `MUGU = "PHOTO · AN ARMY MH-47 CHINOOK AT SUNSET, POINT MUGU, CALIFORNIA, 2022 · NOT THE 1953 OBJECT"` |
| U2GOLD / U2PINK / TU2 / E2 | photo labels | DVIDS 8465347 and 8465345 (Beale, June 3, 2024); 5672066 (TU-2S, Beale, Jan. 22, 2014); 7177846 (E-2D, Point Mugu, 2022) | PASS (note: line 36 uses U2GOLD under the lenticular-cloud definition; the cloud in that photo is not confirmed as lenticular, and the label already says it is not the 1953 object) | |
| S_* source lines | S_P, S_J, S_C, S_L, S_V, S_R | match the documents. S_A is defined but not used | PASS | |
| MAP_CA / MAP_TX | see lines 10 and 51 above | | FIX (title; Levelland sub; bounds) | see above |
| DISPLAY | number and acronym conversions | Applied in list order to every line: all conversions give correct figures (e.g. "between 15,000 and 20,000 feet", "4:29", "5:05", "Highway 116", "WV-2", "SR-71", "1,650 miles", "38.5 miles", "73 years", "$10 million", "2:30"). Acronyms are ordered before "U S", and the "Twenty twenty-three/-six" rules come before "Twenty twenty". No mis-substitutions found | PASS | |
| META credit | Release 08, war.gov/UFO, Nov. 20, 2026; USAF, CIA, DIA, Lockheed, contractor records; DVIDS imagery | matches | PASS | |
| Header comment | Kelly Johnson d. 1990; Reid d. 2021; Inouye d. 2012 | general record | PASS | |

## Packaging (packaging.md)

| Item | Claim | Source checked | Verdict | Replacement (FIX only) |
|---|---|---|---|---|
| Long title | "Why the Man Who Designed the U-2 Believed in Flying Saucers" | D206 p.7 ("definitely believed in the possibility that flying saucers exist"); CBS ("later designed the U-2") | PASS | |
| Thumb A | "U-2 DESIGNER:" / "'SUCH DEVICES EXIST'" / "UNRESOLVED" stamp / "RELEASED NOV. 20, 2026" / chip "U-2, 2024 PHOTO" | D206 p.7 verbatim fragment; D206 file title; Release 08 date; DVIDS 8465347 | PASS | |
| Thumb B | "WHAT / DID HE / SEE?"; tag "LOCKHEED FILE, 1953" | D206 | PASS | |
| Thumb C | "AIR FORCE: 'CLOUD'" / "HIS CREW: NOT A CLOUD"; tag "AIR FORCE FILE, 1953" | D206 p.1, p.9–12 ("his crew" = the Lockheed test crew; acceptable) | PASS | |
| y1 hook | "U-2 DESIGNER: [A SAUCER]" | He wrote "so-called 'saucer'". Without quote marks the hook states it was a saucer | FIX | `U-2 DESIGNER: ["A SAUCER"]` |
| y1 title | "The Man Who Designed the U-2 Saw a 'Flying Saucer'" | quotes present | PASS | |
| y2 hook / title | "A VAULT FOR [EXOTIC TISSUE?]" / "Why Plan a Secret Vault for 'Exotic Material or Tissue'?" | D172 p.9 ("highly secure", "extensively camouflaged") | PASS | |
| y3 hook | "HIS ENGINE [DIED]" | D191 p.5 (his claim) | PASS (headline; the clip itself is attributed) | |
| y3 title | "His Engine Died on a Texas Highway. Then He Saw It." | Lines 53–54 have no attribution in the clip; "It" implies a known object | FIX | `He Told the Air Force His Engine Died. Then He Saw an Object.` |
| s1 | "THE U-2 DESIGNER [SAW THIS]" / "The Engineer Behind the U-2 Watched a 'Saucer' Hover for 3 Minutes" | D206 p.6 ("did not move at all for three minutes"; "hovered stationary for at least three minutes") | PASS | |
| s2 | "ENGINE DEAD. [LIGHTS OUT.]" / "The Night Car Engines Died Near Levelland, Texas" | D191 p.5, p.8 (reported); the clip (lines 52–56) carries attribution | PASS (optional: "...Drivers Said Their Engines Died...") | |
| s3 | "A BURIED VAULT FOR [EXOTIC TISSUE?]" / "A Defense Contractor Planned a Buried Vault for 'Exotic Material or Tissue'" | D172 p.9 | PASS | |
| s4 | "CIA: KEEP IT [FROM THE PRESS]" / "Why the CIA Didn't Want Anyone to Know It Studied Flying Saucers" | D026 p.1; D027 p.2 ("outside knowledge of Agency interest ... must be avoided") | PASS | |
| Clip line ranges | y1 1–2, y2 80–81, y3 53–54, s1 11–16, s2 52–56, s3 80–85, s4 44–47 | LINES indices match the described content | PASS | |
| Description hook | Johnson told the Air Force he was "more firmly convinced than ever"; release Nov. 20, 2026; report, crew statements, "lenticular cloud" | D206 p.1, p.7, p.9–13 | PASS | |

## Summary

- Checked 110 LINES entries, all on-screen graphics, labels and maps, the DISPLAY table, META, and 15 packaging items.
- **19 FIX items, no fabrications.** Every quote presented as verbatim matched its document. Every document crop matches the document and page in its label. All numbers and dates check out, including "almost seventy-three years", Friday Nov. 20, 2026, the Mach 2.5 arithmetic and the 30 and 200+ mile distances. The external facts all hold: U-2/SR-71, the Robertson Panel in January 1953, lenticular clouds, Trinity, Reid and Inouye, Burgess and Lynn, the CBS vault and 2012 claims, and the Parnell quote.
- **Most important fixes:**
  - Line 108 implies Johnson's file was secret until now. The card carries a NARA Blue Book declassification stamp.
  - Line 106 says "a government" wanted secrecy. It was the CIA; the Air Force held a press conference.
  - Lines 55 and 57 leave out the investigating officer's own caveats: only one witness described a landing, and the truck driver's account "cannot be relied upon".
  - Line 78 says "building out", which conflicts with "no public record it was built".
  - Line 34 claims Johnson "did not want" the line read in public, which nothing supports.
  - Technical: MAP_TX bounds cut off Albuquerque. The TOWER and MUGU b-roll labels misdescribe the footage, and the TOWER clip shows a face after about 27 s.
- **Remaining fixes** are wording that states a witness claim or an editorial view as fact: the title card, MAP_CA title, MAP_TX label, and lines 23, 50, 63, 74, 89, 90, 101 and 104. In packaging, the y1 hook and y3 title need the same treatment.
