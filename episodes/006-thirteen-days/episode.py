# FILE 006 — Thirteen Days: The Cuban Missile Photos
# Format: see episodes/001-navy-videos/episode.py
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
CIA92 = "\"CIA DOCUMENTS ON THE CUBAN MISSILE CRISIS, 1962\" (CIA HISTORY STAFF, 1992)"
OCT14 = "U.S. RECONNAISSANCE PHOTO BOARD · \"MRBM FIELD LAUNCH SITE, SAN CRISTOBAL NO. 1, 14 OCTOBER 1962\" · JFK LIBRARY VIA NARA"
LOSPAL = "U.S. RECONNAISSANCE PHOTO · \"MILITARY ENCAMPMENT (MISSILE), LOS PALACIOS, CUBA\" · PRINT DATED 15 OCT 1962"
LOW = "U.S. LOW-LEVEL RECONNAISSANCE PHOTO BOARD · \"MRBM LAUNCH SITE 2, SAN CRISTOBAL, 1 NOVEMBER 1962\""
NOV1 = "U.S. LOW-LEVEL RECONNAISSANCE PHOTO · SOVIET SS-4 MISSILE SITE, CUBA, NOV. 1, 1962"
OCT25 = "U.S. RECONNAISSANCE PHOTO · \"MRBM LAUNCH SITE 2, SAGUA LA GRANDE, CUBA,\" MISSION 5011, 25 OCTOBER 1962 · COURTESY NGA"
MAP14 = "ACTUAL DOCUMENT · CIA MAP OF THE 14 OCTOBER 1962 U-2 FLIGHT · IN " + CIA92
SACMAP = "ACTUAL DOCUMENT · CIA MAP, \"CUBA U-2 OVERFLIGHT BY SAC, 15–22 OCTOBER 62\" · IN " + CIA92
MEMO = "ACTUAL DOCUMENT · CIA MEMORANDUM, \"PROBABLE SOVIET MRBM SITES IN CUBA,\" 16 OCTOBER 1962"
MAP16 = "ACTUAL DOCUMENT · MISSILE RANGE MAP ATTACHED TO THE CIA MEMORANDUM OF 16 OCTOBER 1962"
LUND = "ACTUAL DOCUMENT · ARTHUR C. LUNDAHL, NPIC, \"ADDITIONAL INFORMATION — MISSION 3101,\" 16 OCTOBER 1962"
MCC = "ACTUAL DOCUMENT · JOHN A. McCONE, MEMORANDUM \"SOVIET MRBMs IN CUBA,\" OCT. 31, 1962, QUOTING HIS CABLE OF SEPT. 10, 1962"
SNI = "ACTUAL DOCUMENT · SPECIAL NATIONAL INTELLIGENCE ESTIMATE 85-3-62, \"THE MILITARY BUILDUP IN CUBA,\" 19 SEPTEMBER 1962"
JFKNR = "ARCHIVAL · PRESIDENT KENNEDY'S ADDRESS ON CUBA, OCT. 22, 1962 · UNIVERSAL NEWSREEL (NATIONAL ARCHIVES)"
UNNR = "ARCHIVAL · U.N. SECURITY COUNCIL, NEW YORK, OCTOBER 1962 · UNIVERSAL NEWSREEL (NATIONAL ARCHIVES)"
CAMNR = "ARCHIVAL · AERIAL RECONNAISSANCE CAMERA AND AIRCREW · UNIVERSAL NEWSREEL, OCT. 25, 1962 (NATIONAL ARCHIVES)"
BRDNR = "ARCHIVAL · U.S. RECONNAISSANCE PHOTO OF A CUBAN AIRFIELD, AS SHOWN IN A UNIVERSAL NEWSREEL, OCT. 25, 1962"
BRD2 = "ARCHIVAL · U.S. RECONNAISSANCE PHOTO OF A SOVIET MISSILE SITE IN CUBA, AS SHOWN IN A UNIVERSAL NEWSREEL, OCT. 25, 1962"
SHIPNR = "ARCHIVAL · U.S. NAVY WARSHIPS AT SEA · UNIVERSAL NEWSREEL, OCT. 25, 1962 (NATIONAL ARCHIVES)"
EXC = "WHITE HOUSE PHOTO · EXECUTIVE COMMITTEE OF THE NATIONAL SECURITY COUNCIL, CABINET ROOM, OCT. 29, 1962"
PROCL = "WHITE HOUSE PHOTO · PRESIDENT KENNEDY SIGNS THE CUBA QUARANTINE PROCLAMATION, OVAL OFFICE, OCT. 23, 1962 · NARA"
P2H = "U.S. NAVY PHOTO · P-2H NEPTUNE PATROL PLANE OVER A SOVIET CARGO SHIP, OCTOBER 1962"
USAF = "ARCHIVAL · U.S. AIR FORCE FILM: 4080TH STRATEGIC RECONNAISSANCE WING PILOTS AWARDED THE DFC FOR THE CUBA FLIGHTS, NOV. 28, 1962 (NARA)"
U2B = "B-ROLL · U.S. AIR FORCE U-2 RECONNAISSANCE AIRCRAFT, BEALE AIR FORCE BASE, CALIF., 2023"
DIR = "NGA PHOTO · ROBERT LUNDAHL (LEFT), SON OF ARTHUR LUNDAHL, AND FORMER CIA IMAGERY ANALYST VINCENT DiRENZO, SPRINGFIELD, VA., 2012"
U2ALT = "B-ROLL · VIEW FROM A U.S. AIR FORCE U-2 AT HIGH ALTITUDE, 2026"
DDG = "B-ROLL · U.S. NAVY DESTROYER USS MUSTIN UNDERWAY, INDIAN OCEAN, 2026"
DC = "B-ROLL · VIEW FROM A U.S. AIR FORCE F-22 OVER WASHINGTON, D.C., 2026"
WH = "B-ROLL · THE WHITE HOUSE, WASHINGTON, D.C., 2012"
CAP = "B-ROLL · U.S. CAPITOL, WASHINGTON, D.C., 2012"

