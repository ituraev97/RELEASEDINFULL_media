# FILE 017 — What the Inspector General Found the Night Epstein Died
# Epstein series, part 2 of 4 (death in federal custody, Aug. 10, 2019). Fresh hook: on Nov. 16, 2026 three forensic experts
#   publicly challenged the suicide ruling; the NYC Office of Chief Medical Examiner said it stands by it (CNN via WISN,
#   Al Jazeera, Nov. 16-19, 2026). Also: one year since the Epstein Files Transparency Act; second bill's petition at 218.
# MAIN RECORD: DOJ Office of the Inspector General, "Investigation and Review of the Federal Bureau of Prisons' Custody, Care,
#   and Supervision of Jeffrey Epstein at the Metropolitan Correctional Center in New York, New York", report 23-085, June 2023
#   (oig.justice.gov/sites/default/files/reports/23-085.pdf). Page labels = printed page numbers.
# LEGAL: named living people are only public officials in role (AG Pam Bondi; Reps. Comer, Garcia, Massie, Khanna) and the
#   convicted Ghislaine Maxwell. MCC staff are NOT named (two were charged, charges dismissed after deferred prosecution
#   agreements — said with that outcome); their names are black-barred on every crop. The three experts are not named; their
#   view is attributed and set against the medical examiner's ruling and the IG/FBI findings. No suggestion that any person
#   harmed Epstein. Victims never named; crimes at court-summary level. No method detail beyond "found hanged".
# VISUALS: report pages and report photographs (U.S. government work); DVIDS public-domain b-roll labelled honestly.
#   Not used: report photos of the ligature/cell after death; no photos of any person.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

D = "/home/claude/src/img/doc/"
F = "/home/claude/src/img/"

P = "ACTUAL DOCUMENT · DOJ INSPECTOR GENERAL REPORT 23-085 (JUNE 2023) · P. "
PB = P  # names of staff black-barred by us (note printed on the crop)
EX = "ACTUAL DOCUMENT · DOJ INSPECTOR GENERAL REPORT 23-085 (JUNE 2023) · EXECUTIVE SUMMARY"
FG = "ACTUAL PHOTO · DOJ INSPECTOR GENERAL REPORT 23-085 (2023), FIGURE {} · {}"
NYC = "B-ROLL · LOWER MANHATTAN FROM AN F-22 COCKPIT, NEW YORK CITY, 2025 · THE JAIL IS NOT SHOWN"
NYC2 = "B-ROLL · MANHATTAN FROM AN F-22 COCKPIT, NEW YORK CITY, 2025"
HAR = "B-ROLL · LOWER MANHATTAN FROM NEW YORK HARBOR, JANUARY 2026"
CAP = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C., 2012"
DCA = "B-ROLL · WASHINGTON, D.C., SEEN FROM A MILITARY JET COCKPIT, 2026"

S_IG = "SOURCE: DOJ OFFICE OF THE INSPECTOR GENERAL, REPORT 23-085 (JUNE 2023)"
S_M = "SOURCE: DOJ/FBI MEMO (JULY 2025), AS REPORTED BY AXIOS AND THE NATIONAL NEWS DESK; CBS NEWS (SEPT. 2025, FEB. 2026)"
S_X = "SOURCE: CNN VIA WISN (NOV. 17, 2026); AL JAZEERA (NOV. 18-19, 2026)"
S_H = "SOURCE: NPR (NOV. 10 AND 18, 2026); ABC NEWS AND AXIOS (NOV. 11, 2026)"

