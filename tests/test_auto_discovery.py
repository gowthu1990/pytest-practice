"""
    Autodiscovery of Unit Tests

    - Test files: Must be named test_*.py or *_test.py.
    - Test functions: Must be named test_*.
    - Test classes: Must be named Test*.
"""

def test_addition():
    """
    unit test for addition
    """
    print("\ntest addition")
    assert 1 + 1 == 2

def test_subtraction():
    """
    unit test for subtraction
    """
    print("\ntest subtraction")
    result = 5 - 3
    assert result == 2, "Subtraction test failed!" # The string is an optional error message

def some_other_function():
    """
    This is ignored
    """
    print("\nIgnored tests")
    # This function will be ignored by pytest
    pass
