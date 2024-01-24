from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


from utils import arrs
def test_get():
    # Позитивный тест: индекс существует
    assert arrs.get([1, 2, 3], 1, "test") == 2
    # Позитивный тест: пустой список, используется значение по умолчанию
    assert arrs.get([], 0, "test") == "test"
    # Граничный случай: использование отрицательного индекса (не поддерживается)
    assert arrs.get([1, 2, 3], -1, "test") == "test"
def test_slice():
    # Позитивный тест: выбор среза из списка
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    # Позитивный тест: выбор среза без указания конечного индекса
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    # Граничный случай: пустой список
    assert arrs.my_slice([], start=1, end=3) == []
    # Позитивный тест: отрицательный индекс start (смещение от конца списка)
    assert arrs.my_slice([1, 2, 3], start=-1) == [3]
    # Граничный случай: отрицательный индекс end (не поддерживается)
    assert arrs.my_slice([1, 2, 3], end=-1) == [1, 2]
    # Граничный случай: end больше длины списка (весь список после start)
    assert arrs.my_slice([1, 2, 3], start=1, end=5) == [2, 3]
    # Граничный случай: start больше длины списка (пустой список)
    assert arrs.my_slice([1, 2, 3], start=5) == []
    # Граничный случай: end меньше start (пустой список)
    assert arrs.my_slice([1, 2, 3], start=2, end=1) == []
