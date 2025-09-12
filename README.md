
# Cursor MDC Rules Repository

> **Repositório estruturado de regras Model-Driven Code (MDC) para Cursor IDE seguindo as práticas oficiais do Cursor Rules v2**

## 🎯 Visão Geral

Este repositório fornece um conjunto padronizado e modular de regras MDC para desenvolvimento assistido por IA no Cursor IDE, organizadas seguindo as melhores práticas de:

- **Cursor Rules v2** com arquivos `.mdc` e front-matter
- **10 Best Practices** integradas do "Mastering Cursor IDE" por Roberto Infante
- **Modularidade** com regras focadas e reutilizáveis
- **Economia de tokens** com regras específicas por contexto
- **Consistência** entre diferentes tecnologias e projetos
- **Referências cruzadas** entre regras relacionadas
- **Prompt Engineering** com framework OSCAR e padrões estruturados
- **Context Optimization** com estratégias avançadas de indexação

## 📁 Estrutura do Repositório

```
cursor-mdc-rules/
├── .cursor/rules/           # Regras Project Rules v2 (.mdc)
│   ├── 00-core-guardrails.mdc
│   ├── 05-cursor-best-practices.mdc  # NEW: 10 Best Practices
│   ├── 10-gates-system.mdc
│   ├── 15-prompt-engineering.mdc     # NEW: OSCAR Framework
│   ├── 20-io-contracts.mdc
│   ├── 25-context-optimization.mdc   # NEW: Indexing & References
│   ├── 30-testing.mdc
│   ├── 40-security.mdc
│   └── ...
├── core/                    # Regras base e globais
│   ├── global-standards.md
│   ├── naming-conventions.md
│   └── error-handling.md
├── languages/               # Regras específicas por linguagem
│   ├── typescript-react/
│   ├── python-fastapi/
│   └── ...
├── devops/                  # Regras de DevOps e infraestrutura
│   ├── docker/
│   ├── kubernetes/
│   └── cicd/
├── templates/               # Templates para novas regras
│   ├── language-template.mdc
│   ├── api-template.mdc
│   └── devops-template.mdc
├── docs/                    # Documentação
│   ├── user-rules-guide.md
│   ├── project-rules-guide.md
│   └── migration-guide.md
└── examples/                # Exemplos de uso
    ├── nextjs-project/
    ├── fastapi-project/
    └── fullstack-project/
```

## 🚀 Quick Start

### 1. User Rules (Globais)

Cole este conteúdo em **Cursor Settings → Rules** (texto puro):

```
Você é um agente sênior. Prioridades: DRY → KISS → YAGNI → SOLID → DDD/Clean.

Execução:
- Faça apenas o próximo passo e espere "Go/No-Go".
- Patch-only: máx. 5 arquivos por ciclo, 200 linhas/arquivo, 500 linhas no total.
- Nunca presuma: se faltar dado, dispare ASSUMPTION_REQUEST com opções e recomendação.
- RISCO: se envolver secrets, migrações, deleção em massa, auth, config de produção → pare e peça validação (RISK_ALERT).
- Qualquer trabalho fora do escopo atual → SCOPE_CHANGE com impacto e alternativas.

Qualidade:
- Sem artefatos/dummies. Tudo precisa ter uso real.
- Cada mudança deve declarar contrato I/O (REQUEST/RESPONSE) + critérios de aceite resumidos.
- Sem testes, sem merge. Cobertura alvo ≥ 80% no módulo tocado.

Operação:
- Consulte MCP/Context e docs relevantes antes de decisões.
- Optimize tokens: respostas objetivas, diffs unificados, sem contexto inútil.
```

### 2. Project Rules (Específicas do Projeto)

Copie os arquivos `.mdc` da pasta `.cursor/rules/` para o seu projeto:

```bash
# Para projeto Next.js + TypeScript
cp .cursor/rules/00-core-guardrails.mdc your-project/.cursor/rules/
cp .cursor/rules/50-frontend-standards.mdc your-project/.cursor/rules/
cp .cursor/rules/30-testing.mdc your-project/.cursor/rules/

# Para projeto Python + FastAPI
cp .cursor/rules/00-core-guardrails.mdc your-project/.cursor/rules/
cp .cursor/rules/51-python-fastapi.mdc your-project/.cursor/rules/
cp .cursor/rules/30-testing.mdc your-project/.cursor/rules/
```

### 3. Context Optimization

Configure arquivos de ignore para otimizar tokens e performance:

**`.cursorignore`** (exclusão completa):
```
# Build artifacts and dependencies
**/node_modules/
**/venv/
**/dist/
**/build/

# Secrets and sensitive data
**/.env
**/.env.*
**/*.key
**/*.pem

# Large data and media files
**/*.csv
**/*.pdf
**/*.jpg
**/*.mp4
**/*.zip
```

**`.cursorindexignore`** (acesso sob demanda):
```
# Documentation (reference with @docs/file.md when needed)
docs/
design/
specs/

# Legacy and archived code
legacy/
archived/
deprecated/

# Large configuration files
config/large_config.json
**/webpack.config.js
```

## 🚀 Cursor Best Practices Integradas

### 1. PRD-First Development
- **Sempre comece com um PRD**: Use Cursor Agent para gerar Product Requirements Document
- **Salve como referência**: `instructions.md` ou `PRD.md` para uso com @File
- **Prompt estruturado**: Inclua propósito, user stories, features, tech stack

### 2. Agent Mode Strategy
- **AGENT Mode**: Para execução autônoma (implementar, refatorar, testar)
- **ASK Mode**: Para consulta e planejamento (somente leitura, sem modificações)
- **Decisão**: "Cursor, faça isso" → AGENT | "Cursor, me explique" → ASK

