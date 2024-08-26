def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in range(len(other_words)):
        cur_word_old = other_words[i]
        cur_word = cur_word_old.lower()
        if cur_word.find(root_word) != -1:
            same_words.append(cur_word_old)
            continue
        if root_word.find(cur_word) != -1:
            same_words.append(cur_word_old)
    print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
