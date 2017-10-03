y = [4, 6, 1, 3, 5, 7, 25]
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def stars(arr):
    for i in arr:
        print "*" * i
stars(y)
def starsPlus(arr):
    for i in arr:
        if isinstance(i, int):
            print "*" * i
        elif isinstance(i, str):
            print (i[0].lower()) * len(i)
starsPlus(x)