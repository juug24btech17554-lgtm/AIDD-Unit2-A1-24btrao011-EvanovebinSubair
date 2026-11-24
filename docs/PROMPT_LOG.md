# Prompt Log

| Step # | Technique | Exact prompt used | Tool response + my evaluation |
|---|---|---|---|
| 1 | Zero-shot | Create a file expense_splitter.py with a function split_equally(amount, people) that splits an amount equally among a list of people and returns a dictionary of name to share. | Cursor created the function and returned a dictionary of name to share, with an empty list returning {}. I accepted it because this is a standard task with a clear answer. |
| 2 | Few-shot | I want all functions in this project to follow one style. Here are examples. Example 1: every function has a docstring with Args, Returns and Raises sections. Example 2: if amount is not positive, raise ValueError("Amount must be positive"). Example 3: if the people list is empty, raise ValueError("At least one person required"). Now, in the same style, update split_equally and add add_expense, calculate_balances and format_summary to expense_splitter.py. | Accepted. Cursor first only showed the code in chat, so I asked again in Agent mode and it saved the changes into the file. The examples made every function use the same docstring and error style, which the zero-shot version did not. Screenshot: docs/screenshots/step2.png |