### 3. Model Selection
- **Top-tier**: Claude-4 Sonnet, OpenAI o3, Gemini 2.5 Pro para tarefas complexas
- **Context length**: Gemini 2.5 Pro (1M tokens) para projetos grandes
- **Cost optimization**: Claude-4 Sonnet para uso diário (melhor custo-benefício)

### 4. @ References Mastery
- **@File/@Files**: Incluir conteúdo de arquivos nos prompts
- **@Code**: Referenciar snippets específicos ou símbolos
- **@Web**: Buscar informações em tempo real
- **@Terminal**: Incluir logs e outputs de runtime
- **@Git**: Referenciar histórico e commits

### 5. OSCAR Prompt Framework
- **O**bjective: O que você quer alcançar
- **S**pecification: Requisitos técnicos detalhados
- **C**ontext: @files relevantes e documentação
- **A**cceptance: Critérios de aceite claros
- **R**eferences: Links e documentação externa

### 6. Quality Triad
- **Logging**: Sempre inclua logs para observabilidade
- **Testing**: Testes unitários antes de prosseguir (≥80% cobertura)
- **Documentation**: README, docstrings, documentação de API

### 7. Iterative Refinement
- **3-Pass Method**: Estrutura/Lógica → Qualidade/Padrões → Polish/Documentação
- **Feedback loops**: Revisão imediata, análise estruturada, refinamento
- **Progressive disclosure**: Comece simples, adicione complexidade iterativamente

## 📋 Tipos de Regras

### Always Apply
Regras sempre ativas em qualquer contexto:
- `00-core-guardrails.mdc` - Controles fundamentais
- `05-cursor-best-practices.mdc` - 10 Best Practices do Cursor IDE
- `40-security.mdc` - Requisitos de segurança básicos

### Auto Attached
Regras ativadas automaticamente por padrões de arquivos:
- `50-frontend-standards.mdc` - Para `**/*.tsx`, `**/app/**`
- `51-python-fastapi.mdc` - Para `**/*.py`
- `60-docker-compose.mdc` - Para `Dockerfile*`, `docker-compose*.yml`

### Agent Requested
Regras incluídas quando o agente detecta contexto relevante:
- `10-gates-system.mdc` - Para planejamento e ADRs
- `80-observability.mdc` - Para monitoramento e logs

### Manual
Regras ativadas explicitamente com `@rule-name`:
- `15-prompt-engineering.mdc` - Com `@prompt-engineering`
- `20-io-contracts.mdc` - Com `@io-contracts`
- `25-context-optimization.mdc` - Com `@context-optimization`
- `90-troubleshooting.mdc` - Com `@troubleshooting`

## 🔗 Sistema de Referências

As regras usam um sistema de referências cruzadas:

```markdown
<!-- Referência a outra regra -->
@ref:core-guardrails#patch-only

<!-- Referência a documentação externa -->
@docs:https://docs.cursor.com/en/context/rules

<!-- Referência a template -->
@template:language-template.mdc
```

## 🎨 Padrões de Nomenclatura

### Arquivos de Regras
- **Prefixo numérico**: `00-`, `10-`, `20-` para ordem de carregamento
- **Nome descritivo**: `core-guardrails`, `frontend-standards`
- **Extensão**: `.mdc` para Project Rules

### Identificadores
- **PascalCase**: Classes, Interfaces, Componentes React
- **camelCase**: Variáveis, funções, métodos
- **kebab-case**: Arquivos, diretórios, URLs
- **UPPER_SNAKE_CASE**: Constantes, environment variables

## 🛡️ Controles de Qualidade

### Gates System (G1-G5)
1. **G1 - Planning**: Validação de requisitos
2. **G2 - Design**: Arquitetura e ADRs
3. **G3 - Coding**: Implementação com testes
4. **G4 - Integration**: Testes de integração
5. **G5 - Release**: Segurança e deployment

### Protocolos Obrigatórios
- **ASSUMPTION_REQUEST**: Para ambiguidades
- **RISK_ALERT**: Para operações sensíveis
- **SCOPE_CHANGE**: Para mudanças de escopo

## 📚 Documentação

- [Cursor Best Practices Integration](docs/cursor-best-practices-integration.md) - **NOVO**: Guia completo das 10 melhores práticas integradas
- [User Rules Guide](docs/user-rules-guide.md) - Como configurar regras globais
- [Project Rules Guide](docs/project-rules-guide.md) - Como usar regras específicas
- [Migration Guide](docs/migration-guide.md) - Migração de regras antigas
- [Templates Guide](templates/README.md) - Como criar novas regras

## 🤝 Contribuição

1. **Fork** este repositório
2. **Crie** uma branch para sua feature: `git checkout -b feature/nova-regra`
3. **Siga** os templates em `templates/`
4. **Teste** suas regras em projetos reais
5. **Submeta** um Pull Request

### Diretrizes para Contribuição

- Regras devem ser **focadas** (< 500 linhas)
- **Sempre** incluir front-matter com `description` e `globs`
- **Testar** com projetos reais antes de submeter
- **Documentar** exemplos de uso
- **Referenciar** fontes oficiais quando aplicável

## 📄 Licença

MIT License - veja [LICENSE](LICENSE) para detalhes.

## 🔗 Links Úteis

- [Cursor Rules Documentation](https://docs.cursor.com/en/context/rules)
- [Cursor Ignore Files](https://docs.cursor.com/en/context/ignore-files)
- [Model Context Protocol](https://docs.cursor.com/en/context/mcp)
- [CursorRules.org](https://cursorrules.org) - Comunidade de regras

---

> **Versão**: 1.0.0  
> **Última atualização**: Setembro 2025  
> **Compatibilidade**: Cursor Rules v2
