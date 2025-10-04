# 🔍 Análise Exploratória e Limpeza de Dados Meteorológicos

Este código realiza uma **análise exploratória completa** e **processamento de dados** meteorológicos para determinar as condições ideais para praticar atividades ao ar livre.

## 📊 O que este código faz:

### **1. Exploração Inicial dos Dados**
- Carrega dados meteorológicos do arquivo `tempo.csv`
- Analisa variáveis categóricas: **Aparência**, **Vento** e **Jogar**
- Examina variáveis numéricas: **Temperatura** e **Umidade**
- Gera visualizações para melhor compreensão dos dados

### **2. Tratamento de Dados Problemáticos**

#### 🔧 **Correções Aplicadas:**

**Aparência:**
- ✅ Substituição do valor inválido "menos" por "sol"

**Temperatura:**
- ✅ Identificação de valores fora do domínio esperado (-130°C a 130°C)
- ✅ Substituição dos valores extremos pela **mediana** (86°F)

**Umidade:**
- ✅ Tratamento de valores **faltantes (NAs)**
- ✅ Correção de valores fora da faixa padrão (0-100%)
- ✅ Preenchimento com a **mediana** dos dados válidos

**Vento:**
- ✅ Preenchimento de valores faltantes com "Falso"

## 📈 Resultados da Limpeza:

| Variável | Problema Resolvido | Método de Correção |
|----------|-------------------|-------------------|
| Aparência | Valor inválido "menos" | Substituição por "sol" |
| Temperatura | Valores extremos | Mediana (86°F) |
| Umidade | NAs e valores fora da faixa | Mediana dos dados válidos |
| Vento | Dados faltantes | Preenchimento com "Falso" |

## 🎯 Objetivo Final:
Criar um **dataset limpo e confiável** para análise preditiva da decisão de **jogar** ou não atividades ao ar livre baseada nas condições meteorológicas.
