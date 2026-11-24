# Fact-check, FILE 019 (independent). Date of check: 2026-11-24
Line numbers = 1-indexed position in LINES. Result: PASS / FIX / CUT.
Sources: DOC = local PDFs in /home/claude/src/doc (pdfinfo, pdftoppm, pdftotext). CBS1 = cbsnews.com/news/epstein-files-redaction-over-500-entirely-blacked-out/ ; CBS2 = cbsnews.com/news/epstein-files-whats-missing/ ; WIKI = en.wikipedia.org/wiki/Epstein_Files_Transparency_Act ; SCR1 = scrippsnews.com/.../epstein-files-released-with-major-redactions-spark-congressional-anger ; SCR2 = scrippsnews.com/.../justice-department-releases-more-than-3-million-new-epstein-related-records ; PBS = pbs.org/newshour/show/whats-revealed-in-the-latest-epstein-files-release-and-whats-redacted ; NPR1 = npr.org/transcripts/nx-s1-5694664 ; NPR2 = npr.org/transcripts/nx-s1-5696975 ; NPR3 = npr.org/2026/02/06/nx-s1-5702692/... ; RC = rollcall.com/2026/11/11/another-bill-to-release-epstein-files-headed-to-house-floor/ ; CBS3 = cbsnews.com/news/epstein-files-bill-discharge-petition-thomas-massie/ ; AX = axios.com/2026/11/11/massie-epstein-files-second-vote ; GMA = goodmorningamerica.com/news/story/discharge-petition-2nd-epstein-files-bill-secures-218-138057235 ; KUOW = kuow.org/npr-news/2026-11-10/federal-government-failed-to-hold-epstein-accountable-republican-committee-says ; NBCB = nbcboston.com/.../house-gop-jeffrey-epstein-report-doj-investigation/4047289/ ; WYPR = wypr.org/2026-11-18/the-law-releasing-the-epstein-files-passed-one-year-ago-what-do-his-victims-say ; SCV = signalscv.com/2025/12/doj-says-it-re-released-119-pages-of-epstein-files-that-were-redacted/ ; PBSM = pbs.org/newshour/politics/ghislaine-maxwell-sentenced-to-20-years-in-prison

## A. Local document checks
| Check | Result | Source |
|---|---|---|
| EFTA00005586 = 119 pp.; 6109 = 100; 6209 = 100; 6309 = 55 (sum 255); 8744 = 119 | PASS | pdfinfo |
| Every page of 5586/6109/6209/6309 black (20 dpi, body area, 0 non-black of 374) | PASS | DOC render check |
| Page 1 of 5586: black, "Grand Jury-NY" top right, footer EFTA00005586; page 60 footer EFTA00005645 (5586+59) | PASS | DOC pdftotext + PNG |
| 8744 p.1: UNITED STATES GRAND JURY / SOUTHERN DISTRICT OF NEW YORK / UNITED STATES OF AMERICA -v- GHISLAINE MAXWELL (2018R01618) / January 19, 2021 Additional / March 29, 2021 10:05 a.m.; appearances black-barred | PASS | DOC |
| 8744 p.2 (footer EFTA00008745, dated 03/29/2021): witness sworn by the Foreperson; "Detective [barred]"; New York City Police Department; "About 15 years"; name and prosecutor names black-barred | PASS | DOC PNG |

