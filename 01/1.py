import fileinput

def twosum(xs):
    seen = set()
    for x in xs:
        if 2020 - x in seen:
            return x * (2020 - x)
        seen.add(x)

def threesum(xs):
    xs.sort()
    for i in range(len(xs)-2):
        a = xs[i]
        lo = i+1
        hi = len(xs)-1
        while lo < hi:
            b = xs[lo]
            c = xs[hi]
            if a + b + c > 2020:
                hi -= 1
            elif a + b + c < 2020:
                lo += 1
            else:
                return a*b*c

xs = [int(x) for x in fileinput.input()]

# Part 1
print(twosum(xs))

# Part 2
print(threesum(xs))