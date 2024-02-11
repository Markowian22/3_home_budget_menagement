import sys
import argparse


class Parser:
    """
    Class for parsing command line arguments.

    Methods
    -------
    parse_args():
        Parses command line arguments.
    """

    def __init__(self):
        """
        Initializes the argument parser.
        """
        self.parser = argparse.ArgumentParser(
            description="""Management of the household budget"""
        )

        self.action_group = self.parser.add_mutually_exclusive_group(required=True)

        self.action_group.add_argument(
            "--add-expense",
            dest="action",
            action="store_const",
            const="add_expense",
            help="Adding an expense",
        )

        self.action_group.add_argument(
            "--add-income",
            dest="action",
            action="store_const",
            const="add_income",
            help="Adding income",
        )

        self.action_group.add_argument(
            "--delete",
            dest="action",
            action="store_const",
            const="delete",
            help="Deletion of an expense or income",
        )

        self.action_group.add_argument(
            "--stats",
            dest="action",
            action="store_const",
            const="stats",
            help="Display of statistics",
        )

        self.action_group.add_argument(
            "--list",
            dest="action",
            action="store_const",
            const="list",
            help="Display of entries",
        )

        self.add_group = self.parser.add_argument_group(
            """Adding an item,income or expense"""
        )
        self.add_group.add_argument(
            "--name",
            type=str,
            help="Element name",
            required="--add-expense" in sys.argv or "--add-income" in sys.argv,
        )

        self.add_group.add_argument(
            "--category",
            type=str,
            help="Category name",
            required="--add-expense" in sys.argv or "--add-income" in sys.argv,
        )

        self.add_group.add_argument(
            "--date",
            type=str,
            help="Date of occurrence of expenditure or revenue",
            required="--add-expense" in sys.argv or "--add-income" in sys.argv,
        )

        self.add_group.add_argument(
            "--value",
            type=float,
            help="value",
            required="--add-expense" in sys.argv or "--add-income" in sys.argv,
        )

        self.delete_group = self.parser.add_argument_group("Deleting an item")
        self.delete_group.add_argument(
            "--id", type=int, help="Item identifier", required="--delete" in sys.argv
        )

    def parse_args(self):
        """
        Parses command line arguments.

        Returns
        -------
        argparse.Namespace
            Namespace containing command line arguments.
        """
        return self.parser.parse_args()
