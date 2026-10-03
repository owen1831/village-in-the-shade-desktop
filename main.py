"""Village in the Shade Desktop — A local helper for Village in the Shade farm folders, shade-town notes, and autumn albums."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='village_in_the_shade_desktop',
        description='A local helper for Village in the Shade farm folders, shade-town notes, and autumn albums.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Village in the Shade Desktop')
    print('Keep the village on disk before a JP patch.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
