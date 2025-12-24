def salary_calc(base_salary,addition):
    return 0.9*base_salary + addition


baseSal = float(input("Insert base salary"))
additn = float(input('Insert sal adittions'))

print(f'total calc sal is: ', salary_calc(baseSal,additn))