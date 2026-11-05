# FILE 008 — 144 Reports, 1 Explained: The Government's First UAP Assessment
# Format: see episodes/001-navy-videos/episode.py
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
H = "/home/claude/src/img/"
PAN = "ODNI, \"PRELIMINARY ASSESSMENT: UNIDENTIFIED AERIAL PHENOMENA\" (JUNE 25, 2021)"
PA = "ACTUAL DOCUMENT · " + PAN
ARN = "ODNI, \"2022 ANNUAL REPORT ON UNIDENTIFIED AERIAL PHENOMENA\" (JAN. 2023)"
AR = "ACTUAL DOCUMENT · " + ARN
S_PA = "SOURCE: " + PAN
S_AR = "SOURCE: " + ARN

PR124 = "OFFICIAL UAP VIDEO · DOW-UAP-PR124, \"UNRESOLVED UAP REPORT, PACIFIC OCEAN, 2019\" · NAVY UAP TASK FORCE FILE, RELEASED 2026"
PR123 = "OFFICIAL UAP VIDEO · DOW-UAP-PR123, \"UNRESOLVED UAP REPORT, PACIFIC OCEAN, 2019\" · NAVY UAP TASK FORCE FILE, RELEASED 2026"
CAP = "B-ROLL · U.S. CAPITOL, WASHINGTON, D.C., 2012"
WH = "B-ROLL · THE WHITE HOUSE, WASHINGTON, D.C., 2012"
F22DC = "B-ROLL · FROM THE COCKPIT OF A U.S. AIR FORCE F-22 OVER WASHINGTON, D.C., 2026"
NIM = "B-ROLL · FLIGHT OPERATIONS ABOARD THE USS NIMITZ, PACIFIC OCEAN, 2026"
GW = "B-ROLL · F/A-18 SUPER HORNETS ABOARD THE USS GEORGE WASHINGTON, 2026"
RIMPAC = "B-ROLL · U.S. NAVY F/A-18F SUPER HORNETS, KANEOHE BAY, HAWAII, 2026"
E2D = "B-ROLL · U.S. NAVY E-2D HAWKEYE RADAR AIRCRAFT, TYNDALL AIR FORCE BASE, FLORIDA, 2026"
WXB = "B-ROLL · U.S. MARINES LAUNCH A WEATHER BALLOON, CAMP PENDLETON, CALIFORNIA, 2022 · NOT THE BALLOON IN THE REPORT"
WXP = "B-ROLL · U.S. AIR FORCE WEATHER BALLOON RELEASED FROM USS PORTLAND, PACIFIC OCEAN, 2022 · NOT THE BALLOON IN THE REPORT"
HAB = "B-ROLL · U.S. ARMY HIGH-ALTITUDE BALLOON LAUNCH, YAKIMA TRAINING CENTER, WASHINGTON, 2025 · NOT THE BALLOON IN THE REPORT"
F22 = "U.S. AIR FORCE PHOTO · AN F-22 TAKES OFF FROM JOINT BASE LANGLEY-EUSTIS, VIRGINIA, FEB. 4, 2023"
DEBRIS = "U.S. NAVY PHOTO · THE BALLOON'S DEBRIS FIELD, ATLANTIC OCEAN, FEB. 4, 2023"
EOD = "U.S. NAVY PHOTO · SAILORS RECOVER THE BALLOON OFF MYRTLE BEACH, SOUTH CAROLINA, FEB. 5, 2023"
EOD2 = "U.S. NAVY PHOTO · RECOVERY OF THE BALLOON OFF MYRTLE BEACH, SOUTH CAROLINA, FEB. 5, 2023"
LCAC = "U.S. NAVY PHOTO · RECOVERED BALLOON MATERIAL, VIRGINIA BEACH, VIRGINIA, FEB. 10, 2023"

FIVE = [dict(n="01", t="Airborne clutter", s="BIRDS · BALLOONS · DRONES · PLASTIC BAGS"),
        dict(n="02", t="Natural atmospheric phenomena", s="ICE CRYSTALS · MOISTURE · THERMAL FLUCTUATIONS"),
        dict(n="03", t="U.S. developmental programs", s="GOVERNMENT OR INDUSTRY · NONE CONFIRMED"),
        dict(n="04", t="Foreign adversary systems", s="CHINA · RUSSIA · ANOTHER NATION · NON-GOVERNMENTAL"),
        dict(n="05", t="\"Other\"", s="A CATCHALL BIN")]

