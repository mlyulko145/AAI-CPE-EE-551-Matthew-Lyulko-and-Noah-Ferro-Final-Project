"""
utils.py

Utility functions for price analysis and accessibility scoring.
"""

def average_price(prices: list[float]) -> float:
    """
    Compute the average price of a list of prices.
    
        prices: list of item prices

    Returns:
        Average price as a float
    """
    if not prices:
        raise ValueError("Price list cannot be empty.")

    total = 0.0
    for price in prices:  # for loop 
        total += price

    return total / len(prices)


def accessibility_score(price: float, avg_price: float) -> float:
    """
    Compute accessibility score relative to the average price.

        price: item price
        avg_price: average price for that item

    Returns:
        Accessibility score between 0 and 1
    """
    if avg_price <= 0:  # if statement requirement
        raise ValueError("Average price must be greater than zero.")

    # cheaper items are more accessible
    return min(1.0, avg_price / price)

