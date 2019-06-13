import os
import re

class Dotenv():
  def __init__(self, file=""):
    self.dotenv = ""
    self.set_dotenv(file)

  def setDotenv(self, file):
    if file:
      self.dotenv = file
    else:
      self.dotenv = os.path.dirname(os.path.abspath(__file__)) + "/.env"
    self.load_dotenv(self.dotenv)

  def load(self, file):
    if os.path.exists(file):
      fh = open(file, "r")
      line = fh.readline()
      while line:
        line = line.strip()
        line = re.sub(r"\s*#.*", "", line)
        try:
          (key, val) = line.split("=")
          if val:
            val = re.sub('^"|"$', "", val)
            os.environ[key] = val
          else:
            os.environ[key] = ""
        except:
          line = fh.readline()
          next
        line = fh.readline()