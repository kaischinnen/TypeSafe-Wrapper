from main import JevLib


def run_feel(jl: JevLib) -> None:
    email_state = """
    Please resolve my email immediately!
    """

    if jl.feels(email_state, "needs an urgent reply") > 0.7:
        print("The email needs an urgent reply.")
    else:
        print("The email does not need an urgent reply.")


def main() -> None:
    try:
        with JevLib() as jl:
            print("JevLib initialized successfully.")
            run_feel(jl)
    except RuntimeError as error:
        print(f"Error initializing JevLib: {error}")


if __name__ == "__main__":
    main()
