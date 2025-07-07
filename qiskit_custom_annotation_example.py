from numpy import pi
from qiskit import qasm3
from qiskit.circuit import annotation, QuantumCircuit

class NoSwapAnnotation(annotation.Annotation):
    namespace = "openqasm.noswap"

class Serializer(annotation.OpenQASM3Serializer):
    def dump(self, annotation):
        pass
            
    def load(self, namespace, payload):
        pass

circ = QuantumCircuit(4)
circ.h(range(4))
with circ.box(annotations=(NoSwapAnnotation(),)):
    circ.rx(pi, 0)
    circ.cx(0, 3)
circ.measure_all()
handlers = {"openqasm": Serializer()}
print(qasm3.dumps(circ, annotation_handlers=handlers))