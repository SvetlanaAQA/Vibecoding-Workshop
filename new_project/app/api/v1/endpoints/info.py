from fastapi import APIRouter
from app.use_cases.get_user_info import GetUserInfo

router = APIRouter()

@router.get("/")
async def get_user_info():
    use_case = GetUserInfo()
    return use_case.execute()
