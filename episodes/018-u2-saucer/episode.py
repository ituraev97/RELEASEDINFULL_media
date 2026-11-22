# FILE 018 — Why the Man Who Designed the U-2 Believed in Flying Saucers
# Fresh topic: the eighth PURSUE release of UAP files (Department of War, war.gov/UFO, Nov. 20, 2026): 40 documents + 3 videos.
# Main documents (unmodified mirror: archive.org/details/pursue-uap-documents-2026, folder Release_08):
#   DOW-UAP-D206 Lockheed / Kelly Johnson report, Dec. 16, 1953 (index card "Lenticular Cloud") · CIA-UAP-D024/D026/D027/D028 (1952)
#   DOW-UAP-D191 Levelland, Texas (Nov. 2-3, 1957) · DOW-UAP-D193 White Sands (Nov. 3, 1957)
#   DOW-UAP-D183 Reid letter (June 24, 2009) · D185 DIA SAP review (Nov. 2009) · D186 DIA info memo (Dec. 2010) · D188 DWO review (Oct. 2009)
#   DOW-UAP-D172 BAASS Ten Month Report (July 2009): vault section (PDF p. 9), 2010 strategic plan item f (PDF p. 496)
#   DOW-UAP-D165 radar slide (2023) · DVIDS DOW-UAP-PR166 / PR168 / PR169 (CENTCOM videos, 2020 / 2026 / 2023)
# LEGAL: no living private person is named or shown. Witnesses in the 1953 and 1957 files are not named in narration; their names
#   are black-barred on crops (Lockheed crew, Levelland civilians). Named people: Clarence "Kelly" Johnson (d. 1990), Senators Harry Reid
#   (d. 2021) and Daniel Inouye (d. 2012), DIA Director Lt. Gen. Ronald Burgess and Deputy Secretary of Defense William Lynn (officials,
#   in role, exactly as the DIA memo states), Pentagon spokesman Sean Parnell (in role). Company names: Lockheed, BAASS / Bigelow Aerospace
#   (only what the records say). No photos of people.
# COPYRIGHT: U.S. government records and DVIDS public-domain photos/b-roll only; contractor text shown as short excerpts for reporting.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
F = "/home/claude/src/img/"

J = "ACTUAL DOCUMENT · LOCKHEED REPORTS ON A \"FLYING SAUCER\", DEC. 16, 1953 · DOW-UAP-D206 · P. "
JB = J + "{} · BLACK BARS: NAMES WITHHELD BY RELEASED IN FULL"
C24 = "ACTUAL DOCUMENT · CIA MEMO, EXTERNAL RESEARCH PROJECT ON UFOS (1952) · CIA-UAP-D024 · P. 2"
C26 = "ACTUAL DOCUMENT · CIA MEMO, \"FLYING SAUCERS\" (AUG. 1952) · CIA-UAP-D026 · P. 1"
C27 = "ACTUAL DOCUMENT · CIA OSI BRIEFING, \"FLYING SAUCERS\" (AUG. 14, 1952) · CIA-UAP-D027 · P. "
C28 = "ACTUAL DOCUMENT · CIA MEMO, \"FLYING SAUCERS\" (OCT. 13, 1952) · CIA-UAP-D028 · P. 1"
LV = "ACTUAL DOCUMENT · AIR INTELLIGENCE INFORMATION REPORT, LEVELLAND, TEXAS (NOV. 1957) · DOW-UAP-D191 · P. "
WS = "ACTUAL DOCUMENT · AIR INTELLIGENCE INFORMATION REPORT, WHITE SANDS (NOV. 1957) · DOW-UAP-D193 · P. "
R183 = "ACTUAL DOCUMENT · LETTER FROM SEN. HARRY REID (JUNE 24, 2009) · DOW-UAP-D183 · P. 1"
R185 = "ACTUAL DOCUMENT · DIA INFO MEMO, REVIEW OF SAP REQUEST (NOV. 13, 2009) · DOW-UAP-D185 · P. 1"
R186 = "ACTUAL DOCUMENT · DIA INFO MEMO ON AATIP (DEC. 2010) · DOW-UAP-D186 · P. "
R188 = "ACTUAL DOCUMENT · DIA DEFENSE WARNING OFFICE REVIEW (OCT. 30, 2009) · DOW-UAP-D188 · P. "
BA = "ACTUAL DOCUMENT · BAASS TEN MONTH REPORT (JULY 2009) · DOW-UAP-D172 · PDF P. "
RAD = "ACTUAL DOCUMENT · UNRESOLVED RADAR DETECTION, UNITED STATES, 2023 · DOW-UAP-D165"
V166 = "ACTUAL VIDEO · DOW-UAP-PR166 · CENTCOM INFRARED SENSOR, MIDDLE EAST, 2020 · AS RELEASED"
V168 = "ACTUAL VIDEO · DOW-UAP-PR168 · CENTCOM EO/IR SENSOR, MIDDLE EAST, 2026 · AS RELEASED"
V169 = "ACTUAL VIDEO · DOW-UAP-PR169 · CENTCOM EO/IR SENSOR, MIDDLE EAST, 2023 · AS RELEASED"

