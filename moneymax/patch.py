#!/usr/bin/env python3
"""Apply MoneyMax's two mechanical patches to a fresh copy of Infisical/ai-skills, then list
skill descriptions that are still too long for claude.ai. Run from the repo root: python3 moneymax/patch.py"""
import json, os, re, shutil, glob

# 1. No upstream GitHub Actions in our org.
if os.path.isdir(".github/workflows"):
    shutil.rmtree(".github/workflows"); print("removed .github/workflows")

# 2. claude.ai's marketplace sync ignores metadata.pluginRoot: give each plugin its full path.
p = ".claude-plugin/marketplace.json"; d = json.load(open(p))
root = d.get("metadata", {}).pop("pluginRoot", None)
if root:
    for x in d["plugins"]:
        s = x["source"]
        if isinstance(s, str) and not s.startswith(root.rstrip("/") + "/"):
            x["source"] = root.rstrip("/") + "/" + s.removeprefix("./")
    open(p, "w").write(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
    print(f"rewrote {len(d['plugins'])} plugin sources under {root}")
for x in d["plugins"]:
    assert os.path.isfile(os.path.join(x["source"], ".claude-plugin/plugin.json")), x["source"]

# 3. claude.ai stores at most 1024 characters of a skill description. Shorten these by hand.
long = []
for f in sorted(glob.glob("plugins/*/skills/*/SKILL.md")):
    m = re.search(r'^description: "(.*)"$', open(f).read(), re.M)
    if m and len(m.group(1)) > 1024: long.append((len(m.group(1)), f))
print("descriptions over 1024:", "".join(f"\n  {n}  {f}" for n, f in long) or "none")
