#  function receiving the information from user
def input_sides():
    #  inputting all sides
    a = input("A = ")
    b = input("B = ")
    c = input("C = ")
    #  call the function to check the existing of the triangle
    #  and if we receive "True" than we call another function
    if checking_if_triangle_exist(a, b, c):
        print(f"Perimeter of the triangle with sides: {a}, {b}, {c} = {perimeter_of_triangle(a, b, c)}.")
        print(f"Square of the triangle with sides: {a}, {b}, {c} = {square_of_triangle(a, b, c)}.")
    else:
        #  if we receive False we should say bad news - the triangle does not exist
        print(f"A triangle with sides {a}, {b}, {c} cannot exist. And he doesn't have neither perimeter nor square.")


#  function to check the existing of the triangle
def checking_if_triangle_exist(aa, bb, cc):
    if aa + bb > cc and bb + cc > aa and aa + cc > bb:
        boolean_answer = True
    else:
        boolean_answer = False
    return boolean_answer


#  perimeter of the triangle
def perimeter_of_triangle(aa, bb, cc):
    p = aa + bb + cc
    return p


#  square of the triangle
def square_of_triangle(aa, bb, cc):
    per = (aa + bb + cc) / 2
    s = pow(per * (per - aa) * (per - bb) * (per - cc), 1 / 2)
    return s


#  main part of the application
if __name__ == '__main__':
    print("Enter please three sides of a triangle: a, b, c")
    #  call the function to ask the user input the information
    input_sides()