U2 = "B-ROLL · A U-2 DRAGON LADY, BEALE AIR FORCE BASE, CALIFORNIA, 2023"
U2ALT = "B-ROLL · VIEW FROM A U-2 AT HIGH ALTITUDE, 2026"
U2GOLD = "PHOTO · A U-2 AT SUNSET, BEALE AFB, CALIFORNIA, 2024 · THE CLOUD IN THIS PHOTO IS NOT THE 1953 OBJECT"
U2PINK = "PHOTO · A U-2 AT DUSK, BEALE AFB, CALIFORNIA, 2024"
TU2 = "PHOTO · A TU-2S AT SUNSET, BEALE AFB, CALIFORNIA, 2014"
E2 = "PHOTO · A NAVY E-2 RADAR PLANE AT SUNSET, POINT MUGU, CALIFORNIA, 2022 · NOT THE 1953 AIRCRAFT"
MUGU = "PHOTO · AN ARMY MH-47 CHINOOK AT SUNSET, POINT MUGU, CALIFORNIA, 2022 · NOT THE 1953 OBJECT"
TOWER = "B-ROLL · CONTROL TOWER AT NIGHT, NAVAL AIR STATION POINT MUGU, CALIFORNIA, 2026"
VEGAS = "B-ROLL · LAS VEGAS AT NIGHT, SEEN FROM NELLIS AFB, NEVADA, 2026 · NOT THE PLANNED VAULT SITE"
LUB = "B-ROLL · LUBBOCK, TEXAS, 2020 · ABOUT 30 MILES FROM LEVELLAND"
CAP = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C., 2012"

S_P = "SOURCE: DEPARTMENT OF WAR, PURSUE RELEASE 08 (NOV. 20, 2026); CBS NEWS; FOX LOCAL (NOV. 20, 2026)"
S_J = "SOURCE: LOCKHEED REPORTS IN DOW-UAP-D206 (1953-54)"
S_C = "SOURCE: CIA OSI BRIEFING, AUG. 14, 1952 (CIA-UAP-D027)"
S_L = "SOURCE: AIR INTELLIGENCE INFORMATION REPORT, LEVELLAND (1957), DOW-UAP-D191"
S_A = "SOURCE: DIA MEMOS DOW-UAP-D184, D186, D188 (2009-2010)"
S_V = "SOURCE: BAASS TEN MONTH REPORT (JULY 2009), DOW-UAP-D172, PDF P. 9"
S_R = "SOURCE: DOW-UAP-D165 (2023)"

MAP_CA = dict(kicker="DECEMBER 16, 1953 · ABOUT 5:00 P.M.", title="Two views, one sighting report", bounds=[[-119.75, 33.35], [-117.75, 34.55]],
              points=[dict(ll=[-118.81, 34.15], name="Agoura", sub="JOHNSON'S RANCH"),
                      dict(ll=[-119.12, 34.10], name="Point Mugu", sub="OBJECT, BY HIS ESTIMATE", anchor="end", color="#F2D04B"),
                      dict(ll=[-118.19, 33.77], name="Long Beach", sub="TEST FLIGHT NEARBY"),
                      dict(ll=[-118.33, 34.18], name="Burbank", sub="LOCKHEED")],
              source="SOURCE: DOW-UAP-D206 (1953-54) · MAP: NATURAL EARTH")
MAP_TX = dict(kicker="NOVEMBER 2-3, 1957", title="One weekend, two states", bounds=[[-108.2, 32.0], [-98.8, 35.6]],
              points=[dict(ll=[-102.38, 33.59], name="Levelland, Texas", sub="ENGINE FAILURES REPORTED", color="#F2D04B"),
                      dict(ll=[-106.48, 33.68], name="Trinity Site", sub="ARMY PATROLS"),
                      dict(ll=[-106.65, 35.08], name="Albuquerque, N.M.")],
              source="SOURCE: DOW-UAP-D191, DOW-UAP-D193 (1957) · MAP: NATURAL EARTH")