S_FRUS = "SOURCE: FOREIGN RELATIONS OF THE UNITED STATES, 1961–1963, VOL. XI, DOC. 16 (EDITORIAL NOTE)"
S_MEMO = "SOURCE: CIA MEMORANDUM, \"PROBABLE SOVIET MRBM SITES IN CUBA,\" 16 OCT. 1962 · IN " + CIA92
S_JFK = "SOURCE: PRESIDENT KENNEDY, RADIO AND TELEVISION ADDRESS ON THE SOVIET ARMS BUILDUP IN CUBA, OCT. 22, 1962"
S_SNIE = "SOURCE: SNIE 85-3-62, \"THE MILITARY BUILDUP IN CUBA,\" 19 SEPT. 1962 · IN " + CIA92
S_MCC = "SOURCE: McCONE CABLE OF SEPT. 10, 1962, AS QUOTED IN HIS MEMORANDUM OF OCT. 31, 1962 · IN " + CIA92
S_TAPE = "SOURCE: TRANSCRIPT, \"OFF THE RECORD MEETING ON CUBA,\" WHITE HOUSE, OCT. 16, 1962, 6:30 P.M. · JFK LIBRARY"
S_UN = "SOURCE: U.N. SECURITY COUNCIL, 1025TH MEETING, OCT. 25, 1962 (S/PV.1025)"
S_NSA = "SOURCE: NATIONAL SECURITY ARCHIVE, ELECTRONIC BRIEFING BOOK NO. 449 (2013), FROM SOVIET RECORDS"

