#!/bin/bash
# rename all files in current directory 
# accomplish by search for java and replace by jdk

for i in *; do
    mv "${i}" "${i/jdk/java}"
done
