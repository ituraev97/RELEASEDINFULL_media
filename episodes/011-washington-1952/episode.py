# FILE 011 — Saucers Over the Capital: Washington, 1952, in the Files
# Format: see episodes/001-navy-videos/episode.py
# NOTE on clip timing:
#  dv1023402s = DVIDS 1023402 (DOW-UAP-PR159, Tremonton film, 24 fps) trimmed from 3.0 s (23 s long), retimed to 30 fps at original speed
#               with frame blending (minterpolate mi_mode=blend; no duplicated frames). Times below are relative to that file.
#  dv934516a/b = DVIDS 934516 (National Museum of the USAF B-roll, 4K60) trimmed from 5 s (a) and 130 s (b), scaled to 1080p.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
BB = "ACTUAL DOCUMENT · PROJECT BLUE BOOK STATUS REPORT NO. 8 (JUNE-OCTOBER 1952) · NATIONAL ARCHIVES"
CHART = "ACTUAL DOCUMENT · BLUE BOOK STATUS REPORT NO. 8, APPENDIX I · NATIONAL ARCHIVES"
CIA14 = "ACTUAL DOCUMENT · CIA, \"FLYING SAUCERS\" (AUGUST 14, 1952) · CIA READING ROOM"
CIA24 = "ACTUAL DOCUMENT · CIA, H. M. CHADWELL, \"FLYING SAUCERS\" (SEPT. 24, 1952) · CIA READING ROOM"
DIARY = "ACTUAL DOCUMENT · CIA, OFFICIAL DIARY (AUGUST 18, 1952) · CIA READING ROOM"
HAINES = "ACTUAL DOCUMENT · CIA, \"THE CIA'S ROLE IN THE STUDY OF UFOS, 1947-90\" (STUDIES IN INTELLIGENCE, 1997)"
RP = "ACTUAL DOCUMENT · REPORT OF THE SCIENTIFIC PANEL ON UNIDENTIFIED FLYING OBJECTS (JAN. 17, 1953) · CIA"
RPF = "ACTUAL DOCUMENT · CIA, REPORT OF MEETINGS OF THE SCIENTIFIC ADVISORY PANEL ON UFOS (JANUARY 1953)"
S_HAINES = "SOURCE: CIA, \"THE CIA'S ROLE IN THE STUDY OF UFOS, 1947-90\" (G. K. HAINES, 1997)"
S_CIA14 = "SOURCE: CIA MEMORANDUM \"FLYING SAUCERS,\" AUGUST 14, 1952 (CIA READING ROOM)"
S_CIA24 = "SOURCE: CIA, H. MARSHALL CHADWELL TO THE DCI, \"FLYING SAUCERS,\" SEPTEMBER 24, 1952"
S_RP = "SOURCE: REPORT OF THE SCIENTIFIC PANEL ON UNIDENTIFIED FLYING OBJECTS, JANUARY 17, 1953 (CIA)"
S_RPF = "SOURCE: CIA, REPORT OF MEETINGS OF SCIENTIFIC ADVISORY PANEL ON UFOS (1953), P. 12"
S_BB = "SOURCE: PROJECT BLUE BOOK STATUS REPORT NO. 8 (NATIONAL ARCHIVES)"
S_DVIDS = "SOURCE: DOW-UAP-PR159 / PR160 DESCRIPTIONS, U.S. DEPARTMENT OF WAR VIA DVIDS (SEPT. 18, 2026)"

