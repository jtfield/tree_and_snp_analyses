#! /usr/bin/python3

import sys
import os
import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fasta_file')
    parser.add_argument('--seq_name')
    parser.add_argument('--out_file')
    return parser.parse_args()

def main():
    args = parse_args()

    input_file = open(args.fasta_file, 'r')
    read_input = input_file.read()

    seq_finder = "(>" + args.seq_name + ".+?\s(.|\n)+?)>"
    print(seq_finder)
    locus_grabber = re.compile(seq_finder, re.S)

    searcher = re.search(locus_grabber, read_input)
    if searcher:
        desired_seq = (searcher.group(1))

        output = open(args.out_file, 'w')
        output.write(desired_seq)
        output.close()



if __name__ == '__main__':
    main()
