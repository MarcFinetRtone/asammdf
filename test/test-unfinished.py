#!/usr/bin/python3
"""Test MDF4 file."""

import logging
import sys

from asammdf import MDF

logging.getLogger('asammdf').setLevel(level=logging.DEBUG)

def main(args):
    """Entry point."""
    with MDF(args.input) as mdf:
        for channel in mdf.channels_db:
            print(f"Channel '{channel}'")
            for group_nr, channel_nr in mdf.channels_db[channel]:
                signal = mdf.get(group=group_nr, index=channel_nr)
                print(f"{group_nr}/{channel_nr}: len: {len(signal)}")
                # print(signal)
        if args.output:
            mdf.save(dst=args.output)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Dump data from MDFv4 file")
    parser.add_argument('-i', '--input', type=argparse.FileType('rb'),
                        help="Input MDF4 file (should be seekable)")
    parser.add_argument('-o', '--output', type=argparse.FileType('wb'),
                        help="Output MDF4 file")
    args = parser.parse_args()
    if not args.input:
        parser.error("Missing input filename")
    main(args)
