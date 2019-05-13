#!/usr/bin/env python3

import sys

before = "PATH environment variable does not have"
after = r"\bin"
app_path = (sys.stdin.read().partition(before)[2].split(after)[0] + after).strip()
assert app_path != 'after'
print(f"export PATH={app_path}:$PATH")
#with open('temp.bash', 'w') as out_file:
#    out_file.write(f"#!/usr/bin/env bash\nexport PATH={app_path}:$PATH")
