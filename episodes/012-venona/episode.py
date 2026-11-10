# FILE 012 — VENONA: How Codebreakers Caught Stalin's Atomic Spies
# Format: see episodes/001-navy-videos/episode.py
# Documents: NSA VENONA translations, scans from the archive.org mirror of the NSA release (collection nsia-venona).
# NOTE on clip timing: all times are in the original DVIDS files (no trims).
#  dv395453 (USAF "Yesterday's Air Force", 2015, 1024x576): museum shots only as video; the 1945 Trinity film is used as stills (img/trin_*.jpg).
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
H = "/home/claude/src/img/"

HALL = "ACTUAL DOCUMENT · VENONA: KGB NEW YORK TO MOSCOW, NO. 1585, NOV. 12, 1944 · NSA TRANSLATION"
HALLN = "ACTUAL DOCUMENT · VENONA NO. 1585 (NOV. 12, 1944), TRANSLATORS' COMMENTS · NSA"
LIST = "ACTUAL DOCUMENT · VENONA: NEW YORK TO MOSCOW, NO. 1699, DEC. 2, 1944 · NSA TRANSLATION (1952)"
FUCHS = "ACTUAL DOCUMENT · VENONA: NEW YORK TO MOSCOW, NO. 1606, NOV. 1944 · NSA TRANSLATION (1957)"
LIB = "ACTUAL DOCUMENT · VENONA: NEW YORK TO MOSCOW, NO. 1600, NOV. 14, 1944 · NSA REISSUE"
ETH = "ACTUAL DOCUMENT · VENONA: NEW YORK TO MOSCOW, NO. 1657, NOV. 27, 1944 · NSA REISSUE (1975)"
TINA = "ACTUAL DOCUMENT · VENONA: MOSCOW TO LONDON, SEPT. 16, 1945 · NSA TRANSLATION (VIA DVIDS)"
GARD = "PHOTO · MEREDITH GARDNER (FAR LEFT) WITH ARMY SIGNAL INTELLIGENCE SERVICE CRYPTANALYSTS, 1940s"
TRIN = "ARCHIVAL FILM STILL · TRINITY TEST, NEW MEXICO, JULY 1945 · AS SHOWN IN A USAF VIDEO (2015)"
PLAQ = "PHOTO · TRINITY SITE MARKER, WHITE SANDS MISSILE RANGE, NEW MEXICO, 2017"
OBEL = "PHOTO · TRINITY SITE OPEN HOUSE, WHITE SANDS MISSILE RANGE, NEW MEXICO, 2016"
FATP = "PHOTO · REPLICA \"FAT MAN\" BOMB CASING, TRAVIS AFB HERITAGE CENTER, CALIFORNIA (USAF PHOTO)"
FATV = "B-ROLL · \"FAT MAN\"-TYPE BOMB CASING ON DISPLAY, NATIONAL MUSEUM OF THE USAF (USAF VIDEO, 2015)"
BOCK = "B-ROLL · B-29 \"BOCKSCAR\", NATIONAL MUSEUM OF THE U.S. AIR FORCE, OHIO (USAF VIDEO, 2015)"
B29 = "B-ROLL · B-29 \"DOC\", A RESTORED WWII BOMBER, McCONNELL AFB, KANSAS, 2026"
FBI = "B-ROLL · J. EDGAR HOOVER FBI BUILDING, WASHINGTON, D.C., 2025"
FBIC = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C. (FBI B-ROLL, 2025)"
NYC = "B-ROLL · AERIAL VIEW OF BROOKLYN, NEW YORK, 2025"
BKN = "B-ROLL · BROOKLYN, NEW YORK, 2025"
CAP = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C."
PENN = "B-ROLL · AVENUE LEADING TO THE U.S. CAPITOL, WASHINGTON, D.C."
TREAS = "B-ROLL · THE TREASURY BUILDING, WASHINGTON, D.C."
F22 = "B-ROLL · WASHINGTON, D.C., SEEN FROM AN F-22 COCKPIT, 2026"

