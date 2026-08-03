#!/bin/bash

pkill mpvpaper

sleep 0.3

mpvpaper \
-o "no-audio --loop-file=inf" \
"*" \
"$1" &
