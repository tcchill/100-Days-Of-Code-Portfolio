# Day 95 – Space Invader Shooting Game 🚀

A classic Space Invaders-style game built with Python's Turtle graphics module, featuring custom GIF sprites, alien
attacks, and win/lose conditions.

## Features

- Move player left/right to dodge incoming lasers
- Shoot bullets to destroy alien fleet
- Aliens move in formation and descend each time they hit the boundary
- Aliens randomly fire lasers at the player
- Win by destroying all aliens before they reach you
- Lose if an alien laser hits you or aliens reach your position
- Replay and quit controls

## Tech Stack

- Python 3
- `turtle` — graphics and game rendering
- OOP design — `Player`, `Alien`, `AlienFleet`, `PlayerBullet`, `Laser`, `GameManager`

## How to Run

**1. Install dependencies**

```bash
pip install -r requirements.txt
```

**2. Run the game**

```bash
python main.py
```

## Controls

| Key | Action |
|---|---|
| `←` `→` | Move left / right |
| `Space` | Shoot |
| `R` | Replay |
| `Q` | Quit |

## What I Learned

- Structuring a game with multiple OOP classes across separate files
- Collision detection using `turtle.distance()`
- Managing game state with a central `GameManager` class
- Implementing cooldown logic for player shooting
- Handling keyboard events with `screen.onkey()` and `screen.listen()`