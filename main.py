# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import random


class Document:
    def __init__(self):
        pass

    def __str__(self):
        return ""


class Rangable(Document):
    def __init__(self, bottom, top):
        super().__init__()
        self.bottom = bottom
        self.top = top


class Parenthesis(Rangable):
    def __init__(self, opening, closing, content):
        super().__init__(opening, closing)
        self.content = content

    def __str__(self):
        return f"\\left{self.bottom}{self.content}\\right{self.top}"


class Integral(Rangable):
    def __init__(self, bottom, top):
        super().__init__(bottom, top)

    def __str__(self):
        return f"\\int_{{{self.bottom}}}^{{{self.top}}}"


class Sum(Rangable):
    def __init__(self, bottom, top):
        super().__init__(bottom, top)

    def __str__(self):
        return f"\\sum_{{{self.bottom}}}^{{{self.top}}}"


class ParitalDerivative(Rangable):
    def __init__(self, bottom, top):
        super().__init__(bottom, top)

    def __str__(self):
        return f"\\frac{{\\partial}}{{\\partial {self.bottom}}} \\left({self.top}\\right)"


class Vector(Document):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def __str__(self):
        return f"\\in \\mathbb{{R}}^{{{self.n}}}"


class Func(Document):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f"\\{self.name} "


funcs = ["sin", "cos", "tan", "exp", "log", "nabla", "mathbb{P}", "det", "Phi"]
greeks = ["alpha", "beta", "gamma", "epsilon", "delta", "omega", "rho", "phi", "theta", "pi", "infty"]


def randomGreek():
    return greek(random.choice(greeks))


def randomVar():
    return random.choice(["x", "y", "z", "e", "n", "l", "m", "k", "i", "j", randomGreek()])


def randomStatementEnd(depthrem):
    t = random.randint(0, 1)
    if t == 0:
        return random.choice([" = ", "\\le ", " < "]) + str(randomTerm(depthrem))
    if t == 1:
        return str(Vector(random.randint(1, 4)))


def randomStatement(depthrem):
    depthrem -= 1
    t = random.randint(0, 1)
    if t == 0:
        return randomTerm(depthrem)
        # return Vector(random.randint(1, 4))
    if t == 1:
        return random.choice([" = ", "\\le ", " < "]) + str(randomTerm(depthrem))


def greek(a):
    return f"\\{a} "


def randomTerm(depthrem):
    if depthrem <= 0:
        return random.choice([random.randint(0, 10), randomVar()])
    depthrem -= 1
    t = random.randint(0, 14)
    if t == 0:
        return str(Func(random.choice(funcs))) + str(Parenthesis("(", ")", randomTerm(depthrem)))
    if t == 1:
        return "\\frac{" + str(randomTerm(depthrem - 1)) + "}{" + str(randomTerm(depthrem - 1)) + "}"
    if t == 2:
        return ParitalDerivative(randomVar(), randomTerm(depthrem))
    if t in [3, 4]:
        return random.randint(0, 10)
    if t in [5, 6, 7]:
        return randomVar()
    if t == 8:
        return str(randomTerm(depthrem)) + str(random.choice(["+", "-", "\\odot ", "\\otimes "])) + str(
            randomTerm(depthrem))
    if t == 9:
        return str(Integral(randomTerm(1), randomTerm(0))) + str(
            randomTerm(depthrem)) + " d " + str(
            randomVar())
    if t == 10:
        return str(Sum(str(randomVar() + "=" + str(randomTerm(0))), randomTerm(0))) + str(
            randomTerm(depthrem))
    if t == 11:
        return str("{\\left(" + str(randomTerm(depthrem - 1)) + "\\right)}^{" + str(randomTerm(0)) + "}")
    if t == 12:
        return "\\left({" + str(randomTerm(depthrem)) + "}\\right)_{" + str(randomVar()) + str(randomVar()) + "}"
    if t == 13:
        return "\\sqrt{" + str(randomTerm(depthrem)) + "}"
    if t == 14:
        return "\\lim_{" + str(randomVar()) + "\\rightarrow " + str(randomTerm(0)) + "}" + str(randomTerm(depthrem))

    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    exprs = [randomTerm(3)]
    exprs += [randomStatement(3), randomStatementEnd(3)]
    # exprs2 = [randomTerm(22), randomStatementEnd(8)]
    with open("out.tex", "wt") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage{amsmath}\n")
        f.write("\\usepackage{amsfonts}\n")
        f.write("\\begin{document}\n")
        # f.write("\\section{Problem 1.}\n")
        # f.write("Suppose that")
        f.write("$$\n")
        for expr in exprs:
            print(expr)
            f.write(str(expr))
        f.write("\n$$\n")
        # f.write("Prove that")
        # f.write("$$\n")
        # for expr in exprs2:
        #     print(expr)
        #     f.write(str(expr))
        # f.write("\n$$\n")
        f.write("\n\\end{document}")
    os.system("pdflatex out.tex")
    os.system("rm out.log")
    os.system("open out.pdf")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
