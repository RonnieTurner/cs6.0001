#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ronnieturner
"""

"""
Create initial values
"""
number_of_months = 0
current_savings = 0.0
r = .04

"""
Call user input and assign
"""
annual_salary = input("Enter your annual salary $")
annual_salary = float(annual_salary)
portion_saved = float(input("Enter the percent of your salary to save, as a decimal "))
dream_home = float(input("Enter the cost of your dream home $"))

"""
Calculate monthly rates
"""
monthly_salary = annual_salary / 12
portion_saved = monthly_salary * portion_saved
portion_down = dream_home * .25


"""
Loop until enough has been saved for down payment
"""

while (current_savings < portion_down):
    current_savings += current_savings * r / 12 + portion_saved
    number_of_months += 1

    
print(number_of_months)
