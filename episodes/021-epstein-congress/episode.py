# FILE 021 — Congress Voted 427 to 1 for the Epstein Files. Then What?
# Epstein series, part 4 of 4. Fresh hook: Nov. 10, 2026 House Oversight (majority) report; Nov. 11, 2026 second discharge petition reached 218.
# SOURCES (all opened; see research.md): PBS, Axios, NBC, NPR, AP via WHYY, Roll Call, CBS, ABC/GMA, House Oversight press release, Massie press release.
# LEGAL: only public officials speaking/voting in their roles are named (members of Congress, the Attorneys General and Deputy AG, the Speaker, the Senate leaders,
#   the President in his official acts). No private person is named. No photographs of any person. Victims/survivors never named or shown.
#   Quotes are attributed to the outlet that reported them. "Appearing in these records is not evidence of wrongdoing" is stated in the cold open.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)

CAP = "B-ROLL · THE U.S. CAPITOL, WASHINGTON, D.C., 2012"
CAP2 = "B-ROLL · WASHINGTON, D.C., AROUND THE CAPITOL, 2012"
TRE = "B-ROLL · THE U.S. TREASURY BUILDING, WASHINGTON, D.C., 2012"
WH = "B-ROLL · THE WHITE HOUSE, WASHINGTON, D.C., 2012"
DCA = "B-ROLL · WASHINGTON, D.C., SEEN FROM A MILITARY JET COCKPIT, 2026"

S_VOTE = "SOURCE: NPR AND AP (NOV. 18, 2025) · HOUSE CLERK ROLL CALL 289 AS REPORTED"
S_MEMO = "SOURCE: PBS NEWSHOUR (JULY 2025) · AXIOS (JULY 2025)"
S_PET = "SOURCE: NBC NEWS (NOV. 12, 2025)"
S_DEC = "SOURCE: ROLL CALL (DEC. 19, 2025) · NPR (DEC. 21, 2025) · NBC NEWS"
S_JAN = "SOURCE: NPR (JAN. 30, 2026) · ABC NEWS / GMA · PBS NEWSHOUR"
S_PEP = "SOURCE: PBS NEWSHOUR (FEB. 2026)"
S_HEAR = "SOURCE: NPR (FEB. 11, 2026)"
S_APR = "SOURCE: AP-STYLE REPORT VIA SPECTRUM NEWS (APR. 3, 2026) · LOCAL 10 (JUNE 4, 2026) · PBS NEWSHOUR (JULY 15, 2026)"
S_REP = "SOURCE: HOUSE OVERSIGHT COMMITTEE (NOV. 10, 2026) · NPR · ABC NEWS / GMA"
S_II = "SOURCE: REP. MASSIE'S OFFICE · AXIOS · ROLL CALL · ABC NEWS (NOV. 2026)"

