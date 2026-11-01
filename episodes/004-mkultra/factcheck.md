# FILE 004 — MKUltra: The Files That Survived · FACT-CHECK

Date: 2026-11-01
Checker: independent (did not write the script)
Script checked: episodes/004-mkultra/script_for_factcheck.md (68 lines). The writer's research.md was treated as claims to verify, not as proof.

## Sources actually opened
- 1977 Senate joint hearing, "Project MKULTRA, the CIA's Program of Research in Behavioral Modification" (Aug. 3, 1977): /home/claude/dl/hp.txt (paged text), read in full for pdf pp. 7–13 (Kennedy opening, Turner prepared statement, start of Turner testimony), pp. 22–23, Q&A at hp.txt lines 878–900 ("several Freedom of Information Act requests… any conceivable connection… Very late in March"), Gittinger testimony (the "Manchurian Candidate" passage), Appendix A = Church Committee Final Report Book I pp. 388–406 (pdf pp. 71–89), Appendix B memo of June 22, 1977 (pdf p. 106). Grep of the whole hearing for "assassin", "Manchurian", "programm".
- CIA Inspector General, "Report of Inspection of MKULTRA," July 26, 1963 (CIA release 2019/04/03, C06767515): /home/claude/dl/ig.txt — cover memo paras. 1–9, paras. 12–14, 17, 18, 30, the "Files are notably incomplete" passage, and the annex memos (6%, Apr. 3 / Apr. 13, 1953).
- Every document image used on screen, viewed: h72a, h8a, ig38, ig2a, h74b, h74a, ig16a, h77a, h78a, h84a, ig1, h84b, h87a, h106a, h9a, h1, h9b, h11a (/home/claude/src/img/doc/).
- Every b-roll shot: frames pulled with ffmpeg at the listed time, +3 s and +6 s (17 shots, 51 frames), plus extra checks on dv950025 (4.5–7.0 s and 157–161.3 s) and the opening frames and container metadata of dv1026930/dv1026934. Labels compared with /home/claude/src/rights.json.
- Ford Library, Presidential Handwriting File, July 21, 1975 meeting summary (phw19750721-01.pdf), via WebFetch.
- Ford Library, S. 3035 enrolled bill file and Oct. 12, 1976 signing statement (1669605.pdf), via WebFetch.
- Baltimore Sun story (Matthew Hay Brown), republished by The Bulletin (Bend), Dec. 18, 2012 (bendbulletin.com/?p=2784), via WebFetch.
- DVIDS page for video 1026930: the fetch was blocked (permission prompt timed out). A web search turned up nothing that names the service branch.
- pipeline/build.py (to see how a b-roll start time is used: `clean_start` can move the start by up to about ±1.5 s to avoid source cuts).

## Verdicts by script line

**1. NOTE.** Correct as written. Church Report p. 389: records "destroyed by Technical Services Division personnel acting on the verbal orders of Dr. Sidney Gottlieb, Chief of TSD". Helms (p. 403): "he was retiring and that I was retiring". Optional: in 1973 the unit was formally the Office of Technical Service. Turner, p. 8, calls Gottlieb "the then retiring Chief of the Office of Technical Service". "Technical Services Division" follows the Church Report and is acceptable.

**2. OK.** The quote card matches Church Report pp. 403–404 word for word ("…came to me and said that he was retiring and that I was retiring and he thought it would be a good idea if these files were destroyed"). The date matches fn. 75, "Richard Helms testimony, 9/11/75, p. 5." The image is the matching page.

**3. OK.** Church Report p. 389: "Dr. Gottlieb has testified, and former Director Helms has confirmed, that in ordering the records destroyed, Dr. Gottlieb was carrying out the verbal order of then DCI Helms." Image h72a shows this exact passage.

**4. NOTE.** Accurate as rhetoric, since Kennedy (p. 7) says "We believed that the record, incomplete as it was, was as complete as it was going to be." But the "story" did not end: MKULTRA became public in 1975 (Turner p. 8). Optional rewording: "For four years, it looked as if those records were gone for good." The b-roll (Capitol, 2014) shows the Capitol over the Mall, matching the label.

**5. OK.** Turner p. 9: Retired Records Center "outside of Washington"; an employee "responding to Freedom of Information Act requests". Turner p. 13: "some seven boxes"; "what should have been filed by the branch itself was filed by the Budget and Fiscal Section". Q&A: "Very late in March". The "MARCH 1977" and "filed in the wrong section" stat card is supported.

