# FILE 019 — What's Actually Inside the Epstein Files (and What Is Still Missing)
# Epstein series, part 3 of 4. Fresh hook: Nov. 10, 2026 House Oversight (GOP) report; Nov. 11, 2026 second discharge petition
#   reached 218 signatures -> House vote expected soon (as early as Dec. 2-3, per Axios via earlier research); Nov. 18, 2026 one-year mark.
# MAIN RECORDS: DOJ "Epstein Library" pages EFTA00005586 (119 pp., every page black), EFTA00006109/6209/6309 (100+100+55 pp., every page black),
#   EFTA00008744 (119-pp. grand jury transcript, first two pages shown) — DOJ data sets 3, 4, 6, mirrored on archive.org (item 20251224_20251224_2055).
#   Page checks done locally: every page of the four blacked-out files is black (script check, research file).
# LEGAL: named living people are only public officials acting in role (Reps. Khanna, Massie, Comer, Garcia, Mace, Norman, Fitzpatrick; Sen. Schumer;
#   Deputy AG Todd Blanche; then-AG Pam Bondi) and the convicted Ghislaine Maxwell. No other living person is named. DOJ's own warning that some
#   material may be false or misleading is stated; "appearing in these records is not evidence of wrongdoing" is stated in the opening and on screen.
#   Victims never named or shown (survivors quoted anonymously). Only the first two pages of the grand jury transcript are shown (names already
#   black-barred by DOJ). No photographs of any person.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)

DOC = "ACTUAL DOCUMENT · DOJ EPSTEIN FILES RELEASE · "
CAP = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C., 2012"
CAP2 = "B-ROLL · WASHINGTON, D.C., AROUND THE CAPITOL, 2012"
TRE = "B-ROLL · THE U.S. TREASURY BUILDING, WASHINGTON, D.C., 2012"
DCA = "B-ROLL · WASHINGTON, D.C., SEEN FROM A MILITARY JET COCKPIT, 2026"
NYC = "B-ROLL · MANHATTAN FROM AN F-22 COCKPIT, NEW YORK CITY, 2025"
HAR = "B-ROLL · LOWER MANHATTAN FROM NEW YORK HARBOR, JANUARY 2026"

S_ACT = "SOURCE: PUBLIC LAW 119-38 AS REPORTED BY CBS NEWS (DEC. 2025, JUNE 2026) AND WIKIPEDIA"
S_D19 = "SOURCE: CBS NEWS (DEC. 21, 2025); SCRIPPS NEWS (DEC. 19, 2025)"
S_J30 = "SOURCE: PBS NEWSHOUR (JAN. 30, 2026); SCRIPPS NEWS (JAN. 30, 2026); NPR"
S_ERR = "SOURCE: NPR (FEB. 2026); CBS NEWS (JUNE 2026)"
S_MIS = "SOURCE: CBS NEWS (UPDATED JUNE 19, 2026) — CBS'S FINDINGS, NOT DOJ STATEMENTS"
S_NOV = "SOURCE: ROLL CALL, CBS NEWS AND ABC NEWS (NOV. 11, 2026); NPR AND NBC NEWS (NOV. 10, 2026)"

