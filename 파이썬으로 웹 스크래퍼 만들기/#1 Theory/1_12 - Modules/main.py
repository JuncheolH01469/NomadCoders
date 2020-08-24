# Example 1
import math
from math import ceil, fabs, fsum
from math import fsum as f_sum
from calculator import plus

# 올림
print(math.ceil(1.2))

# 절대값
print(math.fabs(-1.2))

print()

# Example 2
# Example 1에서 math를 모두 import 하면 비효율적일 수 있기 때문에
# from을 사용하여 필요한 함수들만 import
# from math import ceil, fabs, fsum

print(ceil(1.2))
print(fabs(-1.2))
print(fsum([1, 2, 3, 4, 5, 6, 7]))

print()

# Example 3
# 자신이 원하는 이름으로 설정 가능하다
# 그 대신 이후부터 자신이 설정한 이름으로만 사용 가능
# from math import fsum as f_sum

print(ceil(1.2))
print(fabs(-1.2))
print(f_sum([1, 2, 3, 4, 5, 6, 7]))

print()

# Example 4
# 자신이 직접 만든 함수를 다른 파이썬 파일로 해서 만들어도 모듈 형태로 해서 불러올 수 있음
# from calculator import plus

result = plus(3, 4)
print(result)