**6. OK.** Image h8a is the start of Turner's prepared statement and matches its label.

**7. OK.** Intro card.

**8. OK.** Title card.

**9. OK.** Chapter card.

**10. OK.** Church Report pp. 389–390: proposal from "the Assistant Deputy Director for Plans, Richard Helms"; fn. "Memorandum from ADDP Helms to DCI Dulles, 4/3/53"; "approved by the DCI on April 13, 1953". "Covert operations directorate" is an acceptable plain-language name for the Directorate of Plans. Image ig38 is the Dulles memo to the DD/A dated APR 13 1953, "Project MKULTRA – Extremely Sensitive Research and Development Program", and matches its label.

**11. OK.** The quote matches Church Report p. 390 word for word ("Research to develop a capability in the covert use of biological and chemical materials."), from Tab A of the Apr. 3, 1953 Helms memo.

**12. NOTE.** "Umbrella project" comes from Turner p. 8. Church Report p. 391 says grants were made "under ostensible research foundation auspices, thereby concealing the CIA's interest from the specialist's institution." Optional: "went out under the cover of research foundations" is closer to "ostensible". The b-roll is honest: the Treasury frames show "THE TREASURY DEPARTMENT" on the frieze, and the White House frames show the north facade. Neither shows gore.

**13. OK.** Church Report p. 404: "From the inception of MKULTRA normal Agency procedures were waived… six percent of the research and development budget of TSD would be expended 'without the establishment of formal contractual relations' because contracts would reveal government interest." Image ig38, para. 4, shows the "6%… without the signing of the usual contracts" text.

**14. OK.** The quote matches Church Report p. 404 word for word ("are most reluctant to enter into signed agreements of any sort which connect them with this activity"). The spoken "Researchers in this field" paraphrases the source's subject, "qualified individuals in the field". The words after "he wrote" match the source.

**15. OK.** IG cover memo para. 7, shown on image ig2a: "The concepts involved in manipulating human behavior are found by many people both within and outside the Agency to be distasteful and unethical." This is word for word, and 1963 is ten years after 1953.

**16. OK.** Chapter card.

**17. OK.** Church Report p. 390: "first, the search for materials suitable for study; second, laboratory testing on voluntary human subjects in various types of institutions; third, the application of MKULTRA materials in normal life settings." The sublabels are supported by pp. 390–391 (universities, pharmaceutical houses, hospitals; unwitting nonvolunteer subjects in normal life settings).

**18. FIX (b-roll label).** The narration is OK (Church Report p. 390, "standing arrangements with specialists in universities, pharmaceutical houses, hospitals, state and federal institutions, and private research organizations"). The problem is the label "AIR FORCE FLIGHT OVER WASHINGTON, D.C., 2026" on dv1026930 and dv1026934. The DVIDS title in rights.json is "From the Cockpit: America 250 Over Washington, D.C." and does not name the service branch. Nothing in the frames identifies the branch either: they show a fighter cockpit and a pilot in a flight suit with a U.S. flag patch. The DVIDS page could not be checked (fetch blocked). There is no gore.
Replacement label, for every use of these two clips: `B-ROLL · MILITARY JET FLIGHT OVER WASHINGTON, D.C., 2026`. Keep "AIR FORCE" only if someone opens dvidshub.net/video/1026930 and /1026934 and the credited unit is a U.S. Air Force unit.

**19. OK.** Church Report p. 391, shown on image h74b: NIMH Addiction Research Center, Lexington, Kentucky, "a prison for drug addicts serving sentences for drug violations"; "volunteer prisoners"; "As a reward for participation in the program, the addicts were provided with the drug of their addiction." The line is attributed ("According to the Senate report").

**20. OK.** Church Report p. 391: "LSD was one of the materials tested… The final phase of LSD testing involved surreptitious administration to unwitting nonvolunteer subjects in normal life settings by undercover officers of the Bureau of Narcotics acting for the CIA." Image h74a matches.

