"""
plot_eval.py

Parses TD-MPC eval.log files and plots evaluation return vs steps.

Usage:
    python plot_eval.py
"""

import re
from pathlib import Path
import matplotlib.pyplot as plt

# Adjust paths if needed
RUNS = {
    "Baseline": Path("logs/walker-walk/state/default/1/eval.log"),
    "Short Steps": Path("logs/walker-walk/state/abl_short_steps/0/eval.log"),
    "Horizon=5": Path("logs/walker-walk/state/abl_horizon5/0/eval.log"),
}

def parse_eval_log(path):
    lines = path.read_text(errors="ignore").splitlines()
    points = []

    for line in lines:
        nums = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", line)
        if len(nums) < 2:
            continue

        values = [float(n) for n in nums]

        step = max(values)
        rest = [v for v in values if v != step]

        if not rest:
            continue

        ret = min(rest, key=lambda v: abs(v - 1000))

        if step < 1000:
            continue

        points.append((step, ret))

    return sorted(set(points))

plt.figure()

for name, path in RUNS.items():
    if not path.exists():
        print(f"Missing log: {path}")
        continue

    data = parse_eval_log(path)
    if not data:
        print(f"No data parsed for {name}")
        continue

    steps, returns = zip(*data)
    plt.plot(steps, returns, label=name)

plt.xlabel("Environment Steps")
plt.ylabel("Evaluation Return")
plt.title("TD-MPC Evaluation Curves")
plt.legend()
plt.tight_layout()

out = Path("submission/figures/tdmpc_eval_curves.png")
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=200)

print("Saved figure to:", out.resolve())
