import modelVector
from modelVector import Vec

model = modelVector.load_model("glove50/glove_50_fast.wordvectors")

v1 = Vec(model,"india")
v2 = Vec(model,"asia")

v4 = Vec([2]*50)
v6 = Vec([4]*50)
v3 = v1 + v4
v5 = v4 + v3
v7 = v4 + v6



print(v1.elements)
print("\n")
"""
print(v4.elements)
print("\n")
print(v3.elements)
print("\n")
print(v4.elements)
print("\n")
print(v5.elements)
print("\n")
print(v7.elements) """

print(v1.vec_mean())
print(v1.vec_demean().elements)
print(v1.vec_std())
print(v1.norm())