LINES = [
 # ---------------- COLD OPEN (the clock) ----------------
 ("How was Jeffrey Epstein left unchecked for almost eight hours, on the last night of his life? | Nobody looked in. | Not once.",
  [I("f_sign", kb="in", focus=[0.5, 0.45], lab=FG.format("5.2", "SIGN IN THE JAIL'S SPECIAL HOUSING UNIT"))], dict(tag=("METROPOLITAN CORRECTIONAL CENTER, NEW YORK", "AUGUST 9-10, 2019"))),
 ("A sign hung on a computer a few steps from his cell said rounds every thirty minutes, as per God.",
  [I("f_sign", kb="out", focus=[0.5, 0.5], lab=FG.format("5.2", "SIGN IN THE JAIL'S SPECIAL HOUSING UNIT"))], {}),
 ("That is not a theory. | It is the finding of the Justice Department's own Inspector General.",
  [I("c_alone", kb="in", focus=[0.5, 0.5], lab=EX)], {}),
 ("And this week, the night is back in the news. | On November sixteenth, twenty twenty-six, three forensic experts said in London that, in their view, his injuries point to strangulation, not suicide.",
  [C("dv977364c", 31.0, lab=NYC)], dict(tag=("NEW YORK CITY", "NOVEMBER 2026"))),
 ("New York City's medical examiner answered the same day: | it stands by its ruling. | Suicide.",
  [G("stat", k="NYC OFFICE OF CHIEF MEDICAL EXAMINER · NOV. 2026", a="STANDS BY", size=210, b="its determination: suicide by hanging", c="as reported by CNN", source=S_X)], {}),
 ("So what does the official record actually say happened inside that jail? | Who was watching, what the cameras saw, and what they didn't?",
  [I("f_cam", kb="in", focus=[0.62, 0.4], lab=FG.format("6.2", "LOCATION OF THE ONE RECORDING SHU CAMERA"))], {}),
 ("We read all one hundred twenty-eight pages.",
  [I("cover", kb="in", focus=[0.5, 0.4], lab="ACTUAL DOCUMENT · DOJ INSPECTOR GENERAL REPORT 23-085 (JUNE 2023) · COVER")], dict(gap=0.2)),
 ("", [G("intro", n="017")], dict(gap=0.2)),
 ("", [G("title", n="017", t="THE LAST NIGHT", size=160, sub="What the Inspector General Found")], dict(gap=0.4)),

 # ---------------- I. NINTH FLOOR ----------------
 ("It starts with an arrest at an airport.",
  [G("chapter", n="I", t="Ninth Floor")], {}),
 ("On July sixth, twenty nineteen, Epstein flew back from France and was arrested at Teterboro Airport in New Jersey, | charged in New York with sex trafficking of minors.",
  [I("c_arrest", kb="in", focus=[0.5, 0.5], lab=P + "21")], dict(tag=("TETERBORO, NEW JERSEY", "JULY 6, 2019"))),
 ("This is part two of our series on the Epstein records. | Part one covered the two thousand seven Florida deal, under which he served less than thirteen months. | This time, a federal judge refused bail, | finding he was a danger to the community and a flight risk.",
  [I("c_bail", kb="in", focus=[0.5, 0.5], lab=P + "21")], {}),
 ("He was taken to the Metropolitan Correctional Center, a federal jail in Lower Manhattan, at one-fifty Park Row.",
  [C("dv977364c", 36.0, lab=NYC)], dict(tag=("LOWER MANHATTAN", "JULY 2019"))),
 ("Because of the media coverage and other inmates' awareness of who he was, | he was moved on July seventh to the Special Housing Unit, | where inmates are locked in their cells about twenty-three hours a day.",
  [I("f_entry", kb="in", focus=[0.5, 0.5], lab=FG.format("4.1", "ENTRANCE TO THE SPECIAL HOUSING UNIT, NINTH FLOOR"))], {}),
 ("The rules there were strict, at least on paper. | Officers had to look at every inmate at least twice an hour. | There were inmate counts through the night, | and cells were to be searched every day.",
  [I("c_rules", kb="in", focus=[0.5, 0.5], lab=EX),
   G("list", kicker="SPECIAL HOUSING UNIT · THE RULES", title="What BOP and jail rules required", items=[
      dict(t="Observe every inmate twice an hour", s="30-MINUTE ROUNDS"), dict(t="Multiple inmate counts every 24 hours"),
      dict(t="A lieutenant's round every shift"), dict(t="Search common areas and 5+ cells daily")], source=S_IG + ", EXECUTIVE SUMMARY")], {}),
 ("Hold on to those rules. | On his last night, the report found, the rounds, the counts and the cell searches were not done as required.",
  [I("f_station", kb="in", focus=[0.6, 0.45], lab=FG.format("4.11", "VIEW OF EPSTEIN'S CELL DOOR FROM THE OFFICERS' STATION"))], dict(gap=0.9, sil=True)),

 # ---------------- II. JULY 23 ----------------
 ("Less than three weeks before he died, there was a warning.",
  [G("chapter", n="II", t="July 23")], {}),
 ("At about one twenty-seven in the morning on July twenty-third, officers heard noise from Epstein's tier. | They found him on the floor with a piece of orange cloth around his neck.",
  [I("c_jul23", kb="in", focus=[0.5, 0.5], lab=P + "29")], dict(tag=("MCC NEW YORK, SPECIAL HOUSING UNIT", "JULY 23, 2019 · 1:27 A.M."))),
 ("His cellmate told officers Epstein had tried to hang himself. | Epstein told an officer something else: | that he thought his cellmate had tried to kill him.",
  [I("c_kill", kb="in", focus=[0.5, 0.5], lab=P + "29")], {}),
 ("Later he said he did not know what happened, and did not want to talk about it. | A staff psychologist wrote that it was unclear whether Epstein had placed the string around his neck, or someone else had. | Another inmate on the tier backed up parts of the cellmate's account, the report says.",
  [I("c_unclear", kb="in", focus=[0.5, 0.5], lab=P + "30")], {}),
 ("Disciplinary charges against Epstein over the incident were not sustained, for insufficient evidence. | And then, the report says, Epstein asked to be housed with that same cellmate again.",
  [I("c_bunkies", kb="in", focus=[0.5, 0.5], lab=P + "32")], {}),
 ("He was placed on suicide watch. | The next day, a psychologist moved him to psychological observation, a step down. | According to her report, he said he had no interest in killing himself.",
  [I("c_nointerest", kb="in", focus=[0.5, 0.5], lab=P + "46")], dict(tag=("MCC NEW YORK", "JULY 24, 2019"))),
 ("Over the next days, according to Bureau of Prisons records, he said he felt the Special Housing Unit was dangerous, | that he could not sleep because of the noise, | and that it was hard to work on his case.",
  [I("f_cell", kb="in", focus=[0.62, 0.5], lab=FG.format("4.10", "INTERIOR OF EPSTEIN'S LATER CELL, PHOTOGRAPHED EMPTY"))], {}),
 ("On July thirtieth, he went back to the unit. | And one condition went with him.",
  [I("f_entry", kb="in", focus=[0.5, 0.5], lab=FG.format("4.1", "ENTRANCE TO THE SPECIAL HOUSING UNIT, NINTH FLOOR"))], dict(gap=0.9, sil=True)),

 # ---------------- III. THE EMAIL ----------------
 ("The condition was a person.",
  [G("chapter", n="III", t="The Email")], {}),
 ("At twelve thirty p m on July thirtieth, the staff psychologist emailed more than seventy jail employees.",
  [I("c_email", kb="in", focus=[0.5, 0.5], lab=P + "32")], dict(tag=("MCC NEW YORK", "JULY 30, 2019 · 12:30 P.M."))),
 ("Inmate Epstein is being taken off psych observation, | and needs to be housed with an appropriate cellmate.",
  [G("doc", header="EMAIL · STAFF PSYCHOLOGIST · JULY 30, 2019 · AS QUOTED BY DOJ OIG", title="To: over 70 MCC New York staff",
     lines=["\"Inmate Epstein #76318-054 is being taken off Psych Observation", "and {{needs to be housed with an appropriate cellmate.}}\""],
     stamp="RECREATED", source=S_IG + ", P. 32")], dict(slow=True)),
 ("The warden told investigators he picked the new cellmate himself, after consulting Bureau of Prisons leadership. | Supervisors and other witnesses said staff regularly assigned to the unit knew Epstein needed a cellmate.",
  [I("c_warden", kb="in", focus=[0.5, 0.5], lab=EX)], {}),
 ("On August eighth, the U S Marshals Service sent two emails to jail staff. | The cellmate was being transferred to another facility the next day.",
  [I("c_marshals", kb="in", focus=[0.5, 0.5], lab=EX)], dict(tag=("MCC NEW YORK", "AUGUST 8, 2019"))),
 ("On August ninth, he left. | No one assigned Epstein a new cellmate.",
  [G("stat", k="AUGUST 9, 2019", a="0", size=360, b="new cellmates assigned", c="despite the psychology department's directive", source=S_IG)], dict(slow=True)),
 ("One of the two staff members on duty that night told investigators she did not know Epstein needed a cellmate. | The Inspector General did not credit that statement.",
  [I("c_credit", kb="in", focus=[0.5, 0.5], lab=PB + "100")], {}),
 ("Others said they had not been told the cellmate was gone, or thought he had only gone to court.",
  [I("f_cell", kb="out", focus=[0.6, 0.5], lab=FG.format("4.10", "INTERIOR OF EPSTEIN'S LATER CELL, PHOTOGRAPHED EMPTY"))], dict(gap=0.9, sil=True)),

 # ---------------- IV. THE CAMERAS ----------------
 ("Meanwhile, something else had already broken.",
  [G("chapter", n="IV", t="The Cameras")], {}),
 ("On July twenty-ninth, according to the F B I's later forensic analysis, the hard drives in one of the jail's video recorders failed.",
  [I("c_dvr", kb="in", focus=[0.5, 0.5], lab=P + "82")], dict(tag=("MCC NEW YORK", "JULY 29, 2019"))),
 ("The cameras kept showing live pictures on the monitors. | But about half of them, including nearly every camera in and around Epstein's unit, stopped recording.",
  [I("f_map", kb="in", focus=[0.4, 0.45], lab=FG.format("6.1", "SHU CAMERA LOCATIONS AND RECORDING STATUS ON AUGUST 10, 2019"))], {}),
 ("Nobody noticed for eleven days. | On August eighth, staff tried to replay some video for an unrelated matter, and found nothing there.",
  [I("c_eleven", kb="in", focus=[0.5, 0.5], lab=P + "109")], {}),
 ("The next day, a technician got the replacement drives. | But, according to him, the officer with the key to the recorder room was going off shift at four, | so the repair was postponed until the following day.",
  [I("c_key", kb="in", focus=[0.5, 0.5], lab=P + "84")], {}),
 ("That following day was August tenth.",
  [I("f_map", kb="in", focus=[0.35, 0.4], lab=FG.format("6.1", "SHU CAMERA LOCATIONS AND RECORDING STATUS ON AUGUST 10, 2019"))], dict(slow=True)),
 ("The problem was not new. | Back in September twenty eighteen, the jail had won approval to replace its entire camera system, | with contracts worth more than seven hundred thirty thousand dollars.",
  [I("c_funding", kb="in", focus=[0.5, 0.5], lab=P + "82"),
   G("stat", k="CAMERA REPLACEMENT · CONTRACTED SEPT. 2018", a="$730,000+", size=230, b="new system still not finished when Epstein died", c="nor by August 2021, the report found", source=S_IG + ", P. 109")], {}),
 ("And it was not just this jail. | Since at least twenty thirteen, the Inspector General had repeatedly warned about broken or missing cameras across the Bureau of Prisons. | By the Bureau's own assessment, forty-five of its one hundred twenty-two institutions needed camera upgrades.",
  [I("c_2013", kb="in", focus=[0.5, 0.5], lab=P + "110")], {}),
 ("So that night, only one camera covering the unit was still recording. | It watched the common area and the stairs up to Epstein's tier. | His cell door was not in its view.",
  [I("f_cam", kb="in", focus=[0.62, 0.45], lab=FG.format("6.2", "LOCATION OF THE ONE RECORDING SHU CAMERA")),
   I("f_still", kb="in", focus=[0.5, 0.5], lab=FG.format("6.4", "STILL FROM THAT CAMERA: STAIRWAY TO L TIER"))], dict(gap=0.9, sil=True)),

 # ---------------- V. AUGUST 9 ----------------
 ("Now, the last day.",
  [G("chapter", n="V", t="August 9")], {}),
 ("On August eighth, Epstein met his lawyers at the jail and signed a new will. | Jail officials did not learn about it until after his death.",
  [I("c_will", kb="in", focus=[0.5, 0.5], lab=P + "50")], dict(tag=("MCC NEW YORK", "AUGUST 8, 2019"))),
 ("The jail's chief psychologist told the Inspector General it would have been a red flag. | She and a staff psychologist said he would probably have been put back on suicide watch, or some kind of observation.",
  [I("c_redflag", kb="in", focus=[0.5, 0.5], lab=P + "50")], {}),
 ("On August ninth, a federal appeals court unsealed about two thousand pages from a civil lawsuit against Ghislaine Maxwell, | the woman later convicted of conspiring with Epstein to sexually abuse minors.",
  [I("c_unseal", kb="in", focus=[0.5, 0.5], lab=P + "50")], dict(tag=("NEW YORK", "AUGUST 9, 2019"))),
 ("The documents, the report says, contained considerable derogatory information about Epstein, | and there was significant media coverage.",
  [C("dv994186c", 19.0, lab=HAR)], {}),
 ("That evening, after another meeting with his lawyers, a jail manager let Epstein make a phone call, from six fifty-eight to seven nineteen p m. | It was unrecorded and unmonitored, in violation of policy.",
  [I("c_call", kb="in", focus=[0.5, 0.5], lab=P + "58")], {}),
 ("Epstein said he was calling his mother. | The report says he had actually called someone with whom he allegedly had a personal relationship. | His mother, it notes elsewhere, was no longer alive.",
  [I("c_mother", kb="in", focus=[0.5, 0.5], lab=P + "108")], {}),
 ("There is one more thing the rules required that day: cell searches. | Only one was documented on August ninth, and it was not of Epstein's cell. | Records did not show when his cell had last been searched.",
  [I("c_search", kb="in", focus=[0.5, 0.5], lab=EX)], {}),
 ("After his death, investigators found excess blankets, linens and clothing in the cell, | which the jail's captain called a security issue.",
  [I("c_linens", kb="in", focus=[0.5, 0.5], lab=P + "109")], {}),
 ("Around eight p m, he was back in his cell on L tier. | Alone.",
  [I("f_empty", kb="in", focus=[0.7, 0.5], lab=FG.format("4.9", "EPSTEIN'S CELL, SEEN THROUGH THE DOOR WINDOW, PHOTOGRAPHED EMPTY"))], dict(slow=True, gap=0.9, sil=True)),

 # ---------------- VI. THE COUNT ----------------
 ("Overnight, the unit was in the hands of very few people.",
  [G("chapter", n="VI", t="The Count")], {}),
 ("One correctional officer worked a double shift, sixteen hours, from four p m to eight a m. | With her until midnight was a material handler, a warehouse worker filling in on overtime.",
  [I("c_shifts", kb="in", focus=[0.5, 0.5], lab=PB + "57")], {}),
 ("By the ten p m count, the report says, he had worked twenty-two hours in a row.",
  [I("c_22", kb="in", focus=[0.5, 0.5], lab=PB + "63"),
   G("stat", k="AT THE 10 P.M. COUNT, AUGUST 9", a="22", size=380, b="consecutive hours on duty", c="one of the two staff members in the unit", source=S_IG + ", P. 63")], {}),
 ("At ten p m, there was supposed to be a count. | Based on the video, witness statements and records, the Inspector General found it did not happen. | The officer told investigators she did the count; the report did not credit that. | The count slip was signed anyway.",
  [I("f_slips", kb="in", focus=[0.5, 0.5], lab=FG.format("5.1", "10 P.M. COUNT SLIPS, AUGUST 9 (SIGNATURES BLURRED IN THE REPORT)"))], dict(tag=("MCC NEW YORK", "AUGUST 9, 2019 · 10 P.M."))),
 ("The ten p m slip listed seventy-three plus one inmates. | Both of them signed it.",
  [I("c_73", kb="in", focus=[0.5, 0.5], lab=PB + "63")], {}),
 ("After about ten forty, no thirty-minute rounds at all. | And no counts: | not at midnight, | not at three, | not at five.",
  [I("f_station", kb="in", focus=[0.6, 0.45], lab=FG.format("4.11", "VIEW OF EPSTEIN'S CELL DOOR FROM THE OFFICERS' STATION"))], dict(slow=True)),
 ("But the round sheets said otherwise. | More than seventy-five separate entries, the report found, recorded rounds that never happened.",
  [I("c_75", kb="in", focus=[0.5, 0.5], lab=PB + "68")], {}),
 ("At midnight, a second material handler took over beside her, also on overtime. | From about one to three a m, the report says, the two sat at the officers' station without moving, and appeared to be sleeping.",
  [I("f_sign", kb="in", focus=[0.5, 0.55], lab=FG.format("5.2", "SIGN HANGING IN THE UNIT ON AUGUST 9 AND 10"))], {}),
 ("The computers tell the rest. | One searched the internet for furniture sales and read a news article about Epstein. | The other looked at motorcycle sales and sports news.",
  [I("c_furniture", kb="in", focus=[0.5, 0.5], lab=PB + "68")], {}),
 ("One of them admitted dozing off from here and there. | The other said she never slept. | She said that when she appears motionless on the video, she was on the computer.",
  [I("c_doze", kb="in", focus=[0.5, 0.5], lab=PB + "67"), I("c_never", kb="in", focus=[0.5, 0.5], lab=PB + "72")], {}),
 ("And all night, a few steps from Epstein's cell, that orange sign was hanging on the computer.",
  [I("f_sign", kb="out", focus=[0.5, 0.5], lab=FG.format("5.2", "SIGN CREATED BY THE DAY WATCH SHU OFFICER IN CHARGE"))], dict(slow=True, gap=0.9, sil=True)),

 # ---------------- VII. 6:30 A.M. ----------------
 ("Then came breakfast.",
  [G("chapter", n="VII", t="6:30 A.M.")], {}),
 ("At about six thirty a m on August tenth, the two began handing out breakfast. | Epstein did not answer at his food slot.",
  [I("c_breakfast", kb="in", focus=[0.5, 0.5], lab=EX)], dict(tag=("MCC NEW YORK, L TIER", "AUGUST 10, 2019 · 6:30 A.M."))),
 ("They opened the door and found him hanged. | They called for help and started chest compressions. | Other staff arrived about a minute later.",
  [I("f_station2", kb="in", focus=[0.6, 0.45], lab=FG.format("4.12", "THE OFFICERS' STATION SEEN FROM EPSTEIN'S CELL"))], {}),
 ("According to the lieutenant who responded, one of them said, we didn't do the rounds, we messed up.",
  [I("c_messed", kb="in", focus=[0.5, 0.5], lab=PB + "72")], dict(slow=True)),
 ("At seven ten, an ambulance took him to New York Presbyterian Lower Manhattan Hospital. | At seven thirty-six a m, he was pronounced dead.",
  [I("c_pronounced", kb="in", focus=[0.5, 0.5], lab=P + "2")], {}),
 ("His criminal case ended without a trial. | In the Inspector General's words, his death deprived his numerous victims, many of whom were underage girls at the time of the alleged crimes, of their ability to seek justice through the criminal justice process.",
  [I("c_victims", kb="in", focus=[0.5, 0.5], lab=EX)], {}),
 ("The next day, the city's medical examiner performed the autopsy. | Cause of death: hanging. | Manner: suicide. | No medications or illegal drugs were found in his blood.",
  [G("doc", header="OFFICE OF CHIEF MEDICAL EXAMINER, CITY OF NEW YORK · AUG. 11, 2019 · AS REPORTED BY DOJ OIG",
     title="Autopsy findings", lines=["Cause of death: {{hanging}}", "Manner of death: {{suicide}}", "Toxicology: no medications or illegal drugs"],
     stamp="RECREATED", source=S_IG + ", EXECUTIVE SUMMARY")], {}),
 ("Hold on to that ruling. | Seven years later, it is the one being challenged.",
  [C("dv977364c", 40.0, lab=NYC2)], dict(gap=0.9, sil=True)),

 # ---------------- VIII. THE FINDINGS ----------------
 ("The Inspector General published its report in June twenty twenty-three.",
  [G("chapter", n="VIII", t="The Findings")], {}),
 ("It found negligence, misconduct, and outright job performance failures. | The failure to assign a cellmate, the missed rounds and counts, and the excess linens left Epstein unmonitored and alone, | which, in the report's words, provided him an opportunity to commit suicide.",
  [I("c_findings", kb="in", focus=[0.5, 0.5], lab=EX)], {}),
 ("And it said something else. | This is not the first time, the report noted, that it had found significant job performance and management failures at the Bureau of Prisons, | and widespread disregard of the policies meant to keep inmates safe.",
  [I("c_notfirst", kb="in", focus=[0.5, 0.5], lab=EX)], {}),
 ("The two staff members on duty were charged with falsifying records. | The charges were later dismissed after they completed deferred prosecution agreements. | Prosecutors declined to charge other employees who had made false entries.",
  [I("c_dpa", kb="in", focus=[0.5, 0.5], lab=EX)], {}),
 ("And on the question everyone asks, the Inspector General went to the video.",
  [I("f_still2", kb="in", focus=[0.5, 0.5], lab=FG.format("6.5", "STILL FROM THE RECORDING CAMERA: VIEW OF THE OFFICERS' STATION"))], {}),
 ("Between about ten forty p m and six thirty a m, | no one was seen entering Epstein's tier from the common area.",
  [I("c_noone", kb="in", focus=[0.5, 0.5], lab=EX)], dict(slow=True)),
 ("It found no evidence that anyone other than the locked-in inmates was present in Epstein's area that night, | and nothing contradicting the F B I's determination that there was no criminality in how he died.",
  [I("c_contradict", kb="in", focus=[0.5, 0.5], lab=EX)], {}),
 ("Staff, and three inmates with a direct line of sight to his cell door, said no one went in or out after he was locked in that evening.",
  [I("c_sight", kb="in", focus=[0.5, 0.5], lab=EX)], {}),
 ("The medical examiner told investigators his injuries were consistent with suicide by hanging, | with no defensive wounds, no marks on his hands, and nothing under his fingernails that would suggest a fight.",
  [I("c_me", kb="in", focus=[0.5, 0.5], lab=EX)], {}),
 ("The report ended with eight recommendations to the Bureau of Prisons. | The first: assign a cellmate after suicide watch, unless there is a reason not to. | The jail itself had already been temporarily closed, in October twenty twenty-one, over conditions the report calls unrelated.",
  [C("dv994186c", 54.5, lab=HAR)], dict(gap=0.9, sil=True)),

 # ---------------- IX. THE MISSING MINUTE ----------------
 ("Two years later, the video came back.",
  [G("chapter", n="IX", t="The Missing Minute")], {}),
 ("In July twenty twenty-five, the Justice Department and the F B I released a two-page memo, and the footage from that one camera.",
  [C("dv1026930c", 26.0, lab=DCA)], dict(tag=("WASHINGTON, D.C.", "JULY 2025"))),
 ("The memo said the F B I's review confirmed that from about ten forty p m until about six thirty the next morning, | nobody entered any of the tiers in the unit. | It also said investigators found no incriminating client list.",
  [G("quote", q="…from the time Epstein was locked in his cell at around 10:40 pm on August 9, 2019, until around 6:30 am the next morning, {{nobody entered any of the tiers in the SHU.}}",
     who="DOJ / FBI memo", role="July 2025 · as quoted by The National News Desk", size=52, source=S_M)], {}),
 ("But viewers noticed a gap. | The released video jumped from eleven fifty-eight and fifty-eight seconds to midnight.",
  [G("stat", k="RELEASED JAIL VIDEO · JULY 2025", a="11:58:58 → 12:00", size=170, b="a gap of about one minute", c="as reported by CBS News", source=S_M)], {}),
 ("Attorney General Pam Bondi explained that every night, the video is reset, | and every night should have the same minute missing.",
  [C("dv977364c", 0.5, lab=NYC2)], {}),
 ("In September twenty twenty-five, Congress released another version, from six p m to seven a m. | CBS News reported that this one includes the minute, | and that nothing apparently unusual happens in it, | though the files lacked the metadata that would help confirm they were raw exports.",
  [C("dv346026", 3.0, lab=CAP)], {}),
 ("Then, in February twenty twenty-six, CBS reported that F B I records show the bureau's master copy of the footage was authorized for destruction in June twenty twenty-four, | and that the reset explanation appears to have been unverified.",
  [I("f_still2", kb="out", focus=[0.5, 0.5], lab=FG.format("6.5", "STILL FROM THE RECORDING CAMERA: VIEW OF THE OFFICERS' STATION"))], {}),
 ("None of that changes what the one camera showed: no one entering the tier. | But it gave people one more reason to doubt.",
  [I("f_still", kb="out", focus=[0.5, 0.5], lab=FG.format("6.4", "STILL FROM THE RECORDING CAMERA: STAIRWAY TO L TIER"))], dict(gap=0.9, sil=True)),

 # ---------------- X. THE DISPUTE ----------------
 ("Which brings us to this week.",
  [G("chapter", n="X", t="The Dispute")], {}),
 ("On November sixteenth, twenty twenty-six, three forensic experts presented their findings to the Middle Temple, a legal society in London. | Epstein's brother had shared the autopsy file with one of them, according to The New York Times as cited by CNN.",
  [C("dv977364c", 20.0, lab=NYC2)], dict(tag=("LONDON / NEW YORK", "NOVEMBER 16, 2026"))),
 ("Their claim: the ligature marks are, in their words, most consistent with homicidal strangulation from behind.",
  [G("quote", q="The ligature marks are {{most consistent with homicidal strangulation from behind…}}",
     who="Three forensic experts", role="Presentation in London, Nov. 16, 2026 · a claim, not an official finding", size=58, source=S_X)], dict(slow=True)),
 ("They also argued that no photographs were taken of the scene before Epstein was moved.",
  [I("f_station2", kb="out", focus=[0.6, 0.45], lab=FG.format("4.12", "THE OFFICERS' STATION SEEN FROM EPSTEIN'S CELL"))], {}),
 ("Now the other side of the ledger. | Their findings have not been peer-reviewed. | Their review was based on the autopsy file and records, not on the body itself.",
  [G("list", kicker="WEIGHING THE NEW CLAIM", title="What we know about it", items=[
      dict(t="Presented publicly, Nov. 16, 2026"), dict(t="Not yet peer-reviewed", s="CNN"), dict(t="Based on the autopsy file and records"),
      dict(t="The medical examiner stands by its ruling")], source=S_X)], {}),
 ("New York City's Office of Chief Medical Examiner says it stands by its determination. | The F B I found no criminality. | And the Inspector General found no evidence that anyone entered Epstein's tier.",
  [I("c_contradict", kb="down", focus=[0.5, 0.5], lab=EX)], {}),
 ("One of them told The New York Times, as cited by CNN, that he has no idea who might have been responsible, | and that what interests him is how this went so sideways. | And the Inspector General's report is specific about the two staff members on duty: | on the recorded video, they never rose from their seats or approached the cell block that night, | and their reaction that morning was consistent with their being unaware of any harm to Epstein.",
  [C("dv977364c", 8.0, lab=NYC2)], {}),
 ("So, two official findings, and one new expert challenge. | Here is what the record does not contain: | a recording of Epstein's cell door. | Because that night, no one walked the rounds, and the camera on his tier was not recording.",
  [I("f_station", kb="out", focus=[0.6, 0.45], lab=FG.format("4.11", "VIEW OF EPSTEIN'S CELL DOOR FROM THE OFFICERS' STATION"))], dict(slow=True, gap=0.9, sil=True)),

 # ---------------- CLOSE ----------------
 ("And the fight over the rest of the Epstein files is not over either.",
  [C("dv346026", 15.0, lab=CAP)], dict(tag=("WASHINGTON, D.C.", "NOVEMBER 2026"))),
 ("On November tenth, the Republican-led House Oversight Committee released a report faulting the federal government for failing to hold Epstein accountable. | Chairman James Comer said the Justice Department must interview key witnesses.",
  [G("quote", q="The Department of Justice must interview key witnesses, {{investigate everyone who participated in or facilitated these crimes.}}", who="Rep. James Comer (R-Ky.)", role="Chairman, House Oversight Committee · Nov. 2026", size=54, source=S_H)], {}),
 ("The committee's top Democrat, Robert Garcia, called the report partisan and incomplete.",
  [G("quote", q="{{Partisan and incomplete.}}", who="Rep. Robert Garcia (D-Calif.)", role="Top Democrat, House Oversight Committee · Nov. 2026", size=80, source=S_H)], {}),
 ("This week also marks one year since Congress passed the Epstein Files Transparency Act. | A survivor told N P R that when the files came out, she found her own name and phone number unredacted.",
  [G("stat", k="EPSTEIN FILES TRANSPARENCY ACT · NOV. 2025", a="1 YEAR", size=260, b="since Congress passed the law", c="a survivor told NPR she found her own name and number unredacted", source=S_H)], {}),
 ("A day after the committee report, a petition led by Republican Thomas Massie, with Democrat Ro Khanna, reached two hundred eighteen signatures, forcing a House vote on a second Epstein files bill. | A vote could come as early as December second or third.",
  [G("stat", k="DISCHARGE PETITION · NOV. 11, 2026", a="218", size=360, b="signatures: all 214 Democrats and 4 Republicans", c="floor action possible after Thanksgiving", source=S_H)], {}),
 ("So how did one of the most notorious prisoners in America end up unwatched? | According to the government's own investigation: | a new cellmate never assigned, | cameras that weren't recording, | and rounds that were signed for but never walked.",
  [G("timeline", kicker="THE LAST NIGHT, BY THE RECORD", title="August 9-10, 2019", events=[
      dict(y="JUL 29", t="Recorder fails"), dict(y="AUG 9", t="Cellmate leaves"), dict(y="6:58 PM", t="Unmonitored call"),
      dict(y="10:40 PM", t="Last round"), dict(y="6:30 AM", t="Found"), dict(y="7:36 AM", t="Pronounced dead")], source=S_IG)], dict(slow=True)),
 ("Here is our question for you. | The record shows how he was left alone. | Do you think the official investigations answered how he died? | Tell us in the comments.",
  [I("f_sign", kb="in", focus=[0.5, 0.5], lab=FG.format("5.2", "SIGN IN THE JAIL'S SPECIAL HOUSING UNIT"))], {}),
 ("Next in this series: what the three million pages released in twenty twenty-six actually contain, and what stayed blacked out.",
  [G("end", n="017", next="What the 2026 Epstein release contains")], dict(gap=2.5)),
]

