# FILE 010 — The Family Jewels: The CIA's List of Its Own Secrets
# Format: see episodes/001-navy-videos/episode.py
# NOTE on clip timing: dv1026930t = DVIDS 1026930 trimmed from 22 s and scaled to 1080p; dv825871t = DVIDS 825871 trimmed from 120 s.
# Times below are relative to those trimmed files.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
FJN = "CIA, \"FAMILY JEWELS\" (1973; RELEASED JUNE 2007)"
FJ = "ACTUAL DOCUMENT · " + FJN
RKN = "REPORT TO THE PRESIDENT BY THE COMMISSION ON CIA ACTIVITIES WITHIN THE UNITED STATES (JUNE 1975)"
RK = "ACTUAL DOCUMENT · " + RKN
S_FJ = "SOURCE: " + FJN
S_RK = "SOURCE: " + RKN
S_FRUS = "SOURCE: FRUS 1969-1976, VOL. XXXVIII, PART 2 (U.S. DEPARTMENT OF STATE)"
S_NSA = "SOURCE: NATIONAL SECURITY ARCHIVE, \"THE CIA'S FAMILY JEWELS\" (EBB 222, 2007)"

WH = "B-ROLL · THE WHITE HOUSE, WASHINGTON, D.C. · DVIDS, 2012"
CAP = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C. · DVIDS, 2012"
PENN = "B-ROLL · PENNSYLVANIA AVENUE AND THE CAPITOL, WASHINGTON, D.C. · DVIDS, 2012"
F22 = "B-ROLL · WASHINGTON, D.C., SEEN FROM AN F-22 COCKPIT, 2026"
PENT = "B-ROLL · THE PENTAGON, ARLINGTON, VIRGINIA, 2023"
PENT17 = "B-ROLL · THE PENTAGON, ARLINGTON, VIRGINIA, 2017"
MALL = "B-ROLL · THE POTOMAC AND THE WASHINGTON MONUMENT, 2023"
MAIL = "B-ROLL · MILITARY MAIL SORTED IN SOUTH KOREA, 2021 · NOT A CIA OPERATION"

