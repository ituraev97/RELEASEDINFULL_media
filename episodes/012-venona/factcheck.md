# FILE 012 — VENONA: fact-check (independent)

Checked 2026-11-10 against the primary VENONA scans in `/home/claude/src/ven/` (page images read directly, not just the OCR), the two Army ICoE articles (saved DVIDS HTML), DVIDS asset metadata (API), frames pulled from the b-roll clips at the exact cue times, and the official sources below. The proxy blocked direct curl to cia.gov, nsa.gov, defense.gov and af.mil, so those were read through WebFetch.

**Sources actually opened**
- [1585] `/home/claude/src/ven/12nov_possible_new_recruit` (txt + page images); [1699] `2dec_manhattan_project_scientists`; [1606] `hi_16nov_klaus_fuchs_harry_gold-1.png`; [1600] `hi_14nov_recruitment_by_rosenberg-1.png`; [1657] `hi_27nov_mrs_rosenberg-1.png`; doc crops `/home/claude/src/img/doc/*`
- [ARMY46] https://www.dvidshub.net/news/487461 (saved as news487461.html)
- [ARMY95] https://www.dvidshub.net/news/575072 (saved as news575072.html)
- [ALM] https://media.defense.gov/2021/Jun/29/2002752012/-1/-1/0/VENONA_AN_OVERVIEW.PDF
- [BENSON] https://webarchive.library.unt.edu/eot2008/20080920021555/http://www.nsa.gov/publications/publi00039.cfm
- [BW] https://www.cia.gov/resources/csi/static/Venona-Front-Matter-Introduction-chronology-abbreviations.pdf
- [NSA18] https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/history-today-articles/06%202018/19JUN2018%20A%20Highly%20Controversial%20Case%20of%20Espionage%20-%20A%20Summary.pdf
- [FBI] https://www.fbi.gov/history/famous-cases/atom-spy-caserosenbergs
- [STEURY] https://www.cia.gov/resources/csi/static/CIA-Missed-Stalins-Bomb.pdf
- [AF] https://www.af.mil/News/Article-Display/Article/121177/aftac-continues-excellence-as-part-of-air-force-nuclear-enterprise ; [AFTAC] https://www.patrick.spaceforce.mil/Portals/14/AFTAC%20Fact%20Sheet%20as%20of%20September%202018.pdf
- [FRUS] https://history.state.gov/historicaldocuments/frus1949v01/d196 (found by WebSearch, for the Truman date)
- [DVIDS] `https://api.dvidshub.net/asset?...id=video:/image:` for every clip and image listed; frames extracted at each cue time.

**Result: 15 FIX items, 0 blocking factual errors.** Every date, number and name in the narration matches a source. The fixes are about attribution, over-claiming in the framing, and b-roll labels or juxtapositions.

## Title / hook framing

| # | Text | Verdict | Source | Replacement / note |
|---|---|---|---|---|
| META title / G title sub | "How Codebreakers Caught Stalin's Atomic Spies" | FIX (soft) | ARMY46, NSA18, FBI | The FBI and British authorities caught the spies. VENONA supplied the leads. NSA18 says the decrypts "could be used to stimulate investigations" and that "the FBI then had to develop evidence"; the episode's own line 70 says the same thing. Hall was never caught. Use: **"VENONA: How Codebreakers Helped Catch Stalin's Atomic Spies"**. If "Caught" stays for CTR, the body (lines 69 to 72) has to carry the nuance, as it now does. |
| 1, 69 | "How did America catch Stalin's atomic spies? Partly, by reading their mail." | OK | NSA18, FBI | "Partly" makes the claim accurate. |
| 7 / 72 | "never charged" (Hall) | OK | BW ("Special Agents questioned Hall in 1951, but he was never prosecuted") | "Never charged" and "never prosecuted" mean the same thing here. "Why" is supported by line 61, which says "probably". |

## Line-by-line

