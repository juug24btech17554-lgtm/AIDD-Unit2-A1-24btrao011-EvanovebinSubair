def split_equally(amount, people):
    """Split amount equally among people and return name-to-share mapping."""
    if not people:
        return {}
    share = amount / len(people)
    return {name: share for name in people}
