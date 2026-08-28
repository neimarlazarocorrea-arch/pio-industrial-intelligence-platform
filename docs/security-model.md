# Modelo de segurança

## Objetivo

Evitar que um projeto demonstrativo vire um vetor para exposição de informações industriais ou para ações indevidas em redes de automação.

## Fronteiras

- repositório público: apenas dados sintéticos;
- execução local: sem descoberta automática de rede;
- conectores reais: fora do escopo;
- escrita em PLC: fora do escopo;
- credenciais: somente por variáveis locais não versionadas.

## Ameaças principais

| Ameaça | Controle |
|---|---|
| Publicação de IPs, tags ou nomes reais | validador de padrões e revisão humana |
| Credencial versionada | `.gitignore`, secret scanning e política de segurança |
| Banco real incluído | bloqueio de extensões de banco e revisão do histórico |
| Exemplo confundido com integração produtiva | avisos claros no README e documentação |
| Regra sem rastreabilidade | eventos com origem, versão e timestamp |

## Política de publicação

Antes de tornar qualquer módulo público:

1. revisar arquivos e histórico;
2. executar o validador;
3. procurar padrões sensíveis;
4. substituir qualquer referência por conteúdo sintético;
5. revisar imagens e anexos;
6. validar dependências;
7. obter aprovação do mantenedor.
