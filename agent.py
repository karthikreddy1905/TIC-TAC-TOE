"""Holds agent base class.

The agent or learner.

"""
import torch


class Agent:
    """Abstract agent class."""

    def __init__(self, model: torch.nn.Module) -> None:
        """Initializes abstract learner class."""
        self.model = model

        self.stats = {"epsilon": None, "loss": None, "reward": None}

    def _normalize_rewards(self, rewards: torch.Tensor, eps: float = 1e-05) -> torch.Tensor:
        """Normalizes rewards.

        Normalizes rewards if there is more than one reward
        and if standard-deviation is non-zeros.

        Returns:
            Normalized rewards.
        """
        if len(rewards) > 1:
            std = torch.std(rewards)
            if std != 0:
                mean = torch.mean(rewards)
                rewards = (rewards - mean) / (std + eps)
        return rewards

    @staticmethod
    def print_events(events: dict) -> None:
        """Prints events in a better format.

        Useful for debugging.
        """
        for key, value in events.items():
            print(f"{key} = \n")
            for item in value:
                print(f"{item}\n")
