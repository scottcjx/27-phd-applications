import json, sys, os, urllib.request, urllib.parse, time, subprocess
out = sys.argv[1]
REFS = {"Mandar Chitre":"A5067178295","Oliver Armitage":"A5037471411","Dusit Niyato":"A5091266202","Tianyang Ye":"A5054131295","Paul Le Floch":"A5005546087"}
PROFS = {"Fadel Adib":"A5081362240","Seth McCammon":"A5062751548","Yongsung Park":"A5013155255","Jeff Kaeli":"A5025977203",
 "Yogesh Girdhar":"A5072400128","Nare Karapetyan":"A5086445949","Dana Yoerger":"A5026673043","Richard Camilli":"A5018823783",
 "Lee Freitag":"A5073159329","Jim Partan":"A5075223979","Levi Cai":"A5036916741","Federico Tessari":"A5064749168","Oussama Khatib":"A5051336665"}
calls = 0
def works(aid):
    global calls
    fn = os.path.join(out, "works_"+aid+".json")
    if os.path.exists(fn): return json.load(open(fn))
    res, page = [], 1
    while True:
        u = f"https://api.openalex.org/works?filter=author.id:{aid}&per_page=200&page={page}&select=id,title,publication_year,authorships,referenced_works"
        d = json.loads(subprocess.run(["curl","-s","-f",u],capture_output=True,check=True).stdout); calls += 1
        res += d["results"]
        if len(res) >= d["meta"]["count"] or not d["results"]: break
        page += 1; time.sleep(0.2)
    json.dump(res, open(fn, "w")); return res
W = {}
for n,a in {**REFS, **PROFS}.items():
    W[n] = works(a); print(n, len(W[n]), file=sys.stderr)
print("api calls this run:", calls, file=sys.stderr)
def ids(ws): return {w["id"] for w in ws}
def authors(w): return {(x["author"].get("id") or "").split("/")[-1] for x in w["authorships"]}
report = {}
for p,pa in PROFS.items():
    pw = W[p]; pids = ids(pw); report[p] = {}
    for r,ra in REFS.items():
        rw = W[r]; rids = ids(rw)
        co = [w for w in pw if ra in authors(w)]
        pc = [w for w in pw if rids.intersection(w.get("referenced_works") or []) and w not in co]
        rc = [w for w in rw if pids.intersection(w.get("referenced_works") or []) and ra not in [] and pa not in authors(w)]
        if co or pc or rc:
            t = lambda ws: [f'{w["publication_year"]}: {w["title"]}' for w in sorted(ws, key=lambda w: -(w["publication_year"] or 0))[:4]]
            report[p][r] = {"coauthored": len(co), "coauthored_ex": t(co), "prof_cites_ref": len(pc), "prof_cites_ref_ex": t(pc), "ref_cites_prof": len(rc), "ref_cites_prof_ex": t(rc)}
json.dump(report, open(os.path.join(out, "links_report.json"), "w"), indent=1)
for p, d in report.items():
    print("\n##", p)
    if not d: print("   none")
    for r, v in d.items():
        print(f'   {r}: coauthored={v["coauthored"]}  prof_cites_ref={v["prof_cites_ref"]}  ref_cites_prof={v["ref_cites_prof"]}')
        for k in ("coauthored_ex","prof_cites_ref_ex","ref_cites_prof_ex"):
            for e in v[k][:2]: print(f'      [{k[:-3]}] {e}')