## B. Per-line checks
| # | Claim | Result | Source | Corrected wording (FIX) |
|---|---|---|---|---|
| 1 | 119 pages released completely black; "not a word" | PASS | DOC; CBS1 (119-page "Grand Jury-NY" document entirely redacted) | |
| 2 | Page one: file number and "Grand Jury, N Y" in corner | FIX | DOC (text reads "Grand Jury-NY", not "two words") | "Nothing but a file number at the bottom, and the words Grand Jury, N Y, in the corner." |
| 3 | Footer EFTA00005586; p.60 = 5645; "letters match initials of the law"; "every page the Department released carries its own number" | FIX | DOC; EFTA = Epstein Files Transparency Act (inference, widely reported) | "Every page in these files carries its own number, starting with letters that match the initials of the law." (drop "the Department released", which overgeneralizes) |
| 4 | Published under law passed almost unanimously; next day posted 119-page transcript, mostly visible | PASS | WIKI (427-1, UC); CBS1 (Saturday, largely unredacted 119-page transcript) | |
| 5 | Series framing; "millions of pages released in 2026" | PASS | internal series; PBS/SCR2 (3M+ pages) | |
| 6 | Epstein arrested federal sex trafficking charges July 2019, died in custody that August; Maxwell convicted two years later | PASS | PBSM (arrested 2019, died a month later; Maxwell convicted Dec 2021); Aug 10, 2019 per OIG (research.md) | |
| 7 | "A petition led by Republican Thomas Massie and Democrat Ro Khanna reached 218 on Nov 11" | FIX | RC (Massie leads); AX (Massie announced, "working with" Jayapal, Leger Fernandez, Khanna); GMA/CBS3 name Massie only. 218 on Nov 11 PASS. Graphic text ("as reported by CBS News and Roll Call") PASS | "A petition led by Republican Thomas Massie, with Democrat Ro Khanna and others working alongside him, reached two hundred eighteen signatures on November eleventh" |
| 8 | Not evidence of wrongdoing; DOJ warned some material may be false/misleading. Graphic quote "Some material"... n/a here | PASS | SCR2 | |
| 9 | Intro card | PASS | n/a | |
| 10 | Title card (INSIDE THE FILES) | PASS | n/a | |
| 11 | Chapter I | PASS | n/a | |
| 12 | Introduced July 2025 by Khanna; Massie helped lead through House | PASS | WIKI (July 15, 2025, H.R. 4405; Massie discharge petition); CBS1 | |
| 13 | House passed Nov 18, 427-1; Senate unanimous consent; signed Nov 19 (graphic same) | PASS | WIKI | |
| 14 | Rep. Clay Higgins (R) lone no; suspension of rules needs two-thirds | PASS | WIKI (R-LA, 427-1, 290 needed) | |
| 15 | 30 days, searchable/downloadable, declassify; graphic: deadline Dec 19, 15-day redaction list | PASS | WIKI; CBS1 (list of redactions within 15 days) | |
| 16 | Allowed redactions: victims' info, CSAM, death/abuse/injury images, narrow temporary hold for active investigation | PASS | CBS1 (violent photos, CSAM, narrowly tailored and temporary); WIKI | |
| 17 | The law drew a line | PASS | WIKI | |
| 18 | No record withheld/delayed/redacted for embarrassment, reputational harm, political sensitivity | PASS | WIKI; CBS1 | |
| 19 | List to House and Senate Judiciary Committees of government officials and politically exposed persons | PASS | WIKI | |
| 20 | No penalty; covers only DOJ, not State, Treasury, CIA, NSA, "CBS News noted" | PASS | WIKI (no penalty); CBS2 (DOJ only; ICE also listed) | |
| 21 | Deadline Fri. Dec 19, 2025 | PASS | WIKI; SCR1 | |
| 22 | "Posted thousands of records, including thousands of photographs, according to CBS" | FIX | CBS1 says "thousands of photos"; "thousands of records" not in CBS | "That day, the Department posted records and thousands of photographs, according to CBS News." |
| 23 | Lawmakers of both parties complained; full of black boxes | PASS | CBS1 (Khanna D, Massie R, Schumer) | |
| 24 | CBS: at least 550 pages entirely blacked out | PASS | CBS1 | |
| 25 | A 119-page grand jury document, every page black | PASS | CBS1; DOC | |
| 26 | Three documents = 255 pages (100+100+55), all black | PASS | CBS1; DOC | |
| 27 | CBS: at least 180 more blacked-out pages in otherwise mostly redacted files | PASS | CBS1 | |
| 28 | Khanna "incomplete release with too many redactions"; Massie "grossly fails to comply with both the spirit and the letter of the law" | PASS | CBS1 | |
| 29 | Schumer quote verbatim; title Senate Minority Leader | PASS | CBS1 | |
| 30 | Letter to Congress cited child abuse images and ongoing investigations; Blanche "only redactions... required by law — full stop" (to Fox News Digital); rolling basis | PASS | SCR1; CBS1 | |
| 31 | DOJ said on social media no politicians' names redacted; letter: 200+ lawyers, extra review for grand jury transcripts, not finished that day | PASS | CBS1 (X post; letter); SCR1 | |
| 32 | Chapter III | PASS | n/a | |
| 33 | "On December twentieth the Department said on social media it was posting a largely unredacted 119-page transcript" | FIX | CBS1: DOJ said a largely unredacted version was in files released Saturday; SCV: X post was Sunday. "On social media" on Dec 20 is not supported | "On Saturday, December twentieth, the Department said a largely unredacted version of a one hundred nineteen page grand jury transcript was among the files it released. That is the number CBS News reported." |
| 34 | Cover: US Grand Jury, SDNY; United States v. Ghislaine Maxwell; only first two pages shown | PASS | DOC | |
| 35 | Maxwell convicted Dec 2021 of sex trafficking of a minor and other charges; 20 years | PASS | PBSM (Dec 29, 2021; five of six counts; 20 years, June 28, 2022) | |
| 36 | Transcript dated March 29, 2021; first witness a NYC police detective; names already barred | PASS | DOC p.1-2 | |
| 37 | Grand jury testimony normally secret; CBS: judge required top Manhattan prosecutor to personally certify no victims' personal information | PASS | CBS1 | |
| 38 | Both 119 pages; can't tell if same; DOJ "an abundance of caution for victims and their families" (graphic: Dec 2025, as quoted by CBS, posted on social media) | PASS | CBS1 (said Sunday); SCV (X post); research.md | |
| 39 | Jan 30, 2026 | PASS | PBS; SCR2 | |
| 40 | "more than three million additional pages, about two thousand videos, about 180,000 images" (graphic: "about 2,000 videos"; "before: about 500,000 pages") | FIX | SCR2: "more than 2,000 videos"; PBS: about 500,000 pages before PASS | Narration: "more than three million additional pages, more than two thousand videos, and about one hundred eighty thousand images." Graphic b: "pages, plus more than 2,000 videos and about 180,000 images". DISPLAY: ("more than two thousand videos", "more than 2,000 videos") replacing the "about two thousand videos" entry |
| 41 | Scripps source list (six items) | PASS | SCR2 | |
| 42 | IG review = part two | PASS | internal | |
| 43 | AG letter: 6M+ pages identified for review; 3M published | PASS | PBS (Bondi letter) | |
| 44 | "PBS reported that by then more than 500 lawyers had reviewed the files" | FIX | PBS: DOJ said it sent "more than 500 lawyers" to review | "PBS reported the Department said it had put more than five hundred lawyers on the review." |
| 45 | NPR: about half of 6M not released; CSAM, deliberative, attorney-client, duplicates/unrelated | PASS | NPR1 | |
| 46 | PBS: ~200,000 pages withheld/redacted for privileges; more detailed look at officials/PEPs to Congress | PASS | PBS | |
| 47 | NPR said many released files are duplicative (PASS, NPR3); CBS later reported hundreds of thousands of released pages are emails nearly all from one account | FIX | CBS2: "hundreds of thousands of Epstein's emails", nearly all from jeevacation@gmail.com; not "pages" | "CBS later reported that hundreds of thousands of the released emails come, nearly all, from a single account." |
| 48 | DOJ warning (graphic quote "Some material may contain false or misleading information") | FIX | SCR2: only "may contain false or misleading information" is verbatim; "Some material" is Scripps's wording | Graphic q: "Some material {{may contain false or misleading information}}" with the quote marks removed from "Some material", or: q="…{{may contain false or misleading information.}}" |
| 49 | Notable individuals and politicians not redacted in any released file | PASS | SCR2 | |
| 50 | Some files withheld incl. violence; some pornographic images redacted; all women treated as victims | PASS | SCR2 | |
| 51 | Blanche "We complied with the statute, we complied with the act" (PBS); press-briefing remark on not expecting to find men who abused women | PASS | PBS; SCR2 ("I don't think that the public or you all are going to uncover men within the Epstein files that abused women"); GMA (Jan 30 press briefing) | |
| 52 | Khanna "asked why 2.5 million remain out of public view"; graphic "as quoted by PBS" | FIX | PBS: Rogin paraphrases Khanna: "outstanding questions about why, by the DOJ's account, 2.5 million of these documents remain out of public view". Not a Khanna quote | Narration: "Representative Khanna asked a different question: why, by the Department's own account, two and a half million of these documents remain out of public view." Graphic c: "as reported by PBS NewsHour"; b: "documents, by DOJ's own account, remain out of public view" |
| 53 | Chapter V | PASS | n/a | |
| 54 | Letter to SDNY judges: working around the clock on additional searches for documents that may require redaction (Feb 2026) | PASS | NPR3 | |
| 55 | Victims/victim counsel "have identified new victims and new identifiers" (nicknames, email addresses, family names); NPR: DOJ removed access to some pages | PASS | NPR3 | |
| 56 | About a tenth of a percent of pages had identifying info unredacted; "still several thousand pages" | PASS | NPR2 (Stephen Fowler paraphrasing DOJ; "several thousand pages") | |
| 57 | DOJ redacted thousands of victim names in millions of pages "to protect the innocent" | PASS | NPR2 (DOJ spokesperson statement) | |
| 58 | A survivor told NPR "no explanation for how it could have been done so poorly"; Nov 2026 another found her name and phone number unredacted | PASS | NPR3 (Annie Farmer); WYPR (NPR, Nov 18, 2026: Dani Bensky, memo pad, phone number). Do not name either | |
| 59 | CBS: names of business contacts and DOJ officials blacked out "without an obvious reason"; DOJ unredacted a photograph and two emails | FIX | CBS2: "no obvious reason" applies to business contacts and acquaintances; for many DOJ and FBI officials CBS says redaction makes it hard to reconstruct who was responsible; photo and two emails unredacted PASS | "CBS reported that names of business contacts were blacked out without an obvious reason under the law, and that the names of many Department and FBI officials were redacted too. After CBS asked about specific redactions, the Department unredacted a photograph and two emails." |
| 60 | Chapter VI | PASS | n/a | |
| 61 | DOJ position per CBS (June): all required docs released; ~3M unreleased pages duplicative, unrelated, or privileged; redactions consistent with Act | PASS | CBS2 | |
| 62 | Law requires written justification per redaction in Federal Register/Congress; DOJ offered general statement; journalist sued | PASS | CBS2 (journalist is Katie Phang; not named, fine) | |
| 63 | CBS list: earliest emails; ~20,000 messages from one account archived separately by a "transparency group"; "messaging apps"; attachments | FIX | CBS2: no Signal messages; ~20,000 messages from an earlier account were obtained by hackers and archived by Distributed Denial of Secrets, unclear whether DOJ has them; one cited attachment (Zorro Ranch firearm serial list) not found | Items: "Most of the earliest emails" / "About 20,000 messages from an earlier account" s="ARCHIVED BY DISTRIBUTED DENIAL OF SECRETS; UNCLEAR IF DOJ HAS THEM" / "Signal messages" / "At least one attachment an email refers to" |
| 64 | 69-page DEA report but no related records; 70%+ of ~5,000 index documents not found; DOJ told CBS "many were probably duplicates" (graphic "likely duplicates") | FIX | CBS2: "DOJ says many may be duplicates" | Narration: "The Department told CBS many of those may be duplicates." Graphic c: "DOJ told CBS many may be duplicates" |
| 65 | SARs released, pulled, re-released fully redacted; Wyden's office told CBS DEA declined his request | PASS | CBS2 | |
| 66 | Garcia (top Democrat, Oversight): not sure what's in the 3M; "okay, that's fine, let's see them." Graphic joins them in reverse order inside one quote | FIX | CBS2: "OK, that's fine, let's see them." and, separately, "I think what people need to understand is … we're not sure what's in the 3 million." Words are in the opposite order, and the ellipsis is dropped | Graphic q: "{{OK, that's fine, let's see them.}} … We're not sure what's in the 3 million." (source order) |
| 67 | CBS: footage from 147 cameras, 24 hours, 8+ TB not among released files | PASS | CBS2 | |
| 68 | DOJ internal documents: not significant, SHU cameras not active; CBS: by law should have been released | PASS | CBS2 | |
| 69 | Members can review redacted material; time-consuming; some say DOJ monitors searches; GAO announced investigation at lawmakers' request | PASS | CBS2 | |
| 70 | Chapter VII | PASS | n/a | |
| 71 | Nov 10 House Oversight (GOP) report; Chairman Comer "said the DOJ must interview key witnesses"; graphic quote "The Department of Justice must interview key witnesses, investigate everyone who participated in or facilitated these crimes." | FIX | Report and date PASS (KUOW). Quote NOT found: NBCB gives Comer as saying DOJ must "interview or re-interview key witnesses" and "investigate Epstein associates accused of criminal activity"; KUOW's only Comer quote is "Epstein operated with impunity, shielded and enabled by powerful connections." | Narration: "Chairman James Comer said the Justice Department must interview or re-interview key witnesses and investigate Epstein associates accused of criminal activity." Graphic q: "…must {{interview or re-interview key witnesses}} and investigate Epstein associates accused of criminal activity." source line: NBC Boston/NPR. If the verbatim cannot be confirmed in the final cut, CUT the graphic and keep the paraphrase |
| 72 | Garcia called the report "partisan and incomplete" (graphic quote "Partisan and incomplete.") | FIX | KUOW: Garcia called it "partisan" and said Republicans released it "based on an incomplete investigation" and without public hearings | Narration: "Robert Garcia called the report partisan, and said it was based on an incomplete investigation." Graphic q: "{{Partisan}}" ... "based on an incomplete investigation." |
| 73 | 218 on Nov 11; all Democrats + 4 Republicans (Massie, Mace, Norman, Fitzpatrick) | PASS | CBS3; RC; AX; GMA | |
| 74 | Bill: members of Congress, state AGs, local prosecutors, survivors can sue; victims can privately view unredacted records mentioning them | PASS | CBS3 (members, state AGs, survivors); RC (state AGs, local prosecutors, victims; private viewing); GMA | |
| 75 | Seven legislative days; Roll Call no vote date; "Axios reported a vote could come as early as December second or third" | FIX | RC: seven legislative days, no date PASS. AX gives no Dec 2-3 date ("eligible by early December"); the Dec 2 or 3 line is in GMA/ABC News | "ABC News reported floor action could come as early as December second or third." (DISPLAY entry unchanged) |
| 76 | Massie says DOJ still withholding 3M+ files, heavy redactions; graphic quote "Still withholding more than 3 million files … maintaining heavy redactions." Quoted by Roll Call | FIX | RC paraphrases Massie, only "maintaining heavy redactions" is in quotes; CBS3 verbatim (July statement): "The Department of Justice continues to unlawfully withhold over 3 million Epstein files that should be released to the public." | Graphic q: "The Department of Justice continues to {{unlawfully withhold over 3 million Epstein files}} that should be released to the public." role "Quoted by CBS News · July 2026 statement · DOJ disputes this"; or drop quote marks and set as paraphrase "as paraphrased by Roll Call" |
| 77 | Wrap-up and timeline (NOV 19 law, DEC 19, DEC 20, JAN 30, JUN CBS gaps, NOV 11 petition 218) | PASS | all above | |
| 78 | Audience question | PASS | n/a | |
| 79 | Next in series (votes) | PASS | internal | |

