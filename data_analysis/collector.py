import pickle
import argparse
from datetime import datetime
from src.pathfinder import PathFinder
from src.flip import currencies

def gen_filename():
  timestamp = str(datetime.now()).split(".")[0]
  for i in ["-", ":", " "]:
    timestamp = timestamp.replace(i, "_")
  return "{}.pickle".format(timestamp)

def run():

  parser = argparse.ArgumentParser(description="data collection tool for PathFinder class")
  parser.add_argument("--league", default="Flashback Event (BRE001)", help="League specifier, ie. 'Bestiary', 'Hardcore Bestiary' or 'Flashback Event (BRE001)'")
  parser.add_argument("--path", default="data_analysis/raw", help="Location where to save collected data")
  arguments = parser.parse_args()

  p = PathFinder(arguments.league, currencies)
  p.run(3)

  filename = "{}/{}".format(arguments.path, gen_filename())
  with open(filename, "wb") as f:
    pickle.dump(p, f)

if __name__ == "__main__":
  run()
