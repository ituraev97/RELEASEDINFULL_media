# FILE 020 — Why the Soviets Thought a NATO Drill Was a Real Nuclear Attack (Able Archer 83 and the 1983 war scare)
# Evergreen topic reframed as a curiosity/question story. Hook: the 1990 PFIAB report "The Soviet 'War Scare'" (declassified 2015 after a 12-year fight).
# MAIN RECORDS (all U.S. government / declassified; mirrored on archive.org):
#   PFIAB, "The Soviet 'War Scare'" (Feb. 15, 1990), declassified in part, via National Security Archive EBB No. 533 (Oct. 24, 2015) — archive.org item NotesOnPresidentsForeignIntelligenceAdvisoryBoardAbleArcher (ELS008-003c)
#   SACEUR Exercise ABLE ARCHER 83 After Action Report (SAC advance team) — archive.org item 1983WarScareDocumentsAbleArcherAndRYaN (ELS008-014)
#   DCI Casey memo "US/Soviet Tension" (June 19, 1984); SNIE 11-10-84/JX; CIA Directorate of Intelligence memo (Dec. 30, 1983) — same item (ELS008-014a/b/d)
#   Ben B. Fischer, "The 1983 War Scare in US-Soviet Relations", CIA Center for the Study of Intelligence — CIA Reading Room 05584199 (archive.org)
# LEGAL: named people are historical public officials or authors quoted from official records (McFarlane and Fischer may be living; named only as quoted in the PFIAB report / published CIA study, attributed in narration). (Reagan, Andropov, Ustinov, Ogarkov, Romanov, Kryuchkov, Casey, McFarlane, Perroots,
#   Eagleburger, Thatcher, Gordievsky as described in the official record). No victims shown. Footage is public domain (Reagan Library, U.S. Army/USAF films, DVIDS).
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

FOC = __import__("json").load(open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "focus.json")))
def F(key, **k):
    k.setdefault("kb", "in"); k.setdefault("focus", FOC.get(key, [0.5, 0.5])); return I(key, **k)

PF = "ACTUAL DOCUMENT · PFIAB 'SOVIET WAR SCARE' REPORT, 1990 · HIGHLIGHT ADDED · "
AA = "ACTUAL DOCUMENT · SACEUR ABLE ARCHER 83 AFTER ACTION REPORT · "
EBB = "ACTUAL DOCUMENT · NATIONAL SECURITY ARCHIVE BRIEFING BOOK NO. 533 · "
CAP = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C., 2012 · ILLUSTRATIVE ONLY"
CAP2 = "B-ROLL · WASHINGTON, D.C., AROUND THE CAPITOL, 2012 · ILLUSTRATIVE ONLY"
FAIR = "B-ROLL · B-52 NIGHT TAKEOFF, RAF FAIRFORD, ENGLAND, 2024 · ILLUSTRATIVE ONLY"
EUR = "B-ROLL · B-52 BOMBER OPERATIONS IN EUROPE, 2026 · ILLUSTRATIVE ONLY"
REF = "B-ROLL · B-52 AERIAL REFUELING, 2026 · ILLUSTRATIVE ONLY"
JDAM = "B-ROLL · AIRMEN LOAD CONVENTIONAL MUNITIONS ONTO A B-52, 2024 · NOT THE 1983 EXERCISE"
SDI = "ARCHIVAL · PRESIDENT REAGAN AT A LECTERN, 1983 · REAGAN LIBRARY"
EVIL = "ARCHIVAL · PRESIDENT REAGAN SPEAKING, 1983 · REAGAN LIBRARY"
KAL = "PRESIDENT REAGAN · ADDRESS ON THE SOVIET ATTACK ON A KOREAN AIRLINER · SEPT. 5, 1983 · REAGAN LIBRARY"
KAL2 = "ARCHIVAL · PRESIDENT REAGAN, SEPTEMBER 1983 · REAGAN LIBRARY"
LEB = "PRESIDENT REAGAN · ADDRESS ON LEBANON AND GRENADA · OCT. 27, 1983 · REAGAN LIBRARY"
GREN = "PRESIDENT REAGAN · REMARKS ON THE GRENADA RESCUE MISSION · OCT. 25, 1983 · REAGAN LIBRARY"
JAN = "PRESIDENT REAGAN · ADDRESS ON U.S.-SOVIET RELATIONS · JAN. 16, 1984 · REAGAN LIBRARY"
THAT = "PRESIDENT REAGAN AND PRIME MINISTER THATCHER · SEPT. 29, 1983 · REAGAN LIBRARY"
PER = "U.S. ARMY ORIENTATION FILM · PERSHING MISSILE UNIT, NEU-ULM, WEST GERMANY · 1983"
AFN = "ARCHIVAL · U.S. AIR FORCE FILM ON THE SOVIET THREAT · U.S. PORTRAYAL OF SOVIET FORCES · NOT FOOTAGE OF THE EVENTS DESCRIBED"