TREM = "ACTUAL FILM · DOW-UAP-PR159 · NEAR TREMONTON, UTAH, JULY 2, 1952 · RETIMED TO 30 FPS"
RADAR15 = "B-ROLL · AIR FORCE RADAR APPROACH CONTROL, NEW JERSEY, 2015 · NOT 1952 EQUIPMENT"
RADAR16 = "B-ROLL · RADAR APPROACH CONTROL, RAF LAKENHEATH, U.K., 2016 · NOT 1952 EQUIPMENT"
TOWER16 = "B-ROLL · CONTROL TOWER, RAF LAKENHEATH, U.K., 2016"
F15 = "B-ROLL · F-15 TAKEOFF, RAF LAKENHEATH, U.K., 2016"
F22 = "B-ROLL · WASHINGTON, D.C., SEEN FROM AN F-22 COCKPIT, 2026"
WH = "B-ROLL · THE WHITE HOUSE, WASHINGTON, D.C."
CAP = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C."
PENN = "B-ROLL · AVENUE LEADING TO THE U.S. CAPITOL, WASHINGTON, D.C."
TREAS = "B-ROLL · THE TREASURY BUILDING, WASHINGTON, D.C."
MUS = "B-ROLL · NATIONAL MUSEUM OF THE U.S. AIR FORCE, WRIGHT-PATTERSON AFB, OHIO, 2024"
MUSF = "B-ROLL · F-15 FLYOVER, NATIONAL MUSEUM OF THE U.S. AIR FORCE B-ROLL, 2024"
MUSJ = "B-ROLL · KOREAN WAR-ERA AIRCRAFT ON DISPLAY, NATIONAL MUSEUM OF THE USAF, 2024"
BAL = "B-ROLL · WEATHER BALLOON LAUNCH BY A U.S. MARINE CORPS WEATHER TEAM, 2022"

