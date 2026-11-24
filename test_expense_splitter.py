import unittest
from decimal import Decimal

from expense_splitter import (
    add_expense,
    calculate_balances,
    format_summary,
    split_equally,
)


class SplitEquallyTests(unittest.TestCase):
    def test_remainder_cents_go_to_the_first_people(self):
        shares = split_equally(100, ["A", "B", "C"])
        self.assertEqual(
            shares,
            {
                "A": Decimal("33.34"),
                "B": Decimal("33.33"),
                "C": Decimal("33.33"),
            },
        )
        self.assertEqual(sum(shares.values()), Decimal("100.00"))
        for share in shares.values():
            self.assertEqual(share, share.quantize(Decimal("0.01")))

    def test_amount_must_be_positive(self):
        for amount in (0, -1, -0.01):
            with self.assertRaises(ValueError) as caught:
                split_equally(amount, ["A"])
            self.assertEqual(str(caught.exception), "Amount must be positive")

    def test_people_must_not_be_empty(self):
        with self.assertRaises(ValueError) as caught:
            split_equally(100, [])
        self.assertEqual(str(caught.exception), "At least one person required")


class OtherValueErrorTests(unittest.TestCase):
    def test_add_expense_rejects_non_positive_amount(self):
        with self.assertRaises(ValueError) as caught:
            add_expense([], "A", 0, "snack")
        self.assertEqual(str(caught.exception), "Amount must be positive")

    def test_add_expense_requires_a_payer(self):
        with self.assertRaises(ValueError) as caught:
            add_expense([], "", 10, "snack")
        self.assertEqual(str(caught.exception), "Payer is required")

    def test_calculate_balances_requires_people(self):
        with self.assertRaises(ValueError) as caught:
            calculate_balances([], [])
        self.assertEqual(str(caught.exception), "At least one person required")

    def test_calculate_balances_requires_known_payer(self):
        expenses = [{"payer": "Z", "amount": 10, "description": "snack"}]
        with self.assertRaises(ValueError) as caught:
            calculate_balances(expenses, ["A"])
        self.assertEqual(str(caught.exception), "Payer must be included in people")

    def test_format_summary_requires_balances(self):
        with self.assertRaises(ValueError) as caught:
            format_summary({})
        self.assertEqual(str(caught.exception), "At least one person required")


if __name__ == "__main__":
    unittest.main()
