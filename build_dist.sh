#!/bin/zsh
VERSION=1.0.2
test -e dist || mkdir dist
tar czvf dist/AutomationForAccordance-${VERSION}.tar.gz --exclude ".*" Services