LINES = [
 # ---------------- COLD OPEN ----------------
 ("Four hundred twenty-seven to one. | That was the House vote, in November twenty twenty-five, to order the release of the Epstein files. | A year later, Congress is fighting over them again. | So what is the fight about?",
  [G("stat", k="HOUSE VOTE · NOV. 18, 2025", a="427 – 1", size=300, b="to release the Epstein files", c="and a year later, Congress is still fighting over them", source=S_VOTE)], dict(tag=("WASHINGTON, D.C.", "NOVEMBER 2026"))),
 ("The Justice Department says it has met its legal obligations. | Some lawmakers, in both parties, say it has fallen short. | And on November eleventh, a second bill collected enough signatures to force another House vote.",
  [C("dv346026c", 2.0, lab=CAP)], {}),
 ("This is part four of our series on the Epstein records. | Part one covered the two thousand seven Florida deal. | Part two, the Inspector General's report on his death in jail. | Part three, what is inside the files. | Today, the fight in Congress: | who pushed, who resisted, what each side says, and what could happen next.",
  [C("dv346119c", 2.0, lab=CAP2), C("dv346026c", 14.0, lab=CAP)], {}),
 ("One rule before we start. | Appearing in these records is not evidence of wrongdoing. | We name only members of Congress and government officials, in their public roles, and quote what outlets such as N P R, PBS, A P and Roll Call reported them saying.",
  [G("quote", q="Appearing in these records is {{not evidence of wrongdoing.}}", who="Our rule for this series", role="Released in Full", size=70, source="WE NAME ONLY PUBLIC OFFICIALS, IN THEIR PUBLIC ROLES")], dict(slow=True)),
 ("", [G("intro", n="021")], dict(gap=0.2)),
 ("", [G("title", n="021", t="THE VOTES", size=170, sub="Congress and the Epstein Files")], dict(gap=0.4)),

 # ---------------- I. THE MEMO ----------------
 ("It began with a two-page memo.",
  [G("chapter", n="I", t="The Memo")], {}),
 ("On Monday, July seventh, twenty twenty-five, the Justice Department and the F B I released an unsigned memo. | It said that Epstein kept no client list, | and that, according to PBS, no further disclosure would be appropriate or warranted.",
  [G("doc", header="MEMO · JUSTICE DEPARTMENT AND F B I · JULY 7, 2025 · AS REPORTED BY PBS NEWSHOUR", title="Summary of what the memo said",
     lines=["Epstein kept {{no \"client list\".}}", "No further disclosure {{would be appropriate or warranted.}}"], stamp="RECREATED", source=S_MEMO)], dict(slow=True, tag=("WASHINGTON, D.C.", "JULY 2025"))),
 ("PBS reported that the memo also said the department holds more than ten thousand videos and images of child sexual abuse material. | The memo said much of the material was placed under seal by a court to protect victims.",
  [C("dv346119c", 12.0, lab=CAP2)], {}),
 ("The first angry reaction came from conservative figures. | The White House press secretary and a Justice Department spokesman said the Attorney General had meant the files in general, not a literal list, PBS reported.",
  [C("dv346124c", 4.0, lab=WH)], {}),
 ("Within days, the argument moved into Congress. | Speaker Mike Johnson, a Republican, was asked about it on a podcast. | He said, quote, it's a very delicate subject, but we should put everything out there and let the people decide it, end quote, according to Axios.",
  [G("quote", q="It's a very delicate subject, but we should put everything out there and {{let the people decide it.}}", who="Speaker Mike Johnson (R-La.)", role="Podcast interview, July 2025 · as reported by Axios", size=50, source=S_MEMO)], dict(slow=True)),
 ("Democrats, led by Representative Ro Khanna, tried a procedural move to force the Justice Department to release records. | Republicans rejected it as a partisan ploy, Axios reported. | Republican Thomas Massie of Kentucky said he would try something else: a discharge petition.",
  [C("dv346026c", 8.0, lab=CAP)], {}),
 ("Here is what that means. | Normally the Speaker decides what the House votes on. | A discharge petition goes around him. | If two hundred eighteen members, a majority, sign it, the bill can be forced to the floor.",
  [G("stat", k="DISCHARGE PETITION", a="218", size=360, b="signatures: a majority of the House", c="forces a bill to the floor without the Speaker's approval", source="SOURCE: HOUSE RULES, AS DESCRIBED BY ROLL CALL AND ABC NEWS")], {}),

 # ---------------- II. THE PETITION ----------------
 ("But a House committee was already taking its own route.",
  [G("chapter", n="II", t="Subpoenas and a Petition")], {}),
 ("On August fifth, Oversight Committee Chairman James Comer, a Republican, issued eleven subpoenas. | One went to the Justice Department, for its Epstein and Maxwell records. | The others sought depositions from a group of former officials. | N P R reported that Republicans on a subcommittee had joined Democrats to vote for the Justice Department subpoena.",
  [C("dv346119c", 24.0, lab=CAP2), C("dv346120c", 6.0, lab=TRE)], dict(tag=("WASHINGTON, D.C.", "AUGUST 5, 2025"))),
 ("In September, the committee released documents from Epstein's estate, including his will and the two thousand seven non-prosecution agreement from Florida, N P R reported.",
  [C("dv346026c", 16.0, lab=CAP)], {}),
 ("By November, the petition was close. | N B C reported on November twelfth that every Democrat who could sign had done so, along with four Republicans: | Thomas Massie, Marjorie Taylor Greene, Lauren Boebert and Nancy Mace.",
  [G("list", kicker="DISCHARGE PETITION · REPUBLICAN SIGNERS", title="As reported by NBC News, Nov. 12, 2025", items=[
      dict(t="Thomas Massie", s="KENTUCKY"), dict(t="Marjorie Taylor Greene", s="GEORGIA"), dict(t="Lauren Boebert", s="COLORADO"), dict(t="Nancy Mace", s="SOUTH CAROLINA")], source=S_PET)], {}),
 ("A newly sworn-in Democrat, Adelita Grijalva of Arizona, was sworn in that afternoon and supplied the two hundred eighteenth signature, according to AP. | Speaker Johnson had called the push reckless, N B C reported.",
  [C("dv346119c", 34.0, lab=CAP2)], {}),
 ("Six days later, the House voted.",
  [C("dv346026c", 20.0, lab=CAP)], dict(gap=0.4)),

 # ---------------- III. 427 TO 1 ----------------
 ("The vote everyone remembers.",
  [G("chapter", n="III", t="427 to 1")], {}),
 ("On Tuesday, November eighteenth, Speaker Johnson brought the bill to the floor himself, | under a fast-track procedure that required a two-thirds majority, | instead of waiting for the petition.",
  [C("dv346026c", 3.0, lab=CAP)], dict(tag=("WASHINGTON, D.C.", "NOVEMBER 18, 2025"))),
 ("The Epstein Files Transparency Act passed, four hundred twenty-seven to one.",
  [G("stat", k="HOUSE VOTE · NOV. 18, 2025", a="427 – 1", size=300, b="the Epstein Files Transparency Act passes the House", c="216 Republicans and 211 Democrats voted yes · one Republican voted no", source=S_VOTE)], {}),
 ("The one no vote came from Republican Clay Higgins of Louisiana, who argued the bill abandons two hundred fifty years of criminal justice procedure, as N P R reported. | Speaker Johnson voted yes, but called the matter a raw and obvious political exercise, according to A P.",
  [C("dv346119c", 8.0, lab=CAP2)], {}),
 ("Johnson urged the Senate to change the bill to protect victims and whistleblowers. | Senate Majority Leader John Thune declined, saying a four hundred twenty-seven to one vote made that unlikely, CBS News reported.",
  [C("dv346026c", 20.0, lab=CAP)], {}),
 ("Hours later, the Senate passed the bill by unanimous consent. | No objection. No roll call. | Minority Leader Chuck Schumer said it was about, quote, giving the American people the transparency they've been crying for, end quote.",
  [G("quote", q="This is about {{giving the American people the transparency}} they've been crying for.", who="Sen. Chuck Schumer (D-N.Y.)", role="Senate Minority Leader · as reported by AP", size=52, source="SOURCE: AP VIA WHYY (NOV. 18, 2025)")], dict(slow=True)),
 ("Massie, a Republican from Kentucky, and Khanna, a Democrat from California, had pressed the issue together for months. | Khanna urged the Senate to pass the bill unchanged, Axios reported. | And the Senate did not change it.",
  [C("dv346119c", 22.0, lab=CAP2)], {}),
 ("The next evening, President Trump announced that he had signed it. | It became Public Law one nineteen, thirty-eight. | The Justice Department had thirty days.",
  [C("dv346124c", 10.0, lab=WH)], dict(tag=("WASHINGTON, D.C.", "NOVEMBER 19, 2025"))),

 # ---------------- IV. THE DEADLINE ----------------
 ("Thirty days ended on a Friday, December nineteenth.",
  [G("chapter", n="IV", t="The Deadline")], {}),
 ("Here is what the law required, as reported by CBS News. | The Justice Department had to publish its Epstein records in a searchable form within thirty days. | It could redact victims' personal information and child sexual abuse material. | And it could hold back material in a narrow, temporary way if releasing it would jeopardize an active investigation. | But the law said no record could be withheld for embarrassment, reputational harm, or political sensitivity.",
  [G("list", kicker="PUBLIC LAW 119-38 · WHAT IT REQUIRED", title="As reported by CBS News", items=[
      dict(t="Publish the files, searchable", s="WITHIN 30 DAYS · DEC. 19, 2025"), dict(t="Redactions allowed", s="VICTIMS · CHILD ABUSE MATERIAL"),
      dict(t="Narrow, temporary hold", s="ACTIVE INVESTIGATIONS ONLY"), dict(t="No withholding for embarrassment", s="OR REPUTATIONAL HARM OR POLITICAL SENSITIVITY")], source="SOURCE: CBS NEWS (DEC. 2025) · PUBLIC LAW 119-38 AS REPORTED")], dict(slow=True)),
 ("Ahead of the deadline, the Deputy Attorney General, Todd Blanche, told Fox News he expected several hundred thousand documents on deadline day, and more over the following weeks, according to Roll Call.",
  [C("dv346120c", 14.0, lab=TRE)], {}),
 ("Other voices before the deadline came from both sides of the aisle. | Judiciary Committee Chairman Jim Jordan, a Republican, said the department would release what is, quote, required and permitted. | Republican Jeff Van Drew said, quote, my hope and my belief is they're going to release them. | Schumer said, quote, the survivors deserve the truth, and the American people are demanding it.",
  [C("dv346026c", 4.0, lab=CAP)], {}),
 ("On deadline day, Roll Call reported, Democratic Representative Jamie Raskin, the top Democrat on the Judiciary Committee, said he had seen no detectable signs of movement. | Thomas Massie said that if the release contained no names of accused men, then, quote, we know they haven't produced all the documents.",
  [C("dv1026930c", 28.0, lab=DCA)], {}),
 ("The department released part of its records that day, and N P R reported that it missed the deadline. | The department's position, in the weeks that followed, was that it had met its legal obligations. | Some lawmakers, in both parties, pressed for more. | Republican Senator Rand Paul said the department should, quote, give up all the information, release it, end quote.",
  [C("dv346026c", 6.0, lab=CAP)], dict(tag=("WASHINGTON, D.C.", "DECEMBER 19, 2025"))),
 ("Massie and Khanna then proposed inherent contempt, against Attorney General Pam Bondi. | It would let the House itself impose a daily fine, according to N B C News.",
  [G("doc", header="PLAN · REPS. MASSIE (R) AND KHANNA (D) · DEC. 2025 · AS REPORTED BY NPR AND NBC NEWS", title="Inherent contempt against the Attorney General",
     lines=["Inherent contempt would let the House", "{{fine the Attorney General}} directly."], stamp="OUR SUMMARY", source=S_DEC)], dict(slow=True)),
 ("Asked about the threat, Blanche answered, quote, not even a little bit. Bring it on. | A Democratic senator, Tim Kaine, called talk of impeachment premature, and pointed instead to spending bills as a way to force compliance, NBC News reported.",
  [C("dv346119c", 20.0, lab=CAP2)], {}),
 ("The fight moved on to what had actually been released.",
  [C("dv346026c", 12.0, lab=CAP)], dict(gap=0.4)),

 # ---------------- V. THREE MILLION PAGES ----------------
 ("And on January thirtieth, a very large number arrived.",
  [G("chapter", n="V", t="Three Million Pages")], {}),
 ("At a Justice Department news conference, the department said it had released more than three million pages, more than two thousand videos, and about one hundred eighty thousand images. | More than five hundred lawyers and others, it said, reviewed more than six million pages.",
  [G("stat", k="JUSTICE DEPARTMENT · JAN. 30, 2026", a="3 million+", size=240, b="pages released, plus 2,000+ videos and ~180,000 images", c="as announced by the Justice Department · NPR", source=S_JAN)], dict(tag=("WASHINGTON, D.C.", "JANUARY 30, 2026"))),
 ("The department's statement said, quote, notable individuals and politicians were not redacted in the release of any files. | The department said it had met its legal obligations.",
  [C("dv346120c", 2.0, lab=TRE)], {}),
 ("Khanna asked why the rest had not been released. | Representative Robert Garcia, the top Democrat on Oversight, called the release outrageous and concerning. | Massie and Khanna wrote Blanche together, asking to review the unredacted files in person.",
  [C("dv346119c", 8.0, lab=CAP2)], {}),
 ("Less than two weeks later, Bondi faced the House Judiciary Committee.",
  [C("dv346026c", 10.0, lab=CAP)], dict(gap=0.4, tag=("WASHINGTON, D.C.", "FEBRUARY 11, 2026"))),
  ("Republican Thomas Massie told her, quote, this cover-up spans decades, and you are responsible for this portion of it, as N P R reported. | Bondi said she was deeply sorry for what any victim has been through.",
  [G("list", kicker="HOUSE JUDICIARY HEARING · FEB. 11, 2026", title="Two statements, as reported by NPR", items=[
      dict(t="Massie (R): \"This cover-up spans decades\""), dict(t="Bondi: said she was deeply sorry for what any victim has been through")], source=S_HEAR)], dict(slow=True)),
 ("Three days later, Bondi and Blanche sent a letter to the Judiciary Committee leaders in both chambers. | It listed what the department called politically exposed persons who appear in the files, including in press clippings.",
  [C("dv1026930c", 31.0, lab=DCA)], dict(tag=("WASHINGTON, D.C.", "FEBRUARY 14, 2026"))),
 ("PBS reported that the list held about two hundred eighty names, | that the term was never defined, | and that inclusion does not indicate wrongdoing. | Appearing in these records is not evidence of wrongdoing.",
  [G("stat", k="DOJ LETTER · FEB. 14, 2026", a="~280", size=340, b="names on a \"politically exposed persons\" list", c="PBS: the term was not defined · inclusion does not indicate wrongdoing", source=S_PEP)], {}),
 ("At the end of February, Senators Schumer and Dick Durbin, both Democrats, accused the department of a cover-up, ABC News reported. | The department said it would publish any document found to have been improperly tagged.",
  [C("dv346119c", 28.0, lab=CAP2)], {}),

 # ---------------- VI. A CHANGE AT THE TOP ----------------
 ("Then, in the spring, the department got new leadership.",
  [G("chapter", n="VI", t="New Leadership")], {}),
 ("In early April, President Trump announced that Bondi was out. | Blanche became acting Attorney General. | Oversight had subpoenaed Bondi to appear on April fourteenth.",
  [C("dv346124c", 14.0, lab=WH)], dict(tag=("WASHINGTON, D.C.", "APRIL 2026"))),
 ("Khanna, a Democrat, said the Epstein files issue had cost Bondi her job. | Blanche said he had never heard the President link the change to the Epstein files. | A committee spokesperson said Chairman Comer would speak with Republican members about the Bondi subpoena.",
  [C("dv346026c", 18.0, lab=CAP)], {}),
 ("Massie, a Republican, wrote: congratulations to Blanche, quote, now you have thirty days to release the rest of the files.",
  [C("dv346026c", 4.0, lab=CAP)], {}),
 ("In June, the committee released the transcript of Bondi's testimony. | She said Blanche was, quote, in charge, end quote, of the Epstein files, according to Local 10.",
  [C("dv346120c", 22.0, lab=TRE)], {}),
 ("On July fifteenth, Blanche faced the Senate Judiciary Committee for his confirmation hearing. | He said of the redaction mistakes, quote, that doesn't excuse the mistakes, of which I take responsibility. | Democrat Cory Booker said it was, quote, more of a performance review.",
  [C("dv1026930c", 40.0, lab=DCA)], dict(tag=("WASHINGTON, D.C.", "JULY 15, 2026"))),
 ("The Senate confirmed Blanche as Attorney General on August eighth, fifty to forty-nine, according to PBS. | And on July fifteenth, the same day as that hearing, Massie, Khanna and Representative Teresa Leger Fernandez announced a second bill, according to Massie's office.",
  [C("dv346119c", 12.0, lab=CAP2)], {}),

 # ---------------- VII. THE REPORT ----------------
 ("Then, in November, came a committee report.",
  [G("chapter", n="VII", t="The Oversight Report")], {}),
 ("On Tuesday, November tenth, the House Oversight Committee's Republican majority released a report, after a fifteen-month investigation and nineteen interviews and depositions.",
  [G("stat", k="HOUSE OVERSIGHT COMMITTEE · NOV. 10, 2026", a="15 months", size=230, b="19 transcribed interviews and depositions", c="Majority staff report · Chairman James Comer (R-Ky.)", source=S_REP)], dict(tag=("WASHINGTON, D.C.", "NOVEMBER 10, 2026"))),
 ("Its title: a review of the federal government's mishandling of the Epstein and Maxwell criminal investigations. | It points to the two thousand seven non-prosecution agreement, after which Epstein was sentenced to eighteen months.",
  [C("dv346026c", 13.0, lab=CAP)], {}),
 ("On the night Epstein died in custody, the report says, understaffing led to missed rounds and counts, leaving him nearly eight hours without adequate supervision. | It says the Justice Department communicated poorly about releases after the twenty twenty-five law, and that its redactions were deficient.",
  [C("dv346119c", 2.0, lab=CAP2)], {}),
 ("It also says financial institutions failed to act on warning signs, and recommends the Treasury Department review. | And it recommends that Congress pass a bill on nondisclosure agreements and the reporting of suspected grooming.",
  [C("dv346120c", 8.0, lab=TRE)], {}),
 ("Chairman Comer said, quote, the evidence we uncovered makes clear that the Department of Justice must interview or re-interview key witnesses.",
  [G("quote", q="The evidence we uncovered makes clear that the Department of Justice must {{interview or re-interview key witnesses.}}", who="Rep. James Comer (R-Ky.)", role="Chairman, House Oversight Committee · Nov. 10, 2026", size=48, source="SOURCE: HOUSE OVERSIGHT COMMITTEE PRESS RELEASE (NOV. 10, 2026)")], dict(slow=True)),
 ("Representative Garcia, whose party takes over the committee in January, called the report, quote, partisan, and said it came from an incomplete investigation. | Garcia said Democrats plan public hearings.",
  [G("list", kicker="THE REPORT · TWO READINGS", title="As reported by NPR and ABC News", items=[
      dict(t="Majority (R): federal agencies failed to hold Epstein accountable"), dict(t="Garcia (D): the report is \"partisan\"; the investigation \"incomplete\""),
      dict(t="Democrats take the committee in January"), dict(t="Garcia: Democrats plan public hearings")], source=S_REP)], dict(slow=True)),
 ("The Justice Department answered that, quote, the chairman's recommendations have already been addressed. | It said the case is not closed, and that there is no statute of limitations on human trafficking.",
  [C("dv346026c", 3.0, lab=CAP)], {}),

 # ---------------- VIII. ROUND TWO ----------------
 ("And the next day, the petition was complete.",
  [G("chapter", n="VIII", t="Round Two")], {}),
 ("On Wednesday, November eleventh, Democratic Representative John Garamendi of California signed the discharge petition for a second bill. | Roll Call reported that Adam Smith had signed just before him. | That made two hundred eighteen.",
  [G("stat", k="DISCHARGE PETITION · NOV. 11, 2026", a="218", size=360, b="signatures for a second Epstein files bill", c="214 Democrats and 4 Republicans: Massie, Mace, Norman and Fitzpatrick · Axios", source=S_II)], dict(tag=("WASHINGTON, D.C.", "NOVEMBER 11, 2026"))),
 ("The four Republicans were Thomas Massie, Nancy Mace, Ralph Norman and Brian Fitzpatrick.",
  [C("dv346026c", 5.0, lab=CAP)], {}),
 ("Massie said, as Roll Call reported, that Republican colleagues who sign, quote, could be a hero. | And once the petition reaches two hundred eighteen, he said, quote, it goes straight to the floor.",
  [C("dv346119c", 16.0, lab=CAP2)], {}),
 ("So what does the second bill do? | According to Massie's office, it would let state attorneys general, district attorneys, members of Congress, and victims sue the Attorney General over how the department handles Epstein records.",
  [G("list", kicker="EPSTEIN FILES TRANSPARENCY ACT II · ACCORDING TO REP. MASSIE'S OFFICE", title="Who could sue the Attorney General", items=[
      dict(t="State attorneys general"), dict(t="District attorneys"), dict(t="Members of Congress"), dict(t="Epstein victims")], source=S_II)], dict(slow=True)),
 ("Massie said, quote, state attorneys general and victims should have the right to sue the Attorney General of the United States. | Representative Leger Fernandez said, quote, no administration, no Attorney General, and no Department of Justice is above the law.",
  [C("dv346026c", 17.0, lab=CAP)], {}),
 ("Speaker Johnson responded on November thirteenth. | According to a report published that day, CNN's Manu Raju asked him about the petition. | He said, quote, I have never fought getting the Epstein files out, end quote, and called Massie's push a political stunt.",
  [C("dv346124c", 4.0, lab=WH)], dict(tag=("WASHINGTON, D.C.", "REPORTED NOVEMBER 13, 2026"))),
 ("What happens now is a matter of procedure. | A discharge petition must wait at least seven legislative days. | Then a signer can call it up. | The Speaker has two legislative days to act. | ABC News estimated floor action as early as December second or third. | As of this recording, no vote date has been announced.",
  [G("timeline", kicker="WHAT HAPPENS NEXT, ACCORDING TO ABC NEWS", title="The discharge petition process", events=[
      dict(y="NOV 11", t="218th signature"), dict(y="7 DAYS", t="Legislative days wait"), dict(y="CALL UP", t="A signer moves"),
      dict(y="2 DAYS", t="Speaker must act"), dict(y="DEC 2–3?", t="Possible floor vote")], source="SOURCE: ABC NEWS (NOV. 11, 2026) · ESTIMATE, NOT A SCHEDULED DATE")], dict(slow=True)),
 ("And then comes the Senate. | Forbes reported it remains to be seen whether the bill could get the sixty Senate votes needed. | Axios reported that Senate Republican leaders could decline to take it up before January. | The Senate has not voted on the second bill.",
  [C("dv346119c", 33.0, lab=CAP2)], {}),
 ("So here is where the record stands. | One law, passed four hundred twenty-seven to one. | A Justice Department that says it has met its legal obligations. | Some lawmakers, in both parties, who say more should be released. | A committee report, a change in the department's leadership, and a second bill waiting for a vote.",
  [G("timeline", kicker="THE FIGHT, BY THE RECORD", title="July 2025 – Nov. 2026", events=[
      dict(y="JUL 2025", t="DOJ memo: no client list"), dict(y="NOV 18", t="House votes 427–1"), dict(y="DEC 19", t="Deadline"),
      dict(y="JAN 30", t="3 million pages"), dict(y="FEB 14", t="~280 names list"), dict(y="APR", t="Bondi out"), dict(y="NOV 10", t="Oversight report"), dict(y="NOV 11", t="Petition: 218")], source="SOURCES: NPR · PBS · FORBES · AXIOS · ROLL CALL · NBC · ABC · AP · HOUSE OVERSIGHT")], dict(slow=True)),
 ("Here is our question for you. | The Justice Department says it has met its legal obligations. | Some lawmakers, in both parties, say more should be released. | Which reading do you think the records support? | Tell us in the comments, keep it to the records, and please do not name victims or private individuals.",
  [C("dv346026c", 22.0, lab=CAP)], {}),
 ("That is the series. | Four episodes, built only on official records and the reporting about them. | Next, we go back to the Cold War files.",
  [G("end", n="021", next="Back to the Cold War files")], dict(gap=2.5)),
]

