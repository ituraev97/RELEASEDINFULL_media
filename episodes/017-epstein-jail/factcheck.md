# FILE 017 — "What the Inspector General Found the Night Epstein Died" — independent fact-check

Checker: independent (did not write the script). Date: 2026-11-20.
Primary record: DOJ OIG report 23-085 (June 2023), checked against /home/claude/src17/dl/ig.txt and pg_<N>.txt (printed page = PDF page − 7; ES = executive summary, PDF pp. 2–6).
News: summaries in /home/claude/src17/sources_for_checkers.md, plus two web searches (expert photo review; 2026 DOJ release size).
Every doc crop in /home/claude/src/img/doc/ and every report photo f_*.jpg was opened and compared with its lab= label and page. Thumbnails A/B/C were viewed.
Subtitles were checked by running the real DISPLAY pass (pipeline/finish.py disp(), which applies the pairs in order with str.replace).

Verdicts: PASS = supported as written. FIX = change needed (the exact replacement is given).

## Script lines (1-indexed LINES)

| # | Claim (short) | Verdict | Source | Fix (exact wording) |
|---|---|---|---|---|
| 1 | Nobody checked on him for almost 8 hours; "not once" | PASS | p.5–6 ("no CO had checked on Epstein from approximately 10:40 p.m. … until approximately 6:30 a.m."); ES iii. Fig 5.2 label OK | — |
| 2 | Sign "taped" to a computer a few steps from his cell; "every 30 minutes, as per God" | FIX | p.67: sign "on orange paper that he **hung** on a computer in the SHU officer's area"; cell ~15 ft from the station (p.34, 72) | "A sign hung on a computer a few steps from his cell said rounds every thirty minutes, as per God." |
| 3 | This is the finding of the DOJ Inspector General | PASS | ES iii; c_alone crop = ES, verbatim | — |
| 4 | Nov 16, 2026, three experts in London: in their view, strangulation not suicide | PASS | CNN/WISN Nov 17, 2026 | — |
| 5 | Medical examiner answered the same day: it stands by its ruling (suicide). Stat card | PASS | CNN/WISN (OCME statement Monday, Nov 16); Al Jazeera Nov 18 | — |
| 6 | Who was watching… (Fig 4.8 door of the cell shared Jul 30–Aug 9) | FIX (visual) | Fig 4.8 caption matches. The crop f_door.jpg shows Epstein's inmate ID card **with his photo**, which breaks the episode's own rule (no photos of any person) | Blur or crop the ID card in f_door.jpg (it is also used on line 32). Label may stay. |
| 7 | We read all 128 pages | FIX (label) | The PDF is 128 pages: PASS. But the label renders as "… · P. COVER" | lab = "ACTUAL DOCUMENT · DOJ INSPECTOR GENERAL REPORT 23-085 (JUNE 2023) · COVER" |
| 8 | Intro card | PASS | — | — |
| 9 | Title "THE LAST NIGHT / What the Inspector General Found" | PASS | — | — |
| 10 | Starts with an arrest at an airport | PASS | p.21 | — |
| 11 | Jul 6, 2019, back from France, arrested at Teterboro NJ; charged in NY with sex trafficking of minors | PASS | p.21; c_arrest crop = p.21 | — |
| 12 | Part 1: 2007 Florida deal "that let him serve thirteen months"; judge refused bail, danger + flight risk | FIX | Source notes: "served **under** 13 months". Bail: pp.21–22 (crop c_bail = p.21, OK) | "Part one covered the two thousand seven Florida deal, under which he served less than thirteen months." (DISPLAY "thirteen months"→"13 months" still applies) |
| 13 | MCC, federal jail, Lower Manhattan, 150 Park Row | PASS | p.5, 21 ("federal administrative detention facility") | — |
| 14 | Moved Jul 7 to SHU because of media and inmate awareness; locked in ~23 h/day | PASS | ES ii; p.21; Fig 4.1 label OK | — |
| 15 | Rules: twice-hourly observation, counts through the night, daily cell searches. List title "What BOP policy required" | FIX (graphic) | ES ii: the daily search of 5+ cells is an **MCC New York** requirement, not BOP policy. Counts at 12, 3 and 5 a.m. (p.61). c_rules = ES, OK | List title: "What BOP and jail rules required" |
| 16 | "On his last night, the report found, almost none of them were followed" | FIX | The report never says "almost none". Lieutenant rounds were done (Aug 9 evening; ~4 a.m. Aug 10, p.69–70) | "On his last night, the report found, the rounds, the counts and the cell searches were not done as required." |
| 17 | "Two weeks before he died, there was a warning" | FIX | Jul 23 → Aug 10 = 18 days | "Less than three weeks before he died, there was a warning." |
| 18 | ~1:27 a.m. Jul 23, officers heard noise "from Epstein's cell"; orange cloth around his neck | FIX | p.29: they heard noise "coming from the **M Tier** … the tier where Epstein was housed". Cloth: PASS. Crop c_jul23 = p.29, OK | "At about one twenty-seven in the morning on July twenty-third, officers heard noise from Epstein's tier." |
| 19 | Cellmate said he tried to hang himself; Epstein told an officer he thought the cellmate had tried to kill him | PASS | p.29; c_kill = p.29 | — |
| 20 | Later did not know what happened, did not want to talk about it; psychologist: unclear whether he placed the string or someone else did | PASS | ES iii; p.30; c_unclear = p.30 | — |
| 21 | Disciplinary charges not sustained (insufficient evidence); he asked to be housed with the same cellmate | PASS | ES iii; p.31–32; c_bunkies = p.32 | — |
| 22 | Suicide watch; next day stepped down to psychological observation; said no interest in killing himself | PASS | p.31, 46; c_nointerest = p.46; tag Jul 24 OK | — |
| 23 | Per BOP records: SHU dangerous, noise, hard to work on his case | PASS | p.46. Fig 4.10 label ("later cell, photographed empty") OK | — |
| 24 | Jul 30 back to the unit | PASS | p.31 fn 24; p.47 | — |
| 25 | The condition was a person | PASS | — | — |
| 26 | 12:30 p.m. Jul 30, staff psychologist emailed 70+ employees | PASS | p.32; c_email = p.32 | — |
| 27 | Email quote card | PASS | p.32, verbatim; marked RECREATED and "as quoted by DOJ OIG" | — |
| 28 | Warden picked the cellmate after consulting BOP leadership; supervisors said every SHU officer knew | PASS | ES iii; p.32–33 | — |
| 29 | Aug 8, USMS sent two emails; cellmate to be transferred the next day | PASS | ES iii; c_marshals = ES | — |
| 30 | Aug 9 he left; no new cellmate. Stat "0" | PASS | ES iii; p.2 | — |
| 31 | One of the two on duty said she did not know he needed a cellmate; OIG did not credit it | PASS | p.100; c_credit = p.100 | — |
| 32 | "Others said they had not been told the cellmate was gone, or assumed someone else would handle it" | FIX | p.53–57: lieutenants said they thought he had gone to court; some said they had passed the word on, which no one confirmed. Nobody is recorded as having "assumed someone else would handle it". (Also: f_door ID-card photo, see line 6) | "Others said they had not been told the cellmate was gone, or thought he had only gone to court. Two said they had passed the word on. The Inspector General found no one to confirm it." |
| 33 | Something else had already broken | PASS | — | — |
| 34 | Jul 29, per the FBI, hard drives "in one of the jail's two video recorders" failed | FIX | p.82–83: disk failures in DVR 2 (a DVR 1 also existed). The report never says there were only two | "On July twenty-ninth, according to the F B I's later forensic analysis, hard drives in one of the jail's video recorders failed." |
| 35 | Live feeds continued; about half the cameras, incl. nearly all in and around the SHU, stopped recording | PASS | ES iii; p.109. Fig 6.1 label OK | — |
| 36 | Unnoticed 11 days; Aug 8, replay for an unrelated matter found nothing | PASS | p.82–83, 109; c_eleven = p.109 | — |
| 37 | Next day the technician had the drives; key-holder going off shift at 4; repair postponed | FIX (attribution) | p.84: the whole account is "**according to the Electronics Technician**" | "The next day, a technician got the replacement drives. But, according to him, the officer with the key to the recorder room was going off shift at four, | so the repair was postponed until the following day." |
| 38 | Following day was Aug 10 | PASS | p.84 | — |
| 39 | Sept 2018, approval to replace the camera system; contracts >$730,000; not finished by Aug 2021 | PASS | p.82 (request Sep 6, approved; contracts Sep 21/24, $698,108.99 + $34,089.28); p.109. c_funding = p.82 | — |
| 40 | OIG warnings since 2013; "by its count, 45 of 122 federal prisons needed upgrades" | FIX | p.110: it was the **BOP's** own assessment, not the OIG's count. c_2013 = p.110 | "By the Bureau's own assessment, forty-five of its one hundred twenty-two institutions needed camera upgrades." |
| 41 | "One camera in the unit was still recording"; it covered the common area and the stairs; the cell door not in view | FIX | p.85: the recording camera was at the entrance to the adjacent 10 South unit, looking into the SHU common area (Fig 6.2: "at 10th Floor-South entrance"). Field of view: PASS. Fig 6.2/6.4 labels OK | "So that night, only one camera covering the unit was still recording." |
| 42 | Now, the last day | PASS | — | — |
| 43 | Aug 8 new will; officials learned only after his death | PASS | p.50; c_will = p.50 | — |
| 44 | "Two psychologists told the IG … red flag … probably put back on some kind of watch" | FIX | p.50: only the **Chief** Psychologist said "red flag"; both said he probably would have been placed back on suicide watch or some type of observation. c_redflag = p.50 | "The jail's chief psychologist told the Inspector General it would have been a red flag. | She and a staff psychologist said he would probably have been put back on suicide watch or some kind of observation." |
| 45 | Aug 9, appeals court unsealed ~2,000 pages from a civil suit against Maxwell, later convicted of conspiring with Epstein to sexually abuse minors | PASS | p.50 and fn 31; ES iii; c_unseal = p.50 | — |
| 46 | "Considerable derogatory information"; "media coverage was enormous" | FIX | p.50: "considerable derogatory information" is verbatim, but the report says "**significant** media coverage" | "…contained considerable derogatory information about Epstein, | and there was significant media coverage." |
| 47 | Jail manager let him make an unrecorded, unmonitored call, 6:58–7:19 p.m., against policy | FIX (subtitle only) | Facts PASS: p.58, 108; c_call = p.58. Subtitle renders "7:19 p.m.." (double period) | Change the DISPLAY pair to ("six fifty-eight to seven nineteen p m.", "6:58 to 7:19 p.m.") or drop the period after "p m" in the script |
| 48 | Said he was calling his mother; actually called someone with whom he allegedly had a personal relationship; mother deceased | PASS | ES iii; p.108; c_mother = p.108 | — |
| 49 | Only one cell search documented Aug 9, not his; last search unknown | PASS | ES iii; c_search = ES | — |
| 50 | Excess blankets, linens, clothing; Captain called it a security issue | PASS | ES iii; p.109; c_linens = p.109 | — |
| 51 | Around 8 p.m., back in his cell on L tier, alone | PASS | ES iii; p.85 (7:49 p.m. escort). Fig 4.9 label OK | — |
| 52 | Very few people overnight | PASS | p.56–57 | — |
| 53 | CO worked a 16-hour double, 4 p.m.–8 a.m.; with her until midnight a "materials handler", a warehouse worker on overtime | FIX | Facts PASS: p.5 fn 4, p.57. The job title is "**Material** Handler" (also lines 56, 59). Subtitle renders "8 a.m.." | "…With her until midnight was a material handler, a warehouse worker filling in on overtime." Fix the double period in the DISPLAY pair ("from four p m to eight a m." → "from 4 p.m. to 8 a.m.") |
| 54 | By the 10 p.m. count he had worked 22 hours in a row. Stat "22" | PASS | p.63 (verbatim "22 consecutive hours"); c_22 = p.63 | — |
| 55 | "The video shows it did not happen. The count slip was signed anyway" | FIX | p.63: the OIG relied on video **plus** witness statements and records (the video was poor quality, fn 37); the material handler admitted it. Fig 5.1 label OK | "At ten p m, there was supposed to be a count. | Investigators found it did not happen. | The count slip was signed anyway." |
| 56 | Slip listed "73 + 1"; the handler did not know why | FIX (completeness; title) | p.63–65: a Control Center officer said he wrote "+ 1" himself, "ghost counting" an inmate moved out that day. As written, it suggests a mystery the report explains | "The ten p m slip listed seventy-three plus one inmates. | A control-center officer later said he had added the plus one himself, to account for an inmate moved out that day." |
| 57 | After ~10:40 no rounds: "Not at midnight. Not at three. Not at five." | FIX | 12, 3 and 5 a.m. were the **counts**, not rounds (p.5–6, 65) | "After about ten forty, no thirty-minute rounds at all. | And no counts: not at midnight, not at three, not at five." |
| 58 | 75+ entries recorded rounds that never happened | PASS | p.5–6, 68; c_75 = p.68 | — |
| 59 | At midnight a second handler took over, also on overtime; 1–3 a.m. seated without moving, appeared to be sleeping | FIX (title only) | Facts PASS: p.5 fn 4, p.68. Fig 5.2 label OK | "At midnight, a second material handler took over beside her, also on overtime." |
| 60 | Furniture sales and an Epstein news article; motorcycle sales and sports news | PASS | p.68; c_furniture = p.68 | — |
| 61 | One admitted "dozing off from here and there"; the other said she never slept, motionless = on computer | PASS | p.67 (c_doze); p.72 (c_never) | — |
| 62 | All night the orange sign hung on the computer | PASS | p.67 (Day Watch officer: hanging Aug 9 and 10). Fig 5.2 caption OK | — |
| 63 | Then came breakfast | PASS | — | — |
| 64 | ~6:30 a.m. Aug 10, breakfast; no answer at food slot | PASS | ES iii; c_breakfast = ES | — |
| 65 | Opened door, found him hanged; called for help, compressions; others ~1 min later | PASS | ES iii; p.70–71. Fig 4.12 label OK | — |
| 66 | Lieutenant: one said "we didn't do the rounds, we messed up" | PASS | p.72; c_messed = p.72 | — |
| 67 | 7:10 ambulance to NY Presbyterian Lower Manhattan; 7:36 a.m. pronounced dead | PASS | p.2; c_pronounced = p.2 | — |
| 68 | "In the Inspector General's words, his victims … lost the ability to seek justice…" | FIX | ES iv: the words on screen (c_victims) read "depriving his numerous victims, many of whom were underage girls at the time of the alleged crimes, of their ability…". The spoken line is a paraphrase presented as a quote and drops "alleged" | "His criminal case ended without a trial. | In the Inspector General's words, it deprived his numerous victims, many of whom were underage girls at the time of the alleged crimes, of their ability to seek justice through the criminal justice process." |
| 69 | Aug 11 autopsy: hanging / suicide / no medications or illegal substances | PASS | ES iii–iv; p.2; card marked RECREATED and "as reported by DOJ OIG" | — |
| 70 | Seven years later the ruling is challenged | PASS | 2019→2026 | — |
| 71 | Report published June 2023 | PASS | cover | — |
| 72 | Negligence, misconduct, failures … "in the report's words, provided him an opportunity to take his own life" | FIX | On-screen crop c_findings (ES iv) reads "…provided him an opportunity to **commit suicide**". The spoken "quote" does not match the crop | "…which, in the report's words, provided him an opportunity to commit suicide." |
| 73 | "Not the first time" … widespread disregard of policies meant to keep inmates safe | PASS | ES iv; c_notfirst | — |
| 74 | Two charged with falsifying records; dismissed after DPAs; others not prosecuted | PASS | ES iv; p.6; c_dpa | — |
| 75 | IG went to the video | PASS | Fig 6.5 label OK | — |
| 76 | 10:40 p.m.–6:30 a.m., no one seen entering his tier from the common area | PASS | ES iii; c_noone verbatim | — |
| 77 | No evidence anyone other than the locked-in inmates present; nothing contradicting the FBI's no-criminality finding | PASS | ES iv; c_contradict | — |
| 78 | Staff and three inmates with a line of sight: no one went in or out | PASS | ES iv; p.73; c_sight | — |
| 79 | ME: consistent with suicide by hanging; no defensive wounds, no hand marks, no debris under nails | PASS | ES iv; c_me | — |
| 80 | 8 recommendations; first = cellmate after suicide watch with exceptions; jail "closed" Oct 2021 over unrelated conditions | FIX | p.110: Rec. 1 PASS. p.21, p.109 fn 87: BOP "**temporarily** closed" MCC | "The jail itself had already been temporarily closed, in October twenty twenty-one, over conditions the report calls unrelated." |
| 81 | Two years later the video came back | PASS | June 2023 → July 2025 | — |
| 82 | July 2025, DOJ/FBI two-page memo and the footage | PASS | Axios Jul 7, 2025 | — |
| 83 | Memo: nobody entered any tier ~10:40 p.m.–6:30 a.m.; no incriminating client list. Quote card | PASS | WJLA Jul 8, 2025 (verbatim with leading ellipsis); Axios | — |
| 84 | Gap 11:58:58 → midnight. Stat | PASS | CBS Feb 11, 2026 | — |
| 85 | Bondi: video reset every night, same minute missing | PASS | WJLA Jul 8, 2025 (Cabinet meeting) | — |
| 86 | Sept 2025, Congress released 6 p.m.–7 a.m. version; minute included; nothing apparently unusual; lacked metadata "that would confirm" raw exports | FIX | CBS Sep 3, 2025: metadata "that would **help** confirm". Subtitle renders "7 a.m.." | "…though the files lacked the metadata that would help confirm they were raw exports." Fix the double period in the DISPLAY pair |
| 87 | Feb 2026 CBS: master copy authorized for destruction June 2024; reset explanation "appears never to have been verified" | FIX | CBS Feb 11, 2026: "appears to have been unverified" ("never" is stronger). **Subtitle bug:** renders "June twenty 24" because the ("twenty-four","24") pair runs before ("June twenty twenty-four","June 2024") | Spoken: "…and that the reset explanation appears to have been unverified." DISPLAY: delete the unused ("twenty-four", "24") pair, or move it after the June pair |
| 88 | Nothing changes what the one camera showed: no one entering the tier | PASS | ES iii; p.85. Fig 6.4 label OK | — |
| 89 | Brings us to this week | PASS | — | — |
| 90 | Nov 16, 2026, Middle Temple, London; brother shared the autopsy file with one of them (NYT via CNN) | PASS | CNN/WISN Nov 17, 2026; Al Jazeera Nov 19 | — |
| 91 | "the injuries in the autopsy record are, in their words, most consistent with homicidal strangulation from behind." Quote card | FIX (spoken) | CNN/WISN: the words are "The **ligature marks** are most consistent…". Card is verbatim and labelled as a claim: PASS | "Their claim: the ligature marks are, in their words, most consistent with homicidal strangulation from behind." |
| 92 | They argued no photos were taken of the scene before he was moved | FIX (label) | Claim PASS (Al Jazeera Nov 19; CNN "reportedly"). But f_tier2.jpg is the **Figure 6.7** photo (it carries the "Non-Recording Camera" callout), not Fig 4.6 | lab = FG.format("6.7", "L TIER OF THE SPECIAL HOUSING UNIT") |
| 93 | Not peer-reviewed; review "based on the autopsy file and photographs". List card | FIX (sourcing) | Not peer-reviewed: CNN, PASS. "Photographs" is not in the cited sources (CNN/Al Jazeera summaries mention only the autopsy file and death records). It is supported elsewhere (Boston Globe/AP, Nov 16, 2026: "scientist says photos show…") | Either add that source to the card's source line (S_X + "; AP VIA BOSTON GLOBE (NOV. 16, 2026)") or say "Their review was based on the autopsy file and death records." and change the list item to "Based on the autopsy file and records" |
| 94 | OCME stands by it; FBI found no criminality; IG found no evidence anyone entered his tier | PASS | Al Jazeera Nov 18; ES ii, iii–iv | — |
| 95 | They named no one; one told NYT he has no idea who could be responsible; interested in how it went "so sideways" | PASS | CNN/WISN citing NYT (Freeman) | — |
| 96 | "Two official findings, one new expert challenge … nobody was watching it, and no camera was recording it" | FIX | The officers' station had a view of the cell door (p.71: Thomas "could see Epstein's cell door"); three inmates had a line of sight (p.73); the L-tier camera was live-streaming (ES iv). "Nobody was watching" overstates. The real gap is no rounds and no recording | "…a recording of Epstein's cell door. | Because that night, no one walked the rounds, and the camera on his tier was not recording." |
| 97 | Fight over the files is not over | PASS | — | — |
| 98 | Nov 10, GOP-led Oversight report faults the federal government; Comer: DOJ must interview key witnesses | PASS | NPR Nov 10, 2026 | — |
| 99 | Garcia: "partisan and incomplete" | PASS | NPR Nov 10, 2026 | — |
| 100 | One year since the Transparency Act passed; survivor found her name and number unredacted | PASS | NPR Nov 18, 2026 | — |
| 101 | Next day petition (Massie with Khanna) hit 218, forcing a vote; as early as Dec 2 or 3. Stat 214 D + 4 R | PASS | ABC / Axios Nov 11, 2026 | — |
| 102 | Recap: "a cellmate never assigned"; timeline card | FIX (spoken) | He had a cellmate Jul 30–Aug 9 (p.33). It was the **replacement** that was never assigned. Timeline card PASS (Jul 29, Aug 9, 6:58 PM, 10:40 PM, 6:30 AM, 7:36 AM all check, ES/p.2/p.85) | "…a new cellmate never assigned, \| cameras that weren't recording, \| and rounds that were signed for but never walked." |
| 103 | Viewer question | PASS | Neutral framing | — |
| 104 | Next: the ~3 million pages released in 2026 | PASS | DOJ, Jan 30, 2026 (~3 million pages that day; DOJ cites 3.5 million responsive pages in total). Not in the source notes; confirmed by web search (justice.gov, NPR, Al Jazeera, Jan 30, 2026) | — |