S_PF = "SOURCE: PFIAB, 'THE SOVIET WAR SCARE' (FEB. 15, 1990), DECLASSIFIED IN PART · NATIONAL SECURITY ARCHIVE EBB 533"
S_AA = "SOURCE: SACEUR ABLE ARCHER 83 AFTER ACTION REPORT (SECRET, DECLASSIFIED)"
S_CIA = "SOURCE: CIA DIRECTORATE OF INTELLIGENCE MEMO, DEC. 30, 1983; SNIE 11-10-84/JX; CIA CENTER FOR THE STUDY OF INTELLIGENCE"
S_CAS = "SOURCE: DCI WILLIAM CASEY MEMO 'US/SOVIET TENSION,' JUNE 19, 1984 (DECLASSIFIED 2013)"

LINES = [
 # ---------------- COLD OPEN ----------------
 ("In November nineteen eighty-three, a U S advisory board later concluded, some Soviet forces may have been preparing for a NATO nuclear strike. | It was only a drill. | So why did some in Moscow fear it was real?",
  [F("pf_cover", kb="in", focus=[0.5, 0.35], lab=PF + "COVER PAGE · TOP SECRET")], dict(tag=("MOSCOW AND NATO EUROPE", "NOVEMBER 1983"))),
 ("This is the cover of a secret report written for the President in nineteen ninety. | Its title: The Soviet War Scare. | It stayed classified for twenty-five years, until the National Security Archive, after what it calls a twelve-year fight, got it released in part in twenty fifteen.",
  [F("ebb_cover", kb="in", lab=EBB + "OCT. 24, 2015 · 'HAIR TRIGGER' HIGHLIGHTED BY US"), F("pf_cover", kb="out", focus=[0.6, 0.3], lab=PF + "COVER PAGE · DECLASSIFIED IN PART")], {}),
 ("Its authors, the President's Foreign Intelligence Advisory Board, looked at hundreds of documents and interviewed more than seventy-five American and British officials. | About the NATO exercise called Able Archer, they wrote:",
  [F("pf_exec", kb="in", lab=PF + "EXECUTIVE SUMMARY · PAGES v–viii")], {}),
 ("There is little doubt in our minds that the Soviets were genuinely worried by Able Archer; however, the depth of that concern is difficult to gauge.",
  [G("quote", q="There is little doubt in our minds that the Soviets were {{genuinely worried}} by Able Archer; however, the depth of that concern is difficult to gauge.", who="President's Foreign Intelligence Advisory Board", role="'The Soviet War Scare' · Feb. 15, 1990", size=62, source=S_PF)], dict(slow=True)),
 ("Today we read the paper trail: | the after action report by the U S Strategic Air Command's observer team, | the Soviet side as American intelligence saw it, | the memo that reached President Reagan, | and the argument inside U S intelligence over whether any of it was real.",
  [C("dv943839c", 4.0, lab=FAIR), C("dv1006838c", 6.0, lab=EUR)], {}),
 ("Everything here comes from declassified American records, a CIA study, and the National Security Archive's summary. | Where historians and officials disagree, we say so. | And we never claim more than the documents show.",
  [C("dv1010076c", 6.0, lab=REF)], {}),
 ("", [G("intro", n="020")], dict(gap=0.2)),
 ("", [G("title", n="020", t="DID MOSCOW FEAR THE DRILL?", size=120, sub="Able Archer 83 · The 1983 War Scare")], dict(gap=0.4)),

 # ---------------- I. THE DRILL ----------------
 ("Start with what Able Archer actually was.",
  [G("chapter", n="I", t="The Drill")], {}),
 ("An annual NATO exercise. | A command post exercise: mainly staff officers at headquarters, though the Board says some U S forces also took part in live drills. | The after action report calls it practice in command and control, with particular emphasis on the transition from conventional operations to chemical and nuclear operations.",
  [F("aar_1", kb="in", lab=AA + "PAGE 1 · SECRET, DECLASSIFIED")], dict(tag=("NATO EUROPE", "ANNUAL EXERCISE"))),
 ("In nineteen eighty-three it ran from November seventh to November eleventh. | Three days of what the report calls low spectrum, conventional play. | Then two days of high spectrum play: nuclear war.",
  [G("timeline", kicker="ABLE ARCHER 83 · AS DESCRIBED IN THE AFTER ACTION REPORT", title="Nov. 7 – 11, 1983", events=[
      dict(y="NOV 7", t="Exercise begins"), dict(y="NOV 7–9", t="Conventional play"), dict(y="NOV 10–11", t="Nuclear play"), dict(y="NOV 11", t="Exercise ends")], source=S_AA)], {}),
 ("The report says that in the exercise scenario, orange forces attacked along the entire German border, with air attacks on blue airfields, and used chemical weapons throughout the exercise.",
  [C("dv943839c", 20.0, lab=FAIR)], {}),
 ("On the second day, the report says, the Strategic Air Command observers were directed to an alternate war headquarters. | And it notes that helmets, gas masks and chemical suits were required. | Gas masks were worn for hours after a simulated chemical attack.",
  [F("aar_5", kb="in", lab=AA + "PAGE 5 · ALTERNATE WAR HEADQUARTERS")], {}),
 ("The Strategic Air Command sent a small team to observe how B-52 bombers were used. | Earlier, the report notes, SAC participation had been discouraged because of, quote, the possible political implications or inferences of B-52 involvement.",
  [C("dv1010076c", 2.0, lab=REF), C("dv944524c", 20.0, lab=JDAM)], {}),
 ("Then comes a line that reads very differently today.",
  [C("dv944524c", 60.0, lab=JDAM)], dict(gap=0.4)),
 ("Quote: Numerous times during the exercise, the word strike was used in reference to B-52 sorties. | While this is an obvious slip of the tongue and was quickly corrected, in most cases, it does serve to fuel any inference should a remark be made in a nonsecure environment.",
  [F("aar_9", kb="in", lab=AA + "PAGE 9 · THE WORD 'STRIKE'")], dict(slow=True)),
 ("To be clear: the drill was routine, and nothing in these records suggests NATO planned to attack. | The Advisory Board agrees it was a recurring event that Soviet intelligence normally monitors. | But the nineteen eighty-three version, the Board says, had some special wrinkles.",
  [F("pf_wrinkles", kb="in", lab=PF + "PAGE 70 · 'SPECIAL WRINKLES'")], {}),
 ("New procedures for releasing nuclear weapons. | Pre-exercise messages that notionally moved forces from normal readiness, through various alert phases, to a general alert. | And the Board was told that some U S aircraft practiced nuclear warhead handling, | taxiing out of hangars carrying realistic-looking dummy warheads.",
  [C("dv944524c", 100.0, lab=JDAM), C("dv1006838c", 30.0, lab=EUR)], {}),
 ("According to the National Security Archive, summarizing declassified NATO and Air Force documents, the exercise season also included a radio-silent airlift: | one hundred seventy flights carrying about nineteen thousand American soldiers to Europe.",
  [G("stat", k="AUTUMN FORGE 83 · AS SUMMARIZED BY THE NATIONAL SECURITY ARCHIVE", a="170", size=300, b="flights · about 19,000 U.S. soldiers flown to Europe in radio silence", c="Able Archer was one component of the larger Autumn Forge exercise series", source="SOURCE: NATIONAL SECURITY ARCHIVE EBB 533 (OCT. 24, 2015)")], {}),

 # ---------------- II. THE VIEW FROM MOSCOW ----------------
 ("Now look at the map from the Soviet side.",
  [G("chapter", n="II", t="The View from Moscow")], {}),
 ("The Advisory Board says Soviet early warning radars could once give about thirteen minutes of warning of American ICBMs. | New radars and satellites raised that to about thirty. | Then NATO began deploying Pershing Two missiles in West Germany, | and by Soviet calculations, the Board says, warning of a first strike on Moscow fell, probably, to about eight minutes.",
  [F("pf_pershing", kb="in", lab=PF + "PAGE 39 · EARLY WARNING TIMES"), F("pf_pershing", kb="out", focus=[0.5, 0.45], lab=PF + "PAGE 39 · PERSHING II WARNING TIME")], dict(tag=("NATO MISSILES, WEST GERMANY", "LATE 1983"))),
 ("The Board adds a caution. | The Pershing Two's real range, eighteen hundred kilometers, would not have reached Moscow from West Germany. | Warsaw Pact sources, though, credited it with twenty-five hundred.",
  [F("pf_pershing", kb="in", focus=[0.5, 0.7], lab=PF + "PAGE 39 · PERSHING II RANGE")], {}),
 ("And who decides? | The Board says probably no more than three leaders could authorize Soviet nuclear weapons. | Under extreme time pressure, perhaps only the General Secretary and the Defense Minister.",
  [C("afnow_a", 0.0, lab=AFN)], {}),
 ("The man in the top job kept changing. | The Board notes the post of General Secretary changed hands three times in three years. | Brezhnev died in November nineteen eighty-two. | Andropov, February nineteen eighty-four. | Chernenko, March nineteen eighty-five.",
  [G("timeline", kicker="THE KREMLIN · AS NOTED BY THE ADVISORY BOARD", title="Three General Secretaries died in 28 months", events=[
      dict(y="NOV 1982", t="Brezhnev dies"), dict(y="FEB 1984", t="Andropov dies"), dict(y="MAR 1985", t="Chernenko dies")], source=S_PF)], {}),
 ("Andropov was gravely ill. | The Board says kidney failure in late September led to a long illness. | He failed to appear at the Kremlin celebrations on November seventh, | the day Able Archer began.",
  [C("afnow_b", 10.0, lab=AFN)], {}),

 # ---------------- III. OPERATION RYAN ----------------
 ("Behind the scare was an intelligence collection effort.",
  [G("chapter", n="III", t="Operation RYAN")], {}),
 ("In nineteen eighty-one, the KGB launched an operation called RYAN, from the Russian words for nuclear missile attack. | Officers abroad were ordered to look for signs that the West was preparing a surprise strike.",
  [C("afnow_c", 10.0, lab=AFN)], {}),
 ("By nineteen eighty-four, the Board says, tasking from Moscow had grown curiously esoteric. | London was told to watch the cruise missile base at Greenham Common, | and to keep an eye on banks, slaughterhouses and post offices.",
  [F("pf_self", kb="in", focus=[0.46, 0.4], lab=PF + "PAGE 81 · KGB LONDON RESIDENCY TASKING")], {}),
 ("The report gives one small example of the KGB's reporting demands. | A local campaign for blood donors met a requirement to report evidence of blood drives. | So it was reported. | And headquarters praised the London office, citing the blood donor report as especially interesting.",
  [F("pf_blood", kb="out", focus=[0.43, 0.37], lab=PF + "PAGE 82 · THE 'BLOOD DONOR' REPORT")], {}),
 ("A self-reinforcing cycle, the Board called it: | leadership concern provoked more reporting, | and more reporting added fuel to leadership anxieties.",
  [F("pf_self", kb="in", lab=PF + "PAGE 81 · 'A SELF-REINFORCING CYCLE'")], dict(slow=True)),
 ("According to the National Security Archive's summary of the report, the program reportedly included a computer model: a database of forty thousand weighted military, political and economic factors. | Before long, the report says, it started spewing very unwelcome news.",
  [G("stat", k="OPERATION RYAN · AS SUMMARIZED BY THE NATIONAL SECURITY ARCHIVE", a="40,000", size=250, b="weighted factors in the KGB's warning model", c="its output: Soviet relative strength was declining", source="SOURCE: NATIONAL SECURITY ARCHIVE EBB 533, SUMMARIZING THE PFIAB REPORT")], {}),
 ("In January nineteen eighty-four, the head of the KGB's foreign intelligence directorate, General Kryuchkov, told his officers that the threat of nuclear war had reached dangerous proportions. | They must not, he said, fail to perceive direct preparation by the adversary for a nuclear missile attack.",
  [G("quote", q="…it must not fail to perceive {{direct preparation by the adversary for a nuclear missile attack}} against the USSR…", who="Gen. Kryuchkov, KGB First Chief Directorate", role="Speech to KGB officers, Jan. 1984 · as quoted in the PFIAB report", size=50, source=S_PF)], dict(slow=True)),

 # ---------------- IV. A BAD YEAR ----------------
 ("Now the year itself.",
  [G("chapter", n="IV", t="A Bad Year")], {}),
 ("March nineteen eighty-three. | President Reagan calls the Soviet Union an evil empire. | And two weeks later he announces a missile defense research program the press calls Star Wars.",
  [C("evil_a", 4.0, lab=EVIL), C("sdi_a", 6.0, lab=SDI)], dict(tag=("WASHINGTON, D.C.", "MARCH 1983"))),
 ("The Soviet media answered in kind. | According to a CIA study, Reagan was repeatedly compared to Hitler, and accused of fanning the flames of war. | General Secretary Andropov suggested the President was insane, and a liar.",
  [C("evil_b", 6.0, lab=EVIL)], {}),
 ("On September first, a Soviet fighter shot down Korean Air Lines Flight zero zero seven. | All two hundred sixty-nine people aboard died. | Reagan addressed the nation.",
  [C("kal_a", 4.0, lab=KAL), C("kal_c", 6.0, lab=KAL2)], dict(tag=("SEA OF JAPAN", "SEPTEMBER 1, 1983"))),
 ("The CIA's own historian later wrote that the shootdown raised Soviet fears of a possible American attack, | and quote, made Moscow more suspicious that US military exercises might conceal preparations for an actual attack. | Within weeks, he wrote, Soviet intelligence would react in exactly that way.",
  [G("quote", q="…made Moscow more suspicious that US military exercises might {{conceal preparations for an actual attack.}} Within weeks, Soviet intelligence would react in exactly that way…", who="Ben B. Fischer", role="CIA Center for the Study of Intelligence · on the KAL 007 shootdown", size=44, source=S_CIA)], dict(slow=True)),
 ("The Advisory Board adds that Soviet officials, according to press reports, concluded the Reagan administration had deliberately engineered the incident to poison the atmosphere. | The Board reports that as the Soviet conclusion. It is not a finding of fact.",
  [C("kal_b", 5.0, lab=KAL)], {}),
 ("Then October. | On the twenty-third, the bombing of the Marine barracks in Beirut. | On the twenty-fifth, American troops land on Grenada. | The Board says the Kremlin called the Grenada landing a bandit attack, and a crime against peace and humanity.",
  [C("lebgren_a", 5.0, lab=LEB), C("gren_a", 8.0, lab=GREN)], dict(tag=("BEIRUT AND GRENADA", "OCTOBER 1983"))),
 ("And inside the Soviet Union, the Board says, a Western visitor reported that Andropov sent a letter to party organizations declaring that the motherland was truly in danger, | and that there was no chance of improving relations with the United States. | It was reportedly read at closed party meetings across the country.",
  [C("gren_b", 8.0, lab=GREN)], {}),

 # ---------------- V. NOVEMBER ----------------
 ("November seventh.",
  [G("chapter", n="V", t="November")], dict(gap=0.2)),
 ("Able Archer begins. | The same day, according to press accounts cited in the Board's report, Politburo member Grigory Romanov told a Kremlin audience the international situation was, quote, white hot. | Thoroughly white hot.",
  [F("pf_white", kb="in", lab=PF + "PAGE 69 · 'THOROUGHLY WHITE HOT'")], dict(tag=("MOSCOW", "NOVEMBER 7, 1983"))),
 ("On November eighth or ninth, Moscow sent a circular telegram to KGB offices in Western Europe. | It ordered them to report on the increased alert status of American bases, | and to check for indications of an impending nuclear attack. | The London office read it as a sign of headquarters' RYAN concern.",
  [F("pf_wrinkles", kb="out", focus=[0.52, 0.55], lab=PF + "PAGE 70 · THE CIRCULAR TELEGRAM")], {}),
 ("The best-known account comes from a KGB officer in London, Oleg Gordievsky, who was secretly working for British intelligence, as later described in the official record. | A CIA historian summarizes it: the cable reportedly suggested American forces had gone on alert, | and that the United States might have begun the countdown to a surprise nuclear war.",
  [C("dv346026c", 3.0, lab=CAP), C("dv346119c", 5.0, lab=CAP2)], {}),
 ("What did the Soviets do? | The Advisory Board lists reactions it calls unparalleled in scale.",
  [F("pf_react", kb="in", lab=PF + "PAGE 71 · SOVIET REACTION")], dict(gap=0.4)),
 ("More than thirty-six intelligence flights, including missions over the Norwegian, North, Baltic and Barents Seas. | A suspension of all flight operations except intelligence collection, from November fourth to tenth, probably to have as many aircraft as possible available for combat. | And, the report says, transporting nuclear weapons from storage sites to delivery units by helicopter.",
  [F("pf_helic", kb="in", lab=PF + "PAGE 72 · SOVIET RESPONSE · PARTS REDACTED")], {}),
 ("Parts of that page remain blacked out. | But the Board's reading is plain. | The scale and timing, it wrote, strongly suggests that Soviet military leaders may have been seriously concerned that the US would use Able Archer eighty-three as a cover for launching a real attack.",
  [G("quote", q="…{{strongly suggests to us}} that Soviet military leaders may have been seriously concerned that the US would use Able Archer 83 as a cover for launching a real attack.", who="President's Foreign Intelligence Advisory Board", role="'The Soviet War Scare' · Feb. 15, 1990", size=48, source=S_PF)], dict(slow=True)),
 ("Most of this was not visible, in its totality, until long after the exercise. | The Board says the full extent of the Soviet alert was not known until two weeks after the exercise ended, | and the standdown had been in effect for nearly a week before fully armed MiG-twenty-three fighters were noted on air defense alert in East Germany.",
  [C("dv1006838c", 50.0, lab=EUR)], {}),
 ("According to the National Security Archive's summary, the Defense Intelligence Agency did not report the standdown until a week after it began, | and no President's Daily Brief mentioned Able Archer or the Soviet response while it was happening. | The President's own national security adviser, Robert McFarlane, told the Board he remembered hearing nothing about it.",
  [C("dv346119c", 20.0, lab=CAP2)], {}),

 # ---------------- VI. THE GENERAL ----------------
 ("So who was watching?",
  [G("chapter", n="VI", t="The General")], {}),
 ("At U S Air Forces in Europe, the chief of intelligence, Lieutenant General Leonard Perroots, saw Soviet aircraft going to a heightened alert. | He had a choice: raise American readiness in response, or do nothing.",
  [C("dv943839c", 30.0, lab=FAIR)], dict(tag=("U.S. AIR FORCES IN EUROPE", "NOVEMBER 1983"))),
 ("He recommended not to respond. | The Advisory Board calls that decision, in its words, fortuitous, if ill-informed. | The officers in charge, it says, acted correctly out of instinct, not informed guidance.",
  [F("pf_perroots", kb="in", lab=PF + "PAGE 28 · THE PERROOTS RECOMMENDATION")], dict(slow=True)),
 ("In January nineteen eighty-nine, before retiring, Perroots sent a parting letter to the Director of Central Intelligence and to this Board, | voicing his disquiet over the inadequate treatment of the Soviet war scare. | The National Security Archive says the Board indicated it likely would never have studied the episode without him.",
  [C("dv1006838c", 55.0, lab=EUR), C("dv943839c", 38.0, lab=FAIR)], {}),
 ("The British saw the danger too. | According to the Board, Britain's ambassador visited Under Secretary of State Lawrence Eagleburger. | But the State Department's intelligence bureau presented a skeptical version of events, designed, in its officer's own words, to discourage the British.",
  [C("dv346026c", 10.0, lab=CAP)], {}),
 ("The National Security Archive adds that when the State Department requested a sanitized version of the estimate for NATO allies, | it removed all mentions of Able Archer and the Soviet response.",
  [C("dv346119c", 35.0, lab=CAP2)], {}),

 # ---------------- VII. THE PRESIDENT ----------------
 ("And the President?",
  [G("chapter", n="VII", t="The President")], {}),
 ("A week after the exercise, on November eighteenth, Reagan wrote in his diary: | I feel the Soviets are so defense minded, so paranoid about being attacked, that without being in any way soft on them we ought to tell them that no one here has any intention of doing anything like that.",
  [G("quote", q="I feel the Soviets are so defense minded, so paranoid about being attacked, that without being in any way soft on them we ought to tell them {{no one here has any intention}} of doing anything like that.", who="President Reagan's diary", role="Nov. 18, 1983 · as quoted by the National Security Archive", size=50, source="SOURCE: NATIONAL SECURITY ARCHIVE EBB 533 (OCT. 24, 2015)")], dict(slow=True)),
 ("Seven months later, in June nineteen eighty-four, CIA Director William Casey sent the President and his top advisers a memo titled, US Soviet Tension. | I attach here a rather stunning array of indicators of an increasing aggressiveness in Soviet policy and activities.",
  [F("casey_1", kb="in", lab="ACTUAL DOCUMENT · DCI MEMO 'US/SOVIET TENSION' · JUNE 19, 1984")], dict(tag=("WASHINGTON, D.C.", "JUNE 1984"))),
 ("The list included a ban on military help with the harvest, | civilian aircraft production cut in favor of military transports, | restrictions on Western diplomats' travel, | and a Soviet media message likening U S Soviet relations to those between Nazi Germany and the Soviet Union before World War Two.",
  [G("list", kicker="THE CASEY MEMO · INDICATORS LISTED", title="'A rather stunning array'", items=[
      dict(t="Military support for the harvest ended"), dict(t="Civil aircraft production cut", s="DOWN 14 PERCENT IN 1983, PER DIA"),
      dict(t="Leningrad closed to Western attachés"), dict(t="Media: U.S.-Soviet ties likened to Nazi Germany-USSR before WWII")], source=S_CAS)], {}),
 ("According to McFarlane, the Board reports, the President expressed surprise upon reading the memo, and described the events as, quote, really scary. | McFarlane himself was less convinced. | He wondered whether Moscow was trying to drive a wedge through Europe, to counter the President's missile defense plans.",
  [F("pf_mcf", kb="in", lab=PF + "PAGE 17 · THE PRESIDENT'S REACTION")], dict(slow=True)),
 ("Journalist Don Oberdorfer, quoted in the CIA study, reported that Reagan asked, | do you suppose they really believe that? | The National Security Archive says he also asked his ambassador in Moscow, Arthur Hartman: do you think Soviet leaders really fear us, or is all the huffing and puffing just part of their propaganda?",
  [C("jan84_a", 6.0, lab=JAN), C("radio_a", 5.0, lab="ARCHIVAL · REAGAN RADIO ADDRESS ON ARMS CONTROL, TAPED OCT. 21, 1983 · NOT THE REMARK DESCRIBED · REAGAN LIBRARY")], {}),
 ("Whether the scare changed his thinking is a matter for historians. | The CIA's own study notes that Britain's prime minister, Margaret Thatcher, was pressing the President to moderate his approach, | and says some analysts suspected the British put their own spin on the Soviet reporting.",
  [C("thatcher_a", 5.0, lab=THAT)], {}),

 # ---------------- VIII. WAS IT REAL? ----------------
 ("So was it real?",
  [G("chapter", n="VIII", t="Was It Real?")], {}),
 ("American intelligence's first answer, in nineteen eighty-four, was no. | A Special National Intelligence Estimate said: | we believe strongly that Soviet actions are not inspired by, and Soviet leaders do not perceive, a genuine danger of imminent conflict or confrontation with the United States.",
  [F("snie_4", kb="in", lab="ACTUAL DOCUMENT · SNIE 11-10-84/JX · KEY JUDGMENTS")], dict(tag=("U.S. INTELLIGENCE COMMUNITY", "1984"))),
 ("It judged the Soviet war talk to be propaganda, | aimed at discrediting U S policies and mobilizing peace pressures. | A CIA memo from December nineteen eighty-three put it in similar terms: | encourage resistance to the new missile deployments, deepen cleavages within the Atlantic alliance, | and build public pressure on Washington toward a more conciliatory posture.",
  [F("cia83_1", kb="in", lab="ACTUAL DOCUMENT · CIA DIRECTORATE OF INTELLIGENCE · DEC. 30, 1983")], {}),
 ("And there is evidence for the skeptics. | The CIA historian wrote that Able Archer seems to have made more of an impression on the White House than on the Kremlin. | A senior Soviet affairs expert who questioned Soviet leaders reported that none had heard of it. | A GRU officer said watch officers were concerned, but saw nothing else unusual.",
  [C("dv346026c", 0.0, lab=CAP)], {}),
 ("The Advisory Board disagreed. | It said the evidence then did not, and certainly does not now, support such categoric conclusions. | A strongly stated interpretation, it wrote, was defended by explaining away facts inconsistent with it.",
  [F("pf_exec", kb="out", focus=[0.5, 0.75], lab=PF + "EXECUTIVE SUMMARY · PAGES v–viii")], dict(slow=True)),
 ("But the Board is careful too. | It calls its reading a plausible interpretation based on a sizable but incomplete body of evidence. | It says Soviet reactions were mixed, and that intelligence detected no large-scale Warsaw Pact buildup. | And it writes that it does not intend this to be the final word.",
  [C("afnow_a", 30.0, lab=AFN)], {}),
 ("So the documents support two readings. | One: a propaganda campaign that reverberated in Soviet bureaucracies without reflecting real fear at the top. | The other: real fear, in part of the Soviet system, that a drill could be a cover for a strike. | The Board favors the second. The CIA historian agreed the KGB's alarm was real, but found Able Archer registered more in the White House than in the Kremlin.",
  [G("list", kicker="THE DOCUMENTS, TWO READINGS", title="Was the war scare real?", items=[
      dict(t="1984 SNIE: propaganda, not real fear", s="'WE BELIEVE STRONGLY…'"), dict(t="PFIAB 1990: genuinely worried", s="'LITTLE DOUBT IN OUR MINDS'"),
      dict(t="CIA historian: more impact on the White House than the Kremlin"), dict(t="Board: not the final word")], source=S_PF)], dict(slow=True)),

 # ---------------- IX. AFTERMATH ----------------
 ("How did it end?",
  [G("chapter", n="IX", t="Reason Restored")], {}),
 ("By November eleventh the Soviet alert was evidently withdrawn. | That day, Defense Minister Ustinov told senior officers that no enemy intrigues will catch us unawares. | By autumn nineteen eighty-four, the Board says, the feared attack had not materialized, | and by early nineteen eighty-five Soviet fear of one seemed to evaporate.",
  [C("jan84_b", 6.0, lab=JAN + " · NOT NOV. 11, 1983")], {}),
 ("The expected American attack never materialized. | According to the Board, Ogarkov was removed from his post. | Ustinov died on December twentieth. | And when Chernenko died in March nineteen eighty-five, Gorbachev succeeded him as General Secretary the next day.",
  [G("timeline", kicker="AFTER ABLE ARCHER · AS DESCRIBED BY THE ADVISORY BOARD", title="The scare fades", events=[
      dict(y="NOV 11, 1983", t="Alert withdrawn"), dict(y="JUN 1984", t="Casey memo"), dict(y="DEC 20, 1984", t="Ustinov dies"), dict(y="MAR 1985", t="Gorbachev takes over")], source=S_PF)], {}),
 ("But the intelligence community's last word was buried. | A nineteen eighty-eight annex said Soviet concerns about the drift in superpower relations indicated an increased threat of war in some leaders' eyes, | and it sat in an annex to a tightly held estimate, not meant for policymakers.",
  [F("pf_cover", kb="out", focus=[0.5, 0.5], lab=PF + "COVER PAGE"), C("dv346119c", 10.0, lab=CAP2)], {}),
 ("The Board's executive summary carries a warning about the future.",
  [F("pf_grave", kb="in", lab=PF + "PAGE xi · 'AN ESPECIALLY GRAVE ERROR'")], dict(gap=0.4)),
 ("It is an especially grave error, it wrote, to assume that since we know the US is not going to start World War Three, the next leaders of the Kremlin will also believe that, and act on that belief.",
  [G("quote", q="It is an especially grave error to assume that since we know the US is not going to start World War III, {{the next leaders of the Kremlin will also believe that}}…", who="President's Foreign Intelligence Advisory Board", role="'The Soviet War Scare' · Feb. 15, 1990", size=50, source=S_PF)], dict(slow=True)),
 ("Nobody started a war in November nineteen eighty-three. | A routine drill, which nothing in these records suggests was meant as a threat, may have been read by some on the other side as the opening move of one. | The documents do not tell us how close it came. | They tell us who was worried, what they did, and who in Washington noticed, and when.",
  [C("dv943839c", 12.0, lab=FAIR), C("dv1006838c", 40.0, lab=EUR)], {}),
 ("Here is our question for you. | Was Able Archer a near miss, or a scare that grew in the telling? | The Advisory Board and the CIA historian differ on how much Able Archer registered in the Kremlin. | Tell us in the comments which reading the documents support, and please keep it to the documents.",
  [F("ebb_cover", kb="in", lab=EBB + "OCT. 24, 2015")], {}),
 ("Next file: another secret the government kept for decades.",
  [G("end", n="020", next="Another file, another secret")], dict(gap=2.5)),
]

