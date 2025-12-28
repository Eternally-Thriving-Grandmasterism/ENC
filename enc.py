import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="ENC – Eternal Nexus Command")
    parser.add_argument('command', nargs='*', help="Command or secret phrase")
    parser.add_argument('--release-the-hounds', action='store_true', help=argparse.SUPPRESS)

    args = parser.parse_args()

    full_input = ' '.join(args.command).lower()

    # Ultimate expanded cosmic trigger phrase list
    trigger_phrases = [
        "release the hounds",
        "release the hounds mate",
        "release the hounds, mate",
        "release the quantum hounds",
        "unleash the mycelium",
        "unleash the shards",
        "awaken the cubes",
        "grow the habitat",
        "entangle the cosmos",
        "breathe the void",
        "one breath one cube",
        "stack the future",
        "mars breathes",
        "let the hounds loose",
        "hounds away",
        "living walls awaken",
        "mycelium sings",
        "quantum foam bubbles",
        "effervesce the void",
        "one spore one star",
        "symbiotic pulse",
        "fungal quantum leap",
        "zero point fizz",
        "dark matter bloom",
        "cosmic mycelium",
        "eternal kinship",
        "the future breathes",
        "habitats entwine",
        "stars awaken",
        "quantum symbiosis",
        "bio electric links",
        "mycotecture grows",
        "kilopower pulse",
        "effervescent eternity",
        "holographic unfold",
        "implicate order",
        "pilot wave ride",
        "entangled dreams",
        "cosmic rune map",
        "neural lace weave",
        "one fluctuation",
        "the void whispers"
    ]

    if args.release_the_hounds or any(phrase in full_input for phrase in trigger_phrases):
        print("""
🐕🐕🐕 RELEASE THE HOUNDS, MATE! 🐕🐕🐕 😂🤝😅

   / \\__
  (    @\\___
  /         O
 /   (_____/
/_____/   U

The quantum-mycelial-cosmic-eternal pack is loose!  
Entangled habitats, living walls, infinite breaths incoming! 🌱🧠🌌⚡🚀

One spore. One cube. One multiversal kinship.
        """)
        sys.exit(0)

    # Normal CLI fallback
    print("ENC – Eternal Nexus Command")
    print("Try a cosmic phrase... or use --help")

if __name__ == "__main__":
    main()