**21. FIX (spoken words presented as a quote do not match).** The quote card is word for word (Church Report p. 391, quoting IG 1963 p. 21: "that testing of materials under accepted scientific procedures fails to disclose the full pattern of reactions and attributions that may occur in operational situations"). The narration, however, presents altered wording as the report's own words: "it said, failed to disclose the full pattern of reactions that may occur in real operations". Here "failed" replaces "fails", "and attributions" is dropped, and "in real operations" replaces "in operational situations". The card on screen shows the real wording at the same moment, so the gap is visible.
Replacement SPOKEN: "The Senate report quotes the rationale. Testing under accepted scientific procedures, it said, fails to disclose the full pattern of reactions and attributions that may occur in operational situations."

**22. OK.** Word for word with Church Report p. 391 / IG para. 12 ("the effectiveness of the substances on individuals at all social levels, high and low, native American and foreign, is of great significance"). Image h74a shows the passage (italics are "[Emphasis added.]" by the committee).

**23. OK.** Turner p. 11: "some of the unwitting drug testing was carried on in safehouses in San Francisco and New York City." The map points are correct: Lexington's Addiction Research Center (Church Report p. 391) and Washington.

**24. OK.** IG report para. 17 (report p. 14), on image ig16a: "Present practice is to maintain no records of the planning and approval of test programs." Turner also quotes it on p. 9. In context it refers to covert testing, which is where the script places it.

**25. OK.** IG para. 13, quoted in Church Report p. 400: "Their subjects are seldom accessible beyond the first hours of the test… In a number of instances, however, the test subject has become ill for hours or days". Attributed ("According to the same report").

**26. OK.** Chapter card.

**27. OK.** Church Report p. 395: "On November 18, 1953, a group of ten scientists from the CIA and Camp Detrick attended a semi-annual review and analysis conference at a cabin located at Deep Creek Lake, Maryland." The map labels (Camp Detrick in Frederick, Md.; Statler Hotel in New York; cabin meeting Nov. 18–19, 1953) are consistent with pp. 395–397. Locations are marked approximate.

**28. OK.** Church Report p. 394: "a civilian employee of the Army". Church Report p. 395: "an expert in aerobiology". The tag "NOV. 19, 1953" is the dosing date (p. 394).

**29. NOTE.** The facts are correct. Church Report p. 394: "approximately 70 micrograms of LSD in a glass of Cointreau he drank on November 19, 1953. The drug had been placed in the bottle by a CIA officer, Dr. Robert Lashbrook". Church Report p. 396: "According to Gottlieb, a 'very small dose' of LSD was placed in a bottle of Cointreau which was served after dinner… About twenty minutes after they finished their Cointreau, Gottlieb informed the other participants that they had received LSD." Optional: image h78a (p. 395) shows the conference paragraph, not the Cointreau passage, which is on p. 396 (pdf p. 79). Use a crop of pdf p. 79 if available. The current label is still honest.

**30. FIX (ambiguous title, wrong for listeners).** Source, Church Report p. 396: "Neither the Chief of TSS nor the DDP specifically authorized the experiment in which Dr. Olson participated." TSS is the Technical Services Staff. Spoken as "the chief of Gottlieb's staff", it will be heard as "Gottlieb's chief of staff", a subordinate. The person meant is the head of the whole Technical Services Staff, Gottlieb's superior. The report also says Gottlieb secured "the approval of his immediate supervisor" (pp. 395–396).
Replacement SPOKEN: "The Senate report found that neither the chief of the C I A's Technical Services Staff, where Gottlieb worked, nor the head of the covert operations directorate, had specifically authorized that experiment."

**31. FIX (b-roll label only, same as line 18).** The narration is OK. Church Report p. 394: "Shortly after this experiment, Olson exhibited symptoms of paranoia and schizophrenia. Accompanied by Dr. Lashbrook, Olson sought psychiatric assistance in New York City from a physician, Dr. Harold Abramson, whose research on LSD had been funded indirectly by the CIA." (Ruwet also went on the first trip, p. 397. Omitting him is not an error.)
Replacement labels for dv1026934 @15.0 and dv1026930 @33.0: `B-ROLL · MILITARY JET FLIGHT OVER WASHINGTON, D.C., 2026`, unless the DVIDS credit is verified as Air Force.