| # | Claim / on-screen text | Verdict | Source | Exact replacement (FIX only) / note |
|---|---|---|---|---|
| 1 | Telegram shown; tag NEW YORK · NOVEMBER 12, 1944; lab HALL | OK | 1585 | The cable is New York→Moscow, No. 1585, 12 Nov. 44. |
| 2 | KGB New York sent Moscow a coded message, Nov 1944, about a 19-year-old physicist | OK | 1585 | "19 years old … a talented physicist." |
| 3 | Son of a furrier; Harvard graduate | OK | 1585 | Verbatim from the cable. |
| 4 | In charge of a group at "Camp Two"; translators' notes say Los Alamos | OK | 1585 + notes [v] "CAMP-2: LOS ALAMOS" | The cable says "CAMP-2 (SANTA-FE)"; the note gives Los Alamos. |
| 5 | Report about the camp naming key personnel on ENORMOUS = KGB cover name for the Manhattan Project | OK | 1585 + note [vi] "Manhattan Engineering District – U.S. Atomic Energy Project" | |
| 6 | "Codes like this one were widely considered unbreakable. U S Army codebreakers broke into them anyway." | FIX | ARMY46 | ARMY46 is quoting the author Liza Mundy, so the claim needs attribution. → **"The Soviet system, the Army's historians write, was widely considered unbreakable. \| U S Army codebreakers broke into it anyway."** |
| 6 | Visual GARD label "Meredith Gardner (far left) with Army SIS cryptanalysts, 1940s" | OK | DVIDS image:8799384 | The caption matches the DVIDS description (DVIDS spells it "Merideth"). |
| 7 | "How Army codebreakers found the spies inside the atomic bomb project." | FIX | ARMY46 ("With the help of the FBI and British intelligence … several spies were eventually identified"), NSA18 | → **"How Army codebreakers helped expose the spies inside the atomic bomb project."** |
| 7 | trin_b with TRIN label | OK (see Trinity note) | DVIDS video:395453 | |
| 9 | Title card sub | FIX (soft) | see Title row | **"How Codebreakers Helped Catch Stalin's Atomic Spies"** |
| 11 | As early as 1939, the Army collected encrypted Soviet telegrams between Moscow and its intelligence offices in New York, Washington, etc. | OK | ARMY95 | The Army says "diplomatic telegrams … between Moscow and its KGB and GRU offices"; the script's paraphrase is fair. |
| 11 | lab NYC "BROOKLYN, NEW YORK, WITH THE MANHATTAN SKYLINE, 2025" (dv952451 @49s) | FIX | DVIDS video:952451 (Fort Hamilton aerial, Bay Ridge, Feb 11 2025) | At 49 s the skyline is only a faint smudge on the horizon, and DVIDS does not mention it. → **`NYC = "B-ROLL · AERIAL VIEW OF BROOKLYN, NEW YORK, 2025"`** |
| 11 | lab CAP on dv346026 @4s | OK | DVIDS video:346026 (2012) | The frame shows the Capitol. |
| 12 | Stored at Arlington Hall, Virginia | OK | ARMY95 | |
| 12 | dv346119 @2.0s labelled PENN "AVENUE LEADING TO THE U.S. CAPITOL" | FIX | frames at 2 to 7.5 s | From 2 to 7.5 s the clip is a close-up of the Capitol dome behind traffic lights, not an avenue. It also runs while the narration says Arlington Hall, Virginia. → change to **`lab=CAP`** (or cue the clip at 14.0 s, where the avenue shot is). |
| 13 | Feb 1, 1943; Col. Carter Clarke, Military Intelligence Division, ordered them examined; feared separate peace | OK | ARMY95; BW ("Clarke seemed particularly concerned that Moscow and Berlin might negotiate a separate peace") | |
| 13 | tag ARLINGTON HALL, VIRGINIA · FEBRUARY 1, 1943; TREAS / F22 b-roll | OK | ARMY95, DVIDS 346120 / 1026930 | The labels are accurate (the F-22 at 20 s shows the pilot, and DC is visible). |
| 14 | Gene Grabeel, 23, schoolteacher hired six weeks earlier | OK | ARMY95 | |
| 14 | Visual: Gardner photo, focus [0.6,0.45] (centred on an unidentified woman) | FIX | DVIDS image:8799384 | Centring on a woman in the SIS photo while naming Grabeel implies she is Grabeel, and that is not established. → use **`[I("hall_head", kb="in", focus=[0.5, 0.5], lab=HALL)]`** or a text card. If the photo stays, use `focus=[0.5,0.5]`, kb "out", and the label **"PHOTO · ARMY SIGNAL INTELLIGENCE SERVICE CRYPTANALYSTS, 1940s (INDIVIDUALS NOT IDENTIFIED BY THE ARMY, EXCEPT GARDNER, FAR LEFT)"** |
| 15 | Five systems: trading companies, Foreign Ministry, KGB (state intelligence), GRU (military intelligence), naval intelligence; source S_ARMY46 | OK | ARMY46 | |
| 16 | NSA: most valuable = secret agents' traffic, KGB and the two military services | OK | ALM ("KGB, the GRU, and GRU-Naval … proved the most valuable") | |
| 16 | TINA image, label "Moscow to London, Sept. 16, 1945 · NSA translation (via DVIDS)" | OK | DVIDS image:9948187; document shows From MOSCOW To LONDON No. 13, 16 Sept. 45 | |
| 18 | Three layers: code book → 4-digit group; → 5-digit figures; key added from one-time pad (graphic, S_ARMY46) | OK | ARMY46 (Mundy quote) | |
| 19 | One-time pad: pages of random numbers, each page never to be used again | OK | ARMY46 | |
| 20 | ~35,000 pages of duplicate key, wartime pressure, the factory that made the KGB's pads (stat card S_ALM) | OK | ALM | ALM says "company" rather than "factory"; the difference is acceptable. |
| 21 | Oct 1943, team under Lt. Richard Hallock found the first clues | OK | ALM ("Hallock and his team identified clues"); BENSON | |
| 21 | Visual list_head (a 1944 message) during the 1943 sentence | OK | label honest | |
| 22 | "In November 1944, the NSA says, Genevieve Feinstein, who had made the first break into PURPLE in 1940, found a way to spot the messages that shared a key." | FIX | ALM (Nov 1944, Feinstein, key groups sent in the clear); ARMY46 (PURPLE 1940) | The PURPLE claim comes from the Army, not the NSA, and the visual centres an unidentified woman in the SIS photo again. → **"In November nineteen forty-four, the N S A says, Genevieve Feinstein found a way to spot the messages that shared a key. \| According to the Army's historians, she had made the first break into Japan's PURPLE diplomatic cipher, in nineteen forty."** Change the visual to **`I("gardner", kb="out", focus=[0.5, 0.5], lab=GARD)`**, or replace it with a doc crop. |
| 23 | ~3,000 of many thousands sent 1940 to 1948 even partially read (stat S_ALM) | OK | ALM | |
| 25 | Gardner taught German at a university in Ohio; Japanese in 3 months; Russian after the war; rebuilt the KGB code book | OK | ARMY46 (University of Akron) | |
| 26 | Dec 20, 1946, broke into a KGB message sent to Moscow two years earlier; tag ARLINGTON HALL | OK | ARMY46 (Dec. 20, 1946); BENSON ("sent to Moscow Center two years earlier") | |
| 27 | Contained a list of Manhattan Project scientists | OK | ARMY46, BENSON | |
| 28 | NY message of Dec 1944 lists Bethe, Fermi, Lawrence, Teller | OK | 1699 (2 Dec 1944) | All four names appear in the list. |
| 26–28 | LIST label "No. 1699, Dec. 2, 1944 · NSA translation (1952)" | OK | 1699 "Issued … 21/5/1952" | |
| 29 | Army: the discovery proved the Manhattan Project had been infiltrated | OK | ARMY46 (near-verbatim) | |
| 29 | FATV dv395453 @136.9 "Fat Man-type bomb casing, National Museum of the USAF (USAF video, 2015)" | OK | DVIDS video:395453 (Wright-Patterson AFB, 2015); frame shows the yellow/black Fat Man casing beside the B-29 | |
| 30 | "In late summer 1947, the Army cautiously told the FBI." | OK | BENSON ("In late August or early September 1947 … cautiously informed S. Wesley Reynolds"); BW chronology ("Around 1 September" 1947) | |
| 30 | "from October 1948, an FBI agent, Robert Lamphere, worked with Gardner full time" | FIX | BW ("That October he had a private meeting with Meredith Gardner and began fulltime liaison on the project"); BENSON | The source says full-time liaison on the project, not full-time work with Gardner. → **"And from October nineteen forty-eight, an F B I agent, Robert Lamphere, worked full time as the Bureau's liaison to the project, alongside Gardner."** |
| 30 | Bentley, former courier for Soviet intelligence, confessions doubted, confirmed by decrypts | OK | ALM ("confirm her confessions, which had been in doubt"); BENSON ("veteran KGB courier") | |
| 30 | lab FBIC "THE U.S. CAPITOL, SEEN FROM THE FBI BUILDING, 2025" (dv974123 @18.7) | FIX | DVIDS video:974123 ("Generic B-Roll footage of the J. Edgar Hoover Building") | Nothing establishes that the camera position was the FBI building. → **`FBIC = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C. (FBI B-ROLL, 2025)"`** |
| 32 | By 1948 the CIA's estimate: earliest mid-1950, most probable mid-1953; card quote "the most probable date" | OK | STEURY | "the earliest possible date" and "the most probable date" are verbatim. |
| 33 | Report of Aug 24, 1949 still gave that projection | OK | STEURY (OSI/SR-10/49/1, disseminated 24 Aug 1949) | |
| 34 | Aug 29, 1949; "years ahead of the estimate"; source S_STEURY | OK | STEURY | |
| 35 | B-29 between Alaska and Japan with particle sampler picked up debris | OK | AF; AFTAC ("particulate sampler aboard an Air Weather Service modified B-29") | |
| 35 | B29 label "B-29 'Doc', a restored WWII bomber, McConnell AFB, Kansas, 2026" | OK | DVIDS video:1027235 (Oct 22, 2026) | At 23.2 s the aircraft is small in the distance, but the label is correct. |
| 36 | "On September 23, President Truman told the nation." + tag WASHINGTON, D.C. · SEPTEMBER 23, 1949 | FIX (wording) | FRUS ("On September 23, President Truman announced that the United States possessed evidence…") | None of the episode's listed sources has this; FRUS does. It was a written statement, not an address. → **"On September twenty-third, President Truman announced that the United States had evidence of an atomic explosion in the Soviet Union."** Add FRUS 1949 v.1 to the source list. |
| 37 | Americans built their bomb in secret at Los Alamos; Trinity stills | OK | FBI ("developed at Los Alamos") | See the Trinity note. |
| 38 | PLAQ "Trinity Site marker, WSMR, 2017" | OK | DVIDS image:3856843 (plaque on obelisk, Oct 7, 2017) | |
| 40 | 1949: CHARLES and REST identified as Fuchs; one message quoted a paper he wrote | OK | BENSON ("identified as Klaus Fuchs during the summer of 1949"); BW ("author of a paper quoted in one message") | |
| 41 | FBI: Fuchs member of a British team working with Americans at Los Alamos | OK | FBI | |
| 42 | Nov 1944 message: KGB trying to reach him; ARNO visited CHARLES's sister | OK | 1606 ("On ARNO's last visit to CHARLES' sister …"; "taking steps to establish liaison") | |
| 43 | Not left for ISLAND (= Great Britain); at Camp No. 2; promised leave for Christmas | OK | 1606 + comment [vi] "OSTROV: GREAT BRITAIN" | |
| 40–46 | FUCHS label "No. 1606, Nov. 1944 · NSA translation (1957)" | OK | 1606 (hand-corrected "16 Nov. 44"; issued 12/3/1957) | |
| 44 | Fuchs confessed Jan 24, 1950 | OK | BW chronology ("24 January Klaus Fuchs confesses to espionage") | |
| 44 | Tag "LONDON · JANUARY 24, 1950" over dv952451 @8s labelled "BROOKLYN, NEW YORK, 2025" | FIX | DVIDS video:952451; no source opened places the confession in London | The dateline puts London on screen over Brooklyn footage, which is a misleading juxtaposition, and London itself is unsourced. → tag **`("BRITAIN", "JANUARY 24, 1950")`** and visual **`[I("fuchs_cable", kb="out", focus=[0.5, 0.5], lab=FUCHS)]`** (or any non-location card) in place of `C("dv952451", 8.0, lab=BKN)`. |
| 45 | Arrested Feb 2; 14 years; maximum under the Official Secrets Act; stat source S_FBI | OK | FBI | |
| 45 | "Moscow, the official VENONA history says, had already warned some American agents linked to Fuchs that they might have to flee the country, through Mexico." | FIX | BW ("various accounts" say that in October 1949 Moscow "began advising American agents who had dealt with Klaus Fuchs that they might have to flee the country through Mexico") | BW reports this from other accounts and does not state it as its own finding. → **"According to accounts cited in the official VENONA history, Moscow had begun advising American agents who had dealt with Fuchs that they might have to flee the country, through Mexico."** |
| 46 | ARNO = Harry Gold, Philadelphia chemist, arrested May 1950 | OK | 1606 comment [iv] "ARNO: Harry GOLD"; FBI ("a Philadelphia chemist"); BW (arrested 22 May) | |
| 48 | Greenglass, Army enlisted man assigned to Los Alamos 1944 and 1945, Soviet agent | OK | FBI | |
| 48 | FATP "Replica 'Fat Man' bomb casing, Travis AFB Heritage Center, California, 2018" | FIX (minor) | DVIDS image:4071168 | DVIDS dates it 2018-01-10, but the VIRIN 120110-F-VG042-0001 points to Jan 10, 2012. → **`FATP = "PHOTO · REPLICA \"FAT MAN\" BOMB CASING, TRAVIS AFB HERITAGE CENTER, CALIFORNIA (USAF PHOTO)"`** |
| 49 | Nov 14 message: wife OSA agreed to help draw him in, "with a view to ENORMOUS" | OK | 1600 (+ [v] OSA: Ruth Greenglass; [vi] KALIBR: David Greenglass) | |
| 50 | Before her departure LIBERAL will carry out two briefing meetings; notes: Julius Rosenberg | OK | 1600 + comment [ii] | |
| 49–50 | LIB label "No. 1600, Nov. 14, 1944 · NSA reissue" | OK | 1600 "Reissue (T293)" | |
| 51 | Quote card "The most active spy, at least as seen in VENONA messages, was LIBERAL." | OK | NSA18 (verbatim) | |
| 52 | Two weeks later; Ethel; 29; knows about her husband's work | OK | 1657 (27 Nov 1944) | Nov 14 to Nov 27 is 13 days; "two weeks later" is acceptable. |
| 52 | ETH label "No. 1657, Nov. 27, 1944 · NSA reissue (1975)" | OK | 1657 (dated 1 May 1975) | |
| 53 | Spoken: loyal communist, knew of husband's espionage, not crimes worthy of capital punishment; quote card | OK | NSA18 ("Two VENONA decrypts show that Ethel was a loyal communist"; "The decrypts do not suggest she committed any crimes worthy of capital punishment.") | The card text is verbatim. |
| 54 | Verdict Mar 29, 1951; both executed June 19, 1953 at Sing Sing | OK | FBI; NSA18 ("went to the electric chair in Sing Sing Prison on June 19, 1953") | |
| 54 | Timeline DEC 1946 / AUG 1949 / JAN 1950 / MAY 1950 / MAR 1951 / JUN 1953 | OK | ARMY46, STEURY, BW, FBI | |
| 55 | Greenglass testified against sister and brother-in-law; about ten years; Gold released after 15 | OK | FBI; NSA18 ("served a decade"; "Gold was released after 15 years") | FBI says "about nine years"; "about ten" follows NSA18 and is fine. |
| 56 | Agreement: decrypts could stimulate investigations, never used in court or made public; quote card | OK | NSA18 ("under an agreement that stipulated the decrypts could be used to stimulate investigations, but never were to be used in court or otherwise made public.") | The card is verbatim, with ellipses. |
| 58 | Left his photograph, agreed a place for meeting; KGB contact (BEK) described exceptionally keen mind and broad outlook | OK | 1585 | |
| 59 | "His cover name in VENONA was MLAD. Russian for Youngster." (over the 1585 cable) | FIX | BW ("the covername YOUNGSTER [MLAD], found in other messages, matched Hall") | The cable on screen uses his real name, not MLAD. → **"In other VENONA messages, he had a cover name. \| MLAD. \| Russian for Youngster."** |
| 60 | FBI matched the name to Hall; questioned 1951; never prosecuted | OK | BW | |
| 61 | Official VENONA history (NSA/CIA 1996): case probably could not have been made without revealing the program; quote card "…a case could not have been made {{without revealing AFSA's program.}}" | OK | BW ("probably because a case could not have been made without revealing AFSA's program") | Verbatim, with an ellipsis. |
| 62 | Army: in 1948 ASA employee William Weisband revealed the effort | OK | ARMY95 | |
| 63 | Weisband always denied spying; government never prosecuted him for it; no new messages after 1948 | OK | BW ("always denied involvement in espionage, and the US Government never prosecuted him for it"); ARMY95 | Optional: add that he served a year for contempt (BW). |
| 64 | AFSA, then NSA from 1952 | OK | ARMY95 | |
| 65 | VENONA ran until Oct 1, 1980 | OK | ALM | |
| 66 | First public mention of the name in Lamphere's 1986 book (Army) | OK | ARMY95 | |
| 67 | July 11, 1995 ceremony at CIA; NSA, FBI, CIA released the first 49; copies to NARA, LoC, NCM; tag LANGLEY | OK | ARMY95 | |
| 68 | "Over the next two years, about twenty-nine hundred messages came out." | FIX | ARMY95 ("During the next two years, NSA released five more batches … about 2,900 messages in all") | The 2,900 is the total including the first release. → **"Over the next two years, five more releases followed. \| About twenty-nine hundred messages in all."** |
| 68 | "nearly 350 American members of the Communist Party who spied for the Soviet Union" + stat card (S_ARMY95) | OK | ARMY95 | |
| 69 | Soviet shortcut with the pads let codebreakers read fragments of messages sent years earlier | OK | ALM, ARMY46 | |
| 70 | "Those fragments, the NSA says, could only point investigators in the right direction. The FBI had to find the evidence to convict somewhere else." | FIX | NSA18 ("Once the individuals were identified, the FBI then had to develop evidence about their crimes"; the prosecution rested on "a few espionage artifacts and testimony by David Greenglass") | NSA18 does not say "point in the right direction" or "only". → **"Those fragments, the N S A says, could stimulate investigations. \| Once the spies were identified, the F B I then had to develop evidence about their crimes."** |
| 71 | Pointed to Fuchs; investigation reached Gold, Greenglass, Rosenbergs | OK | BENSON, FBI | |
| 72 | Same secret kept one case out of court; 19-year-old never charged | OK | BW | |
| 73 | Release ~half a century after; OBEL label "Trinity Site open house, WSMR, 2016" | OK | 1944→1995; DVIDS image:2902844 (Oct 1, 2016) | |
| 74 | F22 lab, dv1026930 @40.5 | OK | DVIDS (July 3, 2026) | |
| all FBI | lab FBI on dv974123 @31, 60.6, 100.9, 110, 121, 172.4, 89.5 | OK | DVIDS video:974123 (Aug 2025) | Every frame shows the Hoover Building. |
| 64, 67 | TINA reused for AFSA/NSA and 1995 release | OK | ARMY95 used this same image for the 1995 release article | |

## Trinity stills (trin_a = dv395453 @172.5 s; trin_b = @178.6 s)

Verdict: **OK, defensible.** The neighbouring frame at 170.0 s shows the spherical Gadget being prepared under a "WEAR A HARD HAT" sign. 172.5 s shows the device in the shot tower, and 176.5 to 178.6 s show the flash and then the cloud, in that order. That sequence is the well-known 1945 Trinity film. The DVIDS metadata for "Yesterday's Air Force: The Plane that Ended World War II" (2015) does not itself say "Trinity", so the label's hedge "AS SHOWN IN A USAF VIDEO (2015)" is right and should stay. The tower frame (trin_a) is the most clearly identifiable. If you want zero risk on the cloud (trin_b), use trin_a in line 7 instead of trin_b.

## Not covered by the FIX list but worth knowing
- Line 13: the dateline ARLINGTON HALL appears over Treasury/F-22 footage. Every clip is honestly labelled, so this is acceptable, but a doc crop would sit better.
- DVIDS spells the name "Merideth Gardner". The script's "Meredith" is the standard spelling (NSA, BW); keep it.
