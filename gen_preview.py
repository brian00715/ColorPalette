import matplotlib.pyplot as plt
import numpy as np
import json
import os

# Create output directory
os.makedirs("previews", exist_ok=True)

# Load color palettes from JSON file
with open("colors.json", "r") as f:
    color_palettes = json.load(f)


def generate_all_bar_charts():
    """Generate bar charts for all palettes in a single PNG using grid layout"""
    num_palettes = len(color_palettes)
    cols = 5
    rows = (num_palettes + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(15, 3 * rows))
    axes = axes.flatten() if num_palettes > 1 else [axes]

    for idx, (palette_key, colors) in enumerate(color_palettes.items()):
        ax = axes[idx]
        x = np.arange(len(colors))
        values = np.random.randint(50, 100, len(colors))

        ax.bar(x, values, color=colors, edgecolor="black", linewidth=0.5)
        ax.set_title(f"Palette: {palette_key}", fontsize=10, fontweight="bold")
        ax.set_ylabel("Value", fontsize=8)
        ax.set_xticks(x)
        ax.set_xticklabels([f"C{i}" for i in range(len(colors))], fontsize=6)

    # Hide extra subplots
    for idx in range(num_palettes, len(axes)):
        axes[idx].axis("off")

    fig.suptitle("Bar Charts - All Palettes", fontsize=16, fontweight="bold", y=0.995)
    plt.tight_layout()
    plt.savefig(f"previews/all_palettes_bar.png", dpi=150, bbox_inches="tight")
    plt.close()


def generate_all_line_charts():
    """Generate line charts for all palettes in a single PNG using grid layout"""
    num_palettes = len(color_palettes)
    cols = 5
    rows = (num_palettes + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(15, 3 * rows))
    axes = axes.flatten() if num_palettes > 1 else [axes]

    for idx, (palette_key, colors) in enumerate(color_palettes.items()):
        ax = axes[idx]
        x = np.linspace(0, 10, 100)

        for i, color in enumerate(colors):
            y = np.sin(x + i * 0.5) + i * 0.3
            ax.plot(x, y, color=color, linewidth=1.5, label=f"L{i}")

        ax.set_title(f"Palette: {palette_key}", fontsize=10, fontweight="bold")
        ax.set_ylabel("Value", fontsize=8)
        ax.legend(loc="upper right", ncol=min(len(colors), 4), fontsize=6)
        ax.grid(True, alpha=0.3)

    # Hide extra subplots
    for idx in range(num_palettes, len(axes)):
        axes[idx].axis("off")

    fig.suptitle("Line Charts - All Palettes", fontsize=16, fontweight="bold", y=0.995)
    plt.tight_layout()
    plt.savefig(f"previews/all_palettes_line.png", dpi=150, bbox_inches="tight")
    plt.close()


def generate_all_pie_charts():
    """Generate pie charts for all palettes in a single PNG"""
    num_palettes = len(color_palettes)
    cols = 5
    rows = (num_palettes + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(15, 4 * rows))
    axes = axes.flatten() if num_palettes > 1 else [axes]

    for idx, (palette_key, colors) in enumerate(color_palettes.items()):
        ax = axes[idx]
        sizes = np.random.randint(10, 30, len(colors))

        wedges, texts, autotexts = ax.pie(
            sizes, colors=colors, autopct="%1.0f%%", startangle=90, textprops={"fontsize": 6}
        )
        ax.set_title(f"Palette: {palette_key}", fontsize=9, fontweight="bold")

    # Hide extra subplots
    for idx in range(num_palettes, len(axes)):
        axes[idx].axis("off")

    fig.suptitle("Pie Charts - All Palettes", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.savefig(f"previews/all_palettes_pie.png", dpi=150, bbox_inches="tight")
    plt.close()


def generate_all_previews():
    """Generate preview images for all color palettes"""
    print("Generating bar chart for all palettes...")
    generate_all_bar_charts()

    print("Generating line chart for all palettes...")
    generate_all_line_charts()

    print("Generating pie chart for all palettes...")
    generate_all_pie_charts()

    print(f"\nAll previews generated successfully in 'previews/' directory!")
    print(f"Total palettes: {len(color_palettes)}")
    print(f"Total images: 3 (all_palettes_bar.png, all_palettes_line.png, all_palettes_pie.png)")


if __name__ == "__main__":
    generate_all_previews()
