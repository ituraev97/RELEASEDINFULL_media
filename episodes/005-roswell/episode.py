# FILE 005 — Roswell, According to the Air Force
# Format: see episodes/001-navy-videos/episode.py
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
GAO = "ACTUAL DOCUMENT · GAO REPORT TO REP. STEVEN SCHIFF, \"RESULTS OF A SEARCH FOR RECORDS CONCERNING THE 1947 CRASH NEAR ROSWELL\" · JULY 28, 1995"
FBI = "ACTUAL DOCUMENT · FBI TELETYPE, DALLAS OFFICE, JULY 8, 1947 · AS REPRODUCED IN THE GAO REPORT, 1995"
H509 = "ACTUAL DOCUMENT · 509TH BOMB GROUP AND ROSWELL ARMY AIR FIELD HISTORY, JULY 1947 · AS REPRODUCED IN THE GAO REPORT, 1995"
WEAV = "ACTUAL DOCUMENT · \"REPORT OF AIR FORCE RESEARCH REGARDING THE 'ROSWELL INCIDENT',\" JULY 1994 · PUBLISHED IN \"THE ROSWELL REPORT: FACT VS. FICTION\" (USAF, 1995)"
MEMO = "ACTUAL DOCUMENT · COL. RICHARD L. WEAVER, MEMO TO THE SECRETARY OF THE AIR FORCE, JULY 27, 1994"
CAV = "ACTUAL DOCUMENT · SWORN STATEMENT OF LT. COL. SHERIDAN CAVITT (RET.), MAY 24, 1994 · USAF ROSWELL REPORT, 1995"
MOORE = "ACTUAL DOCUMENT · SWORN STATEMENT OF PROF. CHARLES B. MOORE, JUNE 8, 1994 · USAF ROSWELL REPORT, 1995"
MOG46 = "ACTUAL DOCUMENT · AIR MATERIEL COMMAND LETTER ON PROJECT \"MOGUL\" CLASSIFICATION, JULY 8, 1946 · USAF ROSWELL REPORT, 1995"
ML307 = "PHOTO IN THE 1995 USAF REPORT · ML-307C/AP RADAR TARGET, A 1953-MADE MODEL OBTAINED FOR THE 1994 AIR FORCE RESEARCH (1947 FLIGHTS USED THE SIMILAR MODEL B)"
CC = "ACTUAL DOCUMENT · \"THE ROSWELL REPORT: CASE CLOSED\" · U.S. AIR FORCE, 1997"
CCMOG = "ILLUSTRATION IN \"THE ROSWELL REPORT: CASE CLOSED\" (USAF, 1997) · A PROJECT MOGUL BALLOON TRAIN"
CCHD = "U.S. AIR FORCE PHOTO · PROJECT HIGH DIVE DUMMY LAUNCH, WHITE SANDS PROVING GROUND, N.M., JUNE 11, 1957 · IN \"CASE CLOSED\" (1997)"
CCDUM = "PHOTOS IN \"CASE CLOSED\" (1997) · LEFT: TEST DUMMIES ON AN M-342 WRECKER USED TO LAUNCH AND RECOVER THEM · RIGHT: DUMMY IN A PROJECT HIGH DIVE GONDOLA, WHITE SANDS NATIONAL MONUMENT, N.M., OCT. 8, 1957"
CCTRK = "U.S. AIR FORCE PHOTOS · HOLLOMAN AFB BALLOON BRANCH RECOVERY VEHICLES, 1950s · IN \"CASE CLOSED\" (1997)"
EXC = "ARCHIVAL · U.S. AIR FORCE FILM OF PROJECT EXCELSIOR HIGH-ALTITUDE BALLOON FLIGHTS, 1959–60 (NARA 342-USAF-33041)"
CAP = "B-ROLL · U.S. CAPITOL, WASHINGTON, D.C., 2012"
AIR26 = "B-ROLL · VIEW FROM A U.S. AIR FORCE F-22 OVER WASHINGTON, D.C., 2026"
HABDAY = "B-ROLL · MODERN U.S. ARMY HIGH-ALTITUDE BALLOON LAUNCH, YAKIMA TRAINING CENTER, WASH., 2025"
HABNIGHT = "B-ROLL · MODERN HIGH-ALTITUDE BALLOON LAUNCH, NATIONAL TRAINING CENTER, CALIF., 2026"
WSMR = "B-ROLL · WHITE SANDS MISSILE RANGE, NEW MEXICO, 2018"

