# Sharingan Animation in Terminal

> A cinematic anime-inspired Sharingan evolution rendered entirely inside the terminal with Python and ANSI true-color graphics.

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Terminal](https://img.shields.io/badge/Terminal-ANSI%20TrueColor-111111?style=for-the-badge&logo=gnubash&logoColor=white)](https://en.wikipedia.org/wiki/ANSI_escape_code)
[![Dependencies](https://img.shields.io/badge/Dependencies-None-2ea44f?style=for-the-badge)](#requirements)

## Overview

**Sharingan Animation in Terminal** is a procedural terminal-art project inspired by the visual evolution of the Uchiha clan's dōjutsu from *Naruto*.

Instead of playing a pre-rendered video or relying on external image assets, the program generates the eye artwork mathematically and redraws it in real time using ANSI terminal escape sequences.

The animation is designed around a simple progression:

```text
Sharingan
   ↓
Sasuke Mangekyō
   ↓
Itachi Mangekyō
   ↓
Shisui Mangekyō
   ↓
Madara Mangekyō
   ↓
Izuna Mangekyō
   ↓
Obito Mangekyō
   ↓
Kakashi Mangekyō
   ↓
Shin Mangekyō
   ↓
Indra Mangekyō
   ↓
Sarada Mangekyō
   ↓
Madara Eternal Mangekyō
   ↓
Sasuke Eternal Mangekyō
   ↓
Rinnegan
   ↓
Sasuke Rinnegan
   ↓
Loop
```

Each stage lasts **exactly 1 second** and performs **one complete 360° rotation** before transitioning to the next stage.

## Features

- **60 FPS terminal animation** for smooth motion.
- **1-second evolution stages** with one full rotation per stage.
- **ANSI 24-bit true color** for red, black, purple, and shaded iris elements.
- **Procedural geometry** for tomoe, curved forms, rings, and ocular patterns.
- **2× internal vertical framebuffer** with half-block (`▀` / `▄`) output for higher visual resolution.
- **Automatic terminal sizing** so the eye scales to the available terminal window.
- **No external Python packages** are required.
- **Clean Ctrl+C shutdown** that restores the terminal cursor and screen.

## Current Evolution Stages

| # | Stage | Theme |
|---:|---|---|
| 1 | Sharingan | Three tomoe |
| 2 | Sasuke Mangekyō | Sasuke-inspired Mangekyō geometry |
| 3 | Itachi Mangekyō | Itachi-inspired Mangekyō geometry |
| 4 | Shisui Mangekyō | Shisui-inspired Mangekyō geometry |
| 5 | Madara Mangekyō | Madara-inspired geometry |
| 6 | Izuna Mangekyō | Izuna-inspired geometry |
| 7 | Obito Mangekyō | Obito-inspired spiral geometry |
| 8 | Kakashi Mangekyō | Uses the Kamui/Mangekyō geometry |
| 9 | Shin Mangekyō | Shin-inspired radial geometry |
| 10 | Indra Mangekyō | Indra-inspired radial geometry |
| 11 | Sarada Mangekyō | Sarada-inspired radial geometry |
| 12 | Madara Eternal Mangekyō | Composite Eternal Mangekyō treatment |
| 13 | Sasuke Eternal Mangekyō | Composite Eternal Mangekyō treatment |
| 14 | Rinnegan | Concentric ring pattern |
| 15 | Sasuke Rinnegan | Rinnegan + tomoe treatment |

> **Note:** The program is an artistic terminal rendering project. The individual Mangekyō patterns are procedural interpretations inspired by the source material, not frame-perfect reproductions of official anime artwork.

## How It Works

The renderer uses a small mathematical drawing system rather than storing hundreds of animation frames.

```text
Mathematical eye geometry
        ↓
Internal framebuffer
        ↓
ANSI 24-bit colour
        ↓
Half-block terminal renderer
        ↓
Live animation
```

### Procedural rendering

The eye is generated from primitives such as:

- circles and ellipses
- line-segment distance fields
- Bézier-like curve sampling
- radial rotation transforms
- concentric rings

The three tomoe in the base Sharingan are positioned with trigonometric rotation, so their movement is continuous rather than frame-by-frame.

### High-resolution terminal output

The program renders at twice the terminal's vertical character resolution internally. Two adjacent pixels are then represented using Unicode half-block characters:

```text
▀  top pixel
▄  bottom pixel
```

This gives the terminal artwork more vertical detail than rendering a single character per pixel.

## Requirements

- Python **3.9 or newer**
- A terminal with ANSI escape-code support
- True-color support is recommended for the intended visual result

No third-party Python libraries are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/bhuvan0x/Sharingan-Animation-in-Terminal.git
cd Sharingan-Animation-in-Terminal
```

## Run

```bash
python3 sharingan_evolution.py
```

On systems where `python` points to Python 3:

```bash
python sharingan_evolution.py
```

Press **Ctrl+C** to stop the animation safely.

## Performance Notes

The renderer intentionally favors visual quality and portability over minimal CPU usage. Every frame recalculates the procedural geometry and rebuilds the terminal image.

For the smoothest experience:

- use a reasonably sized terminal window;
- use a modern terminal with 24-bit color support;
- avoid extremely small terminal dimensions;
- keep the terminal font at a size where block characters remain visually clear.

## Customization

The main animation parameters are near the top of `sharingan_evolution.py`.

```python
FPS = 60
STAGE_DURATION = 1.0
```

### Change frame rate

```python
FPS = 30
```

### Change evolution timing

```python
STAGE_DURATION = 2.0
```

The current default is intentionally **1.0 second per stage**, meaning each eye completes one full rotation before evolving.

### Add a new eye pattern

Add a new pattern function:

```python
def my_new_eye(x, y, size, angle):
    # Return True where the pattern should be black.
    return False
```

Then register it in `STAGES`:

```python
STAGES.append(
    ("MY NEW EYE", "red", my_new_eye)
)
```

## Project Structure

```text
Sharingan-Animation-in-Terminal/
├── sharingan_evolution.py
└── README.md
```

## Inspiration

This project is inspired by the Sharingan and related dōjutsu from **Naruto** and by the idea of turning anime visual effects into procedural terminal art.

It is intended as a programming/graphics experiment and fan-made terminal artwork.

## Roadmap

Planned improvements include:

- cleaner vector definitions for each Mangekyō design;
- improved transition effects between stages;
- more accurate canonical eye geometry;
- optional color themes;
- configurable stage order and speed;
- additional dōjutsu animations;
- optional audio synchronization for supported terminals/environments.

## Contributing

Contributions are welcome.

A good contribution should keep the renderer self-contained, avoid unnecessary dependencies, and preserve smooth animation on ordinary terminals.

## License

This repository is a fan-made programming/art project. **Naruto**, the Sharingan, Mangekyō Sharingan, Rinnegan, characters, and related fictional concepts belong to their respective rights holders.

The original code in this repository is provided for personal, educational, and experimental use. Please respect the rights of the original creators and do not present the anime artwork or characters as original intellectual property.

## Author

Created by **Bhuvan Jatav** (`@bhuvan0x`).

---

<p align="center">
  <b>From three tomoe to the Rinnegan — rendered frame by frame in your terminal.</b>
</p>
