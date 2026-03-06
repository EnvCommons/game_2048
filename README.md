# Game2048

[![OpenReward Environment](https://img.shields.io/badge/%E2%AD%90%20OpenReward-Environment-f7e6cc)](https://openreward.ai/GeneralReasoning/Game2048)

## Description

**Game2048** is an environment for evaluating agents on the classic sliding tile puzzle game. This environment wraps the 2048 implementation from [TextArena](https://github.com/LeonGuertler/TextArena), a framework for text-based game environments.

## Capabilities

- Single-player puzzle solving with strategic planning
- Tile merging mechanics requiring forward-thinking
- Multiple grid sizes and difficulty levels

## Compute Requirements

2048 does not require a sandbox. It has minimal compute requirements.

## License

[MIT](https://github.com/LeonGuertler/TextArena/blob/main/LICENSE).

## Tasks

There are two splits: train (700 tasks) and test (700 tasks). Each split contains 50 tasks across each of 14 variants:

- **2048-v0**: Standard 4x4 grid with 2048 target
- **2048-v0-3x3**: Smaller 3x3 grid
- **2048-v0-5x5**: Larger 5x5 grid
- **2048-v0-6x6**: Larger 6x6 grid
- **2048-v0-8x8**: Larger 8x8 grid
- **2048-v0-10x10**: Largest 10x10 grid
- **2048-v0-mega-easy**: Very low target tile value
- **2048-v0-ultra-easy**: Ultra low target tile value
- **2048-v0-super-easy**: Super low target tile value
- **2048-v0-very-easy**: Very low target tile value
- **2048-v0-easy**: Low target tile value
- **2048-v0-hard**: High target tile value
- **2048-v0-very-hard**: Very high target tile value
- **2048-v0-extreme**: Extremely high target tile value

Each task is seeded for reproducibility.

## Reward Structure

This is a sparse reward environment. Rewards are mapped from TextArena's native range of {-1, 0, 1} to {0.0, 0.5, 1.0} via `(raw + 1) / 2`.

We do not use LLM graders for this environment; reward is determined programmatically.

## Data

Game state is generated procedurally by the TextArena engine using seeded randomness. No external data files are required.

## Tools

Agents are given a single tool:

- `move(direction)`: Slide all tiles in the given direction (up, down, left, right). Matching tiles merge and double.

## Time Horizon

2048 is a multi-turn environment.

## Environment Difficulty

Medium to Hard. The difficulty varies significantly across variants, with larger grids and higher target values requiring more strategic planning and longer solution paths.

## Other Environment Requirements

There are no further environment requirements; 2048 works out of the box without any secrets or API keys.

## Safety

Agents in 2048 interact only with a sliding tile puzzle game and have no access to external systems, the internet, or sensitive data. The environment does not present safety risks.

## Citations

```bibtex
@software{textarena2024,
  author    = {Guertler, Leon and Banting, Wilfried and Pignatelli, Eduardo},
  title     = {TextArena},
  year      = {2024},
  publisher = {GitHub},
  url       = {https://github.com/LeonGuertler/TextArena}
}
```
