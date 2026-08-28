# Arquitetura Integrada do Portfólio Industrial

## Visão

A PIO — Plataforma Inteligente Operacional — organiza conceitualmente os projetos demonstrativos deste portfólio.

Todos os módulos utilizam dados sintéticos e são independentes de sistemas industriais reais.

## Ecossistema

A arquitetura demonstrativa é organizada em quatro componentes:

### Fontes sintéticas

- cenários genéricos e reproduzíveis;
- sinais sem nomes, endereços ou dados proprietários.

### Collector

- aquisição e validação;
- qualidade e rastreabilidade;
- persistência em banco independente;
- logs, checkpoint, recuperação e exportação.

### Operação & Analytics

- regras operacionais;
- reconstrução e validade de eventos;
- cálculos e indicadores;
- histórico, recorrência e diagnóstico.

### Aplicações

- Industrial Microstop Monitor;
- Industrial Hourly Production Dashboard;
- relatórios, alertas e futuros módulos.

## Relação entre os módulos

Nesta fase, a integração é arquitetural e ocorre por contratos documentados. O Collector permanece independente das aplicações. A camada Operação & Analytics consome o banco de coleta e fornece resultados interpretados aos consumidores.

Cada aplicação mantém responsabilidade limitada ao problema que apresenta. Nenhuma aplicação deve escrever em equipamentos industriais ou depender de infraestrutura corporativa real.

## Princípios

- modularidade;
- rastreabilidade;
- separação entre dado bruto, regra e apresentação;
- reprodutibilidade;
- mudanças incrementais e reversíveis;
- utilização exclusiva de dados sintéticos.

## Segurança

O portfólio não deve conter:

- credenciais;
- endereços ou rotas industriais reais;
- tags ou nomes reais de equipamentos;
- programas ou backups de PLC;
- bancos corporativos;
- telas ou documentos proprietários;
- informações de clientes;
- dados pessoais;
- dados reais de produção.

## Evolução

A arquitetura poderá incorporar aplicações demonstrativas de confiabilidade, condição de ativos, diagnóstico, alarmes, disponibilidade, recorrência e qualidade de dados.

## Objetivo

Demonstrar competências aplicadas em automação industrial, engenharia de dados, Python, SQLite, regras operacionais, testes automatizados, dashboards, segurança da informação e arquitetura modular.

A PIO apresentada neste portfólio não representa um sistema industrial pronto para implantação.
