"""15. Standard Library Essentials — Handy examples"""

from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict

Path("reports").mkdir(exist_ok=True)
today = datetime.now()
Counter("mississippi").most_common(2)

groups = defaultdict(list)
groups["Python"].append("cheatsheet")
