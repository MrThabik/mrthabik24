#!/usr/bin/env python3
"""Rebuild private/manifest.json after you add, remove or rename images.
Put images in private/<track>/ (tracks: intern, originals, esim, project, resume). They are shown in file-name order."""
import os, json
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "private")
man = {}
for t in ("intern", "originals", "esim", "project", "resume"):
    d = os.path.join(root, t)
    man[t] = ["private/%s/%s" % (t, f) for f in sorted(os.listdir(d)) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))] if os.path.isdir(d) else []
json.dump(man, open(os.path.join(root, "manifest.json"), "w"), indent=1)
print({k: len(v) for k, v in man.items()})

# thumbnails for the certificates page (needs: pip install pillow)
try:
    from PIL import Image
    d = os.path.join(root, "originals"); os.makedirs(os.path.join(d, "t"), exist_ok=True)
    for f in sorted(os.listdir(d)):
        if f.lower().endswith(".jpg"):
            im = Image.open(os.path.join(d, f)).convert("RGB"); im.thumbnail((520, 520)); im.save(os.path.join(d, "t", f), quality=80, optimize=True)
    print("thumbnails updated")
except ImportError:
    print("Pillow not installed: thumbnails not updated (pip install pillow)")
