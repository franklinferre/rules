# Cursor MDC Rules Repository

> **Repositório estruturado de regras Model-Driven Code (MDC) para Cursor IDE seguindo as práticas oficiais do Cursor Rules v2**

## 🎯 Visão Geral

Este repositório fornece um conjunto padronizado e modular de **16 regras MDC** para desenvolvimento assistido por IA no Cursor IDE, organizadas seguindo as melhores práticas de:

- **Cursor Rules v2** com arquivos `.mdc` e front-matter estruturado
- **10 Best Practices** integradas do "Mastering Cursor IDE" por Roberto Infante
- **Modularidade** com regras focadas e reutilizáveis por contexto
- **Economia de tokens** com ativação inteligente por padrões de arquivos
- **Consistência** entre diferentes tecnologias e projetos
- **Referências cruzadas** entre regras relacionadas
- **Prompt Engineering** com framework OSCAR e padrões estruturados
- **Context Optimization** com estratégias avançadas de indexação

## 📁 Estrutura do Repositório

```
cursor-mdc-rules/
├── .cursor/rules/           # 16 Regras Project Rules v2 (.mdc)
│   ├── 00-core-guardrails.mdc          # Controles fundamentais
│   ├── 05-cursor-best-practices.mdc    # 10 Best Practices integradas
│   ├── 10-gates-system.mdc             # Sistema de qualidade G1-G5
│   ├── 15-prompt-engineering.mdc       # Framework OSCAR avançado
│   ├── 20-io-contracts.mdc             # Contratos REQUEST/RESPONSE
│   ├── 25-context-optimization.mdc     # Otimização de contexto e tokens
│   ├── 30-testing.mdc                  # Estratégias de teste
│   ├── 40-security.mdc                 # Requisitos de segurança
│   ├── 50-frontend-standards.mdc       # TypeScript/React/Next.js
│   ├── 51-python-fastapi.mdc           # Python/FastAPI/Clean Architecture
│   ├── 60-docker-compose.mdc           # Containerização e Docker
│   ├── 70-database-standards.mdc       # Padrões de banco de dados
│   ├── 71-traefik-proxy.mdc           # Proxy reverso Traefik
│   ├── 72-memory-optimization.mdc      # Otimização de memória
│   ├── 73-rule-authoring.mdc          # Meta-práticas para regras MDC
│   └── 74-fullstack-patterns.mdc      # Arquiteturas full-stack
├── core/                    # Regras base e globais
│   ├── global-standards.md             # Padrões globais de desenvolvimento
│   ├── naming-conventions.md           # Convenções de nomenclatura
│   └── error-handling.md               # Tratamento de erros padronizado
├── docs/                    # Documentação completa
│   ├── cursor-best-practices-integration.md  # Guia das 10 Best Practices
│   ├── user-rules-guide.md                   # Configuração de regras globais
│   ├── project-rules-guide.md                # Uso de regras específicas
│   └── migration-guide.md                    # Migração de regras antigas
├── templates/               # Templates para novas regras
│   ├── language-template.mdc           # Template para linguagens
│   ├── api-template.mdc                # Template para APIs
│   └── devops-template.mdc             # Template para DevOps
├── languages/               # Regras específicas por linguagem (futuro)
├── devops/                  # Regras de DevOps e infraestrutura (futuro)
└── examples/                # Exemplos de uso (futuro)
```

## 📋 Catálogo Completo das 16 Regras MDC

### 🛡️ Regras Fundamentais (Always Apply)

| Regra | Nome | Descrição | Ativação |
|-------|------|-----------|----------|
| **00** | **Core Guardrails** | Controles fundamentais: execução step-by-step, patch-only limits, tratamento de assumptions, alertas de risco | `alwaysApply: true` |
| **40** | **Security** | Requisitos de segurança básicos: autenticação, autorização, proteção de dados | `alwaysApply: true` |

### 🎯 Regras de Produtividade e Best Practices

| Regra | Nome | Descrição | Ativação |
|-------|------|-----------|----------|
| **05** | **Cursor Best Practices** | 10 Best Practices integradas: PRD generation, agent modes, model selection, references, desenvolvimento iterativo | Auto por contexto |
| **10** | **Gates System** | Sistema de qualidade G1-G5 para controle de qualidade e pontos de decisão | Por solicitação |
| **15** | **Prompt Engineering** | Técnicas avançadas de prompt engineering: framework OSCAR, especificações detalhadas, gerenciamento de contexto | Manual (`@prompt-engineering`) |
| **25** | **Context Optimization** | Otimização de contexto e indexação: ignore files, estratégias de referência, gerenciamento de tokens | Manual (`@context-optimization`) |

