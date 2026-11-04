# FILE 007 — Project Azorian: The Ship Built to Steal a Submarine
# Format: see episodes/001-navy-videos/episode.py
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
HISTN = "CIA, \"PROJECT AZORIAN: THE STORY OF THE HUGHES GLOMAR EXPLORER\" (STUDIES IN INTELLIGENCE, 1985; RELEASED 2010)"
HIST = "ACTUAL DOCUMENT · " + HISTN
BLANK = "ACTUAL DOCUMENT · A FULLY WITHHELD PAGE · " + HISTN
FIG5 = "ACTUAL DOCUMENT · \"FIGURE 5. SCHEMATIC DRAWING\" OF THE HUGHES GLOMAR EXPLORER · IN THE CIA HISTORY (RELEASED 2010)"
PDB = "ACTUAL DOCUMENT · THE PRESIDENT'S DAILY BRIEF, APRIL 8, 1975 (RELEASED 2016)"
LETTER = "ACTUAL DOCUMENT · CIA FOIA RESPONSE LETTER, JAN. 19, 2012 (EXCERPT)"
OKC = "B-ROLL · U.S. NAVY SUBMARINE USS OKLAHOMA CITY UNDERWAY, 2019"
COLO = "B-ROLL · U.S. NAVY SUBMARINE USS COLORADO ARRIVING AT PEARL HARBOR, HAWAII, 2026"
GRAB = "B-ROLL · HYDRAULIC SALVAGE GRAB ON A HEAVY-LIFT CRANE SHIP, BALTIMORE, 2024 · NOT THE AZORIAN CLAW"
CRANE = "B-ROLL · HEAVY-LIFT CRANE SHIP, BALTIMORE, 2024"
FOG = "B-ROLL · U.S. COAST GUARD CUTTER EAGLE IN FOG, ATLANTIC OCEAN, 2009"
BOXER = "B-ROLL · AT SEA ABOARD THE USS BOXER, 2026"
SEA1 = "B-ROLL · NOAA REMOTELY OPERATED VEHICLE ON A SEAMOUNT, NORTH ATLANTIC, 2021"
SEA2 = "B-ROLL · NOAA REMOTELY OPERATED VEHICLE ON THE SEAFLOOR OFF ALASKA, NORTH PACIFIC, 2023"
OKEX = "B-ROLL · NOAA SHIP OKEANOS EXPLORER AT SEA, 2021"
OKEXROV = "B-ROLL · NOAA REMOTELY OPERATED VEHICLE LOWERED FROM OKEANOS EXPLORER, 2021"
OKCIN = "B-ROLL · ABOARD THE U.S. NAVY SUBMARINE USS OKLAHOMA CITY, 2019"
ROV = "B-ROLL · RESEARCH VEHICLE LOWERED INTO THE SEA, NOAA OCEAN EXPLORATION, 2024"
WH = "B-ROLL · THE WHITE HOUSE, WASHINGTON, D.C., 2012"
CAP = "B-ROLL · U.S. CAPITOL, WASHINGTON, D.C., 2012"

S_HIST = "SOURCE: " + HISTN
S_FRUS = "SOURCE: MEMORANDUM OF CONVERSATION, WHITE HOUSE CABINET ROOM, MARCH 19, 1975 · FRUS 1969–1976, VOL. XXXV, DOC. 197"
S_USIB = "SOURCE: U.S. INTELLIGENCE BOARD ASSESSMENT, MAY 1974, AS QUOTED IN " + HISTN
S_PHIL = "SOURCE: PHILLIPPI v. CIA, 546 F.2d 1009 (D.C. CIR. 1976), QUOTING THE AGENCY'S RESPONSE"

