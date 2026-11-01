# FILE 004 — MKUltra: The Files That Survived
# Format: see episodes/001-navy-videos/episode.py
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

CAP14 = "B-ROLL · U.S. CAPITOL, WASHINGTON, D.C., 2014"
CAP25 = "B-ROLL · STREET NEAR THE U.S. CAPITOL, WASHINGTON, D.C., 2025"
WH14 = "B-ROLL · THE WHITE HOUSE, WASHINGTON, D.C., 2014"
TRE14 = "B-ROLL · U.S. TREASURY BUILDING, WASHINGTON, D.C., 2014"
AIR26 = "B-ROLL · VIEW FROM A U.S. AIR FORCE F-22 OVER WASHINGTON, D.C., 2026"
HEAR = "ACTUAL DOCUMENT · SENATE HEARING \"PROJECT MKULTRA, THE CIA'S PROGRAM OF RESEARCH IN BEHAVIORAL MODIFICATION\" · AUG. 3, 1977"
TURN = "ACTUAL DOCUMENT · ADM. STANSFIELD TURNER, PREPARED STATEMENT · SENATE HEARING, AUG. 3, 1977"
CHURCH = "ACTUAL DOCUMENT · CHURCH COMMITTEE FINAL REPORT, BOOK I (1976) · REPRINTED IN THE 1977 SENATE HEARING"
MEMO77 = "ACTUAL DOCUMENT · CIA MEMO ON NEWLY FOUND MKULTRA FILES, JUNE 22, 1977 · SENATE HEARING RECORD"
IGR = "ACTUAL DOCUMENT · CIA INSPECTOR GENERAL, \"REPORT OF INSPECTION OF MKULTRA,\" JULY 26, 1963 · RELEASED 2019"
IG53 = "ACTUAL DOCUMENT · CIA MEMO FOR THE FILE, \"PROJECT MKULTRA,\" APRIL 21, 1953 · RELEASED 2019"
IGD = "ACTUAL DOCUMENT · DCI ALLEN W. DULLES MEMO APPROVING PROJECT MKULTRA, APRIL 13, 1953 · CIA RELEASE, 2019"
D = "/home/claude/src/img/doc/"
S_CH = "SOURCE: CHURCH COMMITTEE FINAL REPORT, BOOK I (1976), AS REPRINTED IN THE AUG. 3, 1977 SENATE HEARING"
S_TU = "SOURCE: ADM. STANSFIELD TURNER, DIRECTOR OF CENTRAL INTELLIGENCE · SENATE HEARING, AUG. 3, 1977"
S_IG = "SOURCE: CIA INSPECTOR GENERAL, REPORT OF INSPECTION OF MKULTRA, JULY 26, 1963 (CIA RELEASE, 2019)"
US = dict(kicker="WHERE THE FILES POINT", title="Places in the record", bounds=[[-123.5, 30.5], [-70.0, 45.0]],
          points=[dict(ll=[-77.04, 38.90], name="Washington", anchor="end"),
                  dict(ll=[-74.0, 40.71], name="New York", sub="SAFEHOUSE"),
                  dict(ll=[-122.42, 37.77], name="San Francisco", sub="SAFEHOUSE"),
                  dict(ll=[-84.50, 38.04], name="Lexington, Ky.", sub="ADDICTION RESEARCH CENTER", anchor="end")],
          source="SOURCES: CHURCH COMMITTEE, BOOK I; ADM. TURNER, 1977 · MAP: NATURAL EARTH")
