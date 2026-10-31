# FILE 003 — Area 51: What the CIA Finally Admitted
# Format: see episodes/001-navy-videos/episode.py
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

U2_23 = "B-ROLL · U-2 DRAGON LADY, BEALE AFB, CALIF., 2023"
U2_26 = "B-ROLL · U-2 DRAGON LADY LANDING, BEALE AFB, CALIF., 2026"
U2_16 = "B-ROLL · MODERN U-2 AT HIGH ALTITUDE, AIR FORCE VIDEO, 2016"
U2_17 = "B-ROLL · U-2 PILOT SUITS UP, BEALE AFB, CALIF., 2017"
SR_MUS = "B-ROLL · SR-71 BLACKBIRD, NATIONAL MUSEUM OF THE U.S. AIR FORCE, 2015"
SR_BEALE = "B-ROLL · SR-71 ON DISPLAY, BEALE AFB, CALIF., 2017"
U2_PS = "B-ROLL · U-2 PILOTS AND SUPPORT CREW, BEALE AFB, CALIF., 2026"
U2_26F = "B-ROLL · U-2 AND T-38s IN FORMATION, BEALE AFB, CALIF., 2026"
U2_24 = "B-ROLL · U-2 TRAINING FLIGHT, BEALE AFB, CALIF., 2024"
U2_ALT = "B-ROLL · VIEW FROM A MODERN U-2 AT HIGH ALTITUDE, AIR FORCE VIDEO, 2026"
HIST = "ACTUAL DOCUMENT · CIA, \"THE CIA AND THE U-2 PROGRAM, 1954–1974\" · 1998 RELEASE"
HAI = "ACTUAL DOCUMENT · G. HAINES, \"CIA'S ROLE IN THE STUDY OF UFOs, 1947–90\" · CIA, 1997"
MAPDOC = "ACTUAL DOCUMENT · CIA MAP OF GROOM LAKE / AREA 51 · RELEASED 2013 (VIA NSARCHIVE)"
USGS = "USGS AERIAL PHOTO · GROOM LAKE, NEV., AUG. 28, 1968"
LSAT = "NASA LANDSAT IMAGE · GROOM LAKE, NEV., c. 2000"
A12 = "U.S. AIR FORCE PHOTO · CIA A-12 (OXCART) IN FLIGHT, 1960s"
YF12B = "NASA PHOTO · TWO YF-12 AIRCRAFT (BLACKBIRD FAMILY, BASED ON THE A-12) IN FLIGHT, 1970s"
YF12 = "NASA PHOTO · YF-12A AND YF-12C, BLACKBIRD FAMILY, IN FLIGHT, 1970s"
D = "/home/claude/src/img/doc/"
SRC_H = "SOURCE: CIA HISTORY \"THE CIA AND THE U-2 PROGRAM, 1954–1974\" (2013 RELEASE, VIA NSARCHIVE)"
NV = dict(kicker="APRIL 1955", title="The search for a test site", bounds=[[-118.9, 33.2], [-114.6, 37.6]],
          points=[dict(ll=[-118.31, 34.18], name="Burbank", sub="LOCKHEED SKUNK WORKS"), dict(ll=[-115.14, 36.17], name="Las Vegas"),
                  dict(ll=[-115.81, 37.25], name="Groom Lake", sub="DRY LAKEBED", color="#F2D04B")],
          areas=[dict(ll=[-116.25, 36.68], r=62)],
          labels=[dict(ll=[-118.25, 36.55], t="NEVADA PROVING GROUND →", size=22)],
          source="SOURCE: CIA U-2 HISTORY, CH. 2 · MAP: NATURAL EARTH · AREAS APPROXIMATE")

NV51 = dict(NV, kicker="AREA 51", title="A name from a map", source="SOURCE: CIA U-2 HISTORY, CH. 2 (2013 RELEASE) · MAP: NATURAL EARTH · AREAS APPROXIMATE",
            points=NV["points"][:2] + [dict(ll=[-115.81, 37.25], name="Groom Lake", sub="AREA 51 · ADDED TO THE NEVADA TEST SITE", color="#F2D04B")])
