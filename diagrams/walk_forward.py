import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

folds = [
    [(0, 2),   (2,   0.5), (2.5, 2)],
    [(0, 4.5), (4.5, 0.5), (5,   2)],
    [(0, 7),   (7,   0.5), (7.5, 2)],
    [(0, 9.5), (9.5, 0.5), (10,  2)],
]

colors = {"Train": "#9FE1CB", "Embargo": "#F5C4B3", "Test": "#AFA9EC"}
fig, ax = plt.subplots(figsize=(10, 3))

for i, fold in enumerate(folds):
    train, embargo, test = fold
    ax.barh(i, train[1], left=train[0], color=colors["Train"], edgecolor="white")
    ax.barh(i, embargo[1], left=embargo[0], color=colors["Embargo"], edgecolor="white")
    ax.barh(i, test[1], left=test[0], color=colors["Test"], edgecolor="white")

ax.set_yticks(range(len(folds)))
ax.set_yticklabels([f"Fold {i+1}" for i in range(len(folds))])
ax.set_xlabel("Temps")
ax.legend(handles=[mpatches.Patch(color=v, label=k) for k, v in colors.items()])
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "walk_forward.png")