# FILE 013 — Operation Mongoose: The Secret Plan to Topple Castro by October 1962
# Format: see episodes/001-navy-videos/episode.py
# Documents: Church Committee interim report "Alleged Assassination Plots Involving Foreign Leaders" (S. Rep. 94-465, Nov. 20, 1975),
#   page scans from archive.org item allegedassassina00unit (page n = printed page + 21); FRUS 1961-63 vols. X and XI (text, shown as RECREATED excerpts).
# Film stills: Universal Newsreel (archive.org, public domain), deinterlaced still frames only (yadif), via kb.py.
# NOTE on clip timing: DVIDS times are in the original files, except dv1004651a (= original 70-100 s) and dv1004651b (= original 135-205 s),
#   1080p trims of the 4K60 original.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
H = "/home/claude/src/img/"

BAKER = "ACTUAL DOCUMENT · CHURCH COMMITTEE REPORT (1975), P. 337 · ADDITIONAL VIEWS OF SEN. HOWARD BAKER"
CH = "ACTUAL DOCUMENT · CHURCH COMMITTEE, \"ALLEGED ASSASSINATION PLOTS\" (S. REP. 94-465, 1975), P. "
NRC = "ARCHIVAL FILM STILL · FIDEL CASTRO, CUBA, JANUARY 1959 · UNIVERSAL NEWSREEL"
NRH = "ARCHIVAL FILM STILL · HAVANA, JANUARY 1959 · UNIVERSAL NEWSREEL"
NRC60 = "ARCHIVAL FILM STILL · FIDEL CASTRO IN A CROWD, CUBA, 1960 · UNIVERSAL NEWSREEL"
NRMIL = "ARCHIVAL FILM STILL · CUBAN MILITIA, 1960 · UNIVERSAL NEWSREEL"
NRB26 = "ARCHIVAL FILM STILL · A B-26 BOMBER THAT LANDED IN FLORIDA, APRIL 1961 · UNIVERSAL NEWSREEL"
NRCAMP = "ARCHIVAL FILM STILL · A TRAINING BASE IN GUATEMALA, AS SHOWN IN A 1961 NEWSREEL · UNIVERSAL NEWSREEL"
JFK = "ARCHIVAL FILM STILL · PRESIDENT KENNEDY'S TV ADDRESS ON CUBA, OCTOBER 22, 1962 · UNIVERSAL NEWSREEL"
WH = "B-ROLL · THE WHITE HOUSE, WASHINGTON, D.C., 2012"
CAP = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C., 2012"
TREAS = "B-ROLL · THE TREASURY BUILDING, WASHINGTON, D.C., 2012"
PENN = "B-ROLL · AVENUE LEADING TO THE U.S. CAPITOL, WASHINGTON, D.C., 2012"
F22 = "B-ROLL · WASHINGTON, D.C., SEEN FROM AN F-22 COCKPIT, 2026"
PENT = "B-ROLL · THE PENTAGON, ARLINGTON, VIRGINIA, 2023"
PENT17 = "B-ROLL · THE PENTAGON, ARLINGTON, VIRGINIA, 2017"
GTMO = "B-ROLL · NORTHEAST GATE, U.S. NAVAL BASE GUANTANAMO BAY, CUBA, 2015"
SEA = "B-ROLL · OPEN SEA FROM A U.S. NAVY SHIP OFF KEY WEST, FLORIDA, 2026"
KW = "B-ROLL · NAVY EXERCISE OFF KEY WEST, FLORIDA, 2026"
FLARE = "B-ROLL · ILLUMINATION ROUNDS AT NIGHT, U.S. ARMY TRAINING, 2024"
CG = "B-ROLL · U.S. COAST GUARD CUTTER BEAR, BACK FROM THE FLORIDA STRAITS, 2023"
U2B = "B-ROLL · U.S. AIR FORCE U-2 RECONNAISSANCE AIRCRAFT, BEALE AIR FORCE BASE, CALIF., 2023"