PRON = [("Comer", "Comer"), ("Massie", "Massey"), ("Khanna", "Kahna"), ("Ghislaine", "Ghee-lane"), ("Maxwell", "Maxwell"), ("Bondi", "Bondy"), ("Blanche", "Blanch"),
        ("Schumer", "Shoomer"), ("Fitzpatrick", "Fitz-patrick"), ("Grijalva", "Gree-halva"), ("Garamendi", "Gair-uh-mendy"), ("Leger Fernandez", "Luh-zhay Fernandez"),
        ("Thune", "Thoon"), ("Durbin", "Dur-bin"), ("Boebert", "Bo-bert"), ("Higgins", "Higgins"), ("Kaine", "Kane"), ("Raskin", "Raskin"), ("Jordan", "Jordan"),
        ("Garcia", "Garcia"), ("Mace", "Mace"), ("Norman", "Norman"), ("Booker", "Booker"), ("N P R", "N P R"), ("A P", "A P"), ("C N N", "C N N"), ("N B C", "N B C"),
        ("F B I", "F B I"), ("U S", "U S"), ("Roll Call", "Roll Call"), ("Axios", "Axe-ee-ohs")]

DISPLAY = [
 ("U S", "U.S."), ("N P R", "NPR"), ("A P", "AP"), ("C N N", "CNN"), ("N B C", "NBC"), ("F B I", "FBI"),
 ("twenty twenty-five", "2025"), ("twenty twenty-six", "2026"), ("twenty twenty", "2020"), ("two thousand seven", "2007"),
 ("four hundred twenty-seven", "427"), ("one nineteen, thirty-eight", "119-38"), ("two hundred eighteenth", "218th"), ("two hundred eighteen", "218"),
 ("two hundred fifty years", "250 years"), ("two hundred eighty", "280"), ("one hundred eighty thousand", "180,000"), ("more than three million", "more than 3 million"),
 ("three million", "3 million"), ("six million", "6 million"), ("five hundred", "500"), ("two and a half million", "2.5 million"), ("two thousand videos", "2,000 videos"),
 ("ten thousand", "10,000"), ("eleven subpoenas", "11 subpoenas"), ("nineteen interviews", "19 interviews"), ("fifteen-month", "15-month"), ("eighteen months", "18 months"),
 ("sixty votes", "60 votes"), ("seven legislative days", "7 legislative days"), ("two legislative days", "2 legislative days"),
 ("thirty days", "30 days"), ("two-thirds", "two-thirds"), ("two-page", "two-page"),
 (" | ", " "), ("|", ""),
]

