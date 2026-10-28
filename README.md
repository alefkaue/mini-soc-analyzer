# Mini SOC Analyzer

Exercício Python com eventos definidos no código: contagem, IPs únicos e regras simples de falhas de login e scans. Não é um SOC operacional.

**Área do portfólio:** [Cybersecurity](https://github.com/alefkaue#cybersecurity) · **Contexto:** Exercício de aprendizagem

## Conteúdo e tecnologias

**Linguagens identificadas:** Python.

O arquivo [`soc_analyzer.py`](soc_analyzer.py) contém eventos de exemplo e funções para contagem, IPs únicos, três falhas de login por IP e dois eventos de scan por IP.

## Executar

```console
python soc_analyzer.py
```

Python 3, sem integração de rede. O resultado deriva da lista definida no próprio script.

## Limites

Não ingere logs reais, não usa janela temporal e não comprova ataques. Os limiares são exercícios de contagem. Não há teste automatizado ou CI no snapshot analisado.
