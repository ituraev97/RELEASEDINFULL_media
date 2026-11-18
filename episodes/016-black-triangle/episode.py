# FILE 016 — The Silent Black Triangle Federal Agents Couldn't Identify
# Fresh topic: the seventh PURSUE release of UAP files (Department of War, war.gov/UFO, Oct. 23, 2026).
# Main documents (unmodified mirror: archive.org/details/pursue-uap-documents-2026, folder Release_07):
#   DOW-UAP-D176 AARO Memorandum for Record, triangular UAP (2026) · FBI-UAP-D043 FD-302 with co-signed statement + 9 images (2026)
#   DOW-UAP-D179/D178/D177 Catalina Island 1952/1953/1955 · DOW-UAP-D164 Indiana 1954 · DOW-UAP-D155 Saudi Arabia 1957 (B-52)
#   DOW-UAP-D163 Sweden 1953 · DOW-UAP-D160 Morocco 1953 · DOW-UAP-D161/D162 Alaska 1953
#   EOP-UAP-D002 memo on recovery of foreign materiel (May 29, 1963) · USG-UAP-D002 space-fragment correspondence (1962-64)
#   DOW-UAP-D174 Utah Ranch Investigation Report (BAASS, April 2010)
# LEGAL: no living private person is named. Witnesses in 1950s files are not named in narration (several were minors); the
#   Sweden crops carry our black bars over the pilot/crew names. Officials' names visible on crops: Morris, Ballew, Maddox, Robinson. Named people:
#   historical officials only (Lt. Col. J.H. Morris, 1957; Arnold Frutkin, E.C. Welsh, 1963) and the contractor name BAASS.
#   Sean Parnell is named as the Pentagon spokesman (public official, in role). No photos of people.
# COPYRIGHT: only U.S. government records/images and DVIDS public-domain b-roll; contractor/lab documents shown only as short
#   text excerpts for reporting; no witness drawings, no contractor photos.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
F = "/home/claude/src/img/"

A_ = "ACTUAL DOCUMENT · AARO MEMORANDUM FOR RECORD, TRIANGULAR UAP (2026) · DOW-UAP-D176 · P. "
FB = "ACTUAL DOCUMENT · FBI FD-302 AND CO-SIGNED STATEMENT (2026) · FBI-UAP-D043 · P. "
FI = "IMAGE {} OF 9 ATTACHED TO THE FBI REPORT (2026), AS RELEASED · A DEPICTION, NOT A PHOTO OF THE OBJECT"
SA = "ACTUAL DOCUMENT · AIR INTELLIGENCE INFORMATION REPORT, SAUDI ARABIA (JAN. 1957) · DOW-UAP-D155 · P. "
IN = "ACTUAL DOCUMENT · REPORT, ATTERBURY AFB, INDIANA (JAN. 13, 1954) · DOW-UAP-D164 · P. 1"
C52 = "ACTUAL DOCUMENT · AIR INTELLIGENCE INFORMATION REPORT, SANTA CATALINA (AUG. 28, 1952) · DOW-UAP-D179 · P. 2"
C55 = "ACTUAL DOCUMENT · PROJECT 10073 RECORD CARD, CATALINA ISLE (MARCH 15, 1955) · DOW-UAP-D177 · P. 1"
SW = "ACTUAL DOCUMENT · AIR ATTACHÉ REPORT, STOCKHOLM (JAN. 13, 1954) · DOW-UAP-D163 · P. 2 · BLACK BARS: NAMES WITHHELD BY RELEASED IN FULL"
MO = "ACTUAL DOCUMENT · AIR INTELLIGENCE INFORMATION REPORT, FRENCH MOROCCO (DEC. 1953) · DOW-UAP-D160 · P. 1"
AK = "ACTUAL DOCUMENT · AIR INTELLIGENCE INFORMATION REPORT, GAMBELL, ALASKA (DEC. 8, 1953) · DOW-UAP-D162 · P. 1"
EOP = "ACTUAL DOCUMENT · MEMORANDUM FOR DR. WELSH, \"FRAGMENTS\" (MAY 29, 1963) · EOP-UAP-D002"
UR = "ACTUAL DOCUMENT · BAASS, UTAH RANCH INVESTIGATION REPORT (APRIL 2010) · DOW-UAP-D174 · PDF P. "

