import json
import os

import matplotlib.pyplot as plt
import numpy as np

color_file = "color_ggsci.json"
preview_dir = "previews"
batch_size = 200

os.makedirs(os.path.join(preview_dir, color_file.split(".")[0]), exist_ok=True)
with open(color_file, "r") as f:
    color_palettes = json.load(f)


def generate_all_bar_charts():
    """Generate bar charts for all palettes in batches of 100, each in a separate PNG using grid layout"""

    palette_items = list(color_palettes.items())
    for batch_idx in range(0, len(palette_items), batch_size):
        batch_palettes = dict(palette_items[batch_idx : batch_idx + batch_size])
        num_palettes = len(batch_palettes)
        cols = 5
        rows = (num_palettes + cols - 1) // cols

        fig, axes = plt.subplots(rows, cols, figsize=(15, 3 * rows))
        axes = axes.flatten() if num_palettes > 1 else [axes]

        for idx, (palette_key, colors) in enumerate(batch_palettes.items()):
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

        fig.suptitle(
            f"Bar Charts - Palettes Batch {batch_idx // batch_size + 1}", fontsize=16, fontweight="bold", y=0.995
        )
        plt.tight_layout()
        plt.savefig(
            os.path.join(preview_dir, color_file.split(".")[0], f"bar_{batch_idx // batch_size + 1}.png"),
            dpi=150,
            bbox_inches="tight",
        )
        plt.close()


def generate_all_line_charts():
    """Generate line charts for all palettes in batches of 100, each in a separate PNG using grid layout"""
    batch_size = 100
    palette_items = list(color_palettes.items())
    for batch_idx in range(0, len(palette_items), batch_size):
        batch_palettes = dict(palette_items[batch_idx : batch_idx + batch_size])
        num_palettes = len(batch_palettes)
        cols = 5
        rows = (num_palettes + cols - 1) // cols

        fig, axes = plt.subplots(rows, cols, figsize=(15, 3 * rows))
        axes = axes.flatten() if num_palettes > 1 else [axes]

        for idx, (palette_key, colors) in enumerate(batch_palettes.items()):
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

        fig.suptitle(
            f"Line Charts - Palettes Batch {batch_idx // batch_size + 1}", fontsize=16, fontweight="bold", y=0.995
        )
        plt.tight_layout()
        plt.savefig(
            os.path.join(preview_dir, color_file.split(".")[0], f"line_{batch_idx // batch_size + 1}.png"),
            dpi=150,
            bbox_inches="tight",
        )
        plt.close()


def generate_all_pie_charts():
    """Generate pie charts for all palettes in batches of 100, each in a separate PNG"""
    batch_size = 100
    palette_items = list(color_palettes.items())
    for batch_idx in range(0, len(palette_items), batch_size):
        batch_palettes = dict(palette_items[batch_idx : batch_idx + batch_size])
        num_palettes = len(batch_palettes)
        cols = 5
        rows = (num_palettes + cols - 1) // cols

        fig, axes = plt.subplots(rows, cols, figsize=(15, 4 * rows))
        axes = axes.flatten() if num_palettes > 1 else [axes]

        for idx, (palette_key, colors) in enumerate(batch_palettes.items()):
            ax = axes[idx]
            sizes = np.random.randint(10, 30, len(colors))

            wedges, texts, autotexts = ax.pie(
                sizes, colors=colors, autopct="%1.0f%%", startangle=90, textprops={"fontsize": 6}
            )
            ax.set_title(f"Palette: {palette_key}", fontsize=9, fontweight="bold")

        # Hide extra subplots
        for idx in range(num_palettes, len(axes)):
            axes[idx].axis("off")

        fig.suptitle(f"Pie Charts - Palettes Batch {batch_idx // batch_size + 1}", fontsize=16, fontweight="bold")
        plt.tight_layout()
        plt.savefig(
            os.path.join(preview_dir, color_file.split(".")[0], f"pie_{batch_idx // batch_size + 1}.png"),
            dpi=150,
            bbox_inches="tight",
        )
        plt.close()


def generate_all_previews():
    """Generate preview images for all color palettes"""
    print("Generating bar charts for all palettes...")
    generate_all_bar_charts()

    print("Generating line charts for all palettes...")
    generate_all_line_charts()

    print("Generating pie charts for all palettes...")
    generate_all_pie_charts()

    num_batches = (len(color_palettes) + 99) // 100  # Ceiling division
    print(f"\nAll previews generated successfully in 'previews/' directory!")
    print(f"Total palettes: {len(color_palettes)}")
    print(f"Total images: {3 * num_batches} (batched PNGs for bar, line, and pie charts)")


if __name__ == "__main__":
    generate_all_previews()
