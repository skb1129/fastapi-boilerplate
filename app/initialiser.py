from app.database.initialise import initialise
from app.database.session import SessionLocal


def init() -> None:
    db = SessionLocal()
    initialise(db)


def main() -> None:
    init()


if __name__ == "__main__":
    main()
