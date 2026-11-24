from decimal import Decimal, ROUND_HALF_UP


def split_equally(amount, people):
    """Split an amount equally among a list of people.

    Shares are rounded to 2 decimal places. Any leftover cents are given, one
    cent at a time, to the first people in the list so the shares add up to
    the amount exactly.

    Args:
        amount (float): Total amount to split.
        people (list[str]): Names of the people sharing the amount.

    Returns:
        dict[str, Decimal]: Mapping of each person's name to their share,
            each quantized to 2 decimal places.

    Raises:
        ValueError: If amount is not positive, or if people is empty.
    """
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if not people:
        raise ValueError("At least one person required")
    total = Decimal(str(amount)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    total_cents = int(total * 100)
    base_cents, extra_cents = divmod(total_cents, len(people))
    shares = {}
    for index, name in enumerate(people):
        cents = base_cents + (1 if index < extra_cents else 0)
        shares[name] = (Decimal(cents) / Decimal(100)).quantize(Decimal("0.01"))
    return shares


def add_expense(expenses, payer, amount, description):
    """Append one shared expense paid by a single person.

    Args:
        expenses (list[dict]): Expense records to update. Each record has
            payer, amount, and description.
        payer (str): Name of the person who paid.
        amount (float): Amount paid.
        description (str): Short description of the expense.

    Returns:
        list[dict]: The same expenses list, with the new expense appended.

    Raises:
        ValueError: If amount is not positive, or if payer is empty.
    """
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if not payer:
        raise ValueError("Payer is required")
    expenses.append(
        {"payer": payer, "amount": amount, "description": description}
    )
    return expenses


def calculate_balances(expenses, people):
    """Calculate each person's net balance from equally shared expenses.

    Each expense is split equally across people. The payer is credited the
    full amount, and every person is debited their share. A positive balance
    means the person is owed money. A negative balance means they owe money.

    Args:
        expenses (list[dict]): Expense records with payer, amount, and
            description.
        people (list[str]): Names of everyone in the group, including payers.

    Returns:
        dict[str, float]: Mapping of each person's name to their net balance.

    Raises:
        ValueError: If people is empty, if an expense amount is not positive,
            or if a payer is not included in people.
    """
    if not people:
        raise ValueError("At least one person required")
    balances = {name: Decimal("0.00") for name in people}
    for expense in expenses:
        payer = expense["payer"]
        if payer not in balances:
            raise ValueError("Payer must be included in people")
        shares = split_equally(expense["amount"], people)
        balances[payer] += sum(shares.values())
        for name, share in shares.items():
            balances[name] -= share
    return balances


def format_summary(balances):
    """Format net balances as a readable summary.

    Args:
        balances (dict[str, float]): Mapping of each person's name to their
            net balance. Positive means they are owed money. Negative means
            they owe money.

    Returns:
        str: One line per person, sorted by name. Each line states whether
            that person is owed money, owes money, or is settled.

    Raises:
        ValueError: If balances is empty.
    """
    if not balances:
        raise ValueError("At least one person required")
    lines = []
    for name in sorted(balances):
        balance = balances[name]
        if balance > 0:
            lines.append(f"{name} is owed {balance:.2f}")
        elif balance < 0:
            lines.append(f"{name} owes {abs(balance):.2f}")
        else:
            lines.append(f"{name} is settled")
    return "\n".join(lines)
