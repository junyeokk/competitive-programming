mw, mb = map(int, input().split())
tw, tb = map(int, input().split())
pw, pb = map(int, input().split())

minb = min(mw, tb, pw)
minw = min(mb, tw, pb)
if minb == minw:
    print(2 * minb)
else:
    print(2 * min(minb, minw) + 1)