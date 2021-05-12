"""This module provides the RP tree CLI."""
# cli.py

import argparse
import pathlib
import sys

from . import __version__
from .rptree import DirectoryTree


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("Thse specified root directory doesn't exist")
        sys.exit()
    tree = DirectoryTree(
        root_dir,
        dir_only=args.dir_only,
        output_file=args.output_file
    )
    tree.generate()

def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="RP tree, a directory tree generator",
        epilog="Thnks for using RP tree"
    )
    parser.version = f"RP tree v{__version__}"
    parser.add_argument("-v", "--version",  action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting root_dir"
    )
    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="Generate a directory-only tree"
    )
    parser.add_argument(
        "-o",
        "--output-file",
        metavar="OUTPUT_FILE",
        nargs="?",
        default=sys.stdout,
        help="Generate a full directory tree and save it to file"
    )
    return parser.parse_args()
