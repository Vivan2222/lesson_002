#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set=set(garden)
meadow_set=set(meadow)
# выведите на консоль все виды цветов
al_flowers=meadow_set.union(garden_set)
flowers_a=garden_set.intersection(meadow_set)
print(flowers_a)


# выведите на консоль те, которые растут в саду, но не растут на лугу
print(garden_set.difference(meadow_set))

# выведите на консоль те, которые растут на лугу, но не растут в саду
print(meadow_set.difference(garden_set))