S_GAO = "SOURCE: GAO, \"GOVERNMENT RECORDS: RESULTS OF A SEARCH FOR RECORDS CONCERNING THE 1947 CRASH NEAR ROSWELL, NEW MEXICO\" (GAO/NSIAD-95-187), JULY 28, 1995"
S_W = "SOURCE: REPORT OF AIR FORCE RESEARCH REGARDING THE \"ROSWELL INCIDENT,\" JULY 1994 (IN \"THE ROSWELL REPORT: FACT VS. FICTION,\" USAF, 1995)"
S_CC = "SOURCE: U.S. AIR FORCE, \"THE ROSWELL REPORT: CASE CLOSED\" (1997)"
S_RDR = "SOURCE: ROSWELL DAILY RECORD, JULY 9, 1947, AS REPRODUCED IN THE USAF REPORTS (1995, 1997)"

NM = dict(kicker="JUNE–JULY 1947", title="Where the story happened", bounds=[[-108.6, 31.4], [-96.4, 35.8]],
          points=[dict(ll=[-104.52, 33.39], name="Roswell", sub="ROSWELL ARMY AIR FIELD", anchor="end"),
                  dict(ll=[-105.55, 34.15], name="Debris field", sub="ABOUT 75 MILES NW OF ROSWELL", color="#F2D04B"),
                  dict(ll=[-106.07, 32.84], name="Alamogordo AAF", sub="PROJECT MOGUL LAUNCHES"),
                  dict(ll=[-97.33, 32.75], name="Fort Worth", sub="EIGHTH AIR FORCE HQ", anchor="end")],
          source="SOURCES: USAF ROSWELL REPORTS (1995, 1997) · MAP: NATURAL EARTH · LOCATIONS APPROXIMATE")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("On July eighth, nineteen forty-seven, the public information office at Roswell Army Air Field, in New Mexico, put out a remarkable announcement. | The Army, it said, had recovered a flying disc.",
  [I("gao1", kb="in", focus=[0.5, 0.75], lab=GAO)], dict(tag=("ROSWELL, N.M.", "JULY 8, 1947"))),
 ("The next day, the papers carried a different story. A general in Fort Worth, Texas, had said the object was a radar-tracking balloon.",
  [I("ex1678", kb="in", focus=[0.5, 0.4], lab=EXC)], {}),
 ("For thirty years, almost nobody cared. | Then the story came back, bigger than before. Stories of strange metal, of a second crash site, and of bodies.",
  [I("gao2", kb="in", focus=[0.5, 0.45], lab=GAO)], dict(gap=0.9, sil=True)),
 ("In the nineteen nineties, under pressure from Congress, the Air Force went back through its own records. | It published two official reports. One offered an explanation for the debris. The other, for the stories of bodies.",
  [I("cc0", kb="in", focus=[0.5, 0.35], lab=CC)], {}),
 ("Here is what those reports actually say. And where they've been challenged.",
  [I("w2a", kb="in", focus=[0.5, 0.3], lab=WEAV)], {}),
 ("Let's open the file.",
  [G("intro", n="005")], dict(gap=0.2)),
 ("",
  [G("title", n="005", t="Roswell", size=200, sub="According to the Air Force")], dict(gap=0.4)),

 # ---------------- I. THE DISC ----------------
 ("It started on a ranch.",
  [G("chapter", n="I", t="The Disc")], {}),
 ("According to the Roswell Daily Record, a rancher named W. W. Brazel, known as Mac, and his son came across a large area of bright wreckage on June fourteenth, nineteen forty-seven. About seventy-five miles northwest of Roswell.",
  [G("map", **NM)], {}),
 ("The paper said it was made up of rubber strips, tinfoil, a rather tough paper, and sticks.",
  [G("quote", q="…a large area of bright wreckage made up {{of rubber strips, tinfoil, a rather tough paper, and sticks.}}",
     who="Roswell Daily Record", role="July 9, 1947 · as quoted in the 1995 USAF report", size=58, source=S_RDR)], {}),
 ("In early July, Brazel told the sheriff he might have found a flying disc. The sheriff called the air field. | The base intelligence officer, Major Jesse Marcel, went out to the ranch, and brought the material back.",
  [I("w24a", kb="in", focus=[0.5, 0.6], lab=WEAV)], {}),
 ("Then came the announcement. And within a day, the Commanding General of the Eighth Air Force, Roger Ramey, said the debris was a weather balloon.",
  [I("w2a", kb="down", focus=[0.5, 0.6], lab=WEAV)], {}),
 ("Brazel's own account, in the same newspaper, included some odd details. Tape with flowers printed on it. Eyelets in the paper. | And the whole lot, he estimated, weighed maybe five pounds.",
  [G("list", kicker="ROSWELL DAILY RECORD · JULY 9, 1947", title="What the rancher described", items=[
     dict(n="01", t="Rubber, tinfoil, tough paper, sticks", s="SCATTERED OVER ABOUT 200 YARDS"), dict(n="02", t="Tape with flowers printed on it", s="AND EYELETS IN THE PAPER"),
     dict(n="03", t="About five pounds in all", s="NO ENGINE, NO PROPELLERS, HE SAID")], source=S_RDR)], {}),
 ("But he also said this. I am sure what I found was not any weather observation balloon.",
  [G("quote", q="I am sure what I found {{was not any weather observation balloon.}}", who="W. W. \"Mac\" Brazel",
     role="Roswell Daily Record, July 9, 1947", size=64, source=S_RDR)], dict(slow=True)),
 ("On July eighth, the day of the announcement, the F B I's Dallas office sent a teletype to headquarters. | An Eighth Air Force official had described the object as hexagonal, suspended from a balloon by cable. It resembled, he said, a high-altitude weather balloon with a radar reflector. | But, the message added, a phone call between their office and Wright Field had not borne out this belief.",
  [I("fbi1", kb="in", focus=[0.45, 0.45], lab=FBI)], dict(tag=("FBI, DALLAS", "JULY 8, 1947"))),
 ("The debris, the message said, was being flown to Wright Field, in Ohio, for examination. | No further investigation was being conducted.",
  [I("fbi2", kb="down", lab=FBI)], {}),
 ("The base's own history for July nineteen forty-seven settled it in two sentences. The public information office was kept busy answering inquiries on the flying disc. | The object turned out to be a radar tracking balloon.",
  [I("h509", kb="in", focus=[0.5, 0.5], lab=H509)], dict(gap=0.9, sil=True)),

 # ---------------- II. THE SILENCE ----------------
 ("And that was that.",
  [G("chapter", n="II", t="Thirty Years")], {}),
 ("According to the Air Force, Roswell wasn't even treated as a U F O event until nineteen seventy-eight. | It doesn't appear in Project Blue Book, the Air Force's official investigation of U F O reports.",
  [I("w3a", kb="in", focus=[0.5, 0.5], lab=WEAV)], {}),
 ("In nineteen seventy-eight, a tabloid reported that Marcel, the former intelligence officer, now claimed the debris he handled came from a U F O. | A researcher, Stanton Friedman, began investigating. And in nineteen eighty, a book called The Roswell Incident laid out the case.",
  [I("w3a", kb="up", focus=[0.5, 0.5], lab=WEAV)], {}),
 ("Over the next decade, the story grew. More witnesses came forward, many of them speaking forty years after the fact. | According to the Air Force, the debris grew from a small area to multiple huge debris fields. Sticks and tinfoil became exotic metals.",
  [I("ex1165", kb="in", focus=[0.5, 0.35], lab=EXC)], {}),
 ("And most versions now included a second site, where, it was said, the military recovered bodies, and flew them to Wright Field.",
  [I("w2b", kb="in", focus=[0.5, 0.4], lab=WEAV)], dict(gap=0.9, sil=True)),

 # ---------------- III. THE AUDIT ----------------
 ("Which is where Congress came in.",
  [G("chapter", n="III", t="The Audit")], {}),
 ("In nineteen ninety-three, New Mexico Congressman Steven Schiff asked the Pentagon about Roswell. He felt he was given the runaround.",
  [C("dv346026", 3.0, lab=CAP)], dict(tag=("U.S. CONGRESS", "1993–1994"))),
 ("In January nineteen ninety-four, he told the Washington Post, whatever it was, it wasn't a balloon. Apparently, it's another government coverup.",
  [G("quote", q="…whatever it was, {{it wasn't a balloon. Apparently, it's another government coverup.}}", who="Rep. Steven Schiff (R-N.M.)",
     role="Washington Post, Jan. 14, 1994 · reprinted in the USAF report", size=58, source=S_W)], {}),
 ("At his request, the General Accounting Office, the investigative arm of Congress, opened an audit. | And the Air Force launched its own search.",
  [C("dv1026930", 25.5, lab=AIR26)], {}),
 ("Its researchers went through archives and records centers across the country, including Top Secret files. | Any current or former Air Force official bound by a secrecy oath, the Air Force said, would be freed from it.",
  [I("w1", kb="in", focus=[0.5, 0.3], lab=MEMO)], {}),
 ("In July nineteen ninety-four, Colonel Richard Weaver sent the result to the Secretary of the Air Force. | The search, he wrote, did not identify any indication that the Roswell Incident was any type of extraterrestrial event.",
  [I("w1b", kb="in", focus=[0.5, 0.35], lab=MEMO)], dict(slow=True)),
 ("Nor that the Air Force had engaged in a forty-seven year conspiracy. | He predicted what would happen next. Critics, he wrote, would denounce the report as a continuation of the cover-up.",
  [I("w1b", kb="down", focus=[0.5, 0.55], lab=MEMO)], dict(gap=0.9, sil=True)),

 # ---------------- IV. MOGUL ----------------
 ("So what did the Air Force say actually fell on the ranch?",
  [G("chapter", n="IV", t="Mogul")], {}),
 ("A balloon. But not an ordinary weather balloon. | The answer, the report said, had been declassified for years. A formerly Top Secret project, code-named Mogul.",
  [I("mog46", kb="in", focus=[0.5, 0.4], lab=MOG46)], {}),
 ("After World War Two, the United States needed to know when the Soviet Union tested its first atomic bomb. The Soviet borders were closed. | Mogul's idea was to listen for it. Acoustic sensors, carried high into the atmosphere by balloons, to pick up the low-frequency sound waves of distant explosions.",
  [C("dv1023102", 46.0, lab=HABDAY), C("dv1003608", 37.0, lab=HABNIGHT), I("ex1678", kb="in", focus=[0.5, 0.3], lab=EXC)], {}),
 ("The balloons flew in long trains. According to the Air Force, more than six hundred feet of balloons, sensors, and radar reflectors, strung together on a single line.",
  [I("cc2", kb="up", focus=[0.5, 0.5], lab=CCMOG)], {}),
 ("The radar reflectors were the key. Foil-covered paper on balsa-wood sticks, held with tape, glue and twine. | According to the project's engineer, Charles Moore, some early targets were made by a toy or novelty company, and assembled with purplish-pink tape printed with symbols.",
  [I("ml307", kb="in", focus=[0.5, 0.45], lab=ML307)], {}),
 ("A former project officer, Albert Trakowski, described that tape too. Flowers and hearts.",
  [I("moore", kb="in", focus=[0.5, 0.45], lab=MOORE)], {}),
 ("New York University's team launched the Mogul flights from Alamogordo Army Air Field, in New Mexico, starting in June nineteen forty-seven. Some of the early flights were never logged.",
  [I("ex88", kb="in", focus=[0.6, 0.4], lab=EXC)], {}),
 ("One of them, Flight Four, went up on June fourth, nineteen forty-seven, according to the journal of the field scientist, Albert Crary. | It was not recovered by the N Y U group.",
  [G("stat", k="NYU BALLOON GROUP · ALAMOGORDO, N.M.", a="JUNE 4, 1947", size=170, b="Flight 4 launched", c="not recovered by the NYU group, per A. P. Crary's journal", source=S_W)], {}),
 ("Ten days later, Brazel found his wreckage. | In Moore's scientific opinion, the debris was most probably from Flight Four.",
  [I("w4a", kb="in", focus=[0.5, 0.6], lab=WEAV)], {}),
 ("The Air Force also found the last living one of the three men officially acknowledged to have recovered material from the ranch: Sheridan Cavitt, a counterintelligence agent who went out with Marcel.",
  [I("cav", kb="in", focus=[0.5, 0.3], lab=CAV)], {}),
 ("In a sworn statement, he described bamboo type square sticks, very light, and some sort of metallic reflecting material. | I remember, he said, recognizing this material as being consistent with a weather balloon.",
  [G("quote", q="I remember recognizing this material {{as being consistent with a weather balloon.}}", who="Lt. Col. Sheridan Cavitt (Ret.)",
     role="Sworn statement, May 24, 1994", size=60, source=S_W)], {}),
 ("The report's conclusion was careful. The most likely source of the wreckage was one of the Project Mogul balloon trains. | The flying disc announcement, it said, seemed to be an overreaction, at a time when nobody knew for sure what the term even meant.",
  [I("w5a", kb="in", focus=[0.5, 0.4], lab=WEAV)], dict(gap=0.9, sil=True)),

 # ---------------- V. THE BODIES ----------------
 ("But Mogul couldn't explain the bodies.",
  [G("chapter", n="V", t="The Bodies")], {}),
 ("On June twenty-fourth, nineteen ninety-seven, the Air Force released a second report. Its title: The Roswell Report, Case Closed.",
  [I("cc0", kb="down", focus=[0.5, 0.5], lab=CC)], dict(tag=("U.S. AIR FORCE", "JUNE 24, 1997"))),
 ("Its central claim was that the accounts of bodies, in most instances, described actual Air Force activities. | But those activities hadn't happened in nineteen forty-seven.",
  [I("cc1", kb="in", focus=[0.5, 0.3], lab=CC)], {}),
 ("From nineteen fifty-three to nineteen fifty-nine, Air Force scientists studied how a pilot could survive bailing out at extreme altitude. | To test it, they used human-sized dummies.",
  [I("cc3", kb="in", focus=[0.5, 0.45], lab=CCHD)], {}),
 ("The report counts forty-three balloon flights carrying sixty-seven dummies across New Mexico, between June nineteen fifty-four and February nineteen fifty-nine. | Most came down outside military land, in eastern New Mexico, near Roswell, and around the Tularosa Valley.",
  [G("stat", k="PROJECTS HIGH DIVE & EXCELSIOR · NEW MEXICO", a="67", size=300, b="test dummies dropped from balloons", c="43 flights, June 1954 – February 1959 · up to 98,000 feet", source=S_CC)], {}),
 ("The recovery crews, the report says, arrived fast, in trucks and aircraft, to collect the dummies and their instruments. | That, it says, explains stories of military units arriving just after a crash.",
  [I("cc6", kb="in", focus=[0.5, 0.5], lab=CCTRK), I("ex2098", kb="in", focus=[0.45, 0.5], lab=EXC)], {}),
 ("The claims about bodies at the base hospital, the report said, most likely combined two separate events. | A nineteen fifty-six aircraft accident in which eleven Air Force members lost their lives. And a nineteen fifty-nine balloon mishap in which two Air Force pilots were injured.",
  [G("timeline", kicker="CASE CLOSED (1997)", title="Events years apart, remembered as one", active=0,
     events=[dict(y="JULY 1947", t="Mogul debris recovered"), dict(y="1954–59", t="Dummy drops in New Mexico"),
             dict(y="1956", t="KC-97 crash: 11 killed"), dict(y="1959", t="Balloon mishap: 2 injured")], source=S_CC)], {}),
 ("Its conclusion. Air Force activities over many years had been consolidated, and were now represented to have occurred in two or three days in July nineteen forty-seven.",
  [G("quote", q="Air Force activities which occurred over a period of many years have been consolidated and are now represented to have occurred {{in two or three days in July 1947.}}",
     who="U.S. Air Force", role="The Roswell Report: Case Closed, 1997", size=50, source=S_CC)], dict(slow=True, gap=0.9, sil=True)),

 # ---------------- VI. THE OBJECTIONS ----------------
 ("And that is exactly where the critics pushed back.",
  [G("chapter", n="VI", t="The Objections")], {}),
 ("The problem was obvious. The dummy drops began years after nineteen forty-seven. | Stanton Friedman told reporters that none of that work was done before the nineteen fifties. Another researcher, Karl Pflock, who accepted the Mogul explanation, called the dummy explanation a real stretch.",
  [I("cc5", kb="in", focus=[0.5, 0.4], lab=CCDUM)], {}),
 ("At the Pentagon briefing, according to the Spokesman-Review, Colonel John Haynes answered that when people talk about things over a period of time, they begin to lose exactly when the date was.",
  [C("dv1026930", 41.0, lab=AIR26)], {}),
 ("There were other gaps. The G A O found that records of the base's administrative activity from nineteen forty-five to nineteen forty-nine, and its outgoing messages from late nineteen forty-six to nineteen forty-nine, had been destroyed.",
  [I("gaodes", kb="in", focus=[0.5, 0.5], lab=GAO)], {}),
 ("The disposal form, the G A O said, didn't show who destroyed them, when, or under what authority. | The records center's chief archivist said that happened often in that period.",
  [G("stat", k="GAO REPORT · JULY 28, 1995", a="1945–1949", size=190, b="Roswell base records destroyed", c="administrative files and outgoing messages · no authority recorded on the disposal form", source=S_GAO)], {}),
 ("The Air Force itself admitted it found no document explaining why the base announced a flying disc in the first place. | And the link to Flight Four rests on a journal entry, a scientist's opinion, a witness's memory and the nineteen forty-seven press photos of the debris. The report cites no tag or serial number tying the debris to that flight.",
  [I("w4b", kb="in", focus=[0.5, 0.6], lab=WEAV)], {}),
 ("The G A O's own search turned up just two government records from nineteen forty-seven about the crash. The base history, and the F B I teletype.",
  [I("gaofbi", kb="in", focus=[0.5, 0.5], lab=GAO)], dict(gap=0.9, sil=True)),

 # ---------------- VII. WHAT IT PROVES ----------------
 ("So, what does this file actually prove?",
  [G("chapter", n="VII", t="What It Proves")], {}),
 ("It proves that in July nineteen forty-seven, the Army announced it had a flying disc, and took it back within a day. | And that a Top Secret balloon project was flying over New Mexico at the time.",
  [I("ex1770", kb="in", focus=[0.5, 0.35], lab=EXC)], {}),
 ("It proves that the Air Force, searching its records nearly fifty years later, found nothing describing a crashed craft or recovered bodies. | And it proves that some records that might have helped were already gone.",
  [G("timeline", kicker="THE PAPER TRAIL", title="Roswell, on the record", active=3,
     events=[dict(y="JULY 1947", t="Flying disc, then balloon"), dict(y="1978–80", t="The story returns"),
             dict(y="1994–95", t="Air Force: Project Mogul"), dict(y="1997", t="Air Force: test dummies")],
     source="SOURCES: GAO/NSIAD-95-187 (1995); USAF ROSWELL REPORTS (1995, 1997)")], {}),
 ("What it doesn't prove matters just as much. The Air Force's Mogul answer is a best match, in its own words, the most likely source. | And its explanation for the bodies depends on witnesses having misremembered dates by years. Many people still don't accept that.",
  [I("w5a", kb="out", focus=[0.5, 0.45], lab=WEAV)], dict(slow=True)),
 ("Every secret has a release date. Mogul's came in the nineteen seventies. Roswell's explanation took the Air Force until nineteen ninety-seven. | Whether it closed the case is still being argued.",
  [I("ex1678", kb="out", focus=[0.5, 0.4], lab=EXC)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments.",
  [C("dv346026", 14.0, lab=CAP)], {}),
 ("Next time: the photographs that took the world to the edge of nuclear war.",
  [G("end", n="005", next="Thirteen Days: The Cuban Missile Photos")], dict(gap=2.5)),
]