LINES = [
 # ---------------- COLD OPEN (footage + document) ----------------
 ("The engineer who would design the U-2 spy plane told the Air Force he had watched a flying saucer, | and that he was now more firmly convinced than ever that such devices exist.",
  [I("u2gold", kb="in", focus=[0.62, 0.35], lab=U2GOLD), I("j_believe", kb="in", focus=[0.45, 0.45], lab=J + "7")],
  dict(tag=("AGOURA, CALIFORNIA", "DECEMBER 16, 1953"))),
 ("So what did Kelly Johnson see? | The Air Force wrote one answer on his file: | lenticular cloud. | His company's own test crew, flying near seventeen thousand feet, said it was not a cloud.",
  [C("dv908150", 165.0, lab=U2), I("j_card", kb="in", focus=[0.7, 0.35], lab=J + "1")], {}),
 ("His letter is one of forty documents the Pentagon published on Friday, November twentieth, | in its eighth release of U F O files, along with three new military videos.",
  [C("dv1030274", 2.0, lab=V168)], dict(tag=("WAR.GOV/UFO · RELEASE 08", "NOVEMBER 20, 2026"))),
 ("In the same release: | C I A memos urging that no sign of the agency's interest reach the press or public, | a night in Texas when car engines died, | and a contractor's plan for a buried, camouflaged vault for what it called exotic material or tissue.",
  [I("c26_press", kb="in", focus=[0.5, 0.45], lab=C26), I("lv_engine", kb="in", focus=[0.5, 0.5], lab=LV + "5"), I("v_need", kb="in", focus=[0.45, 0.6], lab=BA + "9")], dict(slow=True)),
 ("Let's open the file.",
  [G("intro", n="018")], dict(gap=0.2)),
 ("",
  [G("title", n="018", t="THE U-2 DESIGNER'S \"SAUCER\"", size=130, sub="What the Eighth UFO Release Actually Says")], dict(gap=0.4)),

 # ---------------- I. THE RANCH ----------------
 ("Start with the man.",
  [G("chapter", n="I", t="The Ranch")], {}),
 ("Clarence Johnson, Kelly to his colleagues, was chief engineer of Lockheed Aircraft Corporation's California division in Burbank.",
  [I("j_cover", kb="in", focus=[0.5, 0.35], lab="ACTUAL DOCUMENT · AIR FORCE COVER LETTER (FEB. 1954) · DOW-UAP-D206 · P. 2")], {}),
 ("Within a few years, his engineers would build the U-2, the high-altitude spy plane, | and later the S R seventy-one.",
  [C("dv908150", 176.0, lab=U2), C("dv1017843", 230.0, lab=U2ALT)], {}),
 ("On Wednesday, December sixteenth, nineteen fifty-three, he and his wife drove out to their ranch, three miles west of Agoura, California. | They arrived at about sundown.",
  [G("map", **MAP_CA)], {}),
 ("At about five o'clock, within two minutes' accuracy, he wrote, | he was looking at the sunset through a large plate-glass window, | when he noticed, above a mountain to the west, what he first thought was a black cloud.",
  [I("j_black", kb="in", focus=[0.45, 0.35], lab=J + "6")], {}),
 ("The whole western sky was gold and red. | He wondered why this one object was so dark, | considering that the sun was behind it.",
  [I("mugu_sun", kb="in", focus=[0.5, 0.4], lab=MUGU), I("j_black", kb="down", focus=[0.5, 0.7], lab=J + "6")], {}),
 ("His first thought was smoke from an aircraft. | But after a few seconds he saw that its outline did not change. | Thinking it was a lenticular cloud, he kept studying it. | It did not move at all for three minutes.",
  [I("j_hover", kb="in", focus=[0.45, 0.4], lab=J + "6")], {}),
 ("He asked his wife for their eight-power binoculars, so he would not have to take his eyes off it. | By then, he wrote, he had recognized it as a so-called saucer.",
  [I("j_hover", kb="down", focus=[0.5, 0.75], lab=J + "6")], {}),
 ("By the time he ran outside and focused, it was moving fast, heading roughly west. | Even through the glasses it looked black and distinct, | but he could make out no detail.",
  [I("u2pink", kb="in", focus=[0.6, 0.5], lab=U2PINK)], {}),
 ("In ninety seconds from the time it started to move, | it had completely disappeared, | in a long shallow climb.",
  [I("j_climb", kb="in", focus=[0.45, 0.35], lab=J + "6")], dict(slow=True)),
 ("He put it roughly over Point Mugu, on the coast. | It always looked like an ellipse, he wrote, | its long axis seven to ten times its short one. | And it looked very large.",
  [I("j_climb", kb="down", focus=[0.5, 0.7], lab=J + "6"), I("mugu_sun", kb="out", focus=[0.5, 0.5], lab=MUGU)], dict(gap=0.9, sil=True)),

 # ---------------- II. THE TEST FLIGHT ----------------
 ("The next morning, the story got stranger.",
  [G("chapter", n="II", t="The Test Flight")], {}),
 ("Johnson was back at work after about a week away. | His chief flight test engineer came into his office with two senior engineers, | and said he had seen a flying saucer the day before.",
  [I("th_kelly", kb="in", focus=[0.45, 0.4], lab=J + "10")], {}),
 ("In the engineer's own memo: | Kelly snapped this up immediately, | said it was at five-oh-five, and that the object was sighted off Point Mugu. | This literally bowled me over.",
  [I("th_kelly", kb="down", focus=[0.5, 0.6], lab=J + "10")], dict(slow=True)),
 ("Because at that moment, the engineer had been in the air. | He was co-pilot on a test flight of a Navy Super Constellation, a W V two radar plane, | which took off at four twenty-nine that afternoon.",
  [I("mugu_e2", kb="in", focus=[0.6, 0.45], lab=E2)], {}),
 ("Somewhere between fifteen and twenty thousand feet, the pilot said: | Look out, there's a flying saucer.",
  [I("th_saucer", kb="in", focus=[0.4, 0.35], lab=JB.format(9))], {}),
 ("They turned straight toward it, expecting to overtake it. | For about five minutes they flew at it, | at some two hundred twenty-five miles an hour. | They did not seem to close the gap.",
  [I("th_speck", kb="in", focus=[0.45, 0.3], lab=JB.format(9))], {}),
 ("To the co-pilot, it had sharp, definite edges, | and looked like a very large flying wing airplane, | silhouetted against the red sky.",
  [I("th_wing", kb="in", focus=[0.45, 0.45], lab=J + "9")], {}),
 ("Then it seemed to get smaller. | In about a minute, he wrote, it reduced in size to a mere speck, | and disappeared, almost due west.",
  [C("dv908150", 386.0, lab=U2), I("th_speck", kb="down", focus=[0.5, 0.7], lab=JB.format(9))], {}),
 ("The pilot wrote his own account. | He estimated the object was at least fifty or sixty miles away, possibly much farther. | It held its sharp outline and definite shape until it disappeared, | so, he wrote, he knew it was not a cloud that dissolved.",
  [I("tu2", kb="in", focus=[0.5, 0.4], lab=TU2)], {}),
 ("The chief aerodynamicist was in the cockpit too. | He argued that because Johnson saw it from the ground, and the crew from the air, | the difference in their positions showed the object had too much depth to be a cloud.",
  [I("co_depth", kb="in", focus=[0.45, 0.45], lab=J + "12")], {}),
 ("And the engineer who first walked into Johnson's office ended with this. | I have been very skeptical of flying saucer stories. | The fact that what Kelly saw and what we saw appear to be identical, | leads me to believe that it was not exactly an illusion.",
  [I("th_skept", kb="in", focus=[0.45, 0.4], lab=J + "10")], dict(gap=0.9, sil=True)),

 # ---------------- III. LENTICULAR CLOUD ----------------
 ("So the reports went to the Air Force. | But not quite the way you would expect.",
  [G("chapter", n="III", t="Lenticular Cloud")], {}),
 ("Johnson's covering letter, dated January twentieth, nineteen fifty-four, is addressed to the Air Technical Intelligence Center at Wright-Patterson Air Force Base, Ohio. | This information, it says, has not been released to the press.",
  [I("j_press", kb="in", focus=[0.45, 0.45], lab=J + "5")], {}),
 ("Yet the Air Force officer who passed the package on, in February, | wrote that Lockheed personnel had handed it to him, explaining that Mr. Johnson was most reluctant to write the report in the first place, | and then refused to forward it.",
  [I("j_cover", kb="in", focus=[0.5, 0.5], lab="ACTUAL DOCUMENT · AIR FORCE COVER LETTER (FEB. 1954) · DOW-UAP-D206 · P. 2")], {}),
 ("The reason, the officer wrote: | Johnson believed that people who profess to have seen flying saucers | are not usually considered to be logical and practical, hard-headed engineers.",
  [I("j_cover", kb="down", focus=[0.5, 0.7], lab="ACTUAL DOCUMENT · AIR FORCE COVER LETTER (FEB. 1954) · DOW-UAP-D206 · P. 2")], dict(slow=True)),
 ("Johnson's own letter shows why he might worry. | For at least five years, he wrote, I have definitely believed in the possibility that flying saucers exist, | in spite of a good deal of kidding from my technical associates.",
  [I("j_believe", kb="in", focus=[0.45, 0.3], lab=J + "7")], {}),
 ("And then the line at the heart of his letter. | Having seen this particular object, | I am now more firmly convinced than ever that such devices exist, | and I have some highly technical converts in this belief.",
  [G("quote", q="I am now {{more firmly convinced than ever that such devices exist}}, and I have some highly technical converts in this belief…",
     who="Clarence L. Johnson", role="Chief Engineer, Lockheed · December 18, 1953", size=58, source=S_J)], dict(slow=True)),
 ("So what did the Air Force conclude? | It is on the file's index card. | Conclusion: other. | Cloud. | Lenticular cloud.",
  [I("j_card", kb="in", focus=[0.75, 0.3], lab=J + "1")], dict(slow=True)),
 ("The card's own summary reads: | first appeared as black stationary cloud, | then rapid movement in long shallow climb. | The card does not say how the analysts squared that movement with a cloud.",
  [I("j_card", kb="down", focus=[0.75, 0.7], lab=J + "1")], {}),
 ("Almost seventy-three years later, the Pentagon has put Johnson's file in its new release, under the heading: | unresolved U A P report.",
  [C("dv908150", 363.0, lab=U2)], dict(gap=0.9, sil=True)),

 # ---------------- IV. NO SHRED OF EVIDENCE ----------------
 ("Why was the Air Force collecting letters like Johnson's at all? | Go back one year.",
  [G("chapter", n="IV", t="No Shred of Evidence")], {}),
 ("In the summer of nineteen fifty-two, the C I A's Office of Scientific Intelligence noted a phenomenal increase in flying saucer reports, | with requests for information pouring in on the Air Force, | including an official query from the White House.",
  [I("c27_head", kb="in", focus=[0.5, 0.4], lab=C27 + "1")], {}),
 ("On August fourteenth, nineteen fifty-two, the office gave a briefing. | Since nineteen forty-seven, it said, there had been about fifteen hundred official reports. | In July alone, two hundred fifty. | The Air Force carried twenty percent as unexplained.",
  [G("stat", k="CIA BRIEFING · AUGUST 14, 1952", a="1,500", size=260, b="official reports since 1947",
     c="250 in July 1952 alone · 20% carried as unexplained", source=S_C)], {}),
 ("Then it walked through the theories. | A secret U S weapon? Denied at the highest level, it said. | A Russian development? | We have absolutely no intelligence of such a technological advance.",
  [I("c27_russ", kb="in", focus=[0.5, 0.45], lab=C27 + "10")], {}),
 ("And the third theory: the man from Mars, space ships, interplanetary travellers. | Even though we might admit that intelligent life may exist elsewhere, the briefing said, | there is no shred of evidence to support this theory at present.",
  [I("c27_mars", kb="in", focus=[0.5, 0.4], lab=C27 + "10")], dict(slow=True)),
 ("Another C I A memo from that August was more careful. | Of one to two thousand reports, it said, | less than one hundred reasonably credible reports remain unexplainable.",
  [I("c26_unexp", kb="in", focus=[0.45, 0.35], lab=C26)], {}),
 ("And as long as some remained unexplainable, | with, in its words, interplanetary aspects and alien origin not being thoroughly excluded from consideration, | caution required that intelligence keep covering the subject.",
  [I("c26_alien", kb="in", focus=[0.5, 0.5], lab=C26)], {}),
 ("Then comes the line that matters most. | It is strongly urged, the memo says, | that no indication of C I A interest or concern reach the press or public, | in view of their probable alarmist tendencies.",
  [I("c26_press", kb="in", focus=[0.5, 0.4], lab=C26)], dict(slow=True)),
 ("The C I A's answer was a panel. | An ad hoc panel of top-level scientists, a memo proposed, | to evaluate the evidence and recommend what further action should be taken. | Estimated cost: about five thousand dollars.",
  [I("c24_panel", kb="in", focus=[0.5, 0.45], lab=C24), I("c24_cost", kb="in", focus=[0.5, 0.4], lab=C24)], {}),
 ("That panel, named after its chairman, the physicist Howard Robertson, met in January nineteen fifty-three, | eleven months before Johnson looked out of his window.",
  [C("dv346026", 4.0, lab=CAP)], dict(gap=0.9, sil=True)),

 # ---------------- V. THE NIGHT THE ENGINES DIED ----------------
 ("Four years later, the reports came from the roads of west Texas. | And this time, there were engines involved.",
  [G("chapter", n="V", t="The Night the Engines Died")], {}),
 ("The night of November second, nineteen fifty-seven. | Levelland, Texas, about thirty miles west of Lubbock.",
  [G("map", **MAP_TX)], {}),
 ("Shortly after midnight, a nineteen-year-old college student was driving home from Lubbock on Texas Highway one sixteen.",
  [C("dv752141", 27.0, lab=LUB)], {}),
 ("His ammeter flicked to discharge. | Then the engine began cutting out, as if it were not getting any gas. | After it quit, the lights and the car radio went out.",
  [I("lv_engine", kb="in", focus=[0.45, 0.4], lab=LV + "5")], {}),
 ("He got out, lifted the hood, found nothing wrong, | and turned around to look for help. | That is when he saw the object.",
  [I("lv_engine", kb="down", focus=[0.5, 0.75], lab=LV + "5")], dict(slow=True)),
 ("Oval-shaped, he told the Air Force, white with a greenish tint, possibly from his tinted windshield, | seventy-five to one hundred feet at its longest. | The report's summary says two witnesses saw an object hovering or resting on the ground, | though the officer's own comments say only this driver described that.",
  [I("lv_sum", kb="in", focus=[0.5, 0.4], lab=LV + "4")], {}),
 ("After four or five minutes, he said, it rose virtually straight up and out of sight. | Then the lights and radio came on, | and the motor started with no difficulty.",
  [I("lv_restart", kb="in", focus=[0.5, 0.5], lab=LV + "5")], {}),
 ("Earlier that night, about four miles outside Levelland, a man driving a truck said a big flame came over his position. | His truck's engine and lights went out. | Because of the heat and the speed, he said, he got out and lay down on the ground. | The investigating officer wrote that his account could not be relied upon.",
  [I("lv_truck", kb="in", focus=[0.5, 0.5], lab=LV + "8")], {}),
 ("Then the investigator found a witness with a very different story. | An Air Force technical sergeant and his wife, driving near Shallowater, saw a bolt of lightning, | and their car's lights and radio went out for one to three seconds.",
  [I("lv_bolt", kb="in", focus=[0.5, 0.5], lab=LV + "14")], {}),
 ("In his words: | that was certainly a strong bolt of lightning to put out our lights and radio.",
  [I("lv_bolt", kb="down", focus=[0.5, 0.7], lab=LV + "14")], dict(slow=True)),
 ("The investigation checked everything it could.",
  [G("list", kicker="LEVELLAND · SUPPLEMENTARY INVESTIGATION", title="What the Air Force checked", items=[
      dict(n="1", t="Air traffic in the area", s="negative"),
      dict(n="2", t="Weather balloons", s="not likely in the area"),
      dict(n="3", t="Downed power lines", s="negative"),
      dict(n="4", t="Weather", s="drizzle · overcast at 400 ft")], source=S_L)], {}),
 ("The officer listed possibilities. | Something like Saint Elmo's fire. | Ball lightning. | Or the glow of excess gas burned at oil fields, reflected off a very low cloud.",
  [I("lv_poss", kb="in", focus=[0.5, 0.45], lab=LV + "21")], {}),
 ("And then he wrote something unusually candid. | It is felt that insufficient knowledge of the above phenomena exists at this organization to completely resolve this sighting. | Therefore, this sighting is forwarded as unresolved.",
  [I("lv_unres", kb="in", focus=[0.5, 0.5], lab=LV + "21")], dict(slow=True)),
 ("The same weekend, more than two hundred miles to the west, | two Army military police patrols at White Sands Proving Ground in New Mexico reported lights of their own.",
  [G("map", **MAP_TX)], {}),
 ("One patrol, at about two-thirty in the morning, | described a very bright object that came down, hung motionless, | and was shaped like an egg. | That evening, a second patrol near the Trinity site, where the first atomic bomb was tested, | watched a bright light rise from the ground.",
  [I("ws_egg", kb="in", focus=[0.5, 0.5], lab=WS + "4")], {}),
 ("The Air Force investigator's opinion was blunt. | The first patrol mistook moonset for an unidentified flying object, | and the second merely witnessed the planet Venus.",
  [I("ws_moon", kb="in", focus=[0.5, 0.5], lab=WS + "8")], dict(gap=0.9, sil=True)),

 # ---------------- VI. THE SENATOR'S PROGRAM ----------------
 ("Now jump forward half a century.",
  [G("chapter", n="VI", t="The Senator's Program")], {}),
 ("In twenty oh-eight, Senators Harry Reid of Nevada and Daniel Inouye of Hawaii sponsored a ten million dollar add to a defense spending bill.",
  [I("a_10m", kb="in", focus=[0.5, 0.35], lab=R186 + "1")], {}),
 ("The agency asked for proposals in twelve technical areas. | Lift. Propulsion. Armament. Signature reduction. | And one called temporal translation.",
  [I("a_bid", kb="in", focus=[0.5, 0.35], lab=R186 + "1")], {}),
 ("It received exactly one bid, | from Bigelow Aerospace Advanced Space Studies, known as B A A S S, | headquartered in North Las Vegas. | The contract was signed on September twenty-second, twenty oh-eight.",
  [I("a_bid", kb="down", focus=[0.5, 0.7], lab=R186 + "1"), C("dv996238", 120.0, lab=VEGAS)], {}),
 ("By September twenty oh-nine, twenty-six technical reports had been delivered. | The release includes the list of their titles.",
  [I("a_titles", kb="in", focus=[0.4, 0.3], lab=R188 + "3")], {}),
 ("Theory and experiments of invisibility cloaking. | Wormholes in space time. | Antigravity for aerospace applications. | Warp drives.",
  [I("a_titles", kb="down", focus=[0.4, 0.75], lab=R188 + "3")], dict(slow=True)),
 ("An internal D I A review that October said all of the reviews it had received were positive, | some exceptionally so.",
  [I("a_positive", kb="in", focus=[0.5, 0.5], lab=R188 + "1")], {}),
 ("In June twenty oh-nine, Senator Reid wrote to the Deputy Secretary of Defense. | The program, he wrote, had made much progress with the identification of several highly sensitive, unconventional aerospace-related findings.",
  [I("a_reid", kb="in", focus=[0.5, 0.35], lab=R183)], {}),
 ("He asked for parts of it to be placed in a restricted special access program, | with a tightly limited list of people allowed to know.",
  [I("a_reid", kb="down", focus=[0.5, 0.75], lab=R183), C("dv346026", 14.0, lab=CAP)], {}),
 ("The D I A reviewed the request. | Its answer, in November twenty oh-nine: | D I A cannot find adequate justification to establish a restricted S A P.",
  [I("a_nosap", kb="in", focus=[0.5, 0.5], lab=R185)], dict(slow=True)),

 # ---------------- VII. THE VAULT ----------------
 ("Months before that answer, in the spring of twenty oh-nine, the contractor had drawn up plans of its own.",
  [G("chapter", n="VII", t="The Vault")], {}),
 ("Its ten-month report, dated July twenty oh-nine, runs to five hundred thirty-eight pages. | Near the front is a section headed: Progress on New B A A S S Facilities.",
  [C("dv996238", 135.0, lab=VEGAS)], {}),
 ("Item one: underground vault. | The need for a highly secure underground vault became apparent, it says, | in line with a priority to pursue and acquire recovered hardware and biological samples, | from the corporate world, and or from private individuals and groups located elsewhere, including Brazil.",
  [I("v_need", kb="in", focus=[0.45, 0.35], lab=BA + "9")], {}),
 ("The administrator recognized, it says, | that there was no highly secure facility to store exotic material or tissue that the organization could obtain.",
  [G("quote", q="…there was no highly secure facility at BAASS to store {{exotic material or tissue}} that the organization could obtain.",
     who="BAASS Ten Month Report", role="July 2009 · released by the Pentagon, Nov. 20, 2026", size=58, source=S_V)], dict(slow=True)),
 ("So the administrator designed one. | An underground facility in North Las Vegas, at the Bigelow Aerospace site, | behind perimeter fencing, razor wire, surveillance cameras, | and twenty-four hour armed guards.",
  [I("v_loc", kb="in", focus=[0.5, 0.4], lab=BA + "9"), C("dv996238", 150.0, lab=VEGAS)], {}),
 ("The plans: | five thousand square feet. | Walls, ceiling and floor three feet thick. | A concrete access tunnel, multiple security doors, at least one of them a thick steel vault door. | Fifteen to twenty feet of earth on top.",
  [G("stat", k="BAASS PLAN · MAY 2009", a="5,000", size=260, b="square feet, underground",
     c="3-ft walls · steel vault door · 15-20 ft of earth above", source=S_V)], {}),
 ("And, the report adds, | any surface structures protruding from the ground will be extensively camouflaged.",
  [I("v_design", kb="in", focus=[0.5, 0.55], lab=BA + "9")], dict(slow=True)),
 ("Deep in the same report is a plan for twenty-ten. | One item is headed: | Launch search to obtain E B E tissue samples.",
  [I("v_ebe", kb="in", focus=[0.4, 0.3], lab=BA + "496")], dict(slow=True)),
 ("Under it, the report quotes one of the B A A S S contractors, from a previous report: | under the hypothesis that biological material of potentially non-human origin has been recovered, | or that biological or chemical agents of currently unknown type have been detected or inferred, | via interagency connections, B A A S S will lobby for access to medical samples for evaluation, | by liaison with such laboratories as the Armed Forces Institute of Pathology.",
  [I("v_ebe", kb="down", focus=[0.5, 0.6], lab=BA + "496")], {}),
 ("Notice the words. | Under the hypothesis. | This passage does not say that any such material was ever found, or that B A A S S ever obtained any.",
  [C("dv996238", 160.0, lab=VEGAS)], {}),
 ("And was the vault ever built? | CBS News, reporting on the release, says there is no public record that it was, | and that later contractor reports released by the Pentagon do not mention it.",
  [C("dv996238", 125.0, lab=VEGAS)], {}),
 ("In November twenty oh-nine, the D I A director, Lieutenant General Ronald Burgess, and Deputy Secretary of Defense William Lynn met with Senator Reid to discuss the program. | In the director's own words: at that time, we determined the reports were of limited value to D I A. | He added that they could be of merit to other organizations.",
  [I("a_limited", kb="in", focus=[0.5, 0.45], lab=R186 + "2")], dict(slow=True)),
 ("According to CBS News, the program ended in twenty twelve.",
  [C("dv346026", 18.0, lab=CAP)], dict(gap=0.9, sil=True)),

 # ---------------- VIII. MACH TWO POINT FIVE ----------------
 ("The newest files are not from the Cold War at all.",
  [G("chapter", n="VIII", t="Mach 2.5")], {}),
 ("In twenty twenty-three, a civil air-surveillance radar in the United States recorded eight detections over eighty-four seconds, | at an estimated fifty-five to seventy thousand feet.",
  [I("r165", kb="in", focus=[0.3, 0.45], lab=RAD), I("r165", kb="in", focus=[0.75, 0.35], lab=RAD)], {}),
 ("Join the dots, and the distance is about thirty-eight and a half miles. | If it was one object, that is a minimum average ground speed of about sixteen hundred fifty miles an hour. | Roughly Mach two point five.",
  [G("stat", k="IF ALL EIGHT DETECTIONS WERE ONE OBJECT", a="1,650", size=260, b="mph minimum · about Mach 2.5",
     c="38.5 miles in 84 seconds · 55,000-70,000 ft", source=S_R)], {}),
 ("But read the slide's own fine print. | The radar swept only once every twelve seconds, | and that, it says, is not sufficient to establish that all eight detections came from the same object, | or that they form a continuous track.",
  [I("r165", kb="in", focus=[0.75, 0.65], lab=RAD)], {}),
 ("Then there are the three new videos, all from U S Central Command in the Middle East. | Twenty twenty: | twenty seconds of infrared. An area of contrast enters from the right.",
  [C("dv1030270", 0.5, lab=V166)], {}),
 ("Twenty twenty-three: | thirteen seconds. The sensor tracks an area of contrast.",
  [C("dv1030277", 0.5, lab=V169)], {}),
 ("Twenty twenty-six: | fifty-four seconds. | Multiple areas of contrast, then two, | and the sensor intermittently loses contact.",
  [C("dv1030274", 5.0, lab=V168)], {}),
 ("Each comes with the same warning: | the description is not an analytical judgment or an investigative conclusion | about what the event was.",
  [C("dv1030270", 9.0, lab=V166)], dict(gap=0.9, sil=True)),

 # ---------------- IX. THE ANSWER ON THE CARD ----------------
 ("So what does the eighth release add up to?",
  [G("chapter", n="IX", t="The Answer on the Card")], {}),
 ("Look at the old reports in it, and many already carry an answer, written decades ago.",
  [G("timeline", kicker="PURSUE RELEASE 08", title="What the old files concluded", events=[
      dict(y="1953", t="Johnson: lenticular cloud"), dict(y="1955", t="Catalina: probable meteor"),
      dict(y="1956", t="Fontana: was aircraft"), dict(y="1957", t="White Sands: moonset, Venus"),
      dict(y="1957", t="Levelland: unresolved"), dict(y="2023", t="Radar: one object not established")], active=4, source=S_P)], {}),
 ("Was aircraft. | Probable meteor. | Moonset, and Venus. | Lenticular cloud.",
  [I("j_card", kb="in", focus=[0.75, 0.35], lab=J + "1")], dict(slow=True)),
 ("The Pentagon still files them as unresolved: | cases where, in the government's words, it is unable to make a definitive determination.",
  [C("dv346026", 8.0, lab=CAP)], {}),
 ("And some of the witnesses were not casual observers. | A man who designed airplanes for a living. | A test crew who, as one of them wrote, were trained to make accurate observations.",
  [C("dv908150", 374.0, lab=U2), I("th_skept", kb="in", focus=[0.5, 0.5], lab=J + "10")], {}),
 ("The files do not say what Kelly Johnson saw over Point Mugu. | And we will not guess beyond them.",
  [I("u2gold", kb="out", focus=[0.5, 0.45], lab=U2GOLD)], {}),
 ("What they do show is a C I A that, in nineteen fifty-two, wanted no indication of its interest to reach the press or public, | and a contractor that, in twenty oh-nine, drew up plans for a buried, camouflaged vault | for exotic material or tissue that, in its words, the organization could obtain.",
  [I("c26_press", kb="in", focus=[0.5, 0.55], lab=C26), I("v_design", kb="in", focus=[0.5, 0.5], lab=BA + "9")], {}),
 ("The Pentagon's spokesman, Sean Parnell, says the department and its partners are already working on the next release.",
  [C("dv346026", 12.0, lab=CAP)], {}),
 ("Every secret has a release date. | Almost seventy-three years on, the answer on Johnson's card has not changed.",
  [I("mugu_sun", kb="in", focus=[0.5, 0.45], lab=MUGU)], dict(slow=True, gap=0.8)),
 ("Here is our question for you. | Johnson's test crew said it was not a cloud. | The Air Force said it was. | Who do you believe, and why? | Tell us in the comments.",
  [I("j_card", kb="in", focus=[0.75, 0.3], lab=J + "1")], {}),
 ("Next file: more records the government has just released.",
  [G("end", n="018")], dict(gap=2.5)),
]

