#!/usr/bin/env python3
import sys
from pathlib import Path
print(f"export PATH={Path(sys.executable).parent.as_posix().replace('C:', '/c')}:$PATH")
