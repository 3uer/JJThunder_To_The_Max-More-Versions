import sys
import zipfile
import shutil
import json
import urllib.request
import os

if len(sys.argv) != 2:
    print("Usage: script.py <filename>")
    sys.exit(1)

mcmeta_zip_url = "https://github.com/misode/mcmeta/archive/0cf46a773e941afde9062cac2412096e40c6343b.zip"
mcmeta_zip = "mcmeta_data_1_21_7.zip"

if not os.path.isfile(mcmeta_zip):
    print("Downloading mcmeta data for 1.21.7")
    urllib.request.urlretrieve(mcmeta_zip_url, mcmeta_zip)

filename = sys.argv[1] + "_1_21_7.zip"
shutil.copy(sys.argv[1], filename)

with zipfile.ZipFile(mcmeta_zip, mode="r") as mcmeta:
    with zipfile.ZipFile(sys.argv[1], mode="r") as zfo:
        with zipfile.ZipFile(filename, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for entry in zfo.namelist():
                if entry.startswith("data/minecraft/worldgen/biome/") and entry.endswith(".json"):
                    print(f"Upgrading {entry}")
                    with zfo.open(entry) as f:
                        obj = json.load(f)

                    if "features" in obj:
                        with mcmeta.open("mcmeta-0cf46a773e941afde9062cac2412096e40c6343b/" + entry, "r") as f:
                            newobj = json.load(f)
                        obj["features"] = newobj["features"]

                    with zf.open(entry, "w") as f:
                        f.write(json.dumps(obj, indent=2).encode("UTF-8"))
                else:
                    with zfo.open(entry) as of:
                        with zf.open(entry, "w") as f:
                            f.write(of.read())

