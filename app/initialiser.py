from app.database.initialise import initialise
from app.database.session import engine
from sqlmodel import Session


def init() -> None:
    with Session(engine) as session:
        initialise(db)


def main() -> None:
    init()


if __name__ == "__main__":
    main()
