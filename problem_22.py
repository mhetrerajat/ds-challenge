"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def get_words(sentence, words):
    if not sentence or not words:
        return []

    words = set(words)
    answer = []

    length = len(sentence)
    for i in range(length):
        limit = i+1
        word_to_check = sentence[0:limit]
        if word_to_check in words:
            answer.append(word_to_check)
            words.remove(word_to_check)
            answer += get_words(sentence[limit:], words)
            break

    return answer



if __name__ == "__main__":
    print(get_words("thequickbrownfox", ['quick', 'brown', 'the', 'fox']))
    print(get_words("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))
