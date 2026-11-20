import subprocess, os, re, glob, sys
PDF="/home/claude/src17/dl/23-085.pdf"; OUT="/home/claude/src/img/doc/"
T={int(re.search(r'pg_(\d+)',f).group(1)): open(f).read() for f in glob.glob('/home/claude/src17/dl/pg_*.txt')}
norm=lambda s: re.sub(r"\s+","",s.lower().replace("’","'").replace("“",'"').replace("”",'"'))
def page(ph, minp=1):
    for p in sorted(T):
        if p>=minp and norm(ph) in norm(T[p]): return p
    return None
C=[ # key, start, end, col, minpage
("c_alone","The combination of these and other failures led","following day.","right",1),
("c_arrest","On Saturday, July 6, 2019, Epstein was arrested","general inmate population","",20),
("c_bail","On July 18, 2019, the court ordered","presumption in favor of detention","",20),
("c_rules","BOP policy requires SHU staff to observe","search the entire SHU every week.","right",1),
("c_jul23","According to BOP documents, at approximately 1:27","attempted to hang himself.","",30),
("c_kill","Senior Officer Specialist 4 further reported","tried to kill him.","",30),
("c_unclear","Later that morning, the MCC New York Staff Psychologist","or if someone else did.","",30),
("c_bunkies","Senior Officer Specialist 1 told the OIG that after Epstein came off","his cellmate.","",30),
("c_nointerest","the Post Suicide Watch Report that the reason for removing","would not do that to himself.","",40),
("c_email","MCC New York staff, on July 30, 2019, at 12:30","appropriate cellmate.","",30),
("c_warden","The Warden at the time told","executive leadership.","left",1),
("c_marshals","On August 8, the U.S. Marshals Service sent","assigned another cellmate.","left",1),
("c_credit","The OIG did not credit Noel","a cellmate","",90),
("c_dvr","According to forensic analysis conducted by the FBI after Epstein","unable to record.","",80),
("c_eleven","MCC New York personnel did not learn of this system failure","Epstein's death.","",100),
("c_key","so he requested access from the only other individual","postpone the repair until the following day.","",80),
("c_funding","on September 6, 2018, the Warden submitted","install the camera system.","",80),
("c_2013","Dating back to at least 2013","required camera system upgrades.","",100),
("c_will","The OIG's investigation and review revealed that MCC New York personnel were unaware","2 days before he died.","",50),
("c_redflag","it were true, it would have been useful information","some type of observation.","",50),
("c_unseal","On August 9, 2019, the U.S. Court of Appeals for the Second Circuit ordered","court filings.","",50),
("c_call","BOP records reflect that Epstein placed an unrecorded","telephone call had been made","",60),
("c_mother","established both that Epstein's mother was deceased","","",100),
("c_search","search was documented on August 9","last searched.","right",1),
("c_linens","the OIG determined that there was an excessive","escape paraphernalia.","",100),
("c_shifts","The Material Handler told the OIG that he felt pressured","12 a.m. on August 10.","",50),
("c_22","The Material Handler said he was present at the time of the 10 p.m. count","consecutive hours at","",60),
("c_73","Nonetheless, Noel and the Material Handler completed","73 + 1.","",60),
("c_75","Noel and Thomas both admitted to the OIG","6:30 a.m. on August 10.","",75),
("c_furniture","Additionally, from approximately 1 a.m. to 3 a.m.","sports news.","",60),
("c_doze","Thomas acknowledged that neither he nor Noel","did not know if Noel slept.","",60),
("c_never","Noel said she never","caught herself and never slept.","",60),
("c_breakfast","On August 10, at approximately 6:30 a.m., the two SHU","call for a medical emergency.","right",1),
("c_messed","When he arrived, Noel told him","We messed up.","",70),
("c_pronounced","At approximately 7:10 a.m., Epstein was transported","7:36 a.m.","",8),
("c_victims","to take his own life, resulting in significant","criminal justice process.","right",1),
("c_notfirst","This is not the first time the OIG has found","safe, secure, and in good health.","right",1),
("c_findings","staff's failure to assign Epstein a cellmate","commit suicide.","right",1),
("c_dpa","New York employees, Noel and Thomas, were charged","false documentation.","right",1),
("c_noone","reviewed the video and found that, between","SHU common area.","left",1),
("c_contradict","While the OIG determined MCC New York staff engaged","locked in their assigned cells.","right",1),
("c_sight","Further, the SHU staff and three interviewed","on August 9.","left",1),
("c_me","The Medical Examiner who performed the autopsy told","bruising on his body.","left",1),
]
only=sys.argv[1:]
for k,a,b,col,mp in C:
    if only and k not in only: continue
    p=page(a,mp)
    if not p: print("NOT FOUND",k,a); continue
    if not b:
        # take the sentence's own line only
        b=a
    env=dict(os.environ, NAMES_EXTRA="noel,tova,thomas,giuffre,virginia,roberts")
    if col: env["COL"]=col
    r=subprocess.run(["python3","/home/claude/releasedinfull_media/pipeline/doc_crop.py",PDF,str(p),a,b,OUT+k+".jpg"],capture_output=True,text=True,env=env)
    foot=[l.strip() for l in T[p].strip().splitlines() if l.strip()][-1][-12:]
    print(k,"pdf",p,"footer",foot,"|",(r.stdout or r.stderr).strip()[:400]); print()
