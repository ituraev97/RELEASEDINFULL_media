# FILE 015 — independent fact-check

Checked against: DOJ OPR report (local per-page text `/home/claude/dl/opr/pg/<PDF page>.txt`), S.D.N.Y. indictment and S.D. Fla. opinion (`/home/claude/src/docs/`), and the news/court URLs in research.md (fetched 2026-11-16). Line numbers are 1-indexed positions in `LINES`. "pX" means OPR PDF page X.

Not verifiable from here: the DVIDS b-roll captions (the DVIDS page did not load; check that clip 1026930 really is F-22 cockpit footage before using "SEEN FROM AN F-22 COCKPIT").

## Summary of FIX items (17)

| # | Line | Issue | Severity |
|---|---|---|---|
| 1 | 15 | Wrong order: PBPD went to the FBI in May 2006, before the July 2006 indictment | High |
| 2 | 42 | "He registered as a sex offender" on plea day. He registered at release, July 22, 2009 (p143) | High |
| 3 | 57 | Only one victim filed on July 7, 2008. The second joined later (p4 fn 2, p139) | High |
| 4 | 79 | In re Wild had one petitioner, not "the two women" | High |
| 5 | 58 | "Deal stayed mostly out of public view": contradicts line 34 (NPA made public Sept 2009) | Medium |
| 6 | 29 | "Federal government would not prosecute him": the NPA bound only USAO-SDFL, which the episode itself says in lines 67 and 82 | Medium |
| 7 | 31 | "Came from a defense draft" leaves out that the language evolved from the prosecutor's own earlier draft (p105) | Medium |
| 8 | 33 | "The defense added it" + quote: the quoted wording is the prosecutor's revision of the defense clause (p109-110) | Medium |
| 9 | 4 | "Failed ... at nearly every turn" is Comer's statement, not a quoted report finding | Medium |
| 10 | 73 | On Nov 12, 2020 DOJ released the executive summary, not the full report | Medium |
| 11 | 87 | "Rushed" is Al Jazeera's word, not the report's | Medium |
| 12 | 93 | "a prosecutor's call" / "no victim was told about" / "Secret agreement": imprecise | Medium |
| 13 | 49 | "Can I indict him now?" has five words, not four | Low |
| 14 | 25 | "next eighteen years": 2007 to 2026 is 19 years | Low |
| 15 | 71 | "under that kind of watch" suggests he was under close watch | Medium |
| 16 | 88 | Page count: Al Jazeera 137, ABC 136 | Low |
| 17 | 94 | Says Congress is voting on whether "poor judgment" is enough. It is voting on releasing the files | Low |

Minor/cosmetic (also listed below): line 2 "up to"; line 55 graphic "18 → 13"; line 60 lab; line 62 source page; line 82 "in one sentence"; line 86 "largest batch so far"; line 79 graphic "The 2007 agreement stood."; line 43 lab (Stockade).

## Line-by-line

