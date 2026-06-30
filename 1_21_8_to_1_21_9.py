import sys
import zipfile
import shutil
import json

if len(sys.argv) != 2:
    print("Usage: script.py <filename>")
    sys.exit(1)

filename = sys.argv[1] + "_1_21_9.zip"
shutil.copy(sys.argv[1], filename)

with zipfile.ZipFile(sys.argv[1], mode="r") as zfo:
    with zipfile.ZipFile(filename, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for entry in zfo.namelist():
            if entry == "pack.mcmeta":
                print(f"Upgrading {entry}: nuking pack.supported_formats")
                with zfo.open(entry) as f:
                    info = json.load(f)
                if "supported_formats" in info["pack"]:
                    del info["pack"]["supported_formats"]
                with zf.open(entry, "w") as f:
                    f.write(json.dumps(info, indent=2).encode("UTF-8"))
            elif entry.startswith("data/minecraft/worldgen/noise_settings/") and entry.endswith(".json"):
                print(f"Upgrading {entry}")
                with zfo.open(entry) as f:
                    settings = json.load(f)
                if 'noise_router' not in settings:
                    print("noise_router not found")
                    continue
                if 'initial_density_without_jaggedness' not in settings['noise_router']:
                    print("noise_router.initial_density_without_jaggedness not found")
                    continue
                if 'noise' not in settings:
                    print("noise not found")
                    continue

                orig = settings['noise_router']['initial_density_without_jaggedness']
                del settings['noise_router']['initial_density_without_jaggedness']
                settings['noise_router']['preliminary_surface_level'] = {
                    "type": "minecraft:find_top_surface",
                    "cell_height": int(settings['noise']['size_vertical']) * 4,
                    "density": {
                        "type": "minecraft:add",
                        "argument1": -0.390625,
                        "argument2": orig
                    },
                    "lower_bound": int(settings['noise']['min_y']),
                    "upper_bound": float(int(settings['noise']['height']) - int(settings['noise']['min_y']))
                }

                with zf.open(entry, "w") as f:
                    f.write(json.dumps(settings, indent=2).encode("UTF-8"))
            else:
                with zfo.open(entry) as of:
                    with zf.open(entry, "w") as f:
                        data = of.read()
                        if b"minecraft:chain" in data:
                            print(f"Upgrading {entry}: minecraft:chain -> minecraft:iron_chain")
                            data = data.replace(b"minecraft:chain", b"minecraft:iron_chain")
                        f.write(data)

