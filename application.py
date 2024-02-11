from parser_1 import Parser


class Application:
    """
    Main application class for managing household budget.

    Methods
    -------
    main():
        Executes the appropriate action based on command line arguments.
    """

    def __init__(self, repository):
        """
        Initializes the application.

        Parameters
        ----------
        repository : Repository
            Repository class object for interacting with the database.
        """
        parser = Parser()
        self.arguments = parser.parse_args()
        self.repository = repository

    def main(self):
        """
        Executes the appropriate action based on command line arguments.
        """
        match self.arguments.action:
            case "list":
                self.list()
            case "stats":
                self.stats()
            case "delete":
                self.delete(self.arguments.id)

            case "add_income":
                self.add_income(
                    self.arguments.name,
                    self.arguments.category,
                    self.arguments.date,
                    self.arguments.value,
                )
            case "add_expense":
                self.add_expense(
                    self.arguments.name,
                    self.arguments.category,
                    self.arguments.date,
                    self.arguments.value,
                )

    def list(self):
        print("List of expenses")
        for item in self.repository.get_item():
            print(item)

    def stats(self):
        print("Stats")
        for item in self.repository.get_stats():
            print(item)

    def delete(self, item_id: int):
        print("Delete")
        self.repository.delete_item(item_id)

    def add_income(self, name: str, category: str, date: str, value: float):
        print("Add income")
        self.repository.add_item(name, category, date, value)

    def add_expense(self, name: str, category: str, date: str, value: float):
        print("Add expense")
        self.repository.add_item(name, category, date, value * -1)
