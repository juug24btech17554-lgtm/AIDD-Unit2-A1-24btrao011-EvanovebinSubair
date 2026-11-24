# AIDD-Unit2-A1-24btrao011-EvanovebinSubair# AIDD Unit 2 - Assignment A1: AI Coding Assistant Practicum

**Name:** Evanove Bin Subair
**USN:** 24BTRAO011

## Tool used
Cursor (Agent mode, free Hobby tier)

## Project
Expense Splitter: a small Python module to split expenses among people, record who paid, calculate balances and print a summary. It includes unit tests.

## How to set up and run
1. Install Python 3.
2. Clone this repository.
3. Run the tests:

python -m unittest -v

## Prompting techniques used
- **Zero-shot (Step 1):** Used for the basic split_equally function, a standard and well-known task.
- **Few-shot (Step 2):** Used to make all functions follow one docstring style (Args, Returns, Raises) and one error-message style, using examples in the prompt.
- **Chain-of-thought (Step 3):** Used for the rounding edge case (100 split among 3 people), where Cursor explained the problem step by step before fixing it.

## Documentation
The full prompt log, screenshots and reflection are in the docs folder:
- docs/PROMPT_LOG.md
- docs/screenshots/
