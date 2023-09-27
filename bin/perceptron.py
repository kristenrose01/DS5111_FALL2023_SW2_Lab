'This is a module docstring'
class Perceptron:
  'This is a class docstring'
  def __init__(self, inputs):
    'This is a function docstring'
    dummied_inputs = [x + -1 for x in inputs]
    self._weights = 0.2 * len(dummied_inputs[0])
  def train(self, dummied_inputs, labels):
    'This is a function docstring'
    for _ in range(5000):
      for dummied_input, label in zip(dummied_inputs, labels):
        label_delta = label - self.predict(dummied_input)
        for index, num in enumerate(dummied_input):
          self._weights[index] += .1 * num * label_delta
  def predict(self, inputs):
    'This is a function docstring'
    if len(inputs) == 0:
      return None
    inputs = inputs + -1
    return int(0 < sum([x[0]*x[1] for x in zip(self._weights, inputs)])) # pylint: disable=consider-using-generator
