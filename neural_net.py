import random
import n_math
import csvparser
import time
import sys

class NeuralNet:
    def __init__(self):
        self.layers = list()

    def initialization(self, layers_sizes):
        for i in range(len(layers_sizes)):
            layer = list()
            for j in range(layers_sizes[i]):
                links = list()
                if i == 0:
                    links = None
                else:
                    for k in range(layers_sizes[i-1]):
                        links.append(Link(random.random()))
                layer.append(Perceptron(0.0, random.random(), links))
            self.layers.append(Layer(layer))

    def initialize_from_file(self, layers_sizes):
        pass

    def process(self, input):
        for item in range(len(input)):
            self.layers[0].perceptrons[item].z = input[item]
        for i in range(1, len(self.layers)):
            for pcpt in self.layers[i].perceptrons:
                pcpt.z = n_math.sigmoid(self.calk_sigmoid_input(pcpt, self.layers[i - 1]))

    def analyze(self):
        last_layer = self.layers[len(self.layers) - 1]
        max = last_layer.perceptrons[0].z
        out = 0
        for i in range(len(last_layer.perceptrons)):
            if last_layer.perceptrons[i].z > max:
                max = last_layer.perceptrons[i].z
                out = i
        return out

    def calk_sigmoid_input(self, pcpt, prev_layer) -> float:
        sum = 0.00
        for j in range(len(pcpt.links)):
            sum += pcpt.links[j].w * prev_layer.perceptrons[j].z - pcpt.b
        return sum

    def back_propagation(self, input):
        deviations = list()
        deviations.append(None)
        for layerid in range(1, len(self.layers)):
            layer_deviations = list()
            for prcpt in self.layers[layerid].perceptrons:
                layer_deviations.append(0.0)
            deviations.append(layer_deviations)

        last_layer_id = len(self.layers) - 1

        for prcpt_id in range(len(self.layers[last_layer_id].perceptrons)):
            prcpt = self.layers[last_layer_id].perceptrons[prcpt_id]
            prv_layer = self.layers[last_layer_id - 1]
            deviations[last_layer_id][prcpt_id] = (prcpt.z - input[prcpt_id])*\
                                                  n_math.sigmoid_derivative(self.calk_sigmoid_input(prcpt, prv_layer))

        for layerid in range(len(self.layers) - 2, 0, -1):
            for prcpt_id in range(len(self.layers[layerid].perceptrons)):
                prcpt = self.layers[layerid].perceptrons[prcpt_id]
                prv_layer = self.layers[layerid - 1]
                next_layer_id = layerid + 1
                w_vector = list()
                for next_prcpt in self.layers[next_layer_id].perceptrons:
                    w_vector.append(next_prcpt.links[prcpt_id].w)
                delta_vector = deviations[next_layer_id]
                deviations[layerid][prcpt_id] = n_math.dot(w_vector, delta_vector) *\
                                                n_math.sigmoid_derivative(self.calk_sigmoid_input(prcpt, prv_layer))

        for layerid in range(1, len(self.layers)):
            for prcpt_id in range(len(self.layers[layerid].perceptrons)):
                prcpt = self.layers[layerid].perceptrons[prcpt_id]
                prcpt.b += deviations[layerid][prcpt_id]

        for layerid in range(1, len(self.layers)):
            for prcpt_id in range(len(self.layers[layerid].perceptrons)):
                prcpt = self.layers[layerid].perceptrons[prcpt_id]
                prev_layer = self.layers[layerid - 1]
                for link_id in range(len(prcpt.links)):
                    prcpt.links[link_id].w += prev_layer.perceptrons[link_id].z * deviations[layerid][prcpt_id]



class Perceptron:
    def __init__(self, _z, _b, _links):
        self.z = _z
        self.b = _b
        self.links = _links


class Link:
    def __init__(self, _w):
        self.w = _w


class Layer:
    def __init__(self, inp):
        self.perceptrons = inp


def test_nn():
    inputs = csvparser.csv_parser("dataset/test.csv")
    nn = NeuralNet()
    nn.initialization([len(inputs[0][1]), 15, 24])

    for input in inputs:
        pixels = input[1]
        input_for_bp = list()
        for i in range(24):
            input_for_bp.append(0)
        input_for_bp[input[0]-1] = 1
        nn.process(pixels)

        nn.back_propagation(input_for_bp)

    nn.process(inputs[0][1])

    print(nn.analyze())



test_nn()