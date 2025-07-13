from fastapi import APIRouter
from pydantic import BaseModel
from app.core.quantum_utils import run_quantum_optimization, build_ghz, optimize_production_schedule
from qiskit_aer import AerSimulator
from qiskit import transpile

router = APIRouter()

class OptimizationRequest(BaseModel):
    problem: str
    constraints: list

class GHZCircuitRequest(BaseModel):
    num_qubits: int

class ProductionScheduleRequest(BaseModel):
    tasks: list
    machines: list
    constraints: dict

@router.post("/optimization")
def quantum_optimization(request: OptimizationRequest):
    result = run_quantum_optimization(request.problem, request.constraints)
    return {
        "rota_otimizada": result["rota"],
        "tempo_estimado": result["tempo"],
        "quantum_simulation": True
    }

@router.post("/ghz_circuit")
def create_and_simulate_ghz_circuit(request: GHZCircuitRequest):
    if request.num_qubits < 1:
        return {"error": "Number of qubits must be at least 1"}

    ghz_circuit = build_ghz(request.num_qubits)

    # Simulate the circuit
    simulator = AerSimulator()
    compiled_circuit = transpile(ghz_circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1024)
    result = job.result()
    counts = result.get_counts(ghz_circuit)

    return {
        "num_qubits": request.num_qubits,
        "circuit_description": ghz_circuit.qasm(),
        "simulation_results": counts
    }

@router.post("/optimize_production_schedule")
def optimize_schedule(request: ProductionScheduleRequest):
    optimized_schedule = optimize_production_schedule(
        request.tasks, request.machines, request.constraints
    )
    return {"optimized_schedule": optimized_schedule}