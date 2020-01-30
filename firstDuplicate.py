'''
Given an array a that contains only numbers in the range from 1 to a.length,
find the first duplicate number for which the second occurrence has the minimal index. In other words,
if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does.
If there are no such elements, return -1.

Example

For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be firstDuplicate(a) = 2;

For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ a.length.

[output] integer

The element in a that occurs in the array more than once and has the minimal index for its second occurrence. If there are no such elements, return -1.


# find the first duplicate number - 첫번째 중복수를 찾아라
import numpy as np
def firstDuplicate(a):
    b=[]                    # empty list 선언
    for i in range(len(a)): # a list 원소수만큼 0에서부터 반복
        print(b, a[i])
        if a[i] in b:       # b list에 a의 원소가 있다면
            print(a[i])     # 그 원소를 반환
            return(a[i])
        elif a[i] not in b and i == (len(a)-1):  # b list에 a의 원소가 없고 인덱스가 마지막이라면
            return -1       # -1 원소를 반환
        else:
            b.append(a[i])  # b list에 a의 원소를 붙인다.
'''
import numpy as np
# 함수 선언 (인자 list 형식 -> a list)
def firstDuplicate(a):
    freq = np.zeros(len(a)+1).astype(int)
    # a list를 받아서 중복되는 수를 찾아낸다.
    # 빈도수 개념으로 접근
    for i, v in enumerate(a):  # a list의 순서대로 원소를 i가 받아낸다.
        freq[v] += 1
        for idx, val in enumerate(freq):
            if val==2 :       # 원소수의 빈도수가 2이상 (중첩)
                return idx           # 인덱스를 반환
        if i == len(a)-1:
            return -1
