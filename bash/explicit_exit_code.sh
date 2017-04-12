#!/bin/bash

echo "Tick ..."

# arbitrary non-zero exit code
exit 5

echo "Tack ..." # not executed due to previous exit code
