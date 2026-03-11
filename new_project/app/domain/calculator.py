from pydantic import BaseModel
from enum import Enum

class OperationType(str, Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"

class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: OperationType

class CalculationResponse(BaseModel):
    result: float
    operation: str
    message: str
