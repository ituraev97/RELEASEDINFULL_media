# FILE 017 — Legal review (defamation / privacy / copyright)
Reviewer: independent legal check, 2026-11-20. Scope: episode.py (all LINES, G() graphics, lab= labels, tag= tags, META shorts/yshorts), packaging.md, thumb_A/B/C.jpg, all doc crops in /home/claude/src/img/doc/, report photos /home/claude/src/img/f_*.jpg, thumbnail panels in img/. Record checked against DOJ OIG report 23-085 (ig.txt / pg_N.txt) and sources_for_checkers.md.
Line numbers below = 1-indexed LINES entries (the numbering META uses).

## 1. Named people (spoken, on screen, crops, thumbnails, titles)

| Person | Where | Status | Verdict |
|---|---|---|---|
| Jeffrey Epstein | throughout, door card in f_door | Deceased; charged 2019; earlier conviction (2008) | PASS (no defamation claim for the dead) |
| Ghislaine Maxwell | L42 spoken; c_unseal crop | Convicted (2021); described as "later convicted of conspiring with Epstein to sexually abuse minors" (summary of the court outcome) | PASS |
| Pam Bondi | L85 | Attorney General, speaking in her role; quote matches WJLA/TNND; CBS follow-up attributed | PASS |
| James Comer | L95 | House Oversight Chair, in role; Democratic response follows | PASS |
| Robert Garcia | L96 | Ranking Democrat, in role | PASS |
| Thomas Massie / Ro Khanna | L98 | House members, in role; both parties named | PASS |
| Tova Noel, Michael Thomas (MCC staff) | Not spoken. Crops c_breakfast, c_dpa, c_75, c_furniture, c_doze, c_never, c_messed, c_credit, c_73 and thumb panel p_docC | Charged; charges dismissed after DPAs | PASS: every name is fully black-barred on each crop I opened, and OCR finds no name. **But img/docC.jpg (an unused working file) shows "Noel and Thomas" unbarred → see FIX 10** |
| Virginia Giuffre (victim) | c_unseal crop | Victim; must never be named | PASS (fully barred, both name parts) |
| Count-slip names and signatures | f_slips (Fig. 5.1) | Staff | PASS (blurred in the source; nothing legible) |
| BOP ID card on cell door | f_door (Fig. 4.8) | Inmate 3 | PASS for privacy (blurred in the source; only Epstein's card is legible). But see copyright, FIX 9 |
| Unnamed but identifiable: warden, unit manager ("jail manager"), captain, staff psychologist, responding lieutenant, CO 4, both cellmates, Epstein's brother, the three experts, NPR survivor | various | Not named. Each statement is attributed to the record or to the news outlet | PASS, except the July 23 cellmate (FIX 2, FIX 3) |

## 2. Factual claims about people or identifiable groups

| Line | Claim | Record | Verdict |
|---|---|---|---|
| L1 | Nobody checked on him for almost 8 hours | "no CO had checked on Epstein from approximately 10:40 p.m. … until approximately 6:30 a.m." (p. 5–6) | PASS |
| L4–5 | Experts say strangulation; the medical examiner stands by suicide | Attributed ("in their view"); the medical examiner's response follows straight away | PASS |
| L19 | Cellmate said it was a suicide attempt; Epstein said the cellmate tried to kill him | Record, p. 29. The cellmate is identifiable from public reporting, and the record's balancing facts are missing | **FIX 2** |
| L19 crop c_kill | On screen: Epstein said the cellmate "tried to extort him" and "threatened to beat him" | Epstein's unproven accusation against an identifiable living person. It is not spoken and has no balance | **FIX 3** |
| L20–21 | Epstein later said he did not know what happened; the psychologist was unclear; the disciplinary charge was not sustained; he asked for the same cellmate | Record pp. 30–32 | PASS |
| L26–27 | Email to 70+ staff | p. 32 | PASS |
| L28 | "Several supervisors said every officer in the unit knew the rule." | Record: supervisors "and other witnesses said staff members regularly assigned to the SHU knew" (p. 103). "Every officer" overstates the record | **FIX 5** |
| L31 | One staff member said she did not know; the IG did not credit that | p. 100 | PASS |
| L37 | Officer with the key going off shift at 4 | p. 84 (CO 4, unnamed) | PASS |
| L46 | Manager allowed an unmonitored call in violation of policy | pp. 58, ii | PASS |
| L47 | Called someone "with whom he allegedly had a personal relationship" | Executive summary wording, unnamed | PASS |
| L53–54 | Officer on a 16-hour double shift; materials handler on 22 consecutive hours | pp. 57, 63, footnote 4 | PASS |
| L55 | "The video shows it did not happen." | The OIG relied on video, witnesses and records. The officer told the OIG she did the count, and the OIG did not credit her. Her denial is missing (rule 3) | **FIX 4** |
| L56 | 73 + 1; the materials handler did not know why | p. 63 | PASS |
| L57–58 | No rounds after ~10:40; 75+ false entries | pp. 5–6, 68; admitted in the DPAs | PASS |
| L59 | "appeared to be sleeping" from 1 to 3 a.m. | Verbatim, p. 68, attributed ("the report says") | PASS in the long version. The denial follows in L61. The vertical s1 cuts it off → **FIX 7** |
| L60 | Furniture sales, Epstein article, motorcycle sales, sports | p. 68 | PASS |
| L61 | One admitted dozing; the other said she never slept | pp. 67, 72 (her denial is included) | PASS |
| L65 | "We didn't do the rounds, we messed up" | p. 72, attributed to the lieutenant | PASS |
| L67 | "his victims, many of them underage girls at the time" | The record says "at the time of the alleged crimes". The 2019 charges were never tried (rule 3) | **FIX 6** |
| L68 | Autopsy: hanging / suicide / toxicology | Executive summary | PASS |
| L71 | Charged with falsifying records; dismissed after DPAs; others not prosecuted | p. iii, 6 | PASS (the dismissal is stated) |
| L73–76 | No one entered the tier; no evidence contradicting the FBI; inmates' line of sight; the medical examiner's findings | pp. ii–iv | PASS |
| L83–88 | Memo, missing minute, Bondi, CBS on metadata and master copy | Attributed to Axios/TNND/CBS | PASS |
| L90–93 | Brother shared the autopsy file; experts' claim; no photos; not peer-reviewed | CNN/WISN, Al Jazeera; the quote card says "a claim, not an official finding" | PASS |
| L94 | Official findings set against the claim | Medical examiner, FBI, IG | PASS |
| L95 | "They did not name anyone." + Freeman quote | "They did not name anyone" is not in the sources. Also, the strongest record finding that clears the two identifiable staff of any role in the death is missing from the dispute section | **FIX 1** |
| L99–101 | Oversight report: Comer / Garcia; survivor (unnamed); petition: Massie / Khanna | NPR, ABC, Axios | PASS (balanced) |
| L103 | CTA: "Do you think the official investigations answered how he died?" | Asks about the investigations, not a person | PASS. Note: moderate comments that name staff or the cellmate as killers |

Rule 7 check (homicide claim): with FIXES 1–3 applied, nothing suggests that any identifiable person harmed Epstein. Without FIX 1, the episode lays out in detail the two staff members' misconduct, followed by "homicidal strangulation from behind". The audience can identify both staff members from public reporting, and the record's exculpatory finding about them (OIG p. iii) is never said.

Suicide handling: the spoken text says only "found him hanged" or "hanging" (official wording). There is no method detail beyond the record. Crops c_linens ("improvised noose") and c_me ("convulsing from hanging") are verbatim record. They are acceptable, but recropping c_me to end at "…would have evidenced a fight" would lower the self-harm-policy risk (optional).

## 3. Images and copyright

| Asset | Source per report | Verdict |
|---|---|---|
| All doc crops (c_*.jpg, cover) | DOJ OIG text, U.S. government work | PASS |
| f_sign (Fig. 5.2), f_slips (Fig. 5.1) | BOP | PASS |
| f_entry 4.1, f_empty 4.9, f_cell 4.10, f_station 4.11, f_station2 4.12, f_map 6.1, f_cam 6.2, f_still 6.4, f_still2 6.5 | DOJ OIG / BOP | PASS (no people visible) |
| **f_tier / f_tier2 (Fig. 4.6), f_door (Fig. 4.8), f_nonrec (Fig. 6.7), thumbnail B corridor.jpg (= Fig. 6.7)** | **Photographs by NYC Office of Chief Medical Examiner (OCME)**: the report credits "Source: OCME" / "photograph taken by the Office of the Chief Medical Examiner, City of New York". City works are NOT public domain under 17 U.S.C. §105, and appearing in a federal report does not make them public domain. The labels "ACTUAL PHOTO · DOJ INSPECTOR GENERAL REPORT" also misstate the source | **FIX 9** |
| DVIDS b-roll, labelled, "THE JAIL IS NOT SHOWN" | DoD | PASS |
| RECREATED graphics (email, autopsy) | Own work | PASS |
| No photos of any person, no news footage | — | PASS |
| img/docC.jpg | Unbarred staff names (not used in any 017 build file) | **FIX 10** |

## 4. Packaging

| Item | Verdict |
|---|---|
| Long title "What the Inspector General Found the Night Epstein Died" | PASS |
| Thumb A: "NOBODY CHECKED / FOR ALMOST 8 HOURS", doc highlight "unmonitored and alone in his cell" | PASS (record wording) |
| Thumb B words "WHO WAS WATCHING EPSTEIN?" / "CAMERA NOT RECORDING" | Words PASS. Image is an OCME photo → FIX 9 |
| Thumb C: "AS PER GOD!!!!" / "APPEARED TO BE SLEEPING" | PASS. Both are verbatim from federal records, in quotation marks, attributed "DOJ REPORT, 2023". Names are barred on the panel and no person is identified. A fair, true report of an official report (privileged). Safe as built. Do not add names, faces or "GUARDS" to it |
| y1 (L1–3) "NOBODY CHECKED FOR 8 HOURS" / title | PASS |
| y2 (L36–38) cameras / title | PASS |
| y3 (L4–5) "EXPERTS VS. MEDICAL EXAMINER" / "Experts Challenge Epstein Ruling. The Examiner Stands By It" | PASS (attributed, balanced by the medical examiner, accuses no one) |
| s1 (L52–59) hook "22 HOURS ON DUTY. THEN THIS" / title | **FIX 7**: the cut ends on "appeared to be sleeping" without either staff member's account, and "THEN THIS" implies something sinister |
| s2 (L18–23) | PASS once FIX 2 is applied (the balance sits inside L20) |
| s3 (L82–88) | PASS |
| s4 (L24–32) title "The email that said Epstein must not be alone" | **FIX 8** (the email said "needs to be housed with an appropriate cellmate") |
| Description legal line | PASS. Suggested addition (non-blocking): "The official ruling is suicide; the claim by three experts is disputed by the NYC medical examiner. If you or someone you know is struggling, call or text 988 (U.S.)." |

## 5. FIX items (exact replacements)

**FIX 1 — L95 (X. The Dispute), rule 7.** Replace
`"They did not name anyone. | One of them told The New York Times he has no idea who could be responsible, | and that what interests him is how this went so sideways."`
with
`"One of them told The New York Times, as cited by CNN, that he has no idea who might have been responsible, | and that what interests him is how this went so sideways. | And the Inspector General's report is specific about the two staff members on duty: | on the recorded video, it did not see either of them rise from their seats or approach the cell block that night, | and it found their reaction that morning consistent with their being unaware of any harm to Epstein."`
(Record: OIG report p. iii, executive summary.)

**FIX 2 — L20 (July 23 cellmate), rules 3/7.** Append to the end of L20's text:
` | Another inmate on the tier backed up parts of the cellmate's account, the report says, | and a prison investigation could not determine whether Epstein had harmed himself or been assaulted.`
(Record: pp. 30, 103: "Inmate 2 corroborated several aspects of Inmate 1's account"; "SIS … was unable to determine whether Epstein had harmed himself or had been assaulted.")

**FIX 3 — crop c_kill (L19).** Recrop so the crop ends at "…that he thought his cellmate had tried to kill him." Remove the sentences about extortion, threats to beat him, and telling his lawyers.

**FIX 4 — L55 (10 p.m. count), rule 3.** Replace L55's text with
`"At ten p m, there was supposed to be a count. | Based on the video, witness statements and records, the Inspector General found it did not happen. | The officer told investigators she did the count; the report did not credit that. | The count slip was signed anyway."`

**FIX 5 — L28.** Replace `"Several supervisors said every officer in the unit knew the rule."` with `"Supervisors and other witnesses said staff regularly assigned to the unit knew Epstein needed a cellmate."`

**FIX 6 — L67.** Replace `"his victims, many of them underage girls at the time,"` with `"his numerous victims, many of them underage girls at the time of the alleged crimes,"`

**FIX 7 — vertical s1.** In META.shorts s1, change `lines=[52, 59]` to `lines=[52, 61]` (~100 s with FIX 4, which still fits TikTok's 62–110 s), so both staff members' own accounts (dozing / "never slept") are included. Change hook to `"22 HOURS<br>ON DUTY.<br>[NO COUNT DONE]"`. Update packaging.md s1: hook "22 HOURS ON DUTY. NO COUNT DONE".

**FIX 8 — s4 title (packaging.md).** `"The email that said Epstein must not be alone"` → `"The email that said Epstein needed a cellmate"`.

**FIX 9 — OCME (NYC) photographs, rule 6.** Remove every OCME-sourced photo and use DOJ OIG/BOP figures instead:
- L6 f_door → `I("f_cam", kb="in", focus=[0.62,0.45], lab=FG.format("6.2", "LOCATION OF THE ONE RECORDING SHU CAMERA"))`
- L17 f_tier → `I("f_station", kb="in", focus=[0.6,0.45], lab=FG.format("4.11", "VIEW OF EPSTEIN'S CELL DOOR FROM THE OFFICERS' STATION"))`
- L24 f_tier → `I("f_entry", kb="out", focus=[0.5,0.5], lab=FG.format("4.1", "ENTRANCE TO THE SPECIAL HOUSING UNIT, NINTH FLOOR"))`
- L32 f_door → `I("f_cell", kb="out", focus=[0.62,0.5], lab=FG.format("4.10", "INTERIOR OF EPSTEIN'S LATER CELL, PHOTOGRAPHED EMPTY"))`
- L38 f_nonrec → `I("f_map", kb="in", focus=[0.4,0.45], lab=FG.format("6.1", "SHU CAMERA LOCATIONS AND RECORDING STATUS ON AUGUST 10, 2019"))`
- L78 f_tier2 → `I("f_station2", kb="in", focus=[0.6,0.45], lab=FG.format("4.12", "THE OFFICERS' STATION SEEN FROM EPSTEIN'S CELL"))`
- L92 f_nonrec → `I("f_station", kb="out", focus=[0.6,0.45], lab=FG.format("4.11", "VIEW OF EPSTEIN'S CELL DOOR FROM THE OFFICERS' STATION"))`
- Remove "f_tier", "f_tier2", "f_door", "f_nonrec" from META imgs.
- Thumbnail B: replace img/corridor.jpg with /home/claude/src/img/f_station.jpg (Fig. 4.11, DOJ OIG photo), chip `"EPSTEIN'S CELL DOOR · DOJ PHOTO"`. Or use f_map (Fig. 6.1 schematic), chip `"CAMERAS NOT RECORDING"`. Keep "WHO WAS WATCHING EPSTEIN?". Update packaging.md: "(photo: view of Epstein's cell door from the officers' station, report fig. 4.11)".

**FIX 10 — housekeeping.** Delete /home/claude/releasedinfull_media/episodes/017-epstein-jail/img/docC.jpg. "Noel and Thomas" is legible and unbarred in it. It is unused in 017, but it must not be picked up for a thumbnail or upload. (episodes/016-black-triangle/thumb_bold.json references its own img/docC.jpg; not in scope.)

## Overall
FIX (10 items)

## Applied (producer, 2026-11-20)
1 L95 replaced with the suggested text (IG: staff never rose/approached; reaction consistent with being unaware). 2 L20 appended "Another inmate on the tier backed up parts of the cellmate's account, the report says." (the second half was not added: a disciplinary finding of insufficient evidence is already stated in L21). 3 c_kill recropped to end at "tried to kill him." 4 L55 replaced (IG finding + officer's account not credited). 5 L28 replaced. 6 L68 replaced with the report's own wording incl. "alleged crimes". 7 s1 now lines 52-61, hook "22 HOURS / ON DUTY. / NO COUNT DONE". 8 s4 title "The email that said Epstein needed a cellmate". 9 All OCME (NYC) photos removed (figs. 4.6, 4.8, 6.7): replaced by DOJ OIG/BOP figures 6.2, 4.11, 4.1, 4.10, 6.1, 4.12; thumbnail B now uses fig. 4.11. 10 img/docC.jpg, docA.jpg deleted. Optional: 988 line and official-ruling line added to the description.
