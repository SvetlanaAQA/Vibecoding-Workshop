from app.domain.user import User

class GetUserInfo:
    def execute(self) -> User:
        # Hardcoded user info as requested
        return User(
            name="Svetlana Pulucciu",
            role="Strategic Business Development & Technical Engineering",
            location="Chisinau, Moldova",
            skills=["FastAPI", "Python", "Clean Architecture", "RAN Integration"]
        )
