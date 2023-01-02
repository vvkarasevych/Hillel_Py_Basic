def input_sides():
    a = input("A = ")
    b = input("B = ")
    c = input("C = ")
    if checking_if_triangle_exist(a, b, c):
        print(f"Perimeter of the triangle with sides: {a}, {b}, {c} = {perimeter_of_triangle(a, b, c)}.")
        print(f"Square of the triangle with sides: {a}, {b}, {c} = {square_of_triangle(a, b, c)}.")
    else:
        print(f"A triangle with sides {a}, {b}, {c} cannot exist. And he doesn't have neither perimeter nor square.")


def checking_if_triangle_exist(aa, bb, cc):
    if aa + bb > cc and bb + cc > aa and aa + cc > bb:
        return True
    else:
        return False


def perimeter_of_triangle(aa, bb, cc):
    p = aa+bb+cc
    return p


def square_of_triangle(aa, bb, cc):
    per = (aa + bb + cc) / 2
    s = pow(per * (per - aa) * (per - bb) * (per - cc), 1 / 2)
    return s


#  main part of the application
if __name__ == '__main__':
    print("Enter please three sides of a triangle: a, b, c")
    input_sides()