MW = "B-ROLL · DUSK OVER THE SAN GABRIEL MOUNTAINS FROM MT. WILSON, CALIFORNIA, 2026 · NOT THE SIGHTING SITE"
B52T = "B-ROLL · A B-52 STRATOFORTRESS TAKES OFF, 2026 · NOT THE 1957 AIRCRAFT"
B52G = "B-ROLL · A B-52 STRATOFORTRESS ON THE GROUND, 2026 · NOT THE 1957 AIRCRAFT"
B52R = "B-ROLL · A B-52 REFUELS FROM A KC-135 TANKER, 2026 · NOT THE 1957 AIRCRAFT"
C47 = "B-ROLL · A C-47, THE MILITARY VERSION OF THE DC-3, TAKES OFF, 2024 · NOT THE 1953 AIRCRAFT"
CAT = "B-ROLL · SANTA CATALINA ISLAND, CALIFORNIA, 2019"
LAB = "B-ROLL · ARMED FORCES DNA IDENTIFICATION LABORATORY, 2015 · NOT THE LAB USED IN 2010"
THM = "B-ROLL · A THERMAL IMAGING CAMERA, 2020 · NOT THE AGENTS' EQUIPMENT"
MAUI = "B-ROLL · MAUI SPACE SURVEILLANCE COMPLEX, HAWAII, 2017"
GC = "B-ROLL · A C-17 REFUELS OVER THE GRAND CANYON, ARIZONA, 2021"
GORGE = "B-ROLL · CANYON LAKE GORGE, TEXAS, 2026 · NOT THE SIGHTING SITE"
CAP = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C., 2012"

S_P = "SOURCE: DEPARTMENT OF WAR, PURSUE RELEASE 07 (OCT. 23, 2026), 28 FILES; EARTHSKY; THE NATIONAL DESK (OCT. 2026)"
S_M = "SOURCE: AARO MEMORANDUM FOR RECORD (2026), DOW-UAP-D176"
S_F = "SOURCE: FBI FD-302 (2026), FBI-UAP-D043"
S_R = "SOURCE: BAASS UTAH RANCH INVESTIGATION REPORT (2010), DOW-UAP-D174"

