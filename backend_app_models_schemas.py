from pydantic import BaseModel
from typing import List, Optional

class SinaisVitais(BaseModel):
    paciente_id: str
    pressao_sistolica: float
    pressao_diastolica: float
    frequencia_cardiaca: float

class ConsultaRequest(BaseModel):
    paciente_id: str
    especialidade: str
    preferencia_idioma: str = "pt"

class PerfilSaude(BaseModel):
    paciente_id: str
    idade: int
    sexo: str
    historico: List[str]

class OptimizationRequest(BaseModel):
    problem: str
    constraints: List[str]

class QuantumPlatform(BaseModel):
    nome: str
    tecnologia_qubit: str
    qubits_fisicos: Optional[List[int]]
    qubits_logicos: Optional[str]
    gate_depth: Optional[int]
    codificacao: str
    temperatura: str
    coerencia: Optional[str]
    fidelidade: Optional[str]
    ano_fundacao: int
    ano_lancamento: Optional[int]