PRON = [("Brazel's", "Bruh-zell's"), ("Brazel", "Bruh-zell"), ("Marcel", "Mar-sell"), ("Ramey", "Ray-mee"), ("Cavitt", "Cav-it"),
        ("Trakowski", "Truh-kow-ski"), ("Crary", "Crair-ee"), ("Pflock", "Flock"), ("Tularosa", "Too-luh-row-sah"),
        ("Alamogordo", "Alamo-gordo"), ("Spokesman-Review", "Spokesman Review"), ("W. W.", "W W"), ("Mogul's", "Moe-gul's"), ("Mogul", "Moe-gul"),
        ("U F O", "U F O"), ("G A O's", "G A O's"), ("F B I's", "F B I's"), ("cover-up", "cover up"), ("coverup", "cover up")]

DISPLAY = [
 ("U F O", "UFO"), ("G A O's", "GAO's"), ("G A O", "GAO"), ("F B I's", "FBI's"), ("F B I", "FBI"),
 ("nineteen forty-seven", "1947"), ("nineteen forty-six", "1946"), ("nineteen forty-five", "1945"), ("nineteen forty-nine", "1949"),
 ("nineteen fifty-three", "1953"), ("nineteen fifty-four", "1954"), ("nineteen fifty-six", "1956"), ("nineteen fifty-nine", "1959"),
 ("nineteen fifties", "1950s"), ("nineteen seventies", "1970s"), ("nineteen seventy-eight", "1978"), ("nineteen eighty", "1980"),
 ("nineteen nineties", "1990s"), ("nineteen ninety-three", "1993"), ("nineteen ninety-four", "1994"), ("nineteen ninety-seven", "1997"),
 ("July eighth", "July 8"), ("June fourteenth", "June 14"), ("June fourth", "June 4"), ("June twenty-fourth", "June 24"),
 ("seventy-five miles", "75 miles"), ("six hundred feet", "600 feet"), ("forty-three", "43"), ("sixty-seven", "67"),
 ("forty-seven year", "47-year"), ("Flight Four", "Flight 4"), ("World War Two", "World War II"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="005", title="Roswell, According to the Air Force",
    imgs={k: D + k + ".jpg" for k in ["gao1", "gao2", "gao509", "gaofbi", "fbi1", "fbi2", "h509", "w1", "w1b", "w2a", "w2b", "w3a", "w3b", "w4a", "w4b",
                                       "w5a", "w5b", "cav", "mog46", "moore", "ml307", "cc0", "cc1", "cc2", "cc3", "cc3b", "cc5", "cc6",
                                       "gaodes", "w24a", "ex88", "ex1085", "ex1165", "ex155", "ex1352", "ex1378", "ex1678", "ex1770", "ex2098", "ex1655", "ex965"]},
    credit="Documents: GAO report GAO/NSIAD-95-187 (1995); U.S. Air Force, The Roswell Report: Fact vs. Fiction in the New Mexico Desert (1995) and The Roswell Report: Case Closed (1997). Archival film: U.S. Air Force, Project Excelsior (NARA 342-USAF-33041). B-roll: U.S. Department of Defense and U.S. Department of State via DVIDS (public domain). Appearance of U.S. government visual information does not imply endorsement.",
    shorts=[
        dict(id="s1", lines=[1, 4], hook="THE ARMY SAID<br>[FLYING DISC]"),
        dict(id="s2", lines=[36, 40], hook="FLIGHT 4<br>[NOT RECOVERED]"),
        dict(id="s3", lines=[44, 47], hook="ROSWELL'S<br>[BODIES]?"),
        dict(id="s4", lines=[11, 14], hook="THE RANCHER<br>[DISAGREED]"),
    ],
)
