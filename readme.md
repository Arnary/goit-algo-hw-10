## Висновки щодо використання методу Монте-Карло для пошуку визначеного інтеграла

Реалізований алгоритм для пошуку визначеного інтеграла за допомогою методу Монте-Карло показав непогані результати, які для перевірки точності були порівнянні із результатами що дає функція quad з підмодуля integrate бібліотеки SciPy. Але видно, що ці результати не стійкі і залежать від конкретної генерації випадкових точок, що являється типовою особливістю методу Монте-Карло: точність залежить від кількості випадкових точок, і результат може змінюватися при кожному запуску програми. Чим більше точок, тим точніший результат. Найближчий результат, до того що надає quad, вдалось досягти при кількості в 10000000 точок (для функції 2x-x^2, для інших функцій, особливо більш складних, може знадобитись ще більше точок, щоб наблизитись до точного результату), далі підвищувати їх кількість здається недоцільним.

Метод Монте-Карло може бути корисним для обчислення інтегралів у складних областях або у випадках, коли інші методи непридатні.
Проте для досягнення заданої точності може знадобитися велика кількість випадкових точок, що може бути обчислювально витратним. Вибір методу залежить від ваших потреб у точності і обчислювальних ресурсах. Якщо точність є критичним фактором, то слід обрати інший метод, якщо такий доступний. Однак, якщо важливіше отримати швидкий оцінковий результат, метод Монте-Карло також може бути корисним.