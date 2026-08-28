# ADR-001 — Arquitetura local-first

## Status

Aceita para os protótipos públicos.

## Contexto

Projetos demonstrativos precisam funcionar sem infraestrutura corporativa, nuvem ou rede industrial.

## Decisão

Usar execução local, Python e SQLite nos primeiros módulos.

## Consequências

- instalação simples;
- boa portabilidade;
- menor custo operacional;
- limites de escala e concorrência;
- necessidade futura de migração quando o volume exigir.
