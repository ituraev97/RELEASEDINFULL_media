# FILE 014 — The Berlin Tunnel: The CIA's Spy Tunnel the Soviets Already Knew About
# Format: see episodes/001-navy-videos/episode.py
# Main document: CIA, Clandestine Services Historical Paper No. 150, "The Berlin Tunnel Operation 1952-1956" (written 1967-68),
#   ISCAP release (Appeal 2014-032, doc. 3, declassified Jan. 3, 2022), archive.org item TheBerlinTunnelOperation1952-1956.
#   Page crops and figures from that PDF (PDF page numbers; figure numbers as printed). Text crops: whole lines, padded 16:9.
# Film stills: Universal Newsreel (archive.org, public domain), deinterlaced still frames only (yadif), via kb.py.
# DVIDS clips (public domain): times are in the original files.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
H = "/home/claude/src/img/"

P = "ACTUAL DOCUMENT · CIA, \"THE BERLIN TUNNEL OPERATION 1952-1956\" (1968) · PDF P. "
F = "ACTUAL DOCUMENT · CIA HISTORY (1968), FIG. "
APPA = "ACTUAL DOCUMENT · CIA HISTORY (1968), APPENDIX A · PDF P. "
NR48 = "ARCHIVAL FILM STILL · A U.S. TRANSPORT PLANE, BERLIN AIRLIFT, 1948 · UNIVERSAL NEWSREEL"
NR53T = "ARCHIVAL FILM STILL · SOVIET TANKS IN EAST BERLIN, JUNE 1953, AS SHOWN IN A UNIVERSAL NEWSREEL"
NR53C = "ARCHIVAL FILM STILL · CROWD IN BERLIN, JUNE 1953, AS SHOWN IN A UNIVERSAL NEWSREEL"
AMUS = "B-ROLL · THE ALLIED MUSEUM, BERLIN, 2014"
NIGHT = "B-ROLL · BERLIN AT NIGHT, NOVEMBER 2014"
BALL = "B-ROLL · LIGHTS MARKING THE ROUTE OF THE BERLIN WALL, BERLIN, NOVEMBER 2014"
MAN = "B-ROLL · AIR NATIONAL GUARD TECHNICIANS WORK IN A CABLE MANHOLE, PENNSYLVANIA, 2017"
WH = "B-ROLL · THE WHITE HOUSE, WASHINGTON, D.C., 2012"
CAP = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C., 2012"

S_H = "SOURCE: CIA, CLANDESTINE SERVICES HISTORY, THE BERLIN TUNNEL OPERATION 1952-1956 (1968; ISCAP RELEASE 2022)"
S_C = "SOURCE: CIA, \"BERLIN TUNNEL: AMERICA'S EAR BEHIND THE IRON CURTAIN\" (APRIL 19, 2024)"