PAC = dict(kicker="MARCH 1968", title="The North Pacific", rotate=[180, 0, 0], bounds=[[138.0, 12.0], [-112.0, 58.0]],
           points=[dict(ll=[158.65, 53.02], name="Petropavlovsk", sub="SOVIET SUBMARINE BASE"),
                   dict(ll=[-176.0, 37.5], name="Approximate area of loss", sub="≈1,560 MI NW OF HAWAII", color="#F2D04B"),
                   dict(ll=[-157.86, 21.31], name="Hawaii", sub="HONOLULU"),
                   dict(ll=[-118.19, 33.77], name="Long Beach", sub="CALIFORNIA")],
           source="SOURCE: " + HISTN + " · MAP: NATURAL EARTH · LOSS LOCATION APPROXIMATE")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("In March nineteen sixty-eight, a Soviet ballistic missile submarine went down in the Pacific Ocean, with all hands.",
  [C("noaa_boulder", 36.0, lab=SEA2)], dict(tag=("NORTH PACIFIC", "MARCH 1968"))),
 ("It came to rest about sixteen thousand five hundred feet down. More than three miles.",
  [C("noaa_boulder", 28.0, lab=SEA2)], {}),
 ("The Soviets searched for two months, and never found it. | The C I A decided to go and get it.",
  [C("dv751245", 4.0, lab=OKC)], {}),
 ("To do it, the Agency had one of the strangest ships of the Cold War built, and told the world it was a mining ship, for Howard Hughes.",
  [I("az_fig5", kb="in", focus=[0.5, 0.45], lab=FIG5)], {}),
 ("It was called the Hughes Glomar Explorer. And when a reporter later asked about it, the C I A gave an answer agencies still use today. | Neither confirm, nor deny.",
  [I("glomar_letter", kb="in", focus=[0.5, 0.5], lab=LETTER)], {}),
 ("This is Project Azorian, as told by the C I A's own history. Declassified in twenty ten, with whole pages still blank.",
  [I("az_blank", kb="in", focus=[0.5, 0.5], lab=BLANK)], {}),
 ("Let's open the file.",
  [G("intro", n="007")], dict(gap=0.2)),
 ("",
  [G("title", n="007", t="Project Azorian", size=170, sub="The Ship Built to Steal a Submarine")], dict(gap=0.4)),

 # ---------------- I. THE LOST SUBMARINE ----------------
 ("It started with a submarine that never came home.",
  [G("chapter", n="I", t="The Lost Sub")], {}),
 ("According to the C I A, the diesel-powered submarine left Petropavlovsk on about March first, nineteen sixty-eight, for a patrol station northeast of Hawaii. | From there, the history says, it would be available for nuclear attack on U S targets, in the event of war.",
  [G("map", **PAC)], {}),
 ("It never got there. The submarine suffered an accident, cause unknown, and sank about fifteen hundred and sixty miles northwest of Hawaii.",
  [C("noaa_boulder", 40.0, lab=SEA2)], {}),
 ("In the West it is usually called K-one twenty-nine. The C I A's history calls it the G-seven twenty-two.",
  [I("az_story", kb="in", focus=[0.5, 0.55], lab=HIST)], {}),
 ("The Soviets ran a massive search for two months. It was fruitless. | How the United States found the wreck, the history does not say.",
  [C("dv751245", 12.0, lab=OKC), C("dv751245", 22.0, lab=OKC)], {}),
 ("What mattered was what might be inside. | In nineteen seventy-four, the U S Intelligence Board spelled it out.",
  [C("dv751245", 41.0, lab=OKC)], {}),
 ("Acquisition of the nuclear warheads and the S S-N-five missile system, together with related documents, would provide a much-improved baseline for estimates of the current and future Soviet strategic threat.",
  [G("quote", q="Acquisition of the nuclear warheads and the SS-N-5 missile system, together with related documents, {{would provide a much-improved baseline}} for estimates of the current and future Soviet strategic threat.",
     who="U.S. Intelligence Board", role="assessment of Project AZORIAN · May 1974", size=48, source=S_USIB)], {}),
 ("Back in April nineteen sixty-nine, Deputy Secretary of Defense David Packard had asked the C I A to take the lead. | Nobody had ever lifted anything that size from that depth.",
  [C("dv346124", 20.0, lab=WH)], dict(gap=0.9, sil=True)),

 # ---------------- II. THE COVER STORY ----------------
 ("The engineers had to invent almost everything.",
  [G("chapter", n="II", t="The Cover Story")], {}),
 ("They studied buoyant material carried to the bottom, gas generated at depth, giant floating winches. | They chose brute force. A ship would lower a string of steel pipe more than three miles, grab the target, and pull it up.",
  [C("noaa_rov", 6.0, lab=ROV)], {}),
 ("The target, the C I A estimated, weighed about seventeen hundred and fifty tons. | In nineteen seventy, the project put the chance of success at about ten percent.",
  [G("stat", k="CIA ESTIMATE · OCTOBER 1970", a="1,750", size=280, b="tons · estimated weight of the target", c="to be lifted from 16,500 feet · early odds of success: about 10%", source=S_HIST)], {}),
 ("Packard's view, as the history puts it: if they were to wait until all the risks were eliminated, the project would never get under way.",
  [C("noaa_dive01", 19.5, lab="B-ROLL · DEEP-SEA LIFE FILMED BY A NOAA REMOTELY OPERATED VEHICLE, NORTH ATLANTIC, 2021")], {}),
 ("A ship like that needed a reason to exist. So it got a cover story. | Deep-ocean mining, for a company owned by Howard Hughes.",
  [I("az_fig5", kb="right", focus=[0.5, 0.5], lab=FIG5)], {}),
 ("In April nineteen seventy-one, the contractor, Global Marine, announced a six-hundred-foot mining ship for the Hughes Tool Company. | It was launched in Pennsylvania on November fourth, nineteen seventy-two, with champagne and speeches.",
  [C("dv921148", 8.0, lab=CRANE), C("dv921148", 14.0, lab=CRANE)], {}),
 ("Inside was what no mining ship needed. A huge well in the middle of the hull, with gates that opened to the sea. | On this page of the C I A's history, a large box is still withheld.",
  [I("az_redbox", kb="in", focus=[0.5, 0.4], lab=HIST)], {}),
 ("Not everyone wanted it. In nineteen seventy-two, the chairman of the Joint Chiefs said he could not support the mission. | A new Deputy Secretary of Defense put the odds of technical success at twenty to thirty percent.",
  [G("list", kicker="1972 · THE DOUBTERS", title="Inside the government", items=[
     dict(n="AUG", t="Joint Chiefs chairman: \"could not support\"", s="ADM. THOMAS MOORER"),
     dict(n="SEP", t="Odds of technical success: 20–30%", s="DEP. SEC. OF DEFENSE KENNETH RUSH"),
     dict(n="DEC", t="The President decides to continue", s="RICHARD NIXON")], source=S_HIST)], {}),
 ("The costs kept growing. In the history, the dollar figures are blacked out. | But in December nineteen seventy-two, President Nixon decided to continue.",
  [C("dv346124", 8.0, lab=WH)], {}),
 ("The ship was too wide for the Panama Canal, so in nineteen seventy-three it sailed around South America. | It reached Valparaíso, in Chile, during the military coup of September eleventh. The C I A called that a bizarre coincidence.",
  [C("dv751245", 0.6, lab=OKC)], dict(gap=0.9, sil=True)),

 # ---------------- III. THE MISSION ----------------
 ("In June nineteen seventy-four, it was time.",
  [G("chapter", n="III", t="The Mission")], {}),
 ("Nixon approved the mission on June seventh, with one condition. No recovery until he was back from a summit in Moscow. | On June twentieth, the Glomar Explorer left its anchorage off Long Beach. The next day, it set course for the site, with a crew of one hundred and seventy-eight. That number was set by the lifeboats.",
  [C("noaa_dive01", 51.0, lab=OKEX), C("noaa_rov", 8.0, lab=ROV), C("dv1027407", 1.0, lab=BOXER)], dict(tag=("OFF LONG BEACH, CALIFORNIA", "JUNE 1974"))),
 ("It reached the site on July fourth. Then the weather turned. | A typhoon swell. Cracks in the docking-leg guides. A tropical storm.",
  [C("dv751245", 20.0, lab=OKC)], {}),
 ("A British merchant ship, the Bel Hudson, radioed for medical help. The ship's doctor went across, treated a sick sailor, and sent him back. | Asked what they were doing, the crew said: deep-ocean mining, with a prototype mining machine. The C I A hoped the Soviets were listening.",
  [C("dv319240", 52.0, lab=FOG), C("dv319240", 76.0, lab=FOG)], {}),
 ("And on July eighteenth, a Soviet ship came out of the fog. The missile range instrumentation ship Chazhma.",
  [C("dv319240", 103.0, lab=FOG)], {}),
 ("Its helicopter made pass after pass, photographing the Glomar Explorer from every angle. | The crew had stacked crates on the helicopter deck, so it couldn't land.",
  [C("dv319240", 30.0, lab=FOG)], {}),
 ("A team was ready to destroy classified material if the Soviets tried to board. | Guns, the history notes, were not issued.",
  [I("az_guns", kb="in", focus=[0.5, 0.6], lab=HIST)], {}),
 ("Then the Soviet ship called over. We are on our way home and heard your fog horn. | What are you doing here?",
  [I("az_chazhma", kb="in", focus=[0.6, 0.55], lab=HIST)], dict(slow=True)),
 ("The answer came straight from the cover story. We are conducting ocean mining tests. Deep-ocean mining tests. | How much time will you be here? Two to three weeks. | The Soviet ship signed off. I wish you all the best.",
  [G("doc", header="RADIO EXCHANGE · JULY 18, 1974 · RECREATED", title="Chazhma and the Glomar Explorer", lines=[
     "CHAZHMA: \"We are on our way home and heard your fog horn. {{What are you doing here?}}\"",
     "HGE: \"We are conducting ocean mining tests—deep-ocean mining tests.\"",
     "CHAZHMA: \"How much time will you be here?\"",
     "HGE: \"We expect to finish testing in two to three weeks.\"",
     "CHAZHMA: \"{{I wish you all the best.}}\""],
     source="SOURCE: " + HISTN + " · EXCERPTS, RECREATED")], {}),
 ("Days later, a Soviet salvage tug arrived. It stayed for almost two weeks, at times passing within two hundred feet.",
  [I("az_chazhma2", kb="in", focus=[0.5, 0.5], lab=HIST)], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE LIFT ----------------
 ("Underneath them, the pipe kept going down.",
  [G("chapter", n="IV", t="The Lift")], {}),
 ("Sixty-foot doubles of pipe, about fifteen tons each, one after another. | Then, on August first, the history reads: lifted from the bottom. The words before that are blacked out.",
  [I("az_liftoff", kb="in", focus=[0.4, 0.4], lab=HIST)], {}),
 ("By then, two hundred and seventy-four doubles were in the water. Sixteen thousand four hundred and forty feet of pipe.",
  [G("stat", k="AUGUST 2, 1974", a="16,440", size=280, b="feet of pipe deployed and coming up", c="274 doubles · about 15 tons each", source=S_HIST)], {}),
 ("The tug was still circling. The C I A's history allows itself a smile. Two Soviet Navy ships, it says, had in effect witnessed the recovery.",
  [G("quote", q="…two Soviet Navy ships were on the scene and, in effect, {{witnessed the recovery operation}} against their lost submarine.",
     who="CIA history of Project AZORIAN", role="Studies in Intelligence · 1985", size=56, source=S_HIST)], {}),
 ("Even now, the cover held. Over open commercial radio, the ship reported that its nodule collector vehicle might have hit a hard outcrop on the bottom. | The damage was fiction. It was the excuse for a trip to port.",
  [C("dv751245", 95.0, lab=OKCIN)], {}),
 ("But the lift did not go as planned. According to a twenty ten book by Norman Polmar and Michael White, as summarized in a C I A review in twenty twelve, two of the grabber arms snapped. | Nearly one hundred feet of the section they held broke away, and fell back to the ocean floor.",
  [C("dv921148", 28.5, lab=GRAB), C("dv921148", 32.5, lab=GRAB)], dict(slow=True)),
 ("The C I A's history never says how much came up. Its first page reads: on August eighth, nineteen seventy-four, a blank, then, that submarine was brought to the surface.",
  [I("az_story", kb="down", focus=[0.5, 0.6], lab=HIST)], {}),
 ("Eight months later, the President's Daily Brief put it plainly. The Glomar Explorer raised part of their submarine.",
  [I("pdb_ussr", kb="in", focus=[0.5, 0.55], lab=PDB)], {}),
 ("Inside, the team found plutonium contamination, apparently from one or more nuclear torpedoes. Their high explosive had gone off without a nuclear explosion. | The warheads, the history says, were one point safe.",
  [I("az_pluto", kb="in", focus=[0.5, 0.45], lab=HIST)], {}),
 ("According to a later C I A article, they also found the remains of several Soviet crewmen. They were buried at sea. | According to the National Security Archive, a videotape of that burial was later given to Russian President Boris Yeltsin.",
  [C("dv1024936", 0.5, lab=COLO)], dict(slow=True, gap=0.9, sil=True)),

 # ---------------- V. THE LEAK ----------------
 ("The secret lasted about six months.",
  [G("chapter", n="V", t="The Leak")], {}),
 ("In June nineteen seventy-four, burglars broke into the Los Angeles headquarters of Hughes's Summa Corporation. | The C I A feared the stolen papers included a memo about the plan.",
  [I("az_cover", kb="in", focus=[0.5, 0.5], lab=HIST)], {}),
 ("In February nineteen seventy-five, the Los Angeles Times ran a story. The history calls it unspecific, and wrong in important facts. | On March eighteenth, Jack Anderson broke it on the radio.",
  [C("dv346026", 4.0, lab=CAP)], {}),
 ("The next morning, President Ford met his advisers in the Cabinet Room. | Defense Secretary James Schlesinger wanted to acknowledge the bare facts. No comment, he said, would be taken as a confirmation.",
  [G("quote", q="This episode has been {{a major American accomplishment.}}",
     who="James R. Schlesinger", role="Secretary of Defense · White House, March 19, 1975", size=62, source=S_FRUS)], {}),
 ("The C I A director, William Colby, disagreed. He pointed to nineteen sixty, when a U-2 shot down over the Soviet Union wrecked a summit. | I go back to the U-2, he said. I think we should not put the Soviet Union under such pressure to respond.",
  [G("quote", q="I go back to the U–2. {{I think we should not put the Soviet Union under such pressure to respond.}}",
     who="William E. Colby", role="Director of Central Intelligence · White House, March 19, 1975", size=56, source=S_FRUS)], {}),
 ("The government said nothing. | In April, the President's Daily Brief reported that the Soviets were patrolling the site. And that Moscow, it seemed, wanted to avoid the subject if possible.",
  [I("pdb_ussr", kb="down", focus=[0.5, 0.5], lab=PDB)], {}),
 ("Colby had proposed a second mission, code-named Matador. The White House killed it.",
  [C("dv346124", 30.0, lab=WH)], dict(gap=0.9, sil=True)),

 # ---------------- VI. NEITHER CONFIRM NOR DENY ----------------
 ("The last word went to a journalist.",
  [G("chapter", n="VI", t="Neither Confirm Nor Deny")], {}),
 ("Harriet Ann Phillippi filed a Freedom of Information request for C I A records on its efforts to keep the story out of the press.",
  [C("dv346026", 12.0, lab=CAP)], {}),
 ("The answer she got: involvement by the U S Government in the activities which are the subject matter of your request can neither be confirmed nor denied.",
  [G("quote", q="…in the interest of national security, involvement by the U.S. Government in the activities which are the subject matter of your request {{can neither be confirmed nor denied.}}",
     who="Central Intelligence Agency", role="response to Harriet Ann Phillippi · 1975", size=48, source=S_PHIL)], dict(slow=True)),
 ("She sued. In nineteen seventy-six, a federal appeals court told the C I A to explain in public, as fully as it could, why it could not confirm or deny.",
  [C("dv346026", 17.0, lab=CAP)], {}),
 ("That kind of answer now has a name. The Glomar response. | A C I A letter from twenty twelve: the C I A can neither confirm nor deny the existence or nonexistence of records responsive to your request.",
  [I("glomar_letter", kb="in", focus=[0.45, 0.45], lab=LETTER)], {}),
 ("On June sixth, twenty fourteen, the C I A's very first tweet read: We can neither confirm nor deny that this is our first tweet.",
  [G("quote", q="We can neither confirm nor deny {{that this is our first tweet.}}",
     who="Central Intelligence Agency", role="first post on Twitter · June 6, 2014", size=70, source="SOURCE: CIA ON TWITTER, JUNE 6, 2014, AS REPORTED BY PBS NEWSHOUR")], dict(gap=0.9, sil=True)),

 # ---------------- VII. STILL BLANK ----------------
 ("So what is in the file today?",
  [G("chapter", n="VII", t="Still Blank")], {}),
 ("The C I A's history was published in nineteen eighty-five, and released in twenty ten. | Its cover note said almost all aspects of the project were still classified.",
  [I("az_cover", kb="down", focus=[0.5, 0.35], lab=HIST)], {}),
 ("Even the name in the newspapers was wrong. The press called it Jennifer. | The project was Azorian. Jennifer was the name of its security system.",
  [G("list", kicker="THE CODE NAMES", title="What the papers got wrong", items=[
     dict(n="01", t="AZORIAN", s="THE RECOVERY PROJECT"), dict(n="02", t="JENNIFER", s="THE SECURITY SYSTEM · USED BY THE PRESS"),
     dict(n="03", t="MATADOR", s="THE SECOND MISSION · CANCELLED")], source="SOURCE: " + HISTN + " · MATADOR: D. ROBARGE, \"THE GLOMAR EXPLORER IN FILM AND PRINT,\" STUDIES IN INTELLIGENCE 56:1 (CIA, 2012)")], {}),
 ("The cost is blacked out. Much of what was recovered is blacked out. | Some pages are blank from top to bottom.",
  [I("az_blank", kb="out", focus=[0.5, 0.5], lab=BLANK)], {}),
 ("What we do know: a ship built on a cover story reached more than three miles down, and brought back part of a Soviet submarine, while Soviet ships watched.",
  [I("az_fig5", kb="out", focus=[0.5, 0.5], lab=FIG5)], {}),
 ("Every secret has a release date. This one came out in pieces. | And some of it, the C I A can still neither confirm, nor deny.",
  [C("noaa_boulder", 30.0, lab=SEA2)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments.",
  [C("dv1024936", 140.0, lab=COLO)], {}),
 ("Next time: the government's first official report on U A P. One hundred and forty-four reports, and one explanation.",
  [G("end", n="007", next="144 Reports, 1 Explained")], dict(gap=2.5)),
]

PRON = [("Azorian", "Ah-zor-ee-an"), ("Glomar", "Glow-mar"), ("Petropavlovsk", "Petro-pav-lofsk"), ("Chazhma", "Chazh-ma"),
        ("Phillippi", "Fill-ip-ee"), ("Valparaíso", "Val-pa-rye-so"), ("Schlesinger", "Shlesinger"), ("Yeltsin", "Yelt-sin"),
        ("Matador", "Matador"), ("K-one twenty-nine", "K one twenty-nine"), ("G-seven twenty-two", "G seven twenty-two"),
        ("S S-N-five", "S S N five"), ("U-2", "U two"), ("U S Government", "U S Government"), ("U S Intelligence", "U S Intelligence"),
        ("U S targets", "U S targets"), ("C I A's", "C I A's"), ("U A P", "U A P"), ("Colby", "Col-bee"), ("Summa", "Soo-ma")]

DISPLAY = [
 ("U S Government", "U.S. Government"), ("U S Intelligence", "U.S. Intelligence"), ("U S targets", "U.S. targets"),
 ("C I A's", "CIA's"), ("C I A", "CIA"), ("U A P", "UAP"), ("S S-N-five", "SS-N-5"), ("K-one twenty-nine", "K-129"), ("G-seven twenty-two", "G-722"),
 ("nineteen sixty-eight", "1968"), ("nineteen sixty-nine", "1969"), ("nineteen seventy-one", "1971"), ("nineteen seventy-two", "1972"),
 ("nineteen seventy-three", "1973"), ("nineteen seventy-four", "1974"), ("nineteen seventy-five", "1975"), ("nineteen seventy-six", "1976"),
 ("nineteen seventy", "1970"), ("nineteen sixty", "1960"), ("nineteen eighty-five", "1985"), ("twenty ten", "2010"), ("twenty twelve", "2012"), ("twenty fourteen", "2014"),
 ("March first", "March 1"), ("November fourth", "November 4"), ("September eleventh", "September 11"), ("June seventh", "June 7"),
 ("June twentieth", "June 20"), ("July fourth", "July 4"), ("July eighteenth", "July 18"), ("August first", "August 1"),
 ("August eighth", "August 8"), ("March eighteenth", "March 18"), ("June sixth", "June 6"),
 ("sixteen thousand five hundred", "16,500"), ("sixteen thousand four hundred and forty", "16,440"), ("seventeen hundred and fifty", "1,750"),
 ("fifteen hundred and sixty", "1,560"), ("one hundred and seventy-eight", "178"), ("two hundred and seventy-four", "274"),
 ("six-hundred-foot", "600-foot"), ("Sixty-foot", "60-foot"), ("two hundred feet", "200 feet"), ("Sixteen thousand four hundred and forty", "16,440"), ("one hundred feet", "100 feet"),
 ("One hundred and forty-four", "144"), ("ten percent", "10 percent"), ("twenty to thirty percent", "20 to 30 percent"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="007", title="Project Azorian: The Ship Built to Steal a Submarine",
    imgs={k: D + k + ".jpg" for k in ["az_fig5", "glomar_letter", "az_blank", "az_story", "az_redbox", "az_guns", "az_chazhma",
                                       "az_chazhma2", "az_liftoff", "pdb_ussr", "az_pluto", "az_cover"]},
    credit="Documents: CIA (released 2010, 2012, 2016); FRUS (U.S. Dept. of State). B-roll: DoD and U.S. Coast Guard via DVIDS;\\NNOAA Ocean Exploration. Modern footage does not show the 1974 events. No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[10, 16], hook="A LOST SOVIET<br>[MISSILE SUB]"),
        dict(id="s2", lines=[30, 36], hook="'WHAT ARE YOU<br>[DOING HERE?]'"),
        dict(id="s3", lines=[40, 45], hook="'RAISED PART OF<br>[THEIR SUBMARINE]'"),
        dict(id="s4", lines=[50, 59], hook="NEITHER CONFIRM<br>[NOR DENY]"),
    ],
)
