import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent / "src"))

from finance_tracker.cli import main

if __name__ == "__main__":
    main()



