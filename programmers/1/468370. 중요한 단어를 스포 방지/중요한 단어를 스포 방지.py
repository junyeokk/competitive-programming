def solution(message, spoiler_ranges):
    res = 0
    i = 0
    words = []
    non_spoiler = set()
    
    while i < len(message):
        if message[i] != ' ':
            start = i
            while i < len(message) and message[i] != ' ':
                i += 1
            words.append((start, i - 1, message[start:i]))
        else:
            i += 1
    
    for w_start, w_end, word in words:
        is_spoiler = False
        for s_start, s_end in spoiler_ranges:
            if not (w_end < s_start or s_end < w_start):
                is_spoiler = True
                break
        if not is_spoiler:
            non_spoiler.add(word)
    
    word_spoilers = []
    for w_start, w_end, word in words:
        overlaps = set()
        for idx, (s_start, s_end) in enumerate(spoiler_ranges):
            if not (w_end < s_start or s_end < w_start):
                overlaps.add(idx)
        word_spoilers.append(overlaps)
    
    seen = set()
    clicked = set()
    
    for click_idx in range(len(spoiler_ranges)):
        clicked.add(click_idx)
        
        for i, (w_start, w_end, word) in enumerate(words):
            if len(word_spoilers[i]) == 0:
                continue
            if word_spoilers[i].issubset(clicked):
                if word not in seen and word not in non_spoiler:
                    res += 1
                seen.add(word)
    
    return res