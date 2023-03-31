from EmbarqueTrabalhador import *

dropTable('FUNCIONARIOS')
dropTable('EMBARQUE')

createTableFuncionario()
createTableEmbarque()

insertFuncionario('Joao', 'Silva', datetime.date(1990, 1, 1), 1)
insertFuncionario('Maria', 'Lima', datetime.date(1995, 3, 5), 1)
insertFuncionario('Lucas', 'Souza', datetime.date(1986, 10, 24), 0)

insertEmbarque(datetime.date(2023, 4, 15), datetime.date(2023, 4, 25), 1)
insertEmbarque(datetime.date(2023, 4, 26), datetime.date(2023, 5, 2), 3)
insertEmbarque(datetime.date(2023, 4, 10), datetime.date(2023, 4, 14), 2)
