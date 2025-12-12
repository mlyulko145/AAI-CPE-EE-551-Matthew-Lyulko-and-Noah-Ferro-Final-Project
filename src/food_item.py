"""
food_item.py

Defines the FoodItem class. Each FoodItem contains a QualityMetric,
supports readable printing via __str__, and supports sorting/comparison via
operator overloading (__lt__).
"""

from __future__ import annotations
from dataclasses import dataclass
from src.quality_metric import QualityMetric

@dataclass
class FoodItem:
    """
    Represents a grocery item sold at a specific store.

    Attributes:
        name (str): Item name 
        store (str): Store name
        price (float): Item price 
        expiration_days (int): Days until expiration
        necessity_score (int): Survey based score
        metric (QualityMetric): Composed quality metric object.
    """
    name: str
    store: str
    price: float
    expiration_days: int
    necessity_score: int
    metric: QualityMetric

    def __str__(self) -> str:
        """
        Return a readable string representation 
        """
        return (
            f"{self.name} @ {self.store} | "
            f"${self.price:.2f}, exp={self.expiration_days} days, "
            f"necessity={self.necessity_score}, score={self.metric.overall_score():.3f}"
        )

    def __lt__(self, other: FoodItem) -> bool:
        """
        Operator overloading 
        Allows sorting FoodItems by overall quality score.
        """
        return self.metric.overall_score() < other.metric.overall_score()

