#!/bin/bash
# rename all files in current directory
# accomplished by search for jdk and replace by java

for i in *; do
    mv "${i}" "${i/jdk/java}"
done
