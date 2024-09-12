"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

in_state_gift = 0

out_state_gift = 0

in_state_tuition = 30792

out_state_tuition = 47882

in_state_gift = in_state_tuition / 0.05

out_state_gift = out_state_tuition / 0.05

print(f'\nIn state gift amount: ${in_state_gift}\n')

print(f'Out of state gift amount: ${out_state_gift}')


