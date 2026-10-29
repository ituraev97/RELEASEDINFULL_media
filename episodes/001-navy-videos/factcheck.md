# FILE 001 — Independent fact-check (script_for_factcheck.md)

Checked 2026-10-29 by an independent reviewer. Every claim below was checked against a page opened in this session, using WebFetch only (no WebSearch, and curl was blocked).
**Could not open:** war.gov/defense.gov statement page, the AARO GoFast PDF (site error), nymag.com, washingtonpost.com, the Black Vault 2022 Navy FOIA article, the ODNI annual-report PDF itself.
- The DoD statement wording was checked against the full block quote reproduced by TWZ and the Black Vault FOIA PDF (21-F-1458), which contains the full statement text.

Verdicts:
- **OK**: supported as written.
- **FIX**: wrong or overstated. Change it.
- **ATTRIBUTE**: true only as someone's claim. Add the attribution.
- **UNVERIFIED**: no source could be opened. This does not mean the claim is wrong.

## Key sources opened
- **[DODCARDS]** https://documents2.theblackvault.com/documents/dod/21-F-1458.pdf: DoD briefing cards, plus the full 27 Apr 2020 statement.
- **[TWZ]** https://www.twz.com/33179/navy-officially-releases-infamous-ufo-videos: the 2020 statement block-quoted.
- **[REG]** https://www.theregister.com/2020/04/27/dod_ufo_video/
- **[FRAVOR]** https://oversight.house.gov/wp-content/uploads/2023/07/David-Fravor-Statement-for-House-Oversight-Committee.pdf
- **[GRAVES]** https://oversight.house.gov/wp-content/uploads/2023/07/Ryan-HOC-Testimony.pdf
- **[HEARING]** https://www.govinfo.gov/link/chrg/118/53-022: transcript, Serial No. 118-53.
- **[CBS21]** https://www.cbsnews.com/news/navy-ufo-sighting-60-minutes-2021-05-16
- **[CBS23]** https://www.cbsnews.com/amp/news/tic-tac-ufo-sighting-uap-video-dave-fravor-alex-dietrich-navy-fighter-pilots-house-testimony
- **[NBC]** https://www.nbcnews.com/news/us-news/navy-confirms-videos-did-capture-ufo-sightings-it-calls-them-n1056201
- **[FOXLA]** https://www.foxla.com/news/ufo-videos-are-footage-of-real-unidentified-objects-us-navy-acknowledges (18 Sep 2019)
- **[NYT17]** https://seclists.org/interesting-people/2017/Dec/57: NYT text, Dec 2017.
- **[SBS]** https://www.sbs.com.au/news/wow-what-is-that-us-navy-pilots-report-unexplained-flying-objects: NYT story, 29 May 2019.
- **[BVTIC]** https://www.theblackvault.com/casefiles/the-vault-files-the-tic-tac-incident-november-14-2004/
- **[MB]** https://www.metabunk.org/posts/220136/: GOFAST thread, 9 Mar 2018.
- **[MBG]** https://www.metabunk.org/threads/the-gimbal-ufo-marik-claims-new-findings-falsify-prosaic-explanations.14839/
- **[WIKI-PV]** https://en.wikipedia.org/wiki/Pentagon_UFO_videos (used as a map only)
- **[WIKI-26]** https://en.wikipedia.org/wiki/United_States_UAP_files (used as a map only)
- **[ODNI]** https://www.intelligence.gov/assets/documents/702 Documents/declassified/Prelimary-Assessment-UAP-20210625.pdf
- **[NPR]** https://www.npr.org/2023/01/13/1149019140/ufo-report
- **[NASA]** https://science.nasa.gov/wp-content/uploads/2023/09/uap-independent-study-team-final-report.pdf
- **[BVGF]** https://www.theblackvault.com/documentarchive/pentagon-releases-aaro-report-on-go-fast-video-analysis/
- **[DG]** https://www.dailygrail.com/2025/02/not-so-gofast-uap-government-office-presents-analysis-of-navy-video/
- **[AAROCR]** https://www.aaro.mil/UAP-Cases/UAP-Case-Resolution-Reports
- **[BVHRR]** https://www.theblackvault.com/documentarchive/report-on-the-historical-record-of-u-s-government-involvement-with-unidentified-anomalous-phenomena-uap-volume-i/amp
- **[ROLL]** https://rollcall.com/2024/03/08/no-evidence-of-extraterrestrial-technology-report-finds/
- **[DS]** https://defensescoop.com/2024/08/26/leader-pentagon-uap-investigation-hub-jon-kosloski/
- **[BVFY25]** https://www.theblackvault.com/documentarchive/aaro-releases-fy2025-uap-report-months-after-statutory-deadline-citing-319-new-cases-and-expanded-satellite-analysis/
- **[BURL]** https://burlison.house.gov/media/press-releases/house-adopts-burlison-amendment-establishing-uap-disclosure-framework
- **[NSA]** https://nsarchive2.gwu.edu/news/20010430/: Northwoods.

