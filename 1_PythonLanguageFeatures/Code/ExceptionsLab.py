# Code for Section 1.14: Exceptions lab

# # Working with Exceptions for a guessing game
# from random import randint

# def parse_guess() -> int:
#     try:
#         if (guess := input('guess a number between 1 and 10 > ')).lower() == 'q':
#             raise GameOver
#         return int(guess)
#     except ValueError:
#         print('your guess must be a valid integer. ')
#         return parse_guess()

# def play():
#     print('press Q to quit.')

#     try:
#         while True:
#             answer = randint(1, 10)

#             while parse_guess() != answer:
#                 print('try again.')
#             else:
#                 print('you win!')

#     except GameOver:        
#         print('thanks for playing!')
#     finally:
#         print('like and subscribe!')

# if __name__ == '__main__':
#     play()

# -----------------------

# Re-raising and Raising From
# Exception handling is not always easy to implement well. Ineffective exception handling can introduce unexpected application behaviors. This lab step focuses on ensuring that exceptions are handled or re-raised.

# Exception handlers that don't resolve the exceptional condition can hide errors. The below "summarize_monthly" function implements four exception handlers. The top three handle specific exceptions and the fourth catches all others.

# billing.py

# import json
# from pathlib import Path

# def deserialize(data: str) -> dict:
#     return json.loads(data)

# def summarize_monthly():
#     path = Path(__file__).parent / 'payments.json'
#     try:
#         with open(path) as p:
#             payments = deserialize(p.read())

#             return { month: sum(payment) for month, payment in payments['months'].items() }
#     except KeyError:
#         print('unexpected file format.')
#     except FileNotFoundError:
#         print('missing required file.')
#     except ValueError:
#         print('non-numeric payment amount.')
#     except Exception as ex:
#         print('unplanned exception.')

# # report.py

# from datetime import datetime

# from billing import summarize_monthly

# this_month = datetime.now().strftime('%b').lower()
# this_month = summarize_monthly()[this_month]

# print(f'The total for this month is: ${this_month}')

# #payments.json - change months to m to throw an exception

# {
#     "months": {
#         "jan": [500.14, 951.93, 74.50, 130.26, 130.26, 130.26],
#         "feb": [367.14, 951.93, 74.50, 130.26, 130.26, 130.26],
#         "mar": [542.14, 951.93, 74.50, 130.26, 130.26, 130.26],
#         "apr": [137.14, 951.93, 74.50, 130.26, 130.26, 130.26],
#         "may": [753.14, 951.93, 74.50, 130.26, 130.26, 130.26],
#         "jun": [794.14, 951.93, 74.50, 130.26, 130.26, 130.26],
#         "jul": [125.14, 951.93, 74.50, 130.26, 130.26, 130.26],
#         "aug": [974.14, 951.93, 74.50, 130.26, 130.26, 130.26],
#         "sep": [372.14, 951.93, 74.50, 130.26, 130.26, 130.26],
#         "oct": [278.14, 951.93, 74.50, 130.26, 130.26, 130.26],
#         "nov": [384.14, 951.93, 74.50, 130.26, 130.26, 130.26],
#         "dec": [709.14, 951.93, 74.50, 130.26, 130.26, 130.26]
#     }
# }