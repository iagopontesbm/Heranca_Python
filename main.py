import hr
import employees
import productivity

# Criado empregados
manager = employees.Manager(1, 'Iago Pontes', 3000)
secretary = employees.Secretary(2, 'John Smith', 1500)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(4, 'Jane Doe', 40, 15)
temporary_secretary = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)

# Gerando lista de empregados
company_employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]

# Instancia Produtividade
productivity_system = productivity.ProductivitySystem()
productivity_system.track(company_employees, 40)

# Instancia Horas
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(company_employees)
