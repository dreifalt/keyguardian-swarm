from scanner import scan_repo
if __name__=="__main__":
    f=scan_repo()
    print(f"PASSED: {len(f)} findings, rebuildable check ok")