LINES = [
 # ---------------- COLD OPEN: the black page ----------------
 ("What is actually inside the Epstein files? | One hundred nineteen pages of them were released completely black. | Not a word of body text on any of them, as released in December twenty twenty-five. | And what is still missing?",
  [I("p_b1", kb="in", focus=[0.5, 0.45], lab=DOC + "EFTA00005586, PAGE 1 OF 119")], dict(tag=("JUSTICE DEPARTMENT RELEASE", "DECEMBER 2025"))),
 ("This is page one. | Nothing but a file number, and the words Grand Jury, N Y, in the corner.",
  [I("p_b1", kb="out", focus=[0.7, 0.1], lab=DOC + "EFTA00005586, PAGE 1 OF 119")], {}),
 ("Look at the bottom of the page. | Every page in these files carries its own number, starting with letters that match the initials of the law. | This one is E F T A zero zero zero zero five five eight six. | Page sixty of the same document is numbered five six four five. | So every page can be counted, and cited.",
  [I("p_b60", kb="in", focus=[0.8, 0.95], lab=DOC + "EFTA00005586, PAGE 60 OF 119 · FOOTER NUMBER EFTA00005645")], {}),
 ("The Department of Justice published it under a law that Congress passed almost unanimously. | The next day it posted a different file: a one hundred nineteen page grand jury transcript with most of its text visible.",
  [I("p_b60", kb="in", focus=[0.5, 0.2], lab=DOC + "EFTA00005586, PAGE 60 OF 119")], {}),
 ("This is part three of our series on the Epstein records. | Part one covered the two thousand seven Florida deal. | Part two, the Inspector General's report on his death in jail. | Today: what the millions of pages released in twenty twenty-six contain, | what the Justice Department says it held back, | and what reporters say is still missing.",
  [C("dv346026c", 3.0, lab=CAP)], dict(tag=("WASHINGTON, D.C.", "NOVEMBER 2026"))),
 ("For anyone arriving here fresh: | Jeffrey Epstein, a financier, was arrested on federal sex trafficking charges in July twenty nineteen, | and died in federal custody that August. | His associate Ghislaine Maxwell was convicted in December twenty twenty-one. | The files are the government's records of those cases, and of the investigations around them.",
  [C("dv977364c", 8.0, lab=NYC)], {}),
 ("And it is back in the news. | A discharge petition led by Republican Thomas Massie, with Democrat Ro Khanna and others working alongside him, reached two hundred eighteen signatures on November eleventh, | setting up a House vote on a second Epstein files bill.",
  [G("stat", k="DISCHARGE PETITION · NOV. 11, 2026", a="218", size=360, b="signatures: a second Epstein files bill is headed to the House floor", c="as reported by CBS News and Roll Call", source=S_NOV)], {}),
 ("One rule before we start. | Appearing in these records is not evidence of wrongdoing. | The Justice Department itself has warned that some of the material may be false or misleading. | We stay with what the documents, and the reporting about them, actually show.",
  [G("quote", q="Appearing in these records is {{not evidence of wrongdoing.}}", who="Our rule for this series", role="Released in Full", size=70, source="THE JUSTICE DEPARTMENT HAS WARNED SOME MATERIAL MAY BE FALSE OR MISLEADING · SCRIPPS NEWS, JAN. 30, 2026")], dict(slow=True)),
 ("", [G("intro", n="019")], dict(gap=0.2)),
 ("", [G("title", n="019", t="INSIDE THE FILES", size=150, sub="What's In Them. What's Missing.")], dict(gap=0.4)),

 # ---------------- I. THE LAW ----------------
 ("To understand the black pages, start with the law.",
  [G("chapter", n="I", t="The Law")], {}),
 ("The Epstein Files Transparency Act was introduced in July twenty twenty-five by Democratic Representative Ro Khanna, | and Republican Thomas Massie co-led it through the House.",
  [C("dv346119c", 1.5, lab=CAP2)], dict(tag=("WASHINGTON, D.C.", "JULY 2025"))),
 ("On November eighteenth, the House passed it, four hundred twenty-seven to one. | The Senate passed it by unanimous consent, and the President signed it on November nineteenth.",
  [G("stat", k="HOUSE VOTE · NOV. 18, 2025", a="427 – 1", size=250, b="the House passes the Epstein Files Transparency Act", c="Senate: unanimous consent · signed Nov. 19, 2025", source=S_ACT)], {}),
 ("Republican Representative Clay Higgins cast the one no vote. | The bill came up under a procedure that required a two-thirds majority, and it cleared that bar by a wide margin.",
  [C("dv346026c", 15.0, lab=CAP)], {}),
 ("The law told the Justice Department to publish its Epstein records in a searchable, downloadable form within thirty days, | and to declassify them to the extent possible.",
  [G("list", kicker="THE LAW · WHAT IT REQUIRED", title="Public Law 119-38", items=[
      dict(t="Publish the Epstein files", s="SEARCHABLE · DOWNLOADABLE"), dict(t="Within 30 days of passage", s="DEADLINE: DEC. 19, 2025"),
      dict(t="Declassify to the extent possible"), dict(t="A list of redactions to Congress", s="WITHIN 15 DAYS OF RELEASE")], source=S_ACT)], {}),
 ("Some redactions were allowed. | Victims' personal information. | Child sexual abuse material. | Images that depict death, abuse, or injury. | And the department could hold back material that would jeopardize an active federal investigation, | in a narrowly tailored and temporary way.",
  [C("dv346119c", 33.0, lab=CAP2)], {}),
 ("But the law also drew a line.",
  [C("dv346026c", 15.0, lab=CAP)], dict(gap=0.5)),
 ("No record, it said, may be withheld, delayed, or redacted on the basis of embarrassment, reputational harm, or political sensitivity.",
  [G("quote", q="No record may be withheld, delayed, or redacted on the basis of {{embarrassment, reputational harm, or political sensitivity.}}",
     who="Epstein Files Transparency Act", role="Public Law 119-38 · Nov. 19, 2025", size=50, source=S_ACT)], dict(slow=True)),
 ("It also required a list, sent to the House and Senate Judiciary Committees, of government officials and politically exposed persons named in the files. | Being on such a list is not evidence of wrongdoing.",
  [C("dv346119c", 8.0, lab=CAP2)], {}),
 ("Two limits are worth knowing. | The law set no penalty for missing the deadline. | And it covers only the Justice Department. | Not the State Department, the Treasury, the CIA, or the N S A, CBS News noted.",
  [G("list", kicker="THE LAW · ITS LIMITS", title="What the Act does not do", items=[
      dict(t="No penalty for noncompliance"), dict(t="Covers only the Justice Department", s="NOT STATE, TREASURY, CIA, NSA"),
      dict(t="Redactions allowed for victims and CSAM"), dict(t="Narrow, temporary hold for live investigations")], source=S_ACT)], {}),

 # ---------------- II. DECEMBER 19 ----------------
 ("The deadline was Friday, December nineteenth, twenty twenty-five.",
  [G("chapter", n="II", t="December 19")], {}),
 ("That day, the Department posted new records and thousands of photographs, according to CBS News.",
  [C("dv1026930c", 28.0, lab=DCA)], dict(tag=("WASHINGTON, D.C.", "DECEMBER 19, 2025"))),
 ("Within hours, lawmakers of both parties were complaining. | The first release, they said, was full of black boxes.",
  [C("dv346026c", 3.0, lab=CAP)], {}),
 ("CBS News counted. | At least five hundred fifty pages in that first release were blacked out entirely.",
  [G("stat", k="FIRST RELEASE · DEC. 2025", a="550+", size=300, b="pages entirely blacked out", c="CBS News count · at least", source=S_D19)], {}),
 ("One document was one hundred nineteen pages, labeled in its corner Grand Jury, N Y. | We pulled it from the Department's release. | Every page, black.",
  [I("p_b1", kb="in", focus=[0.5, 0.5], lab=DOC + "EFTA00005586, PAGE 1 OF 119"), I("p_b60", kb="in", focus=[0.5, 0.2], lab=DOC + "EFTA00005586, PAGE 60 OF 119")], {}),
 ("Another was a series of three documents totaling two hundred fifty-five pages. | These are the first pages of each: one hundred pages, one hundred pages, and fifty-five. | We checked all two hundred fifty-five. | All black.",
  [I("p_series", kb="in", focus=[0.5, 0.5], lab=DOC + "EFTA00006109, EFTA00006209 AND EFTA00006309 · FIRST PAGE OF EACH · 100 + 100 + 55 PAGES")], {}),
 ("And CBS found at least one hundred eighty more blacked-out pages inside files that were otherwise mostly redacted.",
  [I("g_119", kb="out", focus=[0.5, 0.5], lab="OUR VISUALIZATION · EVERY TILE IS ONE BLACK PAGE OF THE RELEASED FILE")], {}),
 ("Representative Khanna called it an incomplete release with too many redactions. | Representative Massie said it grossly fails to comply with both the spirit and the letter of the law.",
  [G("quote", q="{{Grossly fails to comply}} with both the spirit and the letter of the law.", who="Rep. Thomas Massie (R-Ky.)", role="On the Dec. 2025 release · as reported by CBS News", size=62, source=S_D19)], {}),
 ("Senate Democratic leader Chuck Schumer put it this way.",
  [G("quote", q="Simply releasing a mountain of blacked out pages {{violates the spirit of transparency and the letter of the law…}}", who="Sen. Chuck Schumer (D-N.Y.)", role="Senate Minority Leader · Dec. 2025 · as reported by CBS News", size=50, source=S_D19)], {}),
 ("The Justice Department's answer: | its letter to Congress cited child abuse images and ongoing investigations. | Deputy Attorney General Todd Blanche said the only redactions applied were those required by law, full stop. | And the Department said the files would keep coming on a rolling basis.",
  [G("quote", q="The only redactions being applied to the documents are those {{required by law — full stop.}}", who="Todd Blanche", role="Deputy Attorney General · Dec. 2025 · to Fox News Digital, as reported by CBS News", size=56, source=S_D19)], {}),
 ("The Department also said on social media that no politicians' names had been redacted. | And Blanche's letter said more than two hundred Department lawyers were reviewing the files, | and that grand jury transcripts needed additional layers of review. | He said the full set could not be finished that day.",
  [C("dv346119c", 25.0, lab=CAP2)], {}),

 # ---------------- III. THE NEXT DAY ----------------
 ("Then came Saturday.",
  [G("chapter", n="III", t="The Next Day")], {}),
 ("On Saturday, December twentieth, CBS News reported, the Department said a largely unredacted version of a one hundred nineteen page grand jury transcript was among the files it released.",
  [I("t1", kb="in", focus=[0.5, 0.3], lab=DOC + "EFTA00008744, PAGE 1 · GRAND JURY TRANSCRIPT")], dict(tag=("JUSTICE DEPARTMENT RELEASE", "DECEMBER 20, 2025"))),
 ("We pulled it too, and we are showing only its first two pages. | Its cover reads: United States Grand Jury, Southern District of New York. | United States versus Ghislaine Maxwell.",
  [I("t1", kb="out", focus=[0.4, 0.2], lab=DOC + "EFTA00008744, PAGE 1 · NAMES ALREADY BLACK-BARRED BY THE DEPARTMENT")], {}),
 ("Maxwell was convicted in December twenty twenty-one of sex trafficking of a minor and other charges, and sentenced to twenty years in prison.",
  [C("dv346119c", 15.0, lab=CAP2)], {}),
 ("The date on the transcript is March twenty-ninth, twenty twenty-one. | The witness on these pages is a New York City police detective, sworn in before the grand jury. | His name, and the prosecutors' names, were already covered by the Department's own black bars.",
  [I("t2", kb="in", focus=[0.4, 0.5], lab=DOC + "EFTA00008745, PAGE 2 · A DETECTIVE'S NAME COVERED BY THE DEPARTMENT")], {}),
 ("Grand jury testimony is normally secret under federal rules. | CBS reported that the judge who presided over Maxwell's trial required the top federal prosecutor in Manhattan to personally certify | that grand jury documents contain no victims' personal information.",
  [C("dv977364c", 31.0, lab=NYC)], dict(tag=("NEW YORK CITY", "DECEMBER 2025"))),
 ("Here is what we can and cannot say. | The black file and the open transcript are both one hundred nineteen pages, but they carry different file numbers: E F T A zero zero zero zero five five eight six, and E F T A zero zero zero zero eight seven four four. | From the pages alone, we cannot tell whether they are the same document. | We can tell you what the Department said it was doing: reviewing again, with, quote, an abundance of caution for victims and their families.",
  [G("doc", header="STATEMENT · JUSTICE DEPARTMENT · DEC. 2025 · AS QUOTED BY CBS NEWS", title="Posted on social media",
     lines=["\"Documents and photos will continue to be reviewed consistent with", "the law and {{with an abundance of caution for victims and their families.}}\""],
     stamp="RECREATED", source=S_D19)], dict(slow=True)),

 # ---------------- IV. THREE MILLION PAGES ----------------
 ("On January thirtieth, twenty twenty-six, came the big one.",
  [G("chapter", n="IV", t="Three Million Pages")], {}),
 ("The Department said it had published more than three million additional pages, more than two thousand videos, and about one hundred eighty thousand images.",
  [G("stat", k="DOJ RELEASE · JAN. 30, 2026", a="3 MILLION+", size=200, b="pages, plus 2,000+ videos and about 180,000 images", c="before this release: about 500,000 pages", source=S_J30)], {}),
 ("Where did it all come from? | Scripps News listed the sources. | The federal criminal cases against Epstein in Florida and New York. | The New York prosecution of Ghislaine Maxwell. | Investigations into his death. | Multiple F B I investigations. | And a Justice Department Inspector General review of his death.",
  [G("list", kicker="WHAT THE RELEASE DREW ON", title="Source records, per Scripps News", items=[
      dict(t="Federal cases against Epstein", s="FLORIDA AND NEW YORK"), dict(t="The Maxwell prosecution", s="NEW YORK"),
      dict(t="Investigations into his death", s="INCLUDING THE INSPECTOR GENERAL REVIEW"), dict(t="Multiple FBI investigations", s="AND A FLORIDA CASE")], source=S_J30)], {}),
 ("That Inspector General review is the report we read in part two.",
  [C("dv994186c", 19.0, lab=HAR)], dict(tag=("NEW YORK CITY", "JANUARY 2026"))),
 ("The then-Attorney General's letter said Department staff had identified more than six million pages that needed review. | About three million of those were published that day.",
  [G("stat", k="PAGES THE DEPARTMENT SAID IT REVIEWED", a="6 MILLION+", size=230, b="identified for review", c="about 3 million published January 30", source=S_J30)], {}),
 ("PBS reported that the Department said it had put more than five hundred lawyers on the review.",
  [C("dv346119c", 15.0, lab=CAP2)], {}),
 ("The rest? | NPR reported that about half of those six million files would not be released, | because the Department said they contain child sexual abuse material, internal deliberations, or attorney-client privileged information, | or are duplicates or unrelated.",
  [C("dv346026c", 3.0, lab=CAP)], {}),
 ("PBS reported a narrower figure: about two hundred thousand pages withheld or redacted because of various privileges, including attorney-client privilege. | And the Department said it would send Congress a more detailed look at government officials and politically exposed persons.",
  [G("stat", k="PRIVILEGES CITED · AS REPORTED BY PBS", a="~200,000", size=230, b="pages withheld or redacted for privilege", c="including attorney-client privilege", source=S_J30)], {}),
 ("Be careful with the totals. | NPR said many of the released files are duplicative. | CBS later reported that hundreds of thousands of the released emails came nearly all from a single account.",
  [C("dv346119c", 25.0, lab=CAP2)], {}),
 ("The Department also gave its own warning. | Some of the material, it said, may contain false or misleading information, | including reports that were investigated and later cleared.",
  [G("quote", q="Some material, the Department said, {{“may contain false or misleading information.”}}", who="Justice Department", role="Jan. 30, 2026 · as reported by Scripps News", size=66, source=S_J30)], dict(slow=True)),
 ("It said notable individuals and politicians were not redacted in any released file.",
  [C("dv346119c", 8.0, lab=CAP2)], {}),
 ("It also said some files were not being released at all, including those that depict violence. | Some pornographic images were redacted, and the Department said it treated every woman depicted in such images as a victim.",
  [C("dv994186c", 30.0, lab=HAR)], {}),
 ("Deputy Attorney General Blanche said the Department had complied with the law. | And at a press briefing he said this:",
  [G("quote", q="We complied with the statute, {{we complied with the act.}}", who="Todd Blanche", role="Deputy Attorney General · Jan. 30, 2026 · as reported by PBS NewsHour", size=62, source=S_J30)], {}),
 ("\"I don't think that the public or you all are going to uncover men within the Epstein files that abused women.\" | Scripps News reported that the release also includes uncorroborated allegations, which the Department warned may be false.",
  [G("quote", q="I don't think that the public or you all are going to uncover {{men within the Epstein files that abused women.}}", who="Todd Blanche", role="Deputy Attorney General · Jan. 30, 2026 · press briefing, as reported by Scripps News", size=48, source=S_J30)], {}),
 ("By the Department's own account, PBS reported, about two and a half million of these documents remain out of public view. | Representative Khanna asked why.",
  [G("stat", k="AS REPORTED BY PBS NEWSHOUR · JAN. 30, 2026", a="2.5 MILLION", size=190, b="documents remain out of public view, by the DOJ's own account", c="Khanna asked why · as reported by PBS NewsHour", source=S_J30)], {}),
 ("The Department's position is that those pages are duplicative, unrelated, or protected by privilege or law.",
  [C("dv346119c", 1.5, lab=CAP2)], {}),

 # ---------------- V. THE MISTAKES ----------------
 ("Then came a different problem: names that were supposed to stay hidden.",
  [G("chapter", n="V", t="The Mistakes")], {}),
 ("In a letter to federal judges in New York, the Department said its staff were working around the clock to run additional searches for documents that may need more redaction.",
  [C("dv977364c", 36.0, lab=NYC)], dict(tag=("NEW YORK CITY", "FEBRUARY 2026"))),
 ("Victims and their lawyers, it said, had identified new victims and new identifiers, such as nicknames, email addresses, and family names. | NPR reported that the Department removed access to some pages.",
  [G("doc", header="LETTER · JUSTICE DEPARTMENT TO FEDERAL JUDGES · FEB. 2026 · AS QUOTED BY NPR", title="Southern District of New York",
     lines=["Victims and victim counsel {{have identified new victims and new identifiers}}", "(such as nicknames, email addresses, and family names)"],
     stamp="RECREATED", source=S_ERR)], dict(slow=True)),
 ("The Department said about a tenth of a percent of pages had identifying information left unredacted. | NPR's reporter noted that, across millions of pages, that is still several thousand pages.",
  [G("stat", k="DOJ'S OWN ESTIMATE · AS REPORTED BY NPR", a="~0.1%", size=300, b="of pages had identifying information unredacted", c="NPR: still several thousand pages", source=S_ERR)], {}),
 ("The Department's own framing, as NPR reported it: | it had redacted thousands of victim names in the millions of pages it published, to protect the innocent.",
  [C("dv977364c", 20.0, lab=NYC)], {}),
 ("One survivor told NPR there was no explanation for how it could have been done so poorly. | And in November twenty twenty-six, another told NPR she found her own name and a number unredacted.",
  [C("dv994186c", 54.5, lab=HAR)], {}),
 ("The errors ran in both directions. | CBS reported that names of business contacts were blacked out without an obvious reason, and names of many Department officials were redacted too. | After CBS asked about specific redactions, the Department unredacted a photograph and two emails.",
  [C("dv977364c", 50.0, lab=NYC)], {}),

 # ---------------- VI. WHAT'S MISSING ----------------
 ("So what is missing?",
  [G("chapter", n="VI", t="What's Missing")], {}),
 ("The Department's position, as CBS summarized it in June: | every document required by the law has been released. | It said the roughly three million unreleased pages are duplicative, unrelated to Epstein, or privileged. | And the redactions, it said, were consistent with the Act.",
  [C("dv346026c", 15.0, lab=CAP)], dict(tag=("WASHINGTON, D.C.", "JUNE 2026"))),
 ("The law, CBS reported, calls for a written justification for every redaction, published in the Federal Register and submitted to Congress. | What the Department has offered instead, CBS said, is a general statement that its redactions were consistent with the Act, with no specific justifications. | A journalist has sued the Department to force those justifications into the open.",
  [C("dv346119c", 20.0, lab=CAP2)], {}),
 ("CBS News said it did not find several things. | These are CBS's findings, not Department statements, and they are as of June.",
  [G("list", kicker="WHAT CBS SAYS IT COULD NOT FIND · AS OF JUNE 2026", title="Gaps reported by CBS News", items=[
      dict(t="Most of the earliest emails"), dict(t="About 20,000 messages from one account", s="EARLIER ARCHIVED SEPARATELY"),
      dict(t="Signal messages"), dict(t="At least one attachment the emails refer to")], source=S_MIS)], dict(slow=True)),
 ("A sixty-nine page D E A report appeared, | but none of the related records did. | And more than seventy percent of about five thousand documents listed in an index from the Maxwell case could not be found. | The Department told CBS many may be duplicates.",
  [G("stat", k="MAXWELL CASE INDEX · AS REPORTED BY CBS NEWS", a="70%+", size=300, b="of about 5,000 listed documents not found", c="DOJ told CBS many may be duplicates", source=S_MIS)], {}),
 ("CBS also reported that suspicious activity reports, the kind banks file, were released, pulled back, and then re-released in entirely redacted form. | Senator Ron Wyden's office told CBS that the D E A had declined his request for information about its investigation.",
  [C("dv346119c", 38.0, lab=CAP2)], {}),
 ("On the possibility that many of the unreleased pages are duplicates, Representative Robert Garcia, the top Democrat on the House Oversight Committee, said: okay, that's fine, let's see them. | He also said he is not sure what is in the three million.",
  [G("quote", q="{{OK, that's fine, let's see them.}} … We're not sure what's in the 3 million.", who="Rep. Robert Garcia (D-Calif.)", role="Top Democrat, House Oversight Committee · as reported by CBS News, June 2026", size=56, source=S_MIS)], {}),
 ("And there is the jail video, which connects to part two. | CBS reported that footage from one hundred forty-seven cameras, covering twenty-four hours around Epstein's death, over eight terabytes, was not among the released files.",
  [G("stat", k="JAIL VIDEO · AS REPORTED BY CBS NEWS", a="147", size=330, b="cameras · 24 hours · over 8 terabytes", c="CBS: not among the released files", source=S_MIS)], {}),
 ("The Department's internal documents, CBS said, call that footage not significant, since the cameras in the jail's special housing unit were not active at the time. | CBS added that, by law, those videos should have been released. | The Department says it has released every document the law requires.",
  [C("dv977364c", 20.0, lab=NYC)], {}),
 ("Members of Congress can review redacted material, CBS reported, | but the process is time-consuming, and some lawmakers complained that the Department monitors their searches. | Lawmakers also asked the Government Accountability Office to investigate the redactions, and CBS reported that the office announced an investigation.",
  [C("dv346119c", 1.5, lab=CAP2)], {}),

 # ---------------- VII. THE SECOND FIGHT ----------------
 ("Which brings us back to November.",
  [G("chapter", n="VII", t="The Second Fight")], {}),
 ("On November tenth, the Republican-led House Oversight Committee released a report faulting the federal government for failing to hold Epstein accountable. | Chairman James Comer said the Justice Department must interview or re-interview key witnesses, and investigate Epstein associates accused of criminal activity.",
  [G("quote", q="The Justice Department must {{“interview or re-interview key witnesses”}} and “investigate Epstein associates accused of criminal activity.”", who="Rep. James Comer (R-Ky.)", role="Chairman, House Oversight Committee · Nov. 2026 · as paraphrased by NBC News", size=44, source=S_NOV)], dict(tag=("WASHINGTON, D.C.", "NOVEMBER 10, 2026"))),
 ("The committee's top Democrat, Robert Garcia, called the report partisan, and said it was based on an incomplete investigation.",
  [G("quote", q="{{Based on an incomplete investigation.}}", who="Rep. Robert Garcia (D-Calif.)", role="Top Democrat, House Oversight Committee · Nov. 2026 · called the report partisan", size=80, source=S_NOV)], {}),
 ("The next day, the petition reached two hundred eighteen signatures. | According to CBS, all House Democrats signed, and four Republicans: Massie, Nancy Mace, Ralph Norman, and Brian Fitzpatrick.",
  [G("stat", k="DISCHARGE PETITION · NOV. 11, 2026", a="218", size=330, b="signatures · all Democrats and 4 Republicans, per CBS", c="Massie · Mace · Norman · Fitzpatrick", source=S_NOV)], {}),
 ("The new bill would allow members of Congress, state attorneys general, local prosecutors, and survivors to sue the Justice Department for withholding documents. | It would also let victims privately view unredacted records that mention them.",
  [G("list", kicker="THE SECOND BILL · AS REPORTED BY CBS NEWS AND ROLL CALL", title="What it would change", items=[
      dict(t="Members of Congress could sue the DOJ"), dict(t="State attorneys general and local prosecutors could sue"),
      dict(t="Survivors could sue"), dict(t="Victims could privately view unredacted records about them")], source=S_NOV)], {}),
 ("Under House rules, it must sit for seven legislative days before a signer can call it up. | Roll Call reported no vote date. | ABC News reported a vote could come as early as December second or third.",
  [C("dv346026c", 15.0, lab=CAP)], {}),
 ("Representative Massie said in July that the Department continues to unlawfully withhold over three million Epstein files, and he says it is maintaining heavy redactions. | The Department's position, again, is that it has released everything the law requires.",
  [G("quote", q="The Department of Justice continues to {{unlawfully withhold over 3 million Epstein files}} that should be released to the public.", who="Rep. Thomas Massie (R-Ky.)", role="July 2026 statement, as quoted by CBS News · DOJ disputes this", size=58, source=S_NOV)], {}),

 # ---------------- CLOSE ----------------
 ("So here is where the record stands. | A law that said release everything, except what the law protects. | Black pages that the Department says the law required. | Redaction errors, which the Department acknowledged, left some victims' identifying information visible. | And a dispute over the roughly three million unreleased pages: the Department says they are duplicates, unrelated, or privileged; critics in both parties say they want to see them.",
  [G("timeline", kicker="THE FILES, BY THE RECORD", title="Nov. 2025 – Nov. 2026", events=[
      dict(y="NOV 19", t="Law signed"), dict(y="DEC 19", t="First release"), dict(y="DEC 20", t="Transcript posted"),
      dict(y="JAN 30", t="3 million pages"), dict(y="JUN", t="CBS lists gaps"), dict(y="NOV 11, 2026", t="Petition: 218")], source=S_NOV)], dict(slow=True)),
 ("Here is our question for you. | The Justice Department says it has followed the law. | Critics in both parties say it has not. | The Government Accountability Office is looking into the redactions. | Tell us in the comments what you make of the records, and please keep it to the records.",
  [I("p_b60", kb="in", focus=[0.5, 0.5], lab=DOC + "EFTA00005586, PAGE 60 OF 119")], {}),
 ("Next in this series: the votes. | How each party voted on the first law, and what the second bill would change.",
  [G("end", n="019", next="The votes: how Congress fought over the files")], dict(gap=2.5)),
]

