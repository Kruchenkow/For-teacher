text: str = "Не знаю, как там в Лондоне, я не была." \
            "Может, там собака — друг человека." \
            "А у нас управдом — друг человека!"

print(len(text))  # Подсчет кол-ва символов

print(text[::-1])  # Переворот строки

print(text.title())  # Все слова с большой буквы

print(text.upper())  # Вся строка прописными буквами

print((text.count("нд")), "нд в строке")  # Число "нд" в строке
print((text.count("ам")), "ам в строке")  # Число "ам" в строке
print((text.count("о")), "о в строке")  # Число "о" в строке

import transliterate  # Установка модуля перевода

print(transliterate.translit(text, reversed=True))  # Перевод текста, как самостоятельное задание

print(text)  # Вывод в консоль исходной строки

print(text[:-4])  # Вывод в консоль текста с условием "Кличество символов - 4" (Не понял задание)

print(text.count("нд") > text.count("ор"))  # Результаты сравнения числа входжений: "нд" больше чем "ор"?