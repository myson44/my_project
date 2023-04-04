import time
import copy

start = time.time()
A = [0 for _ in range(1000000)]
print("list comp", time.time() - start)

start = time.time()
A = [0] * 8000000
print("[0]*x", time.time() - start)

start = time.time()
B = A[:]
print("slicing", time.time() - start)

start = time.time()
C = copy.deepcopy(A)
print("deep", time.time() - start)


B[0] = 99

# start = time.time()
# while len(A)>0:
#     A.pop()
# print("pop", time.time() - start)


# start = time.time()
# while len(B)>0:
#     B.pop(0)
# print("pop0", time.time() - start)


print(A[:10])
print(B[:10])
print(C[:10])



