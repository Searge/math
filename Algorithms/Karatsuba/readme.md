# Метод Карацуби
Нагадаємо в чому полягає основна ідея методу. Нехай, в нас є два числа $X$ та $Y$,
які мають розрядність $n$, кожне з яких ми можемо розбити навпіл і отримати пари чисел
$a$, $b$ та $c$, $d$ відповідно, кожне з яких буде мати розрядність $n/2$.
В такому випадку можна записати:
$X = 10^{n/2}a + b$ та $Y = 10^{n/2}c + d$

Тоді добуток $X\cdot Y = 10^n ac + 10^{n/2}(ad + dc) + bd$

Основна специфіка методу полягає в тому, щоб обраховувати не чотири менші добутки
$ac, ad, bc, bd$, а три — $ac, bd, (a + b)(c + d)$, де добуток $(a + b)(c + d)$
використовується для обрахунку $ad + bc$ із використанням вже обрахованих сум $ac, bd$:<br />
$ad + bc = (a + b)(c + d) - ac - bd$

Окрім того, що сам метод Карацуби працює швидше за стандартний метод множення в стовпчик, його можна успішно застосовувати для множення чисел у завданнях з,
так званою, довгою арифметикою, коли розрядність чисел може сягати 100 і більше.

Наприклад, при розрядності чисел 50:

X = 21625695688898558125310188636840316594920403182768
Y = 13306827740879180856696800391510469038934180115260
XY = 287769407308846640970310151509826255482575362419155842891311909556878670000425352112987881085839680

Зверніть увагу, мова не йде про використання чисел з плаваючою комою, адже в такому випадку були би втрати в точності отриманого результату.

В рамках даного завдання, вам потрібно реалізувати метод Карацуби для множення чисел з довгої арифметики. Нижче наводяться кілька тестів, які дозволять перевірити коректність роботи ваших програм.

## Зауваження

1. Ви можете реалізовувати метод Карацуби на будь-якій мові програмування, яка для вас є зручною. Тести, що наводяться нижче, не залежать від обраної мови.
2. За [цим посиланням](data_examples.txt) ви можете завантажити приклад вхідних даних із числами різної розмірності та вихідних даних для тестів. Ви можете використовувати інформацію з цього файлу для перевірки роботи вашої програми перед тим, як давати відповіді на контрольні питання.
3. Для спрощення реалізації ви можете припустити, що розрядності всіх вхідних чисел в тестах дорівнюють ступеням двійки, тобто: 2, 4, 8, 16, 32, 64, 128, ...
4. Нагадуємо, що згідно кодексу честі, який прийнятий на цьому курсі, ви не маєте права публікувати готові рішення програм на форумах курсу. Такі повідомлення будуть видалятись. Але ви можете (і це усіляко вітається) запитувати в своїх колег або співробітників курсу питання щодо можливої реалізації. Також дозволено розміщення невеликих фрагментів коду, але які не дозволяють повністю відтворити вашу програму.