**32. FIX (date of death).** The script says the fall happened "On November twenty-seventh, nineteen fifty-three". The Church Report summary sentence (p. 394, image h77a) does say Olson "died on November 27, 1953". But the same report's detailed account (p. 397) says: "At approximately 2:30 a.m. Saturday, November 28, Lashbrook was awakened by a loud 'crash of glass'… he fell to his death from the window of our room on the 10th floor." President Ford's Oct. 12, 1976 signing statement and the S. 3035 file also give the date of death as November 28, 1953. Stating Nov. 27 flatly is contradicted by the detailed record and by the federal documents.
Replacement SPOKEN: "In the early hours of November twenty-eighth, nineteen fifty-three, while in New York for treatment, Frank Olson fell to his death from a tenth-floor window of the Statler Hotel."
Also: during this line, do not hold or zoom on the "who died on November 27, 1953" sentence in h77a. Focus the crop on its last sentence, "While in New York for treatment, Olson fell to his death from a tenth story window in the Statler Hotel." The treatment is non-graphic, which is acceptable.

**33. OK.** The quote matches Church Report p. 398 word for word ("did not notify the Olsons of the circumstances surrounding his demise"). The spoken "worked to make sure his family received death benefits" matches "made a substantial effort to ensure that his family received death benefits".

**34. OK.** Turner p. 8: "During the Rockefeller Commission and Church Committee investigations in 1975, the cryptonym became publicly known when details of the drug-related death of Dr. Frank Olson were publicized." 1953 plus 22 years is 1975. The b-roll (Capitol, 2014) is honestly labelled.

**35. OK.** Ford Library meeting summary, July 21, 1975 (2:00 p.m., Oval Office): "The President met with Mrs. Frank Olson and her three children… apologized on behalf of the U. S. Government for the circumstances of Dr. Frank Olson's death". Attributed ("According to the White House summary"). The b-roll is the White House north facade (2014), labelled correctly.

**36. OK.** S. 3035 file: $187,500 each to four survivors, $750,000 in total. Signing statement released Oct. 12, 1976: "I am today signing into law S. 3035, a private bill for the relief of the survivors of Dr. Frank R. Olson"; "The administration of the drug occurred without his prior knowledge and would appear to have been a proximate cause of his death." The card's quoted fragment is word for word.

**37. FIX (b-roll start shows a DVIDS slate).** The narration is OK. The Baltimore Sun (M. H. Brown), Dec. 18, 2012, says the sons Eric and Nils Olson sued the CIA, claiming their father was murdered (Eric Olson: "our father was killed in (CIA) custody"). It is correctly framed as the family's claim.
The defect: dv950025 shows a full-screen text slate until about 5.0 s ("Streets of D.C. – 60th Presidential Inauguration / Producer: Tech. Sgt. … / Location: Washington, D.C. / Date: January 20, 2025 / VIRIN …"). Measured frame luminance is about 17.8 (black slate) from 4.5 to 4.95 s and about 119 (picture) from 5.0 s. A start at 4.5 s puts about 0.5 s of slate on screen, including an individual's name. Also, build.py's `clean_start` may move the start up to about 1.5 s earlier to avoid the 5.0 s cut, which would show even more slate.
Replacement: `C("dv950025", 6.5, lab=CAP25)` instead of `C("dv950025", 4.5, …)`, and confirm in the rendered segment that frame 1 is picture.
NOTE on the same line: the second shot (@153.0) is honest (the Capitol seen down Pennsylvania Ave., inauguration security fencing, Guard members in hi-vis moving barriers, no injuries). The clip is only 161.5 s long, so if this shot needs more than about 8 s, build.py will clamp it earlier. Check the render.

**38. OK.** Chapter card.

**39. NOTE.** Correct in substance. Church Report pp. 392 and 401: during the 1963 IG survey of TSD the project was learned of, and "On May 24, 1963, the DDP advised the Inspector General that he had briefed the Director… According to the Inspector General, the DDP said that 'the Director indicated no disagreement and therefore the "testing" will continue.'" Image h84a shows it. Optional, for a precise chain of who said what: "And, according to the Inspector General, he said the Director indicated no disagreement, and therefore the testing will continue." Also optional: p. 406 names that DDP as Helms ("In May of 1963, DDP Helms told the Inspector General…"), which would set up "Helms pushed back" in line 41.

**40. OK.** Church Report p. 401: the IG "recommended the termination of the surreptitious administration project. The project was suspended following the Inspector General's report." Image ig1 is the IG cover memo dated 26 July 1963, "Report of Inspection of MKULTRA", and matches its label.

**41. OK.** The quote matches Church Report p. 401 word for word (image h84b). The role line matches the source: memo to the DDCI dated Dec. 17, 1963 ("Memorandum from DDP Helms to DDCI Carter, 12/17/63").