PRON = [("Teterboro", "Teter-borough"), ("Comer", "Comer"), ("Massie", "Massey"), ("Khanna", "Kahna"), ("Ghislaine", "Ghee-lane"),
        ("Maxwell", "Maxwell"), ("Bondi", "Bondy"), ("F B I", "F B I"), ("U S", "U S"), ("p m", "P M"), ("a m", "A M"),
        ("Presbyterian", "Presbyterian"), ("Garcia", "Garcia")]

DISPLAY = [
 ("F B I", "FBI"), ("U S Marshals", "U.S. Marshals"), ("U S", "U.S."),
 ("one twenty-seven in the morning", "1:27 in the morning"), ("twelve thirty p m", "12:30 p.m."), ("six fifty-eight to seven nineteen p m", "6:58 to 7:19 p.m."),
 ("six p m to seven a m", "6 p.m. to 7 a.m."), ("seventy-three plus one", "73 + 1"), ("eight p m", "8 p.m."), ("ten p m", "10 p.m."), ("ten forty p m", "10:40 p.m."), ("about ten forty", "about 10:40"), ("six thirty a m", "6:30 a.m."),
 ("six thirty the next morning", "6:30 the next morning"), ("one to three a m", "1 to 3 a.m."), ("seven thirty-six a m", "7:36 a.m."), ("seven ten", "7:10"),
 ("eleven fifty-eight and fifty-eight seconds", "11:58:58"),
 ("one hundred twenty-eight pages", "128 pages"), ("one-fifty Park Row", "150 Park Row"), ("twenty-three hours", "23 hours"),
 ("more than seventy jail employees", "more than 70 jail employees"), ("twenty-two hours", "22 hours"), ("sixteen hours", "16 hours"), ("from four p m to eight a m", "from 4 p.m. to 8 a.m."),
 ("More than seventy-five", "More than 75"), ("seven hundred thirty thousand dollars", "$730,000"), ("about two thousand pages", "about 2,000 pages"),
 ("three million pages", "3 million pages"), ("two hundred eighteen", "218"), ("sixty-six", "66"), ("thirteen months", "13 months"),
 ("thirty-minute", "30-minute"), ("thirty minutes", "30 minutes"),
 ("July sixth, twenty nineteen", "July 6, 2019"), ("July seventh", "July 7"), ("July twenty-third", "July 23"), ("July twenty-ninth", "July 29"),
 ("July thirtieth", "July 30"), ("August eighth", "August 8"), ("August ninth", "August 9"), ("August tenth", "August 10"),
 ("November sixteenth, twenty twenty-six", "November 16, 2026"), ("November tenth", "November 10"), ("December second or third", "December 2 or 3"),
 ("September twenty eighteen", "September 2018"), ("June twenty twenty-three", "June 2023"), ("October twenty twenty-one", "October 2021"),
 ("July twenty twenty-five", "July 2025"), ("September twenty twenty-five", "September 2025"), ("February twenty twenty-six", "February 2026"),
 ("June twenty twenty-four", "June 2024"), ("released in twenty twenty-six", "released in 2026"), ("two thousand seven", "2007"),
 ("eleven days", "11 days"), ("twenty thirteen", "2013"), ("forty-five of one hundred twenty-two", "45 of 122"), ("N P R", "NPR"), ("at four", "at 4"),
 ("p.m..", "p.m."), ("a.m..", "a.m."), (" | ", " "), ("|", ""),
]

