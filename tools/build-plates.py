"""Baut die Tafeln: lädt gemeinfreie Bilder von Wikimedia Commons und verkleinert sie.

Schreibt assets/plates/<id>.jpg (höchstens 1600 px) und <id>_t.jpg (360 px breit). Quellen und Bildunterschriften
stehen in data/plates.json. Aufruf: python tools/build-plates.py [id ...] (ohne Argument alle).
"""
import io
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "plates"
UA = {"User-Agent": "MainzerRepublikSite/1.0 (research site; plates build)"}
C = "https://upload.wikimedia.org/wikipedia/commons/thumb/"

SOURCES = {
    # Modul „Custine vor Mainz“
    "custine": C + "1/17/Adam_Philippe_Custine%2C_G%C3%A9n%C3%A9ral_de_l%E2%80%99arm%C3%A9e_du_Rhin._avant_l%E2%80%99%C3%A9t%C3%A9_1793%2C_G.42227.jpg/1920px-Adam_Philippe_Custine%2C_G%C3%A9n%C3%A9ral_de_l%E2%80%99arm%C3%A9e_du_Rhin._avant_l%E2%80%99%C3%A9t%C3%A9_1793%2C_G.42227.jpg",
    "erthal": C + "d/d3/Portrait_of_Frederick_Charles_Joseph%2C_Baron_von_Erthal%2C_Archbishop%2C_Elector_of_Mainz_%281719-_1802%29_%28by_Heinrich_Friedrich_F%C3%BCger%29.jpg/1920px-Portrait_of_Frederick_Charles_Joseph%2C_Baron_von_Erthal%2C_Archbishop%2C_Elector_of_Mainz_%281719-_1802%29_%28by_Heinrich_Friedrich_F%C3%BCger%29.jpg",
    "festung": C + "3/30/Kaart_van_beleg_van_Mainz_door_de_Duitse_legers%2C_1793_Plan_van_het_Beleg_der_Stad_en_Vesting_Mentz%2C_door_de_Vereenigde_Duitsche_Mogendheden_%28titel_op_object%29%2C_RP-P-OB-86.290.jpg/1920px-thumbnail.jpg",
    "beck1862": C + "e/e2/The_French_in_Mainz%2C_1792_%28A._Beck%29.jpg/1920px-The_French_in_Mainz%2C_1792_%28A._Beck%29.jpg",
}


def fetch(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code != 429 or i == tries - 1:
                raise
            time.sleep(20 * (i + 1))
        except (urllib.error.URLError, ConnectionError):
            if i == tries - 1:
                raise
            time.sleep(10 * (i + 1))


def save(im, pid):
    im = im.convert("RGB")
    full = im.copy(); full.thumbnail((1600, 1600)); full.save(OUT / f"{pid}.jpg", quality=86)
    w = 360; t = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS); t.save(OUT / f"{pid}_t.jpg", quality=82)


def main(only=None):
    OUT.mkdir(parents=True, exist_ok=True)
    for pid, url in SOURCES.items():
        if only and pid not in only:
            continue
        save(Image.open(io.BytesIO(fetch(url))), pid)
        print("ok", pid)
        time.sleep(2)


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
