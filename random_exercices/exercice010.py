def recursion(var):
    if len(var) == 1:
        return var
    print(f"Print Start Function {var}")

    if var[0] == var [1]:
        print(f"Print Before Condition {var}")
        return recursion(var[1:])
    print(f"Print Before Return {var}")
    return var[0] + recursion (var[1:])
print (recursion("CCCCSSevveen"))
