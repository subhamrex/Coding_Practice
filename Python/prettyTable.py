from prettytable import PrettyTable

mytable = PrettyTable(["Name","Role","Grade"])

mytable.add_row(["Adi","fragger","O"])
mytable.add_row(["Rex","fragger","A"])
mytable.add_row(["Indra","supporter","A"])

print(mytable)