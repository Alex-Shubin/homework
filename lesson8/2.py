'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''
def rect_sq(a, b, square:True):
    return a * b if square else (a + b) * 2
    


