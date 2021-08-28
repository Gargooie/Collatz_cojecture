import matplotlib.pyplot as plt

def f2(x):
    yield x
    while x!=1:
        if x%2==0:
            x=int(x/2)
            yield x
        else:
            x=x*3+1
            yield x

number=26
listing=list(f2(number))
plt.plot(range(len(listing)), listing)
plt.show()

print("{} iterations". format(len(list(f2(number)))))
print(list(f2(number)))
