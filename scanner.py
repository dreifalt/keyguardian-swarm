import re, pathlib, json
PATTERNS = {
    "experiential": r"xpl_[a-zA-Z0-9]{20,}",
    "openai": r"sk-[a-zA-Z0-9]{20,}",
    "aws": r"AKIA[0-9A-Z]{16}",
    "github_pat": r"ghp_[a-zA-Z0-9]{36}"
}
def scan_repo(root="."):
    findings=[]
    for p in pathlib.Path(root).rglob("*"):
        if p.is_file() and p.suffix in [".py",".js",".ts",".env"] and ".git" not in str(p):
            try:
                text=p.read_text(errors="ignore")
                for name, pat in PATTERNS.items():
                    for m in re.finditer(pat, text):
                        findings.append({"file": str(p), "type": name})
            except: pass
    return findings

if __name__=="__main__":
    f=scan_repo()
    print(json.dumps(f, indent=2))
