from app.database.initialise import initialise
from app.database.session import create_session, global_init


def init() -> None:
    global_init()
    db = create_session()
    initialise(db)


def main() -> None:
    init()


if __name__ == "__main__":
    main()
