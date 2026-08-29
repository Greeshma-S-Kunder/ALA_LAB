import sys;
sys.path.append("../")
from ALA_LAB.vector import Vec
import time

print("v1 = Vec([2, -3, 4.5] * 8000)")
start = time.perf_counter()
v1 = Vec([2, -3, 4.5] * 8000)
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nv2 = Vec([2, 9, 3.6] * 8000)")
start = time.perf_counter()
v2 = Vec([2, 9, 3.6] * 8000)
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nv3 = v1 + v2")
start = time.perf_counter()
v3 = v1 + v2
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nv4 = v1 * 3")
start = time.perf_counter()
v4 = v1 * 3
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nv3 = 3 * v1")
start = time.perf_counter()
v3 = 3 * v1
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nv3 *= -2")
start = time.perf_counter()
v3 *= -2
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nv2 = v1 + v3")
start = time.perf_counter()
v2 = v1 + v3
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nv4 = v3 - v1")
start = time.perf_counter()
v4 = v3 - v1
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nv5 = -v1")
start = time.perf_counter()
v5 = -v1
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nv4 += v2")
start = time.perf_counter()
v4 += v2
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nz = Vec.zeros(4)")
start = time.perf_counter()
z = Vec.zeros(4)
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\no = Vec.ones(4)")
start = time.perf_counter()
o = Vec.ones(4)
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nu = Vec.uniform(3)")
start = time.perf_counter()
u = Vec.uniform(4)
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nlen(v1)")
start = time.perf_counter()
len(v1)
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")

print("\nv1 = v1.norm()")
start = time.perf_counter()
v1 = v1.norm()
end = time.perf_counter()
execute_time = end - start
print(f"{execute_time:.5e}")