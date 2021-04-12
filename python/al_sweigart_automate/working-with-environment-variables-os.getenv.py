#!/usr/bin/env python

import os

stage = os.getenv("STAGE", default="dev").upper()

output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)
