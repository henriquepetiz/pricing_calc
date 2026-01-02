# pricing_calc

# Pricing Calculator

A Python script that calculates the final sale price of a product based on its cost price and pre-defined profit margins.

## Features

- Input validation for positive numbers (cost price > 0).
- Error handling for non-numeric inputs using try/except blocks.
- Dynamic profit margin calculation based on cost brackets.
- Formatted output for currency with two decimal places.

## Pricing Logic

The script applies different markup percentages based on the cost price:
- Under 10.00: 70% markup (Cost * 1.70)
- Between 10.00 and 29.99: 50% markup (Cost * 1.50)
- Between 30.00 and 49.99: 40% markup (Cost * 1.40)
- 50.00 and above: 30% markup (Cost * 1.30)

## How to Run

1. Clone the repository:
   git clone https://github.com/henriquepetiz/pricing_calc.git

2. Navigate to the folder:
   cd pricing_calc

3. Run the script:
   python main.py

## Usage Example

Input:
Enter cost price: 20.00

Output:
--> Sale price is: 30.00
