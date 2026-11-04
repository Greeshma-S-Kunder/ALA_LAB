from builtins import Exception
import os
import numpy as np
from gensim.models import KeyedVectors
import sys
import math
from math import sqrt
import random
from typing import Self

def load_model(word2vec_model_path:str) -> KeyedVectors:
    try:
        fast_model_path = os.path.expanduser(word2vec_model_path)
        return KeyedVectors.load(fast_model_path, mmap='r')
    except Exception as e:
        print(f"Failed to load model in word2vec format: {e}")
    return None

class Vec:
    def __init__(self,model_or_elements, word = None):
        if word is not None:
            if isinstance(word, str):
                try:
                    v = model_or_elements[word]
                    assert len(v) == 50
                    #initially v is an numpy array
                    self.elements = list(v)
                except KeyError:
                    print(f"Word '{word}' not in the model vocabulary.")
        else:
            self.elements = model_or_elements


    def __add__(self, t: Self):
        if len(self.elements) != len(t.elements):
            raise TypeError("Type error - vectors must be of same dimensions")
        return Vec([x + y for x, y in zip(self.elements, t.elements)])

    def __sub__(self, t: Self) -> Self:
        if len(self.elements) != len(t.elements):
            raise TypeError("Type error - vectors must be of same dimensions")
        return Vec([x - y for x, y in zip(self.elements, t.elements)])
    
    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        return Vec([x * scalar for x in self.elements])

    def __mul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        return Vec([scalar * x for x in self.elements])
    
    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        for i, val in enumerate(self.elements):
            self.elements[i] = val * scalar
        return self

    def vec_mean(self, src = None):
        if src is not None:
            self.elements = src
    
        mean = sum(self.elements)/len(self.elements)
        return mean
    
    def vec_demean(self, src = None) -> Self:
        if src is not None:
            self.elements = src
        mean_of_vector = self.vec_mean()
        for i in range(len(self.elements)):
            self.elements[i] = self.elements[i] - mean_of_vector
        return self
    
    def vec_std(self, src = None):
        total = 0
        if src is not None:
            self.elements = src
        self.vec_demean()
        for i in range(len(self.elements)):
            total = total + (math.pow(self.elements[i], 2))
        std = round(math.sqrt(total/len(self.elements)), 5)
        return std

    
    @staticmethod
    def zeros(n: int) -> Self:
        if not isinstance(n, int):
            raise TypeError("The value of n should be of type integer")
        if n <= 0:
            raise ValueError("The n value must be greater than 0")
        return Vec([0] * n)

    @staticmethod
    def ones(n: int) -> Self:
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if n <= 0:
            raise ValueError("n must be greater than 0")
        return Vec([1] * n)

    @staticmethod
    def uniform(n: int) -> Self:
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if n <= 0:
            raise ValueError("n must be greater than 0")
        return Vec([random.uniform(0, 1) for _ in range(n)])
    
    def norm(self) -> float:
        sum = 0
        for i in range(len(self.elements)):
            sum = sum + self.elements[i] * self.elements[i]
        return round(math.sqrt(sum), 3)
    
if sys.version_info < (3, 8):
    sys.exit("Error: This script requires Python 3.8 or higher.")
