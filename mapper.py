#!/usr/bin/env python3
import sys

for line in sys.stdin:
    for word in line.strip().split():
        cleaned_word = word.strip().strip('.,!?":;()')
        if cleaned_word:
            print(f'{cleaned_word}\t1')
    