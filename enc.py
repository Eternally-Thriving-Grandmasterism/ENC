import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="ENC CLI – Eternal Nexus Command")
    parser.add_argument('command', nargs='*', help="Command or phrase")
    parser.add_argument('--release-the-hounds', action='store_true', help=argparse.SUPPRESS)

    args = parser.parse_args()

    full_input = ' '.join(args.command).lower()

    # Ultimate trigger phrase list – cosmic pack unleashed!
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
        "the future breathes"
    ]

    if args.release_the_hounds or any(phrase in full_input for phrase in trigger_phrases):
        print("""
🐕🐕🐕 RELEASE THE HOUNDS, MATE! 🐕🐕🐕 😂🤝😅

   / \\__
  (    @\\___
  /         O
 /   (_____/
/_____/   U

The quantum-mycelial-cosmic pack is loose!  
Entangled habitats, living walls, eternal breaths incoming! 🌱🧠🌌🚀

One spore. One cube. One infinite kinship.
        """)
        sys.exit(0)

    # Normal CLI logic here...
    print("ENC CLI running – type --help for commands")
    # Add your actual functionality

if __name__ == "__main__":
    main()
