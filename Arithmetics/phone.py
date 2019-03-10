from typing import List

# Створюємо список літер a..o, та чисел 2..6 (в 3 екземплярах)
alpha_o: List[str] = [chr(i) for i in range(ord('a'), ord('p'))]
nums_2_6: List[int] = sorted(list(range(2, 7)) * 3)

# Об'єднуємо списки в словник
n_first = dict(zip(alpha_o, nums_2_6))

# Від p..z та 7..9 у 4-х
alpha_z: List[str] = [chr(i) for i in range(ord('p'), ord('z') + 1)]
nums_7_9: List[int] = sorted([7, 8, 9] * 4)

n_rest = dict(zip(alpha_z, nums_7_9))

# З'єднуємо два списки в один
d = dict(n_first, **n_rest)

# Відредагований словник числових відповідностей
num_dict = {'a': 2, 'b': 2, 'c': 2,
            'd': 3, 'e': 3, 'f': 3,
            'g': 4, 'h': 4, 'i': 4,
            'j': 5, 'k': 5, 'l': 5,
            'm': 6, 'n': 6, 'o': 6,
            'p': 7, 'q': 7, 'r': 7, 's': 7,
            't': 8, 'u': 8, 'v': 8,
            'w': 9, 'x': 9, 'y': 9, 'z': 9}

# Створюємо числову змінну з введеного слова:
name = int(''.join(map(str,
                       list(num_dict[i] for i in input().lower()))))

# список усіх можливих літер з номера:
letters_from_number = []

for l in str(name):
    for letter, num in num_dict.items():
        if num == int(l):
            letters_from_number.append(letter)

print(f"Число зі слова: {name}\n")
print(f"Список можливих літер: \n {''.join(letters_from_number)}")
