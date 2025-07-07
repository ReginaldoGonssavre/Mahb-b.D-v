from flask import Flask, request, jsonify, render_template
from qiskit import QuantumCircuit, transpile, Aer
from qiskit.visualization import plot_histogram
import base64
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate_deutsch_jozsa():
    data = request.get_json()
    input_value = data.get('value')

    if input_value not in [0, 1]:
        return jsonify({'error': 'Input value must be 0 or 1.'}), 400

    try:
        # Create a quantum circuit for Deutsch-Jozsa algorithm
        # For simplicity, we'll demonstrate a basic constant/balanced function
        # based on the input_value.
        # This is a simplified Deutsch-Jozsa for demonstration purposes.

        qc = QuantumCircuit(2, 1) # 2 qubits, 1 classical bit

        # Apply Hadamard gates to both qubits
        qc.h(0)
        qc.h(1)

        # Apply a barrier for visualization
        qc.barrier()

        # Oracle for constant function f(x) = input_value
        if input_value == 0: # f(x) = 0 (constant)
            pass # No operation needed for f(x) = 0
        else: # f(x) = 1 (constant)
            qc.x(1) # Apply X gate to the second qubit

        # Apply Hadamard to the first qubit again
        qc.barrier()
        qc.h(0)

        # Measure the first qubit
        qc.measure(0, 0)

        # Simulate the circuit
        simulator = Aer.get_backend('qasm_simulator')
        compiled_circuit = transpile(qc, simulator)
        job = simulator.run(compiled_circuit, shots=1024)
        result = job.result()
        counts = result.get_counts(qc)

        # Interpret result for Deutsch-Jozsa
        # If count for '0' is high, function is constant. If count for '1' is high, function is balanced.
        # In this simplified example, we are only demonstrating constant functions.
        if '0' in counts and counts['0'] > 512: # More than half are '0'
            dj_result = f"The function is constant (f(x) = {input_value})."
        else:
            dj_result = "The function is balanced (not demonstrated in this simplified example)."

        # You can also return the circuit drawing as an image
        # fig = qc.draw(output='mpl')
        # buf = io.BytesIO()
        # fig.savefig(buf, format='png')
        # buf.seek(0)
        # img_base64 = base64.b64encode(buf.read()).decode('utf-8')

        return jsonify({'result': dj_result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