### 🔧 Regras de Desenvolvimento

| Regra | Nome | Descrição | Ativação |
|-------|------|-----------|----------|
| **20** | **I/O Contracts** | Contratos obrigatórios REQUEST/RESPONSE para todas as operações | Por solicitação |
| **30** | **Testing** | Estratégia de testes e requisitos de cobertura (unit/integration/e2e) | `**/*tests/**` |
| **73** | **Rule Authoring** | Meta-práticas e padrões para criação de regras MDC efetivas | `**/*.mdc`, `**/rules/**` |

### 💻 Regras de Tecnologia Específica

| Regra | Nome | Descrição | Ativação |
|-------|------|-----------|----------|
| **50** | **Frontend Standards** | Padrões para TypeScript, React, Next.js e Tailwind CSS | `**/*.tsx` |
| **51** | **Python FastAPI** | Padrões Python e FastAPI seguindo Clean Architecture e DDD | `**/*.py` |
| **60** | **Docker Compose** | Padrões de Docker e containerização com multi-stage builds e security hardening | `Dockerfile*`, `docker-compose*.yml` |

### 🗄️ Regras de Infraestrutura e Performance

| Regra | Nome | Descrição | Ativação |
|-------|------|-----------|----------|
| **70** | **Database Standards** | Padrões abrangentes para PostgreSQL, MySQL, SQLite, MongoDB e Supabase com otimização de performance | `**/*.sql`, `**/migrations/**`, `**/models/**` |
| **71** | **Traefik Proxy** | Configuração de proxy reverso Traefik com Docker, terminação SSL e load balancing | `**/traefik/**`, `**/*.toml` |
| **72** | **Memory Optimization** | Gerenciamento de memória, estratégias de cache e técnicas de otimização de performance | `**/*.py`, `**/*.js`, `**/*.ts`, `**/cache/**` |
| **74** | **Full-Stack Patterns** | Arquiteturas full-stack modernas, princípios SOLID e melhores práticas de CI/CD | `**/src/**`, `**/api/**`, `**/frontend/**`, `**/backend/**` |

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
cp .cursor/rules/05-cursor-best-practices.mdc your-project/.cursor/rules/
cp .cursor/rules/50-frontend-standards.mdc your-project/.cursor/rules/
cp .cursor/rules/30-testing.mdc your-project/.cursor/rules/

# Para projeto Python + FastAPI
cp .cursor/rules/00-core-guardrails.mdc your-project/.cursor/rules/
cp .cursor/rules/05-cursor-best-practices.mdc your-project/.cursor/rules/
cp .cursor/rules/51-python-fastapi.mdc your-project/.cursor/rules/
cp .cursor/rules/30-testing.mdc your-project/.cursor/rules/

# Para projeto Full-Stack com Database
cp .cursor/rules/00-core-guardrails.mdc your-project/.cursor/rules/
cp .cursor/rules/70-database-standards.mdc your-project/.cursor/rules/
cp .cursor/rules/74-fullstack-patterns.mdc your-project/.cursor/rules/
cp .cursor/rules/72-memory-optimization.mdc your-project/.cursor/rules/
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
**/.next/
**/__pycache__/

# Secrets and sensitive data
**/.env
**/.env.*
**/*.key
**/*.pem
**/secrets/

# Large data and media files
**/*.csv
**/*.pdf
**/*.jpg
**/*.png
**/*.mp4
**/*.zip
**/*.tar.gz

# Database files
**/*.db
**/*.sqlite
**/dumps/
```

**`.cursorindexignore`** (acesso sob demanda):
```
# Documentation (reference with @docs/file.md when needed)
docs/
design/
specs/
README.md

# Legacy and archived code
legacy/
archived/
deprecated/
old/

# Large configuration files
config/large_config.json
**/webpack.config.js
**/rollup.config.js
**/vite.config.ts