## Packaging

| Item | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| Long title | What the Inspector General Found the Night Epstein Died | PASS | — | — |
| Thumbnail A | "NOBODY CHECKED FOR ALMOST 8 HOURS"; highlight "unmonitored and alone in his cell" (verbatim, ES iv); sign photo labelled "Sign in Epstein's jail unit"; "DOJ REPORT" | PASS | p.5–6; ES iv; p.67 | — |
| Thumbnail B | "WHO WAS WATCHING EPSTEIN?"; "CAMERA NOT RECORDING" on the Fig 6.7 photo | PASS | ES iii; p.84 | — |
| Thumbnail C | "AS PER GOD!!!!" (sign verbatim); "APPEARED TO BE SLEEPING" (verbatim p.68, names barred) | PASS | p.67–68 | — |
| y1 (lines 1–3) | "NOBODY CHECKED FOR 8 HOURS" / "…Almost 8 Hours. Why?" | PASS | p.5–6. (The hook drops "almost"; acceptable for a hook, but "FOR ALMOST 8 HOURS" would be tighter) | — |
| y2 (lines 36–38) | Hook "THE CAMERAS WEREN'T RECORDING"; title "Why Weren't the Cameras Recording…" | FIX | About half the cameras failed, and one camera covering the SHU did record (ES iii). Lines 36–38 alone never say so | Hook: "MOST CAMERAS<br>WEREN'T<br>[RECORDING]". Title: "Why Weren't Most of the Jail's Cameras Recording the Night Epstein Died?" |
| y3 (lines 4–5) | "EXPERTS VS. MEDICAL EXAMINER"; title "Experts Challenge Epstein Ruling. The Examiner Stands By It" | FIX (balance) | Lines 4–5 carry the experts' claim and the OCME reply, but not that the claim is not peer-reviewed, or the FBI/IG findings | Extend the cut to lines 4–5 + 93–94, or add an end card: "Not yet peer-reviewed. The FBI found no criminality; the DOJ Inspector General found no evidence anyone entered his tier." |
| s1 (lines 52–59) | "22 HOURS ON DUTY. THEN THIS"; "The night shift that left Epstein alone, according to the DOJ" | PASS | p.63; ES iv (lines 55–57 and 59 take the fixes above) | — |
| s2 (lines 18–23) | "2 WEEKS BEFORE: A WARNING"; "Two weeks before Epstein died, there was a warning" | FIX | Jul 23 → Aug 10 = 18 days | Hook: "18 DAYS<br>BEFORE:<br>[A WARNING]". Title: "Less than three weeks before Epstein died, there was a warning" |
| s3 (lines 82–88) | "THE MISSING MINUTE" | PASS | CBS Sep 2025 / Feb 2026 (lines 86–87 take the fixes above) | — |
| s4 (lines 24–32) | Hook "'NEEDS A CELLMATE' NONE CAME"; title "The email that said Epstein must not be alone" | FIX | The email said "needs to be housed with an appropriate cellmate" (p.32): "must not be alone" is not a quote. "None came" is wrong: he had a cellmate Jul 30–Aug 9; the replacement never came. The quoted hook fragment is also not contiguous text | Hook: "CELLMATE<br>LEFT.<br>[NO REPLACEMENT]". Title: "The email that said Epstein needed a cellmate" |
| Description legal line | Records/allegations disclaimer | PASS | — | — |

