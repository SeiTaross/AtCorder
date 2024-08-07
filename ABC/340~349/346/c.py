import sys
import io

_INPUT = """\
10 158260522
877914575 24979445 623690081 262703497 24979445 1822804784 1430302156 1161735902 923078537 1189330739

"""

sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int, input().split()))
A = list(set(A))

ans = K*(K+1) // 2
for a in A:
    if a <= K:
        ans -= a

print(ans)