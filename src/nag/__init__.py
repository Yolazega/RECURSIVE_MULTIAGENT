"""
NAG™ - NeuralAgentGenesis
Patent-pending recursive neural network architecture
Copyright © 2025 - All rights reserved
"""

__version__ = "0.1.0"
__author__ = "Robert Zemichiel"

from .core.orchestrator import NAGOrchestrator
from .core.agent import IntelligentAgent

__all__ = ["NAGOrchestrator", "IntelligentAgent"]