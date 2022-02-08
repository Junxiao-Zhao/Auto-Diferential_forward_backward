import sympy

x = sympy.symbols('x')
fx = list()

#compute the ln+1 through recursion
def l_func(n):
    if n == 1:
        return x
    else:
        return 4 * l_func(n - 1) * (1 - l_func(n - 1))

#forward Auto Differential
def forward(val, n):
    f = fx[0]
    df = sympy.diff(fx[0], x)
    for i in range(n):
        df = df * fx[i + 1] + f * sympy.diff(fx[i + 1], x)
        f = f * fx[i + 1]
    return df.evalf(subs={x: val})

def main():
    n = int(input("How many times do you want to get the funtion for Auto Differential? "))
    x = int(input("What's the value of x? "))
    #factor ln+1
    temp = sympy.factor_list(l_func(n))
    for i in range(len(temp[1])):
        fx.append(temp[1][i][0] ** temp[1][i][1])
    fx[0] = fx[0] * temp[0]
    print("The result of Auto Differential (forward) of the function is", forward(x, len(fx) - 1))

main()