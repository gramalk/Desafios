if horas_trabalhadas > 40:
    horas_extras = horas_trabalhadas - 40
    salario_baese = 40 * valor_hora
    adicional = horas_extras * valor_hora * 1.5
    salario_total = salario_base + adicional
else:
    salario_total = horas_trabalhadas * valor_hora