PRON = [("Teterboro", "Teter-borough"), ("Comer", "Comer"), ("Massie", "Massey"), ("Khanna", "Kahna"), ("Ghislaine", "Ghee-lane"),
        ("Maxwell", "Maxwell"), ("Bondi", "Bondy"), ("Blanche", "Blanch"), ("Schumer", "Shoomer"), ("Fitzpatrick", "Fitz-patrick"),
        ("Mace", "Mace"), ("F B I", "F B I"), ("D E A", "D E A"), ("N S A", "N S A"), ("U S", "U S"), ("p m", "P M"), ("a m", "A M"),
        ("Garcia", "Garcia"), ("Wyden", "Why-den"), ("re-interview", "re-interview"), ("Higgins", "Higgins"), ("E F T A", "E F T A"), ("N Y", "N Y"), ("N P R", "N P R"), ("Scripps", "Scripps"), ("Roll Call", "Roll Call")]

DISPLAY = [
 ("F B I", "FBI"), ("D E A", "DEA"), ("N S A", "NSA"), ("N P R", "NPR"), ("U S", "U.S."), ("Grand Jury, N Y", "Grand Jury-NY"),
 ("One hundred nineteen pages", "119 pages"), ("one hundred nineteen pages", "119 pages"), ("one hundred nineteen page", "119-page"),
 ("one hundred nineteen", "119"), ("two hundred fifty-five", "255"), ("fifty-five", "55"), ("one hundred pages, one hundred pages", "100 pages, 100 pages"),
 ("five hundred fifty pages", "550 pages"), ("one hundred eighty more", "180 more"), ("two thousand seven", "2007"),
 ("three million pages", "3 million pages"), ("three million additional pages", "3 million additional pages"), ("six million pages", "6 million pages"),
 ("six million files", "6 million files"), ("three million published", "3 million published"), ("three million files", "3 million files"),
 ("three million unreleased pages", "3 million unreleased pages"), ("two million and a half", "2.5 million"), ("two and a half million", "2.5 million"),
 ("about two thousand videos", "about 2,000 videos"), ("one hundred eighty thousand images", "180,000 images"),
 ("two hundred thousand pages", "200,000 pages"), ("more than two thousand videos", "more than 2,000 videos"), ("E F T A zero zero zero zero eight seven four four", "EFTA00008744"), ("two hundred eighteen", "218"), ("four hundred twenty-seven to one", "427 to 1"),
 ("thirty days", "30 days"), ("fifteen days", "15 days"), ("seven legislative days", "7 legislative days"), ("twenty years", "20 years"),
 ("sixty-nine page", "69-page"), ("seventy percent", "70 percent"), ("about five thousand documents", "about 5,000 documents"),
 ("one hundred forty-seven cameras", "147 cameras"), ("twenty-four hours", "24 hours"), ("eight terabytes", "8 terabytes"),
 ("about a tenth of a percent", "about 0.1 percent"), ("twenty twenty-six", "2026"), ("twenty twenty-five", "2025"), ("twenty twenty-one", "2021"),
 ("July twenty twenty-five", "July 2025"), ("November eighteenth", "November 18"), ("November nineteenth", "November 19"),
 ("November eleventh", "November 11"), ("November tenth", "November 10"), ("December nineteenth", "December 19"), ("December twentieth", "December 20"),
 ("January thirtieth", "January 30"), ("March twenty-ninth", "March 29"), ("December second or third", "December 2 or 3"),
 ("About 20,000", "About 20,000"), ("about twenty thousand", "about 20,000"), ("Public Law 119-38", "Public Law 119-38"),
 ("E F T A zero zero zero zero five five eight six", "EFTA00005586"), ("five six four five", "EFTA00005645"), ("E F T A", "EFTA"), ("Page sixty", "Page 60"), ("two hundred Department lawyers", "200 Department lawyers"), ("five hundred lawyers", "500 lawyers"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="019", title="What's Actually Inside the Epstein Files (and What's Missing)",
    imgs={k: "/home/claude/src/img/" + k + ".jpg" for k in ["p_b1", "p_b60", "p_series", "t1", "t2", "g_119"]},
    credit="Documents: U.S. Department of Justice, Epstein Library (EFTA00005586, 6109, 6209, 6309, 8744-8745), released under the Epstein Files Transparency Act; names black-barred by the Department.\\NB-roll: DoD via DVIDS; modern b-roll does not show the events described. Graphics marked RECREATED are our own summaries of public records; \"our visualization\" tiles are ours.",
    shorts=[
        dict(id="s1", lines=[1, 4], tpl="yellow", hook="119 PAGES<br>[ALL BLACK]", hs=200),
        dict(id="s2", lines=[24, 28], tpl="red", hook="550+ PAGES<br>[BLACKED OUT]", hs=160),
        dict(id="s3", lines=[40, 44], tpl="blue", hook="3 MILLION<br>[PAGES]", hs=200),
        dict(id="s4", lines=[69, 71], tpl="white", hook="THE MISSING<br>[JAIL VIDEO]", hs=190),
    ],
    yshorts=[
        dict(id="y1", lines=[26, 27], tpl="red", hook="255 PAGES<br>[ALL BLACK]", hs=200),
        dict(id="y2", lines=[65, 66], tpl="white", hook="WHAT CBS<br>COULD NOT<br>[FIND]", hs=150),
        dict(id="y3", lines=[13, 14], tpl="yellow", hook="427 TO 1<br>[ONE NO VOTE]", hs=150),
    ],
)


# ---- shot coverage for long lines (more than ~8 s): extra shots from different windows (explicit table) ----
_C = lambda n, s, lab: C(n, s, lab=lab)
EXTRA = {
 5: [_C("dv346119c", 12.0, CAP2), _C("dv346026c", 15.0, CAP)],
 6: [_C("dv977364c", 24.0, NYC), _C("dv994186c", 20.0, HAR)],
 12: [_C("dv346026c", 8.0, CAP)],
 14: [_C("dv346119c", 28.0, CAP2)],
 16: [_C("dv977364c", 60.0, NYC), _C("dv994186c", 40.0, HAR)],
 19: [_C("dv346026c", 2.0, CAP)],
 31: [_C("dv994186c", 64.0, HAR), _C("dv977364c", 72.0, NYC)],
 37: [_C("dv977364c", 44.0, NYC), _C("dv994186c", 54.5, HAR)],
 45: [_C("dv346119c", 12.0, CAP2), _C("dv346026c", 15.0, CAP)],
 47: [_C("dv977364c", 0.0, NYC)],
 50: [_C("dv1026930c", 28.0, DCA)],
 56: [_C("dv994186c", 20.0, HAR)],
 59: [_C("dv994186c", 40.0, HAR)],
 60: [_C("dv977364c", 60.0, NYC)],
 61: [_C("dv994186c", 64.0, HAR), _C("dv1026930c", 31.0, DCA)],
 63: [_C("dv346119c", 34.0, CAP2), _C("dv346119c", 1.0, CAP2)],
 64: [_C("dv346026c", 2.0, CAP), _C("dv977364c", 72.0, NYC), _C("dv346119c", 34.0, CAP2)],
 67: [_C("dv346026c", 8.0, CAP), _C("dv994186c", 20.0, HAR)],
 70: [_C("dv346026c", 13.0, CAP), _C("dv346119c", 12.0, CAP2)],
 71: [_C("dv977364c", 48.0, NYC), _C("dv346026c", 13.0, CAP)],
 77: [_C("dv346119c", 23.0, CAP2)],
}
for _i, _x in EXTRA.items(): LINES[_i - 1][1].extend(_x)
REPLACE = {
 1: [I("p_b1", kb="in", focus=[0.5, 0.45], lab=DOC + "EFTA00005586, PAGE 1 OF 119"), I("g_119", kb="in", focus=[0.5, 0.5], lab="OUR VISUALIZATION · EVERY TILE IS ONE BLACK PAGE OF THE RELEASED FILE")],
 3: [I("p_b1", kb="in", focus=[0.8, 0.95], lab=DOC + "EFTA00005586, PAGE 1 OF 119 · FOOTER NUMBER EFTA00005586"), I("p_b60", kb="in", focus=[0.8, 0.95], lab=DOC + "EFTA00005586, PAGE 60 OF 119 · FOOTER NUMBER EFTA00005645")],
 4: [C("dv346026c", 2.0, lab=CAP), I("t1", kb="in", focus=[0.5, 0.3], lab=DOC + "EFTA00008744, PAGE 1 · GRAND JURY TRANSCRIPT")],
 26: [I("p_series", kb="in", focus=[0.3, 0.5], lab=DOC + "EFTA00006109, EFTA00006209 AND EFTA00006309 · FIRST PAGE OF EACH · 100 + 100 + 55 PAGES"), I("p_series", kb="out", focus=[0.7, 0.5], lab=DOC + "EFTA00006109, EFTA00006209 AND EFTA00006309 · FIRST PAGE OF EACH · 100 + 100 + 55 PAGES")],
 33: [C("dv346119c", 12.0, lab=CAP2), I("t1", kb="in", focus=[0.5, 0.3], lab=DOC + "EFTA00008744, PAGE 1 · GRAND JURY TRANSCRIPT")],
 36: [I("t2", kb="in", focus=[0.4, 0.3], lab=DOC + "EFTA00008745, PAGE 2 · A DETECTIVE'S NAME COVERED BY THE DEPARTMENT"), I("t2", kb="out", focus=[0.5, 0.6], lab=DOC + "EFTA00008745, PAGE 2 · A DETECTIVE'S NAME COVERED BY THE DEPARTMENT")],
 80: [I("p_b1", kb="in", focus=[0.5, 0.5], lab=DOC + "EFTA00005586, PAGE 1 OF 119"), I("g_119", kb="out", focus=[0.5, 0.5], lab="OUR VISUALIZATION · EVERY TILE IS ONE BLACK PAGE OF THE RELEASED FILE")],
}
for _i, _x in REPLACE.items(): LINES[_i - 1] = (LINES[_i - 1][0], _x, LINES[_i - 1][2])
