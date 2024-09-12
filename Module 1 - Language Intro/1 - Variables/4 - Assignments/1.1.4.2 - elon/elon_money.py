"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 1-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""

def compound(n, p, r):
    A = p * ((1 + (r / 100))**n)
    return A

ten_year_final = compound(10, 33000000000, 3.96)

twenty_year_final = compound(20, 33000000000, 4.32)

print(f'Final amount after 10 years: ${ten_year_final:.2f}')

print(f'Final amount after 20 years: ${twenty_year_final:.2f}')