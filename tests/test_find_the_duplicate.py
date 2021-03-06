from challenges.challenge_find_the_duplicate import find_duplicate
import timeit


def test_validar_se_encontra_numeros_repetidos():
    nums = [1, 3, 4, 2, 2]
    assert find_duplicate(nums) == 2
    nums = [3, 1, 3, 4, 2]
    assert find_duplicate(nums) == 3
    nums = [1, 1]
    assert find_duplicate(nums) == 1
    nums = [1, 1, 2]
    assert find_duplicate(nums) == 1
    nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
    assert find_duplicate(nums) == 7


def test_validar_se_retorna_false_quando_nao_envia_valores():
    nums = []
    find_duplicate(nums) is False


def test_validar_se_retorna_false_quando_envia_string():
    nums = ['a', 'b']
    find_duplicate(nums) is False


def test_validar_se_retorna_false_quando_nao_ha_repeticao():
    nums = [1, 2]
    find_duplicate(nums) is False


def test_validar_se_retorna_false_quando_passa_um_valor_apenas():
    nums = [1]
    find_duplicate(nums) is False


def test_validar_se_retorna_false_quando_passa_numero_negativo():
    nums = [-1, -1]
    find_duplicate(nums) is False


def test_validar_tempo_duplicate():
    setup_import = ("from challenges.challenge_find_the_duplicate "
                    "import find_duplicate")
    nums = [1, 3, 4, 2, 2]
    assert timeit.timeit(f'find_duplicate({nums})',
                         setup=f"{setup_import}", number=10000) <= 0.01