| Line | Claim (spoken / on-screen) | Verdict | Source | Proposed replacement (FIX only) |
|---|---|---|---|---|
| 1 | 2007, federal prosecutors in Florida drafted a 60-count indictment; never filed. Tag MAY 2007; lab P.51 | OK | p3 ("In May 2007 ... draft 60-count indictment"); p51 (memo dated May 1, 2007, "proposed 60-count indictment") | — |
| 2 | Pleaded guilty to two state charges; served less than 13 months; "for most of that time ... let out of jail twelve hours a day, six days a week"; graphic "SENTENCE: 18 MONTHS · SERVED: UNDER 13", "12 HRS" | FIX (minor) | p4 (two pleas), p5 ("12 hours a day", "less than 13 months"), p140-141 ("for up to 12 hours per day, six days per week", from Oct 10, 2008). Oct 10, 2008 to Jul 22, 2009 is about 9.4 of 12.7 months, so "most" holds | Spoken: "...and for most of that time, he was let out of jail for up to twelve hours a day, six days a week." Graphic a= "UP TO 12 HRS" (or keep "12 HRS" and set b="a day (up to), six days a week, outside the jail on work release") |
| 3 | DOJ investigated; verdict "poor judgment"; lab P.12 | OK | p12 | — |
| 4 | Nov 10, 2026 House committee report "said the federal government failed Epstein's victims at nearly every turn" | FIX | Al Jazeera: Comer said "These women endured unimaginable abuse, and the federal government failed them at nearly every turn". This is the chairman's statement, not a quoted report finding | "On November tenth, twenty twenty-six, a House committee released a report, and its chairman said the federal government failed Epstein's victims at nearly every turn." |
| 5 | How does a 60-count federal case become 13 months in a county jail | OK (rhetorical) | p3, p5 | — |
| 6-8 | Intro / title / chapter | OK | — | — |
| 9 | March 2005, parents of a 14-year-old told Palm Beach police a man paid their daughter $300 for a massage at his home; lab P.37 | OK | p37 (verbatim match) | — |
| 10 | Multi-millionaire financier, homes in Palm Beach, NYC, abroad; lab P.3 | OK | p3 ("residences in Palm Beach, New York City, and other United States and foreign locations") | — |
| 11 | Assistants recruited girls; in many instances led to sexual activity; lab P.3 | OK | p3 | — |
| 12 | Oct 2005 search: monitors, keyboards, disconnected cameras; computers gone; tag OCT 20, 2005; lab P.39-40 | OK | p39-40. Make sure the crop shows only the last lines of p39 (the rest of p39 has explicit victim descriptions) | — |
| 13 | State Attorney's office told DOJ investigators there were witness problems; offered 5 years' probation; he refused; lab P.40 | OK | p40 (Krischer: "there were witness problems"; Belohlavek offered five-year probation, rejected; fn 9) | — |
| 14 | July 19, 2006 state grand jury, single count felony solicitation of prostitution; did not mention minors; lab P.46 | OK | p46 | — |
| 15 | "The Palm Beach police chief and the lead detective were not satisfied. They took the case to the FBI." Comes right after the July 2006 indictment, so it implies the referral followed it | FIX | p42-44: Chief Reiter's May 1, 2006 letter; the detective met the AUSA and FBI in May 2006; USAO file opened May 23, 2006. All of this was before the July 19, 2006 indictment. (p3 summary gives the motive but not the timing) | "Even before that indictment, the Palm Beach police chief and the lead detective had grown dissatisfied with how the State Attorney was handling the case. | In May two thousand six, they took it to the F B I." (add DISPLAY entry "May two thousand six" → "May 2006") |
| 16 | "Now it was a federal case." | OK | — | — |
| 17 | AUSA in West Palm Beach opened a file with the knowledge of U.S. Attorney Acosta; lab P.3 | OK | p3 ("with her supervisor's approval and with the knowledge of then U.S. Attorney R. Alexander Acosta"). Note: Acosta was told on July 14, 2006 (p44), after the May 23 opening. The wording is still supported by p3 | — |
| 18 | Two FBI agents; more victims; by May 2007, 82-page memo and 60-count draft; graphic "60", "82-page", "never filed" | OK | p3, p51 | — |
| 19 | Immediate supervisor viewed case as prosecutable; decision went to front office in Miami; lab P.51 | OK | p51 ("viewed the case as prosecutable"; "front office involvement from the get-go"; approval in Miami) | — |
| 20 | Managers' concerns: legal issues, witnesses, impact of trial on victims; lab P.12 | OK | p12 | — |
| 21 | Acosta: case belonged first to state; federal role was a backstop. Quote graphic | OK | p12, verbatim: "the federal responsibility in this situation was to serve as a “backstop” to state authorities by encouraging them to do more." | — |
| 22 | Backstop = "a polite way of saying: encouraging the state to do a little bit more"; lab P.174 | OK | p174 (Acosta to OPR) | — |
| 23 | July 31, 2007 offer: end investigation if state plea, at least two years, register, damages mechanism; list graphic; lab P.3 | OK | p3 | — |
| 24 | Defense tried to drop registration; Acosta refused; "Alex will not agree to a non-registration offense", supervisor to prosecutor; lab P.105 | OK | p105 ("U can tell [J]ay that [A]lex will not agree to a nonregistration offense"); p12 (refused to eliminate registration) | — |
| 25 | "weeks of negotiations, and a document that would follow everyone involved for the next eighteen years" | FIX (minor) | July 31 to Sept 24, 2007 is about 8 weeks (OK). 2007 to 2026 is 19 years, and the story is still going | "...and a document that would follow everyone involved for nearly two decades." |
| 26 | Chapter | OK | — | — |
| 27 | Shortly after midnight Sept 24, 2007, Acosta sent final "small edits"; that afternoon signed copy came back; prosecutor emailed "It is done."; lab P.110 | OK | p110 (prosecutor wrote to "her immediate supervisor and her co-counsel"; "colleagues" is fine) | — |
| 28 | Plead guilty in state court to two charges incl. procuring a minor for prostitution; binding rec. 18 months county jail + 12 months community control; lab P.4 | OK | p4, p111 | — |
| 29 | "In return, the federal government would not prosecute him." Doc graphic: "The United States agreed not to prosecute:" | FIX | p4: the USAO agreed "to forgo federal prosecution in the Southern District of Florida". 2d Cir. (Maxwell, 2024): NPA "does not bind USAO-SDNY". As written, this contradicts lines 67 and 82 | Spoken: "In return, federal prosecutors in South Florida would not prosecute him. \| And not only him." Graphic title: "The U.S. Attorney's Office (S.D. Fla.) agreed not to prosecute:" |
| 30 | Four named people and "any potential co-conspirators"; lab P.105 | OK | p4, p105, p112 | — |
| 31 | "That language, the report says, came from a defense draft. The prosecutor kept it. I don't think it hurts us, she wrote."; lab P.106 | FIX | p105: the defense draft extended the clause to "any potential co-conspirators", but "This language had evolved from similar language that [the prosecutor] had included in the USAO's earlier proposed draft federal plea agreement" (fn 122). p106: "I don't think it hurts us" (verbatim OK) | "That exact phrase, the report says, came from a defense draft, which built on language from the prosecutor's own earlier draft. \| She kept it. \| I don't think it hurts us, she wrote." |
| 32 | Supervisor did not remember why the office agreed; lab P.106 | OK | p106 ("did not recall why the USAO agreed to it") | — |
| 33 | "There was one more clause. The defense added it. The parties anticipate that this agreement will not be made part of any public record." Quote graphic; lab P.110 | FIX | p109: the defense first proposed a confidentiality term with different wording ("It is the intention of the parties ... not be disseminated or disclosed except pursuant to court order"). The prosecutor then "changed the confidentiality provision to the following" (p109-110): the quoted "The parties anticipate..." text. The quote is verbatim, but its wording is the USAO's revision | "There was one more clause. \| The defense asked for it, and in the prosecutor's revised wording it went into the final deal: \| The parties anticipate that this agreement will not be made part of any public record." (Lab: P + "109-110") |
| 34 | Sept 2009, after victims and news organizations sued, state judge ordered it made public; lab P.5 | OK | p5 ("victims and news media filed suit") | — |
| 35 | Victims not informed of or consulted about the agreement before signing; lab P.4 | OK | p4 (verbatim) | — |
| 36 | Chapter | OK | — | — |
| 37 | Nine months; extensive team of prominent attorneys; change terms his own team had negotiated; lab P.4 | OK | p4 | — |
| 38 | Tried to invalidate whole agreement; "quintessentially state matter" to senior DOJ officials; tag WASHINGTON 2008 | OK | p4 | — |
| 39 | FBI letters "under investigation"; not false; risked misleading; lab P.13 | OK | p13 | — |
| 40 | June 2008 ODAG answered defense; would not intervene; "added a sentence the defense had not asked for"; tag JUNE 23, 2008; lab P.136 | OK | p4, p136 (the last phrase is the script's own framing and is fair) | — |
| 41 | Quote "Even if we were to substitute..."; role "Letter to Epstein's lawyers · June 23, 2008" | OK | p136, verbatim (letter to Starr and Lefkowitz) | — |
| 42 | June 30, 2008 plea; 12 + 6 months, then a year of community control; "He registered as a sex offender."; timeline graphic | FIX | p4 (plea and sentence OK); p143: "On July 22, 2009 ... released ... At this time, he registered as a sexual offender." p139-140: registration "would not take place until after Epstein completed his sentence" | Replace last sentence with: "He would have to register as a sex offender when he got out." |
| 43 | Began sentence same day in minimum-security county facility "called the Stockade"; walking out most mornings within months; lab P.4 | OK (lab note) | p4 (minimum-security county facility); the name "Stockade" is on p137/p139/p140, not p4. Work release from Oct 10, 2008 (p140) | Optional lab: P + "4" → P + "4, 139" if the Stockade wording should be sourced on screen |
| 44 | Chapter | OK | — | — |
| 45 | Up to 12 hours a day, six days/week, Florida Science Foundation; tag WEST PALM BEACH, OCTOBER 2008; lab P.140-141 | OK | p140-141 | — |
| 46 | At plea hearing: president, existed 15 years, worked there every day; lab P.140 FOOTNOTE | OK | p140 fn 181 | — |
| 47 | Per the prosecutor, entity did not exist until Nov 2007, two months after signing; address was lawyer's office; lab P.140 | OK | p140 (Sept 24 to Nov 2007 is "about two months") | — |
| 48 | Prosecutor had tried to stop this; office expected 18 months behind bars; never got notice of the application; lab P.140 | OK | p139-140 (asked Sheriff to notify; Acosta "aware [she] was trying to ensure that Epstein did not get work release"; "The USAO never received notice") | — |
| 49 | Mid-Nov 2008 found out; "She emailed her bosses a four-word question." | FIX | p141. "Can I indict him now?" has five words | "She emailed her bosses a five-word question." (or "She emailed her bosses one question.") |
| 50 | Quote "Can I indict him now?"; role "Email to her supervisors · November 2008" | OK | p141 (sent to Acosta, Sloman and the Criminal Division Chief) | — |
| 51 | Breach letter: 18 months = confinement 24 hours a day; in breach; lab P.141 | OK | p141 (Nov 24, 2008) | — |
| 52 | Defense: NPA did not prohibit work release; Florida law treated it as part of confinement; lab P.141-142 | OK | p141-142 | — |
| 53 | Letter to Sheriff: foundation's phone number = lawyer's law firm; no acknowledgment or response; labs P.142, P.143 | OK | p142, p143 | — |
| 54 | Never indicted for it; July 22, 2009, almost 13 months, released to home confinement; lab P.143 | OK | p143 | — |
| 55 | 18 on paper; under 13 in custody with gain time; graphic a="18 → 13", "months on paper, months in custody", "work release from October 2008" | FIX (minor) | p5 ("less than 13 months"). The graphic shows a flat "13" | Graphic a= "18 → <13" (or keep "18 → 13" and set b="months on paper · just under 13 months in custody") |
| 56 | Chapter | OK | — | — |
| 57 | "A week after his plea, in July 2008, two women filed suit as Jane Doe 1 and Jane Doe 2." Tag JULY 7, 2008; lab P.4 | FIX | p4 + fn 2: on July 7, 2008 "a victim, identified as 'Jane Doe'" filed; "Another victim subsequently joined the litigation as 'Jane Doe 2.'" p139 says the same. (The tag location is fine: case no. 9:08-cv-80736 is the West Palm Beach division) | "A week after his plea, on July seventh, two thousand eight, one of his victims went to federal court as Jane Doe. \| A second woman soon joined her as Jane Doe two. \| Their claim: the government broke the Crime Victims' Rights Act by keeping them in the dark." (DISPLAY: "July seventh, two thousand eight" → "July 7, 2008"; "Jane Doe two" → "Jane Doe 2") |
| 58 | "For a decade, the deal stayed mostly out of public view, and Epstein ... was otherwise able to resume his lavish lifestyle."; lab P.5 | FIX | p5: Epstein was able to "resume his lavish lifestyle, largely avoiding the interest of the press". The NPA itself was ordered public in Sept 2009 (p5; script line 34), so "the deal stayed out of public view" contradicts line 34 | "The case moved slowly. \| For a decade, the deal drew little press attention, \| and Epstein, the report says, was otherwise able to resume his lavish lifestyle." |
| 59 | By mid-2010, per report, settled multiple civil suits incl. the two women in that case; lab P.5 | OK | p5 ("reportedly settled ... including the two petitioners") | — |
| 60 | Nov 2018 Miami Herald investigation; led to public outrage; lab P.5 | FIX (lab) | Herald report (Nov 28, 2018) is on p5; "led to public outrage" is the first line of p6 | Lab: P + "5-6" |
| 61 | Feb 21, 2019, Judge Marra: government violated CVRA by failing to tell victims it intended to enter the agreement; lab P.6 | OK | p6; CNBC | — |
| 62 | "When the Government gives information to victims, it cannot be misleading." Graphic source "...DOJ OPR REPORT (2020), PDF P. 5" | FIX (source) | Quote verbatim per CNBC. The OPR description of the Feb 21, 2019 ruling is on p6, not p5 | source="SOURCE: CNBC (FEB. 21, 2019); DOJ OPR REPORT (2020), PDF P. 6" |
| 63 | "That same month, OPR opened its own investigation." | OK | opr.txt (report intro): on Feb 6, 2019 DOJ told Sen. Sasse that OPR had opened an investigation, so February 2019 is right. (OPR opened it before the Feb 21 ruling; "that same month" is accurate) | — |
| 64 | Chapter | OK | — | — |
| 65 | July 6, 2019, private plane from Paris landed at Teterboro; arrested; map | OK | WUSF/AP; p6 (arrest July 6, 2019) | — |
| 66 | SDNY charged sex trafficking and conspiracy; indictment alleged he sexually abused dozens of minor girls in NY and Palm Beach; pleaded not guilty; tag JULY 8, 2019; lab IND P.1 | OK | Indictment ("sexually exploited and abused dozens of minor girls at his homes in Manhattan, New York, and Palm Beach, Florida"); WUSF/AP (not-guilty plea) | — |
| 67 | U.S. Attorney in Manhattan: binds only SD Fla.; quote graphic | OK | WUSF/AP (Berman), verbatim | — |
| 68 | Two days later (July 10, 2019) Acosta press conference; "walk free with no jail time, nothing"; jail, registration, damages; lab P.6 | OK | p6 | — |
| 69 | July 12, 2019 resigned; "The right thing was to step aside." | OK | NPR (verbatim); p6-7 | — |
| 70 | Never stood trial; Aug 10, 2019 died in federal custody in Manhattan; ruled a suicide; graphic | OK | p7 (NYC Chief Medical Examiner concluded suicide); NPR/GPB 2026 | — |
| 71 | "How a man under that kind of watch died in a federal jail is its own file." | FIX | "Under that kind of watch" suggests he was under close watch or on suicide watch when he died. Nothing in this episode's sources supports that, and it hints at wrongdoing beyond the record. Leave it to the next episode's sources (OIG) | "How a man in federal custody died in a federal jail is its own file. \| We will open it in this series." |
| 72 | Chapter | OK | — | — |
| 73 | "On November 12, 2020, OPR released its findings. 348 pages." Tag NOV 12, 2020 | FIX | DOJ statement (Nov 12, 2020): the executive summary was released to victims and posted online; "The Privacy Act prohibits the Department from releasing the full report publicly". The full report went to Congress and became public later. The local PDF is 348 pages including exhibits and blank pages | "On November twelfth, twenty twenty, the Justice Department announced the findings and released a summary. \| The full report runs three hundred forty-eight pages." |
| 74 | No professional misconduct by any of the five prosecutors examined; lab P.12 | OK | p12; opr.txt ("all five subjects"; all five were attorneys/prosecutors) | — |
| 75 | No evidence of corruption, or of wealth, status or associations; Acosta refused to drop jail time and registration; lab P.12 | OK | p12 | — |
| 76 | "constitutes poor judgment"; quote graphic | OK | p12, verbatim | — |
| 77 | Federalism too expansive; federal interest too narrow; state system too imperfect | OK | p12 (report says "application of federalism principles was too expansive"; the paraphrase is fair) | — |
| 78 | Victims not treated with forthrightness and sensitivity expected by the Department; lab P.14 | OK | p13-14 (sentence begins on p13, ends p14); DOJ statement | — |
| 79 | "Months later, the full appeals court in Atlanta ruled against the two women in their thirteen-year lawsuit. Because no federal charge had ever been filed, it held, the law gave them no case to bring." Graphic "...{{The 2007 agreement stood.}}" | FIX | In re Wild (11th Cir. en banc, Apr. 15, 2021): the petitioner was one woman (Jane Doe 1, who filed the mandamus petition in her own name; opr p7). Holding: the CVRA gives no private right of action outside a preexisting proceeding, and none existed because no charges were filed. July 2008 to April 2021 is 12.8 years. The opinion did not rule on the NPA itself | Spoken: "Months later, the full appeals court in Atlanta ruled against Jane Doe one, who had carried the case for almost thirteen years. \| Because no federal charge had ever been filed, it held, the law gave her no case to bring." Graphic last line: "{{The victims' case ended there.}}" (instead of "The 2007 agreement stood.") |
| 80 | Co-conspirator clause tested in court; lab P.105 | OK | p105 | — |
| 81 | Dec 2021 Manhattan jury convicted Maxwell of sex trafficking a minor and other charges; 20 years; lawyers say innocent; tag DEC 29, 2021 | OK | WHYY/AP (Dec 29, 2021, five of six counts); 2d Cir. (240 months, sex trafficking of a minor); ABC/AP Oct 2025 (Markus: "innocent") | — |
| 82 | Appeal argued NPA protected her; 2024 appeals court "answered in one sentence"; quote | OK (optional tweak) | 2d Cir., verbatim "We hold that the NPA with USAO-SDFL does not bind USAO-SDNY." The opinion is long; the holding is one sentence | Optional: "...the federal appeals court in New York summed up its answer in one sentence." |
| 83 | Oct 2025 Supreme Court declined | OK | ABC/AP (Oct 6, 2025) | — |
| 84 | Chapter | OK | — | — |
| 85 | Nov 2025 EFTA passed; House 427-1; ordered DOJ to release Epstein and Maxwell files; graphic Massie/Khanna, Senate days later, signed | OK | Roll Call; AP (Jan 30, 2026) | — |
| 86 | Missed Dec 19 deadline; Jan 30, 2026 released 3M+ pages, 2,000+ videos, 180,000 images. Graphic title "The largest batch so far" | FIX (graphic) | AP via WFSB: numbers verbatim; "largest batch yet" was true as of Jan 2026. "So far" in a Nov 2026 video is unverified | Graphic title: "The largest batch at the time" |
| 87 | Names disclaimer; "a congressional report would later say the rushed release had deficient redactions that exposed sensitive information about victims" | FIX | Al Jazeera: report cites "deficient redaction" that "exposed sensitive information"; "rushed" is Al Jazeera's own description, not the report's | "...And a congressional report would later say deficient redactions in the released files exposed sensitive information about victims." |
| 88 | Nov 10, 2026, Oversight Committee led by Republican chairman James Comer released a 137-page report | FIX (minor) | Al Jazeera: "137-page report"; ABC: 136 pages. Sources disagree | "...released a report of more than one hundred thirty pages." (DISPLAY: "one hundred thirty pages" → "130 pages"), or keep 137 only after checking the committee PDF |
| 89 | Blamed poor judgment and Epstein's influence; Acosta's hands-off approach; crimes after 2005 could have been prevented; list incl. "re-interview witnesses" | OK | Al Jazeera; NPR/GPB ("if not for the 'failures' ... Epstein's crimes after 2005 could have been prevented"; "interview or re-interview witnesses") | — |
| 90 | Garcia: partisan, incomplete investigation, zero public hearings; DOJ: recommendations already addressed, case not closed; doc graphic | OK | NPR/GPB; ABC ("the Attorney General has repeatedly said that the Epstein case is not closed") | — |
| 91 | One day later, Massie's petition reached 218, both parties; graphic Garamendi 218th | OK | Roll Call | — |
| 92 | New bill: AGs, local prosecutors, victims may sue; victims view unredacted records | OK | Roll Call | — |
| 93 | "a prosecutor's call that a state case was enough, an agreement no victim was told about, and a work release program that let him leave six days a week"; timeline "Secret agreement" | FIX | p12: the state-based resolution was Acosta's decision, not the line prosecutor's (she opposed it and wanted to indict, p141, p174). p4: victims were not told before signing; some were told of a state resolution later (p13). The NPA had a confidentiality clause; OPR warns against the "misimpression" that the government colluded to keep it secret (p13) | Spoken: "...a U S Attorney's call that a state case was enough, \| an agreement victims were not told about before it was signed, \| and a work release program that let him leave six days a week." Timeline: t="Confidential agreement" (instead of "Secret agreement") |
| 94 | "The review found poor judgment, not misconduct. Whether that is enough is the question Congress is still voting on." | FIX (minor) | The bill is about releasing records (Roll Call), not about the OPR verdict | "...Whether the full record is out yet is the question Congress is still voting on." |
| 95 | Tagline | OK | — | — |
| 96 | Viewer question | OK | — | — |
| 97 | Next: federal jail, Inspector General | OK | — | — |
| META | Title "How Epstein Got 13 Months" / "60 Federal Counts Became 13 Months" | OK | "almost 13 months" (p143) | — |
