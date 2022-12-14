
# скопировано с интернета) S = √p(p - a)(p - b)(p - c)

# подсчёт площади треугольника
a, b, c = 6, 8, 13
# условие if позволяет добавлять ветвление в выполнение программы
# (разные варианты выполнения в зависимости от входных данных)
# if <некое условие>:
#     <на отступе что выполнять если условие соблюдается>
# else: (иначе, если нужно указываем, если нет - можно пропустить)
#     <на отступе что выполнять если условие НЕ соблюдается>
# само условие можно совмещать с помощью ключевого слово and (чтобы выполнялись все условия)
# так же есть оператор or (чтобы выполнялось хотя бы одно из условий)
if a + b > c and b + c > a and a + c > b:
    p = (a + b + c) / 2
    s = pow(p * (p - a) * (p - b) * (p - c), 1 / 2)
    print(f"Площадь треугольника со сторонами {a}, {b}, {c} составляет: {s}")
else:
    print(f'Треугольник со сторонами {a}, {b}, {c} существовать не может. И площади у него тоже нет :)')