#!/usr/bin/env bash
# https://www.youtube.com/watch?v=1mt2-LbKuvY&list=WL&index=25&t=5s
# Shell Ninja: Mastering the Art of Shell Scripting | Roland Huß

# Fail on a single failed command in a pipeline
set -o pipefail

# Fail on error and undefined variables
set -eu

# I was going to recreate https://github.com/ro14nd-talks/shell-ninja.git
# by listening to the talk
# It turned to be somewhat wasteful, because speakter does not use getops,
# which would make life a lot easier.
# It is also very fast and a little hard to comprehend

# The main reason why I listened to this talk was get to know bats
# Bash Automated Testing System
