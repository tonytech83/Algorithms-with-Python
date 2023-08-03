# exam: 05. Word Cruncher
# judge: https://judge.softuni.org/Contests/Compete/Index/3460#4

def word_cruncher(idx, words_by_idx, words_count, used_words):
    if len(''.join(used_words)) >= len(target_word):
        print(' '.join(used_words))
        return

    if idx not in words_by_idx:
        return

    for current_word in words_by_idx[idx]:
        if words_count[current_word] == 0:
            continue

        used_words.append(current_word)
        words_count[current_word] -= 1

        word_cruncher(idx + len(current_word), words_by_idx, words_count, used_words)

        used_words.pop()
        words_count[current_word] += 1


words = input().split(', ')
target_word = input()
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
            idx = target_word.index(word, idx)

            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(word)
            idx += len(word)
    except ValueError:
        pass

word_cruncher(0, words_by_idx, words_count, [])
