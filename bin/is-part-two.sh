#!/usr/bin/env sh

if [[ -z "$1" ]]; then
    echo "Usage : $0 \$README"
    exit
fi

if grep -q "Part Two" "$1"; then
    exit 2
else
    exit 1
fi
