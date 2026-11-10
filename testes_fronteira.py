"""Testes de fronteira das 30 tarefas da amostra (RASCUNHO para revisão da dupla).

Regra: cada teste usa uma entrada no limite citado no enunciado e, quando a
entrada existe, um vizinho de cada lado. O oráculo vem só do enunciado e dos
exemplos. Campos: tid, args, expected, kind (no limite / vizinho abaixo /
vizinho acima / extremo), why (justificativa pelo enunciado).
Status: CONGELADO em 09/11/2026 após revisão cruzada (João: 113 OK, 1 discutido; Lucas: 114 OK).
HE/21 B3 mantido como vizinho acima do tamanho mínimo (o vizinho abaixo, 1 elemento, é proibido).
"""

def T(tid, args, expected, kind, why):
    return {"tid": tid, "args": args, "expected": expected, "kind": kind, "why": why}

TASKS = [
 {"id": "HumanEval/0", "entry": "has_close_elements",
  "excerpt": "are any two numbers closer to each other than given threshold",
  "tests": [
   T("B1", [[1.0, 2.0], 1.0], False, "no limite", "distância 1.0 igual ao limiar: não é 'closer than'."),
   T("B2", [[1.0, 2.0], 1.25], True, "vizinho acima", "limiar maior que a distância: são mais próximos."),
   T("B3", [[1.0, 2.0], 0.75], False, "vizinho abaixo", "limiar menor que a distância.")]},
 {"id": "HumanEval/12", "entry": "longest",
  "excerpt": "Return the first one in case of multiple strings of the same length.",
  "tests": [
   T("B1", [["ab", "cd"]], "ab", "no limite", "empate de tamanho: devolve a primeira."),
   T("B2", [["ab", "cde"]], "cde", "vizinho acima", "a segunda é uma letra maior."),
   T("B3", [["abc", "de"]], "abc", "vizinho abaixo", "a segunda é uma letra menor."),
   T("B4", [["x"]], "x", "extremo", "lista com uma só string.")]},
 {"id": "HumanEval/21", "entry": "rescale_to_unit",
  "excerpt": "Given list of numbers (of at least two elements) ... smallest will become 0 and the largest will become 1",
  "tests": [
   T("B1", [[2.0, 6.0]], [0.0, 1.0], "no limite", "exatamente dois elementos (mínimo permitido)."),
   T("B2", [[6.0, 2.0]], [1.0, 0.0], "no limite", "dois elementos com o maior primeiro."),
   T("B3", [[2.0, 4.0, 6.0]], [0.0, 0.5, 1.0], "vizinho acima", "três elementos.")]},
 {"id": "HumanEval/30", "entry": "get_positive",
  "excerpt": "Return only positive numbers in the list.",
  "tests": [
   T("B1", [[0]], [], "no limite", "0 não é positivo."),
   T("B2", [[1]], [1], "vizinho acima", "1 é positivo."),
   T("B3", [[-1]], [], "vizinho abaixo", "-1 não é positivo."),
   T("B4", [[-1, 0, 1]], [1], "no limite", "os três juntos, mantendo a ordem.")]},
 {"id": "HumanEval/68", "entry": "pluck",
  "excerpt": "non-negative integer nodes ... smallest even value ... smallest index ... If there are no even values ... return []",
  "tests": [
   T("B1", [[0]], [0, 0], "no limite", "0 é o menor valor permitido e é par."),
   T("B2", [[1]], [], "vizinho acima", "1 é ímpar: não há pares."),
   T("B3", [[2, 0, 0]], [0, 1], "no limite", "empate de zeros: menor índice."),
   T("B4", [[1, 2]], [2, 1], "vizinho acima", "menor par é 2.")]},
 {"id": "HumanEval/72", "entry": "will_it_fly",
  "excerpt": "the sum of its elements is less than or equal the maximum possible weight w",
  "tests": [
   T("B1", [[2, 2], 4], True, "no limite", "soma igual a w é permitida."),
   T("B2", [[2, 2], 3], False, "vizinho abaixo", "w uma unidade menor que a soma."),
   T("B3", [[2, 2], 5], True, "vizinho acima", "w uma unidade maior que a soma."),
   T("B4", [[3], 3], True, "no limite", "um elemento, soma igual a w.")]},
 {"id": "HumanEval/80", "entry": "is_happy",
  "excerpt": "A string is happy if its length is at least 3 and every 3 consecutive letters are distinct",
  "tests": [
   T("B1", ["abc"], True, "no limite", "tamanho 3, letras distintas."),
   T("B2", ["ab"], False, "vizinho abaixo", "tamanho 2 não atinge o mínimo."),
   T("B3", ["abcd"], True, "vizinho acima", "tamanho 4, toda janela distinta.")]},
 {"id": "HumanEval/96", "entry": "count_up_to",
  "excerpt": "integers that are prime numbers and less than n",
  "tests": [
   T("B1", [7], [2, 3, 5], "no limite", "7 é primo, mas não é menor que 7."),
   T("B2", [8], [2, 3, 5, 7], "vizinho acima", "7 é menor que 8."),
   T("B3", [6], [2, 3, 5], "vizinho abaixo", "5 é menor que 6."),
   T("B4", [2], [], "no limite", "2 não é menor que 2."),
   T("B5", [3], [2], "vizinho acima", "2 é menor que 3.")]},
 {"id": "HumanEval/108", "entry": "count_nums",
  "excerpt": "number of elements which has a sum of digits > 0 ... -123 has signed digits -1, 2, and 3",
  "tests": [
   T("B1", [[-11]], 0, "no limite", "-1 + 1 = 0, não é > 0 (o exemplo do enunciado confirma)."),
   T("B2", [[-12]], 1, "vizinho acima", "-1 + 2 = 1 > 0."),
   T("B3", [[-10]], 0, "vizinho abaixo", "-1 + 0 = -1."),
   T("B4", [[0]], 0, "no limite", "soma dos dígitos de 0 é 0.")]},
 {"id": "HumanEval/122", "entry": "add_elements",
  "excerpt": "sum of the elements with at most two digits from the first k elements of arr. 1 <= k <= len(arr)",
  "tests": [
   T("B1", [[99, 100], 2], 99, "no limite", "99 tem dois dígitos (entra); 100 tem três (piloto)."),
   T("B2", [[10, 9], 2], 19, "no limite", "10 tem dois dígitos e entra (piloto)."),
   T("B3", [[5, 6, 7], 3], 18, "extremo", "k = len(arr), maior valor permitido (piloto)."),
   T("B4", [[5, 6, 7], 1], 5, "extremo", "k = 1, menor valor permitido.")]},
 {"id": "HumanEval/126", "entry": "is_sorted",
  "excerpt": "If list has more than 1 duplicate of the same number, return False.",
  "tests": [
   T("B1", [[1, 1]], True, "no limite", "uma duplicata é aceita (exemplo [1,2,2,3,3,4] -> True)."),
   T("B2", [[1, 1, 1]], False, "vizinho acima", "três iguais é mais de uma duplicata."),
   T("B3", [[1, 2]], True, "vizinho abaixo", "sem duplicata."),
   T("B4", [[5]], True, "extremo", "um elemento (exemplo do enunciado).")]},
 {"id": "HumanEval/129", "entry": "minPath",
  "excerpt": "Given a grid with N rows and N columns (N >= 2) and a positive integer k",
  "tests": [
   T("B1", [[[1, 2], [3, 4]], 1], [1], "no limite", "N = 2 e k = 1, os menores valores permitidos."),
   T("B2", [[[1, 2], [3, 4]], 3], [1, 2, 1], "no limite", "N = 2: vai e volta entre 1 e 2."),
   T("B3", [[[4, 3], [2, 1]], 2], [1, 2], "no limite", "N = 2 com o 1 no canto oposto."),
   T("B4", [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1], [1], "vizinho acima", "N = 3, k = 1.")]},
 {"id": "HumanEval/136", "entry": "largest_smallest_integers",
  "excerpt": "'a' is the largest of negative integers, and 'b' is the smallest of positive integers",
  "tests": [
   T("B1", [[-1, 0, 1]], (-1, 1), "no limite", "0 não é negativo nem positivo."),
   T("B2", [[0, 0]], (None, None), "no limite", "só zeros (exemplo [0] -> (None, None))."),
   T("B3", [[-2, -1]], (-1, None), "vizinho abaixo", "maior negativo é -1."),
   T("B4", [[1, 2]], (None, 1), "vizinho acima", "menor positivo é 1.")]},
 {"id": "HumanEval/156", "entry": "int_to_mini_roman",
  "excerpt": "Restrictions: 1 <= num <= 1000",
  "tests": [
   T("B1", [1], "i", "no limite", "menor valor permitido."),
   T("B2", [2], "ii", "vizinho acima", "vizinho do mínimo."),
   T("B3", [1000], "m", "no limite", "maior valor permitido."),
   T("B4", [999], "cmxcix", "vizinho abaixo", "vizinho do máximo.")]},
 {"id": "HumanEval/163", "entry": "generate_integers",
  "excerpt": "return the even digits between a and b, in ascending order ... generate_integers(2, 8) => [2, 4, 6, 8]",
  "tests": [
   T("B1", [2, 2], [2], "no limite", "a = b par: o exemplo mostra que os extremos entram."),
   T("B2", [3, 3], [], "vizinho acima", "a = b ímpar."),
   T("B3", [1, 2], [2], "no limite", "extremo superior par entra."),
   T("B4", [7, 9], [8], "vizinho", "um só dígito par no intervalo.")]},
 {"id": "Mbpp/66", "entry": "pos_count",
  "excerpt": "count the number of positive numbers in a list",
  "tests": [
   T("B1", [[0]], 0, "no limite", "0 não é positivo."),
   T("B2", [[1]], 1, "vizinho acima", "1 é positivo."),
   T("B3", [[-1]], 0, "vizinho abaixo", "-1 não é positivo."),
   T("B4", [[-1, 0, 1]], 1, "no limite", "os três juntos.")]},
 {"id": "Mbpp/167", "entry": "next_power_of_2",
  "excerpt": "smallest power of 2 greater than or equal to n",
  "tests": [
   T("B1", [16], 16, "no limite", "16 já é potência de 2 (piloto)."),
   T("B2", [17], 32, "vizinho acima", "17 passa de 16."),
   T("B3", [15], 16, "vizinho abaixo", "15 sobe para 16."),
   T("B4", [1], 1, "extremo", "1 = 2^0 (piloto)."),
   T("B5", [2], 2, "no limite", "2 é potência de 2 (piloto).")]},
 {"id": "Mbpp/223", "entry": "is_majority",
  "excerpt": "The majority element is the element that occurs more than n/2 times.",
  "tests": [
   T("B1", [[1, 1, 2, 2], 4, 1], False, "no limite", "2 ocorrências = n/2, não é mais que n/2."),
   T("B2", [[1, 1, 1, 2], 4, 1], True, "vizinho acima", "3 > 2."),
   T("B3", [[1, 2, 3, 4], 4, 1], False, "vizinho abaixo", "1 ocorrência."),
   T("B4", [[1, 1, 2], 3, 1], True, "no limite", "n ímpar: 2 > 1,5.")]},
 {"id": "Mbpp/238", "entry": "number_of_substrings",
  "excerpt": "count the number of non-empty substrings of a given string",
  "tests": [
   T("B1", [""], 0, "no limite", "string vazia não tem substring não vazia."),
   T("B2", ["a"], 1, "vizinho acima", "uma substring."),
   T("B3", ["ab"], 3, "vizinho acima", "a, b, ab.")]},
 {"id": "Mbpp/239", "entry": "get_total_number_of_sequences",
  "excerpt": "each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m",
  "tests": [
   T("B1", [2, 2], 1, "no limite", "só (1, 2): 2 é exatamente o dobro de 1 e igual a m."),
   T("B2", [1, 2], 0, "vizinho abaixo", "m = 1 não comporta o dobro de 1."),
   T("B3", [3, 2], 2, "vizinho acima", "(1, 2) e (1, 3)."),
   T("B4", [4, 2], 4, "no limite", "(1,2), (1,3), (1,4), (2,4): 4 é o dobro de 2 e igual a m.")]},
 {"id": "Mbpp/244", "entry": "next_Perfect_Square",
  "excerpt": "find the next perfect square greater than a given number",
  "tests": [
   T("B1", [36], 49, "no limite", "36 já é quadrado; o próximo maior é 49."),
   T("B2", [35], 36, "vizinho abaixo", "exemplo do enunciado."),
   T("B3", [37], 49, "vizinho acima", "o próximo é 49.")]},
 {"id": "Mbpp/256", "entry": "count_Primes_nums",
  "excerpt": "returns the number of prime numbers less than the given non-negative number",
  "tests": [
   T("B1", [7], 3, "no limite", "2, 3, 5; o 7 não é menor que 7."),
   T("B2", [8], 4, "vizinho acima", "inclui o 7."),
   T("B3", [6], 3, "vizinho abaixo", "2, 3, 5."),
   T("B4", [2], 0, "no limite", "2 não é menor que 2."),
   T("B5", [0], 0, "extremo", "menor valor não negativo.")]},
 {"id": "Mbpp/277", "entry": "dict_filter",
  "excerpt": "only include entries with values greater than or equal to n",
  "tests": [
   T("B1", [{"a": 5, "b": 4, "c": 6}, 5], {"a": 5, "c": 6}, "no limite", "valor igual a n entra."),
   T("B2", [{"a": 5, "b": 4, "c": 6}, 6], {"c": 6}, "vizinho acima", "n uma unidade maior."),
   T("B3", [{"a": 5, "b": 4, "c": 6}, 4], {"a": 5, "b": 4, "c": 6}, "vizinho abaixo", "n uma unidade menor.")]},
 {"id": "Mbpp/283", "entry": "validate",
  "excerpt": "frequency of each digit in the integer is less than or equal to the digit itself",
  "tests": [
   T("B1", [22], True, "no limite", "o 2 aparece 2 vezes (igual ao dígito)."),
   T("B2", [222], False, "vizinho acima", "o 2 aparece 3 vezes."),
   T("B3", [2], True, "vizinho abaixo", "o 2 aparece 1 vez."),
   T("B4", [11], False, "vizinho acima", "o 1 aparece 2 vezes.")]},
 {"id": "Mbpp/388", "entry": "highest_Power_of_2",
  "excerpt": "highest power of 2 that is less than or equal to n",
  "tests": [
   T("B1", [16], 16, "no limite", "16 é potência de 2."),
   T("B2", [17], 16, "vizinho acima", "17 desce para 16."),
   T("B3", [15], 8, "vizinho abaixo", "15 desce para 8."),
   T("B4", [1], 1, "extremo", "1 = 2^0.")]},
 {"id": "Mbpp/433", "entry": "check_greater",
  "excerpt": "check whether the entered number is greater than the elements of the given array",
  "tests": [
   T("B1", [[1, 2, 3], 3], False, "no limite", "3 não é maior que 3 (piloto)."),
   T("B2", [[1, 2, 3], 4], True, "vizinho acima", "4 é maior que todos (piloto)."),
   T("B3", [[1, 2, 3], 2], False, "vizinho abaixo", "2 não é maior que 3.")]},
 {"id": "Mbpp/566", "entry": "sum_digits",
  "excerpt": "sum of the digits of a non-negative integer",
  "tests": [
   T("B1", [0], 0, "no limite", "menor valor não negativo."),
   T("B2", [9], 9, "vizinho", "maior número de um dígito."),
   T("B3", [10], 1, "vizinho", "menor número de dois dígitos.")]},
 {"id": "Mbpp/589", "entry": "perfect_squares",
  "excerpt": "find perfect squares between two given numbers; assert perfect_squares(1,30)==[1, 4, 9, 16, 25]",
  "tests": [
   T("B1", [4, 8], [4], "no limite", "o exemplo mostra que o limite inferior entra."),
   T("B2", [5, 10], [9], "vizinho acima", "limite inferior logo acima de 4."),
   T("B3", [3, 8], [4], "vizinho abaixo", "limite inferior logo abaixo de 4.")]},
 {"id": "Mbpp/603", "entry": "get_ludic",
  "excerpt": "get all lucid numbers smaller than or equal to a given integer",
  "tests": [
   T("B1", [7], [1, 2, 3, 5, 7], "no limite", "7 é lúdico e igual a n: entra."),
   T("B2", [6], [1, 2, 3, 5], "vizinho abaixo", "7 fica de fora."),
   T("B3", [8], [1, 2, 3, 5, 7], "vizinho acima", "8 não é lúdico."),
   T("B4", [1], [1], "extremo", "1 é lúdico (o exemplo começa em 1).")]},
 {"id": "Mbpp/745", "entry": "divisible_by_digits",
  "excerpt": "numbers within a given range from startnum to endnum; assert divisible_by_digits(1,22)==[1, ..., 22]",
  "tests": [
   T("B1", [22, 22], [22], "no limite", "o exemplo mostra que os extremos entram."),
   T("B2", [12, 15], [12, 15], "no limite", "os dois extremos são válidos."),
   T("B3", [13, 14], [], "vizinho", "13 e 14 não dividem pelos dígitos."),
   T("B4", [14, 15], [15], "no limite", "extremo superior entra; 14 não divide por 4.")]},
]
