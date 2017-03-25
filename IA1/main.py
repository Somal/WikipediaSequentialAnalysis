import os

os.system("cat input | python3 mapper.py | sort | python3 reducer.py | sort -nk2 -r > output")
