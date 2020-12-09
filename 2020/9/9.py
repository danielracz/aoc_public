import itertools

INPUT_FILE = "9.in"

with open(INPUT_FILE, 'r') as f:
    inp = list(map(int, f.read().splitlines()))

for i in range(25, len(inp)):
    if inp[i] not in (sum(x) for x in itertools.combinations(inp[i - 25 : i], r = 2)):
        n = inp[i]
        # part1
        print(n)
        break

# from stackoverflow (old python docu?)
def sliding_window(seq, n = 2):
    it = iter(seq)
    result = tuple(itertools.islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

## this is nice (from a blogpost)
#def sliding_window(iterable, n=2):
#    iterables = itertools.tee(iterable, n)
#
#    for iterable, num_skipped in zip(iterables, itertools.count()):
#        for _ in range(num_skipped):
#            next(iterable, None)
#
#    return zip(*iterables)

inp = [x for x in inp if x < n]
print(next(max(w) + min(w) for r in range(len(inp))
           for w in sliding_window(inp, r)
           if sum(w) == n))
