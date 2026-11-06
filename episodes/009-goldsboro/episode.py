# FILE 009 — One Switch: The Goldsboro Accident, 1961
# Format: see episodes/001-navy-videos/episode.py
# NOTE on clip timing: the 4K DVIDS clips were pre-trimmed and scaled to 1080p in /home/claude/src
# (dv1006838 from 112 s, dv943839 from 38 s, dv1010076 from 20 s, dv1015133 from 46 s, dv944524 from 14 s);
# the times below are relative to those trimmed files.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
H = "/home/claude/src/img/"
NARN = "DEPARTMENT OF DEFENSE, \"NARRATIVE SUMMARIES OF ACCIDENTS INVOLVING U.S. NUCLEAR WEAPONS 1950-1980\" (1981)"
NAR = "ACTUAL DOCUMENT · " + NARN
S_NAR = "SOURCE: " + NARN
S_NSA = "SOURCE: SANDIA CORP., SCDR 8-81 (FEB. 1961), AS SUMMARIZED BY THE NATIONAL SECURITY ARCHIVE (EBB 475, 2014)"
S_NARA = "SOURCE: NATIONAL ARCHIVES, \"BRUSH WITH CATASTROPHE\" (PIECES OF HISTORY, JAN. 22, 2021)"
S_JONES = "SOURCE: PARKER F. JONES, SANDIA, \"GOLDSBORO REVISITED\" (OCT. 22, 1969) · EXCERPT, RECREATED"

NIGHT = "B-ROLL · U.S. AIR FORCE B-52H NIGHT TAKEOFF, RAF FAIRFORD, ENGLAND, 2024 · NOT THE 1961 AIRCRAFT"
EU = "B-ROLL · U.S. AIR FORCE B-52H TAKEOFF, EUROPE, 2026 · NOT THE 1961 AIRCRAFT"
REF = "B-ROLL · AN AIR NATIONAL GUARD KC-135 REFUELS A B-52, OVER THE U.S. MIDWEST, 2026"
MOT = "B-ROLL · A B-52H AT MINOT AIR FORCE BASE, NORTH DAKOTA, 2026"
LOAD = "B-ROLL · AIRMEN LOAD CONVENTIONAL BOMBS INTO A B-52H, RAF FAIRFORD, ENGLAND, 2024 · NOT NUCLEAR WEAPONS"
NVG = "B-ROLL · NIGHT-VISION VIEW FROM A B-52 COCKPIT, NELLIS AIR FORCE BASE, NEVADA, 2012"
CKP = "B-ROLL · B-52 CREW IN THE COCKPIT, RED FLAG EXERCISE, NELLIS AIR FORCE BASE, NEVADA, 2012"
SJ = "B-ROLL · SEYMOUR JOHNSON AIR FORCE BASE, GOLDSBORO, NORTH CAROLINA, 2020"
PINES = "B-ROLL · PINE TREES AT SEYMOUR JOHNSON AIR FORCE BASE, NORTH CAROLINA, 2020 · NOT THE CRASH SITE"
H52 = "U.S. AIR FORCE PHOTO · AIRMEN LOAD A BOMB INTO A B-52, DYESS AFB, TEXAS, 1960s · NOT THE GOLDSBORO WEAPONS"
NB52 = "NASA PHOTO · THE NB-52A \"THE HIGH AND MIGHTY ONE\" CARRYING A NASA LIFTING-BODY RESEARCH PLANE, 1960s"

SEQ = [dict(n="01", t="Safing pins pulled", s="BY LANYARDS, AS THE PLANE BROKE UP"),
       dict(n="02", t="Power source freed", s="GENERATOR PINS PULLED"),
       dict(n="03", t="Parachute opened", s="TIMER STARTED"),
       dict(n="04", t="Timer ran", s="ACCORDING TO LATER ACCOUNTS"),
       dict(n="05", t="Arm/Safe switch", s="STILL ON SAFE · PREVENTED A NUCLEAR EXPLOSION")]

