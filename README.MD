# ⚡ Calculadora de Consumo de Energia

Projeto desenvolvido em Python para calcular o consumo estimado de energia elétrica de aparelhos domésticos.

## 📋 Sobre o projeto

A **Calculadora de Consumo de Energia** permite que o usuário informe:

* 🔌 Nome do aparelho
* ⚡ Potência do aparelho em watts (W)
* ⏱️ Tempo médio de utilização diária em horas

Com essas informações, o programa calcula o consumo mensal estimado em **kWh/mês**.

Além disso, o projeto apresenta uma estimativa do custo mensal utilizando o valor de **R$ 0,75 por kWh**.

## 🧮 Fórmula utilizada

O consumo mensal é calculado através da fórmula:

```text
consumoMensal = (potencia × horasDia × 30) / 1000
```

Para calcular o custo:

```text
custoMensal = consumoMensal × valorKwh
```

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd consumo-energia
```

### 3. Execute o programa

```bash
python app.py
```

## 💻 Exemplo

```text
===================================
   CALCULADORA DE CONSUMO ELÉTRICO
===================================

Nome do aparelho: Geladeira
Potência do aparelho (W): 60
Tempo médio de uso diário (horas): 24

===================================
           RESULTADO
===================================
Aparelho: Geladeira
Consumo estimado: 43.20 kWh/mês
Custo estimado: R$ 32.40/mês
===================================
```

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 💻 Git
* 🐙 GitHub

## 📁 Estrutura do projeto

```text
consumo-energia/
├── app.py
└── README.md
```

## 🎯 Objetivo

Este projeto foi desenvolvido como atividade do curso técnico em Desenvolvimento de Sistemas, com o objetivo de praticar conceitos básicos de programação em Python, entrada de dados, cálculos matemáticos, formatação de resultados e publicação de projetos no GitHub.

## 👨‍💻 Autor

Projeto desenvolvido durante o curso técnico na ETEC em Desenvolvimento de sistemas.
