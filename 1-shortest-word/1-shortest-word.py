"""
Given a string of words, return the length of the shortest word(s).
"""

# FORM 1
# def get_shortest_word(text: str) -> int:
#     word_list = text.split()
#     len_list = []

#     for word in word_list:
#         len_list.append(len(word))

#     return min(len_list)


# FORM 2
# def get_shortest_word(text: str) -> int:
#     return min(map(lambda word: len(word), text.split()))


def get_shortest_word(text: str) -> int:  # FORM 3
    return len(min(text.split(), key=lambda word: len(word)))


text = 'El Alquimista relata el viaje del pastor Santiago en busca de un tesoro que le había sido revelado a través de un sueño repetitivo que le mostraba'
print(get_shortest_word(text))
