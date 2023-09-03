# Exam 1

## Requirements

**Do not use:** anything that has not been covered until now, such as lists, tuples, dictionaries, other data structures, classes, objects, exception handling, and errors, etc.

**Use:** the statements seen so far: strings, loops, conditionals, etc.

## 1. Rental Car Company Pricing

A company dedicated to car rental charges a fixed amount of $300 for the first 300 km of travel. For more than 300 km and up to 1000 km, an additional fee of $15 is charged for each kilometer exceeding 300 km. For more than 1000 km, an additional fee of $10 is charged for each kilometer exceeding 1000 km. The final price should include a 20% general sales tax, VAT. Design an algorithm to determine the amount to be paid for renting a vehicle, requesting the total kilometers traveled by the user (this data must be validated as an integer greater than or equal to 1). The algorithm should print the amount to be paid by the user without including VAT, the VAT amount, and the total amount.

## 2. Calculation of Mean and Standard Deviation

Write a routine that receives a list of n numbers separated by commas; then calculate the mean and standard deviation of these numbers using the following formulas:

$$
\mu = {1 \over n} \sum_{k=1}^{n} x_k
$$

$$
\sigma = \sqrt{{1 \over n} \sum_{k=1}^{n} x_k^2 - \mu^2}
$$

Display the results with an approximation of two decimal places.

### EXAMPLE

**Input:** `11, 12, 17, 17, 12, 19, 13, 12, 10`

**Output:** `mean=13.67; standard deviation=2.98`

## 3. Counting Even and Odd Digits

Develop an algorithm that asks the user to enter positive integers (this entry must be validated) until the user enters zero. It should report how many even and how many odd digits each number has. Report at the end the total count of even and odd digits counted.
