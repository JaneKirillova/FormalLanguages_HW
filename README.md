# HW_6
Парсер написан на языке программирования python с использованием библиотеки `parsita`.

Для использования нужно установить эту библиотеку коммандой `pip3 install parsita` (для компилятора `python3`)

В данном репозитории содержатся следующие файлы:

`parser.py` - непосредственно сам парсер

`test.py` - тесты к парсеру

# Как использовать:

Программа запускается из консоли следующей командой:

`python3 parser.py <ключ(опционально)> <имя_файла> `

Для ключей есть следующие варианты:

`--atom` - парсер одного атома

`--module` - парсер определения модуля

`--relation` - парсер для определения отношения

`--relations` - парсер для определения последовательности отношений, разделенных точкой

`--prog` - парчер для программы целиком (аналогично запуску без ключа)

Если в файле были только корретктные отношения, то программа выведет в файл все отношения, указанные в файле, в формате:

`operation ( left_operand ) (right_operand)`

То есть для отношения `f :- a` вывод будет таким: `:- (ID(f)) (ID(a))`

Все идентификаторы дополнительно оборачиваются в скобки.

Если же файл был некорректным, то будет выведена ошибка

# Запуск тестов:

Для тестов нужно из консоли ввести команду

`python3 test.py`

Если все тесты прошли, то выведется строчка `All tests pass!`, иначе программа упадет по assert