LINES = [
 # ---------------- COLD OPEN ----------------
 ("On June twenty-fifth, twenty twenty-one, Congress got a report it had asked for a year earlier.",
  [C("dv346026", 3.0, lab=CAP)], dict(tag=("WASHINGTON, D.C.", "JUNE 2021"))),
 ("The subject was U A P. Unidentified aerial phenomena. Things in the sky that military crews reported, and nobody could name.",
  [C("dv1017805", 3.0, lab=PR123)], {}),
 ("U S intelligence had gathered one hundred and forty-four reports, from two thousand four to twenty twenty-one.",
  [I("pa_one", kb="in", focus=[0.5, 0.62], lab=PA)], {}),
 ("How many could it explain? | One.",
  [I("pa_one", kb="hold", focus=[0.5, 0.5], lab=PA)], dict(slow=True)),
 ("And that one, the report says, was a large, deflating balloon.",
  [C("dv867753", 42.5, lab=WXB)], {}),
 ("The others, in the report's own words, remain unexplained. | This is U S intelligence's first public U A P assessment. Nine pages. Unclassified.",
  [I("pa_cover", kb="in", focus=[0.5, 0.5], lab=PA)], {}),
 ("Let's open the file.",
  [G("intro", n="008")], dict(gap=0.2)),
 ("",
  [G("title", n="008", t="144 Reports, 1 Explained", size=150, sub="U.S. Intelligence's First Public UAP Assessment")], dict(gap=0.4)),

 # ---------------- I. THE REQUEST ----------------
 ("It started with a request from the Senate.",
  [G("chapter", n="I", t="The Request")], {}),
 ("In June twenty twenty, the Senate Intelligence Committee wrote that it supported a U A P task force at the Office of Naval Intelligence. | But it was concerned. There was, it said, no unified, comprehensive process within the Federal Government for collecting and analyzing this kind of intelligence.",
  [C("dv346026", 12.0, lab=CAP), C("dv346124", 10.0, lab=WH)], {}),
 ("So the committee directed the Director of National Intelligence, working with the Secretary of Defense, to write an assessment. | It was to be unclassified, though it could include a classified annex.",
  [I("pa_scope", kb="in", focus=[0.5, 0.5], lab=PA)], {}),
 ("The Senate's list ran to eight items. | Among them: F B I data on U A P intrusions over restricted U S airspace, and any sign that a potential adversary had achieved breakthrough aerospace capabilities.",
  [C("dv346124", 30.0, lab=WH)], {}),
 ("In August twenty twenty, the Pentagon set up the Unidentified Aerial Phenomena Task Force, with the Navy in the lead. | Its job, the Navy announced, was to detect, analyze and catalog U A P that could pose a threat to U S national security.",
  [C("dv1001705", 4.0, lab=NIM), C("dv1001705", 31.0, lab=NIM)], {}),
 ("The task force and the intelligence community's National Intelligence Manager for Aviation drafted it, with input from more than a dozen agencies and offices, from the F B I and the N S A to the F A A and NOAA.",
  [C("dv1026930", 9.0, lab=F22DC)], {}),
 ("The report was dated June twenty-fifth, twenty twenty-one. | That same day, Deputy Secretary of Defense Kathleen Hicks directed the Pentagon to develop a plan to formalize the task force's mission.",
  [C("dv1026930", 24.0, lab=F22DC), C("dv346026", 20.0, lab=CAP)], dict(gap=0.9, sil=True)),

 # ---------------- II. THE DATASET ----------------
 ("So what was actually in the file?",
  [G("chapter", n="II", t="The Dataset")], {}),
 ("The report admits the problem on its first page of findings. | The limited amount of high-quality reporting, it says, hampers our ability to draw firm conclusions about the nature or intent of U A P.",
  [I("pa_exec", kb="in", focus=[0.5, 0.45], lab=PA)], {}),
 ("Its definition of U A P was broad. Airborne objects, not immediately identifiable.",
  [C("dv1000301", 10.0, lab=NIM)], {}),
 ("For years, there was no system at all. | No standardized reporting mechanism existed, it says, until the Navy established one in March twenty nineteen. The Air Force adopted it in November twenty twenty.",
  [I("pa_navy", kb="in", focus=[0.5, 0.5], lab=PA)], {}),
 ("The task force regularly heard, anecdotally, about other sightings. Ones that were never captured in any formal or informal report.",
  [I("pa_navy", kb="down", focus=[0.5, 0.6], lab=PA)], {}),
 ("The task force focused on reports from military aviators who saw things firsthand, collected from systems it considered reliable. | The incidents ran from November two thousand four to March twenty twenty-one. Most came in the last two years.",
  [C("dv1015995", 63.0, lab=RIMPAC), C("dv1015995", 84.0, lab=RIMPAC)], {}),
 ("One hundred and forty-four reports. Most of the data, the report notes, came from the Navy. Eighty of them involved observation with multiple sensors.",
  [G("stat", k="THE DATASET · NOV. 2004 – MAR. 2021", a="144", size=300, b="UAP reports from U.S. Government sources", c="80 involved observation with multiple sensors", source=S_PA)], {}),
 ("Radar, infrared, electro-optical, weapon seekers, and the human eye. | That is why, the report concludes, most of these probably do represent physical objects.",
  [G("quote", q="Most of the UAP reported {{probably do represent physical objects}} given that a majority of UAP were registered across multiple sensors, to include radar, infrared, electro-optical, weapon seekers, and visual observation.",
     who="Preliminary Assessment", role="Executive summary · June 25, 2021", size=48, source=S_PA)], {}),
 ("And most reports, it says, described them as objects that interrupted pre-planned training or other military activity. | Navy aviators have a name for that. A range fouler.",
  [G("quote", q="…an activity or object that {{interrupts pre-planned training or other military activity}} in a military operating area or restricted airspace.",
     who="U.S. Navy aviators' definition of a \"range fouler\"", role="Preliminary Assessment, Appendix A", size=56, source=S_PA)], dict(gap=0.9, sil=True)),

 # ---------------- III. THE ONE ----------------
 ("And then there was the one they solved.",
  [G("chapter", n="III", t="The One")], {}),
 ("Out of one hundred and forty-four reports, the task force could identify just one with high confidence. | A large, deflating balloon.",
  [C("dv1023102", 44.0, lab=HAB)], dict(slow=True)),
 ("The public report gives no date, no place, and no picture. It does not say whose balloon it was. Just those words.",
  [I("pa_one", kb="down", focus=[0.5, 0.55], lab=PA)], {}),
 ("For everything else, it set out five bins. If and when these incidents are resolved, it says, they will fall into one of five categories.",
  [G("list", kicker="THE FIVE BINS", title="Possible explanations", items=FIVE, source=S_PA)], {}),
 ("Airborne clutter. Birds, balloons, recreational drones, even plastic bags. | Natural atmospheric phenomena. Ice crystals, moisture, and thermal fluctuations that can register on infrared and radar.",
  [I("pa_bins", kb="in", focus=[0.5, 0.3], lab=PA)], {}),
 ("Secret American programs? Possible, the report says. | But it was unable to confirm that any of them accounted for any of the reports it collected.",
  [I("pa_bins", kb="down", focus=[0.5, 0.6], lab=PA)], {}),
 ("Foreign systems, from China, Russia, another nation, or a non-governmental entity. | And a fifth bin, simply called other. For objects that might require, in its words, additional scientific knowledge to understand.",
  [C("dv1007494", 93.2, lab=E2D), C("dv1021582", 29.2, lab=GW)], {}),
 ("Other is not an answer. It is a place to keep a question, pending scientific advances.",
  [C("dv1007494", 43.0, lab=E2D)], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE HANDFUL ----------------
 ("Then came the part that made the headlines.",
  [G("chapter", n="IV", t="The Handful")], {}),
 ("In eighteen incidents, described in twenty-one reports, observers reported unusual movement patterns or flight characteristics.",
  [I("pa_18", kb="in", focus=[0.5, 0.4], lab=PA)], {}),
 ("Some appeared to stay still in winds aloft, move against the wind, maneuver abruptly, or move at considerable speed, without discernable means of propulsion.",
  [I("pa_18", kb="down", focus=[0.5, 0.55], lab=PA)], {}),
 ("In a small number of cases, military aircraft systems processed radio frequency energy associated with the sightings.",
  [C("dv1021582", 2.0, lab=GW), C("dv1021582", 30.0, lab=GW)], {}),
 ("And the task force held, in its words, a small amount of data that appear to show U A P demonstrating acceleration, or a degree of signature management.",
  [G("quote", q="The UAPTF holds a small amount of data that appear to show UAP {{demonstrating acceleration or a degree of signature management.}}",
     who="Preliminary Assessment", role="June 25, 2021", size=56, source=S_PA)], {}),
 ("Additional rigorous analysis, it says, is needed by multiple teams of technical experts. | We are conducting further analysis, the report adds, to determine if breakthrough technologies were demonstrated.",
  [I("pa_sig", kb="in", focus=[0.5, 0.5], lab=PA)], {}),
 ("But the same report hedges, on its first page of findings. | These observations, it says, could be the result of sensor errors, spoofing, or observer misperception, and require additional rigorous analysis.",
  [G("quote", q="These observations {{could be the result of sensor errors, spoofing, or observer misperception}} and require additional rigorous analysis.",
     who="Preliminary Assessment", role="Executive summary · June 25, 2021", size=58, source=S_PA)], {}),
 ("There was also a pattern in where they showed up. U A P sightings tended to cluster around U S training and testing grounds.",
  [I("pa_cluster", kb="in", focus=[0.5, 0.5], lab=PA)], {}),
 ("But the report warns that this may be collection bias. | That is where the newest sensors are, where crews are paying attention, and where they have been told to report anomalies.",
  [C("dv1001705", 40.0, lab=NIM), C("dv1000301", 33.0, lab=NIM)], dict(gap=0.9, sil=True)),

 # ---------------- V. THE HAZARD ----------------
 ("For the military, the most immediate worry was simpler.",
  [G("chapter", n="V", t="The Hazard")], {}),
 ("U A P, the report says, clearly pose a safety of flight issue, and may pose a challenge to U S national security.",
  [I("pa_safety", kb="in", focus=[0.5, 0.45], lab=PA)], {}),
 ("The safety concern, it says, centers on aviators contending with an increasingly cluttered air domain.",
  [C("dv1021582", 40.7, lab=GW)], {}),
 ("The task force had eleven reports of documented instances in which pilots reported near misses with a U A P.",
  [G("stat", k="SAFETY OF FLIGHT", a="11", size=320, b="documented near misses reported by pilots", c="in the task force's dataset", source=S_PA)], {}),
 ("When hazards appear on a range, pilots may stop their training and land. | And that, the report notes, has a deterrent effect on reporting.",
  [I("pa_near", kb="in", focus=[0.5, 0.45], lab=PA)], {}),
 ("There was another reason people stayed quiet. | Aviators and analysts described disparagement for observing U A P, reporting it, or even trying to discuss it with colleagues.",
  [I("pa_stigma", kb="in", focus=[0.5, 0.4], lab=PA)], {}),
 ("Reputational risk, the report says, may keep many observers silent.",
  [G("quote", q="…{{reputational risk may keep many observers silent,}} complicating scientific pursuit of the topic.",
     who="Preliminary Assessment", role="\"UAP Collection Challenges\" · June 25, 2021", size=66, source=S_PA)], {}),
 ("And the sensors themselves were built for other jobs. Those on U S military platforms, it says, are not generally suited for identifying U A P.",
  [C("dv1000301", 50.0, lab=NIM), C("dv1021582", 55.0, lab=GW)], {}),
 ("Cameras give some sense of size, shape, and structure. Radar gives better speed and range. | How many sensors see an object, and from where, the report says, plays a substantial role in telling U A P apart from known objects.",
  [C("dv1015995", 100.8, lab=RIMPAC)], {}),
 ("Was any of it a foreign spy program? The report said it currently lacked data to indicate that. | But it would keep watching, because some U A P had been detected near military facilities, or by aircraft carrying the government's most advanced sensor systems.",
  [I("pa_nsec", kb="in", focus=[0.5, 0.5], lab=PA)], {}),
 ("Its prescription was not dramatic. Standardize the reporting. Consolidate the data. | Then use machine learning to check new reports against known objects, like weather balloons, high-altitude balloons, and wildlife.",
  [C("dv867588", 6.0, lab=WXP), C("dv867588", 30.0, lab=WXP)], {}),
 ("The Air Force had started a six-month pilot program in November twenty twenty. And the task force had begun receiving data from the Federal Aviation Administration.",
  [C("dv1026930", 38.0, lab=F22DC)], dict(gap=0.9, sil=True)),

 # ---------------- VI. WHAT CAME NEXT ----------------
 ("The report asked for more data. It got it.",
  [G("chapter", n="VI", t="What Came Next")], {}),
 ("In July twenty twenty-two, the task force was replaced by a new Pentagon office. The All-domain Anomaly Resolution Office. A A R O. | Congress had required it in the defense bill for fiscal year twenty twenty-two, to coordinate U A P work across the Pentagon and the intelligence community.",
  [I("ar_aaro", kb="in", focus=[0.5, 0.5], lab=AR)], {}),
 ("In January twenty twenty-three, the next annual report counted five hundred and ten U A P reports. More than three times the original number. | Two hundred and forty-seven were new. One hundred and nineteen more were older cases, discovered or reported late.",
  [I("ar_510", kb="in", focus=[0.5, 0.5], lab=AR)], {}),
 ("Part of the rise, the new report said, came from reduced stigma around reporting. | And there had been no reported collisions between U S aircraft and U A P.",
  [I("ar_coll", kb="in", focus=[0.5, 0.5], lab=AR)], {}),
 ("This time, many had a likely answer. One hundred and sixty-three were characterized as balloons, or balloon-like. Twenty-six as drones, or drone-like. Six as clutter. | One hundred and seventy-one were still uncharacterized.",
  [G("stat", k="366 NEWLY IDENTIFIED REPORTS · INITIAL CHARACTERIZATION", a="163", size=300, b="balloons or balloon-like entities", c="26 drones or drone-like · 6 clutter · 171 uncharacterized", source=S_AR)], {}),
 ("The report added a warning. Initial characterization, it says, does not mean positively resolved.",
  [I("ar_163", kb="in", focus=[0.5, 0.6], lab=AR)], {}),
 ("Weeks later, on February fourth, twenty twenty-three, U S fighter aircraft brought down a Chinese high-altitude surveillance balloon over U S territorial waters, off South Carolina.",
  [I("hab_f22", kb="right", focus=[0.5, 0.5], lab=F22), I("hab_debris", kb="in", focus=[0.5, 0.5], lab=DEBRIS)], {}),
 ("Navy divers and sailors spent days recovering what was left of it from the Atlantic.",
  [I("hab_eod", kb="in", focus=[0.5, 0.45], lab=EOD), I("hab_lcac", kb="left", focus=[0.5, 0.5], lab=LCAC)], {}),
 ("The first report's only answer had been a balloon. | Now balloons were the largest group of likely answers.",
  [I("hab_eod2", kb="in", focus=[0.5, 0.5], lab=EOD2)], {}),
 ("In twenty twenty-six, the Pentagon launched a public website for U A P files. Among them, videos that the Navy's task force had handed to its successor office in twenty twenty-two.",
  [C("dv1017805", 44.0, lab=PR123)], {}),
 ("This one was filmed over the Pacific in twenty nineteen. | The release notes are blunt. A hand-held recording of an infrared screen. Not native sensor data. Digitally altered before it was reported, and presented as it was received.",
  [C("dv1017805", 14.0, lab=PR123), C("dv1017805", 34.0, lab=PR123)], {}),
 ("Its official title still carries one word. Unresolved.",
  [C("dv1017805", 56.5, lab=PR123)], dict(gap=0.9, sil=True)),

 # ---------------- VII. STILL UNEXPLAINED ----------------
 ("So what does that first report actually tell us?",
  [G("chapter", n="VII", t="Still Unexplained")], {}),
 ("It does not say where these objects came from. | It says most were probably physical objects, that there are probably several kinds, and that the data was too thin to say what they were.",
  [I("pa_five", kb="in", focus=[0.5, 0.5], lab=PA)], {}),
 ("One hundred and forty-four reports. One explanation. | And a government admitting, on paper, how much it did not know. | Nine pages could not answer the question. But they put it on the record.",
  [I("pa_one", kb="out", focus=[0.5, 0.5], lab=PA)], {}),
 ("Every secret has a release date. This one came with a line on page two. | Data continues to be collected and analyzed.",
  [I("pa_data", kb="out", focus=[0.5, 0.5], lab=PA)], dict(slow=True, gap=0.8)),
 ("If there's a government file you want us to open, tell us in the comments.",
  [C("dv1023102", 50.0, lab=HAB)], {}),
 ("Next time: the night two hydrogen bombs fell on North Carolina. Goldsboro, nineteen sixty-one.",
  [G("end", n="008", next="Goldsboro 1961")], dict(gap=2.5)),
]

PRON = [("U A P", "U A P"), ("A A R O", "A A R O"), ("Goldsboro", "Golds-burrow"), ("discernable", "discernible"),
        ("U S intelligence", "U S intelligence"), ("U S national", "U S national"), ("U S training", "U S training"),
        ("U S military", "U S military"), ("U S fighter", "U S fighter"), ("U S territorial", "U S territorial"),
        ("electro-optical", "electro optical"), ("aloft", "a-loft")]

DISPLAY = [
 ("U S intelligence's", "U.S. intelligence's"), ("U S intelligence", "U.S. intelligence"), ("U S national", "U.S. national"), ("U S training", "U.S. training"),
 ("U S military", "U.S. military"), ("U S fighter", "U.S. fighter"), ("U S territorial", "U.S. territorial"),
 ("F B I", "FBI"), ("N S A", "NSA"), ("F A A", "FAA"), ("U S airspace", "U.S. airspace"), ("U S aircraft", "U.S. aircraft"),
 ("U A P", "UAP"), ("A A R O", "AARO"),
 ("June twenty-fifth", "June 25"), ("February fourth", "February 4"),
 ("twenty twenty-one", "2021"), ("fiscal year twenty twenty-two", "fiscal year 2022"), ("twenty twenty-two", "2022"), ("twenty twenty-three", "2023"), ("twenty twenty-six", "2026"),
 ("twenty twenty", "2020"), ("twenty nineteen", "2019"), ("two thousand four", "2004"), ("nineteen sixty-one", "1961"),
 ("one hundred and forty-four", "144"), ("One hundred and forty-four", "144"), ("five hundred and ten", "510"),
 ("Two hundred and forty-seven", "247"), ("One hundred and nineteen", "119"), ("One hundred and sixty-three", "163"),
 ("One hundred and seventy-one", "171"), ("Twenty-six", "26"), ("twenty-one reports", "21 reports"),
 ("eighteen incidents", "18 incidents"), ("eleven reports", "11 reports"), ("Eighty of them", "80 of them"), ("Six as", "6 as"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="008", title="144 Reports, 1 Explained: U.S. Intelligence's First Public UAP Assessment",
    imgs=dict({k: D + k + ".jpg" for k in ["pa_one", "pa_cover", "pa_scope", "pa_exec", "pa_navy", "pa_bins", "pa_18", "pa_cluster",
                                           "pa_safety", "pa_near", "pa_stigma", "pa_nsec", "pa_five", "pa_sig", "ar_coll", "pa_data", "ar_aaro", "ar_510", "ar_163"]},
              hab_f22=H + "hab_7619707.jpg", hab_debris=H + "hab_7619792.jpg", hab_eod=H + "hab_7620705.jpg",
              hab_lcac=H + "hab_7629315.jpg", hab_eod2=H + "hab_7620700.jpg"),
    credit="Documents: ODNI (2021, 2023). B-roll: U.S. Navy, Marine Corps, Army, Air Force and Department of State via DVIDS. UAP videos: DoD/AARO via DVIDS (released 2026).\\NModern b-roll does not show the incidents in the report. No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[21, 27], hook="144 UAP REPORTS.<br>[ONE EXPLAINED]"),
        dict(id="s2", lines=[34, 41], hook="'UNUSUAL FLIGHT<br>[CHARACTERISTICS]'"),
        dict(id="s3", lines=[42, 51], hook="11 NEAR MISSES<br>[WITH UAP]"),
        dict(id="s4", lines=[56, 62], hook="THEN CAME THE<br>[BALLOONS]"),
    ],
)