S_ARMY46 = "SOURCE: U.S. ARMY INTELLIGENCE CENTER OF EXCELLENCE, \"SIS UNCOVERS SOVIET INFILTRATION OF MANHATTAN PROJECT\" (2024)"
S_ARMY95 = "SOURCE: U.S. ARMY INTELLIGENCE CENTER OF EXCELLENCE, \"VENONA OFFICIALLY RELEASED TO THE PUBLIC\" (2026)"
S_ALM = "SOURCE: NSA, CRYPTOLOGIC ALMANAC 50TH ANNIVERSARY SERIES, \"VENONA: AN OVERVIEW\""
S_STEURY = "SOURCE: D. P. STEURY, \"HOW THE CIA MISSED STALIN'S BOMB,\" STUDIES IN INTELLIGENCE 49:1 (2005)"
S_NSA18 = "SOURCE: NSA, \"A HIGHLY CONTROVERSIAL CASE OF ESPIONAGE: A SUMMARY\" (JUNE 19, 2018)"
S_BW = "SOURCE: R. L. BENSON & M. WARNER, EDS., VENONA: SOVIET ESPIONAGE AND THE AMERICAN RESPONSE (NSA/CIA, 1996)"
S_FBI = "SOURCE: FBI, \"ATOM SPY CASE/ROSENBERGS\" (FBI.GOV HISTORY)"

