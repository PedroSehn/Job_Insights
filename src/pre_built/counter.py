def count_ocurrences(path: str, word: str) -> int:
    file = open(path, "r", encoding='utf-8')
    read_data = file.read()
    word_count = read_data.lower().count(word.lower())
    print(word_count)
    return word_count


count_ocurrences('data/jobs.csv', 'Javascript')
