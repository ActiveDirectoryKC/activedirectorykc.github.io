"""Redirect stubs for post URLs that existed before posts moved under /posts/.

GitHub Pages cannot send HTTP redirects, so each old URL gets a small page with
a canonical link and a meta refresh. Add a row only for URLs that were already
public. New posts never need an entry.
"""
from pathlib import Path

SITE = "https://www.activedirectorykc.net"

# old path -> new path (both without leading or trailing slash)
LEGACY = {
    "2020/08/24/cannot-bind-argument-to-parameter-exception-because-it-is-null-with-backup-bitlockerkeyprotector":
        "posts/2020/08/24/cannot-bind-argument-to-parameter-exception-because-it-is-null-with-backup-bitlockerkeyprotector",
    "2021/04/22/configuring-the-ad-site-topology-for-non-routed-networks":
        "posts/2021/04/22/configuring-the-ad-site-topology-for-non-routed-networks",
}

STUB = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{site}/{new}/">
<meta http-equiv="refresh" content="0; url=/{new}/">
</head>
<body>
<p>This post moved to <a href="/{new}/">{site}/{new}/</a>.</p>
</body>
</html>
"""


def on_post_build(config):
    out = Path(config["site_dir"])
    for old, new in LEGACY.items():
        if not (out / new / "index.html").is_file():
            raise FileNotFoundError(f"Redirect target missing from build: {new}")
        stub = out / old / "index.html"
        stub.parent.mkdir(parents=True, exist_ok=True)
        stub.write_text(STUB.format(site=SITE, new=new), encoding="utf-8")
