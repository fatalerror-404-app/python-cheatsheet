"""8. Functions — Scope and lambda"""

# Good: create a fresh list for each call
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
