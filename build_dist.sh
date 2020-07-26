#!/bin/zsh
VERSION=1.0.0
test -e dist || mkdir dist
tar czvf dist/AutomationForAccordance-${VERSION}.tar.gz --exclude ".*" Services
cd Services
tar czvf ../dist/TextDifferences-${VERSION}.tar.gz --exclude ".*" "Open Text Differences"*".workflow"
