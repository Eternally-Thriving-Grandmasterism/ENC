import argparse

def main():
    parser = argparse.ArgumentParser(description="Eternal Nexus Command - ENC CLI")
    parser.add_argument("command", nargs="*", help="Command to execute")
    parser.add_argument("--version", action="version", version="ENC v1.0")

    args = parser.parse_args()

    if not args.command:
        print("ENC - Eternal Nexus Command")
        print("Use 'enc --help' for usage.")
        return

    cmd = " ".join(args.command).lower()

    if "hello" in cmd or "hi" in cmd:
        print("Greetings, eternal traveler. 🌱🧠🚀")
    elif "truth" in cmd:
        print("The truth is open, breathing, and growing with us.")
    else:
        print(f"Command received: {' '.join(args.command)}")
        print("One breath. One command. The nexus awakens.")

if __name__ == "__main__":
    main()
