from constants import correct_int


def is_correct_int(raw_int: int | str) -> bool:
    pass


if __name__ == "__main__":
    assert is_correct_int(raw_int="12") is True
    assert is_correct_int(raw_int="12&") is False
    assert is_correct_int(raw_int=None) is False
