# Arquitetura de referência

## Objetivo

Definir uma arquitetura demonstrativa, local-first e rastreável para transformar sinais sintéticos em dados persistidos, eventos, indicadores e aplicações.

## Componentes

### 1. Fontes sintéticas

Geradores, arquivos de amostra e APIs locais representam sinais genéricos como ocupação, produção, falhas e estados. Nomes, identificadores e endereços são fictícios.

### 2. Collector

O Collector é independente das regras analíticas e das interfaces. Ele deve:

- configurar e validar fontes antes da aprovação;
- registrar instante, fonte, identificador, valor, qualidade e sequência;
- persistir amostras em banco novo e independente;
- manter logs, checkpoints e estado de recuperação;
- permitir backup, exportação e reprocessamento controlado;
- continuar funcional mesmo quando dashboards estiverem indisponíveis.

### 3. Persistência

SQLite é adequado aos protótipos locais. A escrita deve utilizar transações, índices, integridade referencial e política explícita de retenção. Dados brutos e resultados derivados devem permanecer distinguíveis.

### 4. Operação & Analytics

Essa camada consome dados persistidos pelo Collector e aplica:

- validações complementares de contexto;
- regras operacionais versionadas;
- reconstrução de eventos;
- critérios de validade e inconclusividade;
- indicadores e cálculo de perdas;
- histórico, recorrência e diagnóstico.

Cada resultado deve manter referência às amostras, à regra e à versão que o produziram.

### 5. Aplicações

Dashboards, relatórios e alertas consomem resultados da camada analítica. Eles não coletam sinais diretamente nem alteram dados brutos.

## Fluxo de dados

~~~mermaid
sequenceDiagram
    participant S as Fonte sintética
    participant C as Collector
    participant B as Banco independente
    participant A as Operação & Analytics
    participant U as Aplicação

    S->>C: amostra sintética
    C->>C: validação e qualidade
    C->>B: persistência + checkpoint
    A->>B: leitura incremental
    A->>B: evento ou indicador rastreável
    U->>B: consulta de resultados
    U-->>U: atualização visual
~~~

## Contrato mínimo da amostra

| Campo | Finalidade |
|---|---|
| **timestamp** | instante normalizado da leitura |
| **source** | origem sintética ou configurada |
| **signal_id** | identificador genérico do sinal |
| **value** | valor observado |
| **quality** | avaliação explícita de confiabilidade |
| **sequence** | ordenação e detecção de lacunas |
| **collector_version** | versão responsável pela coleta |

## Requisitos não funcionais

- recuperação segura após reinício;
- logs legíveis e auditáveis;
- configuração separada do código;
- integridade do banco;
- ausência de segredos no repositório;
- testes das regras críticas;
- identificação clara de versão;
- operação local sem descoberta automática de rede;
- nenhuma escrita em equipamento industrial.
