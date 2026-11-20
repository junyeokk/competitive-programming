sentence = list(map(str, input().split()))
cnt = 0

for s in sentence:
    if 'ae' in s:
        cnt += 1

if cnt / len(sentence) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")