## Notes (no change required)
- **Balance on the cause of death:** handled well overall. The experts' view is attributed ("in their view", "a claim, not an official finding"), the OCME reply, the FBI and the IG findings follow, and Freeman's "no idea who" is included. Fixes 91, 93, 96 and y3 tighten it.
- Crops c_* were all checked: each crop's text matches its page label (P.21, 29, 30, 32, 46, 50, 57, 58, 63, 67, 68, 72, 82, 84, 100, 108, 109, 110, ES, P.2). Staff names are black-barred on every crop that contains them.
- f_tier.jpg (Fig 4.6) is an OCME photo; the orange cloth seen in the full figure is cropped out, which keeps the rule against after-death photos. Keep it that way.
- Line 37: the report also notes the rebuild would have taken ~24 hours regardless (p.84). It is optional context.

## Summary
- Script lines: 104 checked: **73 PASS, 31 FIX** (FIX: 2, 6, 7, 12, 15, 16, 17, 18, 32, 34, 37, 40, 41, 44, 46, 47, 53, 55, 56, 57, 59, 68, 72, 80, 86, 87, 91, 92, 93, 96, 102).
- Packaging: 12 items: **8 PASS, 4 FIX** (y2, y3, s2, s4).
- Total: **81 PASS, 35 FIX.**

