#!/usr/bin/env bats

load /usr/lib/node_modules/bats-support/load.bash
load /usr/lib/node_modules/bats-assert/load.bash

@test "simple math" {
# Arrange
#
# Act
  result="$(echo '2 + 2' | bc)"
#
# Assert
#  [[ "$result" -eq 4 ]]
assert_equal "${result}" 4
}