LINES = [
 # ---------------- COLD OPEN ----------------
 ("On May ninth, nineteen seventy-three, the Director of Central Intelligence sent a memo to every employee of the C I A.",
  [I("sch_head", kb="in", focus=[0.5, 0.45], lab=FJ)], {}),
 ("It asked them to report anything the agency had done, now or in the past, that might be outside the law that created it.",
  [I("sch_page", kb="in", focus=[0.5, 0.78], lab=FJ)], {}),
 ("And it told them exactly how. | Anyone who has such information should call my secretary, extension six three six three.",
  [I("sch_direct", kb="in", focus=[0.45, 0.6], lab=FJ)], dict(slow=True)),
 ("The answers filled a file of about seven hundred pages. | Inside the agency, it got a nickname. | The Family Jewels.",
  [I("att_page", kb="in", focus=[0.5, 0.2], lab=FJ)], dict(slow=True)),
 ("Wiretaps on reporters. Mail opened in New York. A member of the Mafia, used in an attempt to assassinate Fidel Castro. A Soviet defector, held for more than two years in a cell with nothing but a cot.",
  [I("att_a", kb="in", focus=[0.5, 0.5], lab=FJ)], {}),
 ("The full file stayed classified for thirty-four years.",
  [C("dv884981", 150.0, lab=MALL)], {}),
 ("This is the C I A's own list of its secrets. | Let's open it.",
  [G("intro", n="010")], dict(gap=0.2)),
 ("",
  [G("title", n="010", t="The Family Jewels", size=150, sub="The CIA's List of Its Own Secrets")], dict(gap=0.4)),

 # ---------------- I. THE ORDER ----------------
 ("To understand why a spy agency would write all this down, start with a burglary.",
  [G("chapter", n="I", t="The Order")], {}),
 ("In June nineteen seventy-two, burglars were arrested at the headquarters of the Democratic National Committee, in the Watergate building in Washington.",
  [C("dv346119", 2.0, lab=PENN), C("dv346124", 24.0, lab=WH)], dict(tag=("WASHINGTON, D.C.", "JUNE 1972"))),
 ("According to the presidential commission that later investigated the C I A, four of the people in the break-in had ties to the agency.",
  [I("rk_title", kb="in", focus=[0.5, 0.45], lab=RK)], {}),
 ("One of them was E Howard Hunt, a former C I A officer then working with the White House.",
  [C("dv346124", 36.0, lab=WH)], {}),
 ("The Family Jewels describe what Hunt had received a year earlier. | On July twenty-third, nineteen seventy-one, the agency gave him alias documents in the name Edward Joseph Warren. | And disguise materials. A wig, glasses, and a speech alteration device.",
  [I("hunt", kb="in", focus=[0.5, 0.6], lab=FJ)], dict(slow=True)),
 ("In later meetings, the file says, he was given a tape recorder in a typewriter case, and a camera disguised in a tobacco pouch.",
  [I("hunt2", kb="in", focus=[0.5, 0.4], lab=FJ)], {}),
 ("Later he brought in an associate, later identified from press photos as G Gordon Liddy, who got a wig and an alias of his own.",
  [I("hunt2", kb="down", focus=[0.5, 0.8], lab=FJ)], {}),
 ("The commission found no evidence that the C I A took part in the Watergate break-in itself. | But by May nineteen seventy-three, press reports were describing the agency's help to Hunt.",
  [C("dv346026", 6.0, lab=CAP)], {}),
 ("James Schlesinger had just become its director. | He wrote that he was determined that the law shall be respected.",
  [G("quote", q="…I am determined that {{the law shall be respected…}}",
     who="James R. Schlesinger", role="Director of Central Intelligence · May 9, 1973", size=66, source=S_FJ)], {}),
 ("So he ordered all the senior operating officials to report, immediately, on anything that might be construed to be outside the agency's legislative charter. | And he invited former employees to do the same.",
  [I("sch_order", kb="in", focus=[0.5, 0.5], lab=FJ)], dict(gap=0.9, sil=True)),

 # ---------------- II. THE LIST ----------------
 ("The reports started arriving within a week.",
  [G("chapter", n="II", t="The List")], {}),
 ("On May sixteenth, the agency's Director of Security, Howard Osborn, sent his. | The subject line was two words in quotation marks. | Family Jewels.",
  [I("osb_subj", kb="in", focus=[0.45, 0.42], lab=FJ)], dict(slow=True)),
 ("He went back to nineteen fifty-nine, he explained, because those activities still had what he called a viable flap potential.",
  [I("osb_flap", kb="in", focus=[0.5, 0.4], lab=FJ)], {}),
 ("Many of the people involved were still alive, and could embarrass the agency.",
  [G("quote", q="…still have a viable {{\"flap potential\"}} in that many of the people involved… are still alive…",
     who="Howard J. Osborn", role="CIA Director of Security · May 16, 1973", size=60, source=S_FJ)], {}),
 ("He added an assurance. | Unless otherwise stated, each of these activities was approved by higher authority.",
  [I("osb_page", kb="in", focus=[0.5, 0.8], lab=FJ)], {}),
 ("His memo came with a short list, headed Attachment A. | Its title, again in quotation marks. Family Jewels.",
  [I("att_page", kb="in", focus=[0.5, 0.25], lab=FJ)], {}),
 ("Item two. Johnny Roselli. | The use of a member of the Mafia in an attempt to assassinate Fidel Castro.",
  [I("att_a", kb="in", focus=[0.4, 0.15], lab=FJ)], dict(slow=True)),
 ("Item four. Yuriy Nosenko, a K G B defector, confined from August nineteen sixty-five to October nineteen sixty-seven in a specially constructed jail. | Literally, the memo says, in a cell with nothing but a cot.",
  [I("att_a", kb="in", focus=[0.4, 0.7], lab=FJ)], {}),
 ("Memos like his came in from across the agency. The collection was put together under William Colby, the head of the clandestine service, who would soon become director himself.",
  [C("dv516411", 20.0, lab=PENT17)], {}),
 ("When the C I A finally released the collection, it ran to about seven hundred pages, with many passages still blacked out.",
  [G("stat", k="THE FAMILY JEWELS · RELEASED JUNE 2007", a="702", to=702, size=300, b="pages in the released collection",
     c="first announced as 693 pages", source=S_NSA)], dict(gap=0.9, sil=True)),

 # ---------------- III. THE WIRETAPS ----------------
 ("So what was in it? | Start with the reporters.",
  [G("chapter", n="III", t="The Wiretaps")], {}),
 ("In March nineteen sixty-three, the C I A began tapping the phones of two Washington newsmen who had been publishing classified material.",
  [I("mock1", kb="in", focus=[0.5, 0.3], lab=FJ)], {}),
 ("The file calls it Project Mockingbird. | Taps went into their office and into each of their homes. Three lines in all.",
  [I("mock_page", kb="in", focus=[0.5, 0.25], lab=FJ)], {}),
 ("The authority, it says, came from Director John McCone. | And McCone coordinated it with the Attorney General, Robert Kennedy, and the Secretary of Defense, Robert McNamara.",
  [I("mock1", kb="down", focus=[0.5, 0.75], lab=FJ), C("dv884981", 70.0, lab=PENT)], {}),
 ("The taps ran for about three months. | And the file is candid about what they caught.",
  [C("dv346026", 14.0, lab=CAP)], {}),
 ("During that period, it says, the reporters received information from twelve senators and six members of Congress, all identified. | From twenty-one congressional staff members. | And from sixteen government employees, including a staff member of the White House.",
  [I("mock2", kb="in", focus=[0.5, 0.45], lab=FJ)], dict(slow=True)),
 ("Eight years later, the reporters were different, but the goal was the same. | Find their sources.",
  [C("dv1026930t", 4.0, lab=F22)], {}),
 ("In late nineteen seventy-one, at the director's direction, the agency's Office of Security followed Michael Getler of the Washington Post, and watched his office building from an observation post in the Statler Hilton Hotel.",
  [C("dv346119", 30.0, lab=PENN)], {}),
 ("In nineteen seventy-two, it followed columnist Jack Anderson, and at various times three of his reporters. | One of them, the file spells as Britt Hume. | The purpose was to find Anderson's sources for classified agency information in his columns.",
  [I("celotex", kb="in", focus=[0.5, 0.45], lab=FJ)], dict(slow=True)),
 ("The file's code name for that operation was CELOTEX two.",
  [G("list", kicker="OFFICE OF SECURITY · SURVEILLANCE OF NEWSMEN", title="As listed in the Family Jewels",
     items=[dict(n="1963", t="Project MOCKINGBIRD", s="TWO NEWSMEN · PHONE TAPS"),
            dict(n="1971", t="CELOTEX I", s="MICHAEL GETLER · WASHINGTON POST"),
            dict(n="1972", t="CELOTEX II", s="JACK ANDERSON AND HIS \"LEG MEN\"")],
     source=S_FJ)], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE MAIL ----------------
 ("Then there was the mail.",
  [G("chapter", n="IV", t="The Mail")], {}),
 ("Since nineteen fifty-three, the Office of Security wrote, it had run a mail intercept program at Kennedy Airport in New York City. | Its main target was mail going to and from the Soviet Union.",
  [I("mail", kb="in", focus=[0.5, 0.35], lab=FJ)], {}),
 ("It wasn't only photographing envelopes. | The file says it also included surreptitious opening and photographing of selected items of mail.",
  [I("mail", kb="down", focus=[0.5, 0.6], lab=FJ), C("dv825871t", 30.0, lab=MAIL)], {}),
 ("The presidential commission later put numbers on it. | In the last year before the program ended, out of four million, three hundred and fifty thousand items of mail to and from the Soviet Union, the New York intercept examined the outside of two million, three hundred thousand.",
  [I("rk_mail", kb="in", focus=[0.5, 0.5], lab=RK)], {}),
 ("It photographed thirty-three thousand envelopes. | And it opened eight thousand seven hundred items of mail.",
  [G("stat", k="NEW YORK MAIL INTERCEPT · ITS LAST YEAR", a="8,700", to=8700, size=280, b="items of mail opened",
     c="33,000 envelopes photographed · 2,300,000 examined", source=S_RK)], dict(slow=True)),
 ("According to the commission, the F B I knew about the program from nineteen fifty-eight, and received fifty-seven thousand items from it.",
  [C("dv825871t", 60.0, lab=MAIL)], {}),
 ("And according to the commission, a nineteen sixty-two C I A memo indicates the agency was aware the mail openings would be viewed as violating federal criminal laws.",
  [G("doc", header="CIA MEMORANDUM · 1962 · AS DESCRIBED BY THE ROCKEFELLER COMMISSION", title="On the mail openings",
     lines=["…the Agency was aware that the mail openings", "{{would be viewed as violating federal criminal laws}}", "prohibiting obstruction or delay of the mails."],
     source="SOURCE: ROCKEFELLER COMMISSION REPORT (1975), P. 20 · WORDING OF THE REPORT, RECREATED")], {}),
 ("The program ended in nineteen seventy-three, when the Chief Postal Inspector refused to let it continue without fresh high-level approval.",
  [C("dv825871t", 100.0, lab=MAIL)], dict(gap=0.9, sil=True)),

 # ---------------- V. CHAOS ----------------
 ("One program in the file had a name that sounds like a warning.",
  [G("chapter", n="V", t="Chaos")], {}),
 ("The C I A described it as a worldwide program to collect information abroad on foreign efforts to support, encourage, exploit, or manipulate domestic U S extremism.",
  [I("chaos", kb="in", focus=[0.5, 0.45], lab=FJ)], {}),
 ("It named the foreign players. Cuba, Communist China, North Vietnam, the Soviet Union, North Korea, and the Arab fedayeen. | And it insisted the agency's efforts were foreign.",
  [I("chaos", kb="down", focus=[0.5, 0.7], lab=FJ), I("chaos2", kb="in", focus=[0.5, 0.4], lab=FJ)], {}),
 ("The commission saw it differently.",
  [C("dv1026930t", 14.0, lab=F22)], {}),
 ("During six years, it found, the operation compiled some thirteen thousand different files, including files on seven thousand two hundred American citizens.",
  [I("rk_chaos", kb="in", focus=[0.5, 0.6], lab=RK)], {}),
 ("The names of more than three hundred thousand persons and organizations went into a computerized index.",
  [G("stat", k="OPERATION CHAOS · SIX YEARS", a="300,000+", size=250, b="names in a computerized index",
     c="13,000 files · 7,200 on American citizens", source=S_RK)], dict(slow=True)),
 ("Some of its domestic activities, the commission concluded, unlawfully exceeded the C I A's statutory authority.",
  [C("dv884981", 20.0, lab=PENT)], dict(gap=0.9, sil=True)),

 # ---------------- VI. THE LEAK ----------------
 ("For a year and a half, the list itself stayed out of public view.",
  [G("chapter", n="VI", t="The Leak")], {}),
 ("Then, on December twenty-second, nineteen seventy-four, the New York Times ran a front-page story by Seymour Hersh.",
  [C("dv346119", 12.0, lab=PENN)], dict(tag=("NEW YORK TIMES", "DECEMBER 22, 1974"))),
 ("Its headline. | Huge C I A Operation Reported in U S Against Antiwar Forces, Other Dissidents in Nixon Years.",
  [G("doc", header="THE NEW YORK TIMES · DECEMBER 22, 1974 · FRONT PAGE", title="Headline",
     lines=["{{Huge C.I.A. Operation Reported in U.S.}}", "Against Antiwar Forces, Other Dissidents", "in Nixon Years"],
     source="SOURCE: FRUS 1969-1976, VOL. XXXVIII, PART 2, DOC. 17 (EDITORIAL NOTE) · HEADLINE, RECREATED")], dict(slow=True)),
 ("It said the agency had kept intelligence files on at least ten thousand American citizens.",
  [C("dv346124", 30.0, lab=WH)], {}),
 ("According to the State Department's official history, Colby phoned President Gerald Ford aboard Air Force One. | He said nothing comparable to the article's allegations was going on at the agency at that time. | The White House had not been briefed on the Family Jewels.",
  [C("dv1026930t", 2.0, lab=F22), C("dv884981", 160.0, lab=MALL)], {}),
 ("On January fourth, nineteen seventy-five, Ford signed Executive Order eleven eight twenty-eight, creating a commission on C I A activities within the United States, chaired by Vice President Nelson Rockefeller.",
  [I("rk_members", kb="in", focus=[0.5, 0.4], lab=RK)], {}),
 ("Its eight members included a retired general named Lyman Lemnitzer. The same man who, as Chairman of the Joint Chiefs, signed the Operation Northwoods memo. | And a former governor of California. | Ronald Reagan.",
  [I("rk_members", kb="down", focus=[0.5, 0.75], lab=RK)], dict(slow=True)),
 ("On January seventeenth, in the Oval Office, Secretary of State Henry Kissinger told the President. | The morale of the C I A must be terrible.",
  [G("quote", q="{{The morale of the CIA must be terrible.}}",
     who="Henry A. Kissinger", role="To President Ford · January 17, 1975", size=72, source=S_FRUS + ", DOC. 29")], {}),
 ("Ten days after that, the Senate voted eighty-two to four to create its own investigation, led by Senator Frank Church.",
  [C("dv346026", 18.0, lab=CAP)], dict(gap=0.9, sil=True, tag=("U.S. SENATE", "JANUARY 27, 1975"))),

 # ---------------- VII. THE VERDICT ----------------
 ("The Rockefeller Commission delivered its report in June nineteen seventy-five.",
  [G("chapter", n="VII", t="The Verdict")], {}),
 ("Some of these activities, it said, were initiated or ordered by Presidents. | Some fell in a doubtful area. | And some of them were plainly unlawful, and constituted improper invasions upon the rights of Americans.",
  [I("rk_unlawful", kb="in", focus=[0.5, 0.75], lab=RK)], dict(slow=True)),
 ("It also found that the agency's own actions, mostly in nineteen seventy-three and nineteen seventy-four, had gone far to end those activities.",
  [C("dv884981", 40.0, lab=PENT)], {}),
 ("On the mail, it was blunt. | While in operation, the C I A's domestic mail opening programs were unlawful.",
  [G("quote", q="…the CIA's domestic mail opening programs {{were unlawful.}}",
     who="Rockefeller Commission", role="Report to the President · June 1975", size=66, source=S_RK)], {}),
 ("The Church Committee went further, into assassination plots abroad, and into the F B I and other agencies. | Its final report came in April nineteen seventy-six.",
  [C("dv346119", 40.0, lab=PENN)], {}),
 ("By then, President Ford had signed Executive Order eleven nine-oh-five. | One line in it reads, No employee of the United States Government shall engage in, or conspire to engage in, political assassination.",
  [G("doc", header="EXECUTIVE ORDER 11905 · FEBRUARY 18, 1976 · SEC. 5(g)", title="Prohibition of Assassination",
     lines=["No employee of the United States Government", "shall engage in, or conspire to engage in,", "{{political assassination.}}"],
     source="SOURCE: EXECUTIVE ORDER 11905, SIGNED BY GERALD R. FORD · TEXT, RECREATED")], dict(slow=True)),
 ("In nineteen seventy-six, the Senate created a permanent intelligence committee. | And in nineteen seventy-eight, Congress passed the Foreign Intelligence Surveillance Act, so that national security wiretaps would need a warrant from a special court.",
  [G("timeline", kicker="AFTER THE FAMILY JEWELS", title="What changed",
     events=[dict(y="1975", t="Rockefeller Commission"), dict(y="1975", t="Church Committee formed"),
             dict(y="1976", t="Ban on political assassination"), dict(y="1976", t="Senate Intelligence Committee"),
             dict(y="1978", t="FISA court warrants")],
     source="SOURCES: ROCKEFELLER COMMISSION (1975); U.S. SENATE HISTORICAL OFFICE; EXECUTIVE ORDER 11905")], dict(gap=0.9, sil=True)),

 # ---------------- VIII. THE RELEASE ----------------
 ("But the list itself stayed locked away.",
  [G("chapter", n="VIII", t="The Release")], {}),
 ("In June two thousand seven, C I A Director Michael Hayden declassified it. | He called it a glimpse of a very different time and a very different agency.",
  [G("quote", q="…a glimpse of {{a very different time and a very different Agency.}}",
     who="Michael V. Hayden", role="CIA Director · June 2007", size=66, source=S_NSA)], {}),
 ("Today the full collection can be read online, page by page.",
  [I("att_page", kb="down", focus=[0.5, 0.6], lab=FJ)], {}),
 ("Whole lines are still blacked out. | The first item on the attachment that gave the file its name is a blank box.",
  [I("att_page", kb="in", focus=[0.5, 0.2], lab=FJ)], dict(slow=True)),
 ("But much of the file is there to read. | And it all goes back to one memo, and one phone number.",
  [I("sch_page", kb="in", focus=[0.5, 0.5], lab=FJ)], {}),
 ("Every secret has a release date. | For the C I A's own list of its secrets, it came thirty-four years after that memo.",
  [I("sch_direct", kb="out", focus=[0.45, 0.6], lab=FJ)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments.",
  [C("dv884981", 170.0, lab=MALL)], {}),
 ("Next time: two weekends in July nineteen fifty-two, when radar operators saw something over Washington. | UFOs over the Capitol.",
  [G("end", n="010", next="Saucers Over the Capitol, 1952")], dict(gap=2.5)),
]

PRON = [("Schlesinger", "Shlessinger"), ("McCone", "Mc-Cone"), ("Getler", "Gettler"), ("Lemnitzer", "Lem-nitzer"),
        ("Colby", "Colby"), ("Osborn", "Oz-born"), ("Hersh", "Hersh"), ("fedayeen", "fedda-yeen"),
        ("Statler", "Statler"), ("Roselli", "Ro-selly"), ("Nosenko", "No-senko"), ("Yuriy", "Yuri"), ("Liddy", "Liddy"), ("CELOTEX", "Cello-tex"), ("C I A's", "C I A's"),
        ("surreptitious", "surreptitious"), ("eleven nine-oh-five", "eleven nine oh five")]

DISPLAY = [
 ("C I A's", "CIA's"), ("C I A", "CIA"), ("F B I", "FBI"), ("U S extremism", "U.S. extremism"), ("Reported in U S", "Reported in U.S."),
 ("E Howard Hunt", "E. Howard Hunt"), ("G Gordon Liddy", "G. Gordon Liddy"),
 ("extension six three six three", "extension 6363"), ("Executive Order eleven eight twenty-eight", "Executive Order 11828"),
 ("Executive Order eleven nine-oh-five", "Executive Order 11905"), ("CELOTEX two", "CELOTEX II"),
 ("four million, three hundred and fifty thousand", "4,350,000"), ("two million, three hundred thousand", "2,300,000"),
 ("thirty-three thousand", "33,000"), ("eight thousand seven hundred", "8,700"), ("fifty-seven thousand", "57,000"),
 ("thirteen thousand", "13,000"), ("seven thousand two hundred", "7,200"), ("three hundred thousand", "300,000"),
 ("ten thousand", "10,000"), ("eighty-two to four", "82 to 4"), ("seven hundred pages", "700 pages"),
 ("twelve senators", "12 senators"), ("six members", "6 members"), ("twenty-one congressional", "21 congressional"), ("sixteen government", "16 government"),
 ("May ninth", "May 9"), ("May sixteenth", "May 16"), ("July twenty-third", "July 23"), ("December twenty-second", "December 22"),
 ("January fourth", "January 4"), ("January seventeenth", "January 17"),
 ("nineteen seventy-three", "1973"), ("nineteen seventy-two", "1972"), ("nineteen seventy-one", "1971"), ("nineteen seventy-four", "1974"),
 ("nineteen seventy-five", "1975"), ("nineteen seventy-six", "1976"), ("nineteen seventy-eight", "1978"), ("nineteen sixty-three", "1963"), ("nineteen sixty-five", "1965"), ("nineteen sixty-seven", "1967"), ("K G B", "KGB"),
 ("nineteen sixty-two", "1962"), ("nineteen fifty-nine", "1959"), ("nineteen fifty-eight", "1958"), ("nineteen fifty-three", "1953"),
 ("nineteen fifty-two", "1952"), ("two thousand seven", "2007"), ("thirty-four years", "34 years"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="010", title="The Family Jewels: The CIA's List of Its Own Secrets",
    imgs={k: D + k + ".jpg" for k in ["sch_head", "sch_order", "sch_direct", "sch_page", "att_a", "att_page", "osb_subj", "osb_flap", "osb_page",
                                      "mock1", "mock2", "mock_page", "celotex", "mail", "hunt", "hunt2", "chaos", "chaos2", "rk_title", "rk_members", "rk_unlawful", "rk_mail", "rk_chaos"]},
    credit="Documents: CIA \"Family Jewels\" (1973, released 2007); Rockefeller Commission report (1975).\\NB-roll: U.S. government footage via DVIDS (2012-2026). No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[18, 26], hook="THE CIA'S OWN<br>[SECRET LIST]"),
        dict(id="s2", lines=[30, 38], hook="THE CIA TAPPED<br>[REPORTERS' PHONES]"),
        dict(id="s3", lines=[40, 46], hook="THE CIA OPENED<br>[8,700 ITEMS]<br>OF MAIL"),
        dict(id="s4", lines=[10, 16], hook="THE CIA GAVE HUNT<br>[A WIG]"),
    ],
    yshorts=[
        dict(id="y1", lines=[1, 4], hook="\"CALL MY SECRETARY<br>[(EXTENSION 6363)]\""),
        dict(id="y2", lines=[32, 34], hook="A CIA WIRETAP<br>[ON REPORTERS]"),
        dict(id="y3", lines=[48, 52], hook="\"AGENCY EFFORTS<br>[ARE FOREIGN.]\""),
    ],
)