META = dict(
    n="021", title="Congress Voted 427 to 1 for the Epstein Files. Then What?",
    imgs={},
    credit="Sources: PBS NewsHour, Axios, Forbes, Local 10, NBC News, NPR, AP, Roll Call, CBS News, ABC News, House Oversight Committee (press release, Nov. 10, 2026), Rep. Massie's office.\\NB-roll: DoD and State Department footage via DVIDS (public domain); it does not show the events described. Graphics marked RECREATED are our own summaries of public reporting. No photographs of any person are used.",
    shorts=[
        dict(id="s1", lines=[1, 3], tpl="yellow", hook="427 TO 1<br>[THEN WHAT?]", hs=200),
        dict(id="s2", lines=[38, 40], tpl="red", hook="3 MILLION<br>[PAGES]", hs=200),
        dict(id="s3", lines=[43, 44], tpl="blue", hook="THE 280-NAME<br>[DOJ LETTER]", hs=150),
        dict(id="s4", lines=[62, 64], tpl="white", hook="218<br>[SIGNATURES]", hs=220),
    ],
    yshorts=[
        dict(id="y1", lines=[22, 23], tpl="yellow", hook="427 TO 1<br>[ONE NO VOTE]", hs=170),
        dict(id="y2", lines=[54, 55], tpl="red", hook="15 MONTHS<br>[THE REPORT]", hs=150),
        dict(id="y3", lines=[34, 35], tpl="white", hook="CONTEMPT<br>[PROPOSED]", hs=160),
    ],
)


# ---- shot coverage for long lines (more than ~9 s of narration): extra shots from different clips/windows ----
_POOL = [("dv346119c", [0.0, 14.0, 26.0, 38.0], CAP2), ("dv346026c", [0.0, 7.0, 12.0, 18.0], CAP), ("dv346120c", [0.0, 12.0, 26.0, 40.0], TRE),
         ("dv1026930c", [0.0, 12.0, 28.0, 44.0], DCA)]
_n = 0
for _i, (_t, _shots, _o) in enumerate(LINES):
    _words = len(_t.replace("|", "").split())
    if _words > 24 and _shots and _shots[0][0] not in ("g:stat", ) and not _shots[0][0].startswith("g:"):
        _have = {_shots[0][0]}
        for _k in range(2 if _words > 45 else 1):
            for _tries in range(len(_POOL)):
                _clip, _starts, _lab = _POOL[_n % len(_POOL)]; _n += 1
                if _clip not in _have:
                    _have.add(_clip); _shots.append(C(_clip, _starts[_n % len(_starts)], lab=_lab)); break