## Line-by-line

| Line | Claim | Verdict | Evidence | Suggested exact replacement |
|---|---|---|---|---|
| L1 | Navy targeting camera locked on something over the Atlantic. Tag and labels: GOFAST, Jan 2015 | OK | [AAROCR] (GoFast, Jan 2015, above the Atlantic off Florida); [MB] | — |
| L2 | "Pilots can't tell what it is. You can hear it in their voices" (over GIMBAL) | OK (interpretive) | [MB]: crew audio includes "What is that thing?" | — |
| L3 | Clips were leaks, "copies of copies" online. FLIR1 label Nov 2004 | OK | [DODCARDS], [BVTIC] | — |
| L4 | April 2020 DoD release. B-roll labelled "USS NIMITZ, 2026" | OK | [TWZ]; labelled as b-roll | — |
| L5 | DoD released 3 videos and said they were "unidentified." Doc-graphic excerpts | OK text / **FIX graphic** | [TWZ], [DODCARDS]. All three excerpt lines match the statement wording ("has authorized the release of three unclassified Navy videos", "to clear up any misconceptions by the public", "aerial phenomena observed in the videos remain characterized as 'unidentified.'"). The real statement is a press release and has no "RELEASED" stamp. | Remove `"stamp": "RELEASED"` |
| L9 | "Three clips. Two oceans. A decade apart." | OK | Nov 2004 vs Jan 2015 is just over 10 years | (optional) "More than a decade apart." |
| L10 | 14 Nov 2004, Nimitz CSG, ~100 mi SW of San Diego. Map source cites "FRAVOR STATEMENT TO HOUSE OVERSIGHT" | **FIX (source)** + ATTRIBUTE | [CBS23]/[CBS21]: "about 100 miles southwest of San Diego" is what "Fravor told 60 Minutes". [FRAVOR] does **not** mention San Diego or 100 miles. The DoD card only says "off the west coast" [DODCARDS]. | Spoken: "…training off Southern California. According to CBS News, about a hundred miles southwest of San Diego." Map source: `SOURCE: CBS NEWS / 60 MINUTES, 2021` |
| L11 | Cmdr. David Fravor led a two-jet flight sent to check an unknown contact | OK (attributed) | [FRAVOR]: CO of VFA-41, retired Commander. [HEARING]: "Commander David Fravor (Ret.)" | — |
| L12 | Quote "…a small white Tic Tac shaped object…" | OK (verbatim) | [FRAVOR] | — |
| L13 | Princeton tracked objects ~2 weeks, descending from high altitude. "Radar data has never been made public" | OK (attributed) / UNVERIFIED last sentence | [FRAVOR]: "previous 2 weeks", "descending from above 80,000ft… to 20,000ft". No source opened confirms that no radar data has ever been released (2026 PURSUE batches not checked). | "That radar data has not been publicly released." |
| L14 | A second crew went up later that day and filmed with the IR pod. No sound | OK | [FRAVOR]: "one of my crews who were getting ready to launch… took the now famous approximately 90 second video". [BVTIC]: "no audio in the released version" | — |
| L15 | IR camera sees heat. White-hot/black-hot. Locks on miles away | OK (general explainer) | Standard FLIR polarity. [BVTIC]: FLIR1 "switches modes and zoom settings" (not all IR). | (optional precision) "The camera inside that pod can see heat, not just visible light." Check that the clip at 44 s is in IR mode, not TV mode. |
| L16 | Officer whose crew recorded it never saw the object with his own eyes | ATTRIBUTE (name the source) | [BVTIC]: Underwood "did not see the Tic Tac with his own eyes". NYMag (2019) not openable; cited via [WIKI-PV]. "Officer whose crew" is imprecise: Underwood is the aviator credited with recording it. | "Chad Underwood, the aviator credited with recording it, told New York Magazine in 2019 that he never saw the object with his own eyes. Only on the screen." |
| L17 | GIMBAL/GOFAST Jan 2015, USS Theodore Roosevelt, off the East Coast | OK | [AAROCR] (GoFast, Jan 2015, off Florida); [WIKI-PV] | — |
| L18 | "According to NYT, the pilots were from VFA-11 Red Rippers. Those two clips got the names GIMBAL and GOFAST." | **FIX** | [SBS]/NYT 2019 says VFA-11 pilots reported the sightings and mentions "a plane's camera in early 2015". It does **not** say the GIMBAL/GOFAST pilots were VFA-11 and does not name the clips. [GRAVES] says GIMBAL was "recorded by my squadron". He does not tie GOFAST to it. | "According to The New York Times, pilots from Strike Fighter Squadron Eleven, the Red Rippers, reported strange objects off the East Coast in 2014 and 2015. The two clips from that January became known as GIMBAL and GOFAST." |
| L20–L22 | GOFAST readouts: jet ~25,000 ft, camera angle below horizon, RNG in nautical miles | OK | [MB]: 25,000 ft baro, −26°, 4.4 NM; [DG]: jet ~25,000 ft | — |
| L24 | 2004 video posted online in 2007 without permission, per a DoD FOIA briefing card | OK | [DODCARDS]: "In 2007, one of those crewmembers posted the video onto the public web." Statement: "someone aboard ship shared the video without authorization." Graphic is labelled summary/recreated and invents no quote. | — |
| L25 | "Few people noticed. That changed ten years later." | OK | [BVTIC]: 2007 copy "gained little notice"; 2017 is 10 years later | — |
| L26 | 16 Dec 2017, NYT story on secret program, with FLIR1 + GIMBAL. Timeline "2018 GOFAST surfaces" | OK | [NYT17], [WIKI-PV], [BVTIC]; [MB] (GOFAST thread 9 Mar 2018) | — |
| L27 | "The same day, To The Stars Academy put them out too. GOFAST surfaced a few months later." | UNVERIFIED ("same day") | [BVTIC] only says "first published by the NYT and To The Stars Academy in December 2017". "Same day" was not confirmed. [MB] confirms TTSA released GOFAST around Mar 2018. | "That same month, a private company called To The Stars Academy put them out too. A third clip, GOFAST, surfaced a few months later." |
| L28 | Pentagon said the 2015 clips reached the press via an "unauthorized release". "In its own words, the Navy had no information on how they got into circulation." | **FIX (quote framing)** | [DODCARDS]: "These same videos had been published by NYT in December 2017, via an unauthorized release" (about all three) and "With respect to the other two videos, Navy has no information on how they were released into general circulation." "In its own words" signals a verbatim quote, but the script paraphrases. | Spoken: "…In the Pentagon's own words, the Navy had 'no information on how they were released into general circulation.'" Graphic line 2: `"Navy has no information on how they were released into general circulation."` Graphic line 1: `"…published by NYT in December 2017, via an {{unauthorized release}}."` |
| L29 | NYT: $22M. DoD: studied foreign aerospace threats, ended 2012, disputes "UFO program" | OK | [NYT17]: "$22 million spent on the Advanced Aerospace Threat Identification Program". [DODCARDS]: "AATIP… ended in 2012", "foreign advanced aerospace weapons system applications", "UFO Program.' It was not." | — |
| L30 | "But nobody official had said a word about them." | **FIX (overclaim)** | DoD officials did comment on AATIP in Dec 2017 ([NYT17]), and the Navy discussed UAP reporting in 2019. What was missing was official confirmation of the videos. | "So now the videos were everywhere. But nobody official had confirmed they were real." |
| L31–L32 | Sept 2019, Gradisher: "…copies of official Navy footage…" | OK (verbatim) | [NBC]; [FOXLA] dated 18 Sep 2019 | — |
| L33 | Navy considers objects unidentified; incursions into training ranges | OK | [FOXLA]: "The Navy considers the phenomena… as unidentified". [NBC]: "incursions into our military training ranges" | — |
| L34 | TTSA said the videos were approved for public release. Gradisher said they were not | OK | [NBC]; [DODCARDS]: "DOPSR did not grant final approval…" | — |
| L35 | UAP term (Navy 2019). Current term "unidentified anomalous phenomena" | OK | [FOXLA], [NBC], [HEARING] title | — |
| L36 | 27 Apr 2020 statement. Excerpt "…does not reveal any sensitive capabilities or systems…" | OK text / **FIX graphic** | [TWZ], [REG]. Same invented "RELEASED" stamp as L5. | Remove `"stamp": "RELEASED"` |
| L37 | "Unclassified… already leaked, now released on the record" | OK | [TWZ], [DODCARDS] | — |
| L38 | Reason: clear up misconceptions about whether the footage was real | OK | [REG] | — |
| L39 | Stat: "UNIDENTIFIED: the official status of all three objects" | OK (in context of the 2020 statement) | [TWZ] | (optional) b: "the official status of all three objects in 2020" |
| L40 | In 2022 the Navy confirmed it holds other UAP videos, refused release, "harm national security" | OK / ATTRIBUTE context | [WIKI-PV] (map): Sept 2022, Navy FOIA deputy director Gregory Cason: "The release of this information will harm national security…", in reply to a Black Vault FOIA. Primary article not openable. | "In twenty twenty-two, answering a Freedom of Information Act request, the Navy confirmed it holds other U A P videos, but refused to release them. It said releasing them would harm national security." |
| L42 | July 2023 hearing. All sworn. Serial 118-53, title, witnesses | OK | [HEARING]: 26 Jul 2023, "[Witnesses are sworn.]" | — |
| L43 | Quote "…a white Tic Tac object…". Within about half a mile | OK (verbatim) | [HEARING]: "saw a white Tic Tac object", "within about a half mile of it" | — |
| L44 | Object turned toward jet, climbed, accelerated, gone | OK (attributed: "in his account") | [FRAVOR]: "rapidly accelerated and disappeared" | — |
| L45 | Wingman Alex Dietrich didn't testify. 2021 TV interview: no predictable trajectory | OK | [CBS21] (60 Minutes, 16 May 2021): "No predictable movement, no predictable trajectory". [HEARING]: not a witness. Fravor calls her "the other pilot in my flight" [FRAVOR]. | (optional) "The pilot of the other jet in his flight, Alex Dietrich, did not testify. But in a twenty twenty-one 60 Minutes interview…" |
| L46 | Felt exposed, nothing to defend themselves | OK (spoken paraphrase) | [CBS21]: "I felt the vulnerability of not having anything to defend ourselves" | — |
| L47 | Graves, former Red Rippers pilot, "the squadron behind GIMBAL and GOFAST" | **FIX** | [GRAVES]: "former F-18 pilot", VFA-11, "the full GIMBAL video recorded by my squadron". He mentions GO-FAST only as "from a Navy F/A-18". No source ties GOFAST to VFA-11. | "Then there's Ryan Graves, a former pilot with the Red Rippers. According to Graves, his squadron recorded GIMBAL." |
| L48 | 2019 NYT: pilots saw objects almost every day, for months. Stat "ALMOST DAILY", 2014–2015 | OK (attributed) | [SBS]: "appeared almost daily from the summer of 2014 to March 2015" | (optional) Stat c: delete "no confirmed explanation published" (not sourced), or change it to "according to the pilots" |
| L49 | Graves relayed another pilot's report: "…a dark gray cube inside of a clear sphere…", off Virginia Beach | OK quote / **FIX role label** | [GRAVES] (written): "a dark gray cube inside of a clear sphere", W-72, "ten miles east of Virginia Beach". Orally he said "dark gray or a black cube" [HEARING], so the quote is verbatim only from the written statement, not the sworn oral testimony. | role: `"relaying another pilot's report · written statement, July 2023"` |
| L50 | Grusch, "former intelligence official", told of a secret crashed-craft recovery program | OK (attributed) | [HEARING]: "a former senior intelligence officer…". Said he was told of the program. | (optional) "a former intelligence officer" |
| L51 | Grusch: testimony based on what others told him. Pentagon: no verifiable evidence. Doc graphic | OK spoken / **FIX graphic** | [HEARING]: "My testimony is based on information I have been given by individuals". [BVHRR]: "no verifiable evidence" belongs to the **access/reverse-engineering** finding. The sighting finding reads "no evidence that any U.S. government investigation… confirmed" a UAP "represented extraterrestrial technology". The graphic attaches "no verifiable evidence" to the wrong finding. | Graphic lines: `"Found {{no evidence}} that any U.S. government investigation confirmed a UAP sighting represented extraterrestrial technology."` and `"{{No verifiable evidence}} that the U.S. government or private companies have access to, or have reverse-engineered, extraterrestrial technology."` |
| L53 | June 2021 ODNI, 144 reports from USG sources (2004–2021) | OK | [ODNI]: "144 reports originated from USG sources", Nov 2004–Mar 2021 | — |
| L54 | One explained: large, deflating balloon. Other 143 unexplained | OK | [ODNI] | — |
| L55 | 80 multi-sensor. "Eighteen incidents showed unusual movement." 11 near-misses | **FIX (wording)** | [ODNI]: "In 18 incidents, described in 21 reports, observers **reported** unusual UAP movement patterns or flight characteristics." The script states as fact what ODNI attributes to observers. "11 reports of documented instances in which pilots reported near misses" | "…In eighteen incidents, observers reported unusual movement or flight characteristics. And in eleven, pilots reported near-misses." Graphic item 2: `"incidents where observers reported unusual movement"` |
| L56 | Five categories, including "Secret U S programs" | FIX (minor) | [ODNI]: "USG or U.S. industry developmental programs". "Secret" is not the category name. Graphic item 03 is correct. | "…U S government or industry programs…" |
| L57 | AARO created "a year later". First count, early 2023, 510 reports by Aug 2022 | OK | [DS]: AARO est. July 2022 (Hicks). [NPR]: 510 as of end Aug 2022; report released Jan 2023 by ODNI with AARO | — |
| L58 | "Of those [510], 163 balloons, 26 drones, 6 clutter, 171 uncharacterized" | **FIX (math/scope)** | [NPR]: the breakdown covers the **366** newer reports (247 new + 119 late), not 510. 163+26+6+171 = 366. Also "balloons or balloon-like entities", and these are initial characterizations. | "Of the three hundred sixty-six newer reports in that set, one hundred sixty-three were characterized as balloons or balloon-like objects. Twenty-six as drones. Six as clutter. And one hundred seventy-one were still uncharacterized." Graphic title: `"What 366 new reports turned into"`. Item 1: `"balloons or balloon-like"` |
| L59–L61 | Bridge and geometry explanation | OK | [NASA] | — |
| L62 | NASA 2023: ~13,000 ft, roughly halfway between jet and sea | OK | [NASA]: "the object is at an altitude of 13,000 feet". Jet ~25,000 ft [MB]/[DG] | — |
| L63 | ~40 mph, roughly wind speed at that height | OK | [NASA]: "average speed of 40 mph", "typical wind speed at 13,000 feet", "most likely drifting with the wind" | — |
| L64 | Jet doing hundreds of mph. Parallax | OK | [NASA]: jet ~435 mph; "parallax effect" | (optional) "The object moves far slower than it seems." Avoid "barely moves" (~40 mph). |
| L65 | Feb 2025 AARO: same altitude and explanation, "consistent with something small, like a balloon". Graphic adds "RESOLVED" stamp and "true speed" | **FIX** | [BVGF]: dated 6 Feb 2025; ~13,000 ft; "apparent high speed is attributable to motion parallax"; 5–92 mph "depending on wind"; consistent with "a small airborne object such as a balloon **or drone**". AARO PDF itself could not be opened. Dropping "or drone" overstates the balloon case. [DG] shows the speed basis is ambiguous. | Spoken: "…It said the object was consistent with something small, like a balloon or a drone." Graphic line 3: `"Estimated speed: 5 – 92 mph, depending on wind."` Line 4: `"Assessment: consistent with a small airborne object, such as a balloon or drone."` Remove the "RESOLVED" stamp unless it appears on the actual card (not verified). |
| L66 | Original file and data lost. Worked from public 34-second clip. Never identified the object | OK | [DG]: "publicly available 34-second FLIR video", "the original file and its accompanying metadata are no longer available". [BVGF] | — |
| L67 | Critics: no pilot interviews, no size estimate | ATTRIBUTE | [DG]: the author of the critique, The Daily Grail's Red Pill Junkie, raised both points | "Critics, including writers at The Daily Grail, have pointed out other gaps. They say AARO didn't interview the pilots, and it didn't estimate the object's size." |
| L69 | GIMBAL glare theory: disputed, no government body has endorsed or ruled it out. List item "A craft that rotates itself" | OK spoken / FIX graphic item | [MBG]: critics argue "it could be the actual object rotating". [AAROCR]: no GIMBAL resolution. "Craft" implies a vehicle, which goes beyond the critics' claim. | Item 2: `{"n": "CLAIM", "t": "The object itself rotates", "s": "critics of the glare theory"}` |
| L70 | FLIR1: no official explanation from Navy or AARO | OK | [AAROCR] lists no Tic Tac/FLIR1. [TWZ] (2020: "unidentified") | — |
| L72 | WaPo: president directed agencies in Feb 2026 to identify and declassify UAP files | UNVERIFIED (primary) / OK as attributed | [WIKI-26]: Trump "ordered federal agencies to identify and declassify…", citing WaPo 19 Feb 2026 ("Trump says he will release…"). WaPo not openable. The headline wording ("says he will release") is softer than "directed". | Keep the attribution. Confirm the WaPo text before publishing. Timeline: `"JUL 22" → "House adopts disclosure amendment"` (it was adopted as an NDAA amendment, not passed as a bill) |
| L73 | May: Pentagon launched release website, in batches. July: AARO report, 319 new, 370 resolved | OK | [WIKI-26]: PURSUE 8 May 2026, batches 8 May / 22 May / 12 Jun. [BVFY25]: 319 new, 370 resolved, released July 2026 | — |
| L73–L74 footage | AARO DVIDS 961723 labelled "OFFICIAL AARO VIDEO · MIDDLE EAST, 2023" over "every one of those resolved cases had an ordinary explanation" | **FIX (footage context)** | Research pack (DVIDS 961723) titles it "**Unresolved** UAP Report: Middle East 2023". Showing an unresolved case while narrating resolved ones is misleading. | Label: `OFFICIAL AARO VIDEO · UNRESOLVED CASE, MIDDLE EAST 2023`, and don't use it under L74. Use neutral b-roll there instead. |
| L74 | All resolved cases had ordinary explanations, per AARO | OK | [BVFY25]: "every resolved case was attributed to ordinary explanations" | — |
| L75 | July: House approved amendment creating UAP records collection at National Archives. Not yet law | OK (as of July). Final NDAA status as of late Oct 2026 UNVERIFIED | [BURL]: adopted 22 Jul 2026 in the FY2027 NDAA; "not yet law" | Re-check Senate/conference status on publish day |
| L77 | GOFAST official answer: "most likely something small, drifting on the wind" | OK | [BVGF]/[AAROCR]: ~13,000 ft, moving with the wind, small object. [NASA]: "most likely drifting with the wind" | — |
| L78 | Other two still officially unidentified; not alien | OK | [AAROCR], [TWZ] | — |
| L79 | Closing | OK | — | — |
| L80 | Northwoods: JCS plan on paper in 1962; staged attacks to justify war with Cuba | OK (minor precision) | [NSA]: 13 Mar 1962 JCS memo to McNamara, "Justification for U.S. Military Intervention in Cuba", proposing pretext attacks | (optional) "…Staged attacks, to justify a U.S. invasion of Cuba." |
| Credit | Navy videos: U.S. Navy / NAVAIR FOIA. B-roll via DVIDS | OK | Research pack, [TWZ] (NAVAIR FOIA reading room) | — |