**42. OK.** Church Report p. 401: "the program would only be 'pro forma' resulting in a 'false sense of accomplishment and readiness.'" Image h84b matches.

**43. FIX (end date stated as fact; sequence error).**
(a) "MKUltra itself ran until nineteen sixty-four" is the CIA's 1977 account (Turner pp. 8, 12: "conducted from 1953-1964", "termination of this activity in 1964"). The Church Report, which this line otherwise cites as "The Senate found", says on p. 392: "According to the CIA, the project was decreased significantly each budget year until its complete termination in the late 1960s." The sources disagree, so the 1964 end date must be attributed.
(b) "By then, the Inspector General had counted 144 projects" places the count in 1964. The IG counted them in the July 1963 report (para. 30: "TSD has initiated 144 projects relating to the control of human behavior… during the ten years of operation of the MKULTRA program").
Replacement SPOKEN: "The Senate found that the covert testing in the United States was halted in nineteen sixty-three. By then, the Inspector General had counted one hundred forty-four projects related to the control of human behavior. According to the C I A, MKUltra itself ended in nineteen sixty-four."
Replacement timeline event 4: `{"y": "1964", "t": "Program ends (CIA account)"}`.

**44. OK.** The quote matches IG report p. 23 word for word, as quoted in Church Report fn. 77 (p. 404): "Files are notably incomplete, poorly organized, and lacking in evaluative statements…". The spoken paraphrase "A substantial part of the record seemed to rest in the memories…" fits "A substantial portion of the MKULTRA record appears to rest in the memories of the principal officers". It is not presented as a direct quote.

**45. OK.** Chapter card.

**46. NOTE.** The quote card matches Church Report pp. 403–404 word for word. In the narration, Helms's words ("assisted us") come straight after narrator paraphrase without a marker. Optional: "So, in his words, they got rid of the files, so that anybody who assisted us…".

**47. OK.** Church Report p. 404 (image h87a): waiver of CSI 70-10, "retirement of inactive records"; "The heart of this judgment is to ensure that the complete story can be reconstructed in later years…"

**48. OK.** The quote matches Church Report p. 404 word for word (image h87a). The spoken line paraphrases "impossible for the Select Committee to determine the full range and extent…" and is attributed.

**49. OK.** Church Report p. 404, fn.: "at least one assistant to Dr. Gottlieb protested against the document destruction". Attributed. (The footnote is not in the h87a crop. The label is still honest.)

**50. OK.** Chapter card.

**51. OK.** Turner Q&A: "All this started with several Freedom of Information Act requests… through every file with which the branch that conducted this type of activity had any conceivable connection." The June 22, 1977 memo (pdf p. 106, image h106a): "As a result of John Marks FOIA request (F-76-374)… the OTS material in the Retired Records Center was searched." John Marks is named in the Senate record, so naming him is acceptable. The image matches its label.

**52. OK.** Q&A: "Very late in March, he discovered these seven boxes." Turner p. 9 (image h9a): "sent to the Retired Records Center in 1970 by the Budget and Fiscal Section… The reason for this departure from normal procedure is not known."

**53. OK.** The quote matches Turner's prepared statement p. 9 word for word ("the material escaped retrieval and destruction in 1973 by the then-retiring Director of the Office"). Turner was DCI.

**54. OK.** A joint hearing of the Select Committee on Intelligence and the Subcommittee on Health and Scientific Research, Aug. 3, 1977 (title page h1, matching its label). The b-roll (Capitol, 2014) is honest.

**55. OK.** Turner p. 9 (image h9b): "the recovered folders are finance folders. The bulk of the material in them consists of approvals for advance of funds, vouchers, accountings, and the like". Turner p. 10: the new detail includes "the names of previously unidentified researchers and institutions".

**56. NOTE.** Turner p. 11: "185 non-government researchers and assistants… the 149 subprojects… 80 institutions". The stat card is correct. Optional: viewers will have just heard "144 projects" (IG, 1963) in line 43. A brief clause such as "in the recovered files, there were 149 subprojects" avoids the appearance of a contradiction.

