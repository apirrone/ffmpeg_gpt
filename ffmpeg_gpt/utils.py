def yesno(question):
    while True:
        answer = input(question + " ([Y]/n): ")
        if answer.lower() in ("y", "yes") or answer == "":
            return True
        elif answer.lower() in ("n", "no"):
            return False
        else:
            print("Please answer with 'y' or 'n'.")