LINES = [
 # ---------------- COLD OPEN ----------------
 ("How did America catch Stalin's atomic spies? | Partly, by reading their mail. | This is one of the telegrams.",
  [I("hall_head", kb="in", focus=[0.5, 0.5], lab=HALL)], dict(tag=("NEW YORK", "NOVEMBER 12, 1944"))),
 ("In November nineteen forty-four, the K G B in New York sent Moscow a coded message about a nineteen-year-old American physicist.",
  [I("hall_19", kb="in", focus=[0.62, 0.45], lab=HALL)], {}),
 ("Theodore Hall. | The son of a furrier. | A graduate of Harvard.",
  [I("hall_19", kb="in", focus=[0.35, 0.5], lab=HALL)], dict(slow=True)),
 ("He was in charge of a group at a place the telegram calls Camp Two. | The translators' notes identify it. | Los Alamos.",
  [I("hall_camp", kb="in", focus=[0.4, 0.5], lab=HALL), I("hall_notes", kb="in", focus=[0.4, 0.55], lab=HALLN)], {}),
 ("And he had handed over a report about the camp, naming the key personnel employed on ENORMOUS. | The K G B's cover name for the Manhattan Project.",
  [I("hall_camp", kb="in", focus=[0.65, 0.6], lab=HALL), I("hall_notes", kb="down", focus=[0.5, 0.75], lab=HALLN)], {}),
 ("The Soviet system, the Army's historians write, was widely considered unbreakable. | U S Army codebreakers broke into it anyway.",
  [I("gardner", kb="in", focus=[0.3, 0.5], lab=GARD)], {}),
 ("This is VENONA. | How Army codebreakers helped expose the spies inside the atomic bomb project. | And why the nineteen-year-old in this telegram was never charged.",
  [I("hall_full", kb="in", focus=[0.5, 0.3], lab=HALL), I("trin_b", kb="in", focus=[0.5, 0.4], lab=TRIN)], {}),
 ("Let's open the file.",
  [G("intro", n="012")], dict(gap=0.2)),
 ("",
  [G("title", n="012", t="VENONA", size=170, sub="How Codebreakers Helped Catch Stalin's Atomic Spies")], dict(gap=0.4)),

 # ---------------- I. THE BOXES ----------------
 ("It began with stacks of paper nobody could read.",
  [G("chapter", n="I", t="The Boxes")], {}),
 ("As early as nineteen thirty-nine, according to the Army's historians, the Army had begun collecting encrypted Soviet telegrams sent between Moscow and its intelligence offices in New York, Washington and other American cities.",
  [C("dv952451", 49.0, lab=NYC), C("dv346026", 4.0, lab=CAP)], {}),
 ("As they came in, they were put in storage at Arlington Hall, Virginia.",
  [C("dv346119", 14.0, lab=PENN)], {}),
 ("On February first, nineteen forty-three, Colonel Carter Clarke, of the Army's Military Intelligence Division, ordered them examined. | He feared they would reveal that the Soviet Union and Germany were secretly negotiating a separate peace.",
  [C("dv346120", 3.0, lab=TREAS), C("dv1026930", 20.0, lab=F22)], dict(tag=("ARLINGTON HALL, VIRGINIA", "FEBRUARY 1, 1943"))),
 ("The job went first to Gene Grabeel. | She was twenty-three, a schoolteacher who had been hired just six weeks earlier.",
  [I("hall_head", kb="in", focus=[0.5, 0.5], lab=HALL)], {}),
 ("The traffic, the Army found, used five separate Soviet systems.",
  [G("list", kicker="VENONA · FIVE SOVIET SYSTEMS", title="Who was sending",
     items=[dict(t="Soviet trading companies"), dict(t="The Foreign Ministry"), dict(t="The KGB", s="STATE INTELLIGENCE"),
            dict(t="The GRU", s="MILITARY INTELLIGENCE"), dict(t="Naval intelligence")], source=S_ARMY46)], dict(slow=True)),
 ("The most valuable, the N S A says, would turn out to be the secret agents' traffic. | The K G B and the two military services.",
  [I("tina", kb="in", focus=[0.5, 0.35], lab=TINA)], dict(gap=0.9, sil=True)),

 # ---------------- II. THE MISTAKE ----------------
 ("The system had been built so that this could never be read.",
  [G("chapter", n="II", t="The Mistake")], {}),
 ("A clerk looked up each word in a code book, which turned it into a four-digit group. | The numbers were converted into five-digit figures. | Then a second set of numbers was added on top. | The key.",
  [G("list", kicker="HOW A VENONA MESSAGE WAS ENCIPHERED", title="Three layers",
     items=[dict(n="01", t="Code book", s="WORD → 4-DIGIT GROUP"), dict(n="02", t="Converted", s="→ 5-DIGIT FIGURES"),
            dict(n="03", t="Key added", s="FROM A ONE-TIME PAD")], source=S_ARMY46)], {}),
 ("The key came from a one-time pad. | Pages of random numbers, each page never to be used again.",
  [I("hall_head", kb="in", focus=[0.75, 0.6], lab=HALL)], {}),
 ("But the pads were used again. | Under wartime pressure, according to an N S A history, the Soviet factory that made the K G B's pads produced about thirty-five thousand pages of duplicate key.",
  [G("stat", k="NSA · VENONA: AN OVERVIEW", a="35,000", to=35000, size=280, b="pages of duplicate key",
     c="a one-time pad, printed more than once", source=S_ALM)], dict(slow=True)),
 ("Duplicate pages meant that some messages shared the same key. | In October nineteen forty-three, a team under Lieutenant Richard Hallock found the first clues.",
  [I("list_head", kb="in", focus=[0.5, 0.6], lab=LIST)], {}),
 ("In nineteen forty-four, the N S A says, Genevieve Feinstein found a way to spot the messages that shared a key. | According to the Army's historians, she had made the first break into Japan's PURPLE diplomatic cipher, in nineteen forty.",
  [I("gardner", kb="out", focus=[0.5, 0.5], lab=GARD)], {}),
 ("Even then, the work was painfully slow. | Of the many thousands of messages sent from nineteen forty to nineteen forty-eight, the N S A says, only about three thousand were ever even partially read.",
  [G("stat", k="NSA · VENONA MESSAGES, 1940-1948", a="~3,000", size=280, b="even partially read and translated",
     c="out of many thousands sent", source=S_ALM)], dict(gap=0.9, sil=True)),

 # ---------------- III. THE LIST ----------------
 ("The man who made the messages talk was a linguist.",
  [G("chapter", n="III", t="The List")], {}),
 ("Meredith Gardner had taught German at a university in Ohio. | In the Army, he taught himself Japanese in three months. | After the war, he taught himself Russian, and began rebuilding the K G B's code book.",
  [I("gardner", kb="in", focus=[0.15, 0.45], lab=GARD), C("dv346120", 20.0, lab=TREAS)], {}),
 ("On December twentieth, nineteen forty-six, he broke into a K G B message sent to Moscow two years earlier.",
  [I("list_head", kb="in", focus=[0.4, 0.25], lab=LIST)], dict(tag=("ARLINGTON HALL", "DECEMBER 20, 1946"))),
 ("It contained a list of scientists working on the Manhattan Project.",
  [I("list_names", kb="in", focus=[0.5, 0.5], lab=LIST)], {}),
 ("One New York message of December nineteen forty-four, in its N S A translation, lists them by name. | Hans Bethe. | Enrico Fermi. | Ernest Lawrence. | Edward Teller.",
  [I("list_names", kb="right", focus=[0.5, 0.5], lab=LIST)], dict(slow=True)),
 ("According to the Army's historians, that discovery proved the Manhattan Project had been infiltrated by Soviet spies.",
  [C("dv395453", 136.9, lab=FATV)], {}),
 ("In late summer nineteen forty-seven, the Army cautiously told the F B I. | And from October nineteen forty-eight, an F B I agent, Robert Lamphere, worked full time as the Bureau's liaison to the project, alongside Gardner. | The decrypts also helped confirm the story of Elizabeth Bentley, a former courier for Soviet intelligence, whose confessions had been doubted.",
  [C("dv974123", 30.9, lab=FBI), C("dv974123", 18.7, lab=FBIC), I("gardner", kb="out", focus=[0.5, 0.5], lab=GARD)], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE BOMB ----------------
 ("In nineteen forty-nine, time ran out.",
  [G("chapter", n="IV", t="The Bomb")], {}),
 ("By nineteen forty-eight, the C I A's analysts had a date in mind for the first Soviet atomic bomb. | Earliest possible, mid-nineteen fifty. | Most probable, mid-nineteen fifty-three.",
  [G("stat", k="CIA ESTIMATE · FIRST SOVIET ATOMIC BOMB", a="MID-1953", size=240, b="\"the most probable date\"",
     c="earliest possible: mid-1950", source=S_STEURY)], dict(slow=True)),
 ("According to a C I A history, a report sent out on August twenty-fourth, nineteen forty-nine, still gave that projection.",
  [C("dv346026", 14.0, lab=CAP)], {}),
 ("Five days later, the Soviet Union tested its first atomic bomb.",
  [G("stat", k="FIRST SOVIET ATOMIC TEST", a="AUG. 29, 1949", size=190, b="years ahead of the estimate", source=S_STEURY)], dict(slow=True)),
 ("An American plane found out. | According to the Air Force, a B twenty-nine flying between Alaska and Japan, with a particle sampler on board, picked up debris from the test.",
  [C("dv1027235", 23.2, lab=B29), C("dv1027235", 39.6, lab=B29)], {}),
 ("On September twenty-third, President Truman announced that the United States had evidence of an atomic explosion in the Soviet Union.",
  [C("dv346119", 14.0, lab=PENN)], dict(tag=("WASHINGTON, D.C.", "SEPTEMBER 23, 1949"))),
 ("The Americans had built their bomb in secret, at Los Alamos.",
  [I("trin_a", kb="in", focus=[0.5, 0.4], lab=TRIN), I("trin_b", kb="in", focus=[0.6, 0.4], lab=TRIN)], {}),
 ("Now the question was who had carried its secrets out. | And the answers were already sitting in the old messages.",
  [I("plaque", kb="in", focus=[0.5, 0.4], lab=PLAQ)], dict(gap=0.9, sil=True)),

 # ---------------- V. CHARLES ----------------
 ("The first name to fall was a physicist.",
  [G("chapter", n="V", t="Charles")], {}),
 ("In nineteen forty-nine, two cover names in the messages, CHARLES and REST, were identified as Klaus Fuchs. | One message, the official VENONA history says, quoted a paper he had written.",
  [I("fuchs_notes", kb="in", focus=[0.5, 0.6], lab=FUCHS)], {}),
 ("Fuchs, the F B I says, was a member of a British team working with the Americans on the atom bomb at Los Alamos.",
  [I("trin_a", kb="in", focus=[0.4, 0.5], lab=TRIN)], {}),
 ("This message, from November nineteen forty-four, shows the K G B trying to reach him. | A contact called ARNO had visited CHARLES's sister.",
  [I("fuchs_cable", kb="in", focus=[0.5, 0.25], lab=FUCHS)], {}),
 ("CHARLES, it reports, had not left for the ISLAND, the K G B's word for Great Britain. | He was at Camp Number Two. | And he had promised to come on leave for Christmas.",
  [I("fuchs_camp", kb="in", focus=[0.5, 0.5], lab=FUCHS)], dict(slow=True)),
 ("British authorities questioned Fuchs. | On January twenty-fourth, nineteen fifty, he confessed.",
  [I("fuchs_cable", kb="out", focus=[0.5, 0.5], lab=FUCHS)], dict(tag=("BRITAIN", "JANUARY 24, 1950"))),
 ("He was arrested on February second, and sentenced to fourteen years. | The maximum under Britain's Official Secrets Act. | According to accounts cited in the official VENONA history, Moscow had begun advising American agents who had dealt with Fuchs that they might have to flee the country, through Mexico.",
  [G("stat", k="KLAUS FUCHS · 1950", a="14 YEARS", size=230, b="the maximum under the Official Secrets Act", source=S_FBI)], {}),
 ("ARNO was the next link. | The F B I identified him as Harry Gold, a Philadelphia chemist, and arrested him in May nineteen fifty.",
  [I("fuchs_notes", kb="in", focus=[0.35, 0.65], lab=FUCHS), C("dv974123", 60.6, lab=FBI)], dict(gap=0.9, sil=True)),

 # ---------------- VI. LIBERAL ----------------
 ("The trail led back to Los Alamos.",
  [G("chapter", n="VI", t="Liberal")], {}),
 ("David Greenglass, the F B I says, was an Army enlisted man assigned to Los Alamos in nineteen forty-four and forty-five. | And a Soviet agent.",
  [I("fatman", kb="up", focus=[0.5, 0.4], lab=FATP)], {}),
 ("In VENONA, he had a cover name too. | This message from November fourteenth says his wife, cover name OSA, had agreed to help draw him in, with a view to ENORMOUS.",
  [I("osa", kb="in", focus=[0.5, 0.5], lab=LIB)], {}),
 ("Before she left, it says, a man called LIBERAL would carry out two briefing meetings. | The translators' notes name him. | Julius Rosenberg.",
  [I("osa", kb="in", focus=[0.75, 0.75], lab=LIB), I("lib_notes", kb="in", focus=[0.4, 0.4], lab=LIB)], {}),
 ("The N S A calls LIBERAL the most active spy, at least as seen in VENONA messages.",
  [G("quote", q="The most active spy, at least as seen in VENONA messages, {{was LIBERAL.}}",
     who="National Security Agency", role="Summary of the Rosenberg case · 2018", size=66, source=S_NSA18)], {}),
 ("Two weeks later, New York sent Moscow a description of LIBERAL's wife. | First name, Ethel. | Twenty-nine years old. | Knows about her husband's work.",
  [I("ethel", kb="in", focus=[0.5, 0.45], lab=ETH)], dict(slow=True)),
 ("The N S A's own summary is careful. | The decrypts, it says, show that Ethel was a loyal communist, and that she knew about her husband's espionage activities. | They do not suggest she committed any crimes worthy of capital punishment.",
  [G("quote", q="The decrypts {{do not suggest she committed any crimes worthy of capital punishment.}}",
     who="National Security Agency", role="On Ethel Rosenberg · 2018", size=64, source=S_NSA18)], dict(slow=True)),
 ("On March twenty-ninth, nineteen fifty-one, a jury found Julius and Ethel Rosenberg guilty. | On June nineteenth, nineteen fifty-three, both were executed at Sing Sing Prison, in New York.",
  [G("timeline", kicker="THE ATOM SPY CASE", title="From decrypt to verdict",
     events=[dict(y="DEC 1946", t="Gardner reads the scientists' list"), dict(y="AUG 1949", t="First Soviet atomic test"),
             dict(y="JAN 1950", t="Fuchs confesses"), dict(y="MAY 1950", t="Gold arrested"),
             dict(y="MAR 1951", t="Rosenbergs convicted"), dict(y="JUN 1953", t="Rosenbergs executed")],
     source="SOURCES: U.S. ARMY ICoE (2024); STUDIES IN INTELLIGENCE (2005); BENSON & WARNER (1996); FBI")], {}),
 ("Greenglass testified against his sister and brother-in-law. | He served about ten years in prison. | Gold was released after fifteen.",
  [C("dv974123", 100.9, lab=FBI)], {}),
 ("And the codebreakers' work stayed out of the courtroom. | Under an agreement, the N S A says, the decrypts could be used to stimulate investigations. | But they were never to be used in court, or otherwise made public.",
  [G("quote", q="…could be used to stimulate investigations… {{but never were to be used in court or otherwise made public.}}",
     who="National Security Agency", role="On the VENONA decrypts · 2018", size=60, source=S_NSA18)], dict(gap=0.9, sil=True)),

 # ---------------- VII. YOUNGSTER ----------------
 ("Which brings us back to the nineteen-year-old.",
  [G("chapter", n="VII", t="Youngster")], {}),
 ("In the telegram, he gave the K G B more than a report. | He left his photograph, and agreed on a place for meeting. | The K G B's contact described him as having an exceptionally keen mind and a broad outlook.",
  [I("hall_full", kb="in", focus=[0.5, 0.75], lab=HALL)], {}),
 ("In other VENONA messages, he had a cover name. | MLAD. | Russian for Youngster.",
  [I("hall_full", kb="down", focus=[0.5, 0.4], lab=HALL)], {}),
 ("The F B I matched the name to Theodore Hall. | Special agents questioned him in nineteen fifty-one. | But he was never prosecuted.",
  [C("dv974123", 110.0, lab=FBI), C("dv974123", 121.0, lab=FBI)], {}),
 ("The likely reason is spelled out in the official VENONA history, published by the N S A and the C I A in nineteen ninety-six. | A case, it says, probably could not have been made without revealing the codebreaking program.",
  [G("quote", q="…a case could not have been made {{without revealing AFSA's program.}}",
     who="Benson & Warner, eds.", role="VENONA: Soviet Espionage and the American Response · NSA/CIA, 1996", size=66, source=S_BW)], dict(slow=True)),
 ("The program had already been betrayed. | According to the Army's historians, in nineteen forty-eight an Army Security Agency employee named William Weisband revealed the effort to the Soviets.",
  [C("dv346119", 30.0, lab=PENN)], {}),
 ("Weisband always denied spying, and the government never prosecuted him for it. | After nineteen forty-eight, no new messages were collected.",
  [C("dv1026930", 36.0, lab=F22)], {}),
 ("But the work on the old ones continued. | At the Armed Forces Security Agency, and from nineteen fifty-two, at the new National Security Agency.",
  [I("tina", kb="down", focus=[0.5, 0.6], lab=TINA)], dict(gap=0.9, sil=True)),

 # ---------------- VIII. THE RELEASE ----------------
 ("VENONA ran until October first, nineteen eighty.",
  [G("chapter", n="VIII", t="The Release")], {}),
 ("Even then, it stayed secret. | The first public mention of the name, the Army says, came in nineteen eighty-six, in a book by the former F B I agent Robert Lamphere.",
  [C("dv974123", 172.4, lab=FBI)], {}),
 ("On July eleventh, nineteen ninety-five, at a ceremony at the C I A, the N S A, F B I and C I A released the first forty-nine VENONA translations. | Copies went to the National Archives, the Library of Congress, and the N S A's National Cryptologic Museum.",
  [I("tina", kb="in", focus=[0.4, 0.3], lab=TINA)], dict(tag=("LANGLEY, VIRGINIA", "JULY 11, 1995"))),
 ("Over the next two years, five more releases followed. | About twenty-nine hundred messages in all. | According to the Army's historians, they exposed nearly three hundred and fifty American members of the Communist Party who spied for the Soviet Union.",
  [G("stat", k="VENONA RELEASES · 1995-1997", a="~2,900", size=280, b="Soviet messages made public",
     c="nearly 350 American Communist Party members exposed as Soviet spies", source=S_ARMY95)], {}),
 ("So how did America catch Stalin's atomic spies? | A Soviet shortcut with the one-time pads let codebreakers read fragments of messages sent years earlier.",
  [I("list_names", kb="in", focus=[0.3, 0.5], lab=LIST)], {}),
 ("Those fragments, the N S A says, could stimulate investigations. | Once the spies were identified, the F B I had to develop the evidence about their crimes.",
  [C("dv974123", 89.5, lab=FBI)], {}),
 ("They pointed to Klaus Fuchs. | And the investigation that followed reached Gold, Greenglass and the Rosenbergs.",
  [I("fuchs_cable", kb="out", focus=[0.5, 0.5], lab=FUCHS)], {}),
 ("But the same secret that caught them also kept one case out of court. | The nineteen-year-old in the November nineteen forty-four telegram was never charged.",
  [I("hall_19", kb="in", focus=[0.6, 0.45], lab=HALL)], dict(slow=True)),
 ("Every secret has a release date. | For VENONA, it came about half a century after the messages were sent.",
  [I("obelisk", kb="in", focus=[0.3, 0.5], lab=OBEL)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments.",
  [C("dv1026930", 40.5, lab=F22)], {}),
 ("Next time: another file, released in full.",
  [G("end", n="012", next="Another file, released in full")], dict(gap=2.5)),
]

PRON = [("Grabeel", "Gra-beel"), ("Hallock", "Hal-lock"), ("PURPLE", "Purple"), ("Feinstein", "Fine-stine"), ("Lamphere", "Lamp-heer"), ("Weisband", "Wise-band"),
        ("Greenglass", "Green-glass"), ("Fuchs", "Fooks"), ("MLAD", "M-lahd"), ("VENONA", "Venona"), ("ENORMOUS", "enormous"),
        ("LIBERAL", "Liberal"), ("CHARLES", "Charles"), ("ARNO", "Arno"), ("OSA", "Osa"), ("REST", "Rest"), ("ISLAND", "Island"),
        ("Bethe", "Bay-ta"), ("Teller", "Teller"), ("C I A's", "C I A's"), ("K G B's", "K G B's")]

DISPLAY = [
 ("C I A's", "CIA's"), ("C I A", "CIA"), ("K G B's", "KGB's"), ("K G B", "KGB"), ("N S A's", "NSA's"), ("N S A", "NSA"), ("F B I", "FBI"),
 ("U S Army", "U.S. Army"), ("B twenty-nine", "B-29"),
 ("nineteen-year-old", "19-year-old"), ("twenty-three", "23"), ("Twenty-nine years old", "29 years old"),
 ("thirty-five thousand", "35,000"), ("three thousand", "3,000"), ("twenty-nine hundred", "2,900"),
 ("three hundred and fifty", "350"), ("first forty-nine", "first 49"), ("fourteen years", "14 years"), ("fifteen", "15"), ("about ten years", "about 10 years"),
 ("four-digit", "four-digit"), ("Camp Number Two", "Camp No. 2"),
 ("November twelfth", "November 12"), ("November fourteenth", "November 14"), ("December twentieth", "December 20"), ("February first", "February 1"),
 ("August twenty-fourth", "August 24"), ("September twenty-third", "September 23"), ("January twenty-fourth", "January 24"),
 ("February second", "February 2"), ("March twenty-ninth", "March 29"), ("June nineteenth", "June 19"), ("July eleventh", "July 11"),
 ("October first", "October 1"),
 ("nineteen thirty-nine", "1939"), ("nineteen forty-three", "1943"), ("nineteen forty-four and forty-five", "1944 and 1945"),
 ("nineteen forty-four", "1944"), ("nineteen forty-six", "1946"), ("nineteen forty-seven", "1947"), ("nineteen forty-eight", "1948"),
 ("nineteen forty-nine", "1949"), ("nineteen fifty-one", "1951"), ("nineteen fifty-two", "1952"), ("nineteen fifty-three", "1953"),
 ("nineteen fifty", "1950"), ("nineteen forty", "1940"), ("nineteen eighty-six", "1986"), ("nineteen eighty", "1980"), ("nineteen ninety-six", "1996"),
 ("nineteen ninety-five", "1995"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="012", title="VENONA: How Codebreakers Helped Catch Stalin's Atomic Spies",
    imgs=dict({k: D + k + ".jpg" for k in ["hall_head", "hall_19", "hall_camp", "hall_full", "hall_notes", "list_head", "list_names",
                                           "fuchs_cable", "fuchs_camp", "fuchs_notes", "ethel", "osa", "lib_notes"]},
              gardner=H + "gardner_8799384.jpg", tina=H + "tina_9948187.jpg", plaque=H + "plaque_3856843.jpg", obelisk=H + "obelisk_2902844.jpg",
              fatman=H + "fatman_4071168.jpg", trin_a=H + "trin_a.jpg", trin_b=H + "trin_b.jpg"),
    credit="Documents: NSA VENONA translations (released 1995-97). Photos and b-roll: U.S. Army, U.S. Air Force, FBI and DoD via DVIDS.\\NModern b-roll does not show the people or places of the 1940s unless labelled. No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[1, 7], hook="A KGB TELEGRAM NAMED<br>[A 19-YEAR-OLD]"),
        dict(id="s2", lines=[40, 46], hook="HOW DID THE FBI<br>[FIND KLAUS FUCHS?]"),
        dict(id="s3", lines=[32, 40], hook="THE CIA SAID 1953.<br>[IT CAME IN 1949]"),
        dict(id="s4", lines=[48, 54], hook="THE ROSENBERG CASE<br>[IN THE DECRYPTS]"),
    ],
    yshorts=[
        dict(id="y1", lines=[3, 7], hook="19, AT LOS ALAMOS,<br>[NEVER CHARGED]"),
        dict(id="y2", lines=[32, 35], hook="CIA: MID-1953.<br>[STALIN: 1949]"),
        dict(id="y3", lines=[51, 53], hook="WHAT THE NSA SAYS<br>[ABOUT ETHEL]"),
    ],
)
