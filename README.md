# TIC-TAC-TOE
Final project
# Developing and Evaluating Multiple Tic-Tac-Toe Agents in a Tournament Environment

This project implements a tournament setting for multiple Tic-Tac-Toe agents. The agents are designed to play against each other in a competitive environment, showcasing different strategies and approaches to the classic game.

## Overview

In this implementation, several Tic-Tac-Toe agents are programmed to compete against each other. Each agent employs a unique algorithm or strategy to make moves and attempt to win the game. The tournament provides a platform to assess the performance of these agents against various opponents.

## Agents

1. **Random Agent**: This agent makes random moves on the Tic-Tac-Toe board, providing a baseline for comparison against more sophisticated strategies.

2. **Minimax Agent**: Utilizes the Minimax algorithm to search through the game tree and select the optimal move, assuming the opponent plays perfectly.

3. **Alpha-Beta Pruning Agent**: Enhances the Minimax algorithm by implementing alpha-beta pruning, allowing for more efficient search and faster decision-making.

4. **Reinforcement Learning Agent (Deep Q-Learning)**: Trained using deep Q-learning, a reinforcement learning technique, to learn optimal strategies through interactions with the environment.



## Tournament Setup

The tournament consists of multiple rounds, with each agent playing against every other agent multiple times to mitigate randomness. The outcome of each game is recorded, and metrics such as win rate, average game length, and computational resources utilized are analyzed to evaluate the performance of each agent.

## Getting Started

To run the tournament:

1. Clone this repository to your local machine.
2. Install the required dependencies specified in the `requirements.txt` file.
3. Execute the main tournament script, specifying the number of rounds and agents to include.
4. Analyze the results to compare the performance of different agents.

## Future Work

- Integration of more advanced agents with novel strategies.
- Fine-tuning agent parameters for improved performance.
- Visualization tools for better understanding of game dynamics and agent behavior.

## Contribution

Contributions to this project are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to open an issue or submit a pull request.