META = dict(
    n="017", title="What the Inspector General Found the Night Epstein Died",
    imgs={**{k: D + k + ".jpg" for k in ["cover", "c_alone", "c_arrest", "c_bail", "c_rules", "c_jul23", "c_kill", "c_unclear", "c_bunkies",
                                         "c_nointerest", "c_email", "c_warden", "c_marshals", "c_dvr", "c_eleven", "c_key", "c_funding", "c_will",
                                         "c_redflag", "c_unseal", "c_call", "c_mother", "c_shifts", "c_22", "c_75", "c_furniture", "c_doze",
                                         "c_never", "c_breakfast", "c_messed", "c_pronounced", "c_victims", "c_findings", "c_dpa", "c_noone",
                                         "c_contradict", "c_me", "c_credit", "c_2013", "c_search", "c_linens", "c_sight", "c_73", "c_notfirst"]},
          **{k: F + k + ".jpg" for k in ["f_sign", "f_entry", "f_cell", "f_empty", "f_map", "f_cam",
                                         "f_still", "f_still2", "f_slips", "f_station", "f_station2"]}},
    credit="Documents and photographs: DOJ Office of the Inspector General, report 23-085 (June 2023); names of jail staff black-barred by us.\\NB-roll: DoD via DVIDS; modern b-roll does not show the events described. Graphics marked RECREATED are our own summaries. No endorsement implied.",
    shorts=[
        dict(id="s1", lines=[53, 61], tpl="blue", hook="22 HOURS<br>ON DUTY.<br>[NO COUNT DONE]", hs=175),
        dict(id="s2", lines=[18, 23], tpl="yellow", hook="18 DAYS<br>BEFORE:<br>[A WARNING]", hs=195),
        dict(id="s3", lines=[82, 88], tpl="white", hook="THE<br>MISSING<br>[MINUTE]", hs=210),
        dict(id="s4", lines=[24, 32], tpl="red", hook="CELLMATE<br>LEFT.<br>[NO REPLACEMENT]", hs=170),
    ],
    yshorts=[
        dict(id="y1", lines=[1, 3], tpl="yellow", hook="NOBODY<br>CHECKED<br>[FOR 8 HOURS]", hs=190),
        dict(id="y2", lines=[36, 38], tpl="red", hook="THE CAMERAS<br>STOPPED<br>[RECORDING]", hs=175),
        dict(id="y3", lines=[76, 77], tpl="white", hook="WHAT THE<br>VIDEO<br>[SHOWED]", hs=200),
    ],
)
