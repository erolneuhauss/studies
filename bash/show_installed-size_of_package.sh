/bin/bash

dpkg-query -W -f='${Installed-Size} \t${Status} \t${binary:Package}\n' | sort -n
