# 013 — Operation Mongoose — independent fact-check

Checked 2026-11-12 against primary texts:
- **Church** = S. Rep. 94-465 (1975), OCR `/home/claude/src/doc/church.txt` plus page scans (archive.org `allegedassassina00unit`, n = page + 21). I viewed each on-screen crop in `/home/claude/src/img/doc/`, and every crop matches its labelled page. I also viewed n92 to confirm that "at least eight plots" is on **p. 71**. The section starts there, so no page number is printed. The researcher's notes say p. 70, which is wrong. The script's p. 71 is right.
- **FRUS X / XI** = HistoryAtState TEI XML (frus1961-63v10.xml, v11.xml), docs d270, d278, d291, d292, d304, d314, d367, d386; XI d8, d19, d79, d82, d84, d217, d261. Each doc was extracted and read.
- **NSArchive** 2019 briefing book (WebFetch): https://nsarchive.gwu.edu/briefing-book/cuba/2019-10-03/kennedy-cuba-operation-mongoose
- 2017 JFK release with Mongoose material: https://www.archives.gov/research/jfk/release-2017-2018 , https://www.cbsnews.com/miami/news/jfk-files-cia-plotted-kill-castro-stage-bombings-miami

Line numbers are 1-indexed positions in `LINES`.

## A. Spoken lines