**57. OK.** Turner p. 11: "44 colleges or universities, 15 research foundations or chemical or pharmaceutical companies and the like, 12 hospitals or clinics (in addition to those associated with universities), and 3 penal institutions." 44 + 15 + 12 + 3 = 74, not 80. The script never says the four categories add up to 80, and Turner's "include" allows for others. The card's kicker "THE 80 INSTITUTIONS" above four rows could still suggest they are the whole set. Optional: change the kicker to "AMONG THE 80 INSTITUTIONS". This does not change the verdict.

**58. OK.** Word for word with Turner p. 11: "Most of the people and institutions involved are not aware of Agency sponsorship." Attributed.

**59. OK.** Turner p. 11: "a contribution of $375,000 to a building fund of a private medical institution… made through an intermediary, which made it appear to be a private donation. As a private donation, the contribution was then matched by federal funds."

**60. OK.** Word for word with Kennedy, hearing p. 7: "The Central Intelligence Agency drugged American citizens without their knowledge or consent."

**61. OK.** Chapter card.

**62. OK.** The approval is documented on ig38 and in IG cover memo para. 5. The program's scope is in IG para. 3 and Turner p. 8 ("research on drugs and behavioral modification"). Unwitting LSD testing in the U.S. is covered in Church Report pp. 391 and 400–401.

**63. OK.** Church Report pp. 394 and 398 (the experiment, his death, and that the family was not notified of the circumstances). Turner p. 8 (details publicized in 1975). Non-graphic.

**64. OK.** Each timeline entry is supported: IG para. 17; Church Report p. 389 (Jan. 1973); Turner p. 8 (1975); Turner p. 9 and the Q&A (1977). "Filed in the wrong place" is supported by Turner p. 13.

**65. FIX (b-roll label only, same as line 18).** The narration is OK. Turner p. 9: "does not include status reports or other documents relating to operational considerations or progress". A full-text search of the hearing, which includes Church Book I pp. 385–422, and of the IG report finds no programmed-assassin claim. The only "Manchurian Candidate" mention is a CIA witness calling the idea "impossible". The 1957 IG reference to "assassination delivery systems" concerns devices, not programmed people. Theories are framed as theories.
Replacement label for dv1026930 @41.0: `B-ROLL · MILITARY JET FLIGHT OVER WASHINGTON, D.C., 2026`, unless the DVIDS credit is verified as Air Force. The dv346119 Capitol 2014 shot is OK.

**66. OK.** Rhetorical close, consistent with the record. The image h1 matches its label.

**67. OK.** Call to action. The b-roll (Capitol, 2014) is OK.

**68. OK.** Next-episode tease, no factual claim.

## Summary
- OK: 53
- NOTE: 7 (lines 1, 4, 12, 29, 39, 46, 56). Optional suggestions inside line 37 (second shot) and line 57 (kicker) do not change those verdicts.
- FIX: 8 (lines 18, 21, 30, 31, 32, 37, 43, 65)

RESULT: FIXES REQUIRED

---
## Fixes applied by the producer (2026-11-01, before rendering)
1. Lines 18, 31, 65: DVIDS page 1026930 opened — credit: U.S. Air Force F-22 Raptor Demonstration Team, 1st Fighter Wing, D.C., July 3, 2026. Label now `B-ROLL · VIEW FROM A U.S. AIR FORCE F-22 OVER WASHINGTON, D.C., 2026`.
2. Line 21: narration now verbatim ("fails to disclose the full pattern of reactions and attributions that may occur in operational situations").
3. Line 30: "neither the chief of the CIA's Technical Services Staff, where Gottlieb worked, nor the head of the covert operations directorate".
4. Line 32: "In the early hours of November twenty-eighth, nineteen fifty-three…"; on screen a date card (NOV. 28, 1953, sourced to Church p. 397 and Ford statement) replaces the h77a crop.
5. Line 37: dv950025 starts at 7.0 s (after the title slate) and 150.0 s; verified in contact sheets after build.
6. Line 43: reordered; "According to the CIA, MKUltra itself ended in nineteen sixty-four."; timeline "Program ends (CIA account)".
NOTEs adopted: line 4 ("it looked as if the paper trail was gone for good"), line 12 ("under the cover of research foundations"), line 29 (new crop h79a showing the Cointreau passage, Church p. 396), line 39 (Helms named; "According to the Inspector General, Helms said…"), line 46 ("in his words"), line 56 ("In the recovered files…"), line 57 (kicker "AMONG THE 80 INSTITUTIONS").
All FIX items resolved → 0 open FIX.
