import json
import yaml
import operator

def main():
  manifest = json.load(open("fontcustom-manifest-template.json", "r"))
  icons = yaml.safe_load(open("icons.yml", "r"))

  for icon in sorted(icons["icons"], key=operator.itemgetter("id")):
    manifest["glyphs"][icon["id"]] ={
        "codepoint": int(icon["unicode"], base=16),
        "source": "svg/{}.svg".format(icon["id"])
        }


  json.dump(manifest, open(".fontcustom-manifest.json","w"), indent=2)


if __name__ == "__main__":
  main()

