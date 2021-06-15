#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 08:32:35 2021

@author: zdx
"""


def main(input_file):
    with open(input_file, 'r') as f:
        data = f.read().splitlines()
        data = ' '.join(data)

    if '  ' in data:
        data = data.replace('  ', ' ')
    if '.' in data:
        data = data.replace('. ', '.\n\n')
    if '?' in data:
        data = data.replace('? ', '?\n\n')
    if '!' in data:
        data = data.replace('! ', '!\n\n')
        
    with open(input_file, 'w') as f:
        f.write(data)

if __name__ == "__main__":
    from argparse import ArgumentParser
    ap = ArgumentParser()
    ap.add_argument('-i', '--input_file', required=True)
    args = ap.parse_args()
    main(args.input_file)