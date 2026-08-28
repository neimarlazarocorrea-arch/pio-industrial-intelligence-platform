# ADR-002 — Separação entre Collector e Operação & Analytics

## Status

Aceita para a nova geração da arquitetura demonstrativa.

## Contexto

Versões anteriores aproximavam coleta, regras operacionais, persistência de eventos e dashboards. Esse acoplamento dificulta recuperação, testes, reprocessamento e evolução independente das aplicações.

## Decisão

Separar a arquitetura em:

1. **Collector independente**, responsável por fontes, qualidade inicial, persistência, logs, checkpoint, backup e exportação;
2. **Operação & Analytics**, responsável por regras versionadas, reconstrução de eventos, validade, indicadores, recorrência e diagnóstico;
3. **Aplicações**, responsáveis apenas pela experiência e apresentação do problema atendido.

A nova geração utiliza banco novo. Históricos anteriores não são conectados ao runtime e podem ser usados somente em análise forense ou testes offline controlados.

## Consequências

- menor acoplamento;
- recuperação e coleta independentes das interfaces;
- reprocessamento auditável;
- contratos de dados explícitos;
- maior esforço inicial de modelagem e versionamento;
- necessidade de compatibilidade controlada entre Collector e Analytics.
