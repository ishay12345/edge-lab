"""Example test module."""

import pytest


def test_import_edge_lab():
    """Test that edge_lab package can be imported."""
    import edge_lab

    assert edge_lab.__version__ == "0.1.0"


def test_basic_assertion():
    """Test basic assertion."""
    assert 1 + 1 == 2


@pytest.mark.parametrize("value,expected", [(1, 2), (2, 3), (3, 4)])
def test_parametrized(value, expected):
    """Test with parametrized inputs."""
    assert value + 1 == expected
