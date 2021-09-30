# import math
#
# T = int(input())
# for tc in range(T):
#     n, k = map(int, input().split())
#     s = input()
#     A_alphabet = list(map(int, input().split()))
#     letter_to_index = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10,
#                        'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20,
#                        'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
#     index_to_letter = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 7: 'g', 6: 'f', 9: 'i', 8: 'h', 11: 'k', 10: 'j',
#                        13: 'm', 12: 'l', 15: 'o', 14: 'n', 17: 'q', 16: 'p', 19: 's', 18: 'r', 21: 'u', 20: 't',
#                        23: 'w', 22: 'v', 25: 'y', 24: 'x', 26: 'z'}
#     s_to_numbers = []
#     for i in range(n):
#         s_to_numbers.append(A_alphabet[letter_to_index[s[i]] - 1])
#     #s_copy_sorted = s_to_numbers.copy()
#     #s_copy_sorted.sort(reverse=True)
#     #sum_first_k = sum(s_copy_sorted[0:k])
#     #print(s_copy_sorted)
#
#     biggest = 0
#     smallest = math.inf
#     biggest_index = None
#     smallest_index = None
#     sequence_letters = []
#     sequence_numbers = []
#     for j in range(n):
#         if s_to_numbers[j] >= biggest:
#             if len(sequence_numbers) == k:
#                 sequence_numbers.pop(smallest_index)
#                 sequence_letters.pop(smallest_index)
#             sequence_letters.insert(letter_to_index[s[j]], s[j])
#             sequence_numbers.append(letter_to_index[s[j]], s_to_numbers[j])
#             biggest = s_to_numbers[j]
#             biggest_index = letter_to_index[s[j]]
#             if len(sequence_numbers) == 1:
#                 smallest = s_to_numbers[j]
#         elif biggest > s_to_numbers[j] > smallest:
#             if len(sequence_numbers) == k:
#                 sequence_numbers.pop()
#                 sequence_letters.pop()
#             sequence_letters.insert(0, index_to_letter[j])
#             sequence_numbers.insert(0, s_to_numbers[j])
#             biggest = s_to_numbers[j]
#             if len(sequence_numbers) == 1:
#                 smallest = s_to_numbers[j]
#
