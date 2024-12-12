# TIC-TAC-TOE
Final project
# Developing and Evaluating Multiple Tic-Tac-Toe Agents in a Tournament Environment

This project creates a competitive tournament environment for multiple Tic-Tac-Toe agents. Each agent showcases a unique strategy, allowing for performance evaluation in a classic game setting.

## Overview

The project implements several Tic-Tac-Toe agents that compete against one another using distinct algorithms and strategies. The tournament framework serves as a platform to evaluate their performance against various opponents.

## Agents

1. **Random Agent**: This agent makes random moves on the Tic-Tac-Toe board, providing a baseline for comparison against more sophisticated strategies.

2. **Minimax Agent**: Utilizes the Minimax algorithm to search through the game tree and select the optimal move, assuming the opponent plays perfectly.

3. **Alpha-Beta Pruning Agent**: Enhances the Minimax algorithm by implementing alpha-beta pruning, allowing for more efficient search and faster decision-making.

4. **Reinforcement Learning Agent (Deep Q-Learning)**: Trained using deep Q-learning, a reinforcement learning technique, to learn optimal strategies through interactions with the environment.



## Tournament Setup

- The tournament involves multiple rounds, with each agent playing against every other agent several times to reduce the influence of randomness.
- Game outcomes are recorded, and the following metrics are analyzed:
  1. Win Rate
  2. Average Game Length
  3. Computational Efficiency
- Results are compared to assess agent performance.


## Getting Started

To run the tournament:

1. Clone this repository.
2. Install the dependencies listed in requirements.txt.
3. Run the main tournament script, specifying the number of rounds and agents to include.
4. Review the results to compare agent performance.

## Future Work

- Adding advanced agents with novel strategies.
- Parameter tuning for improved agent performance.
- Creating visualization tools to analyze game dynamics and agent behaviors.

## Contribution

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or submit a pull request.