LINES = [
 # ---------------- COLD OPEN ----------------
 ("What was the Berlin Tunnel? | It was a secret passage the C I A and British intelligence dug under the border into Soviet East Berlin, to tap the Soviet military's telephone lines.",
  [I("fig9", kb="in", focus=[0.5, 0.5], lab=F + "9 · VIEW OF THE COMPLETED TUNNEL")], dict(tag=("BERLIN", "1955"))),
 ("It was one thousand four hundred seventy-six feet long. | For eleven months and eleven days, it listened.",
  [G("stat", k="THE BERLIN TUNNEL · 1955-1956", a="1,476 FT", size=260, b="dug in secret under the border of East Berlin",
     c="in operation for 11 months and 11 days", source=S_H)], {}),
 ("Then, at about two in the morning on April twenty-second, nineteen fifty-six, Soviet and East German crews digging up a faulty cable broke into the tap chamber. | A hidden microphone picked up their voices.",
  [I("t_0050", kb="in", focus=[0.5, 0.5], lab=APPA + "61")], dict(tag=("EAST BERLIN", "APRIL 22, 1956"))),
 ("For more than thirteen hours it recorded them working out what they had found. | The cable is tapped. | Unless one had seen it for oneself, nobody would believe it.",
  [I("fig15", kb="in", focus=[0.5, 0.5], lab=F + "15 · TARGET CABLES EXPOSED"), I("t_filthy", kb="in", focus=[0.5, 0.5], lab=APPA + "71")], {}),
 ("But the C I A later learned something worse. | The Soviets had known about the tunnel months before the digging even began.",
  [I("t_blake2", kb="in", focus=[0.5, 0.6], lab=P + "48")], dict(slow=True)),
 ("This is the file on the Berlin Tunnel. | The C I A's own secret history of the operation, written in nineteen sixty-eight.",
  [I("cover", kb="in", focus=[0.5, 0.45], lab=P + "1 · COVER PAGE")], {}),
 ("Let's open the file.",
  [G("intro", n="014")], dict(gap=0.2)),
 ("",
  [G("title", n="014", t="THE BERLIN TUNNEL", size=150, sub="The CIA's Spy Tunnel the Soviets Already Knew About")], dict(gap=0.4)),

 # ---------------- I. THE GAP ----------------
 ("It started with a gap.",
  [G("chapter", n="I", t="The Gap")], {}),
 ("In the late nineteen forties, the C I A's history says, American intelligence lost some of its sources, just as the Cold War escalated. | Tapping Soviet phone lines might fill the gaps.",
  [I("nr_c54sky", kb="in", focus=[0.5, 0.45], lab=NR48)], dict(tag=("BERLIN", "1948"))),
 ("Berlin was the place to try. | The city sat deep inside the Soviet zone of Germany. | And according to the C I A, East Berlin was a hub of Soviet communications.",
  [I("fig1", kb="in", focus=[0.5, 0.5], lab=F + "1 · MAP OF BERLIN")], {}),
 ("In nineteen fifty-one, an agent network got inside the East Berlin office of the East German telephone service. | It delivered the details of the Soviet circuits. | Subsequent events, the history says, proved them completely correct.",
  [I("nr_crowd53", kb="in", focus=[0.5, 0.5], lab=NR53C), I("t_agents", kb="in", focus=[0.5, 0.5], lab=P + "7")], {}),
 ("A test tap recorded samples for about six months. | Somewhat ironically, the first actual material recovered was a recording of a student teletypist practicing on the home keys.",
  [I("t_home", kb="in", focus=[0.5, 0.5], lab=P + "9")], {}),
 ("The British had done this before. | In nineteen fifty-one, they told the C I A they had been tapping Soviet cables through tunnels in Vienna for some years. | Berlin, they suggested, might offer the same chance.",
  [I("t_vienna", kb="in", focus=[0.5, 0.5], lab=P + "9"), C("dv372209", 57.5, lab=AMUS)], dict(gap=0.9, sil=True)),

 # ---------------- II. THE WAREHOUSE ----------------
 ("The answer was a warehouse.",
  [G("chapter", n="II", t="The Warehouse")], {}),
 ("The site was in Rudow, on the southeastern edge of the American sector. | Just across the border, under a main road to Schoenefeld airport, ran the target cables.",
  [I("fig3", kb="in", focus=[0.5, 0.5], lab=F + "3 · AERIAL VIEW OF RUDOW SECTION, BERLIN")], dict(tag=("RUDOW, WEST BERLIN", "1953"))),
 ("Three questions remained. | Could a tunnel of about fifteen hundred feet be dug in secret, under a heavily patrolled border? | Where would three thousand tons of sand go? | And what could stand there without raising suspicion?",
  [I("t_q3", kb="down", focus=[0.5, 0.5], lab=P + "15")], {}),
 ("The sand, the history says, haunted the planners for many weeks. | Until someone suggested, facetiously, that they dig a hole and put the dirt in it.",
  [G("quote", q="…the suggestion was made facetiously that we {{\"dig a hole and put the dirt in it.\"}}",
     who="CIA history of the Berlin Tunnel", role="Written 1967-68", size=68, source=S_H + ", P. 7"),
   I("t_dirt", kb="in", focus=[0.5, 0.6], lab=P + "15")], {}),
 ("Local engineers were told it had been decided to try a new type of warehouse, half above the ground and half below. | So the basement was dug under the eyes of the border guards, and we had our hole to put the dirt in.",
  [I("fig4", kb="in", focus=[0.5, 0.5], lab=F + "4 · DIRT IN THE BASEMENT"), I("t_ware", kb="down", focus=[0.5, 0.5], lab=P + "16")], {}),
 ("The C I A's later account says the compound was presented as a U S Air Force radar site.",
  [I("fig6", kb="in", focus=[0.5, 0.5], lab=F + "6 · EAST GERMAN VIEW OF THE COMPOUND")], {}),
 ("The other side watched it closely. | The sight of the Soviets and East Germans standing on top of the tunnel, binoculars focused on the roof, the history says, provided considerable amusement to the people inside.",
  [I("fig5", kb="in", focus=[0.5, 0.5], lab=F + "5 · VOPOS STUDYING THE INSTALLATION"), I("t_bin", kb="in", focus=[0.5, 0.5], lab=P + "19")], dict(gap=0.9, sil=True)),

 # ---------------- III. THE DIG ----------------
 ("Then they had to dig.",
  [G("chapter", n="III", t="The Dig")], {}),
 ("In December nineteen fifty-three, C I A Director Allen Dulles approved the terms for talks with the British. | The Americans would build the site, drive the tunnel and record the signals. | The British would make the taps.",
  [C("dv346124", 12.0, lab=WH), I("t_dec53", kb="in", focus=[0.5, 0.5], lab=P + "19")], dict(tag=("WASHINGTON, D.C.", "DECEMBER 1953"))),
 ("For the digging, Dulles went to the Army. | It chose Lieutenant Colonel Leslie Gross, who built a practice tunnel some one hundred fifty yards long at a high-security base in New Mexico.",
  [I("t_gross", kb="in", focus=[0.5, 0.5], lab=P + "23"), C("dv346026", 6.0, lab=CAP)], {}),
 ("One hundred twenty-five tons of steel tunnel liner crossed East Germany by freight train. | The loss of any package, the history says, could have blown the project.",
  [I("t_steel", kb="in", focus=[0.5, 0.5], lab=P + "34")], {}),
 ("In late August nineteen fifty-four, a shaft was started in the warehouse basement. | Ground water appeared at sixteen feet, instead of the predicted thirty-two.",
  [I("fig13", kb="in", focus=[0.5, 0.5], lab=F + "13 · SHAFT AND TUNNEL ENTRANCE IN WAREHOUSE BASEMENT")], dict(tag=("RUDOW, WEST BERLIN", "AUGUST 1954"))),
 ("The diggers worked behind a steel shield, with horizontal blinds to stop the sand caving in. | Hydraulic jacks pushed it forward, and a new ring of steel liner was bolted in place.",
  [I("fig7", kb="in", focus=[0.5, 0.5], lab=F + "7 · BLINDS ON THE SHIELD"), I("fig8", kb="in", focus=[0.5, 0.5], lab=F + "8 · EXCAVATING USING THE BLINDS")], {}),
 ("Each time East German guards walked their patrol over the tunnel, the digging stopped. | The sand rode back to the basement on trailers behind a converted fork lift.",
  [I("t_patrol", kb="in", focus=[0.5, 0.5], lab=P + "37"), I("fig14", kb="in", focus=[0.5, 0.5], lab=F + "14 · CONVERTED FORK LIFT AND DIRT BOX")], {}),
 ("To fix their position, the engineers organized a baseball game, to knock a ball as far into the East Zone as possible. | It failed, the history says, because of the friendliness of the East German guards, who kept returning the baseball.",
  [I("t_base", kb="in", focus=[0.5, 0.5], lab=P + "40")], dict(slow=True)),
 ("The tunnel was completed on February twenty-eighth, nineteen fifty-five. | One thousand four hundred seventy-six feet. | More than a quarter of a mile.",
  [I("fig16", kb="in", focus=[0.5, 0.45], lab=F + "16 · SCHEMATIC VIEW OF TUNNEL"), I("fig9", kb="down", focus=[0.5, 0.5], lab=F + "9 · VIEW OF THE COMPLETED TUNNEL")], dict(tag=("RUDOW, WEST BERLIN", "FEBRUARY 28, 1955"))),
 ("No one, the history says, had ever tunneled that far in secret, expecting to hit a target two inches in diameter, twenty-seven inches below a main German Soviet highway.",
  [G("quote", q="…hitting a target {{two inches in diameter and 27 inches below}} a main German/Soviet highway.",
     who="CIA history of the Berlin Tunnel", role="Written 1967-68", size=62, source=S_H + ", P. 18")], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE TAP ----------------
 ("Now came the tap.",
  [G("chapter", n="IV", t="The Tap")], {}),
 ("British engineers dug the final shaft up toward the road. | By March twenty-eighth, nineteen fifty-five, the three target cables lay exposed in a chamber just beneath it.",
  [I("fig10", kb="in", focus=[0.5, 0.5], lab=F + "10 · CONSTRUCTION OF THE VERTICAL SHAFT"), I("fig12", kb="in", focus=[0.5, 0.45], lab=F + "12 · VIEW OF CABLES AND TAPS")], {}),
 ("The chamber was insulated so it would not act like a drum. | Even so, the history says, it was a weird sensation to be inside when an iron-shod horse trotted across.",
  [I("t_horse", kb="in", focus=[0.5, 0.35], lab=P + "32 · FOOTNOTE")], {}),
 ("One foggy morning, the chamber microphone picked up dull thuds. | When the fog burned away, East German police had set up a checkpoint right on top. | The officer in charge was stomping his feet to keep warm.",
  [C("dv567511", 24.5, lab=MAN), I("t_horse", kb="in", focus=[0.5, 0.75], lab=P + "32 · FOOTNOTE")], {}),
 ("Everyone knew it would end one day. | The tunnel was mined with demolition charges at the border. | And if it was found, the American posture would be flat denial of any knowledge of the tunnel.",
  [I("fig16", kb="in", focus=[0.35, 0.5], lab=F + "16 · SCHEMATIC VIEW OF TUNNEL"), I("t_denial", kb="in", focus=[0.5, 0.5], lab=P + "43")], {}),
 ("A heavy steel and concrete door sealed the tunnel near its end. | It carried a sign, neatly lettered in German and Cyrillic. | Entry is forbidden by order of the Commanding General.",
  [G("quote", q="{{\"Entry is forbidden by order of the Commanding General.\"}}",
     who="Inscription on the tunnel's \"anti-personnel\" door", role="In German and Cyrillic · as recorded in the CIA history", size=72, source=S_H + ", P. 21, FN. 4")], dict(slow=True)),
 ("The three cables were tapped on May eleventh, May twenty-first, and August second, nineteen fifty-five.",
  [I("fig19", kb="in", focus=[0.5, 0.5], lab=F + "19 · TAPPING BRIDLE"), I("fig18", kb="in", focus=[0.5, 0.5], lab=F + "18 · PRE-AMP CHAMBER")], dict(gap=0.9, sil=True, tag=("EAST BERLIN", "MAY 11, 1955"))),

 # ---------------- V. THE TAKE ----------------
 ("And then they listened.",
  [G("chapter", n="V", t="The Take")], {}),
 ("The three cables held two hundred seventy-three pairs of wires, about twelve hundred channels. | On average, one hundred twenty-one voice circuits and twenty-eight teletype circuits were recorded continuously.",
  [I("t_stats", kb="in", focus=[0.5, 0.5], lab=P + "51")], {}),
 ("About fifty thousand reels of magnetic tape were used. | Some twenty-five tons.",
  [G("stat", k="THE BERLIN TUNNEL · 1955-1956", a="50,000", size=300, b="reels of magnetic tape — some 25 tons", source=S_H + ", P. 25")], {}),
 ("In London, at the peak, three hundred seventeen people worked on the voice tapes. | Three hundred sixty-eight thousand Soviet conversations were fully transcribed. | In Washington, three hundred fifty people worked on the teletype traffic.",
  [I("t_london", kb="in", focus=[0.5, 0.5], lab=P + "51"), C("dv346124", 30.0, lab=WH)], {}),
 ("The reports, code-named Regal, covered Soviet forces in East Germany and Poland, and identified several thousand Soviet officers.",
  [I("nr_tanks53a", kb="in", focus=[0.5, 0.5], lab=NR53T), I("t_officers", kb="in", focus=[0.5, 0.5], lab=P + "76 · APPENDIX B")], {}),
 ("Processing went on until September nineteen fifty-eight, more than two years after the tunnel closed. | The total cost of the project was six point seven million dollars.",
  [G("stat", k="TOTAL COST OF THE PROJECT", a="$6.7M", size=320, b="processing continued until September 30, 1958", source=S_H + ", P. 26"),
   I("t_cost", kb="in", focus=[0.5, 0.5], lab=P + "52")], dict(gap=0.9, sil=True)),

 # ---------------- VI. THE NIGHT ----------------
 ("It ended with rain.",
  [G("chapter", n="VI", t="The Night")], {}),
 ("In April nineteen fifty-six, after heavy rains, cables around Berlin flooded and began to fail. | Soviet signal troops and East German technicians worked frantically to keep communications running.",
  [C("dv373122", 5.5, lab=NIGHT), I("t_rain", kb="in", focus=[0.5, 0.5], lab=APPA + "58")], dict(tag=("BERLIN", "APRIL 1956"))),
 ("At about ten to one on the morning of April twenty-second, the watchers at the site saw forty or fifty men digging along the road, right over the cable.",
  [I("t_0050", kb="in", focus=[0.5, 0.4], lab=APPA + "61")], dict(tag=("SCHOENEFELDER ALLEE, EAST BERLIN", "APRIL 22, 1956"))),
 ("At two o'clock, they found the roof of the tap chamber. | At two ten, Russian speech came through the microphone. | At first, they thought it was a manhole covering a repeater point.",
  [I("fig17", kb="in", focus=[0.5, 0.5], lab=F + "17 · INITIAL STAGE OF CONSTRUCTION OF PRE-AMP CHAMBER")], {}),
 ("By four fifteen, the tone had changed. | One Soviet signals officer told another on the phone, when we speak we must do so carefully. | We know what the matter is.",
  [G("quote", q="\"When we speak we must do so carefully. {{We know what the matter is,}} so we will speak carefully.\"",
     who="Lt. Col. Vyunik, Soviet signals officer, by telephone", role="About 4:15 a.m., April 22, 1956 · as recorded in the CIA history", size=58, source=S_H + ", APPENDIX A, P. 8")], {}),
 ("Early that morning, someone at the hole said it for the first time. | The cable is tapped.",
  [I("t_tapped", kb="in", focus=[0.5, 0.5], lab=APPA + "66")], dict(slow=True)),
 ("They feared a box on the floor was a booby trap. | One officer suggested tearing it away with a grappling iron. | If there is no explosion, he said, then we can calmly go ahead and deal with it.",
  [I("t_boom", kb="in", focus=[0.5, 0.5], lab=APPA + "68")], {}),
 ("Twice they noticed the microphone, and did not recognize it. | The first time, someone said, that is not a microphone.",
  [G("quote", q="{{\"That is not a microphone.\"}}",
     who="Unidentified voice at the tap chamber", role="April 22, 1956 · as recorded in the CIA history", size=86, source=S_H + ", APPENDIX A, P. 12")], {}),
 ("Just before noon, a German worker exclaimed, the box is an entry to a shaft! | The padlock on the trap door was identified as of English origin.",
  [I("t_shaft", kb="in", focus=[0.5, 0.5], lab=APPA + "69"), I("t_eng", kb="in", focus=[0.5, 0.5], lab=APPA + "70")], {}),
 ("Once inside, they were impressed. | It must have cost a pretty penny, one German said. | How neatly and tidily they have done it, said another.",
  [I("fig18", kb="in", focus=[0.6, 0.5], lab=F + "18 · PRE-AMP CHAMBER"), I("t_penny", kb="in", focus=[0.5, 0.5], lab=APPA + "71")], {}),
 ("One German indignantly called it a filthy trick. | Another replied, unless one had seen it for oneself, nobody would believe it.",
  [G("quote", q="\"What a filthy trick…\" — {{\"Unless one had seen it for oneself, nobody would believe it.\"}}",
     who="Two East German workers at the tap chamber", role="April 22, 1956 · as recorded in the CIA history", size=58, source=S_H + ", APPENDIX A, P. 14")], {}),
 ("That afternoon, the tap wires were cut. | At about ten to four, they started dismantling the microphone. | Shortly afterward, it went dead.",
  [I("t_dead", kb="in", focus=[0.5, 0.5], lab=APPA + "72")], dict(gap=0.9, sil=True)),

 # ---------------- VII. THE MOLE ----------------
 ("Then came the twist.",
  [G("chapter", n="VII", t="The Mole")], {}),
 ("The planners expected Moscow to keep quiet. | Instead, the acting Soviet commandant in Berlin, Colonel Ivan Kotsyuba, invited the Berlin press corps on a tour.",
  [I("t_kots", kb="in", focus=[0.5, 0.5], lab=P + "53"), I("fig21", kb="in", focus=[0.5, 0.4], lab=F + "21 · SOVIET PRESS BRIEFING")], dict(tag=("EAST BERLIN", "APRIL 1956"))),
 ("It became, the history says, the most highly publicized peacetime espionage enterprise in modern times before the U two incident. | Worldwide reaction was outstandingly favorable to American prestige.",
  [I("t_pub", kb="in", focus=[0.5, 0.5], lab=P + "54")], {}),
 ("The tunnel's staff concluded the discovery was bad luck. | One old cable in very poor condition, and a long period of unusually heavy rain.",
  [I("t_bad", kb="in", focus=[0.5, 0.5], lab=P + "48")], {}),
 ("But in nineteen sixty-one, British intelligence officer George Blake was arrested as a Soviet agent. | According to the C I A history, he had been recruited while a prisoner in North Korea in nineteen fifty-two.",
  [I("t_blake2", kb="in", focus=[0.5, 0.3], lab=P + "48")], {}),
 ("Blake was privy to the tunnel from the earliest planning stages. | He said he told his Soviet contact about it in late nineteen fifty-three, when its location was decided.",
  [I("t_blake2", kb="down", focus=[0.5, 0.7], lab=P + "48")], dict(slow=True)),
 ("So why did the Soviets let it run for nearly a year? | It is most probable, the C I A wrote in nineteen sixty-eight, that we will never know.",
  [I("t_never", kb="in", focus=[0.5, 0.5], lab=P + "50")], {}),
 ("In twenty twenty-four, the agency went further. | Its public account says the K G B let the tunnel run, then staged the discovery for propaganda.",
  [C("dv372209", 44.2, lab=AMUS)], {}),
 ("A twenty twenty review by a member of the C I A's History Staff agrees with a recent book that the Soviets decided they had to let it operate, to avoid a premature exposure of their source. | And the nineteen sixty-eight history says there was no evidence that the Soviets ever tried to feed deception material through the cables.",
  [I("t_nodec", kb="in", focus=[0.5, 0.55], lab=P + "52")], {}),
 ("Blake was sentenced to forty-two years in prison. | In nineteen sixty-six he escaped from a London prison, and fled to the Soviet Union. | He died in Moscow in twenty twenty.",
  [C("dv373122", 19.0, lab=BALL)], dict(gap=0.9, sil=True)),

 # ---------------- VIII. THE RELEASE ----------------
 ("The paper trail was thin by design.",
  [G("chapter", n="VIII", t="The Release")], {}),
 ("Allen Dulles had ordered that as little as possible about the project be put in writing. | It is probable, the history's author noted, that few orders have been so conscientiously obeyed.",
  [I("t_dulles", kb="in", focus=[0.5, 0.5], lab=P + "3 · PREFACE")], {}),
 ("The history was written in nineteen sixty-eight. | A declassified version came out in two thousand seven. | More of it was declassified on appeal in twenty twenty-two, and the C I A released another copy in twenty twenty-three.",
  [G("timeline", kicker="CLANDESTINE SERVICES HISTORY NO. 150", title="How the file came out",
     events=[dict(y="1968", t="History written"), dict(y="2007", t="First release"),
             dict(y="2022", t="ISCAP declassification"), dict(y="2023", t="CIA re-release"), dict(y="2024", t="CIA public account")],
     source="SOURCES: CIA; ISCAP APPEAL 2014-032; FEDERATION OF AMERICAN SCIENTISTS (2007)")], {}),
 ("So what was the Berlin Tunnel? | A joint American and British wiretap, dug under the border of East Berlin, that recorded hundreds of thousands of Soviet and East German conversations.",
  [I("fig9", kb="in", focus=[0.5, 0.45], lab=F + "9 · VIEW OF THE COMPLETED TUNNEL")], {}),
 ("Betrayed before it was dug. | Found after a long spell of heavy rain. | And, as far as the C I A could tell, never used by the Soviets to feed it false information.",
  [I("fig21", kb="in", focus=[0.5, 0.5], lab=F + "21 · SOVIET PRESS BRIEFING"), C("dv373122", 6.0, lab=NIGHT)], dict(slow=True)),
 ("Every secret has a release date. | For the Berlin Tunnel, the first one came from the Soviets themselves, in April nineteen fifty-six.",
  [I("nr_tanks53b", kb="in", focus=[0.5, 0.5], lab=NR53T)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments.",
  [C("dv567511", 130.0, lab=MAN)], {}),
 ("Next time: another file, released in full.",
  [G("end", n="014", next="Another file, released in full")], dict(gap=2.5)),
]

PRON = [("Rudow", "Roo-doh"), ("Schoenefeld", "Shuh-neh-felt"), ("Schoenefelder Allee", "Shuh-neh-felder Allay"), ("Kotsyuba", "Kot-syoo-bah"),
        ("Vyunik", "Vyoo-nik"), ("V Che", "Vay Chay"), ("Ridgway", "Ridge-way"), ("C I A's", "C I A's"), ("K G B", "K G B"),
        ("U two", "U two"), ("Cyrillic", "Sir-ill-ick"), ("Regal", "Regal"), ("Dulles", "Dull-us"), ("tunneled", "tunnelled")]

DISPLAY = [
 ("C I A's", "CIA's"), ("C I A", "CIA"), ("K G B", "KGB"), ("U S Air Force", "U.S. Air Force"), ("U two", "U-2"), ("V Che", "VChe"),
 ("one thousand four hundred seventy-six feet", "1,476 feet"), ("one thousand four hundred seventy-six", "1,476"),
 ("eleven months and eleven days", "11 months and 11 days"), ("fifteen hundred feet", "1,500 feet"), ("three thousand tons", "3,000 tons"),
 ("one hundred fifty yards", "150 yards"), ("one hundred twenty-five tons", "125 tons"), ("sixteen feet", "16 feet"), ("thirty-two", "32"),
 ("two inches", "two inches"), ("twenty-seven inches", "27 inches"), ("two hundred seventy-three", "273"), ("twelve hundred", "1,200"),
 ("one hundred twenty-one", "121"), ("twenty-eight teletype", "28 teletype"), ("fifty thousand", "50,000"), ("twenty-five tons", "25 tons"),
 ("three hundred seventeen", "317"), ("three hundred sixty-eight thousand", "368,000"), ("three hundred fifty", "350"),
 ("four thousand feet", "4,000 feet"), ("ten feet wide, fifteen feet long and eight feet high", "10 feet wide, 15 feet long and 8 feet high"),
 ("six point seven million dollars", "$6.7 million"), ("forty or fifty", "40 or 50"), ("forty-two years", "42 years"),
 ("thirteen hours", "13 hours"), ("two ten", "2:10"), ("four fifteen", "4:15"), ("ten to one", "12:50"), ("ten to four", "3:50"),
 ("April twenty-second", "April 22"), ("February twenty-eighth", "February 28"), ("March twenty-eighth", "March 28"),
 ("May eleventh", "May 11"), ("May twenty-first", "May 21"), ("August second", "August 2"),
 ("nineteen forties", "1940s"), ("nineteen fifty-one", "1951"), ("nineteen fifty-two", "1952"), ("nineteen fifty-three", "1953"),
 ("nineteen fifty-four", "1954"), ("nineteen fifty-five", "1955"), ("nineteen fifty-six", "1956"), ("nineteen fifty-eight", "1958"),
 ("nineteen sixty-one", "1961"), ("nineteen sixty-six", "1966"), ("nineteen sixty-eight", "1968"),
 ("two thousand seven", "2007"), ("twenty twenty-two", "2022"), ("twenty twenty-three", "2023"), ("twenty twenty-four", "2024"), ("in twenty twenty,", "in 2020,"), ("in twenty twenty.", "in 2020."), ("twenty twenty", "2020"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="014", title="The Berlin Tunnel: The CIA's Spy Tunnel the Soviets Already Knew About",
    imgs=dict({k: D + k + ".jpg" for k in ["fig1", "fig3", "fig4", "fig5", "fig6", "fig7", "fig8", "fig9", "fig10", "fig12", "fig13", "fig14",
                                           "fig15", "fig16", "fig17", "fig18", "fig19", "fig20", "fig21", "cover",
                                           "t_0050", "t_filthy", "t_blake2", "t_vche", "t_agents", "t_home", "t_vienna", "t_q3", "t_dirt",
                                           "t_ware", "t_qm", "t_bin", "t_dec53", "t_gross", "t_steel", "t_patrol", "t_base", "t_horse",
                                           "t_denial", "t_stats", "t_london", "t_officers", "t_cost", "t_rain", "t_tapped", "t_boom",
                                           "t_shaft", "t_eng", "t_penny", "t_dead", "t_kots", "t_pub", "t_bad", "t_never", "t_nodec", "t_dulles"]},
              **{k: H + k + ".jpg" for k in ["nr_c54sky", "nr_crowd53", "nr_tanks53a", "nr_tanks53b"]}),
    credit="Documents and figures: CIA, Clandestine Services History, The Berlin Tunnel Operation 1952-1956 (1968).\\NFilm stills: Universal Newsreel (public domain). B-roll: DoD via DVIDS. Modern b-roll does not show 1950s events. No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[48, 53], hook="THE SOVIETS FOUND THE TAP.<br>[A HIDDEN MIC HEARD THEM]"),
        dict(id="s2", lines=[58, 63], hook="THEY BLAMED THE RAIN.<br>[THEN CAME THE MOLE]"),
        dict(id="s3", lines=[16, 21], hook="WHERE DO YOU HIDE<br>[3,000 TONS OF SAND?]"),
        dict(id="s4", lines=[33, 38], hook="A SECRET ROOM<br>[UNDER A SOVIET ROAD]"),
    ],
    yshorts=[
        dict(id="y1", lines=[52, 55], hook="\"THAT IS NOT<br>[A MICROPHONE.\"]"),
        dict(id="y2", lines=[18, 20], hook="3,000 TONS OF SAND.<br>[WHERE DID IT GO?]"),
        dict(id="y3", lines=[61, 63], hook="THE TUNNEL WAS BETRAYED<br>[BEFORE IT WAS DUG]"),
    ],
)
