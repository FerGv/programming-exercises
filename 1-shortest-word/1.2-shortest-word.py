"""
Given a string of words, return the length of the shortest word(s) and the word(s).
"""

# FORM 1
# def get_shortest_word(text: str) -> (int, str):
#     word_list = text.split()
#     len_list = []

#     for word in word_list:
#         len_list.append(len(word))

#     min_len = min(len_list)
#     min_word = None

#     for word in word_list:
#         if len(word) == min_len:
#             min_word = word

#     return min_len, min_word


# FORM 2
# def get_shortest_word(text: str) -> (int, str):
#     min_len = min(map(lambda word: len(word), text.split()))
#     min_word = list(
#         filter(lambda word: len(word) == min_len, text.split())
#     )[0]

#     return min_len, min_word


def get_shortest_word(text: str) -> (int, str):  # FORM 3
    min_word = min(text.split(), key=lambda word: len(word))

    return len(min_word), min_word


text = 'El Alquimista relata el viaje del pastor Santiago en busca de un tesoro que le había sido revelado a través de un sueño repetitivo que le mostraba'
print(get_shortest_word(text))
