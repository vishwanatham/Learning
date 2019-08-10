import re

# '.' meta character means any single character
if re.match(r"gr.y", "greey"):
    print("match found")

# '.' meta character means any single character