# Test fixtures and mocks
**/fixtures/
**/mocks/
**/test-data/
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
1. **G1 - Planning**: Validação de requisitos e PRD
2. **G2 - Design**: Arquitetura e ADRs (Architecture Decision Records)
3. **G3 - Coding**: Implementação com testes unitários
4. **G4 - Integration**: Testes de integração e performance
5. **G5 - Release**: Segurança, deployment e monitoramento

### Protocolos Obrigatórios
- **ASSUMPTION_REQUEST**: Para ambiguidades e dados faltantes
- **RISK_ALERT**: Para operações sensíveis (secrets, migrations, auth)
- **SCOPE_CHANGE**: Para mudanças de escopo com análise de impacto

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

## 🆕 Novas Funcionalidades (Regras 70-74)

### 🗄️ Database Standards (Regra 70)
- **PostgreSQL, MySQL, SQLite**: Otimizações específicas por engine
- **MongoDB**: Padrões NoSQL e agregações
- **Supabase**: Integração com RLS e Edge Functions
- **Performance**: Indexação, query optimization, connection pooling

### 🌐 Traefik Proxy (Regra 71)
- **Docker Integration**: Configuração automática com labels
- **SSL Termination**: Let's Encrypt e certificados customizados
- **Load Balancing**: Algoritmos e health checks
- **Middleware**: Rate limiting, auth, compression

### ⚡ Memory Optimization (Regra 72)
- **Caching Strategies**: Redis, in-memory, CDN
- **Memory Profiling**: Ferramentas por linguagem
- **Garbage Collection**: Otimizações específicas
- **Performance Monitoring**: Métricas e alertas

### 📝 Rule Authoring (Regra 73)
- **Meta-practices**: Como criar regras efetivas
- **Front-matter Standards**: Estrutura obrigatória
- **Testing Rules**: Validação em projetos reais
- **Documentation**: Padrões de documentação

### 🏗️ Full-Stack Patterns (Regra 74)
- **SOLID Principles**: Aplicação prática
- **Clean Architecture**: Camadas e dependências
- **CI/CD Pipelines**: GitHub Actions, GitLab CI
- **Monitoring**: Observabilidade e alertas

## 📊 Estatísticas do Repositório

- **16 Regras MDC** ativas e testadas
- **4 Documentos** de guia e migração
- **3 Templates** para criação de novas regras
- **Cobertura**: Frontend, Backend, DevOps, Database, Performance
- **Compatibilidade**: Cursor Rules v2 completa
- **Última atualização**: Setembro 2025

## 📚 Documentação

- [**Cursor Best Practices Integration**](docs/cursor-best-practices-integration.md) - Guia completo das 10 melhores práticas integradas
- [**User Rules Guide**](docs/user-rules-guide.md) - Como configurar regras globais no Cursor
- [**Project Rules Guide**](docs/project-rules-guide.md) - Como usar regras específicas por projeto
- [**Migration Guide**](docs/migration-guide.md) - Migração de regras antigas para v2

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
- **Seguir** padrões de nomenclatura estabelecidos

## 🔮 Roadmap

### Próximas Regras Planejadas
- **75-supabase-integration.mdc** - Integração oficial Supabase
- **76-lovable-integration.mdc** - Integração com Lovable platform
- **80-observability.mdc** - Monitoramento e observabilidade
- **90-troubleshooting.mdc** - Debugging e resolução de problemas

### Melhorias Futuras
- Exemplos práticos por tecnologia
- Integração com mais IDEs
- Templates específicos por framework
- Validação automática de regras

## 📄 Licença

MIT License - veja [LICENSE](LICENSE) para detalhes.

## 🔗 Links Úteis

- [Cursor Rules Documentation](https://docs.cursor.com/en/context/rules)
- [Cursor Ignore Files](https://docs.cursor.com/en/context/ignore-files)
- [Model Context Protocol](https://docs.cursor.com/en/context/mcp)
- [CursorRules.org](https://cursorrules.org) - Comunidade de regras
- [Mastering Cursor IDE](https://www.cursor.com/blog) - Blog oficial

---

> **Versão**: 2.0.0  
> **Regras Ativas**: 16 (00-74)  
> **Última atualização**: 12 de Setembro de 2025  
> **Compatibilidade**: Cursor Rules v2  
> **Status**: ✅ Produção

**⚠️ Nota**: Para acessar repositórios privados, certifique-se de conceder as permissões necessárias através do [GitHub App](https://github.com/apps/abacusai/installations/select_target).
