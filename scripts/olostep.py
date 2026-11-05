"""Minimal Olostep API helper for NEXUS research.

Reads OLOSTEP_API_KEY from the environment (User scope as fallback on Windows).
The key is never printed or written to disk.

Usage:
  python olostep.py map <url> <out_name>
  python olostep.py scrape <url> <out_name>
  python olostep.py answer "<question>" <out_name>
Outputs are saved to knowledge-base/research-answers/<out_name>.json (and .md for scrapes).
"""
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.olostep.com/v1"
RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "knowledge-base", "research-answers")


def get_key():
    key = os.environ.get("OLOSTEP_API_KEY")
    if not key and os.name == "nt":
        import winreg
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
                key, _ = winreg.QueryValueEx(k, "OLOSTEP_API_KEY")
        except OSError:
            key = None
    if not key:
        sys.exit("OLOSTEP_API_KEY is not set")
    return key


def post(endpoint, payload, timeout=180):
    req = urllib.request.Request(
        f"{API}/{endpoint}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {get_key()}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:500]}")


def save(name, data, markdown=None):
    os.makedirs(RAW_DIR, exist_ok=True)
    with open(os.path.join(RAW_DIR, f"{name}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    if markdown:
        with open(os.path.join(RAW_DIR, f"{name}.md"), "w", encoding="utf-8") as f:
            f.write(markdown)


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    cmd, target, name = sys.argv[1], sys.argv[2], sys.argv[3]
    sys.stdout.reconfigure(encoding="utf-8")

    if cmd == "map":
        data = post("maps", {"url": target})
        save(name, data)
        urls = data.get("urls", [])
        print(f"URLS: {len(urls)}")
        print("\n".join(sorted(urls)))
    elif cmd == "scrape":
        data = post("scrapes", {"url_to_scrape": target, "formats": ["markdown"]})
        md = (data.get("result") or {}).get("markdown_content") or ""
        save(name, data, md)
        print(md[:6000])
    elif cmd == "answer":
        data = post("answers", {"task": target})
        save(name, data)
        result = data.get("result") or {}
        print(json.dumps(result.get("json_content") or result, ensure_ascii=False, indent=2)[:6000])
    else:
        sys.exit(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
