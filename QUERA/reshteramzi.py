# link : https://quera.ir/problemset/contest/106796/%D8%B1%D8%B4%D8%AA%D9%87%E2%80%8C%DB%8C%20%D8%B1%D9%85%D8%B2%DB%8C
# cc6

def end_to_start(string: str):
    string = list(string)
    string.insert(0, string[-1])
    string.pop(-1)

    return ''.join(string)


alpha = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n',
         'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}


def alpha_next(string: str):
    string = list(string)
    for i in range(len(string)):
        string[i] = alpha[string[i]]
    return ''.join(string)


l = int(input())
k = int(input())
string = input()

for i in range(k):
    string = end_to_start(string)
    string = alpha_next(string)

print(string)