NV57 = dict(NV, kicker="JUNE 1957", title="A nuclear neighbor", source="SOURCE: CIA U-2 HISTORY (2013 RELEASE) · MAP: NATURAL EARTH · AREAS APPROXIMATE")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("This is page fifty-six of a secret C I A history, the way the agency released it in nineteen ninety-eight.",
  [I("p56", kb="in", focus=[0.5, 0.4], lab=HIST)], dict(tag=("CIA HISTORY", "RELEASED 1998"))),
 ("Under the heading, Preparations for testing the U two, line after line is blacked out.",
  [I("p56b", kb="down", lab=HIST)], {}),
 ("Turn the page, and almost all of it is gone.",
  [I("p57", kb="in", focus=[0.5, 0.35], lab=HIST)], dict(slow=True, gap=0.9, sil=True)),
 ("In two thousand thirteen, the same history came back with fewer redactions. | Behind the black boxes were a map. | And a name.",
  [I("p57b", kb="in", focus=[0.5, 0.4], lab=HIST)], dict(slow=True)),
 ("Area fifty-one.",
  [G("stat", k="CIA U-2 HISTORY · LESS-REDACTED RELEASE, 2013", a="AREA 51", size=240, b="the name under the black boxes", source="SOURCE: NATIONAL SECURITY ARCHIVE, ELECTRONIC BRIEFING BOOK NO. 434, AUG. 15, 2013")], dict(slow=True, gap=0.8, sil=True)),
 ("For decades, it was the most famous secret base in America. So what did the C I A's own historians say actually happened there? | And why, according to them, did so many people see fiery objects in the sky?",
  [C("dv908150", 158.0, lab=U2_23), C("dv908150", 336.0, lab=U2_23)], {}),
 ("Let's open the file.",
  [G("intro", n="003")], dict(gap=0.2)),
 ("",
  [G("title", n="003", t="Area 51", size=170, sub="What the CIA finally admitted")], dict(gap=0.4)),

 # ---------------- I. THE PROBLEM ----------------
 ("The story starts with a problem.",
  [G("chapter", n="I", t="The Problem")], {}),
 ("By the early nineteen-fifties, the Soviet Union had tested an atomic bomb, and then a hydrogen bomb. And American leaders could see very little of what was happening inside its borders.",
  [C("dv1017843", 105.0, lab=U2_PS), C("dv940701", 12.0, lab=U2_24)], {}),
 ("The answer they backed was a plane that could fly higher than Soviet fighters and anti-aircraft guns could reach. Around seventy thousand feet.",
  [C("dv1017843", 141.6, lab=U2_ALT), C("dv995792", 24.0, lab=U2_26F)], {}),
 ("In November nineteen fifty-four, President Eisenhower approved the project. The C I A would run it, with the Air Force. Lockheed would build the plane.",
  [G("timeline", kicker="PROJECT U-2", title="From idea to approval", active=2,
     events=[dict(y="1949", t="Soviet atomic test"), dict(y="AUG 1953", t="Soviet hydrogen bomb test"),
             dict(y="NOV 1954", t="Eisenhower approves the project"), dict(y="AUG 1955", t="Promised first flight")],
     source="SOURCES: CIA U-2 HISTORY, CH. 1; G. HAINES, CIA, 1997")], {}),
 ("Lockheed's designer, Kelly Johnson, ran a secret shop in Burbank, California, known as the Skunk Works. He promised the plane would be flying by August nineteen fifty-five. | About eight months after construction began.",
  [C("dv908150", 38.0, lab=U2_23), C("dv908150", 72.0, lab=U2_23)], {}),
 ("The C I A man in charge was Richard Bissell. And he had a second problem. | Where do you test a plane that isn't supposed to exist?",
  [C("dv908150", 182.0, lab=U2_23), C("dv940701", 100.0, lab=U2_24)], dict(gap=0.8)),

 # ---------------- II. THE RANCH ----------------
 ("In April nineteen fifty-five, they went looking.",
  [G("chapter", n="II", t="The Ranch")], {}),
 ("On April twelfth, Bissell, Air Force Colonel Osmond Ritland, and Kelly Johnson flew over Nevada in a small Beechcraft, piloted by Lockheed's chief test pilot, Tony LeVier.",
  [G("map", **NV)], {}),
 ("They spotted what looked like an airstrip, next to a dry salt flat called Groom Lake. It sat near the northeast corner of the Atomic Energy Commission's Nevada Proving Ground.",
  [G("quote", q="…a salt flat known as {{Groom Lake}}, near the northeast corner of the Atomic Energy Commission's (AEC) Nevada Proving Ground.",
     who="CIA History Staff", role="The CIA and the U-2 Program, ch. 2", size=54, source=SRC_H)], {}),
 ("LeVier set the plane down on the lakebed instead. Good call. According to the history, the old strip had turned into ankle-deep dust. Had he landed on it, the plane would probably have nosed over, killing or injuring all of the key figures in the U two project.",
  [I("p56b", kb="in", focus=[0.5, 0.25], lab=HIST)], {}),
 ("Bissell's group asked the Atomic Energy Commission to add the site to its land in Nevada. | And according to the history, President Eisenhower approved the addition of this strip of wasteland, known by its map designation as Area fifty-one, to the Nevada Test Site.",
  [G("doc", header="CIA HISTORY STAFF · THE CIA AND THE U-2 PROGRAM · CHAPTER 2", title="Preparations for testing the U-2",
     lines=["President Eisenhower also approved the addition of this strip of wasteland,",
            "{{known by its map designation as Area 51,}} to the Nevada Test Site."],
     source=SRC_H + " · EXCERPT, RECREATED")], dict(slow=True)),
 ("That's where the name comes from. Not a code word. A label on a map.",
  [G("map", **NV51)], {}),
 ("To make the place sound more attractive to his workers, Kelly Johnson called it the Paradise Ranch. That was soon shortened to the Ranch. | And when rain flooded the lakebed, the base picked up another unofficial name, Watertown Strip.",
  [G("quote", q="Kelly Johnson called it the {{Paradise Ranch,}} which was soon shortened to the Ranch.", who="CIA History Staff", role="The CIA and the U-2 Program, ch. 2", size=58, source=SRC_H)], {}),
 ("By that summer, the base was ready. Getting people there quietly was another matter. Lockheed workers were flown in on Monday mornings, and back to Burbank on Friday evenings. One project officer nicknamed it Bissell's Narrow-Gauge Airline.",
  [I("p72a", kb="in", focus=[0.5, 0.4], lab=HIST)], {}),
 ("The base had a difficult neighbor. Next door was a nuclear test range. In June nineteen fifty-seven, according to the history, planned atomic tests, whose fallout was expected to contaminate the Groom Lake facility, forced the project to evacuate the base for a time.",
  [G("map", **NV57)], {}),
 ("On November seventeenth, nineteen fifty-five, an Air Force transport bound for the base crashed. All fourteen people aboard were killed. The history calls it the greatest single loss of life in the entire U two program.",
  [I("p72a", kb="down", lab=HIST)], dict(gap=0.9, sil=True)),
 ("But by then, the plane was flying. | In early August, during a taxi test on the lakebed, the U two lifted off before LeVier meant it to. | I had no intentions whatsoever of flying, he said.",
  [C("dv995792", 63.0, lab=U2_26), C("dv908150", 261.5, lab=U2_23)], {}),
 ("The first planned flight came on August fourth. On August eighth, with Bissell watching, came the official first flight. | Kelly Johnson had met his eight-month deadline.",
  [C("dv908150", 360.0, lab=U2_23), C("dv908150", 395.0, lab=U2_23)], {}),
 ("On September eighth, the U two reached sixty-five thousand six hundred feet. The history calls these altitudes never before attained in sustained flight.",
  [I("p71", kb="in", focus=[0.5, 0.7], lab=HIST)], dict(gap=0.8)),

 # ---------------- III. FIERY OBJECTS ----------------
 ("And that's where the UFO part of this story begins.",
  [G("chapter", n="III", t="Fiery Objects")], {}),
 ("The C I A's history gives it its own section. U twos, UFOs, and Operation Blue Book.",
  [I("p72u", kb="in", focus=[0.5, 0.2], lab=HIST)], {}),
 ("In the mid-nineteen-fifties, it says, most airliners flew between ten and twenty thousand feet. Military jets like the B forty-seven stayed below forty thousand. | The U two flew above sixty thousand.",
  [G("alt", kicker="MID-1950s", title="Who flew where", glint=63000,
     bands=[dict(lo=10000, hi=20000, t="AIRLINERS", s="10,000 – 20,000 FT"), dict(lo=20000, hi=40000, t="MILITARY JETS (B-47, B-57)", s="BELOW 40,000 FT"),
            dict(lo=60000, hi=70000, t="U-2", s="ABOVE 60,000 FT", hl=True)],
     source="SOURCE: CIA U-2 HISTORY, P. 72 · ILLUSTRATION, NOT TO SCALE")], {}),
 ("Now picture an airliner flying west at dusk. For its pilot, the sun has already set. But sixty thousand feet up, a U two is still in sunlight.",
  [C("dv1017843", 230.0, lab=U2_ALT), C("dv908150", 212.0, lab=U2_23)], {}),
 ("In the history's words, its silver wings would catch and reflect the rays of the sun, and appear to the airliner pilot, forty thousand feet below, to be fiery objects.",
  [G("quote", q="…its silver wings would catch and reflect the rays of the sun and appear to the airliner pilot, 40,000 feet below, to be {{fiery objects.}}",
     who="CIA History Staff", role="The CIA and the U-2 Program, p. 72", size=52, source=SRC_H)], dict(slow=True)),
 ("That's why the finish mattered. According to Gerald Haines, a C I A historian, the early U twos were silver. They were later painted black.",
  [C("dv908150", 375.0, lab=U2_23), C("dv940701", 160.0, lab=U2_24)], {}),
 ("And at the time, the history adds, no one believed manned flight was possible above sixty thousand feet. So no one expected to see an object that high in the sky.",
  [C("dv1017843", 150.4, lab=U2_ALT), C("dv908150", 300.0, lab=U2_23)], {}),
 ("Pilots reported what they saw. People on the ground wrote letters to the Air Force. Those reports went to Project Blue Book, the Air Force's UFO investigation, based at Wright-Patterson Air Force Base in Ohio.",
  [I("p73", kb="in", focus=[0.5, 0.3], lab=HIST)], {}),
 ("According to the history, Blue Book investigators regularly called the C I A's project staff in Washington, to check sightings against U two flight logs. That let them rule out the majority of the reports. | But they could not tell the letter writers what had really caused them.",
  [I("p73", kb="down", lab=HIST)], {}),
 ("Then comes the line that made headlines in two thousand thirteen, even though it had been public since the nineteen ninety-eight version. | U two and later OXCART flights accounted for more than one-half of all UFO reports, during the late nineteen-fifties and most of the nineteen-sixties.",
  [G("quote", q="U-2 and later OXCART flights accounted for {{more than one-half of all UFO reports}} during the late 1950s and most of the 1960s.",
     who="CIA History Staff", role="The CIA and the U-2 Program, p. 73", size=54, source=SRC_H)], dict(slow=True)),
 ("That claim had appeared before. In nineteen ninety-seven, Haines published it, citing later estimates from C I A officials who had worked on the U two and OXCART projects.",
  [I("h07", kb="in", focus=[0.5, 0.4], lab=HAI)], {}),
 ("Haines went further. This, he wrote, led the Air Force to make misleading and deceptive statements to the public, to allay public fears and to protect an extraordinarily sensitive national security project.",
  [G("quote", q="This led the Air Force to make {{misleading and deceptive statements}} to the public in order to allay public fears and to protect an extraordinarily sensitive national security project.",
     who="Gerald K. Haines", role="CIA historian · Studies in Intelligence, 1997", size=46, source="SOURCE: G. HAINES, \"CIA'S ROLE IN THE STUDY OF UFOs, 1947–90,\" CIA, 1997")], dict(slow=True)),
 ("While perhaps justified, he added, this deception added fuel to the later conspiracy theories.",
  [I("h07q", kb="in", focus=[0.5, 0.5], lab=HAI)], {}),
 ("Haines also noted that the share of sightings the Air Force considered unexplained fell to five point nine percent in nineteen fifty-five, and to four percent in nineteen fifty-six.",
  [G("stat", k="AIR FORCE \"UNEXPLAINED\" UFO SIGHTINGS", a="4%", b="of sightings in 1956", c="down from 5.9 percent in 1955", source="SOURCE: G. HAINES, \"CIA'S ROLE IN THE STUDY OF UFOs, 1947–90,\" CIA, 1997")], {}),
 ("One caution. More than half is, according to Haines, a later estimate by C I A officials who worked on the programs. The released history doesn't list which reports, or show the math. | And it doesn't claim to explain every sighting.",
  [C("dv908150", 218.0, lab=U2_23), C("dv995792", 40.0, lab=U2_26F)], dict(gap=0.9, sil=True)),

 # ---------------- IV. OVERFLIGHT ----------------
 ("Meanwhile, the U two went to work.",
  [G("chapter", n="IV", t="Overflight")], {}),
 ("On July fourth, nineteen fifty-six, a U two made the first overflight of the Soviet Union, over Leningrad. The next day, a second flight passed Moscow. According to the history, when Allen Dulles asked, Bissell told him they had overflown both.",
  [C("dv1017843", 216.6, lab=U2_ALT), C("dv1017843", 240.5, lab=U2_ALT)], dict(tag=("USSR", "JULY 4, 1956"))),
 ("Soviet radar picked up the flights, and fighters went up after them. They couldn't reach the U two. Mission photos showed Soviet fighters climbing toward it, and falling away. | Six days later, Moscow protested, describing the plane as a twin-engine medium bomber.",
  [C("dv908150", 170.0, lab=U2_23), C("dv908150", 192.0, lab=U2_23), C("dv908150", 205.0, lab=U2_23)], {}),
 ("The overflights went on, on and off, for almost four years. | Then, on May first, nineteen sixty, a Soviet surface-to-air missile brought down the U two flown by Francis Gary Powers, near Sverdlovsk.",
  [G("timeline", kicker="U-2 OVER THE USSR", title="Four years of overflights", active=3,
     events=[dict(y="AUG 1955", t="First flight, Nevada"), dict(y="JUL 4, 1956", t="First Soviet overflight"),
             dict(y="JUL 10, 1956", t="Soviet protest note"), dict(y="MAY 1, 1960", t="Powers shot down")],
     source="SOURCE: CIA U-2 HISTORY, CH. 2 – 4")], {}),
 ("President Eisenhower ordered an end to overflights of the Soviet Union. | But the C I A was already working on a successor. A program called OXCART.",
  [C("dv940701", 170.0, lab=U2_24), C("dv908150", 487.0, lab=U2_23)], dict(gap=0.8)),

 # ---------------- V. OXCART ----------------
 ("OXCART was built for speed.",
  [G("chapter", n="V", t="OXCART")], {}),
 ("The plane was the A twelve. It had to fly at Mach three point two, about two thousand one hundred fifty miles an hour, at around ninety-one thousand feet.",
  [I("yf12b", kb="in", focus=[0.5, 0.5], lab=YF12B), C("dv396020", 100.0, lab=SR_MUS)], {}),
 ("At that speed, friction heats the skin. So Lockheed built more than ninety percent of the airframe out of a titanium alloy.",
  [C("dv396020", 270.0, lab=SR_MUS), C("dv396020", 300.0, lab=SR_MUS)], {}),
 ("Like the U two, it was flight-tested in Nevada. On April twenty-fifth, nineteen sixty-two, Lockheed test pilot Lou Schalk took it up for the first time. The official first flight followed five days later.",
  [C("dv640384", 8.0, lab=SR_BEALE), C("dv396020", 430.0, lab=SR_MUS)], {}),
 ("The C I A and the Air Force ordered fifteen OXCART aircraft. | In February nineteen sixty-four, the White House announced a plane called the A eleven, testing at Edwards Air Force Base. What it surfaced was the Air Force's interceptor version, not the C I A's reconnaissance plane.",
  [I("yf12", kb="in", focus=[0.5, 0.5], lab=YF12), C("dv396020", 480.0, lab=SR_MUS)], {}),
 ("The A twelve finally flew operational missions in nineteen sixty-seven, from Okinawa, under the name Black Shield. The first, on May thirty-first, was over North Vietnam.",
  [C("dv396020", 515.0, lab=SR_MUS), C("dv640384", 12.0, lab=SR_BEALE)], dict(tag=("OKINAWA", "MAY 31, 1967"))),
 ("In January nineteen sixty-eight, after North Korea seized the U S S Pueblo, an A twelve flew over North Korea, and photographed the captured ship.",
  [C("dv396020", 360.0, lab=SR_MUS), C("dv396020", 540.0, lab=SR_MUS)], {}),
 ("But the program was already ending. The Air Force had its own reconnaissance version of OXCART, the two-seat SR seventy-one. The A twelve flew its last operational mission in May nineteen sixty-eight.",
  [C("dv396020", 330.0, lab=SR_MUS), C("dv396020", 70.0, lab=SR_MUS)], {}),
 ("The SR seventy-one, the famous Blackbird, became the public face of the family. And the U two, the plane that started it all at Groom Lake, is still flying today.",
  [C("dv640384", 82.0, lab=SR_BEALE), C("dv908150", 440.0, lab=U2_23)], dict(gap=0.9, sil=True)),

 # ---------------- VI. WHAT IT PROVES ----------------
 ("So, what does this file actually prove?",
  [G("chapter", n="VI", t="What It Proves")], {}),
 ("It proves that Area fifty-one began as a C I A test site for the U two, picked from the air in nineteen fifty-five, and named for its designation on a map.",
  [G("map", **NV51)], {}),
 ("It proves that the agency's own historians tied more than half of the UFO reports from that era to its spy planes. | And that, according to Haines, the Air Force misled the public to protect the secret.",
  [I("p72u", kb="up", lab=HIST)], {}),
 ("And it shows how slowly that secret came out. The history was written in nineteen ninety-two. A heavily redacted version was published in nineteen ninety-eight. In two thousand five, the National Security Archive filed a Freedom of Information Act request. | The less redacted version came out in two thousand thirteen.",
  [G("timeline", kicker="THE PAPER TRAIL", title="From secret to released", active=3,
     events=[dict(y="1992", t="History written (classified)"), dict(y="1998", t="Redacted version published"),
             dict(y="2005", t="FOIA request filed"), dict(y="AUG 2013", t="Area 51 references released")],
     source="SOURCE: NATIONAL SECURITY ARCHIVE, ELECTRONIC BRIEFING BOOK NO. 434, 2013")], {}),
 ("What the file doesn't cover matters just as much. It stops in nineteen seventy-four. It says nothing about what was tested at the base after that. | Claims about other work there remain claims. Theories remain theories, until a document says otherwise.",
  [C("dv940701", 120.0, lab=U2_24), C("dv940701", 145.0, lab=U2_24)], dict(slow=True)),
 ("Every secret has a release date. For the C I A to put that name on the record, it took fifty-eight years.",
  [I("p57", kb="out", focus=[0.5, 0.35], lab=HIST)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments. We read every one.",
  [C("dv908150", 465.0, lab=U2_23)], {}),
 ("Next time: the C I A's mind-control program, MKUltra, and the files that survived the shredder.",
  [G("end", n="003", next="MKUltra: The Files That Survived")], dict(gap=2.5)),
]

