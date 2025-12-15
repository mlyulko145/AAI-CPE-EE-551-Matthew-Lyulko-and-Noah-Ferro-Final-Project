import pytest
from src.quality_metric import QualityMetric
from src.utils import average_price


def test_overall_score_computation():
    metric = QualityMetric(0.8, 0.6, 0.9)
    score = metric.overall_score()
    assert 0 <= score <= 1


def test_average_price_empty_list():
    with pytest.raises(ValueError):
        average_price([])
