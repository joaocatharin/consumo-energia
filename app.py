print("===================================")
print("   CALCULADORA DE CONSUMO ELÉTRICO")
print("===================================")

aparelho = input("Nome do aparelho: ")
potencia = float(input("Potência do aparelho (W): "))
horas_dia = float(input("Tempo médio de uso diário (horas): "))

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo do custo estimado
valor_kwh = 0.75
custo_mensal = consumo_mensal * valor_kwh

print("\n===================================")
print("           RESULTADO")
print("===================================")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_mensal:.2f}/mês")
print("===================================")