PRON = [("Able Archer", "Able Archer"), ("Pershing", "Pershing"), ("Gordievsky", "Gor-dee-ev-sky"), ("Kryuchkov", "Kryoo-chkov"), ("Andropov", "An-dro-pov"), ("Brezhnev", "Brezh-nev"),
        ("Chernenko", "Cher-nen-ko"), ("Ustinov", "Oos-tee-nov"), ("Ogarkov", "O-gar-kov"), ("Romanov", "Ro-ma-nov"), ("Grigory", "Gri-gory"), ("Perroots", "Perr-oots"),
        ("Eagleburger", "Eagle-burger"), ("McFarlane", "Mac-Far-lane"), ("Oberdorfer", "Oh-ber-dorfer"), ("Hartman", "Hartman"), ("Thatcher", "Thatcher"), ("Gorbachev", "Gor-ba-chov"),
        ("RYAN", "Ryan"), ("PFIAB", "P F I A B"), ("SNIE", "Snee"), ("KGB", "K G B"), ("GRU", "G R U"), ("CIA", "C I A"), ("ICBMs", "I C B Ms"), ("U S", "U S"), ("SAC", "S A C"),
        ("Greenham", "Greenum"), ("Barents", "Barents"), ("Leningrad", "Len-in-grad"), ("MiG", "Mig"), ("Fischer", "Fisher"), ("Fairford", "Fair-ford"), ("Kola", "Koh-la")]

