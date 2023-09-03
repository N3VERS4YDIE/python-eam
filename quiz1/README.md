# Quiz 1

## Requirements

**Do not use:** anything that has not been covered until now, such as lists, tuples, dictionaries, other data structures, classes, objects, exception handling, and errors, etc.

**Use:** the statements seen so far, such as strings, loops, conditionals, etc.

## 1. Ticket Cost Calculation

Build an algorithm that allows calculating and displaying the cost of a ticket once the type of ticket and the number of tickets to be purchased are entered. Assume that a person can buy one or more tickets of a single and different type.

| Ticket   | Criteria                                                                                                                                                                                                                  |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VIP      | Ticket price is $80. If the person is underage, they receive a 20% discount.                                                                                                                                              |
| Platinum | Ticket price is $50. If 5 or fewer Platinum tickets are purchased, there is no discount; if 6 to ten Platinum tickets are purchased, there is a 5% discount; for more than ten Platinum tickets, there is a 10% discount. |
| General  | Ticket price is $25.                                                                                                                                                                                                      |

**The algorithm should print:** the total number of tickets the user bought, the total cost of the tickets, and the amount of the discount.

## 2. Digit-to-Word Conversion

Write an algorithm that asks the user for a positive integer and writes it with the names of its digits.

**Input:** `352108`

**Output:** `three-five-two-one-zero-eight`

**Note:** You should validate the input number to ensure it is an integer and greater than or equal to zero.

## 3. Finding the Largest Digit

Ask the user for an integer greater than or equal to 10 (validate the input) and determine the largest digit in it and its position.

**Input:** `458128`

**Output:** `Largest digit is 8, position 3`

**Note:** In case of the largest digit being repeated, select the first occurrence.