LINES = [
 # ---------------- COLD OPEN ----------------
 ("In July nineteen fifty-two, according to the C I A's own history, radar scopes at Washington National Airport and Andrews Air Force Base tracked mysterious blips.",
  [C("dv503512", 80.6, lab=RADAR16), I("haines_dc", kb="in", focus=[0.5, 0.35], lab=HAINES)], dict(tag=("WASHINGTON, D.C.", "JULY 1952"))),
 ("A week later, the blips came back. | The Air Force sent interceptors up to look. | They found nothing.",
  [C("dv1026930", 36.5, lab=F22), C("dv431279", 13.2, lab=RADAR15)], {}),
 ("Two days after that, the Air Force held a press conference on flying saucers.",
  [I("chart", kb="in", focus=[0.62, 0.12], lab=CHART)], {}),
 ("Project Blue Book's own chart of that summer marks the spike with three labels. | Publicized incident at Washington. Highly publicized incident at Washington. | And the press conference.",
  [I("chart", kb="out", focus=[0.6, 0.3], lab=CHART)], dict(slow=True)),
 ("By September, the C I A was asking whether flying saucers were a threat to national security.",
  [I("sep24_head", kb="in", focus=[0.5, 0.5], lab=CIA24)], {}),
 ("And in twenty twenty-six, the Pentagon released a film shot that same July. | Its own description says it still has no conclusive answer.",
  [C("dv1023402s", 7.2, lab=TREM)], {}),
 ("This is the summer of nineteen fifty-two, as the files tell it. | Let's open them.",
  [G("intro", n="011")], dict(gap=0.2)),
 ("",
  [G("title", n="011", t="Saucers Over the Capital", size=140, sub="Washington, 1952, in the Files")], dict(gap=0.4)),

 # ---------------- I. THE TALK ----------------
 ("The story starts four months earlier, with a tape.",
  [G("chapter", n="I", t="The Talk")], {}),
 ("In March nineteen fifty-two, an Air Force officer, Captain Edward J Ruppelt, gave a presentation on the Air Force's reorganized investigation of unidentified flying objects.",
  [C("dv934516a", 1.3, lab=MUSF), C("dv934516b", 9.0, lab=MUSJ)], {}),
 ("In May twenty twenty-six, a congressman asked about a reel of tape with Ruppelt listed as the briefer. | Its label read, flying saucer talk.",
  [G("doc", header="REEL-TO-REEL TAPE · AS DESCRIBED BY REP. ERIC BURLISON, MAY 8, 2026", title="How it is identified",
     lines=["AF-ATIC-FILM, 03/52", "{{\"flying saucer talk\"}}"],
     source="SOURCE: OFFICE OF REP. ERIC BURLISON, PRESS RELEASE, MAY 8, 2026 · TEXT AS QUOTED, RECREATED")], {}),
 ("In September, the Pentagon released an audio recording of his presentation.",
  [C("dv934516a", 8.2, lab=MUS)], {}),
 ("According to the Pentagon's description, Ruppelt explains that out of about eight hundred cases the Air Force had reviewed, about twenty percent remained unexplained.",
  [G("stat", k="CAPT. EDWARD J. RUPPELT · MARCH 1952", a="20%", size=300, b="of about 800 cases remained unexplained",
     c="as described in the 2026 release (DOW-UAP-PR160)", source=S_DVIDS)], {}),
 ("Those reports, it says, came from military personnel, commercial pilots, and other qualified technical observers. | He also pointed to clusters of reports around nuclear weapons sites, like Los Alamos and Oak Ridge.",
  [C("dv934516b", 1.5, lab=MUSJ)], {}),
 ("And some radar detections indicated air speeds between one thousand and three thousand five hundred miles an hour. | Speeds that, the description notes, were unconfirmed.",
  [C("dv503512", 78.3, lab=RADAR16)], {}),
 ("That same month, according to the National Archives, the Air Force's Director of Intelligence, Major General Charles Cabell, ordered a new project. | The Korean War was on, and Cold War tensions were rising. | Its name was Project Blue Book.",
  [C("dv934516b", 10.0, lab=MUSJ)], {}),
 ("Its job was to collect and explain the reports. | By the end of July, it would be buried in them.",
  [I("st_status", kb="in", focus=[0.5, 0.3], lab=BB)], dict(gap=0.9, sil=True)),

 # ---------------- II. THE FILM ----------------
 ("One of that summer's most closely studied cases came on July second.",
  [G("chapter", n="II", t="The Film")], {}),
 ("Near Tremonton, Utah, a Navy Chief Warrant Officer named Delbert C Newhouse reported seeing a group of bright objects in the sky. | He filmed them with a handheld camera, in color.",
  [C("dv1023402s", 6.4, lab=TREM)], dict(tag=("TREMONTON, UTAH", "JULY 2, 1952"))),
 ("Then he sent the film to the Air Force. | About sixteen hundred frames of Kodachrome.",
  [I("rb_trem", kb="in", focus=[0.5, 0.45], lab=RPF)], {}),
 ("This is that film, as the Pentagon released it. | The objects are the small white points of light, moving across the sky.",
  [C("dv1023402s", 10.4, lab=TREM)], dict(slow=True)),
 ("At the Air Force's request, the Navy's Photo Interpretation Laboratory spent about a thousand man-hours on it. | It plotted the motion and brightness of the objects, frame by frame.",
  [I("rb_pil", kb="in", focus=[0.5, 0.3], lab=RPF)], {}),
 ("Its analysts reached a striking opinion. | The objects were not birds, balloons or aircraft. | They were not reflections, because there was no blinking. | And they were, therefore, self-luminous.",
  [G("quote", q="…not birds, balloons or aircraft, were {{\"not reflections…\"}} and were, therefore, {{\"self-luminous\".}}",
     who="U.S. Navy Photo Interpretation Laboratory", role="As recorded by the CIA's scientific panel · January 1953", size=62, source=S_RPF)], dict(slow=True)),
 ("Hold on to that verdict. | It would be argued over in a secret meeting six months later.",
  [C("dv1023402s", 9.6, lab=TREM)], dict(gap=0.9, sil=True)),

 # ---------------- III. THE RADAR ----------------
 ("Two and a half weeks after Tremonton, it was Washington's turn.",
  [G("chapter", n="III", t="The Radar")], {}),
 ("On July nineteenth and twentieth, the C I A's history says, radar at Washington National Airport and at Andrews Air Force Base tracked mysterious blips.",
  [C("dv431279", 102.5, lab=RADAR15), C("dv503512", 78.4, lab=RADAR16)], {}),
 ("On July twenty-seventh, the blips reappeared.",
  [C("dv503512", 81.5, lab=RADAR16)], dict(tag=("WASHINGTON, D.C.", "JULY 27, 1952"))),
 ("The Air Force scrambled interceptor aircraft to investigate. | According to the same history, they found nothing.",
  [C("dv503512", 38.6, lab=F15), C("dv1026930", 4.0, lab=F22)], {}),
 ("But the incidents caused headlines across the country.",
  [C("dv346026", 6.0, lab=CAP)], {}),
 ("Blue Book's chart shows what happened to its in-tray. | On July twenty-eighth, the project received forty-three reports in a single day. | The peak of that summer.",
  [I("chart", kb="in", focus=[0.55, 0.2], lab=CHART), I("st_peak", kb="in", focus=[0.5, 0.35], lab=BB)], {}),
 ("For the month of July, the total was over four hundred and forty reports.",
  [G("stat", k="PROJECT BLUE BOOK · JULY 1952", a="440+", size=300, b="reports in a single month",
     c="peak: 43 reports on July 28", source=S_BB)], dict(slow=True)),
 ("From June through October, it received eight hundred and eighty-six. | That was a hundred and forty-nine more than in the previous five years put together.",
  [I("st_status", kb="down", focus=[0.5, 0.55], lab=BB)], {}),
 ("In July, the staff was increased to four officers, two airmen and two secretaries. | For forty-five days, a weather officer was brought in to help.",
  [I("st_staff", kb="in", focus=[0.5, 0.5], lab=BB)], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE ANSWER ----------------
 ("Washington wanted an answer. | Including the White House.",
  [G("chapter", n="IV", t="The Answer")], {}),
 ("A C I A memo dated August fourteenth records that requests for information poured in on the Air Force, including an official query from the White House.",
  [I("aug14", kb="in", focus=[0.5, 0.3], lab=CIA14), C("dv346124", 24.0, lab=WH)], {}),
 ("On July twenty-ninth, Major General John Samford, the Air Force's Director of Intelligence, held a press conference.",
  [C("dv346119", 30.0, lab=PENN)], dict(tag=("WASHINGTON, D.C.", "JULY 29, 1952"))),
 ("According to the memo, he said analysis showed no pattern of anything remotely consistent with any menace to the United States.",
  [G("quote", q="…{{\"no pattern of anything remotely consistent with any menace to the United States\"}}…",
     who="Maj. Gen. John A. Samford", role="Press conference, July 29, 1952 · as summarized by the CIA", size=60, source=S_CIA14)], {}),
 ("And the recent Washington sightings, he said, were possibly due to temperature inversions.",
  [I("aug14", kb="in", focus=[0.5, 0.6], lab=CIA14)], {}),
 ("In an inversion, the air gets warmer with height instead of cooler. | Under the right conditions, according to the National Weather Service's parent agency, a radar beam can be bent back toward the Earth, and produce false echoes.",
  [C("dv867753", 21.0, lab=BAL), C("dv867753", 41.0, lab=BAL)], {}),
 ("Samford also stated, emphatically, that the unexplained sightings could not have resulted from any experiments or tests conducted by the United States.",
  [I("aug14", kb="down", focus=[0.5, 0.8], lab=CIA14)], {}),
 ("Later, according to the C I A's history, a Civil Aeronautics Administration investigation confirmed that such radar blips were quite common, and were caused by temperature inversions.",
  [I("haines_caa", kb="in", focus=[0.5, 0.6], lab=HAINES)], {}),
 ("That was the public answer. | Inside the C I A, it was just getting started.",
  [C("dv346120", 20.0, lab=TREAS)], dict(gap=0.9, sil=True)),

 # ---------------- V. THE AGENCY ----------------
 ("The agency had monitored UFO reports for at least three years.",
  [G("chapter", n="V", t="The Agency")], {}),
 ("After the new rash of sightings, its history says, it formed a special study group.",
  [C("dv346119", 12.0, lab=PENN)], {}),
 ("For the group, an official named Edward Tauss reported that most sightings could be easily explained. | But he urged the agency to keep its interest hidden from the press and the public, in view of their probable alarmist tendencies.",
  [C("dv346124", 36.0, lab=WH)], {}),
 ("At Wright-Patterson, Air Force officials told the C I A group that ninety percent of the sightings were easily accounted for. | The other ten percent, they said, were a number of incredible reports from credible observers.",
  [G("quote", q="…{{\"a number of incredible reports from credible observers.\"}}",
     who="U.S. Air Force briefers", role="To the CIA study group · 1952", size=70, source=S_HAINES)], {}),
 ("Director Walter Bedell Smith believed there was only one chance in ten thousand that the phenomenon posed a threat to the security of the country. | But even that chance, he said, could not be taken.",
  [G("quote", q="…only one chance in 10,000 that the phenomenon posed a threat… {{but even that chance could not be taken.}}",
     who="Gen. Walter Bedell Smith", role="Director of Central Intelligence · 1952", size=60, source=S_HAINES)], dict(slow=True)),
 ("On Monday, August eighteenth, an official C I A diary records an announcement at the Deputies' meeting. | A briefing on flying saucers, eleven in the morning, Wednesday, in the Director's conference room. | Twenty minutes.",
  [I("diary", kb="in", focus=[0.5, 0.75], lab=DIARY)], {}),
 ("On September twenty-fourth, H Marshall Chadwell, the C I A's Assistant Director for Scientific Intelligence, sent the director a memo. | Its subject was two words. Flying Saucers.",
  [I("sep24_head", kb="in", focus=[0.4, 0.75], lab=CIA24)], dict(slow=True)),
 ("Since nineteen forty-seven, it said, the Air Force had received about fifteen hundred official reports, and carried twenty percent as unexplained. | Of the reports from January through July nineteen fifty-two, twenty-eight percent.",
  [I("sep24_july", kb="in", focus=[0.5, 0.5], lab=CIA24)], {}),
 ("Chadwell saw two dangers. | The first was psychological. | A fair proportion of our population, he wrote, is mentally conditioned to the acceptance of the incredible.",
  [I("incredible", kb="in", focus=[0.5, 0.5], lab=CIA24)], dict(slow=True)),
 ("His team had also read the Soviet press. | Up to the time of the inquiry, the memo says, there had been no report or comment on flying saucers in the Soviet press, even satirical, apart from one humorous mention by Gromyko. | With a state-controlled press, it reasoned, that could result only from an official policy decision.",
  [I("soviet", kb="in", focus=[0.5, 0.6], lab=CIA24)], {}),
 ("The second was air defense. | At any moment of attack, he wrote, we cannot, on an instant basis, distinguish hardware from phantom.",
  [G("quote", q="…we cannot, on an instant basis, {{distinguish hardware from phantom…}}",
     who="H. Marshall Chadwell", role="CIA Assistant Director, Scientific Intelligence · Sept. 24, 1952", size=66, source=S_CIA24)], dict(slow=True)),
 ("And as tension mounts, he warned, there is the even greater danger of falsely identifying the real as phantom.",
  [I("phantom", kb="in", focus=[0.5, 0.75], lab=CIA24)], {}),
 ("By December, the agency's history says, he was convinced that something was going on that must have immediate attention.",
  [C("dv1026930", 38.5, lab=F22)], dict(gap=0.9, sil=True)),

 # ---------------- VI. THE PANEL ----------------
 ("So the C I A called in scientists.",
  [G("chapter", n="VI", t="The Panel")], {}),
 ("From January fourteenth to seventeenth, nineteen fifty-three, a panel chaired by the physicist H P Robertson, of the California Institute of Technology, reviewed the evidence.",
  [I("rp_head", kb="in", focus=[0.5, 0.5], lab=RP)], {}),
 ("According to the C I A's history, the panel spent twelve hours studying the phenomena, and decided that reasonable explanations could be suggested for most, if not all, sightings.",
  [C("dv346026", 20.0, lab=CAP)], {}),
 ("Its case list included the Washington area sightings of July nineteenth. | And the film from Tremonton.",
  [C("dv1023402s", 12.0, lab=TREM)], {}),
 ("The Navy lab's analysts presented their plots. | The panel was impressed, it wrote, by their enthusiasm, industry and extent of effort. | But it could not accept the conclusions reached.",
  [I("rb_pil", kb="down", focus=[0.5, 0.75], lab=RPF)], {}),
 ("A semi-spherical object, it noted, can reflect sunlight without blinking.",
  [I("rb_gulls", kb="in", focus=[0.5, 0.3], lab=RPF)], {}),
 ("Then the panel watched a short film showing the high reflectivity of seagulls in bright sunlight. | The motions, sizes and brightnesses of the objects, it concluded, strongly suggested birds.",
  [I("rb_gulls", kb="in", focus=[0.5, 0.55], lab=RPF)], dict(slow=True)),
 ("Its report, dated January seventeenth, said the evidence showed no indication that these phenomena constitute a direct physical threat to national security.",
  [I("rp_strip", kb="in", focus=[0.5, 0.45], lab=RP)], {}),
 ("And it recommended that the national security agencies strip the unidentified flying objects of the special status they have been given, and the aura of mystery they have unfortunately acquired.",
  [G("quote", q="…strip the Unidentified Flying Objects of the special status they have been given and {{the aura of mystery they have unfortunately acquired.}}",
     who="The Robertson Panel", role="Report of the Scientific Panel · January 17, 1953", size=56, source=S_RP)], dict(slow=True)),
 ("The way to do it, the panel suggested, was a program to reassure the public of the total lack of evidence of inimical forces behind the phenomena.",
  [I("rp_strip", kb="in", focus=[0.5, 0.85], lab=RP)], dict(gap=0.9, sil=True)),

 # ---------------- VII. THE RELEASE ----------------
 ("Project Blue Book kept going for almost eighteen years.",
  [G("chapter", n="VII", t="The Release")], {}),
 ("When it closed in December nineteen sixty-nine, the Air Force says, it had logged twelve thousand six hundred and eighteen sightings. | Seven hundred and one remained unidentified.",
  [G("stat", k="PROJECT BLUE BOOK · 1947-1969", a="701", to=701, size=300, b="sightings still \"unidentified\"",
     c="out of 12,618 reported", source="SOURCE: USAF FACT SHEET 95-03, \"UNIDENTIFIED FLYING OBJECTS AND AIR FORCE PROJECT BLUE BOOK\"")], dict(slow=True)),
 ("On September eighteenth, twenty twenty-six, the Pentagon published a digitized print of the Tremonton film, in its sixth batch of U A P files.",
  [C("dv1023402s", 8.0, lab=TREM)], {}),
 ("Its description is careful. | The film's limited detail and lack of fixed reference points, it says, prevented a conclusive resolution.",
  [G("quote", q="The film's limited detail and lack of fixed reference points {{prevented a conclusive resolution.}}",
     who="DOW-UAP-PR159", role="Official description · September 2026", size=62, source=S_DVIDS)], {}),
 ("It also notes something odd. | From the fifty-five second mark, the surviving print switches to unrelated footage that appears to show a demonstration of sewing equipment. | The record, it says, does not establish how the two were combined.",
  [C("dv1023402s", 7.2, lab=TREM)], {}),
 ("The Ruppelt recording came out the same day. | Online, some posts claimed his talk described the Washington sightings.",
  [C("dv934516b", 16.5, lab=MUSJ)], {}),
 ("It could not have. | He spoke in March. | The radar blips over Washington came in July.",
  [G("timeline", kicker="1952, IN THE FILES", title="The order of events",
     events=[dict(y="MAR", t="Ruppelt's talk; Blue Book ordered"), dict(y="JUL 2", t="Tremonton film"),
             dict(y="JUL 19-20", t="Washington radar"), dict(y="JUL 27", t="Blips return"),
             dict(y="JUL 29", t="Samford press conference")],
     source="SOURCES: DVIDS (2026); CIA, HAINES (1997); CIA MEMO, AUGUST 14, 1952; NATIONAL ARCHIVES")], {}),
 ("So what did the radar see over Washington? | The Air Force's answer was, possibly, the weather. Temperature inversions. | The C I A's own history repeats it.",
  [C("dv431279", 12.6, lab=RADAR15), C("dv503512", 78.3, lab=RADAR16)], {}),
 ("What the files show for certain is the reaction. | One summer of reports brought the C I A into the question, and a panel that recommended taking the mystery away.",
  [C("dv346026", 16.0, lab=CAP)], {}),
 ("Every secret has a release date. | For this print of the Tremonton film, the Pentagon's release came seventy-four years after it was shot.",
  [C("dv1023402s", 8.8, lab=TREM)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments.",
  [C("dv1026930", 40.5, lab=F22)], {}),
 ("Next time: for more than two decades, the U S government paid people to try to see things from far away. | Stargate.",
  [G("end", n="011", next="Stargate: The Pentagon's Psychic Spies")], dict(gap=2.5)),
]

PRON = [("Ruppelt", "Roo-pelt"), ("Tremonton", "Tremmon-tun"), ("Newhouse", "New-house"), ("Samford", "Samford"),
        ("Chadwell", "Chad-well"), ("Kodachrome", "Koda-chrome"), ("inimical", "in-imical"), ("Burlison", "Burr-lison"), ("Gromyko", "Gro-meeko"),
        ("Walter Bedell Smith", "Walter Beedle Smith"), ("C I A's", "C I A's"), ("U A P", "U A P")]

DISPLAY = [
 ("C I A's", "CIA's"), ("C I A", "CIA"), ("U A P", "UAP"), ("U S government", "U.S. government"),
 ("Edward J Ruppelt", "Edward J. Ruppelt"), ("Delbert C Newhouse", "Delbert C. Newhouse"), ("H Marshall Chadwell", "H. Marshall Chadwell"),
 ("H P Robertson", "H. P. Robertson"),
 ("eight hundred cases", "800 cases"), ("twenty percent", "20 percent"), ("ninety percent", "90 percent"), ("ten percent", "10 percent"), ("twelve hours", "12 hours"), ("twenty-eight percent", "28 percent"),
 ("one thousand and three thousand five hundred", "1,000 and 3,500"), ("sixteen hundred frames", "1,600 frames"),
 ("a thousand man-hours", "1,000 man-hours"), ("forty-three reports", "43 reports"),
 ("four hundred and forty reports", "440 reports"), ("eight hundred and eighty-six", "886"),
 ("a hundred and forty-nine", "149"), ("forty-five days", "45 days"), ("fifteen hundred official", "1,500 official"),
 ("one chance in ten thousand", "one chance in 10,000"), ("twelve thousand six hundred and eighteen", "12,618"),
 ("Seven hundred and one", "701"), ("fifty-five second mark", "55-second mark"), ("seventy-four years", "74 years"),
 ("July nineteenth and twentieth", "July 19 and 20"), ("July nineteenth", "July 19"), ("July twenty-seventh", "July 27"),
 ("July twenty-eighth", "July 28"), ("July twenty-ninth", "July 29"), ("July second", "July 2"), ("August fourteenth", "August 14"),
 ("August eighteenth", "August 18"), ("September twenty-fourth", "September 24"), ("September eighteenth", "September 18"),
 ("January fourteenth to seventeenth", "January 14 to 17"), ("January seventeenth", "January 17"),
 ("nineteen fifty-two", "1952"), ("nineteen fifty-three", "1953"), ("nineteen forty-seven", "1947"), ("nineteen sixty-nine", "1969"),
 ("twenty twenty-six", "2026"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="011", title="Saucers Over the Capital: Washington, 1952, in the Files",
    imgs={k: D + k + ".jpg" for k in ["chart", "haines_caa", "st_status", "st_peak", "st_staff", "aug14", "sep24_head", "sep24_july", "phantom", "incredible", "soviet",
                                      "rb_trem", "rb_pil", "rb_gulls", "rp_head", "rp_strip", "haines_dc", "diary"]},
    credit="Documents: Project Blue Book (National Archives); CIA Reading Room (1952-53); CIA Studies in Intelligence (1997).\\NFootage: U.S. government via DVIDS, incl. DOW-UAP-PR159 (1952 film, released 2026). No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[19, 24], hook="A NAVY LAB SAID<br>[NOT BIRDS]"),
        dict(id="s2", lines=[26, 33], hook="RADAR TRACKED BLIPS<br>[OVER WASHINGTON]"),
        dict(id="s3", lines=[35, 42], hook="THE AIR FORCE SAID<br>[MAYBE THE WEATHER]"),
        dict(id="s4", lines=[49, 55], hook="\"HARDWARE<br>[FROM PHANTOM]\""),
    ],
    yshorts=[
        dict(id="y1", lines=[21, 24], hook="THE NAVY LAB SAID<br>[\"SELF-LUMINOUS\"]"),
        dict(id="y2", lines=[26, 30], hook="RADAR BLIPS<br>[OVER WASHINGTON]"),
        dict(id="y3", lines=[53, 56], hook="\"HARDWARE<br>[FROM PHANTOM]\""),
    ],
)
