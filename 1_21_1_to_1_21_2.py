import sys
import zipfile
import shutil
import json

if len(sys.argv) != 2:
    print("Usage: script.py <filename>")
    sys.exit(1)

filename = sys.argv[1] + "_1_21_2.zip"
shutil.copy(sys.argv[1], filename)

with zipfile.ZipFile(sys.argv[1], mode="r") as zfo:
    with zipfile.ZipFile(filename, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for entry in zfo.namelist():
            if entry.startswith("data/minecraft/worldgen/biome/") and entry.endswith(".json"):
                print(f"Upgrading {entry}")
                with zfo.open(entry) as f:
                    obj = json.load(f)

                if 'carvers' in obj:
                    obj['carvers'] = obj['carvers']['air']

                with zf.open(entry, "w") as f:
                    f.write(json.dumps(obj, indent=2).encode("UTF-8"))
            else:
                with zfo.open(entry) as of:
                    with zf.open(entry, "w") as f:
                        f.write(of.read())