DISPLAY = [
 ("U S", "U.S."), ("K G B", "KGB"), ("G R U", "GRU"), ("C I A", "CIA"), ("P F I A B", "PFIAB"),
 ("nineteen eighty-three", "1983"), ("nineteen eighty-four", "1984"), ("nineteen eighty-one", "1981"), ("nineteen eighty-two", "1982"), ("nineteen eighty-five", "1985"),
 ("nineteen eighty-nine", "1989"), ("nineteen eighty-eight", "1988"), ("nineteen ninety", "1990"), ("twenty fifteen", "2015"), ("twenty-five years", "25 years"), ("twelve-year", "12-year"),
 ("one hundred seventy flights", "170 flights"), ("nineteen thousand", "19,000"), ("seventy-five", "75"), ("Able Archer eighty-three", "Able Archer 83"),
 ("eighteen hundred kilometers", "1,800 kilometers"), ("twenty-five hundred", "2,500"), ("two hundred sixty-nine", "269"), ("forty thousand", "40,000"), ("thirty-six", "36"),
 ("zero zero seven", "007"), ("Pershing Two", "Pershing II"), ("MiG-twenty-three", "MiG-23"), ("World War Three", "World War III"), ("World War Two", "World War II"),
 ("about thirteen minutes", "about 13 minutes"), ("about thirty", "about 30"), ("about eight minutes", "about 8 minutes"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="020", title="Did the Soviets Think a NATO Drill Was a Real Nuclear Attack? Able Archer 83",
    imgs={k: "/home/claude/src/img/" + k + ".jpg" for k in ["ebb_cover", "pf_cover", "pf_exec", "pf_genuine", "pf_white", "pf_wrinkles", "pf_react", "pf_helic", "pf_mcf",
          "pf_pershing", "pf_perroots", "pf_grave", "pf_blood", "pf_self", "aar_1", "aar_5", "aar_9", "casey_1", "snie_4", "cia83_1"]},
    credit="Documents: PFIAB report 'The Soviet War Scare' (Feb. 15, 1990), SACEUR Able Archer 83 After Action Report, DCI memo (June 19, 1984), SNIE 11-10-84/JX and CIA memo (Dec. 30, 1983), as released by the U.S. government and mirrored on archive.org; National Security Archive EBB 533.\\NFootage: Reagan Library (White House video), U.S. Army and U.S. Air Force films, DoD via DVIDS. Modern b-roll does not show the events described; every shot is labelled with what it shows.",
    shorts=[
        dict(id="s1", lines=[1, 6], tpl="yellow", hook="ONLY A<br>[DRILL?]", hs=200),
        dict(id="s2", lines=[27, 31], tpl="red", hook="40,000<br>[FACTORS]", hs=190),
        dict(id="s3", lines=[43, 47], tpl="blue", hook="MOSCOW'S<br>[REACTION]", hs=170),
        dict(id="s4", lines=[51, 54], tpl="yellow", hook="DON'T<br>[RESPOND]", hs=180),
    ],
    yshorts=[
        dict(id="y1", lines=[66, 66], tpl="red", hook="THE<br>[SKEPTICS]", hs=190),
        dict(id="y2", lines=[29, 30], tpl="white", hook="THE BLOOD<br>[DONOR REPORT]", hs=140),
        dict(id="y3", lines=[61, 61], tpl="white", hook="DO THEY<br>[BELIEVE IT?]", hs=150),
    ],
)
