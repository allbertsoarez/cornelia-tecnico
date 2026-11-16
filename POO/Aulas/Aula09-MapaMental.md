# MAPA MENTAL
Aqui está o mapa mental convertido para o formato `graph TD` (fluxograma hierárquico). 

Esta estrutura utiliza apenas recursos básicos e maduros do Mermaid, garantindo que a renderização seja **idêntica e sem erros** no GitHub, Obsidian, Notion ou qualquer outro visualizador.

```mermaid
graph TD
    A([Coleções Python]) --> B(Conceito)
    A --> C(Listas)
    A --> D(Dicionários)
    A --> E(Boas Práticas)

    B --> B1[Agrupar dados]
    B --> B2[Substituir variáveis únicas]

    C --> C1[Sintaxe com colchetes]
    C --> C2[Estruturas mutáveis]
    C --> C3[Método append]

    D --> D1[Sintaxe com chaves]
    D --> D2[Par chave e valor]
    D --> D3[Método get]

    E --> E1[Inicializar no __init__]
    E --> E2[Validar antes de inserir]
    E --> E3[Evitar IndexError]
```

### Por que este formato é mais seguro?
1. **Sem caracteres especiais no ID**: Os nós usam identificadores simples (ex: `C1`, `D2`), evitando conflitos de sintaxe.
2. **Hierarquia clara**: O uso de `-->` cria uma árvore visual que substitui perfeitamente a função de um mapa mental.
3. **Compatibilidade retroativa**: Funciona em versões do Mermaid.js de até 5 anos atrás, eliminando qualquer risco de "Parse error".

Se precisar ajustar algum termo ou adicionar mais um ramo a este gráfico, é só solicitar!
