import sys
sys.path.append(".")
import pytest
import os

from bin.perceptron import Perceptron

@pytest.fixture
def train_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    return the_perceptron

def test_perceptron(train_perceptron):
    assert train_perceptron.predict([1,1]) ==  1, "Failed when given [1,1]"
    assert train_perceptron.predict([1,0]) ==  1, "Failed when given [1,0]"
    assert train_perceptron.predict([0,1]) ==  1, "Failed when given [0,1]"
    assert train_perceptron.predict([0,0]) ==  0, "Failed when given [0,0]"

@pytest.mark.xfail(reason="Creating a failed test")
def test_perceptron_fail(train_perceptron):
    assert train_perceptron.predict([1,1]) ==  1, "Failed when given [1,1]"
    assert train_perceptron.predict([1,0]) ==  1, "Failed when given [1,0]"
    assert train_perceptron.predict([0,1]) ==  1, "Failed when given [0,1]"
    assert train_perceptron.predict([0,0]) ==  1, "Failed when given [0,0]"

@pytest.mark.skipif(sys.platform != "linux", reason="Must use linux")
def test_memory():
    # Getting all memory using os.popen()
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])
    
    assert total_memory >= 500, "Not enough total memory"
    assert used_memory <= 200, "Too much used memory"
    assert free_memory >= 300, "Not enough free memory"

@pytest.mark.skip(reason="This test is not yet ready for prime time")
def test_silly():
    x = 1 + 2 + 3

    assert x > 1

@pytest.mark.parametrize("trainingset, labels, expected", [
    ([[0,0], [1,0], [1,1]], [0, 1, 1], [0, 1, 1]),
    ([[1,1], [0,1], [0,1], [1,0], [0,0]], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]),
    ([[0,1], [1,1], [0,0], [0,1], [0,1], [0,0], [1,1]], [1, 1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1]),
    ([[1,0], [0,0], [0,1], [1,0]], [1, 0, 1, 1], [1, 0, 1, 1]),
    ([[0,0], [1,0], [0,1], [0,1], [1,1], [0,0], [1,0]], [0, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 0, 1])
    ])
def test_new_set(trainingset, labels, expected):
    the_perceptron = Perceptron()
    the_perceptron.train(trainingset, labels)

    for item in range(len(trainingset)):
        assert the_perceptron.predict(trainingset[item]) == expected[item], f"Failed when given {trainingset[item]}" 
