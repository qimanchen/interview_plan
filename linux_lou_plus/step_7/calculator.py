#!/usr/bin/env python3

import sys

def need_revenue_money(initSalary, start_point=3500):
    return initSalary - start_point if initSalary > start_point else 0.00


def get_rate(salary, revenue_rate, delete_num):
    return salary * revenue_rate - delete_num


def main(initSalary):
    salary = need_revenue_money(initSalary)

    if salary > 80000:
        result = get_rate(salary, 0.45, 13505)
    elif salary > 55000 and salary <= 80000:
        result = get_rate(salary, 0.35, 5505)
    elif salary >35000 and salary <= 55000:
        result = get_rate(salary, 0.30, 2755)
    elif salary >9000 and salary <= 35000:
        result = get_rate(salary, 0.25, 1005)
    elif salary > 4500 and salary <= 9000:
        result = get_rate(salary, 0.20, 555)
    elif salary > 1500 and salary <= 4500:
        result = get_rate(salary, 0.10, 105)
    else:
        result = get_rate(salary, 0.03, 0)
    if result == 0:
		result = 0.00
    return result

	
if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Parameter Error")
        sys.exit(1)
    try:
        initSalary = int(sys.argv[1])
    except:
        print("Parameter Error")
        sys.exit(1)
    print(format(main(initSalary), ".2f"))
