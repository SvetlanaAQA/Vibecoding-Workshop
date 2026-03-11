from fastapi import APIRouter
from app.domain.calculator import CalculationRequest, CalculationResponse
from app.use_cases.calculate import Calculate

router = APIRouter()

@router.post("/calculate", response_model=CalculationResponse)
async def calculate_endpoint(request: CalculationRequest):
    use_case = Calculate()
    return use_case.execute(request)
