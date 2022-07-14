def solutions(idx, target, words_by_idx, words_count, used_words):
    # base case - check we hit the end of target
    if idx >= len(target):
        print(' '.join(used_words))
        return

    if idx not in words_by_idx:
        return

    for word in words_by_idx[idx]:
        if words_count[word] == 0:
            continue
        used_words.append(word)
        words_count[word] -= 1

        # recursion
        solutions(idx + len(word), target, words_by_idx, words_count, used_words)

        used_words.pop()
        words_count[word] += 1


words = input().split(", ")
target = input()

# create dictionary
words_by_idx = {}
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1

    try:
        idx = 0
        while True:
            idx = target.index(word, idx)

            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(word)
            idx += len(word)
    except ValueError:
        pass

solutions(0, target, words_by_idx, words_count, [])