## MUST-FIX list
1. **L58 and its graphic: wrong denominator.** 163 balloons, 26 drones, 6 clutter and 171 uncharacterized are a breakdown of the **366** newer reports, not the 510 total (163+26+6+171 = 366). Also say "balloons or balloon-like".
2. **L65 and its graphic: dropped "or drone".** AARO said the object was consistent with a small object "such as a balloon or drone". Restore "or drone", change "true speed" to "Estimated speed: 5–92 mph, depending on wind", and remove the unverified "RESOLVED" stamp.
3. **L18 and L47: GOFAST is not linked to VFA-11.** The NYT does not tie the videos to VFA-11. Graves ties only **GIMBAL** to his squadron. Remove "the squadron behind GIMBAL and GOFAST" and the implied NYT attribution.
4. **L51 graphic: "no verifiable evidence" is on the wrong finding.** AARO used "no verifiable evidence" for the access/reverse-engineering finding. The sighting finding says "no evidence that any USG investigation confirmed…". Swap the wording.
5. **L28: paraphrase presented as a quote.** "In its own words" is followed by a paraphrase. Use the real wording: "Navy has no information on how they were released into general circulation." Fix the graphic too.
6. **L5 and L36: invented "RELEASED" stamp.** The DoD statement graphics carry a stamp the real press statement doesn't have. Remove it.
7. **L73–L74 footage: unresolved case shown over resolved cases.** The AARO "Middle East 2023" clip is an **unresolved** case and is shown under "every resolved case had an ordinary explanation". Relabel it as unresolved and move it off L74.
8. **L10 map source.** Fravor's House statement does not contain "100 mi SW of San Diego". That comes from CBS / 60 Minutes. Fix the on-screen source and attribute the distance.
9. **L55: ODNI says observers reported it.** In ODNI's wording, observers *reported* unusual movement in 18 incidents and pilots *reported* 11 near-misses. Don't state either as established fact.
10. **L30: overclaim.** "Nobody official had said a word about them" goes too far. Change it to "nobody official had confirmed they were real."
11. **L67: name the critics.** Attribute the "no pilot interviews / no size" points to the critics who made them (e.g. The Daily Grail).
12. **L49 role label.** The quote is verbatim from Graves's **written statement**. Orally he said "dark gray or a black cube". Change the role to "written statement".

**Should-fix:**
- **L27:** "same day" (TTSA) is unverified. Use "that same month".
- **L16:** name Underwood and the NY Mag source.
- **L40:** add "answering a FOIA request".
- **L56:** replace "Secret U S programs" with "U S government or industry programs".
- **L69:** change "A craft that rotates itself" to "The object itself rotates".
- **L72:** use "House adopts" in the timeline and confirm the WaPo wording.
- **L13:** "never made public" becomes "not publicly released".
- **L75:** re-check NDAA status on publish day.
