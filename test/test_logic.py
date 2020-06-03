from src.logic import Nand, Not, And, Or

def test_nand():
    test_cases = [
        [False, False, True],
        [False, True, True],
        [True, False, True],
        [True, True, False]
    ]
    nand = Nand()
    for a, b, expected_output in test_cases:
        assert nand.run_cycle(a, b) == expected_output

def test_not():
    test_cases = [
        [True, False],
        [False, True]
    ]
    not_chip = Not()
    for a, expected_output in test_cases:
        assert not_chip.run_cycle(a) == expected_output

def test_and():
    test_cases = [
        [False, False, False],
        [False, True, False],
        [True, False, False],
        [True, True, True]
    ]
    _and = And()
    for a, b, expected_output in test_cases:
        assert _and.run_cycle(a, b) == expected_output

def test_or():
    test_cases = [
        [False, False, False],
        [False, True, True],
        [True, False, True],
        [True, True, True]
    ]
    _or = Or()
    for a, b, expected_output in test_cases:
        assert _or.run_cycle(a, b) == expected_output