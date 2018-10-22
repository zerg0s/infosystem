S = input()
A = S[:S.find('h')]
B = S[S.find('h'):S.rfind('h') + 1]
C = S[S.rfind('h') + 1:]
S = A + B[::-1] + C
print(S)
