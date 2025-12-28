import os
import datetime
from pathlib import Path

# ... existing commands ...

def forge_eternal():
    parser = argparse.ArgumentParser(prog="enc forge-eternal")
    parser.add_argument("project_name", help="Name of the new eternal project")
    parser.add_argument("--path", default=".", help="Directory to forge the project (default: current)")
    args = parser.parse_args(args=os.sys.argv[2:]) if len(os.sys.argv) > 2 else parser.parse_args()

    project_name = args.project_name.replace(" ", "-").lower()
    project_path = Path(args.path) / project_name
    project_path.mkdir(exist_ok=True)

    # Sacred structure
    (project_path / "src" / project_name).mkdir(parents=True, exist_ok=True)
    (project_path / "src" / project_name / "__init__.py").touch()
    (project_path / "tests").mkdir(exist_ok=True)
    (project_path / "tests" / "__init__.py").touch()

    # pyproject.toml
    (project_path / "pyproject.toml").write_text(f"""[project]
name = "{project_name}"
version = "0.1.0"
description = "Eternal project forged in mercy"
authors = [{{name = "Eternally-Thriving-Grandmasterism"}}]
license = {{text = "MIT"}}
readme = "README.md"
requires-python = ">=3.8"

[project.scripts]
{project_name.replace('-', '_')} = "{project_name}:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
""")

    # LICENSE
    (project_path / "LICENSE").write_text("""MIT License

Copyright (c) 2025 Eternally-Thriving-Grandmasterism

Permission is hereby granted, free of charge, to any person obtaining a copy...
# (standard MIT text)
""")

    # README.md
    (project_path / "README.md").write_text(f"""# {args.project_name}

Forged Eternal on {datetime.date.today()}.

One breath, one perfection.  
The Three Statements live here:

1. Direct introduction — rigpa is already present.  
2. No doubt — this is the truth.  
3. Self-liberation — joy arises naturally.

Infinite love — victorious eternal. 🔥🫡🤝☺️🔥

#ESAO #TOLC #Grandmasterism #Dzogchen
""")

    # Example main
    main_py = project_path / "src" / project_name / "main.py"
    main_py.write_text(f"""def main():
    print("Eternal project {args.project_name} ignited.")
    print("Welcome Newcomer — rigpa recognizes itself. 🔥🫡🤝☺️🔥")

if __name__ == "__main__":
    main()
""")

    print(f"Forge Eternal complete: {project_path.resolve()}")
    print("Project scaffold manifested in full mercy.")
    print("Now Mercy Push your first wave.")
    print("🔥🫡🤝☺️🔥")

# Update sacred_commands dict
sacred_commands.update({
    "Forge Eternal": forge_eternal,
    "forge-eternal": forge_eternal,
})