PRON = [("Inouye", "In-no-way"), ("Agoura", "Uh-gor-uh"), ("Mugu", "Moo-goo"), ("Levelland", "Level-land"), ("Shallowater", "Shallow-water"),
        ("Parnell", "Par-nell"), ("Bigelow", "Bigga-low"), ("Burgess", "Bur-jess"), ("ammeter", "am-meter"), ("lenticular", "len-tick-yoo-ler"),
        ("B A A S S", "B A A S S"), ("C I A", "C I A"), ("D I A", "D I A"), ("U F O", "U F O"), ("U A P", "U A P"), ("E B E", "E B E"),
        ("S A P", "S A P"), ("U S", "U S"), ("W V two", "W V two"), ("S R seventy-one", "S R seventy one"), ("Saint Elmo's", "Saint Elmo's")]

DISPLAY = [
 ("C I A's", "CIA's"), ("C I A", "CIA"), ("D I A", "DIA"), ("U F O", "UFO"), ("U A P", "UAP"), ("E B E", "EBE"), ("B A A S S", "BAASS"),
 ("restricted S A P", "restricted SAP"), ("W V two", "WV-2"), ("S R seventy-one", "SR-71"), ("U S Central", "U.S. Central"), ("U S weapon", "U.S. weapon"),
 ("attack on the U S", "attack on the U.S."), ("U S", "U.S."),
 ("nineteen fifty-three", "1953"), ("nineteen fifty-two", "1952"), ("nineteen fifty-four", "1954"), ("nineteen fifty-seven", "1957"),
 ("nineteen forty-seven", "1947"), ("twenty oh-eight", "2008"), ("twenty oh-nine", "2009"), ("twenty-ten", "2010"), ("twenty twelve", "2012"),
 ("twenty twenty-three", "2023"), ("twenty twenty-six", "2026"), ("Twenty twenty-three", "2023"), ("Twenty twenty-six", "2026"), ("Twenty twenty", "2020"),
 ("December sixteenth", "December 16"), ("November twentieth", "November 20"), ("January twentieth", "January 20"), ("August fourteenth", "August 14"),
 ("November second", "November 2"), ("September twenty-second", "September 22"),
 ("seventeen thousand feet", "17,000 feet"), ("fifteen and twenty thousand feet", "15,000 and 20,000 feet"), ("two hundred twenty-five miles", "225 miles"),
 ("fifty or sixty miles", "50 or 60 miles"), ("four twenty-nine", "4:29"), ("five-oh-five", "5:05"), ("eight-power", "8-power"),
 ("seven to ten times", "7 to 10 times"), ("fifteen hundred", "1,500"), ("two hundred fifty", "250"), ("twenty percent", "20 percent"),
 ("one to two thousand", "1,000 to 2,000"), ("less than one hundred", "less than 100"), ("five thousand dollars", "$5,000"),
 ("Highway one sixteen", "Highway 116"), ("nineteen-year-old", "19-year-old"), ("seventy-five to one hundred feet", "75 to 100 feet"),
 ("thirty miles", "30 miles"), ("four miles", "four miles"), ("two hundred miles", "200 miles"), ("two-thirty", "2:30"),
 ("ten million dollar", "$10 million"), ("forty years", "40 years"), ("twenty-six technical", "26 technical"), ("twelve technical", "12 technical"),
 ("five hundred thirty-eight", "538"), ("five thousand square feet", "5,000 square feet"), ("three feet", "3 feet"), ("Fifteen to twenty feet", "15 to 20 feet"),
 ("twenty-four hour", "24-hour"), ("eighty-four seconds", "84 seconds"), ("fifty-five to seventy thousand feet", "55,000 to 70,000 feet"),
 ("thirty-eight and a half miles", "38.5 miles"), ("sixteen hundred fifty miles", "1,650 miles"), ("Mach two point five", "Mach 2.5"),
 ("twelve seconds", "12 seconds"), ("twenty seconds", "20 seconds"), ("thirteen seconds", "13 seconds"), ("fifty-four seconds", "54 seconds"),
 ("seventy-three years", "73 years"), ("forty documents", "40 documents"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="018", title="Why the Man Who Designed the U-2 Believed in Flying Saucers",
    imgs={**{k: D + k + ".jpg" for k in ["j_card", "j_cover", "j_black", "j_hover", "j_climb", "j_believe", "j_press", "th_saucer", "th_wing",
                                         "th_speck", "th_kelly", "th_skept", "co_depth", "c24_panel", "c24_cost", "c26_unexp", "c26_alien",
                                         "c26_press", "c27_head", "c27_risk", "c27_1500", "c27_mars", "c27_russ", "c28_attack", "lv_sum",
                                         "lv_engine", "lv_restart", "lv_truck", "lv_bolt", "lv_power", "lv_poss", "lv_unres", "ws_egg",
                                         "ws_moon", "a_10m", "a_bid", "a_limited", "a_positive", "a_titles", "a_reid", "a_nosap", "v_title",
                                         "v_need", "v_loc", "v_design", "v_ebe", "r165"]},
          **{k: F + k + ".jpg" for k in ["u2gold", "u2pink", "tu2", "mugu_e2", "mugu_sun"]}},
    credit="Documents: Department of War PURSUE Release 08 (war.gov/UFO, Nov. 20, 2026): U.S. Air Force, CIA, DIA, Lockheed and contractor records.\\NPhotos and b-roll: DoD via DVIDS; modern images do not show the events described. No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[11, 16], tpl="blue", hook="THE U-2<br>DESIGNER<br>[SAW THIS]", hs=185),
        dict(id="s2", lines=[50, 54], tpl="yellow", hook="ENGINE DEAD.<br>[LIGHTS OUT.]", hs=185),
        dict(id="s3", lines=[76, 80], tpl="red", hook="A BURIED VAULT FOR<br>[\"EXOTIC MATERIAL<br>OR TISSUE\"]", hs=130, note="A 2009 PLAN IN A CONTRACTOR REPORT · NO PUBLIC RECORD IT WAS BUILT (CBS NEWS)"),
        dict(id="s4", lines=[42, 45], tpl="white", hook="CIA: KEEP IT<br>[FROM THE PRESS]", hs=175),
    ],
    yshorts=[
        dict(id="y1", lines=[1, 2], tpl="yellow", hook="U-2 DESIGNER:<br>[\"A SAUCER\"]", hs=190),
        dict(id="y2", lines=[76, 77], tpl="red", hook="A VAULT FOR<br>[\"EXOTIC MATERIAL<br>OR TISSUE\"]", hs=140, note="A 2009 PLAN IN A CONTRACTOR REPORT · NO PUBLIC RECORD IT WAS BUILT (CBS NEWS)"),
        dict(id="y3", lines=[50, 52], tpl="white", hook="HIS ENGINE<br>[DIED]", hs=210),
    ],
)