PRON = [("LeVier", "Le Veer"), ("Ritland", "Ritland"), ("Schalk", "Shawk"), ("OXCART", "ox cart"), ("U twos", "you twos"), ("U two", "you two"),
        ("A twelve", "A twelve"), ("Sverdlovsk", "Sverdlofsk"), ("MKUltra", "M K Ultra"), ("U S S Pueblo", "U S S Pweblo"), ("Wright-Patterson", "Wright Patterson"),
        ("Beechcraft", "Beech craft"), ("allay", "a-lay")]

DISPLAY = [
 ("C I A", "CIA"), ("U twos", "U-2s"), ("U two", "U-2"), ("A twelve", "A-12"), ("A eleven", "A-11"), ("SR seventy-one", "SR-71"), ("B forty-seven", "B-47"),
 ("U S S Pueblo", "USS Pueblo"), ("Area fifty-one", "Area 51"), ("page fifty-six", "page 56"),
 ("nineteen ninety-eight", "1998"), ("nineteen ninety-two", "1992"), ("nineteen ninety-seven", "1997"), ("nineteen seventy-four", "1974"),
 ("nineteen fifty-four", "1954"), ("nineteen fifty-five", "1955"), ("nineteen fifty-six", "1956"), ("nineteen fifty-seven", "1957"), ("nineteen sixty-two", "1962"), ("nineteen sixty-four", "1964"),
 ("nineteen sixty-seven", "1967"), ("nineteen sixty-eight", "1968"), ("nineteen sixty", "1960"), ("nineteen-fifties", "1950s"), ("nineteen-sixties", "1960s"),
 ("two thousand thirteen", "2013"), ("two thousand five", "2005"),
 ("seventy thousand feet", "70,000 feet"), ("sixty-five thousand six hundred feet", "65,600 feet"), ("ninety-one thousand feet", "91,000 feet"),
 ("ten and twenty thousand feet", "10,000 and 20,000 feet"), ("forty thousand feet", "40,000 feet"), ("forty thousand", "40,000"), ("sixty thousand feet", "60,000 feet"), ("sixty thousand", "60,000"),
 ("Mach three point two", "Mach 3.2"), ("two thousand one hundred fifty miles an hour", "2,150 miles an hour"), ("ninety percent", "90 percent"),
 ("April twelfth", "April 12"), ("April twenty-fifth", "April 25"), ("August fourth", "August 4"), ("August eighth", "August 8"), ("September eighth", "September 8"),
 ("November seventeenth", "November 17"), ("July fourth", "July 4"), ("May first", "May 1"), ("May thirty-first", "May 31"),
 ("five point nine percent", "5.9 percent"), ("four percent", "4 percent"), ("fourteen people", "14 people"), ("fifteen OXCART", "15 OXCART"), ("fifty-eight years", "58 years"), ("eight-month", "eight-month"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="003", title="Area 51: What the CIA Finally Admitted",
    imgs={"p56": D + "p56.jpg", "p56b": D + "p56b.jpg", "p57": D + "p57.jpg", "p57b": D + "p57b.jpg", "p71": D + "p71.jpg", "p72a": D + "p72a.jpg", "p72u": D + "p72u.jpg",
          "p73": D + "p73.jpg", "h07": D + "h07.jpg", "h07q": D + "h07q.jpg", "title": D + "title.jpg",
          "yf12": "/home/claude/src/dvimg749221.jpg", "yf12b": "/home/claude/src/dvimg858296.jpg"},
    credit="Documents: CIA history \"The CIA and the U-2 Program, 1954-1974\" (1998 and 2013 releases); G. Haines, CIA, 1997. B-roll: U.S. Air Force via DVIDS (public domain). Appearance of U.S. government visual information does not imply endorsement.",
    shorts=[
        dict(id="s1", lines=[1, 5], hook="THE [BLACK BOX]<br>ON PAGE 57"),
        dict(id="s2", lines=[30, 34], hook="WHY PILOTS SAW<br>[FIERY OBJECTS]"),
        dict(id="s3", lines=[37, 40], hook="[\"MORE THAN HALF\"]<br>OF UFO REPORTS"),
        dict(id="s4", lines=[16, 20], hook="HOW AREA 51<br>GOT ITS [NAME]"),
    ],
)
