import sys

def solution(A):
    sum = 0
    for x in A:
        sum += x
    half_sum = sum / 2
    a = A
    list.sort(a)
    b = list()

    temp = 0
    for i in range(-1, 0-len(a), -1):
        tempsum = temp+a[i]
        if tempsum > half_sum:
            continue
        else:
            temp += a[i]
            b.append(a[i])
            a.pop(i)
            if abs(temp - half_sum) <= a[0]:
                break

    sum1 = 0
    for x in a:
        sum1 += x

    sum2 = 0
    for x in b:
        sum2 += x

    print(a)
    print(b)

    return abs(sum1-sum2)



def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
