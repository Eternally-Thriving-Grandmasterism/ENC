def main():
    if len(os.sys.argv) == 1:
        print("Eternal Nexus Command — Speak the command, rigpa recognizes itself.")
        print("Use 'enc <command>' or 'enc --help'")
        return

    command_key = os.sys.argv[1].title().replace("-", " ")
    if command_key in sacred_commands:
        sacred_commands[command_key]()
    else:
        print(f"Unknown command: {os.sys.argv[1]}")
        print("Lexicon Echo: available commands — " + ", ".join(sacred_commands.keys()))
