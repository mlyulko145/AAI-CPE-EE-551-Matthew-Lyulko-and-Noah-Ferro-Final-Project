"""
quality_metric.py

Defines the QualityMetric class, which calculates a single overall quality score
from price, necessity, and expiration factors.
"""

from dataclasses import dataclass


@dataclass
class QualityMetric:
    """
    Stores scoring components for a grocery item and computes an overall score.

    Attributes:
        price_score (float): Higher is better - cheaper relative to average 
        necessity_score (float): Higher is more necessary 
        expiration_score (float): Higher is better 
    """
    price_score: float
    necessity_score: float
    expiration_score: float

    def overall_score(self, weights: tuple[float, float, float] | None = None) -> float:
    """
    Compute the weighted overall quality score.

    Args:
        weights: (w_price, w_necessity, w_expiration)

    Returns:
        Weighted score as a float.
    """
    if weights is None:
        weights = (0.5, 0.3, 0.2)

    w_price, w_nec, w_exp = weights
    return (
        (w_price * self.price_score)
        + (w_nec * self.necessity_score)
        + (w_exp * self.expiration_score)
    )


