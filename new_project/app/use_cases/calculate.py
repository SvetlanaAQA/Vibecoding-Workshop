from app.domain.calculator import CalculationRequest, CalculationResponse, OperationType
from fastapi import HTTPException

class Calculate:
    def execute(self, request: CalculationRequest) -> CalculationResponse:
        result = 0.0
        msg = ""

        if request.operation == OperationType.ADD:
            result = request.num1 + request.num2
            msg = f"Sum of {request.num1} and {request.num2}"
        elif request.operation == OperationType.SUBTRACT:
            result = request.num1 - request.num2
            msg = f"Subtraction of {request.num2} from {request.num1}"
        elif request.operation == OperationType.MULTIPLY:
            result = request.num1 * request.num2
            msg = f"Product of {request.num1} and {request.num2}"
        elif request.operation == OperationType.DIVIDE:
            if request.num2 == 0:
                raise HTTPException(status_code=400, detail="Cannot divide by zero")
            result = request.num1 / request.num2
            msg = f"Quotient of {request.num1} divided by {request.num2}"

        return CalculationResponse(
            result=result,
            operation=request.operation.value,
            message=msg
        )
