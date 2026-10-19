import re, pathlib
def create_env():
    pathlib.Path(".env.example").write_text("EXPERIENTIAL_API_KEY=your_key_here\nOPENAI_API_KEY=your_key_here\n")
    if not pathlib.Path(".env").exists():
        pathlib.Path(".env").write_text("EXPERIENTIAL_API_KEY=placeholder\n")
    print("[+] Fixed")
if __name__=="__main__":
    create_env()