CUBA = dict(kicker="1962", title="Western Cuba", bounds=[[-84.4, 22.0], [-81.0, 24.8]],
            points=[dict(ll=[-82.37, 23.13], name="Havana", sub="CAPITAL"),
                    dict(ll=[-83.05, 22.71], name="San Cristóbal", sub="SUSPECTED MISSILE SITE", color="#F2D04B", anchor="end"),
                    dict(ll=[-81.78, 24.56], name="Key West", sub="FLORIDA", anchor="end")],
            source="SOURCES: FRUS 1961–63 VOL. XI, DOC. 16; CIA MEMORANDUM, 16 OCT. 1962 · MAP: NATURAL EARTH · LOCATIONS APPROXIMATE")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("On the morning of October fourteenth, nineteen sixty-two, an Air Force pilot, Major Richard Heyser, flew a U-2 spy plane across western Cuba.",
  [C("dv908150", 166.0, lab=U2B)], dict(tag=("WESTERN CUBA", "OCT. 14, 1962"))),
 ("He was over the island for about six minutes. | His cameras took nine hundred and twenty-eight photographs.",
  [C("dv1017843", 226.0, lab=U2ALT)], {}),
 ("Two days later, the President of the United States was looking at some of them. | They showed what Soviet spokesmen had repeatedly said would never happen.",
  [I("oct14", kb="in", focus=[0.5, 0.45], lab=OCT14)], {}),
 ("Soviet ballistic missiles, being set up in Cuba.",
  [I("lospal", kb="in", focus=[0.4, 0.4], lab=LOSPAL)], dict(slow=True)),
 ("What followed was a thirteen-day standoff. Often called the closest the world has come to nuclear war.",
  [I("jfk1", kb="in", focus=[0.45, 0.4], lab=JFKNR)], {}),
 ("This is the story of those photographs. What they proved. What they missed. | And the documents that stayed secret for decades.",
  [I("memo16a", kb="in", focus=[0.5, 0.4], lab=MEMO)], {}),
 ("Let's open the file.",
  [G("intro", n="006")], dict(gap=0.2)),
 ("",
  [G("title", n="006", t="Thirteen Days", size=180, sub="The Cuban Missile Photos")], dict(gap=0.4)),

 # ---------------- I. THE WARNING ----------------
 ("The warning signs came weeks earlier.",
  [G("chapter", n="I", t="The Warning")], {}),
 ("On August twenty-ninth, nineteen sixty-two, a U-2 flight photographed something new in Cuba. Surface-to-air missile sites. | According to the C I A, eight of them were being set up, on what looked like a crash basis.",
  [G("stat", k="U-2 PHOTOGRAPHY · 29 AUGUST 1962", a="8", size=300, b="surface-to-air missile sites being set up", c="\"the program is proceeding on a crash basis\" · CIA memorandum", source="SOURCE: RAY S. CLINE, MEMORANDUM FOR ACTING DCI, \"RECENT SOVIET MILITARY ACTIVITIES IN CUBA,\" 3 SEPT. 1962 · IN " + CIA92)], {}),
 ("In public, Kennedy warned the Soviets twice, on September fourth and September thirteenth. | Moscow's answer, according to Kennedy, was a series of assurances. The buildup in Cuba was defensive, and the Soviet Union had no need to station strategic missiles in any other country.",
  [C("dv346124", 20.0, lab=WH)], {}),
 ("The director of the C I A, John McCone, was on his honeymoon in France. | He didn't like what he was hearing. It was difficult, he wrote, to rationalize such extensive, costly defenses.",
  [I("mccone10", kb="in", focus=[0.5, 0.45], lab=MCC)], {}),
 ("On September tenth, he cabled his deputy at headquarters. Appears to me quite possible, he wrote, measures now being taken are for purpose of insuring secrecy of some offensive capability such as M R B Ms. | Medium-range ballistic missiles.",
  [G("quote", q="Appears to me quite possible measures now being taken are for purpose of insuring secrecy {{of some offensive capability such as MRBMs}} to be installed by Soviets…",
     who="John A. McCone", role="Director of Central Intelligence · cable, Sept. 10, 1962", size=50, source=S_MCC)], {}),
 ("His own analysts disagreed. | On September nineteenth, the intelligence community's Special National Intelligence Estimate on Cuba weighed exactly that possibility.",
  [I("sniD", kb="in", focus=[0.5, 0.5], lab=SNI)], {}),
 ("Soviet missiles in Cuba, it said, would be incompatible with Soviet practice to date and with Soviet policy as we presently estimate it.",
  [G("quote", q="Either development, however, would be {{incompatible with Soviet practice to date}} and with Soviet policy as we presently estimate it.",
     who="Special National Intelligence Estimate 85-3-62", role="\"The Military Buildup in Cuba\" · Sept. 19, 1962", size=54, source=S_SNIE)], dict(slow=True)),
 ("The estimate was wrong. | By the beginning of October, according to the C I A's own account, analysts had marked an area near the town of San Cristóbal as a suspected missile site. | They needed a photograph.",
  [G("map", **CUBA)], dict(gap=0.9, sil=True)),

 # ---------------- II. THE FLIGHT ----------------
 ("The flight that got it was delayed for days by bad weather.",
  [G("chapter", n="II", t="The Flight")], {}),
 ("Heyser took off from Edwards Air Force Base, in California, late on October thirteenth. | He crossed into Cuba from the south, at about seven thirty in the morning, flying around fourteen miles high.",
  [C("dv908150", 362.0, lab=U2B), C("dv1017843", 241.0, lab=U2ALT)], {}),
 ("The C I A had planned one route. A C I A map shows the route the Air Force actually flew, straight over the target area.",
  [I("map14", kb="in", focus=[0.45, 0.45], lab=MAP14)], {}),
 ("About six minutes later he was out of Cuban airspace, and on his way to McCoy Air Force Base, in Florida. | The film went to Washington, to the National Photographic Interpretation Center.",
  [I("cam1", kb="in", focus=[0.5, 0.45], lab=CAMNR)], {}),
 ("After that morning, the flights didn't stop. | Another C I A map shows the Strategic Air Command's U-2 tracks over Cuba from October fifteenth to the twenty-second. The whole island, crossed again and again.",
  [I("sacmap", kb="in", focus=[0.5, 0.5], lab=SACMAP)], dict(gap=0.9, sil=True)),

 # ---------------- III. THE LIGHT TABLE ----------------
 ("And there, on October fifteenth, the analysts saw them.",
  [G("chapter", n="III", t="The Light Table")], {}),
 ("According to the National Geospatial-Intelligence Agency, the analyst who first found the evidence was Vincent DiRenzo, of the C I A.",
  [I("direnzo", kb="in", focus=[0.5, 0.3], lab=DIR)], {}),
 ("According to the State Department's official history, they identified three medium-range missile sites near San Cristóbal. | Eight large missile transporters. And four erector launchers, in tentative firing positions.",
  [I("oct14", kb="in", focus=[0.35, 0.6], lab=OCT14)], {}),
 ("Two more U-2 missions on October fifteenth found a fourth medium-range site. | Two sites for intermediate-range missiles, at Guanajay. And twenty-one crates for Soviet I L-twenty-eight bombers, at an airfield.",
  [G("list", kicker="U-2 MISSIONS · OCTOBER 14–15, 1962", title="What the film showed", items=[
     dict(n="01", t="Four MRBM sites near San Cristóbal", s="MEDIUM-RANGE BALLISTIC MISSILES"), dict(n="02", t="Two IRBM sites at Guanajay", s="INTERMEDIATE-RANGE BALLISTIC MISSILES"),
     dict(n="03", t="21 crates for IL-28 bombers", s="SAN JULIÁN AIRFIELD")], source=S_FRUS)], {}),
 ("How could they tell from fourteen miles up? | By measuring. The center's director, Arthur Lundahl, reported canvas-covered missile trailers about sixty-seven feet long and nine feet wide.",
  [I("lund16a", kb="in", focus=[0.5, 0.55], lab=LUND)], {}),
 ("At one launch site, he wrote, there were at least eight missile trailers, and four probable erector launchers. At the westernmost position, a missile trailer was lined up with its erector.",
  [I("lund16b", kb="in", focus=[0.5, 0.4], lab=LUND)], {}),
 ("The C I A compared those dimensions with what it knew of Soviet missiles. The trailers matched the general size and configuration of the S S-three and the S S-four.",
  [I("memo16a", kb="down", focus=[0.5, 0.6], lab=MEMO)], {}),
 ("The S S-four, the memo said, could carry a three-thousand-pound warhead about eleven hundred nautical miles.",
  [G("stat", k="CIA MEMORANDUM · 16 OCTOBER 1962", a="1,100", size=280, b="nautical miles · SS-4 maximum range", c="3,000-lb warhead · road-mobile · \"no heavy construction work\" needed", source=S_MEMO)], {}),
 ("That evening, a C I A deputy director, General Marshall Carter, told the President's national security adviser, McGeorge Bundy. | Bundy decided to wait. The President had come back from a campaign trip at one-forty that morning, and the briefing materials wouldn't be ready until morning. | Bundy wrote later that a quiet evening and a night of sleep were the best preparation the President could have.",
  [C("dv346124", 8.0, lab=WH)], {}),
 ("On October sixteenth, Kennedy was shown the photographs.",
  [I("lospal", kb="down", focus=[0.6, 0.5], lab=LOSPAL)], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE CHOICE ----------------
 ("What he did next was decided in secret.",
  [G("chapter", n="IV", t="The Choice")], {}),
 ("The C I A's memo that day attached a map. | Rings around Cuba. The outer one, labelled one thousand and twenty nautical miles, reached Washington.",
  [I("map16", kb="in", focus=[0.5, 0.42], lab=MAP16)], {}),
 ("But one thing was missing from every photograph. | No facility to store nuclear warheads, the memo said, could be identified at any of the sites.",
  [I("memo16b", kb="in", focus=[0.5, 0.75], lab=MEMO)], {}),
 ("At a meeting in the White House that evening, General Carter put it plainly. We have no evidence whatsoever of any nuclear warhead storage near the field launchers. | The analysts estimated the sites could be fully operational within two weeks.",
  [G("quote", q="We have no evidence whatsoever {{of any nuclear warhead storage near the field launchers.}}",
     who="Gen. Marshall S. Carter", role="Deputy Director of Central Intelligence · White House meeting, Oct. 16, 1962", size=58, source=S_TAPE)], {}),
 ("For six days, Kennedy and a small group of advisers argued in secret. | The Joint Chiefs, according to the State Department, all favored an air strike followed by an invasion.",
  [I("excomm", kb="in", focus=[0.5, 0.45], lab=EXC)], {}),
 ("Kennedy chose a middle course. | On the evening of October twenty-second, he went on television.",
  [I("jfk2", kb="in", focus=[0.5, 0.35], lab=JFKNR)], dict(tag=("WASHINGTON, D.C.", "OCT. 22, 1962"))),
 ("He told the country that some of the sites included medium-range ballistic missiles, capable of carrying a nuclear warhead for a distance of more than one thousand nautical miles. | Others appeared designed for intermediate-range missiles, able to reach most of the major cities in the hemisphere.",
  [G("quote", q="…medium-range ballistic missiles capable of carrying a nuclear warhead {{for a distance of more than 1,000 nautical miles.}}",
     who="President John F. Kennedy", role="Address to the nation · Oct. 22, 1962", size=56, source=S_JFK)], {}),
 ("He announced a strict quarantine on all offensive military equipment under shipment to Cuba. | Quarantine, not blockade. According to the State Department, the word legally distinguished it from a blockade. | The same day, the Joint Chiefs raised the military's alert level to DEFCON three.",
  [I("procl", kb="up", focus=[0.5, 0.4], lab=PROCL)], {}),
 ("And he drew a line. Any nuclear missile launched from Cuba against any nation in the Western Hemisphere would be treated as an attack by the Soviet Union on the United States.",
  [G("quote", q="…any nuclear missile launched from Cuba against any nation in the Western Hemisphere {{as an attack by the Soviet Union on the United States…}}",
     who="President John F. Kennedy", role="Address to the nation · Oct. 22, 1962", size=54, source=S_JFK)], dict(slow=True)),
 ("He didn't pretend it was safe. The path we have chosen for the present, he said, is full of hazards, as all paths are.",
  [I("jfk1", kb="down", focus=[0.45, 0.45], lab=JFKNR)], dict(gap=0.9, sil=True)),

 # ---------------- V. THE PROOF ----------------
 ("Now the photographs had to convince the world.",
  [G("chapter", n="V", t="The Proof")], {}),
 ("On October twenty-third, Navy reconnaissance jets began flying low over Cuba. RF-8A Crusaders, from Light Photographic Squadron Sixty-Two, under the code name Blue Moon. | Their film was developed at Naval Air Station Jacksonville, in Florida.",
  [C("dv1024711", 7.5, lab=DDG), I("p2h", kb="in", focus=[0.5, 0.5], lab=P2H)], {}),
 ("They flew from Key West, streaking in over Cuba at low level, and brought back close-up pictures of the missile sites.",
  [I("lowsc2", kb="in", focus=[0.45, 0.5], lab=LOW)], {}),
 ("On October twenty-fifth, at the United Nations Security Council, the American ambassador, Adlai Stevenson, turned to the Soviet ambassador, Valerian Zorin.",
  [I("un1", kb="in", focus=[0.5, 0.5], lab=UNNR)], dict(tag=("UNITED NATIONS, N.Y.", "OCT. 25, 1962"))),
 ("Do you, Ambassador Zorin, deny that the U S S R has placed and is placing medium- and intermediate-range missiles and sites in Cuba? | Yes or no. Don't wait for the translation.",
  [G("quote", q="Do you, Ambassador Zorin, deny that the U.S.S.R. has placed and is placing medium- and intermediate-range missiles and sites in Cuba? {{Yes or no—don't wait for the translation—yes or no?}}",
     who="Ambassador Adlai E. Stevenson", role="U.N. Security Council · Oct. 25, 1962", size=46, source=S_UN)], {}),
 ("Zorin refused to answer. Earlier, he had called the American evidence false. | Stevenson said he was prepared to wait for an answer until hell freezes over. | And he was prepared to present the evidence in that room. His team set up enlarged reconnaissance photographs.",
  [I("un2", kb="in", focus=[0.45, 0.5], lab=UNNR), I("nrboard", kb="in", focus=[0.5, 0.5], lab=BRDNR)], {}),
 ("Meanwhile, the work on the missile sites continued. In one photograph from that same day, tracks in the ground led to a missile shelter tent.",
  [I("oct25", kb="in", focus=[0.5, 0.5], lab=OCT25)], dict(gap=0.9, sil=True)),

 # ---------------- VI. THE EDGE ----------------
 ("Then came the worst day of the crisis.",
  [G("chapter", n="VI", t="The Edge")], {}),
 ("On October twenty-sixth, Khrushchev sent Kennedy a long, emotional message, hinting at a deal. Let us take measures, he wrote, to untie that knot. | The next day, a second message raised the price. Any deal must include the removal of American Jupiter missiles from Turkey.",
  [C("dv1026930", 22.0, lab=DC)], {}),
 ("That same day, October twenty-seventh, a U-2 was shot down over Cuba by a Soviet-built surface-to-air missile. | Its pilot, Air Force Major Rudolf Anderson, was killed.",
  [C("dv908150", 192.0, lab=U2B)], dict(slow=True)),
 ("Kennedy answered the first message, and ignored the second. | He offered a guarantee against an invasion of Cuba, in return for removing the missiles under United Nations supervision.",
  [I("jfk3", kb="in", focus=[0.5, 0.35], lab=JFKNR)], {}),
 ("In private, his brother, Attorney General Robert Kennedy, met the Soviet ambassador, Anatoly Dobrynin. | He indicated that the Jupiters would be removed from Turkey soon anyway. But that could not be part of any public deal.",
  [C("dv346026", 4.0, lab=CAP)], {}),
 ("On October twenty-eighth, Khrushchev announced that the missiles would be dismantled and taken home.",
  [I("nrboard2", kb="in", focus=[0.5, 0.5], lab=BRD2)], dict(gap=0.9, sil=True)),

 # ---------------- VII. WHAT THE PHOTOS MISSED ----------------
 ("So what did those photographs actually prove?",
  [G("chapter", n="VII", t="What They Missed")], {}),
 ("They proved that Soviet ballistic missiles were being installed in Cuba, while Soviet officials said otherwise. | And they proved it with photographs that anyone at the U N could look at.",
  [I("oct14", kb="out", focus=[0.5, 0.5], lab=OCT14)], {}),
 ("But the cameras never saw the warheads. | Decades later, at a conference in Havana in January nineteen ninety-two, a Soviet general, Anatoly Gribkov, revealed that Soviet nuclear warheads had been in Cuba in nineteen sixty-two.",
  [I("memo16b", kb="out", focus=[0.5, 0.5], lab=MEMO)], {}),
 ("According to Soviet records published by the National Security Archive, that included ninety-eight tactical nuclear warheads. Eighty for short-range cruise missiles, twelve for Luna rockets, and six bombs.",
  [G("stat", k="SOVIET RECORDS · PUBLISHED 2013", a="98", size=300, b="tactical nuclear warheads in Cuba", c="80 for FKR-1 cruise missiles · 12 for Luna rockets · 6 bombs for IL-28s", source=S_NSA)], {}),
 ("According to the Archive, U S intelligence did not detect any of the nuclear warheads in Cuba during the crisis. | And after the deal of October twenty-eighth, almost forty-three thousand Soviet troops, and all the nuclear warheads, were still on the island.",
  [G("quote", q="U.S. intelligence did not detect {{any of the nuclear warheads in Cuba}} during the crisis.",
     who="National Security Archive", role="Electronic Briefing Book No. 449 · Dec. 11, 2013", size=62, source=S_NSA)], {}),
 ("The quarantine stayed in place until the Soviets agreed to remove their I L-twenty-eight bombers. It ended on November twentieth. The Jupiter missiles left Turkey in April nineteen sixty-three. | And ten U-2 pilots of the Cuba flights were awarded the Distinguished Flying Cross.",
  [I("usafgrp", kb="in", focus=[0.5, 0.45], lab=USAF), I("usafpin", kb="in", focus=[0.5, 0.4], lab=USAF)], {}),
 ("The two leaders had struggled to read each other's intentions. Afterwards, they set up a direct line between the White House and the Kremlin. The Hotline.",
  [C("dv346124", 30.0, lab=WH)], {}),
 ("Every secret has a release date. The C I A's memo from October sixteenth was published in nineteen ninety-two. The warheads came out of Soviet files. | Thirteen days in October took decades to fully come into view.",
  [I("map16", kb="out", focus=[0.5, 0.5], lab=MAP16)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments.",
  [C("dv1026934", 12.0, lab=DC)], {}),
 ("Next time: the C I A, a sunken Soviet submarine, and a ship built to lift it.",
  [G("end", n="006", next="Project Azorian")], dict(gap=2.5)),
]

PRON = [("Heyser", "High-zer"), ("Lundahl", "Lun-doll"), ("McCone", "Mc-Cone"), ("Zorin", "Zor-in"), ("Gribkov", "Grib-koff"),
        ("Dobrynin", "Doh-bree-nin"), ("Khrushchev", "Kroosh-chev"), ("San Cristóbal", "San Cris-toe-bal"), ("Guanajay", "Gwah-nah-high"),
        ("Valerian", "Va-leh-ree-an"), ("Anatoly", "Anna-toe-lee"), ("Luna", "Loona"), ("RF-8A", "R F eight A"), ("U-2", "U two"),
        ("S S-three", "S S three"), ("S S-four", "S S four"), ("M R B Ms", "M R B Ms"), ("U S S R", "U S S R"), ("U N", "U N"),
        ("C I A's", "C I A's"), ("Bundy", "Bun-dee"), ("U S intelligence", "U S intelligence"), ("I L-twenty-eight", "I L twenty-eight"), ("DiRenzo", "Dee-Ren-zo"), ("DEFCON three", "Def-con three"), ("Jupiters", "Jupiters")]

DISPLAY = [
 ("U S intelligence", "U.S. intelligence"), ("C I A's", "CIA's"), ("C I A", "CIA"), ("I L-twenty-eight", "IL-28"), ("M R B Ms", "MRBMs"), ("U S S R", "USSR"), ("U N", "UN"),
 ("S S-three", "SS-3"), ("S S-four", "SS-4"),
 ("nineteen sixty-two", "1962"), ("nineteen sixty-three", "1963"), ("nineteen ninety-two", "1992"),
 ("October fourteenth", "October 14"), ("October thirteenth", "October 13"), ("October fifteenth", "October 15"),
 ("October sixteenth", "October 16"), ("October twenty-second", "October 22"), ("October twenty-third", "October 23"),
 ("October twenty-fifth", "October 25"), ("October twenty-sixth", "October 26"), ("October twenty-seventh", "October 27"),
 ("October twenty-eighth", "October 28"), ("November twentieth", "November 20"), ("August twenty-ninth", "August 29"),
 ("September tenth", "September 10"), ("September nineteenth", "September 19"),
 ("nine hundred and twenty-eight", "928"), ("ninety miles", "90 miles"), ("sixty-seven feet", "67 feet"), ("nine feet", "9 feet"),
 ("three-thousand-pound", "3,000-pound"), ("eleven hundred", "1,100"), ("one thousand and twenty", "1,020"),
 ("one thousand nautical", "1,000 nautical"), ("ninety-eight", "98"), ("Eighty for", "80 for"), ("twelve for", "12 for"),
 ("six bombs", "6 bombs"), ("forty-three thousand", "43,000"), ("Sixty-Two", "62"), ("seven thirty", "7:30"), ("one-forty", "1:40"), ("twenty-one crates", "21 crates"), ("DEFCON three", "DEFCON 3"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="006", title="Thirteen Days: The Cuban Missile Photos",
    imgs={k: D + k + ".jpg" for k in ["oct14", "lospal", "lowsc2", "nov1", "oct25", "map14", "sacmap", "memo16a", "memo16b", "map16",
                                       "lund16a", "lund16b", "mccone10", "sniD", "jfk1", "jfk2", "jfk3", "un1", "un2", "cam1", "nrboard",
                                       "nrship", "nrboard2", "direnzo", "excomm", "procl", "p2h", "usafgrp", "usafpin"]},
    credit="Documents: CIA (1992 release). Photographs: U.S. government (JFK Library/NARA, NGA, White House, U.S. Navy).\\NFilm: Universal Newsreel and U.S. Air Force (NARA). B-roll: DoD via DVIDS. No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[1, 4], hook="6 MINUTES.<br>[928 PHOTOS]"),
        dict(id="s2", lines=[12, 15], hook="THE ESTIMATE SAID<br>[INCOMPATIBLE]"),
        dict(id="s3", lines=[45, 47], hook="'UNTIL HELL<br>[FREEZES OVER]'"),
        dict(id="s4", lines=[57, 59], hook="WHAT THE PHOTOS<br>[MISSED]"),
    ],
)
