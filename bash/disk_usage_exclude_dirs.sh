/bin/bash

du -h --max-depth=3 -X exclude.list / | sort -h
