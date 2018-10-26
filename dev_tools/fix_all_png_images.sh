#!/bin/bash

find . -type f -iname '*.png' ! -path "./virtualenv/*" ! -path "./virtualenv3/*" -exec pngcrush -ow -rem allb -reduce {} \;