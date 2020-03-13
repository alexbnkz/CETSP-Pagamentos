[![HitCount](http://hits.dwyl.com/learning-crawlers/CETSP-Pagamentos.svg)](http://hits.dwyl.com/learning-crawlers/CETSP-Pagamentos)

# CETSP Folha De Pagamentos
Extração de dados com Requests para listar pagamentos da CET - Companhia de Engenharia de Tráfego da cidade de São Paulo

## Modo de usar

Execute o arquivo run.py:

```bash
python run.py
```

## Resultado

**Schema**

- empresa: string
- mes: string
- ano: string
- nome: string
- cargo: string
- lotacao: string
- admissao: string
- nascimento: string
- vencimentos: string
- encargos: string
- beneficios: string
- outras_remuneracoes: string
- vinculo: string
- detalhe_vinculo: string
- liminar: string
- arquivo_id: string

**Dados**

```json
{
    "empresa": "CET",
    "mes": "1",
    "ano": "2020",
    "nome": "WALDEMAR DE A C CHRISTIANINI",
    "cargo": "GESTOR TRANSITO",
    "lotacao": "DEPTO DE PLAN CONTR OPERAC-MB",
    "admissao": "12/01/1976",
    "nascimento": "1950",
    "vencimentos": " R$16.363,25 ",
    "encargos": " R$6.178,17 ",
    "beneficios": " R$1.143,08 ",
    "outras_remuneracoes": " R$-   ",
    "vinculo": "CLT: contrato por tempo indeterminado",
    "detalhe_vinculo": "Concursado NO ocupante de cargo em comisso",
    "liminar": "-",
    "arquivo_id": "dc47d100-1217-4c61-8db5-29555f6e784d"
}
```