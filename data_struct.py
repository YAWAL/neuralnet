# import _sha256
#
# class Layer:
#     perceptrons = list()
#
#     def __init__(self, inp):
#         self.perceptrons = inp
# #
#
#
# class Neuron:
#     # value = float
#
#     def __init__(self, inp):
#         self.value = inp
#
#     def neuron_hash(self):
#         return _sha256.sha256(self.value)
#
#
# class Link:
#     neurons = list()
#
#     def __init__(self, neuron1, neuron2):
#         self.neurons.append(neuron1)
#         self.neurons.append(neuron2)
#
#     def print_neuron_hashes(self):
#         print(self.neurons[0].neuron_hash())
#         print(self.neurons[1].neuron_hash())
#
#
# neuron1 = Neuron(4.5660)
# neuron2 = Neuron(1.0567)
#
# link = Link(neuron1, neuron2)
#
# link.print_neuron_hashes()
#
# # print(neuron.value)