MD = dict(kicker="NOVEMBER 1953", title="A meeting in the mountains", bounds=[[-80.2, 37.6], [-73.6, 41.2]],
          points=[dict(ll=[-79.33, 39.51], name="Deep Creek Lake", sub="NOV. 18–19, 1953", color="#F2D04B", anchor="end"),
                  dict(ll=[-77.41, 39.41], name="Camp Detrick", sub="FREDERICK, MD."),
                  dict(ll=[-77.04, 38.90], name="Washington", anchor="end"),
                  dict(ll=[-73.99, 40.75], name="New York", sub="STATLER HOTEL", anchor="end")],
          source="SOURCE: CHURCH COMMITTEE FINAL REPORT, BOOK I (1976) · MAP: NATURAL EARTH · LOCATIONS APPROXIMATE")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("In January nineteen seventy-three, two men at the top of the C I A were about to retire. | The Director, Richard Helms. And the chief of the agency's Technical Services Division, Sidney Gottlieb.",
  [I("h72a", kb="in", focus=[0.5, 0.45], lab=CHURCH)], dict(tag=("CIA", "JANUARY 1973"))),
 ("Helms later told Senate investigators. Gottlieb, he said, came to him and said he thought it would be a good idea if these files were destroyed.",
  [G("quote", q="…he was retiring and that I was retiring and he thought it would be a good idea if {{these files were destroyed.}}",
     who="Richard Helms", role="Former CIA Director · testimony, Sept. 11, 1975", size=56, source=S_CH)], dict(slow=True)),
 ("The files were the records of a program code-named MKUltra. | Staff destroyed them on Gottlieb's verbal orders. Gottlieb testified he was carrying out an order from Helms, and Helms confirmed it.",
  [I("h72a", kb="down", lab=CHURCH)], dict(gap=0.9, sil=True)),
 ("For four years, it looked as if the paper trail was gone for good.",
  [C("dv346026", 2.0, lab=CAP14)], dict(slow=True)),
 ("Then, in nineteen seventy-seven, a C I A employee answering Freedom of Information Act requests went looking in a records center outside Washington. | He found seven boxes. The destruction had missed them.",
  [G("stat", k="FOUND IN A CIA RECORDS CENTER · MARCH 1977", a="7", size=300, b="boxes of MKUltra records", c="filed in the wrong section", source=S_TU)], {}),
 ("What was in those boxes is the closest thing we have to the full story.",
  [I("h8a", kb="in", focus=[0.5, 0.3], lab=TURN)], {}),
 ("Let's open the file.",
  [G("intro", n="004")], dict(gap=0.2)),
 ("",
  [G("title", n="004", t="MKUltra", size=190, sub="The files that survived")], dict(gap=0.4)),

 # ---------------- I. THE CHARTER ----------------
 ("It started with a memo.",
  [G("chapter", n="I", t="The Charter")], {}),
 ("On April third, nineteen fifty-three, Richard Helms, then a senior officer in the C I A's covert operations directorate, sent a proposal to Director Allen Dulles. | Ten days later, Dulles approved it.",
  [I("ig38", kb="in", focus=[0.5, 0.3], lab=IGD)], dict(tag=("CIA", "APRIL 13, 1953"))),
 ("The goal, in the proposal's words, was research to develop a capability in the covert use of biological and chemical materials.",
  [G("quote", q="Research to develop a capability in the {{covert use of biological and chemical materials.}}",
     who="Richard Helms", role="Proposal to DCI Allen Dulles, April 3, 1953", size=62, source=S_CH)], dict(slow=True)),
 ("The C I A later called MKUltra an umbrella project. | Grants to researchers went out under the cover of research foundations, which hid the agency's interest from the researchers' own institutions.",
  [C("dv346120", 1.5, lab=TRE14), C("dv346124", 2.0, lab=WH14)], {}),
 ("From the start, normal rules were waived. Six percent of the research budget of the agency's technical branch could be spent without formal contracts. | Contracts, Helms noted, would reveal government interest.",
  [I("ig38", kb="down", focus=[0.5, 0.65], lab=IGD)], {}),
 ("Researchers in this field, he wrote, are most reluctant to enter into signed agreements of any sort which connect them with this activity.",
  [G("quote", q="…are {{most reluctant to enter into signed agreements}} of any sort which connect them with this activity…",
     who="Richard Helms", role="Proposal to DCI Allen Dulles, 1953", size=58, source=S_CH)], {}),
 ("Ten years later, the C I A's own Inspector General summed up the problem. | The concepts involved in manipulating human behavior, he wrote, are found by many people both within and outside the Agency to be distasteful and unethical.",
  [I("ig2a", kb="in", focus=[0.5, 0.45], lab=IGR)], dict(slow=True, gap=0.8)),

 # ---------------- II. THE TESTS ----------------
 ("So what did MKUltra actually do?",
  [G("chapter", n="II", t="The Tests")], {}),
 ("The Senate's investigators described three phases. First, the search for materials worth studying. Second, laboratory tests on volunteers. | Third, using the materials in normal life settings.",
  [G("list", kicker="MKULTRA", title="Three phases", items=[dict(n="01", t="Search for materials", s="UNIVERSITIES, DRUG FIRMS, HOSPITALS"),
     dict(n="02", t="Laboratory tests", s="VOLUNTEER SUBJECTS"), dict(n="03", t="Normal life settings", s="INCLUDING UNWITTING PEOPLE")], source=S_CH)], {}),
 ("The search ran through standing arrangements with specialists at universities, pharmaceutical houses, hospitals, and private research organizations.",
  [C("dv1026930", 25.5, lab=AIR26), C("dv1026934", 40.0, lab=AIR26)], {}),
 ("One of the first studies ran at a federal center in Lexington, Kentucky, which was then a prison for drug addicts serving sentences. | According to the Senate report, volunteer prisoners were given hallucinogenic drugs. As a reward, they were provided with the drug of their addiction.",
  [I("h74b", kb="in", focus=[0.5, 0.35], lab=CHURCH)], {}),
 ("LSD was one of the materials tested. And the last phase of testing went further. | Undercover officers of the Bureau of Narcotics, acting for the C I A, gave it to unwitting people in normal life settings. People who had never agreed to take part.",
  [I("h74a", kb="in", focus=[0.5, 0.3], lab=CHURCH)], dict(slow=True)),
 ("The Senate report quotes the rationale. Testing under accepted scientific procedures, it said, fails to disclose the full pattern of reactions and attributions that may occur in operational situations.",
  [G("quote", q="…testing of materials under accepted scientific procedures {{fails to disclose the full pattern of reactions}} and attributions that may occur in operational situations.",
     who="CIA rationale", role="As quoted by the Church Committee, 1976", size=50, source=S_CH)], {}),
 ("And a C I A passage quoted in the same report says the effectiveness of the substances on individuals at all social levels, high and low, native American and foreign, is of great significance.",
  [I("h74a", kb="up", focus=[0.5, 0.75], lab=CHURCH)], {}),
 ("In nineteen seventy-seven, the C I A told the Senate that some of the unwitting testing took place in safehouses in San Francisco and New York City.",
  [G("map", **US)], {}),
 ("The Inspector General's report also explains why so little of this can be reconstructed. | Present practice, it says, is to maintain no records of the planning and approval of test programs.",
  [I("ig16a", kb="in", focus=[0.5, 0.5], lab=IGR)], dict(slow=True)),
 ("According to the same report, the people tested were seldom accessible beyond the first hours of the test. In a number of cases, a subject became ill for hours or days.",
  [I("ig16a", kb="down", lab=IGR)], dict(gap=0.9, sil=True)),

 # ---------------- III. DEEP CREEK LAKE ----------------
 ("One test is documented in more detail than any other.",
  [G("chapter", n="III", t="Deep Creek Lake")], {}),
 ("On November eighteenth, nineteen fifty-three, a group of ten scientists from the C I A and the Army's Camp Detrick, in Maryland, met for a review conference at a cabin at Deep Creek Lake.",
  [G("map", **MD)], {}),
 ("One of them was Frank Olson, a civilian employee of the Army, and an expert in aerobiology.",
  [I("h77a", kb="in", focus=[0.5, 0.3], lab=CHURCH)], dict(tag=("DEEP CREEK LAKE, MD.", "NOV. 19, 1953"))),
 ("After dinner on November nineteenth, the group was served a bottle of Cointreau. A C I A officer, Robert Lashbrook, had put LSD in it. Olson received about seventy micrograms. | About twenty minutes later, according to Gottlieb's account, he told the others what they had taken.",
  [I("h79a", kb="in", focus=[0.5, 0.4], lab=CHURCH)], {}),
 ("The Senate report found that neither the chief of the C I A's Technical Services Staff, where Gottlieb worked, nor the head of the covert operations directorate, had specifically authorized that experiment.",
  [I("h78a", kb="down", lab=CHURCH)], {}),
 ("Shortly afterward, according to the report, Olson showed symptoms of paranoia. | With Lashbrook, he went to New York to see a doctor, whose own LSD research had been funded indirectly by the C I A.",
  [C("dv1026934", 15.0, lab=AIR26), C("dv1026930", 33.0, lab=AIR26)], {}),
 ("In the early hours of November twenty-eighth, nineteen fifty-three, while in New York for treatment, Frank Olson fell to his death from a tenth-floor window of the Statler Hotel.",
  [G("stat", k="STATLER HOTEL · NEW YORK CITY", a="NOV. 28, 1953", size=170, b="Frank Olson dies", c="nine days after the Deep Creek Lake experiment", source="SOURCES: CHURCH COMMITTEE, BOOK I, P. 397; PRESIDENT FORD, STATEMENT ON S. 3035, OCT. 12, 1976")], dict(slow=True, gap=1.0, sil=True)),
 ("According to the Senate report, the C I A worked to make sure his family received death benefits. | But it did not tell them the circumstances of his death.",
  [G("quote", q="…did not notify the Olsons of {{the circumstances surrounding his demise.}}", who="Church Committee", role="Final Report, Book I, 1976", size=60, source=S_CH)], {}),
 ("Those details became public twenty-two years later, in nineteen seventy-five, during the investigations by the Rockefeller Commission and the Church Committee.",
  [C("dv346119", 1.5, lab=CAP14), C("dv346026", 14.0, lab=CAP14)], {}),
 ("On July twenty-first, nineteen seventy-five, President Gerald Ford met Olson's widow and their three children. | According to the White House summary of the meeting, he apologized on behalf of the U S government.",
  [C("dv346124", 14.0, lab=WH14), C("dv346124", 30.0, lab=WH14)], {}),
 ("In nineteen seventy-six, Ford signed a private bill paying Olson's survivors seven hundred fifty thousand dollars. | In his statement, he said the drug would appear to have been a proximate cause of his death.",
  [G("stat", k="PRIVATE LAW FOR OLSON'S SURVIVORS · OCT. 1976", a="$750,000", size=230, b="paid by act of Congress", c="President Ford: the drug \"would appear to have been a proximate cause of his death\"",
     source="SOURCE: GERALD R. FORD LIBRARY, WHITE HOUSE RECORDS ON S. 3035 (1976)")], {}),
 ("His family later came to doubt the official account. In two thousand twelve, according to the Baltimore Sun, his sons sued, claiming that their father had been killed. | That is their claim, not an established finding.",
  [C("dv346120", 25.0, lab=TRE14), C("dv1026934", 23.0, lab=AIR26)], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE INSPECTOR ----------------
 ("Olson's death did not end the testing.",
  [G("chapter", n="IV", t="The Inspector")], {}),
 ("In nineteen sixty-three, the Inspector General learned of the unwitting tests during a survey of the technical division. | In May, the head of the covert operations directorate, by then Richard Helms, told him he had briefed the Director. According to the Inspector General, Helms said the Director indicated no disagreement, and therefore the testing will continue.",
  [I("h84a", kb="in", focus=[0.5, 0.35], lab=CHURCH)], {}),
 ("The Inspector General recommended ending it. Following his report, the project was suspended.",
  [I("ig1", kb="in", focus=[0.5, 0.3], lab=IGR)], {}),
 ("Helms pushed back. In December nineteen sixty-three, he argued that testing on unwitting people was the only realistic method of maintaining the capability, because the operational targets will certainly be unwitting.",
  [G("quote", q="…{{the only realistic method of maintaining the capability,}} considering the intended operational use of materials to influence human behavior as the operational targets will certainly be unwitting.",
     who="Richard Helms", role="Memo to the Deputy Director of Central Intelligence, Dec. 17, 1963", size=46, source=S_CH)], {}),
 ("Otherwise, he warned, the program would only be pro forma, resulting in a false sense of accomplishment and readiness.",
  [I("h84b", kb="in", focus=[0.5, 0.45], lab=CHURCH)], {}),
 ("The Senate found that the covert testing in the United States was halted in nineteen sixty-three. By then, the Inspector General had counted one hundred forty-four projects related to the control of human behavior. | According to the C I A, MKUltra itself ended in nineteen sixty-four.",
  [G("timeline", kicker="PROJECT MKULTRA", title="Eleven years, then silence", active=3,
     events=[dict(y="APR 1953", t="Dulles approves MKUltra"), dict(y="NOV 1953", t="Olson experiment"),
             dict(y="1963", t="Inspector General report"), dict(y="1964", t="Program ends (CIA account)")],
     source="SOURCES: CHURCH COMMITTEE, BOOK I; ADM. TURNER, 1977; CIA IG REPORT, 1963")], {}),
 ("And even then, he wrote, the files were notably incomplete.",
  [G("quote", q="Files are {{notably incomplete,}} poorly organized, and lacking in evaluative statements…",
     who="CIA Inspector General", role="Report on MKULTRA, 1963 · as quoted by the Church Committee", size=60, source=S_CH)], dict(gap=0.9, sil=True)),

 # ---------------- V. DESTROYED ----------------
 ("Which brings us back to January nineteen seventy-three.",
  [G("chapter", n="V", t="Destroyed")], {}),
 ("Helms explained the decision this way. There had been relationships with outsiders. | So they got rid of the files, in his words, so that anybody who assisted us in the past would not be subject to follow-up or questions, embarrassment, if you will.",
  [G("quote", q="…so that {{anybody who assisted us in the past}} would not be subject to follow-up or questions, embarrassment, if you will.",
     who="Richard Helms", role="Testimony, Sept. 11, 1975", size=56, source=S_CH)], dict(slow=True)),
 ("To do it, the agency waived its own rule on retiring old records. | That rule said the heart of the judgment is to ensure that the complete story can be reconstructed in later years.",
  [I("h87a", kb="in", focus=[0.5, 0.4], lab=CHURCH)], {}),
 ("According to the Church Committee, the destruction made it impossible to determine the full range of the program. | It also kept the C I A from locating and providing medical assistance to the people who had been its subjects.",
  [G("quote", q="The destruction also {{prevented the CIA from locating and providing medical assistance}} to the individuals who were subjects in the program.",
     who="Church Committee", role="Final Report, Book I, 1976", size=52, source=S_CH)], {}),
 ("At least one of Gottlieb's assistants protested against the destruction, according to the committee. | It went ahead anyway.",
  [I("h87a", kb="down", lab=CHURCH)], dict(gap=0.9, sil=True)),

 # ---------------- VI. SEVEN BOXES ----------------
 ("Then came the requests.",
  [G("chapter", n="VI", t="Seven Boxes")], {}),
 ("Several Freedom of Information Act requests had come in. One was from a researcher named John Marks. | Working through them, a C I A employee searched every file the responsible branch had any conceivable connection with.",
  [I("h106a", kb="in", focus=[0.5, 0.5], lab=MEMO77)], {}),
 ("Very late in March nineteen seventy-seven, he found the seven boxes. | They had been sent to the Retired Records Center in nineteen seventy by the branch's Budget and Fiscal Section, not with the project files. Why, the C I A said, is not known.",
  [I("h9a", kb="in", focus=[0.5, 0.5], lab=TURN)], {}),
 ("As a result, in the words of C I A Director Stansfield Turner, the material escaped retrieval and destruction in nineteen seventy-three.",
  [G("quote", q="…the material {{escaped retrieval and destruction in 1973}} by the then-retiring Director of the Office…",
     who="Adm. Stansfield Turner", role="Director of Central Intelligence · Aug. 3, 1977", size=58, source=S_TU)], {}),
 ("On August third, nineteen seventy-seven, Turner laid out what was inside, before two Senate panels.",
  [I("h1", kb="in", focus=[0.5, 0.3], lab=HEAR), C("dv346026", 16.0, lab=CAP14)], dict(tag=("U.S. SENATE", "AUG. 3, 1977"))),
 ("They were finance folders. Mostly approvals for advance of funds, vouchers, and accountings. | But the paperwork named names.",
  [I("h9b", kb="in", focus=[0.5, 0.3], lab=TURN)], {}),
 ("In the recovered files, there were one hundred forty-nine MKUltra subprojects. The files named one hundred eighty-five researchers and assistants from outside the government. And eighty institutions.",
  [G("stat", k="RECOVERED MKULTRA FINANCE FILES · 1977", a="149", size=300, b="subprojects", c="185 outside researchers and assistants · 80 institutions", source=S_TU)], {}),
 ("Forty-four colleges or universities. Fifteen research foundations, or chemical and pharmaceutical companies. Twelve hospitals or clinics. | And three penal institutions.",
  [G("list", kicker="AMONG THE 80 INSTITUTIONS", title="Named in the recovered files", items=[dict(n="44", t="Colleges or universities"),
     dict(n="15", t="Research foundations, chemical or drug companies"), dict(n="12", t="Hospitals or clinics"), dict(n="3", t="Penal institutions")], source=S_TU)], {}),
 ("Most of the people and institutions involved, Turner said, are not aware of Agency sponsorship.",
  [I("h11a", kb="in", focus=[0.5, 0.5], lab=TURN)], {}),
 ("One subproject sent three hundred seventy-five thousand dollars to the building fund of a private medical institution, through an intermediary, so it looked like a private gift. | Federal matching funds followed.",
  [I("h11a", kb="down", lab=TURN)], {}),
 ("Senator Edward Kennedy summed it up at the hearing. The Central Intelligence Agency drugged American citizens without their knowledge or consent.",
  [G("quote", q="The Central Intelligence Agency {{drugged American citizens without their knowledge or consent.}}",
     who="Sen. Edward M. Kennedy", role="Senate hearing, Aug. 3, 1977", size=60, source="SOURCE: SENATE HEARING ON PROJECT MKULTRA, AUG. 3, 1977")], dict(slow=True, gap=0.9, sil=True)),

 # ---------------- VII. WHAT IT PROVES ----------------
 ("So, what does this file actually prove?",
  [G("chapter", n="VII", t="What It Proves")], {}),
 ("It proves the C I A ran a program, approved by its Director, to research drugs and other ways to influence human behavior. | And that it tested LSD on Americans who did not know.",
  [I("ig38", kb="out", focus=[0.5, 0.4], lab=IGD)], {}),
 ("It proves that at least one man died after being given LSD in a C I A experiment, and that his family was not told the circumstances for twenty-two years.",
  [I("h79a", kb="out", focus=[0.5, 0.4], lab=CHURCH)], {}),
 ("And it proves the main records were destroyed on purpose, and that some survived only because they were filed in the wrong place.",
  [G("timeline", kicker="THE PAPER TRAIL", title="From destroyed to released", active=3,
     events=[dict(y="1963", t="IG: no records of test approvals"), dict(y="JAN 1973", t="MKUltra files destroyed"),
             dict(y="1975", t="Olson case made public"), dict(y="1977", t="Seven boxes found")],
     source="SOURCES: CIA IG REPORT, 1963; CHURCH COMMITTEE, BOOK I; ADM. TURNER, 1977")], {}),
 ("What it doesn't prove matters just as much. The surviving files are mostly financial, with few reports on results. | Popular claims about programmed assassins, or specific famous people, do not appear in these documents. Theories remain theories, until a document says otherwise.",
  [C("dv346119", 8.0, lab=CAP14), C("dv1026930", 41.0, lab=AIR26)], dict(slow=True)),
 ("Every secret has a release date. MKUltra's records were supposed to have none. Seven boxes in the wrong section changed that.",
  [I("h1", kb="out", focus=[0.5, 0.35], lab=HEAR)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments. We read every one.",
  [C("dv346026", 20.0, lab=CAP14)], {}),
 ("Next time: Roswell, and what the Air Force's own reports actually say.",
  [G("end", n="004", next="Roswell, According to the Air Force")], dict(gap=2.5)),
]

PRON = [("MKUltra's", "M K Ultra's"), ("MKUltra", "M K Ultra"), ("LSD", "L S D"), ("Cointreau", "Kwan-troh"), ("Lashbrook", "Lash brook"),
        ("aerobiology", "aero biology"), ("Detrick", "Detrick"), ("Statler", "Statler"), ("pro forma", "pro forma"),
        ("Gottlieb's", "Gott leeb's"), ("Gottlieb", "Gott leeb"), ("Helms's", "Helmses"), ("safehouses", "safe houses"), ("U S government", "U S government")]

DISPLAY = [
 ("C I A", "CIA"), ("U S government", "U.S. government"), ("MKUltra", "MKUltra"),
 ("nineteen seventy-three", "1973"), ("nineteen seventy-seven", "1977"), ("nineteen seventy-five", "1975"), ("nineteen seventy-six", "1976"),
 ("nineteen seventy", "1970"), ("nineteen fifty-three", "1953"), ("nineteen sixty-three", "1963"), ("nineteen sixty-four", "1964"),
 ("two thousand twelve", "2012"), ("April third", "April 3"), ("November eighteenth", "November 18"), ("November nineteenth", "November 19"),
 ("November twenty-eighth", "November 28"), ("July twenty-first", "July 21"), ("August third", "August 3"),
 ("seven hundred fifty thousand dollars", "$750,000"), ("three hundred seventy-five thousand dollars", "$375,000"),
 ("one hundred forty-nine", "149"), ("one hundred eighty-five", "185"), ("one hundred forty-four", "144"), ("seventy micrograms", "70 micrograms"),
 ("Forty-four colleges", "44 colleges"), ("Fifteen research", "15 research"), ("Twelve hospitals", "12 hospitals"), ("three penal", "3 penal"),
 ("eighty institutions", "80 institutions"), ("Six percent", "Six percent"), ("twenty-two years", "22 years"), ("tenth-floor", "tenth-floor"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="004", title="MKUltra: The Files That Survived",
    imgs={k: D + k + ".jpg" for k in ["h1", "h8a", "h9a", "h9b", "h11a", "h72a", "h74a", "h74b", "h77a", "h78a", "h79a", "h84a", "h84b", "h87a", "h106a",
                                       "ig1", "ig2a", "ig16a", "ig38"]},
    credit="Documents: Senate hearing on Project MKULTRA (Aug. 3, 1977), incl. Church Committee Final Report, Book I; CIA Inspector General report on MKULTRA (1963, CIA release 2019). B-roll: U.S. Department of Defense via DVIDS (public domain). Appearance of U.S. government visual information does not imply endorsement.",
    shorts=[
        dict(id="s1", lines=[1, 5], hook="THE CIA [DESTROYED]<br>THESE FILES"),
        dict(id="s2", lines=[51, 55], hook="7 BOXES THE<br>CIA [MISSED]"),
        dict(id="s3", lines=[20, 22], hook="[UNWITTING]<br>TEST SUBJECTS"),
        dict(id="s4", lines=[28, 32], hook="THE NIGHT AT<br>[DEEP CREEK LAKE]"),
    ],
)