## Applied (producer, 2026-11-20)
All FIX items applied before rendering: lines 2, 7, 12, 15 (list title), 16, 17, 18, 32, 34, 37, 40, 41, 44, 46, 47/53/86 (DISPLAY double period: cleanup pair added), 53/56/59 ("material handler"), 55, 56 (mystery removed: "Both of them signed it."), 57, 68, 72, 80, 86, 87 (+ removed the ("twenty-four","24") DISPLAY pair), 91, 93 ("based on the autopsy file and records, not on the body itself"; list item changed), 96, 102. Line 6/32 (f_door with Epstein's ID-card photo) and line 92 (fig. 6.7): images replaced (see legal review — OCME photos removed). Packaging: y2 hook/title, y3 replaced by lines 76-77 (official video findings, balanced), s2 "18 DAYS", s4 hook/title fixed.
Post-check edit (producer, for the gate's "question in the first 5 s"): line 1 reworded to "How was Jeffrey Epstein left unchecked for almost eight hours, on the last night of his life? | Nobody looked in. | Not once." — same facts as the checked line (report: unmonitored from about 10:40 p.m. to about 6:30 a.m.; no rounds after about 10:40 p.m.). B-roll changes after QC (no new claims): lines 85/87 images, lines 98-99 now on-screen quotes of Comer (NPR verbatim) and Garcia ("partisan and incomplete", NPR), line 100 a stat card restating the spoken line.
