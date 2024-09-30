#täällä tyhjää

def kertoma(n):
    if n == 1:
        return 1
    else:
        return n * kertoma(n - 1)

# Tästä taitaa tulla Pythonin stack overflow?!
kertoma(2000)