S_CH = "SOURCE: CHURCH COMMITTEE, ALLEGED ASSASSINATION PLOTS INVOLVING FOREIGN LEADERS (S. REP. 94-465, 1975)"
S_X = "SOURCE: FOREIGN RELATIONS OF THE UNITED STATES, 1961-1963, VOL. X, CUBA (STATE DEPT., 1997)"
S_XI = "SOURCE: FOREIGN RELATIONS OF THE UNITED STATES, 1961-1963, VOL. XI (STATE DEPT.)"

MAP = dict(kicker="1961 – 1962", title="Florida and Cuba", bounds=[[-87.5, 18.8], [-73.5, 31.0]],
           points=[dict(ll=[-80.19, 25.76], name="Miami", sub="CIA STATION JM/WAVE"), dict(ll=[-81.78, 24.56], name="Key West"),
                   dict(ll=[-82.37, 23.13], name="Havana"),
                   dict(ll=[-83.95, 22.48], name="Matahambre", sub="COPPER MINE", anchor="end", color="#F2D04B")],
           source="SOURCE: CHURCH COMMITTEE REPORT (1975); NATIONAL SECURITY ARCHIVE (2019) · MAP: NATURAL EARTH")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("What was Operation Mongoose? | It was the Kennedy administration's secret war on Fidel Castro's Cuba. | And its plan had a target date.",
  [I("revolt", kb="in", focus=[0.35, 0.3], lab=CH + "143")], dict(tag=("WASHINGTON, D.C.", "FEBRUARY 20, 1962"))),
 ("On February twentieth, nineteen sixty-two, the man running it wrote down the schedule. | Phase five. | Revolt. | First two weeks of October nineteen sixty-two. | Open revolt and overthrow of the Communist regime.",
  [G("doc", header="OPERATION MONGOOSE · PROGRAM REVIEW · FEBRUARY 20, 1962", title="The Cuba Project",
     lines=["Phase V, Revolt, first two weeks of October 1962.", "{{Open revolt and overthrow}}", "{{of the Communist regime.}}"],
     source="SOURCE: FRUS 1961-1963, VOL. X, DOC. 304 · TEXT, RECREATED")], dict(slow=True)),
 ("The revolt never came. | But in the first weeks of that October, something else did.",
  [I("nr_castro_grp", kb="in", focus=[0.5, 0.4], lab=NRC)], {}),
 ("On October fourteenth, an American U two flew over western Cuba, and photographed Soviet missile sites.",
  [C("dv908150", 166.0, lab=U2B)], dict(tag=("WESTERN CUBA", "OCTOBER 14, 1962"))),
 ("This is the file on Mongoose. | Kennedy's order. | The tasks. | The ideas that the Senate later made public. | And how the secret war ran straight into the most dangerous month of the Cold War.",
  [I("tasks32", kb="in", focus=[0.5, 0.4], lab=CH + "142"), C("dv346124", 30.0, lab=WH)], {}),
 ("Let's open the file.",
  [G("intro", n="013")], dict(gap=0.2)),
 ("",
  [G("title", n="013", t="OPERATION MONGOOSE", size=150, sub="The Secret Plan to Topple Castro by October 1962")], dict(gap=0.4)),

 # ---------------- I. THE ORDER ----------------
 ("It started with a failure.",
  [G("chapter", n="I", t="The Order")], {}),
 ("In April nineteen sixty-one, Cuban exiles trained and backed by the C I A landed at the Bay of Pigs. | The invasion collapsed within days.",
  [I("nr_camp", kb="in", focus=[0.5, 0.5], lab=NRCAMP), I("nr_b26", kb="in", focus=[0.45, 0.5], lab=NRB26)], {}),
 ("After that failure, the Senate's investigators later found, President Kennedy distrusted the C I A.",
  [C("dv346124", 10.0, lab=WH)], {}),
 ("On November third, nineteen sixty-one, at a meeting in the White House, he authorized a new program to undermine Castro's government. | Its code name was Mongoose.",
  [C("dv346124", 38.0, lab=WH), C("dv1026930", 20.0, lab=F22)], dict(tag=("THE WHITE HOUSE", "NOVEMBER 3, 1961"))),
 ("His brother, Attorney General Robert Kennedy, wrote down his own idea in longhand. | To stir things up on the island, with espionage, sabotage, general disorder. | Run and operated by Cubans themselves.",
  [G("quote", q="My idea is to stir things up on island {{with espionage, sabotage, general disorder}}",
     who="Robert F. Kennedy", role="Handwritten notes · November 1961", size=66, source=S_X + ", DOC. 270")], dict(slow=True)),
 ("On November thirtieth, the President put it in writing. | We will use our available assets, his memo says, to help Cuba overthrow the communist regime.",
  [G("doc", header="MEMORANDUM FROM PRESIDENT KENNEDY · NOVEMBER 30, 1961 · TOP SECRET", title="The Cuba Operation",
     lines=["We will use our available assets", "to go ahead with the discussed project", "{{in order to help Cuba overthrow}}", "{{the communist regime.}}"],
     source="SOURCE: FRUS 1961-1963, VOL. X, DOC. 278 · TEXT, RECREATED")], {}),
 ("The man in charge was an Air Force general, Edward Lansdale. | His title was Chief of Operations. | According to the Senate report, he had built a reputation in the Philippines and Vietnam for dealing with revolutionary insurgencies.",
  [C("dv884981", 12.0, lab=PENT), C("dv884981", 160.0, lab=PENT)], {}),
 ("A new committee would oversee him, the Special Group Augmented. | General Maxwell Taylor was its chairman. | But Robert Kennedy, the State Department's historians write, was the principal motive force within the group.",
  [I("tfw", kb="in", focus=[0.5, 0.35], lab=CH + "140")], dict(gap=0.9, sil=True)),

 # ---------------- II. THE TASKS ----------------
 ("Lansdale moved fast.",
  [G("chapter", n="II", t="The Tasks")], {}),
 ("On January eighteenth, nineteen sixty-two, he handed out thirty-two tasks to the agencies taking part. | Two days later, he told his working group, it is our job to put the American genius to work on this project. | We are in a combat situation, where we have been given full command.",
  [I("tasks32", kb="down", focus=[0.5, 0.5], lab=CH + "142")], dict(tag=("WASHINGTON, D.C.", "JANUARY 18, 1962"))),
 ("The goal, his review said, was to help the Cubans overthrow the Communist regime from within Cuba. | And when the revolt came, the United States would give it open support. | Including military force, as necessary.",
  [G("quote", q="Such support will include {{military force, as necessary.}}",
     who="Edward Lansdale", role="Program review, Operation Mongoose · January 18, 1962", size=70, source=S_X + ", DOC. 291")], {}),
 ("The day after the tasks went out, a thirty-third task was added. | A plan to incapacitate Cuban sugar workers during the harvest, by chemical means. | It was found unfeasible, and dropped.",
  [I("nr_havana_street", kb="in", focus=[0.5, 0.5], lab=NRH)], {}),
 ("On January nineteenth, Robert Kennedy met the Mongoose team in his office. | A C I A memo on the meeting records his words. | The top priority in the United States Government. | No time, money, effort, or manpower is to be spared.",
  [I("jan19", kb="in", focus=[0.5, 0.55], lab=CH + "141"),
   G("quote", q="…all else is secondary— {{no time, money, effort, or manpower is to be spared.}}",
     who="Robert F. Kennedy, as recorded by the CIA", role="Meeting on Cuba · January 19, 1962", size=60, source=S_X + ", DOC. 292")], dict(slow=True)),
 ("Inside the C I A, Mongoose belonged to Task Force W, under William Harvey. | According to the Senate report, it employed about four hundred people, at headquarters and at the agency's station in Miami.",
  [G("stat", k="CIA TASK FORCE W · 1962", a="~400", size=300, b="people at CIA headquarters and its Miami station",
     source=S_CH + ", P. 140")], {}),
 ("The Miami station had a code name. | J M Wave.",
  [G("map", **MAP)], {}),
 ("Every plan went up the chain in detail. | Harvey's executive assistant later testified that it went down to the gradients on the beach, and the composition of the sand.",
  [I("beach", kb="in", focus=[0.5, 0.6], lab=CH + "144"), C("dv1004651b", 18.3, lab=KW)], dict(gap=0.9, sil=True)),

 # ---------------- III. THE TIMETABLE ----------------
 ("Then came the schedule.",
  [G("chapter", n="III", t="The Timetable")], {}),
 ("Lansdale's plan of February twentieth had six phases.",
  [G("timeline", kicker="THE CUBA PROJECT · FEBRUARY 20, 1962", title="Six phases to October",
     events=[dict(y="MAR", t="Action"), dict(y="APR–JUL", t="Build-up"), dict(y="AUG 1", t="Readiness"),
             dict(y="AUG–SEP", t="Resistance"), dict(y="OCT 1–14", t="Revolt"), dict(y="OCT", t="New government")],
     source="SOURCE: FRUS 1961-1963, VOL. X, DOC. 304")], dict(slow=True)),
 ("Action in March. | A build-up through July. | Guerrilla operations in August and September. | Revolt in early October. | A new government by the end of the month.",
  [I("revolt", kb="down", focus=[0.4, 0.5], lab=CH + "143")], {}),
 ("For the resistance phase, the plan as quoted by the Senate listed attacks on the cadre of the regime, including key leaders. | Gangster elements, it said, might provide the best recruitment potential for actions against police and intelligence officials.",
  [I("revolt", kb="in", focus=[0.5, 0.78], lab=CH + "143")], dict(slow=True)),
 ("And it asked the question everything depended on. | Will the U S respond promptly with military force to aid the Cuban revolt?",
  [C("dv516411", 60.0, lab=PENT17)], {}),
 ("The answer, in the guidelines of March fourteenth, was blunt. | The United States would make maximum use of Cuban resources. | But final success will require decisive U S military intervention.",
  [G("doc", header="GUIDELINES FOR OPERATION MONGOOSE · MARCH 14, 1962", title="Guidelines",
     lines=["…recognizes that", "{{final success will require}}", "{{decisive U.S. military intervention.}}"],
     source="SOURCE: FRUS 1961-1963, VOL. X, DOC. 314 · TEXT, RECREATED")], dict(slow=True)),
 ("The President, according to a State Department note, was skeptical that circumstances would arise to justify sending American forces. | No such decision was made.",
  [C("dv346124", 20.0, lab=WH), C("dv346119", 30.0, lab=PENN)], {}),
 ("For the coming months, the guidelines said, the priority would be hard intelligence. | Lansdale's six-phase schedule, the Senate found, had been shelved by the group overseeing him.",
  [C("dv346120", 3.0, lab=TREAS), C("dv1026930", 30.0, lab=F22)], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE IDEAS ----------------
 ("Some of the ideas that circulated became famous later.",
  [G("chapter", n="IV", t="The Ideas")], {}),
 ("On January twenty-seventh, nineteen sixty-two, Lansdale wrote to Robert Kennedy that we might uncork the touchdown play independently of the institutional program. | Asked about it in nineteen seventy-five, he testified that the touchdown play meant a Cuban revolt to overthrow the regime.",
  [I("touchdown", kb="in", focus=[0.5, 0.6], lab=CH + "142")], {}),
 ("In January, the Defense Department's representative sent Lansdale a concept called Operation Bounty. | Leaflets dropped over Cuba would offer rewards for killing or delivering alive known Communists.",
  [I("bounty144", kb="in", focus=[0.5, 0.45], lab=CH + "144")], {}),
 ("From five thousand dollars for an informer to one hundred thousand dollars for government officials. | The reward listed for Castro himself was two cents. | Lansdale testified it was meant to denigrate Castro in the eyes of the Cuban people.",
  [G("stat", k="OPERATION BOUNTY · JANUARY 30, 1962", a="2¢", size=320, b="the reward listed for Castro himself",
     c="meant \"to denigrate\" him, Lansdale testified", source=S_CH + ", P. 144")], dict(slow=True)),
 ("Lansdale testified that he tabled it. | According to the report, he never brought it before the group.",
  [I("bounty144", kb="down", focus=[0.5, 0.8], lab=CH + "144")], {}),
 ("One idea survives only in testimony. | In nineteen seventy-five, the group's former secretary, Thomas Parrott, told the Senate about a plan he attributed to Lansdale.",
  [I("illum", kb="in", focus=[0.5, 0.45], lab=CH + "142, FOOTNOTE")], {}),
 ("Spread the word in Cuba, he said, that the Second Coming of Christ was imminent. | Then, on the day, an American submarine would surface off Cuba and send up star shells.",
  [C("dv929212", 1.5, lab=FLARE), C("dv1004651a", 9.6, lab=SEA)], dict(slow=True)),
 ("Parrott told the story sarcastically. | Some wag, he said, called it Elimination by Illumination. | Robert McNamara, Kennedy's defense secretary, testified that same month. | We were hysterical about Castro at the time of the Bay of Pigs and thereafter. | But, he added, I don't believe we contemplated assassination.",
  [G("quote", q="Some wag called this operation… {{Elimination by Illumination.}}",
     who="Thomas Parrott, testimony", role="Senate Select Committee · July 10, 1975", size=70, source=S_CH + ", P. 142, FN. 2")], {}),
 ("And alongside Mongoose, the Senate found, ran something the committee overseeing it was not told about. | In April nineteen sixty-two, Harvey passed poison pills to John Rosselli, an underworld figure, for use against Castro.",
  [C("dv516411", 120.0, lab=PENT17), I("uhaul", kb="in", focus=[0.5, 0.4], lab=CH + "84")], {}),
 ("With help from the Miami station, Harvey and the station chief rented a U-Haul truck under an assumed name, loaded it with explosives, rifles and radios, and left it in a parking lot.",
  [I("uhaul", kb="in", focus=[0.5, 0.6], lab=CH + "84")], dict(gap=0.9, sil=True)),

 # ---------------- V. PLAN B PLUS ----------------
 ("By summer, Washington wanted more.",
  [G("chapter", n="V", t="Plan B Plus")], {}),
 ("On August eighth, at the group's request, Lansdale laid out a stepped-up course. | Major sabotage. | Submarines for infiltration. | Radio and leaflets.",
  [C("dv1004651b", 58.0, lab=KW), C("dv449861", 12.0, lab=GTMO)], dict(tag=("WASHINGTON, D.C.", "AUGUST 8, 1962"))),
 ("Even then, his paper reported, the C I A's own operational people did not believe it would bring down the regime by itself. | They believed the use of U S military force in the final stage must be anticipated.",
  [G("quote", q="…the use of U.S. military force {{in the final stage must be anticipated, for success.}}",
     who="Edward Lansdale, reporting the CIA operators' view", role="\"Stepped Up Course B\" · August 8, 1962", size=62, source=S_X + ", DOC. 367")], {}),
 ("On August tenth, at a meeting in the Secretary of State's office, the question of assassinating Cuban leaders came up. | Three days later, Lansdale asked Harvey for an option on the liquidation of leaders.",
  [I("liquid", kb="in", focus=[0.5, 0.6], lab=CH + "161")], dict(tag=("WASHINGTON, D.C.", "AUGUST 10, 1962"))),
 ("Harvey objected to putting it on paper. | He wrote of the stupidity of putting this type of comment in writing. | The meeting's minutes contain no reference to assassination.",
  [G("quote", q="…the inadmissability and {{stupidity of putting this type of comment in writing}}",
     who="William Harvey, CIA", role="Memo to Richard Helms · August 14, 1962", size=62, source=S_CH + ", P. 162")], {}),
 ("On August twenty-third, a national security memo conveyed President Kennedy's orders. | Mongoose Plan B plus should be developed with all possible speed.",
  [G("doc", header="NATIONAL SECURITY ACTION MEMORANDUM NO. 181 · AUGUST 23, 1962", title="NSAM 181",
     lines=["The line of activity projected for", "{{Operation Mongoose Plan B plus}}", "{{should be developed with all possible speed.}}"],
     source="SOURCE: FRUS 1961-1963, VOL. X, DOC. 386 · TEXT, RECREATED")], dict(slow=True)),
 ("The same memo asked for something else. | An analysis of what it would mean if the Soviets put missiles in Cuba that could reach the United States.",
  [I("nr_militia60", kb="in", focus=[0.5, 0.5], lab=NRMIL)], {}),
 ("For the purpose of its plan, a C I A paper that month assumed that Soviet troops will not be present in Cuba in force.",
  [I("nr_castro60", kb="in", focus=[0.55, 0.4], lab=NRC60)], {}),
 ("On August thirtieth, an operation was approved to blow up a copper mine in western Cuba. | Matahambre.",
  [I("matah", kb="in", focus=[0.5, 0.45], lab=BAKER)], dict(gap=0.9, sil=True)),

 # ---------------- VI. OCTOBER ----------------
 ("Then it was October.",
  [G("chapter", n="VI", t="October")], {}),
 ("On October fourth, Robert Kennedy reported on his talks with the President about Cuba. | He was dissatisfied, the record says, with the lack of action in the sabotage field.",
  [C("dv346026", 14.0, lab=CAP), C("dv346120", 20.0, lab=TREAS)], {}),
 ("On October sixteenth, the day the President was shown the missile photographs, Robert Kennedy met the Mongoose team that afternoon.",
  [C("dv908150", 194.0, lab=U2B)], dict(tag=("WASHINGTON, D.C.", "OCTOBER 16, 1962"))),
 ("He spoke of the general dissatisfaction of the President. | A year in, the results were discouraging. | There had been no acts of sabotage, and even the one attempted had failed twice.",
  [G("quote", q="…the {{\"general dissatisfaction of the President\"}} with Operation Mongoose.",
     who="Richard Helms, CIA", role="Memo on the Mongoose meeting · October 16, 1962", size=62, source=S_XI + ", DOC. 19")], dict(slow=True)),
 ("Six days later, the President went on television and told the country about the missiles.",
  [I("jfk62a", kb="in", focus=[0.5, 0.35], lab=JFK)], {}),
 ("On the morning of October twenty-sixth, C I A Director John McCone told the President's crisis committee he had stood down an operation to send ten teams, fifty people, into Cuba by submarine. | That afternoon, three teams already on the way were recalled.",
  [C("dv873616", 2.0, lab=CG), G("stat", k="OCTOBER 26, 1962", a="10 TEAMS", size=230, b="50 people, to go into Cuba by submarine — stood down",
     source=S_XI + ", DOCS. 79, 82")], {}),
 ("No major acts of sabotage should be undertaken at this time, the afternoon minutes say. | That morning, the President had suggested that Mongoose be reconstituted, and oriented toward problems of a Cuba after Castro.",
  [C("dv1004651b", 40.0, lab=KW), C("dv873616", 9.0, lab=CG)], {}),
 ("That same day, a letter came from Nikita Khrushchev. | The threat of armed attack, he wrote, had constantly hung over Cuba. | He did not name Mongoose.",
  [G("quote", q="…the threat of armed attack, aggression, {{has constantly hung… over Cuba.}}",
     who="Nikita Khrushchev to President Kennedy", role="Letter · October 26, 1962 · U.S. Embassy translation", size=62, source=S_XI + ", DOC. 84")], {}),
 ("Two days later, he agreed to remove the missiles. | The Matahambre team, according to National Security Archive researchers, went in during the crisis, and was never recovered.",
  [I("jfk62c", kb="in", focus=[0.5, 0.4], lab=JFK), G("map", **MAP)], dict(gap=0.9, sil=True)),

 # ---------------- VII. DEAD END ----------------
 ("After the crisis, Mongoose wound down.",
  [G("chapter", n="VII", t="Dead End")], {}),
 ("In late November, McCone said future activity should be restricted to intelligence gathering. | On January fourth, nineteen sixty-three, McGeorge Bundy, the national security adviser, wrote to the President.",
  [C("dv346119", 14.0, lab=PENN), C("dv884981", 100.0, lab=PENT)], {}),
 ("There is well nigh universal agreement that Mongoose is at a dead end.",
  [G("quote", q="…there is well nigh universal agreement that {{Mongoose is at a dead end.}}",
     who="McGeorge Bundy to President Kennedy", role="Memorandum · January 4, 1963", size=70, source=S_XI + ", DOC. 261")], dict(slow=True)),
 ("The program ended. | The sabotage, one senator later wrote, continued.",
  [I("matah2", kb="in", focus=[0.5, 0.55], lab=BAKER)], {}),
 ("In November nineteen seventy-five, the Senate's Church Committee pulled the story into the open. | It found concrete evidence of at least eight plots involving the C I A to assassinate Fidel Castro, from nineteen sixty to nineteen sixty-five.",
  [G("stat", k="CHURCH COMMITTEE · NOVEMBER 20, 1975", a="8", size=360, b="plots involving the CIA to kill Castro",
     c="1960–1965 · \"concrete evidence of at least eight\"", source=S_CH + ", P. 71")], {}),
 ("Those plots, it said, could not be understood without the fully authorized assaults on his regime, including Operation Mongoose.",
  [I("ctx6", kb="in", focus=[0.5, 0.6], lab=CH + "6")], {}),
 ("But the committee could not find that any President had authorized the plots. | The system, it wrote, was so ambiguous that it is difficult to be certain at what levels assassination activity was known and authorized. | It was also possible, the committee added, that there had been a successful plausible denial, in which authorization was issued but is now obscured.",
  [I("find6", kb="in", focus=[0.5, 0.45], lab=CH + "6"), I("find7", kb="in", focus=[0.5, 0.45], lab=CH + "7")], dict(gap=0.9, sil=True)),

 # ---------------- VIII. THE RELEASE ----------------
 ("The paper trail came out in stages.",
  [G("chapter", n="VIII", t="The Release")], {}),
 ("The Senate report in November nineteen seventy-five. | In nineteen ninety-seven, the State Department's official history volume on Cuba, with Kennedy's order, Lansdale's plans and the meeting notes. | And more records from the National Archives' Kennedy assassination collection in twenty seventeen and twenty twenty-five.",
  [G("timeline", kicker="OPERATION MONGOOSE", title="How the file came out",
     events=[dict(y="1975", t="Church Committee report"), dict(y="1997", t="FRUS vol. X: Cuba"),
             dict(y="2017", t="JFK records release"), dict(y="2019", t="National Security Archive collection"),
             dict(y="2025", t="JFK records release")],
     source="SOURCES: S. REP. 94-465; U.S. DEPT. OF STATE; NATIONAL ARCHIVES; NATIONAL SECURITY ARCHIVE")], {}),
 ("So what was Operation Mongoose? | A secret program, ordered in writing by the President and driven by his brother, to bring down Castro's government from inside Cuba.",
  [I("nr_castro_rifle", kb="in", focus=[0.5, 0.35], lab=NRC)], {}),
 ("Its own planners said success would need American troops. | Its target date was October nineteen sixty-two. | And that October, instead of a revolt, the world got the Cuban Missile Crisis.",
  [I("revolt", kb="in", focus=[0.35, 0.3], lab=CH + "143"), C("dv449861", 40.5, lab=GTMO)], dict(slow=True)),
 ("Every secret has a release date. | For Mongoose, the first one came thirteen years later, in a Senate report.",
  [I("nr_havana_cap", kb="in", focus=[0.5, 0.4], lab=NRH)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments.",
  [C("dv1026930", 40.5, lab=F22)], {}),
 ("Next time: another file, released in full.",
  [G("end", n="013", next="Another file, released in full")], dict(gap=2.5)),
]

PRON = [("Mongoose", "Mongoose"), ("Lansdale", "Lans-dale"), ("Matahambre", "Mata-ahm-bray"), ("Rosselli", "Ro-selli"),
        ("McCone", "Mc-Cone"), ("Khrushchev", "Kroosh-chev"), ("Parrott", "Parrot"), ("U-Haul", "U Haul"),
        ("J M Wave", "J M Wave"), ("C I A's", "C I A's"), ("U two", "U two"), ("nigh", "nye")]

DISPLAY = [
 ("C I A's", "CIA's"), ("C I A", "CIA"), ("J M Wave", "JM/WAVE"), ("U S military", "U.S. military"), ("the U S respond", "the U.S. respond"),
 ("U two", "U-2"), ("two cents", "2 cents"),
 ("thirty-two tasks", "32 tasks"), ("thirty-third task", "33rd task"), ("four hundred", "400"),
 ("five thousand dollars", "$5,000"), ("one hundred thousand dollars", "$100,000"),
 ("ten teams, fifty people", "10 teams, 50 people"), ("three teams", "three teams"), ("at least eight", "at least eight"),
 ("February twentieth", "February 20"), ("October fourteenth", "October 14"), ("November third", "November 3"),
 ("November thirtieth", "November 30"), ("January eighteenth", "January 18"), ("January nineteenth", "January 19"),
 ("August eighth", "August 8"), ("August tenth", "August 10"), ("August twenty-third", "August 23"), ("August thirtieth", "August 30"),
 ("October fourth", "October 4"), ("March fourteenth", "March 14"), ("October sixteenth", "October 16"), ("October twenty-sixth", "October 26"),
 ("January fourth", "January 4"), ("January twenty-seventh", "January 27"),
 ("nineteen sixty-one", "1961"), ("nineteen sixty-two", "1962"), ("nineteen sixty-three", "1963"), ("nineteen sixty-five", "1965"),
 ("nineteen sixty", "1960"), ("nineteen seventy-five", "1975"), ("nineteen ninety-seven", "1997"),
 ("twenty seventeen", "2017"), ("twenty twenty-five", "2025"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="013", title="Operation Mongoose: The Secret Plan to Topple Castro by October 1962",
    imgs=dict({k: D + k + ".jpg" for k in ["revolt", "tasks32", "tfw", "jan19", "beach", "bounty144", "illum", "uhaul", "liquid", "matah",
                                           "ctx6", "find6", "find7", "touchdown", "matah2"]},
              **{k: H + k + ".jpg" for k in ["nr_castro_grp", "nr_castro_rifle", "nr_havana_cap", "nr_havana_street", "nr_camp", "nr_b26",
                                             "nr_militia60", "nr_castro60", "jfk62a", "jfk62c"]}),
    credit="Documents: U.S. Senate, Church Committee report (1975). Film stills: Universal Newsreel (public domain).\\NB-roll: DoD via DVIDS. Modern b-roll does not show the events of 1961-62 unless labelled. No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[33, 39], hook="A 2-CENT BOUNTY IDEA.<br>[A 'SECOND COMING'?]"),
        dict(id="s2", lines=[9, 15], hook="WHAT WAS<br>[OPERATION MONGOOSE?]"),
        dict(id="s3", lines=[53, 58], hook="THE DAY JFK SAW<br>[THE MISSILE PHOTOS]"),
        dict(id="s4", lines=[43, 48], hook="SUMMER 1962:<br>[THE SECRET WAR ESCALATES]"),
    ],
    yshorts=[
        dict(id="y1", lines=[34, 36], hook="A PROPOSED BOUNTY:<br>[TWO CENTS]"),
        dict(id="y2", lines=[37, 39], hook="A FAKE SECOND COMING?<br>[A WITNESS SAID SO]"),
        dict(id="y3", lines=[52, 55], hook="OCTOBER 16, 1962:<br>[RFK MEETS MONGOOSE]"),
    ],
)