LINES = [
 # ---------------- COLD OPEN (image sequence) ----------------
 ("Two federal agents watched a matte-black triangle rise over a ridge in total silence, | hover, | and dive into a canyon at what they estimated was fighter-jet speed.",
  [I("fbi4", kb="in", focus=[0.6, 0.33], lab=FI.format(4)), I("fbi5", kb="in", focus=[0.66, 0.36], lab=FI.format(5)), I("fbi8", kb="in", focus=[0.48, 0.55], lab=FI.format(8))],
  dict(tag=("LOCATION REDACTED", "2026"))),
 ("A search of the canyon the next morning | found no wreckage at all.",
  [I("m_survey", kb="in", focus=[0.5, 0.5], lab=A_ + "3")], {}),
 ("That is not a story from the nineteen fifties. | It happened in twenty twenty-six, | and on October twenty-third, the Pentagon published the government's own reports about it.",
  [I("m_head", kb="in", focus=[0.5, 0.4], lab=A_ + "1")], dict(tag=("WAR.GOV/UFO · RELEASE 07", "OCTOBER 23, 2026"))),
 ("There are two of them: one from the Pentagon's U F O office, and one from the F B I. | And they do not tell the same story.",
  [I("f_head", kb="in", focus=[0.5, 0.4], lab=FB + "1")], {}),
 ("So what did those agents see? | And why did the government put it in the same release as a nineteen fifty-seven bomber, | a Cold War memo about falling space junk, | and a lab test on hair from a fence where a witness said a Skinwalker had run?",
  [C("dv996969s", 2.0, lab=MW)], dict(slow=True)),
 ("Let's open the file.",
  [G("intro", n="016")], dict(gap=0.2)),
 ("",
  [G("title", n="016", t="THE BLACK TRIANGLE", size=150, sub="What the Seventh UFO Release Actually Says")], dict(gap=0.4)),

 # ---------------- I. THE RIDGE ----------------
 ("Start with the setting.",
  [G("chapter", n="I", t="The Ridge")], {}),
 ("The date is blacked out. So is the place. | The memo, written by the All-domain Anomaly Resolution Office, known as Arrow, says only this: | twenty twenty-six, eight twenty-three in the evening, local time.",
  [I("m_shape", kb="in", focus=[0.3, 0.45], lab=A_ + "1")], {}),
 ("Two federal law enforcement agents were on a hilltop, at what the memo calls the primary observation post, | doing what it calls routine observation support.",
  [I("m_post", kb="in", focus=[0.5, 0.5], lab=A_ + "2")], {}),
 ("The sun had just gone down. | The memo describes a residual sunset gradient behind the western ridge lines, | while the valleys below were falling into shadow.",
  [C("dv996969s", 26.0, lab=MW), C("dv996969s", 56.0, lab=MW)], {}),
 ("Their main optical gear and their tripod-mounted sensors were pointed east. | The thing came from the west.",
  [I("m_post", kb="down", focus=[0.5, 0.6], lab=A_ + "2")], {}),
 ("A third witness, at a second post, was scanning west with long-range thermal equipment, | picked up an object moving over the ridge line, | and called it out on the radio.",
  [I("m_call", kb="in", focus=[0.5, 0.35], lab=A_ + "2"), C("dv754130", 2.0, lab=THM)], {}),
 ("The two agents immediately moved across the peak to get a view to the west. | The tripod-mounted thermal system could not be moved quickly, so it stayed behind. | One agent had binoculars and a handheld thermal monocular.",
  [I("m_call", kb="down", focus=[0.5, 0.65], lab=A_ + "2")], {}),
 ("He saw it with his own eyes first, | a dark shape against the last light in the western sky.",
  [I("fbi4", kb="in", focus=[0.62, 0.32], lab=FI.format(4))], dict(gap=0.9, sil=True)),

 # ---------------- II. THIRTY SECONDS ----------------
 ("By the memo's account, what happened next lasted about half a minute. | The memo splits it into three phases.",
  [G("chapter", n="II", t="Thirty Seconds")], {}),
 ("Phase one. | The object was climbing straight up over the ridge, slowly and perfectly level. | No tilt, no sway, no wobble. | About ten seconds.",
  [I("m_ph1", kb="in", focus=[0.5, 0.45], lab=A_ + "2"), I("fbi2", kb="in", focus=[0.55, 0.4], lab=FI.format(2))], {}),
 ("It was matte black and did not reflect light. | The memo lists everything the agents did not see: | no rotors, no rivets, no panels, no windows, no canopy, no exhaust.",
  [I("m_silent", kb="in", focus=[0.5, 0.5], lab=A_ + "2")], {}),
 ("Its size, as the agents estimated it: | a wingspan of thirteen to fifteen feet, | six to nine feet long, | and only one to two feet thick.",
  [G("stat", k="AS ESTIMATED BY THE WITNESSES", a="13-15 FT", size=230, b="wingspan · 6-9 ft long · 1-2 ft thick",
     c="matte black, nonreflective, \"featureless\"", source=S_M)], {}),
 ("By their terrain estimates, it was somewhere between one point four and three point two miles away.",
  [I("m_ph1", kb="down", focus=[0.5, 0.75], lab=A_ + "2")], {}),
 ("Phase two. | About two to three hundred feet above the ridge, it stopped climbing, instantly, | and hovered. | For about twenty seconds it held still: no drift, no oscillation.",
  [I("m_ph2", kb="in", focus=[0.5, 0.45], lab=A_ + "2"), I("fbi5", kb="in", focus=[0.66, 0.36], lab=FI.format(5))], {}),
 ("Through the thermal monocular, the whole airframe showed one even temperature. | No hot spots, no engine heat, no exhaust plume.",
  [C("dv754130", 12.0, lab=THM), I("m_silent", kb="down", focus=[0.5, 0.3], lab=A_ + "2")], {}),
 ("Phase three. | It went from hovering straight into high-speed horizontal flight, with no visible build-up of speed, | banked, | and dropped into a canyon, hugging the terrain, | in a way the memo compares to low-altitude terrain-masking flight.",
  [I("m_ph3b", kb="in", focus=[0.5, 0.4], lab=A_ + "3"), I("fbi7", kb="in", focus=[0.4, 0.45], lab=FI.format(7)), I("fbi9", kb="in", focus=[0.6, 0.6], lab=FI.format(9))], {}),
 ("That last phase lasted two to three seconds. | The agents compared its speed to a fighter jet. | But the memo is careful to add: | no instrumented speed measurement was obtained.",
  [I("m_ph3a", kb="in", focus=[0.5, 0.6], lab=A_ + "3")], {}),
 ("The infrared lock was lost because the object accelerated out of the monocular's narrow field of view. | And through all of it, the memo says, there was absolute acoustic silence.",
  [I("m_survey", kb="in", focus=[0.5, 0.35], lab=A_ + "3")], dict(slow=True)),
 ("The F B I file includes nine images of this. | They are not photographs of the object. | They show the same dusk landscape, with a small black shape placed in a different spot in each one, | rising, | hovering, | and dropping toward the canyon.",
  [I("fbi1", kb="in", focus=[0.6, 0.4], lab=FI.format(1)), I("fbi4", kb="in", focus=[0.6, 0.32], lab=FI.format(4)),
   I("fbi6", kb="in", focus=[0.65, 0.4], lab=FI.format(6)), I("fbi9", kb="in", focus=[0.6, 0.6], lab=FI.format(9))], dict(gap=0.9, sil=True)),

 # ---------------- III. THE OTHER STATEMENT ----------------
 ("But there is a second account of the same evening.",
  [G("chapter", n="III", t="The Other Statement")], {}),
 ("It is an F B I form called an F D three-oh-two. | Attached to it is a written statement co-signed by two agents, | quoted word for word.",
  [I("f_head", kb="in", focus=[0.5, 0.6], lab=FB + "1")], {}),
 ("In their words, they almost immediately observed a substantial, nonreflective, dark black triangular object, | most resembling a delta wing drone.",
  [I("f_obj", kb="in", focus=[0.5, 0.4], lab=FB + "1")], {}),
 ("Their wingspan estimate is broader: nine to fifteen feet. | Through the thermal device, they wrote, it appeared hotter than ambient temperature, | with a completely consistent thermal signature across the entire airframe, and no visible exhaust gases.",
  [I("f_obj", kb="down", focus=[0.5, 0.65], lab=FB + "1")], {}),
 ("The ridge, they wrote, was about three point two miles west. | The object climbed to about two hundred feet above it, | then moved into horizontal flight at a very significant velocity, approaching their position, | and descended to the southeast.",
  [I("f_ridge", kb="in", focus=[0.5, 0.5], lab=FB + "1"), I("f_end", kb="in", focus=[0.5, 0.3], lab=FB + "2")], {}),
 ("They lost sight of it about one and a half miles away. | Even the clock is different: the F B I statement says about seven twenty-three in the evening; the memo says eight twenty-three. | And here is the biggest difference.",
  [I("f_end", kb="in", focus=[0.5, 0.5], lab=FB + "2")], {}),
 ("The F B I statement says: | the total duration of the sighting was approximately three seconds.",
  [I("f_end", kb="down", focus=[0.5, 0.55], lab=FB + "2")], dict(slow=True)),
 ("The Pentagon memo describes about ten seconds of climbing, | twenty seconds of hovering, | and two to three seconds of flight. | Roughly half a minute.",
  [G("list", kicker="SAME EVENING · TWO OFFICIAL RECORDS", title="Where the accounts differ", items=[
      dict(n="AARO", t="Climb ~10 s · hover ~20 s · dash 2-3 s", s="13-15 ft wingspan"),
      dict(n="FBI", t="\"approximately three seconds\" in total", s="9-15 ft wingspan"),
      dict(n="AARO", t="\"unidentified craft\"", s="what it was called"),
      dict(n="FBI", t="\"most resembling a delta wing drone\"", s="what it was called")], source=S_M + "; " + S_F)], {}),
 ("The documents do not explain the gap. | And the F B I statement ends with one more line: | neither agent detected any auditory output from the unmanned aerial system.",
  [I("f_end", kb="in", focus=[0.5, 0.75], lab=FB + "2")], {}),
 ("Unmanned aerial system. | A drone. | That is the agents' own description. | It is not a finding. | Nobody, in either document, says what it was.",
  [I("fbi5", kb="in", focus=[0.66, 0.36], lab=FI.format(5))], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE CANYON ----------------
 ("Which brings us back to the canyon.",
  [G("chapter", n="IV", t="The Canyon")], {}),
 ("No impact, no smoke, no dust, the memo says. | And a ground survey of the canyon the next morning found no wreckage, no ground scarring, and no damage to the plants.",
  [I("m_survey", kb="down", focus=[0.5, 0.7], lab=A_ + "3"), C("dv1021908", 16.0, lab=GORGE)], {}),
 ("Then comes a note from the person who wrote the memo. | Both agents, it says, have extensive experience working with drones, alongside government agencies and academic studies, | and they regularly see ordinary aircraft around that site.",
  [I("m_note", kb="in", focus=[0.5, 0.35], lab=A_ + "3")], {}),
 ("On that hilltop, they told the interviewers, | even a small drone, a quadcopter motor or a helicopter one point four miles away would have been clearly audible.",
  [I("m_note", kb="down", focus=[0.5, 0.6], lab=A_ + "3")], {}),
 ("They judged its size against the trees on the ridge behind it.",
  [C("dv996969s", 32.0, lab=MW)], {}),
 ("And the memo reports none of the strange extras that fill a lot of U F O stories. | No nausea, no headaches, no lost time. | No odd smells. | No interference with any of their equipment.",
  [I("m_noeff", kb="in", focus=[0.5, 0.5], lab=A_ + "3")], {}),
 ("But the very first paragraph carries a warning that matters as much as anything after it. | This report, it says, reflects the reporter's interpretation at the time of the event, | and its descriptions should not be taken as conclusive about the object's features or performance.",
  [I("m_overview", kb="in", focus=[0.5, 0.5], lab=A_ + "1")], dict(slow=True)),
 ("Two trained observers. | Two documents. | One object nobody could name. | And no video of it in the release.",
  [C("dv996969s", 44.0, lab=MW)], dict(gap=0.9, sil=True)),

 # ---------------- V. SAME WORDS ----------------
 ("Here is the strange part of this release. | The same ideas keep turning up, more than seventy years earlier.",
  [G("chapter", n="V", t="Same Words, 1952")], {}),
 ("The seventh batch is not only about twenty twenty-six. | About half of its twenty-eight files are old Air Force reports, from California to Sweden, Morocco, Alaska and Saudi Arabia.",
  [G("map", kicker="PURSUE RELEASE 07", title="Where the files come from", bounds=[[-175, 15], [55, 70]], points=[
      dict(ll=[-118.42, 33.39], name="Catalina 1952-55", anchor="end"), dict(ll=[-85.89, 38.96], name="Indiana 1954"),
      dict(ll=[-171.7, 63.78], name="Alaska 1953"), dict(ll=[13.77, 56.16], name="Sweden 1953", anchor="end"),
      dict(ll=[-6.8, 34.0], name="Morocco 1953", anchor="end"), dict(ll=[47.0, 27.0], name="Saudi Arabia 1957", anchor="end"),
      dict(ll=[-110.0, 40.3], name="Utah 2010", sub="RANCH REPORT")], source=S_P)], {}),
 ("June twenty-fifth, nineteen fifty-two. Santa Catalina Island, off Southern California. | Three Boy Scouts from a summer camp are hiking up a mountain.",
  [C("dv676629", 9.8, lab=CAT), I("cat52_head", kb="in", focus=[0.5, 0.5], lab=C52)], dict(tag=("SANTA CATALINA ISLAND, CALIFORNIA", "JUNE 25, 1952"))),
 ("The Air Force report says they saw a silver object, faster than a conventional jet. | There was no sound observed. | It made one climbing turn, | and then came what the report calls its disappearance by disintegration.",
  [I("cat52_sum", kb="in", focus=[0.5, 0.6], lab=C52)], {}),
 ("The officer who filed it added a blunt note. | No estimate of reliability could be attempted, | and the experience of the observers was probably meager at best.",
  [I("cat52_rel", kb="in", focus=[0.5, 0.6], lab=C52)], {}),
 ("Eighteen months later, in December nineteen fifty-three, a couple driving near Seymour, Indiana, reported two objects | that hovered with complete level stability, | and then left with what the report calls incredible speed.",
  [I("in_head", kb="in", focus=[0.5, 0.4], lab=IN), I("in_sound", kb="in", focus=[0.5, 0.6], lab=IN)], dict(tag=("NEAR SEYMOUR, INDIANA", "DECEMBER 1953"))),
 ("And about the sound, one line: | none to the ear, although observers stood outside of car to make sure.",
  [I("in_sound", kb="down", focus=[0.5, 0.35], lab=IN)], dict(slow=True)),
 ("Each one, the report says, looked like a circular ring of smoke, | with four brilliant points of light rotating slowly clockwise, | and no structure above or below.",
  [I("in_shape", kb="in", focus=[0.5, 0.45], lab=IN)], {}),
 ("Silent. | Hovering. | Then gone, at great speed. | The same three ideas, in reports written more than seventy years apart.",
  [C("dv996969s", 6.0, lab=MW)], {}),
 ("But the old files also show what can happen to cases like these. | Catalina again, March fifteenth, nineteen fifty-five: | a very bright round object, orange, then red, falling straight down for about two seconds.",
  [I("cat55", kb="in", focus=[0.4, 0.5], lab=C55)], dict(tag=("AVALON, CATALINA ISLAND", "MARCH 15, 1955"))),
 ("The Air Force record card has one conclusion, typed in the corner: | probable meteor.",
  [I("cat55", kb="in", focus=[0.75, 0.55], lab=C55)], dict(gap=0.9, sil=True)),

 # ---------------- VI. THE BOMBER ----------------
 ("Then there is the file stamped Secret.",
  [G("chapter", n="VI", t="The Bomber")], {}),
 ("January nineteen fifty-seven. | B fifty-two bombers were flying around the world without landing, | refuelling in the air, on a mission called Operation Power Flite.",
  [C("dv1006838t", 42.0, lab=B52T)], dict(tag=("OPERATION POWER FLITE", "JANUARY 16-18, 1957"))),
 ("They covered twenty-four thousand three hundred twenty-five miles in forty-five hours and nineteen minutes, according to the Air Force.",
  [C("dv1006838t", 82.0, lab=B52T)], {}),
 ("Over Saudi Arabia, at night, at thirty-nine thousand feet, | B fifty-two number three ninety-four, commanded by Lieutenant Colonel J H Morris, | was about to meet its tanker.",
  [I("sa_sum", kb="in", focus=[0.5, 0.45], lab=SA + "1"), C("dv1010076s", 24.0, lab=B52R)], dict(tag=("OVER SAUDI ARABIA, 27°N 47°E", "JANUARY 1957"))),
 ("Just before the rendezvous, the gunner's radar scope picked up an unidentified aircraft.",
  [I("sa_scope", kb="in", focus=[0.5, 0.3], lab=SA + "1")], {}),
 ("The report even includes a drawing of the scope. | The unknown blip sat at the six thousand yard marker, in the center of the scope, | for five to seven minutes.",
  [I("sa_diag", kb="in", focus=[0.5, 0.45], lab=SA + "2")], {}),
 ("Then the B fifty-two banked left, and the blip slid off the scope. | The report admits the bomber's turn may have caused that. | But it notes the object seemed to disappear in the direction of the Baghdad flight identification region.",
  [I("sa_scope", kb="down", focus=[0.5, 0.65], lab=SA + "1"), C("dv1010076s", 60.0, lab=B52R)], {}),
 ("Its return was smaller than a second B fifty-two flying nearby. | And the report's whole significance comes down to one sentence: | the unidentified aircraft appeared on the scope where no aircraft were expected.",
  [I("sa_sig", kb="in", focus=[0.5, 0.5], lab=SA + "1")], dict(slow=True)),
 ("Another file, from Sweden, December seventeenth, nineteen fifty-three. | The chief pilot of a Swedish airline was flying a D C three when a shining metal elliptical object passed below it, in the opposite direction.",
  [C("dv934491s", 32.0, lab=C47), I("sw_robot", kb="in", focus=[0.5, 0.4], lab=SW)], dict(tag=("NEAR HÄSSLEHOLM, SWEDEN", "DECEMBER 17, 1953"))),
 ("It was visible for six to seven seconds. | The pilot told a newspaper it was something absolutely new, | possibly an unmanned robot. | The U S air attache in Stockholm translated the article and sent it home.",
  [I("sw_robot", kb="down", focus=[0.5, 0.7], lab=SW)], {}),
 ("His crew chief, who saw it longer, thought it was almost phosphorescent. | And the pilot was sure of one thing: | the object could definitely not have been a meteor. | It gave off no waste gases or condensation traces.",
  [I("sw_meteor", kb="in", focus=[0.5, 0.5], lab=SW), C("dv934491s", 40.0, lab=C47)], {}),
 ("The attache's report adds a caution: | a Swedish Air Board source who had known the pilot all his life personally doubted his story, | while Sweden's Defense Staff kept investigating.",
  [I("sw_note", kb="in", focus=[0.5, 0.5], lab=SW.replace("P. 2", "P. 3"))], {}),
 ("But the same batch also keeps the boring answers. | In French Morocco, radar operators saw returns shaped like V's, W's and M's. | The explanation offered: anomalous propagation, radar jamming from a ship, | or geese or storks in flight.",
  [I("mo", kb="in", focus=[0.5, 0.5], lab=MO)], {}),
 ("In Alaska, a light seen west of Gambell, on Saint Lawrence Island: | possibly, the report says, an unidentified ship operating in or near U S territorial waters.",
  [I("ak", kb="in", focus=[0.5, 0.5], lab=AK)], dict(gap=0.9, sil=True)),

 # ---------------- VII. WHO GETS THE PIECES ----------------
 ("And then there is a practical question in these files: | what happens when something falls out of the sky?",
  [G("chapter", n="VII", t="Who Gets the Pieces")], {}),
 ("In nineteen sixty-two and sixty-three, the National Aeronautics and Space Council, part of the Executive Office of the President, held meetings on a practical question. | When pieces of satellites and rockets fell to Earth, | who would collect them?",
  [G("stat", k="1962-1963 · NATIONAL AERONAUTICS AND SPACE COUNCIL", a="WHO GETS", size=200, b="the pieces when space hardware falls to Earth?", c="Executive Office of the President", source="SOURCE: USG-UAP-D002, SPACE-FRAGMENT CORRESPONDENCE 1962-1964 (PURSUE RELEASE 07)")], {}),
 ("Draft guidelines in this file make NASA the agency responsible for receiving and identifying fragments of space vehicles of all types. | But anything from a foreign launch, including whole vehicles, | was to go to the Defense Department, quickly, for intelligence analysis.",
  [G("doc", top=60, w=1400, header="RECREATED · DRAFT, MARCH 1963 · VERBATIM EXCERPTS", title="Guidelines for interagency handling of space vehicle fragments", lines=[
      "The National Aeronautics and Space Administration (NASA) is designated as the agency responsible for receiving and identifying fragments, or suspected fragments of space vehicles.",
      "... fragments {{(including whole vehicles)}} which are readily identifiable or suspect as coming from vehicles launched from foreign countries ...",
      "Such foreign fragments which come initially into possession of the DoD {{will be retained by DoD for analysis.}}"],
      source="SOURCE: USG-UAP-D002 (PURSUE RELEASE 07) · RECREATED, WORDING VERBATIM")], {}),
 ("On May twenty-ninth, nineteen sixty-three, a memo went to the council's executive secretary, Doctor Edward Welsh, about a meeting with Arnold Frutkin, NASA's director of international programs.",
  [I("eop_head", kb="in", focus=[0.5, 0.5], lab=EOP)], dict(tag=("WASHINGTON, D.C.", "MAY 29, 1963"))),
 ("Frutkin, the memo says, was now very negative on the project. | He seemed to feel that no public announcement was needed, | and that a statement from the White House would scare people needlessly.",
  [I("eop_list", kb="in", focus=[0.5, 0.3], lab=EOP)], {}),
 ("And point four, still Frutkin's view as the memo records it: | the Defense Department and the Air Force want to use NASA for a cover, | but have no intention of letting NASA do anything but return some pieces.",
  [I("eop_cover", kb="in", focus=[0.5, 0.5], lab=EOP)], dict(slow=True)),
 ("To be clear, this memo is about rockets and satellites. | It says nothing about U F O's. | But it records a NASA official's view that NASA was meant to be the public face, | while the draft guidelines sent foreign pieces to the Defense Department first, for analysis.",
  [I("eop_list", kb="down", focus=[0.5, 0.7], lab=EOP)], dict(gap=0.9, sil=True)),

 # ---------------- VIII. THE RANCH ----------------
 ("The last file is the strangest one.",
  [G("chapter", n="VIII", t="The Ranch")], {}),
 ("In March and April twenty ten, a team from a private contractor, Bigelow Aerospace Advanced Space Studies, | working under a Defense Intelligence Agency contract, | went to a ranch near Fort Duchesne, Utah.",
  [I("ranch_cover", kb="in", focus=[0.5, 0.5], lab=UR + "1")], dict(tag=("NEAR FORT DUCHESNE, UTAH", "MARCH-APRIL 2010"))),
 ("Their report lists what local witnesses told them: | balls of light at close range, | dog-like creatures running on two legs, | little people, | and a giant worm.",
  [I("ranch_abs", kb="in", focus=[0.5, 0.4], lab=UR + "8")], {}),
 ("The team set up seven game cameras. | And one witness said that a couple of days before they arrived, he had seen what he believed was a Skinwalker. | His dogs chased it, he said, and it ran through a barbed-wire fence.",
  [I("ranch_exec", kb="in", focus=[0.5, 0.5], lab=UR + "5")], {}),
 ("Hair was collected from the fence, | along with a control sample from one of the dogs on that property, | and sent to a laboratory for D N A testing.",
  [C("dv403905", 72.0, lab=LAB), C("dv403905", 140.0, lab=LAB)], {}),
 ("And the lab report is in the release too.",
  [C("dv403905", 180.0, lab=LAB)], {}),
 ("The fence hairs and the dog's hair all showed the same canine D N A sequence, | one the lab says is frequently found in domestic dogs.",
  [I("dna", kb="in", focus=[0.5, 0.5], lab=UR + "37")], dict(slow=True)),
 ("The contractor's own analysis says this suggests, though not one hundred percent definitively, the same canine individual. | And because the dogs on that property run at will, it says the evidence strongly argues the hairs are from the same animal.",
  [I("dog", kb="in", focus=[0.5, 0.5], lab=UR + "38")], {}),
 ("And a fourth hair, found embedded in a red-stained rock? | Raccoon.",
  [I("rac", kb="in", focus=[0.5, 0.5], lab=UR + "38")], dict(slow=True)),
 ("Several people at the ranch had reported raccoons nearby, the analysis added, | so this finding would not be out of the ordinary.",
  [I("rac", kb="down", focus=[0.5, 0.6], lab=UR + "38")], dict(gap=0.9, sil=True)),

 # ---------------- IX. STILL UNRESOLVED ----------------
 ("So what does all of this add up to?",
  [G("chapter", n="IX", t="Still Unresolved")], {}),
 ("News reports on the release said officials describe these files as unresolved, | meaning investigators did not have enough information to identify what was seen, | not that it was linked to anything from another world.",
  [C("dv346026", 4.0, lab=CAP)], {}),
 ("The Pentagon's spokesman, Sean Parnell, said the department will release additional files on a rolling basis.",
  [C("dv346026", 14.0, lab=CAP)], {}),
 ("Look at these files together and a pattern appears. | A probable meteor. | Possibly storks on radar. | Possibly a ship. | A bomber's turn that may explain a vanishing blip. | Dog hair and a raccoon. | Again and again, the files either point to something ordinary, | or simply run out of information.",
  [G("timeline", kicker="PURSUE RELEASE 07", title="What the files concluded", events=[
      dict(y="1952", t="Catalina: no conclusion"), dict(y="1953", t="Morocco: maybe storks"), dict(y="1955", t="Catalina: probable meteor"),
      dict(y="1957", t="B-52: unidentified"), dict(y="2010", t="Ranch: dog, raccoon"), dict(y="2026", t="Triangle: open")], active=5, source=S_P)], {}),
 ("Which is exactly why the newest file stands out. | Two experienced observers. | A thermal reading. | A clear evening, terrain to measure against, and a search the next morning.",
  [I("fbi5", kb="in", focus=[0.66, 0.36], lab=FI.format(5))], {}),
 ("And still, in the government's own words, an unidentified craft.",
  [I("m_shape", kb="in", focus=[0.5, 0.35], lab=A_ + "1")], dict(slow=True)),
 ("Maybe it was a drone the agents could not hear. | Maybe it was something else entirely. | The documents do not say, | and we will not guess beyond them.",
  [C("dv784204", 4.0, lab=GC)], {}),
 ("What they do show is that in twenty twenty-six, federal agents described something in much the same terms an Air Force officer used about three Boy Scouts in nineteen fifty-two. | Silent. Faster than a jet. Gone.",
  [I("cat52_sum", kb="in", focus=[0.5, 0.5], lab=C52), I("fbi9", kb="in", focus=[0.6, 0.6], lab=FI.format(9))], {}),
 ("Every secret has a release date. | This one has a date that is still blacked out.",
  [C("dv996969s", 108.0, lab=MW)], dict(slow=True, gap=0.8)),
 ("Here is our question for you. | Two official reports, about thirty seconds versus three. | Which account do you trust more, and why? | Tell us in the comments.",
  [I("fbi4", kb="in", focus=[0.6, 0.33], lab=FI.format(4))], {}),
 ("Next file: another set of records the government has just released.",
  [G("end", n="016")], dict(gap=2.5)),
]

PRON = [("Arrow", "Arrow"), ("Frutkin", "Froot-kin"), ("Welsh", "Welsh"), ("Duchesne", "Doo-shane"), ("Parnell", "Par-nell"),
        ("Bigelow", "Bigga-low"), ("Skinwalker", "Skin-walker"), ("attache", "atta-shay"), ("F D three-oh-two", "F D three oh two"),
        ("F B I", "F B I"), ("U S", "U S"), ("U F O's", "U F Os"), ("D N A", "D N A"), ("D C three", "D C three"), ("Flite", "Flight")]

DISPLAY = [
 ("All-domain Anomaly Resolution Office, known as Arrow", "All-domain Anomaly Resolution Office, known as AARO"),
 ("F D three-oh-two", "FD-302"), ("F B I", "FBI"), ("U F O's", "UFOs"), ("U F O", "UFO"), ("D N A", "DNA"), ("D C three", "DC-3"),
 ("U S air attache", "U.S. air attaché"), ("U S territorial", "U.S. territorial"), ("U S", "U.S."),
 ("B fifty-two", "B-52"), ("three ninety-four", "394"), ("J H Morris", "J.H. Morris"),
 ("twenty twenty-six", "2026"), ("twenty ten", "2010"), ("nineteen fifty-two", "1952"), ("nineteen fifty-three", "1953"),
 ("nineteen fifty-five", "1955"), ("nineteen fifty-seven", "1957"), ("nineteen fifties", "1950s"), ("nineteen sixty-three", "1963"),
 ("nineteen sixty-two and sixty-three", "1962 and 1963"),
 ("eight twenty-three in the evening", "8:23 in the evening"), ("October twenty-third", "October 23"), ("June twenty-fifth", "June 25"),
 ("March fifteenth", "March 15"), ("December seventeenth", "December 17"), ("May twenty-ninth", "May 29"),
 ("thirteen to fifteen feet", "13 to 15 feet"), ("nine to fifteen feet", "9 to 15 feet"), ("six to nine feet", "6 to 9 feet"),
 ("one to two feet", "1 to 2 feet"), ("one hundred percent", "100 percent"), ("one point four and three point two miles", "1.4 and 3.2 miles"), ("one point four miles", "1.4 miles"),
 ("three point two miles", "3.2 miles"), ("one and a half miles", "1.5 miles"), ("two to three hundred feet", "200 to 300 feet"),
 ("two hundred feet", "200 feet"), ("six thousand yard", "6,000-yard"), ("thirty-nine thousand feet", "39,000 feet"),
 ("twenty-four thousand three hundred twenty-five miles", "24,325 miles"), ("forty-five hours and nineteen minutes", "45 hours and 19 minutes"),
 ("seventy years", "70 years"), ("twenty-eight files", "28 files"), ("seven twenty-three in the evening", "7:23 in the evening"), ("says eight twenty-three", "says 8:23"), ("attache's", "attaché's"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="016", title="The Silent Black Triangle Federal Agents Couldn't Identify",
    imgs={**{k: D + k + ".jpg" for k in ["m_shape", "m_climb", "m_overview", "m_silent", "m_post", "m_call", "m_ph1", "m_ph2", "m_ph3a",
                                         "m_ph3b", "m_survey", "m_note", "m_noeff", "m_head", "f_head", "f_obj", "f_ridge", "f_end",
                                         "sa_head", "sa_sum", "sa_scope", "sa_sig", "sa_diag", "in_head", "in_shape", "in_sound", "cat55",
                                         "cat52_head", "cat52_sum", "cat52_rel", "sw_robot", "sw_meteor", "mo", "ak", "eop_head", "eop_list",
                                         "eop_cover", "dna", "rac", "dog", "ranch_cover", "ranch_abs", "ranch_exec", "sw_note"]},
          **{f"fbi{i}": F + f"fbi{i}.jpg" for i in range(1, 10)}},
    credit="Documents: Department of War PURSUE Release 07 (war.gov/UFO, Oct. 23, 2026): AARO, FBI, U.S. Air Force, LBJ Library and contractor records.\\NB-roll: DoD via DVIDS; modern b-roll does not show the events described. Images of the triangle are depictions attached to the FBI report. No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[59, 63], tpl="blue", hook="B-52 RADAR:<br>SOMETHING<br>[NOT EXPECTED]", hs=170),
        dict(id="s2", lines=[80, 86], tpl="yellow", hook="THE<br>'SKINWALKER'<br>[HAIR TEST]", hs=175),
        dict(id="s3", lines=[29, 36], tpl="white", hook="THE FBI<br>FILE:<br>[3 SECONDS]", hs=185),
        dict(id="s4", lines=[72, 76], tpl="red", hook="1963 MEMO:<br>'NASA FOR<br>[A COVER]'", hs=185),
    ],
    yshorts=[
        dict(id="y1", lines=[1, 3], tpl="yellow", hook="SILENT<br>BLACK<br>[TRIANGLE]", hs=210),
        dict(id="y2", lines=[81, 83], tpl="red", hook="'SKINWALKER'<br>HAIR:<br>[DNA RESULT]", hs=175),
        dict(id="y3", lines=[33, 34], tpl="white", hook="30 SECONDS<br>OR<br>[3?]", hs=210),
    ],
)