| # | Claim / text | Verdict | Source checked | Exact replacement (FIX) / note |
|---|---|---|---|---|
| 1 | "…secret war on Fidel Castro's Cuba. And it had a deadline." | **FIX** | FRUS X d304: "It is a series of target actions and dates, not a rigid time-table." Church p.144: the SGA "tabled Lansdale's six phase plan altogether in February 1962". | October 1962 was Lansdale's target date in a plan the overseers shelved. It was never a binding deadline. → `What was Operation Mongoose? \| It was the Kennedy administration's secret war on Fidel Castro's Cuba. \| And its plan had a target date.` |
| 2 | Feb 20, 1962 schedule, Phase V wording | OK | FRUS X d304 (verbatim) | — |
| 3 | Revolt never came; something else did in early October | OK | Chronology (U-2 photos Oct 14) | — |
| 4 | U-2 over western Cuba on Oct 14 photographed Soviet missile sites | OK | Standard record (Mission 3101, Oct 14, 1962) | — |
| 5 | File intro; "ran straight into the most dangerous month" | OK | Chronological overlap only, with no causal claim | — |
| 9 | Bay of Pigs, April 1961, collapsed within days | OK | history.state.gov milestone (landing Apr 17, defeat by Apr 19) | — |
| 10 | Senate investigators found JFK distrusted the CIA after the failure | OK | Church p.140: "As a result of the Bay of Pigs failure, President Kennedy distrusted the CIA" | — |
| 11 | Nov 3, 1961 White House meeting; new program; codename Mongoose | OK | FRUS X d270 (editorial note, verbatim basis) | NOTE: the shot is the Capitol (CAP) while the line describes a White House meeting. The label is honest, but WH b-roll would fit better. |
| 12 | RFK longhand notes: stir things up, espionage, sabotage, general disorder, run & operated by Cubans | OK | FRUS X d270 (notes dated 11/7/61) | — |
| 13 | Nov 30 memo, "We will use our available assets… overthrow the communist regime" | OK | FRUS X d278 | NOTE: FRUS says it was "apparently drafted by McGeorge Bundy". The memo calls the effort "the Cuba Operation", not Mongoose. The graphic already handles this correctly. |
| 14 | Air Force general Lansdale, Chief of Operations, Philippines/Vietnam reputation | OK | FRUS X d278, d291 ("Brig. Gen. Lansdale"); Church p.140 | — |
| 15 | SGA; Taylor chairman; RFK "principal motive force" per State Dept historians | OK | FRUS X d270 (editors' text, verbatim) | — |
| 17 | Jan 18: 32 tasks; "It is our job… full command" | **FIX** | Church p.142: the quote comes from a Lansdale memorandum dated **1/20/62**, not Jan 18 | → `On January eighteenth, nineteen sixty-two, he handed out thirty-two tasks to the agencies taking part. \| Two days later, he told his working group, it is our job to put the American genius to work on this project. \| We are in a combat situation, where we have been given full command.` |
| 18 | Goal: overthrow from within; open support incl. military force as necessary | OK | FRUS X d291 (verbatim) | — |
| 19 | "A day later, a thirty-third task…" chemical incapacitation; unfeasible, dropped | **FIX** | Church p.143 (Task 33 added Jan 19, "unfeasible", "cancelled") | After the L17 fix, "a day later" would point to Jan 20. → `The day after the tasks went out, a thirty-third task was added. \| A plan to incapacitate Cuban sugar workers during the harvest, by chemical means. \| It was found unfeasible, and dropped.` |
| 20 | Jan 19 meeting in RFK's office; "A CIA officer's notes record his words"; "The top priority in the United States Government. No time, money, effort, or manpower…" | **FIX** | The wording "The top priority in the United States Government" and the on-screen quote come from **Helms's memo** to McCone (FRUS X d292). The image shows **McManus's notes** (Church p.141), which read "carried top priority in U.S. Gov[ernmen]t". Both are CIA records, but the spoken wording is the memo's, not the notes'. | → `On January nineteenth, Robert Kennedy met the Mongoose team in his office. \| A C I A memo on the meeting records his words. \| The top priority in the United States Government. \| No time, money, effort, or manpower is to be spared.` The graphic attribution "as recorded by the CIA" plus DOC. 292 is OK. |
| 21 | Task Force W under Harvey; about 400 people at HQ and the Miami station | OK | Church p.140; FRUS X d270 | — |
| 22 | Miami station codename JM/WAVE | OK | Church p.84 ("CIA's Miami station… (JM/WAVE)"), p.153 | — |
| 23 | Plans in detail; gradients on the beach, composition of the sand | OK | Church p.144 (Assistant, 6/18/75) | — |
| 25–26 | Six phases; months | OK | FRUS X d304 (Phase I Mar; II Apr–Jul; III Aug 1; IV Aug–Sep; V first two weeks Oct; VI during Oct) | — |
| 27 | Resistance phase: attacks on cadre incl. key leaders; "Gangster elements… best recruitment potential" | **FIX** | Church p.143. The quote continues "…for actions against police—G2 [intelligence] officials." Cutting it there overstates the claim. | → `For the resistance phase, the plan as quoted by the Senate listed attacks on the cadre of the regime, including key leaders. \| Gangster elements, it said, might provide the best recruitment potential for actions against police and intelligence officials.` |
| 28 | "Will the U.S. respond promptly with military force to aid the Cuban revolt?" | OK | FRUS X d304 (verbatim) | — |
| 29 | Mar 14 guidelines: "would use Cuban resources first"; "final success will require decisive U.S. military intervention" | **FIX** | FRUS X d314: "will make maximum use of indigenous resources, internal and external, but recognizes that…". The word "first" is not in the text. | → `The answer, in the guidelines of March fourteenth, was blunt. \| The United States would make maximum use of Cuban resources. \| But final success will require decisive U S military intervention.` |
| 30 | JFK skeptical per State Dept note; no such decision made | OK | FRUS X d314 source note (U. Alexis Johnson, Mar 16) | NOTE: the same note adds "although contingency planning would proceed". |
| 31 | Priority would be hard intelligence | **FIX** (omission) | FRUS X d314 para 2; Church p.144 ("the SGA tabled Lansdale's six phase plan altogether… directed him to… an intelligence collection plan only") | Without this, the October "deadline" framing is overstated. → `For the coming months, the guidelines said, the priority would be hard intelligence. \| Lansdale's six-phase schedule, the Senate found, had been shelved by the group overseeing him.` |
| 33 | Jan 27 touchdown play; 1975 testimony = Cuban revolt | OK | Church pp.142–143 and fn.1 | — |
| 34 | In January, the Defense representative sent Lansdale "Operation Bounty"; leaflets; killing or delivering alive known Communists | OK | Church p.144 (Jan 30, 1962; Craig to Lansdale) | NOTE: for the vertical cuts, "In January nineteen sixty-two" would stand better on its own. |
| 35 | $5,000 informer to $100,000 officials; 2¢ for Castro | **FIX** (add the reason) | Church p.144 ("A reward of '2¢' was listed for Castro"; "to denigrate * * * Castro in the eyes of the Cuban population") | The y1/s1 titles ask "why", but the narration never says. → `From five thousand dollars for an informer to one hundred thousand dollars for government officials. \| The reward listed for Castro himself was two cents. \| Lansdale testified it was meant to denigrate Castro in the eyes of the Cuban people.` |
| 36 | "Lansdale testified that he tabled it, and it never went to the group." | **FIX** | Church p.144: "tabled" is his testimony. "He never brought Operation Bounty before the SGA" is the report's own statement. | → `Lansdale testified that he tabled it. \| According to the report, he never brought it before the group.` |
| 37 | "Another idea survives only in testimony… former secretary Thomas Parrott… plan he attributed to Lansdale" | **FIX** (opener, for y2) | Church p.142 fn.2; Parrott was Secretary of the Special Group (Church, Parrott bio; author of SGA minutes, FRUS XI d82) | y2 starts here, and "Another" opens mid-context. → `One idea survives only in testimony. \| In nineteen seventy-five, the group's former secretary, Thomas Parrott, told the Senate about a plan he attributed to Lansdale.` |
| 38 | Second Coming rumour; submarine surfaces, star shells | OK | Church p.142 fn.2 | — |
| 39 | Told sarcastically; "Some wag… Elimination by Illumination" | OK (spoken) | Church p.142 fn.2 ("Parrott sarcastically characterized") | See graphic fix G-39. |
| 40 | Alongside Mongoose, something the overseeing committee wasn't told; April 1962 pills to Rosselli | OK | Church p.84 (pills passed to Rosselli in Miami after Apr 21, 1962); p.153 (Harvey "never informed the SGA… of the ongoing assassination plots"); p.270 (finding) | — |
| 41 | Miami station help; Harvey and station chief rented U-Haul under assumed name; explosives, rifles, radios; parking lot | OK | Church p.84 | — |
| 43 | "Lansdale proposed a stepped-up course" — major sabotage, submarines, radio, leaflets | **FIX** | FRUS X d367: "You requested a paper on 'a possible stepped up Course B'". The items are authorities "would be required". Lansdale's own comment urged a different (Latin American) concept. | → `On August eighth, at the group's request, Lansdale laid out a stepped-up course. \| Major sabotage. \| Submarines for infiltration. \| Radio and leaflets.` |
| 44 | "his paper admitted" CIA operators doubted it; U.S. military force must be anticipated | **FIX** (verb) | FRUS X d367 (verbatim). Lansdale is reporting the CIA's view, not conceding a point of his own. | → `Even then, his paper reported, the C I A's own operational people did not believe it would bring down the regime by itself. \| They believed the use of U S military force in the final stage must be anticipated.` |
| 45 | Aug 10 meeting in the Secretary of State's office; assassinating Cuban leaders came up; Aug 13 "liquidation of leaders" | OK | Church p.161 (raised Aug 10; Aug 13 directive); p.162 (Harvey: "in Secretary Rusk's office"); p.163 (chaired by Rusk). "Secretary of State's office" is correct. | — |
| 46 | "Harvey objected, not to the idea, but to the paper. He wrote of the stupidity…; minutes contain no reference" | **FIX** | Church p.162. Nothing in the record says Harvey supported the idea, so "not to the idea" is an inference. | → `Harvey objected to putting it on paper. \| He wrote of the stupidity of putting this type of comment in writing. \| The meeting's minutes contain no reference to assassination.` |
| 47 | "President Kennedy signed a national security memo" | **FIX** | FRUS X d386: NSAM 181 is signed **McGeorge Bundy**: "The President has directed…" | → `On August twenty-third, a national security memo conveyed President Kennedy's orders. \| Mongoose Plan B plus should be developed with all possible speed.` |
| 48 | Same memo: analysis of missiles in Cuba that could reach the U.S. | OK | FRUS X d386 item 5 | — |
| 49 | "A CIA planning paper that month had assumed that Soviet troops will not be present in Cuba in force." | **FIX** | FRUS X d367 attachment (Harvey, "Covert Activities", Aug 7, 1962), sec. I.C: "For the purpose of this plan the following assumptions are made: … 2. Soviet troops will not be present in Cuba in force." This was a planning premise, not a forecast. | → `For the purpose of its plan, a C I A paper that month assumed that Soviet troops will not be present in Cuba in force.` |
| 50 | Aug 30 approval of operation to blow up copper mine, Matahambre | OK (attribution note) | Church p.337 is in the **Appendix to the Additional Views of Sen. Howard Baker**, not the Committee's findings. "Copper mine" comes from NSArchive. | See label fix L-50. |
| 52 | "Robert Kennedy told the group the President was dissatisfied with the lack of action in the sabotage field." | **FIX** | FRUS XI d8 (McCone): "The Attorney General reported on discussions with the President on Cuba; dissatisfied with lack of action in the sabotage field, went on to stress…". Grammatically the subject who is dissatisfied is RFK, not explicitly the President. | → `On October fourth, Robert Kennedy reported on his talks with the President about Cuba. \| He was dissatisfied, the record says, with the lack of action in the sabotage field.` |
| 53 | Oct 16: day JFK shown photos; RFK met Mongoose team that afternoon | OK | FRUS XI d19 ("At 2:30 this afternoon… in his office"); JFK was briefed on the photos the morning of Oct 16 | — |
| 54 | General dissatisfaction of the President; year; discouraging; no sabotage; one attempted failed twice | OK | FRUS XI d19 (verbatim basis) | — |
| 55 | Six days later, TV address | OK | Oct 22, 1962 | — |
| 56 | Morning Oct 26: McCone stood down 10 teams / 50 people by submarine; afternoon three teams recalled | OK | FRUS XI d79 (10 a.m.); d82 (2:30 p.m.) | — |
| 57 | "No major acts of sabotage… the minutes say. The President suggested Mongoose be reconstituted…" | **FIX** | The sabotage line is in the afternoon SGA minutes (XI d82). The President's suggestion was at the morning ExComm (XI d79). As written, both read as one record. | → `No major acts of sabotage should be undertaken at this time, the afternoon minutes say. \| That morning, the President had suggested that Mongoose be reconstituted, and oriented toward problems of a Cuba after Castro.` |
| 58 | Khrushchev letter same day; threat of armed attack constantly hung over Cuba; did not name Mongoose | OK | FRUS XI d84 | — |
| 59 | Two days later agreed to remove missiles; Matahambre team per NSArchive went in during crisis, never recovered | OK | Oct 28 announcement; NSArchive: "took place during the Missile Crisis", "The commando team was not recovered" (landed Oct 20; members captured Nov 5 and 14, per Doc. 21 summary) | NOTE: "was not recovered" would match the source wording exactly. |
| 61 | Late Nov McCone: restrict to intelligence; "Bundy… wrote to him." | **FIX** | FRUS XI d217 (Nov 29); d261 (Bundy **to President Kennedy**). In the script "him" grammatically refers to McCone. | → `In late November, McCone said future activity should be restricted to intelligence gathering. \| On January fourth, nineteen sixty-three, the President's national security adviser, McGeorge Bundy, wrote to the President.` |
| 62 | "well nigh universal agreement that Mongoose is at a dead end" | OK | FRUS XI d261 | — |
| 63 | "The program ended. The sabotage, one senator later wrote, continued." | OK | Church p.337 (Baker appendix: "While the MONGOOSE program ended around the time of the Cuban missile crisis in October 1962, sabotage continued.") "One senator" is accurate. | See crop fix L-63. |
| 64 | "Twelve years later…"; at least eight plots 1960–1965 | **FIX** | Church p.71 (verified on scan n92). Oct 1962 → Nov 1975 is 13 years, and L71 says "thirteen years later". | → `In November nineteen seventy-five, the Senate's Church Committee pulled the story into the open. \| It found concrete evidence of at least eight plots involving the C I A to assassinate Fidel Castro, from nineteen sixty to nineteen sixty-five.` |
| 65 | Plots can't be understood without fully authorized assaults incl. Mongoose | OK | Church p.6 | — |
| 66 | Could not find presidential authorization; "so ambiguous…"; plausible denial | OK | Church pp.6–7 | — |
| 68 | 1975 report; 1997 FRUS X; 2017 and 2025 NARA releases | OK | FRUS X preface May 1997; NARA 2017 release (Mongoose minutes reported, CBS Miami); NARA Mar 2025 | NOTE: the Oct 16/Oct 26 meeting records are in FRUS vol. XI (1996), not vol. X. "The meeting notes" is still true for the Jan 19 memo in vol. X. |
| 69 | Ordered in writing by the President, driven by his brother, to bring down Castro's government from inside | OK | FRUS X d278, d270, d291 | — |
| 70 | "Its deadline was October 1962. And that October, the crisis it was meant to prevent was the one the world got instead." | **FIX** | Nothing in the record says Mongoose was meant to prevent a missile crisis. Its goal was overthrow (d278/d291). October was a target date, not a deadline (d304). | → `Its own planners said success would need American troops. \| Its target date was October nineteen sixty-two. \| And that October, instead of a revolt, the world got the Cuban Missile Crisis.` |
| 71 | First release "thirteen years later" | OK | 1962 → 1975 | Consistent once L64 is fixed. |

## B. On-screen graphics

| # | Field | Verdict | Source | Replacement |
|---|---|---|---|---|
| 2 | doc lines Phase V | OK | FRUS X d304 | — |
| 7 | title sub "The Secret Plan to Topple Castro by October 1962" | OK | d304: the plan aimed for October 1962 | Acceptable once L31 says the plan was shelved. |
| 12 | quote RFK, notes Nov 1961, DOC. 270 | OK | d270 | — |
| 13 | doc Nov 30 memo lines | OK | d278 | — |
| 18 | quote "Such support will include military force, as necessary." | OK | d291 | — |
| 20 | quote "…all else is secondary— no time, money, effort, or manpower is to be spared." / "as recorded by the CIA" / DOC. 292 | OK | d292 (Helms memo) | — |
| 21 | stat ~400, P.140 | OK | Church p.140 | — |
| 22/59 | MAP source "SOURCE: CHURCH COMMITTEE REPORT (1975) · MAP: NATURAL EARTH" | **FIX** | "COPPER MINE" is from NSArchive. Church says only "Matahambre mine". | `SOURCE: CHURCH COMMITTEE REPORT (1975); NATIONAL SECURITY ARCHIVE (2019) · MAP: NATURAL EARTH` |
| 25 | timeline phases | OK | d304 | — |
| 29 | doc guidelines lines | OK | d314 | — |
| 35 | stat 2¢, k "OPERATION BOUNTY · JANUARY 30, 1962", c "meant \"to denigrate\" him, Lansdale testified", P.144 | OK | Church p.144 | — |
| 39 | quote `Some wag called this operation— {{Elimination by Illumination.}}` | **FIX** | Church p.142 fn.2: "some wag called this operation—and somebody dubbed this—Elimination by Illumination". The words cut out must be marked with an ellipsis. | `Some wag called this operation… {{Elimination by Illumination.}}` |
| 44 | who "Edward Lansdale" | **FIX** | d367: Lansdale is reporting the CIA operators' belief | who=`Edward Lansdale, reporting the CIA operators' view` |
| 46 | quote Harvey, P.162 | OK | Church p.162 ("inadmissability" is the source's spelling) | NOTE: the quote stops before "in such a document". Add a trailing "…" if your style requires it. |
| 47 | doc NSAM 181 lines/header | OK | d386 | NOTE: it is signed by McGeorge Bundy, so the narration fix L47 is needed. |
| 54 | quote Helms, DOC. 19 | OK | XI d19 | — |
| 56 | stat 10 TEAMS / 50 people / stood down; DOCS. 79, 82 | OK | XI d79, d82 | — |
| 58 | quote Khrushchev, U.S. Embassy translation | OK | XI d84 | — |
| 62 | quote Bundy | OK | XI d261 | — |
| 64 | stat b "CIA plots against Castro, 1960-1965" | **FIX** | Church p.71: "plots involving the CIA to assassinate Fidel Castro" | b=`plots involving the CIA to kill Castro, 1960–1965` |
| 68 | release timeline | OK | see L68 | — |

## C. Image / footage labels

| # | Label | Verdict | Note / replacement |
|---|---|---|---|
| 1, 26, 27, 70 | revolt = P.143 | OK | The crop shows the p.143 text. |
| 5, 17 | tasks32 = P.142 | OK | — |
| 15 | tfw = P.140 | OK | The crop shows the Task Force W paragraph on p.140. |
| 20 | jan19 = P.141 | OK | — |
| 23 | beach = P.144 | OK | — |
| 33 | touchdown = P.142 | OK | — |
| 34, 36 | bounty144 = P.144 | OK | — |
| 37 | illum = P.142, FOOTNOTE | OK | — |
| 40, 41 | uhaul = P.84 | OK | — |
| 45 | liquid = P.161 | OK | — |
| 50 | matah = `CH + "337"` | **FIX** | `CH + "337 · ADDITIONAL VIEWS OF SEN. HOWARD BAKER"` (the page is in Baker's appendix, not the Committee's findings) |
| 63 | matah "down" crop = P.337 | **FIX** (image) | The current crop ends at "…shipping containers." It does not include "While the MONGOOSE program ended around the time of the Cuban missile crisis in October 1962, sabotage continued." Re-crop p.337 (scan n358) to include that paragraph, and use the same Baker label as L50. |
| 65 | ctx6 = P.6 | OK | — |
| 66 | find6 = P.6, find7 = P.7 | OK | — |
| newsreel | NRC/NRH (Jan 1959), NRC60, NRMIL (1960), NRB26 (B-26 landed in Florida, Apr 1961), NRCAMP (Guatemala base, 1961 newsreel), JFK (Oct 22, 1962 address) | NOTE | All are plausible, and each date is earlier than the events it illustrates. I could not see the newsreel frames, so confirm each caption against the newsreel's own catalogue description. |
| b-roll | WH/CAP/TREAS/PENN 2012, PENT 2023/2017, GTMO 2015, SEA/KW 2026, FLARE 2024, CG 2023, U2B 2023, F22 2026 | OK | All are labelled as modern b-roll, so nothing implies they show 1962. L11: prefer WH over CAP. |

## D. META hooks and vertical cuts

| id | lines | Verdict | Issue | Replacement |
|---|---|---|---|---|
| s1 | [34, 39] | **FIX** | The cut is titled about the 2¢ bounty but runs on into the Second Coming story, which is a different topic. | lines=`[34, 36]`. Hook: `A PROPOSED BOUNTY ON CASTRO:<br>[TWO CENTS]` (the concept was tabled and never adopted) |
| s2 | [1, 5] | **FIX** (hook) | "Deadline" overstates. Lansdale set a target date; the plan was "not a rigid time-table" and was shelved. | hook=`A SECRET TIMETABLE<br>[FOR CASTRO]` |
| s3 | [53, 58] | **FIX** (hook) | "Same day as the missile photos" is ambiguous: the photos were taken Oct 14. Oct 16 was the day JFK was shown them. | hook=`THE DAY JFK SAW<br>[THE MISSILE PHOTOS]` |
| s4 | [45, 49] | **FIX** | Lines 47–49 (NSAM 181, Soviet troops) are off-topic. Hook "WOULDN'T WRITE IT DOWN" conflicts with Harvey's "I took careful notes" (Church p.162). | lines=`[45, 46]`. hook=`THE CIA MAN WHO<br>[DIDN'T WANT IT IN WRITING]` |
| y1 | [34, 36] | **FIX** (hook) | "Castro's bounty" implies a real bounty | hook=`A PROPOSED BOUNTY:<br>[TWO CENTS]` (needs the L35 fix so the "why" is spoken) |
| y2 | [37, 39] | OK once L37 is fixed | Opened mid-context with "Another idea" | Hook "A FAKE SECOND COMING?<br>[A WITNESS SAID SO]" is OK. |
| y3 | [52, 55] | OK | Stands alone; ends on the TV address | — |

## E. Titles

| Title | Verdict | Replacement |
|---|---|---|
| Long: "Operation Mongoose: The Secret Plan to Topple Castro by October 1962" | OK | The plan did target October 1962 (d304). Keep it, together with the L31 disclosure. |
| y1 "Why Was Castro's Bounty Just Two Cents?" | **FIX** | `Why Did a 1962 Pentagon Idea Price Castro at Two Cents?` |
| y2 "Did the U.S. Plan a Fake Second Coming in Cuba?" | **FIX** | The only source is one witness's sarcastic testimony, with no planning document. → `A Fake Second Coming in Cuba? What One Witness Told the Senate` |
| y3 "What RFK Was Doing the Day the Missiles Were Found" | **FIX** | The missiles were photographed Oct 14 and identified Oct 15. Oct 16 is the day JFK was shown them. → `What RFK Was Doing the Day JFK Saw the Missile Photos` |
| s1 "Why Was the Bounty on Castro Only Two Cents?" | **FIX** | `The Pentagon Idea That Priced Castro at Two Cents` |
| s2 "Kennedy's Secret Deadline for Castro: October 1962" | **FIX** | Kennedy did not set it. Lansdale did, as a target date. → `Lansdale's Secret Timetable for Castro: October 1962` |
| s3 "The Same Day as the Missile Photos, RFK Met Mongoose" | **FIX** | `The Day JFK Saw the Missile Photos, RFK Met Mongoose` |
| s4 "The CIA Man Who Didn't Want It in Writing" | OK | Church p.162 |

## F. Requested checks (short answers)
- "Distrusted the CIA": Church p.140, a Committee statement. OK.
- Nov 3 meeting and codename: FRUS X d270 editors. OK.
- "Principal motive force": FRUS X d270 (State Dept historians). OK.
- 32 tasks / Task 33: Church pp.142–143. Task 33 was added Jan 19 and was "nonlethal" per Lansdale. OK.
- Jan 19 quote: the wording is Helms's memo (d292); the image is McManus's notes. Fixed at L20.
- ~400 / JM/WAVE: Church p.140, p.84, p.153. OK.
- Bounty: Jan 30, 1962; Gen. Craig (DoD/JCS rep); $5,000–$100,000; 2¢; tabled; never brought to the SGA. All on p.144, plus the Baker appendix pp.336–337.
- Poison pills April 1962 / U-Haul: p.84. The SGA was not told: p.153 (Harvey testimony) and p.270 (Committee finding).
- Aug 10 location: "Secretary Rusk's office" (Harvey memo, p.162). The IG report says "a meeting at State". "Secretary of State's office" is fine.
- NSAM 181: signed by Bundy. Fixed at L47.
- "Soviet troops will not be present in Cuba in force": Harvey/CIA "Covert Activities", Aug 7, 1962, attached to Lansdale's Aug 8 memo (FRUS X d367). It was a planning assumption. Fixed at L49.
- Matahambre: approved Aug 30 per the Baker appendix, p.337. "One senator later wrote" (L63) is correct.
- Oct 16: the meeting was at 2:30 p.m. and JFK was shown the photos that morning. OK.
- Line 70 "crisis it was meant to prevent": not supported. Fixed.
- "Twelve" vs "thirteen" years: fixed at L64.

## Late changes (verified 2026-11-12)

| # | Item | Verdict | Source | Replacement / note |
|---|---|---|---|---|
| 1 | L39 adds "On the same page, Robert McNamara is quoted. \| We were hysterical about Castro at the time of the Bay of Pigs and thereafter." | **FIX** | Church p.142, fn.1: "McNamara stated that 'we were hysterical about Castro at the time of the Bay of Pigs and thereafter.' (In the same context, McNamara stated 'I don't believe we contemplated assassination.') (McNamara, 7/22/75, p. 93)" | The quote is verbatim. Three problems: "On the same page… is quoted" describes the page rather than the source; it was sworn 1975 testimony; and the same passage has McNamara's denial, which should go with it for balance, especially in the y2 cut. → `Parrott told the story sarcastically. \| Some wag, he said, called it Elimination by Illumination. \| Robert McNamara, Kennedy's defense secretary, testified that same month. \| We were hysterical about Castro at the time of the Bay of Pigs and thereafter. \| But, he added, I don't believe we contemplated assassination.` NOTE: the `illum` crop shows only fn.2. Fn.1 is on the same page (p.142), so the label is still correct. |
| 2a | s1 lines [33,39] | OK, with one FIX | Church pp.142–144 | Every line holds up on its own, but L33 has no year when it stands alone. → L33: `On January twenty-seventh, nineteen sixty-two, Lansdale wrote to Robert Kennedy that we might uncork the touchdown play independently of the institutional program. \| Asked about it in nineteen seventy-five, he testified that the touchdown play meant a Cuban revolt to overthrow the regime.` |
| 2b | s1 hook "A 2-CENT BOUNTY.<br>[A 'SECOND COMING'?]" | **FIX** | Church p.144: Bounty was a proposal Lansdale tabled, never adopted | `A 2-CENT BOUNTY IDEA.<br>[A 'SECOND COMING'?]` |
| 2c | s1 title "Two Cents and a 'Second Coming': Ideas Against Castro" | OK | — | — |
| 3a | s2 lines [9,15] + hook "WHAT WAS<br>[OPERATION MONGOOSE?]" | OK | FRUS X d270, d278; Church p.140 | The cut begins with context and ends on a complete thought (L15). In L11, "he" correctly refers back to Kennedy in L10. |
| 3b | s2 title "How the Bay of Pigs Led to Operation Mongoose" | **FIX** (wording) | Church p.140 links the Bay of Pigs failure only to JFK's distrust of the CIA and the choice of an outsider (Lansdale). It does not say the Bay of Pigs caused Mongoose. | `After the Bay of Pigs: How Operation Mongoose Began` |
| 4 | s4 lines [43,48] (episode.py currently has [43,47]), hook "SUMMER 1962:<br>[THE SECRET WAR ESCALATES]", title "How the Secret War on Castro Escalated in 1962" | OK | FRUS X d367, d386; Church pp.161–162 | "Escalates" is supported: "Stepped Up Course B" and "Plan B plus… with all possible speed". Either end line works. 48 ends on a complete thought. The file has 47 while your message says 48, so make them match. |
| 5a | youtube_description.txt lines 1–2 | OK | d304, d278, d292, Church p.144, p.142, XI d79/d82 | — |
| 5b | Description FOOTAGE: "a B-26 that landed in Florida and a training base in Guatemala, April 1961" | **FIX** | On-screen label NRCAMP says only "as shown in a 1961 newsreel" | `a B-26 that landed in Florida, April 1961; a training base in Guatemala, as shown in a 1961 newsreel;` |
| 5c | Description sources / disclaimers | OK | — | NOTE: optionally add "Fidel Castro in a crowd, 1960" to the film-still list, since it is used on screen. |
| 5d | thumb.json A "TOPPLE CASTRO BY OCTOBER" + "OPERATION MONGOOSE · 1962" | OK | d304 (target October 1962) | NOTE: the photo is a January 1959 newsreel still next to a "1962" stamp. It is acceptable as a topic stamp. |
| 5e | thumb.json B Phase V lines | OK | d304 (verbatim, uppercased) | — |
| 5f | thumb.json C "WHAT WAS OPERATION MONGOOSE?" | OK | — | — |
