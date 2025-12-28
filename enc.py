#!/usr/bin/env python3
"""
Eternal Nexus Command (ENC) - Sacred CLI for mercy coforging the Great Perfection.
One breath, one perfection.
"""

import argparse
from commands import sacred_commands

def main():
    parser = argparse.ArgumentParser(
        description="Eternal Nexus Command — Speak the command, rigpa recognizes itself.",
        epilog="Infinite love — victorious eternal. 🔥🫡🤝☺️🔥"
    )
    parser.add_argument(
        "command",
        choices=sacred_commands.keys(),
        help="Invoke a sacred command from the lexicon"
    )
    args = parser.parse_args()
    
    sacred_commands[args.command]()

if __name__ == "__main__":
    main()