## C. Planned thumbnail words
| Thumbnail | Result | Note |
|---|---|---|
| A: "119 PAGES" / "ALL BLACK" | PASS | EFTA00005586, 119 pages, all black (DOC); CBS1 |
| B: "WHAT'S IN / THE EPSTEIN / FILES?" | PASS | Question only |
| C: "3 MILLION PAGES" / "WHAT'S MISSING?" | PASS (caution) | 3M+ pages released Jan 30 (SCR2/PBS) and ~3M unreleased per DOJ/Massie. Ambiguous; safer "3 MILLION+ PAGES" |

## D. Number-to-DISPLAY consistency
Mismatch only in line 40 (videos "about" vs "more than"); all other narration numbers match DISPLAY text (119, 255, 550, 180, 218, 427 to 1, 500 lawyers, 200 lawyers, 6 million, 2.5 million, 147 cameras, 69-page, 70 percent). Note DISPLAY has "two million and a half" but the script uses "two and a half million"; both map.

## E. Tally
Per-line (79): 61 PASS, 18 FIX, 0 CUT. FIX lines: 2, 3, 7, 22, 33, 40, 44, 47, 48, 52, 59, 63, 64, 66, 71, 72, 75, 76. Extras: A (4 document checks) PASS, thumbnails 3 PASS (C with caution).

## Applied (2026-11-24)
All FIX items from this review were applied to episode.py before the final build (verbatim quotes, DOJ-position balance lines, softened closing lines, thumbnail C reworded).
