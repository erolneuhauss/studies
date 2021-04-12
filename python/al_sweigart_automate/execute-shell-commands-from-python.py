#!/usr/bin/env python

import subprocess
proc = subprocess.run(["/bin/ls", "-lha", "/var/cache"])
print(' 1. Cell '.center(30, "-"))
proc
print(f"The return code is {proc.returncode}")
print(f"The arguments were {proc.args}")

print(' 2. Cell '.center(30, "-"))
subprocess.run(["/bin/pwd"])