LINES = [
 # ---------------- COLD OPEN ----------------
 ("Just after midnight on January twenty-fourth, nineteen sixty-one, a B fifty-two bomber came apart in the sky over North Carolina.",
  [C("dv943839", 24.0, lab=NIGHT)], dict(tag=("WAYNE COUNTY, N.C.", "JANUARY 24, 1961"))),
 ("It was carrying two hydrogen bombs.",
  [I("h52load", kb="in", focus=[0.5, 0.45], lab=H52)], dict(slow=True)),
 ("One came down under its parachute and was found hanging in a tree. | The other hit a waterlogged field so hard that part of it was never recovered.",
  [C("dv150146", 44.0, lab=NVG), C("dv739519", 98.2, lab=PINES), I("nar_gb_bot", kb="in", focus=[0.5, 0.5], lab=NAR)], {}),
 ("Twenty years later, the Pentagon's own summary of the accident needed just three words for the outcome. | No explosion occurred.",
  [I("nar_gb", kb="in", focus=[0.5, 0.5], lab=NAR)], dict(slow=True)),
 ("But in nineteen sixty-nine, a safety engineer at Sandia, one of the laboratories behind America's nuclear weapons, wrote a very different sentence.",
  [C("dv944524", 30.0, lab=LOAD), C("dv1015133", 40.0, lab=MOT)], {}),
 ("One simple, dynamo-technology, low voltage switch stood between the United States and a major catastrophe.",
  [G("quote", q="One simple, dynamo-technology, {{low voltage switch stood between the United States and a major catastrophe!}}",
     who="Parker F. Jones", role="Sandia · \"Goldsboro Revisited\" · 1969", size=60, source=S_JONES)], dict(slow=True)),
 ("This is the file on Goldsboro. | Let's open it.",
  [G("intro", n="009")], dict(gap=0.2)),
 ("",
  [G("title", n="009", t="One Switch", size=170, sub="The Goldsboro Accident, 1961")], dict(gap=0.4)),

 # ---------------- I. AIRBORNE ALERT ----------------
 ("To understand that night, start with the job that bomber was doing.",
  [G("chapter", n="I", t="Airborne Alert")], {}),
 ("In those years, Strategic Air Command kept some of its B fifty-twos in the air around the clock, carrying nuclear weapons. | The Pentagon called it airborne alert.",
  [C("dv1006838", 22.0, lab=EU), C("dv1006838", 30.0, lab=EU)], {}),
 ("Years later, the Pentagon published summaries of thirty-two accidents involving U S nuclear weapons. | Most of the aircraft accidents on that list happened on ferry flights, or on Strategic Air Command airborne alert missions.",
  [I("nar_cover", kb="in", focus=[0.5, 0.5], lab=NAR)], {}),
 ("That meant real weapons, aloft day and night, often over American soil. | And it meant that sooner or later, one of those planes would crash.",
  [C("dv1010076", 4.0, lab=REF)], {}),
 ("The question was what a crash would do to the bombs.",
  [I("nb52", kb="in", focus=[0.6, 0.45], lab=NB52)], {}),
 ("In nineteen fifty-eight, documents from the Joint Chiefs of Staff called the risk of an accidental nuclear detonation of the newer sealed-pit weapons a negligible factor.",
  [G("doc", header="JOINT CHIEFS OF STAFF · MARCH 1958", title="On sealed-pit nuclear weapons",
     lines=["…a {{\"negligible factor.\"}}"],
     source="SOURCE: JCS RECORDS (RG 218), AS QUOTED BY THE NATIONAL SECURITY ARCHIVE · EXCERPT, RECREATED")], {}),
 ("That same year, a mishap at Sidi Slimane, in Morocco, raised a new worry inside the government. | What would happen as Western Europe filled up with American nuclear stockpiles?",
  [C("dv943839", 30.0, lab=NIGHT)], {}),
 ("In February nineteen fifty-nine, a Strategic Air Command letter described a point of balance, between safety on one side, and reliability and reaction time on the other.",
  [C("dv944524", 45.0, lab=LOAD)], {}),
 ("That same month, a Sandia study put it bluntly. | Safety, it said, was fundamentally a matter of playing percentages.",
  [G("quote", q="…fundamentally {{a matter of playing percentages.}}",
     who="Sandia Corporation", role="Weapon safety study · 1959", size=72, source="SOURCE: SANDIA CORP. (1959), AS QUOTED BY THE NATIONAL SECURITY ARCHIVE (EBB 475)")], {}),
 ("Its estimate for the risk of a spontaneous nuclear detonation, not counting human error, was one in a hundred million.",
  [G("stat", k="SANDIA SAFETY STUDY · 1959", a="1 IN 100,000,000", size=150, b="estimated risk of a spontaneous detonation, excluding human error",
     source="SOURCE: SANDIA CORP. (1959), AS SUMMARIZED BY THE NATIONAL SECURITY ARCHIVE (EBB 475)")], dict(gap=0.9, sil=True)),

 # ---------------- II. THE BREAKUP ----------------
 ("Then came January nineteen sixty-one.",
  [G("chapter", n="II", t="The Breakup")], {}),
 ("Late on January twenty-third, a B fifty-two G based at Seymour Johnson Air Force Base, near Goldsboro, North Carolina, was flying one of those missions. It was three days after John F Kennedy took office. | According to the National Archives, its call sign was Keep nineteen.",
  [C("dv1015133", 20.0, lab=MOT), C("dv943839", 10.0, lab=NIGHT)], {}),
 ("Eight men were aboard. The aircraft commander was Major Walter Tulloch.",
  [C("dv149961", 112.0, lab=CKP)], {}),
 ("During in-flight refueling, the tanker's crew spotted a problem. | Fuel was leaking from the bomber's right wing.",
  [C("dv1010076", 23.0, lab=REF), C("dv1010076", 33.0, lab=REF)], {}),
 ("According to the National Archives, the bomber lost more than five thousand four hundred gallons of fuel, about thirty-seven thousand pounds, in less than three minutes.",
  [C("dv149961", 179.0, lab=CKP)], {}),
 ("It was ordered to Seymour Johnson for an emergency landing.",
  [C("dv150146", 47.0, lab=NVG)], {}),
 ("It never got there. | The right wing failed, and the aircraft broke apart, somewhere between two thousand and ten thousand feet.",
  [I("nar_gb_top", kb="in", focus=[0.5, 0.55], lab=NAR)], dict(slow=True)),
 ("Major Tulloch ordered the crew to bail out. | According to the National Archives, one man climbed out through the top hatch.",
  [C("dv150146", 122.0, lab=NVG), C("dv943839", 32.0, lab=NIGHT)], {}),
 ("Five of the eight survived.",
  [I("nar_gb", kb="down", focus=[0.5, 0.62], lab=NAR)], {}),
 ("Three did not. The National Archives names them as Major Shelton, Major Richards, and Sergeant Barnish.",
  [G("stat", k="KEEP 19 · JANUARY 24, 1961", a="3", size=300, b="crewmen died", c="Maj. Shelton · Maj. Richards · Sgt. Barnish",
     source=S_NARA)], dict(slow=True)),
 ("In military language, an accident like this has a code name. | A Broken Arrow.",
  [C("dv943839", 44.0, lab=NIGHT)], dict(slow=True)),
 ("The wreckage was scattered across roughly two square miles of farmland near the community of Faro, about ten miles northeast of Seymour Johnson Air Force Base.",
  [G("map", kicker="JANUARY 24, 1961", title="Wayne County, North Carolina", bounds=[[-78.12, 35.30], [-77.72, 35.58]],
     points=[dict(ll=[-77.993, 35.385], name="Goldsboro", anchor="end"), dict(ll=[-77.962, 35.339], name="Seymour Johnson AFB", sub="BOMBER'S HOME BASE"),
             dict(ll=[-77.88, 35.50], name="Crash site", sub="NEAR FARO · APPROX."), dict(ll=[-77.876, 35.542], name="Eureka", anchor="end", sub="2012 STATE MARKER")],
     areas=[dict(ll=[-77.88, 35.50], r=60)], source="SOURCES: NATIONAL ARCHIVES (2021); N.C. DEPT. OF NATURAL AND CULTURAL RESOURCES; N.C. HIGHWAY MARKER F-70 · LOCATIONS APPROXIMATE")],
  dict(gap=0.9, sil=True, tag=("FARO, N.C.", "JANUARY 24, 1961"))),

 # ---------------- III. TWO BOMBS ----------------
 ("So what happened to the bombs?",
  [G("chapter", n="III", t="Two Bombs")], {}),
 ("They were Mark thirty-nine thermonuclear weapons. | Each, according to the National Archives, had a yield of three to four megatons. Roughly two hundred and fifty times the bomb dropped on Hiroshima.",
  [G("stat", k="MARK 39 · EACH BOMB", a="3-4 MEGATONS", size=170, b="about 250 times the Hiroshima bomb", c="two aboard", source=S_NARA)], {}),
 ("Each weighed at least six thousand five hundred pounds, and was about twelve feet long. | More than seven hundred were built, between nineteen fifty-seven and nineteen fifty-nine.",
  [I("h52load", kb="out", focus=[0.5, 0.45], lab=H52)], {}),
 ("As the bomber broke up, both of them separated from the aircraft.",
  [I("nar_gb_top", kb="down", focus=[0.5, 0.6], lab=NAR)], {}),
 ("A month later, two Sandia engineers delivered a detailed analysis of what had happened inside them. | Their report even got the town wrong. Its title says Greensboro.",
  [G("doc", header="SANDIA CORPORATION · SCDR 8-81 · FEBRUARY 1961", title="Report title",
     lines=["Analysis of the Safety Aspects of the MK 39 MOD 2 Bombs Involved in B-52G Crash Near {{Greensboro,}} North Carolina"],
     source="SOURCE: NATIONAL SECURITY ARCHIVE, EBB 475 (2014) · TITLE, RECREATED")], {}),
 ("Both bombs, they found, had been set to safe. | But the crash itself started the fuzing sequence on both of them.",
  [C("dv944524", 95.0, lab=LOAD)], {}),
 ("Take the first bomb. | As the plane broke apart, lanyards pulled out its safing pins, and the crash yanked the pins on the generator that supplied its electric power.",
  [G("list", kicker="BOMB ONE · THE ARMING SEQUENCE", title="What the crash set off", items=SEQ, source="SOURCES: SANDIA SCDR 8-81 AS SUMMARIZED BY THE NATIONAL SECURITY ARCHIVE (EBB 475, 2014); DOD (1981) · STEP 04: LATER ACCOUNTS")], {}),
 ("Its parachute opened. And according to later accounts, its timer ran.",
  [C("dv150146", 126.0, lab=NVG)], {}),
 ("What remained was the Arm-Safe switch, controlled by the crew. | It was still set to safe. And that, Sandia's analysts found, prevented a nuclear explosion.",
  [G("stat", k="BOMB ONE · THE LAST STEP", a="SAFE", size=280, b="the Arm/Safe switch was still on safe", c="it \"worked exactly as it was supposed to\"", source=S_NSA)], dict(slow=True)),
 ("That bomb drifted down under its parachute, and was found hanging in a tree, essentially undamaged.",
  [C("dv739519", 98.2, lab=PINES), C("dv1006838", 24.0, lab=EU)], {}),
 ("The second bomb's parachute never opened. | It fell free, hit the waterlogged ground at high speed, and broke apart.",
  [I("nar_gb_bot", kb="in", focus=[0.5, 0.3], lab=NAR)], {}),
 ("Because its parachute never opened, its timer never started its high-voltage battery. | But when its Arm-Safe switch was dug out of the mud, the indicator read armed.",
  [C("dv943839", 26.0, lab=NIGHT)], {}),
 ("Sandia's analysts concluded that the impact had spun the indicator, and damaged the switch's contacts. | That bomb, they found, was not close to going off.",
  [C("dv1015133", 4.0, lab=MOT)], {}),
 ("The close call was the bomb in the tree.",
  [I("nar_gb", kb="in", focus=[0.5, 0.42], lab=NAR)], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE MUD ----------------
 ("Then came the digging.",
  [G("chapter", n="IV", t="The Mud")], {}),
 ("According to the National Archives, over eight days the recovery team dug out much of the buried bomb, including its ninety-two detonators. | Its nuclear pit came out on January twenty-ninth.",
  [C("dv944524", 75.0, lab=LOAD), C("dv1015133", 34.0, lab=MOT)], {}),
 ("But the thermonuclear stage, the secondary, was never found.",
  [I("nar_gb_bot", kb="down", focus=[0.5, 0.55], lab=NAR)], dict(slow=True)),
 ("The Pentagon's summary says the excavation went down fifty feet in the waterlogged farmland. | A portion of the weapon, containing uranium, could not be recovered.",
  [I("nar_gb_bot", kb="in", focus=[0.5, 0.62], lab=NAR)], {}),
 ("So the Air Force bought an easement. To dig there, you need permission.",
  [I("nar_gb_bot", kb="hold", focus=[0.5, 0.75], lab=NAR)], {}),
 ("And the summary adds a final line. | There is no detectable radiation, and no hazard in the area.",
  [I("nar_gb_bot", kb="in", focus=[0.5, 0.82], lab=NAR)], {}),
 ("There was also the question of what to tell the public. | The Pentagon's policy, its summary explains, is normally to neither confirm nor deny the presence of nuclear weapons at any specific place.",
  [I("nar_policy", kb="in", focus=[0.5, 0.4], lab=NAR)], {}),
 ("After an accident, it says, their presence may or may not be divulged at the time, depending on the possibility of public hazard or alarm.",
  [I("nar_policy", kb="down", focus=[0.5, 0.65], lab=NAR)], dict(gap=0.9, sil=True)),

 # ---------------- V. ONE SWITCH ----------------
 ("So how close did it come?",
  [G("chapter", n="V", t="One Switch")], {}),
 ("Sandia's analysis pointed to the Arm-Safe switch on the first bomb. | In the National Security Archive's summary of that report, the switch worked exactly as it was supposed to, and prevented a nuclear explosion.",
  [C("dv150146", 52.0, lab=NVG), C("dv1006838", 50.0, lab=EU)], {}),
 ("The analysts had a second concern. Those lanyards were already scheduled to be removed, under a modification called ALT one ninety-seven. | They urged that it be done quickly, across the whole Mark fifteen and thirty-nine family used on airborne alert.",
  [C("dv944524", 60.0, lab=LOAD), C("dv1010076", 28.0, lab=REF)], {}),
 ("Defense Secretary Robert McNamara later described the accident this way.",
  [C("dv1006838", 26.0, lab=EU)], {}),
 ("By the slightest margin of chance, literally the failure of two wires to cross, a nuclear explosion was averted.",
  [G("quote", q="…by the slightest margin of chance, {{literally the failure of two wires to cross,}} a nuclear explosion was averted.",
     who="Robert S. McNamara", role="Secretary of Defense", size=60, source="SOURCE: AS QUOTED BY THE NATIONAL SECURITY ARCHIVE, EBB 475 (2014)")], dict(slow=True)),
 ("In nineteen sixty-nine, Parker F Jones, who supervised Sandia's nuclear weapons safety department, went back over the accident in a memo he called Goldsboro Revisited. | He was responding to a book by the physicist Ralph Lapp, which had described the crash.",
  [C("dv1015133", 30.0, lab=MOT), C("dv943839", 18.0, lab=NIGHT)], {}),
 ("His verdict on the weapon was blunt. | The Mark thirty-nine Mod two bomb did not possess adequate safety for the airborne alert role in the B fifty-two.",
  [G("doc", header="SANDIA LABORATORIES · OCTOBER 22, 1969", title="Goldsboro Revisited",
     lines=["The MK 39 Mod 2 bomb {{did not possess adequate safety}} for the airborne alert role in the B-52.",
            "One simple, dynamo-technology, low voltage switch stood between the United States and a major catastrophe!"],
     source=S_JONES)], {}),
 ("That memo was declassified decades later. | In twenty thirteen, the journalist Eric Schlosser, who had obtained it while researching a book, shared it with The Guardian, which published it.",
  [C("dv943839", 40.0, lab=NIGHT), C("dv1006838", 62.0, lab=EU)], {}),
 ("Not everyone reads the file the same way. | Official statements, the National Archives notes, have said there was no danger of the bombs exploding. | Others, it adds, indicate that most of the steps needed for a detonation did occur.",
  [G("quote", q="Official statements indicate that there was {{no danger of the bombs exploding…}}",
     who="National Archives", role="\"Brush with Catastrophe\" · 2021", size=62, source=S_NARA)], {}),
 ("And the Pentagon's nineteen eighty-one summary says there has never been even a partial inadvertent U S nuclear detonation.",
  [I("nar_never", kb="in", focus=[0.5, 0.5], lab=NAR)], {}),
 ("Both can be true. The bomb did not go off. | And according to Sandia's own analysts, one switch was the safeguard that held.",
  [C("dv1006838", 34.0, lab=EU)], dict(gap=0.9, sil=True)),

 # ---------------- VI. AFTER GOLDSBORO ----------------
 ("Goldsboro was not the last accident.",
  [G("chapter", n="VI", t="After Goldsboro")], {}),
 ("In January nineteen sixty-six, a B fifty-two collided with a tanker over Palomares, Spain. Seven crew members died. | Conventional explosives in some of its weapons detonated, scattering plutonium. One bomb was lost at sea for nearly three months, until it was recovered.",
  [C("dv1010076", 12.0, lab=REF), C("dv1006838", 4.0, lab=EU)], {}),
 ("In January nineteen sixty-eight, a B fifty-two crashed near Thule, Greenland. | Its weapons broke up and scattered radioactive debris. One crew member died.",
  [C("dv1015133", 0.5, lab=MOT)], {}),
 ("Those two, the Pentagon's summary says, were the only accidents that resulted in a widespread dispersal of nuclear materials.",
  [I("nar_never", kb="down", focus=[0.5, 0.7], lab=NAR)], {}),
 ("That year, airborne alert ended. The Pentagon later listed its reasons. The accidents, particularly Palomares and Thule. The rising cost. And a missile force that could take over part of the bombers' job.",
  [I("nar_alert", kb="in", focus=[0.5, 0.5], lab=NAR)], {}),
 ("The standards tightened too. A policy review in the late nineteen sixties set a goal. The risk of an accidental nuclear detonation should be no more than one in a million per year, for an arsenal of ten thousand weapons or more.",
  [G("stat", k="SAFETY STANDARD · LATE 1960s", a="1 IN 1,000,000", size=150, b="maximum annual risk of an accidental detonation", c="for a stockpile of 10,000 weapons or more",
     source="SOURCE: NATIONAL SECURITY ARCHIVE, EBB 475 (2014)")], {}),
 ("Even so, in nineteen eighty-seven, a Sandia history of the safety program concluded that the United States could not claim, in an absolute sense, that it was doing everything possible to keep weapons safe, while they stayed fully assembled on combat-ready systems.",
  [G("timeline", kicker="THE PAPER TRAIL", title="More than half a century of the Goldsboro file", active=2,
     events=[dict(y="1958", t="\"Negligible factor\""), dict(y="1959", t="\"Playing percentages\""), dict(y="FEB 1961", t="Sandia analysis"),
             dict(y="1969", t="\"Goldsboro Revisited\""), dict(y="1981", t="DoD summary"), dict(y="1987", t="Sandia safety history"),
             dict(y="2013-14", t="Memo and report published")],
     source="SOURCES: NATIONAL SECURITY ARCHIVE (EBB 475); DOD (1981); THE GUARDIAN (2013)")], dict(gap=0.9, sil=True)),

 # ---------------- VII. THE MARKER ----------------
 ("Today, near the crash site, there is a sign.",
  [G("chapter", n="VII", t="The Marker")], {}),
 ("In twenty twelve, North Carolina put up a state historical marker in Eureka, about three miles north of where the bomber came down.",
  [C("dv1015133", 50.0, lab=MOT)], dict(tag=("EUREKA, N.C.", "MARKER F-70, 2012"))),
 ("It reads, in full. | B fifty-two transporting two nuclear bombs crashed, January nineteen sixty-one. Widespread disaster averted. Three crewmen died, three miles south.",
  [G("doc", header="NORTH CAROLINA HIGHWAY HISTORICAL MARKER F-70 · 2012", title="Nuclear Mishap",
     lines=["B-52 transporting two nuclear bombs crashed, Jan. 1961.", "{{Widespread disaster averted;}} three crewmen died 3 mi. S."],
     source="SOURCE: N.C. OFFICE OF ARCHIVES AND HISTORY (VIA THE HISTORICAL MARKER DATABASE) · TEXT, RECREATED")], dict(slow=True)),
 ("Widespread disaster averted. | The files explain how. A switch set to safe, in a bomb hanging from a tree.",
  [C("dv739519", 98.2, lab=PINES), C("dv943839", 40.0, lab=NIGHT)], {}),
 ("Three crewmen died. Two bombs fell. | One was lifted out of a tree. The other, in part, is still in the ground.",
  [I("nar_gb_bot", kb="in", focus=[0.5, 0.6], lab=NAR)], dict(slow=True)),
 ("Every secret has a release date. | For the full story of Goldsboro, it came more than fifty years after the crash.",
  [I("nar_gb", kb="out", focus=[0.5, 0.5], lab=NAR)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments.",
  [C("dv1015133", 44.0, lab=MOT)], {}),
 ("Next time: the C I A's own list of everything it had done that might be illegal. The Family Jewels.",
  [G("end", n="009", next="The Family Jewels")], dict(gap=2.5)),
]

PRON = [("Goldsboro", "Golds-burrow"), ("Greensboro", "Greens-burrow"), ("Sandia", "San-dee-uh"), ("Thule", "Too-lee"),
        ("Tulloch", "Tull-uck"), ("Palomares", "Pa-lo-MAR-es"), ("Faro", "Fair-oh"), ("Barnish", "Bar-nish"), ("Sidi Slimane", "Sidi Slee-mahn"), ("Lapp", "Lap"),
        ("fuzing", "fuzing"), ("Arm-Safe", "arm safe"), ("aloft", "a-loft"), ("Schlosser", "Shlosser"),
        ("ALT one ninety-seven", "alt one ninety-seven"), ("Mod two", "mod two"), ("C I A's", "C I A's")]

DISPLAY = [
 ("B fifty-two G", "B-52G"), ("B fifty-twos", "B-52s"), ("B fifty-two", "B-52"),
 ("Mark thirty-nine Mod two", "MK 39 Mod 2"), ("Mark fifteen and thirty-nine", "Mark 15 and 39"), ("Mark thirty-nine", "Mark 39"),
 ("Arm-Safe", "Arm/Safe"), ("ALT one ninety-seven", "ALT 197"), ("Parker F Jones", "Parker F. Jones"), ("John F Kennedy", "John F. Kennedy"), ("thirty-two accidents", "32 accidents"), ("six thousand five hundred pounds", "6,500 pounds"), ("seven hundred", "700"), ("twelve feet", "12 feet"), ("C I A's", "CIA's"),
 ("U S nuclear", "U.S. nuclear"), ("Keep nineteen", "Keep 19"),
 ("January twenty-fourth", "January 24"), ("January twenty-third", "January 23"), ("January twenty-ninth", "January 29"),
 ("nineteen sixty-one", "1961"), ("nineteen sixty-nine", "1969"), ("nineteen fifty-eight", "1958"), ("nineteen fifty-nine", "1959"), ("nineteen fifty-seven", "1957"),
 ("nineteen sixty-six", "1966"), ("nineteen sixty-eight", "1968"), ("nineteen eighty-one", "1981"), ("nineteen eighty-seven", "1987"),
 ("late nineteen sixties", "late 1960s"), ("twenty thirteen", "2013"), ("twenty twelve", "2012"),
 ("five thousand four hundred gallons", "5,400 gallons"), ("thirty-seven thousand pounds", "37,000 pounds"),
 ("two thousand and ten thousand feet", "2,000 and 10,000 feet"), ("two hundred and fifty times", "250 times"),
 ("ninety-two detonators", "92 detonators"), ("fifty feet", "50 feet"), ("ten thousand weapons", "10,000 weapons"),
 ("one in a hundred million", "one in 100 million"), ("three to four megatons", "three to four megatons"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="009", title="One Switch: The Goldsboro Accident, 1961",
    imgs=dict({k: D + k + ".jpg" for k in ["nar_gb", "nar_gb_top", "nar_gb_bot", "nar_cover", "nar_never", "nar_alert", "nar_policy"]},
              h52load=H + "h52_2816773.jpg", nb52=H + "nb52_833063.jpg"),
    credit="Documents: Department of Defense (1981). B-roll: U.S. Air Force via DVIDS (2012-2026); historical photos: U.S. Air Force, NASA.\\NModern b-roll does not show the 1961 aircraft or its weapons. No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[20, 29], hook="A B-52 BROKE APART<br>[OVER NORTH CAROLINA]"),
        dict(id="s2", lines=[35, 44], hook="TWO H-BOMBS FELL.<br>[ONE SWITCH HELD]"),
        dict(id="s3", lines=[45, 52], hook="PART OF IT WAS<br>[NEVER RECOVERED]"),
        dict(id="s4", lines=[56, 63], hook="'ONE SIMPLE,<br>[LOW VOLTAGE SWITCH]'"),
    ],
)
