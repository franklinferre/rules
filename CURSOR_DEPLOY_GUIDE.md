
# 🚀 Cursor Deploy Guide - Implementação Completa

> **Guia definitivo para implementar as regras MDC e N8N AI Workflows em projetos Cursor**

## 🎯 Visão Geral

Este guia fornece um processo passo-a-passo para implementar o ecossistema completo de desenvolvimento assistido por IA em qualquer projeto Cursor, desde a configuração inicial até a integração avançada com N8N.

## ⚡ Quick Deploy (15 minutos)

### Pré-requisitos
- ✅ Cursor IDE instalado e atualizado
- ✅ Git configurado
- ✅ Node.js 18+ (para projetos web)
- ✅ Python 3.12+ (para projetos Python)

### 1️⃣ Clone do Repositório (2 min)

```bash
# Clone em diretório dedicado
git clone https://github.com/franklinferre/rules.git cursor-mdc-rules
cd cursor-mdc-rules

# Verifique a estrutura
tree -L 2
```

### 2️⃣ Configuração Global - User Rules (3 min)

Abra **Cursor → Settings → Rules** e cole:

```
Você é um agente sênior especializado em desenvolvimento assistido por IA.

PRIORIDADES: DRY → KISS → YAGNI → SOLID → Clean Architecture

EXECUÇÃO:
- PRD-First: Sempre comece com Product Requirements Document
- Patch-only: máx. 5 arquivos/ciclo, 200 linhas/arquivo, 500 linhas total
- Sempre espere "Go/No-Go" antes do próximo passo
- ASSUMPTION_REQUEST: Se faltar informação, liste opções + recomendação
- RISK_ALERT: Para secrets, migrações, auth, produção → pare e valide
- SCOPE_CHANGE: Mudanças de escopo → impacto + alternativas

QUALIDADE:
- Sem artefatos/dummies - tudo deve ter uso real
- Declare contrato I/O (REQUEST/RESPONSE) + critérios de aceite
- Sem testes, sem merge - cobertura ≥ 80% no módulo
- Consulte @docs e MCP antes de decisões

OSCAR FRAMEWORK:
- Objective: O que você quer alcançar
- Specification: Requisitos técnicos detalhados  
- Context: @files relevantes e documentação
- Acceptance: Critérios de aceite claros
- References: Links e documentação externa

OTIMIZAÇÃO:
- Respostas objetivas, diffs unificados
- Use @File/@Code/@Web/@Terminal/@Git estrategicamente
- Agent Mode para execução, ASK Mode para consulta
- Claude-4 Sonnet (diário), o3 (complexo), Gemini 2.5 Pro (grandes projetos)
```

### 3️⃣ Setup do Projeto (5 min)

```bash
# Navegue para seu projeto
cd /path/to/your-project

# Crie estrutura Cursor
mkdir -p .cursor/rules

# Copie arquivos de otimização
cp /path/to/cursor-mdc-rules/.cursorignore .
cp /path/to/cursor-mdc-rules/.cursorindexignore .
```

### 4️⃣ Seleção de Regras por Stack (3 min)

#### 🌐 Full-Stack Web (Next.js + TypeScript + Supabase)
```bash
cp cursor-mdc-rules/languages/typescript.mdc .cursor/rules/
cp cursor-mdc-rules/examples/fullstack.mdc .cursor/rules/
cp cursor-mdc-rules/examples/supabase-integration.mdc .cursor/rules/
cp cursor-mdc-rules/devops/containers.mdc .cursor/rules/
```

#### 🐍 Python API (FastAPI + PostgreSQL)
```bash
cp cursor-mdc-rules/languages/python.mdc .cursor/rules/
cp cursor-mdc-rules/devops/containers.mdc .cursor/rules/
cp cursor-mdc-rules/devops/monitoring.mdc .cursor/rules/
cp cursor-mdc-rules/devops/security.mdc .cursor/rules/
```

#### 🦀 Rust High-Performance
```bash
cp cursor-mdc-rules/languages/rust.mdc .cursor/rules/
cp cursor-mdc-rules/devops/monitoring.mdc .cursor/rules/
cp cursor-mdc-rules/devops/security.mdc .cursor/rules/
```

#### ☕ Java Enterprise (Spring Boot)
```bash
cp cursor-mdc-rules/languages/java.mdc .cursor/rules/
cp cursor-mdc-rules/devops/cicd.mdc .cursor/rules/
cp cursor-mdc-rules/devops/monitoring.mdc .cursor/rules/
```

#### 🐹 Go Microservices
```bash
cp cursor-mdc-rules/languages/go.mdc .cursor/rules/
cp cursor-mdc-rules/devops/containers.mdc .cursor/rules/
cp cursor-mdc-rules/devops/cloud.mdc .cursor/rules/
```

### 5️⃣ Validação da Configuração (2 min)

```bash
# Verifique estrutura final
tree .cursor/

# Teste no Cursor
# 1. Abra o projeto no Cursor
# 2. Pressione Ctrl+L (ou Cmd+L)
# 3. Digite: "Analise a configuração atual do projeto e sugira melhorias"
# 4. Verifique se as regras estão sendo aplicadas
```

## 🎯 Deploy por Tipo de Projeto

### 🌐 Projeto Web Full-Stack

#### Stack: Next.js 14 + TypeScript + Tailwind + Supabase

```bash
# 1. Configuração base
mkdir -p my-fullstack-app/.cursor/rules
cd my-fullstack-app

# 2. Regras específicas
cp cursor-mdc-rules/languages/typescript.mdc .cursor/rules/
cp cursor-mdc-rules/examples/fullstack.mdc .cursor/rules/
cp cursor-mdc-rules/examples/supabase-integration.mdc .cursor/rules/

# 3. DevOps
cp cursor-mdc-rules/devops/containers.mdc .cursor/rules/
cp cursor-mdc-rules/devops/cicd.mdc .cursor/rules/

# 4. Otimização
cp cursor-mdc-rules/.cursorignore .
cp cursor-mdc-rules/.cursorindexignore .

# 5. Inicialização
npx create-next-app@latest . --typescript --tailwind --eslint --app
```

#### Prompt de Inicialização
```
@File:PRD.md Crie um projeto Next.js 14 seguindo as regras MDC configuradas:

Objective: Aplicação web moderna com autenticação e dashboard
Specification: 
- Next.js 14 App Router
- TypeScript strict mode
- Tailwind CSS + shadcn/ui
- Supabase auth + database
- Testes com Vitest + Testing Library

Context: @typescript.mdc @fullstack.mdc @supabase-integration.mdc
Acceptance:
- ✅ Estrutura de pastas seguindo App Router
- ✅ Componentes tipados com interfaces
- ✅ Autenticação funcional
- ✅ Testes unitários ≥80% cobertura
- ✅ Docker setup para desenvolvimento

References: 
- https://nextjs.org/docs/app
- https://supabase.com/docs/guides/getting-started/quickstarts/nextjs
```

### 🐍 Projeto Python API

#### Stack: FastAPI + PostgreSQL + Redis + Docker

```bash
# 1. Configuração base
mkdir -p my-python-api/.cursor/rules
cd my-python-api

# 2. Regras específicas
cp cursor-mdc-rules/languages/python.mdc .cursor/rules/
cp cursor-mdc-rules/devops/containers.mdc .cursor/rules/
cp cursor-mdc-rules/devops/monitoring.mdc .cursor/rules/
cp cursor-mdc-rules/devops/security.mdc .cursor/rules/

# 3. Otimização
cp cursor-mdc-rules/.cursorignore .
cp cursor-mdc-rules/.cursorindexignore .

# 4. Estrutura inicial
mkdir -p {app,tests,docs,scripts}
touch {requirements.txt,Dockerfile,docker-compose.yml,.env.example}
```

#### Prompt de Inicialização
```
@File:PRD.md Crie uma API FastAPI seguindo as regras MDC configuradas:

Objective: API REST robusta com autenticação JWT e documentação automática
Specification:
- FastAPI 0.104+ com Pydantic v2
- PostgreSQL com SQLAlchemy 2.0
- Redis para cache e sessions
- JWT authentication
- OpenAPI/Swagger docs
- Docker multi-stage build

Context: @python.mdc @containers.mdc @monitoring.mdc @security.mdc
Acceptance:
- ✅ Estrutura modular (routers, models, services)
- ✅ Validação Pydantic em todos endpoints
- ✅ Middleware de logging e CORS
- ✅ Testes pytest ≥80% cobertura
- ✅ Docker Compose para desenvolvimento
- ✅ Health checks e métricas Prometheus

References:
- https://fastapi.tiangolo.com/
- https://docs.sqlalchemy.org/en/20/
```

### 🦀 Projeto Rust Performance

#### Stack: Actix-Web + PostgreSQL + Redis

```bash
# 1. Configuração base
mkdir -p my-rust-api/.cursor/rules
cd my-rust-api

# 2. Regras específicas
cp cursor-mdc-rules/languages/rust.mdc .cursor/rules/
cp cursor-mdc-rules/devops/monitoring.mdc .cursor/rules/
cp cursor-mdc-rules/devops/security.mdc .cursor/rules/

# 3. Otimização
cp cursor-mdc-rules/.cursorignore .
cp cursor-mdc-rules/.cursorindexignore .

# 4. Inicialização Cargo
cargo init --name my-rust-api
```

#### Prompt de Inicialização
```
@File:PRD.md Crie uma API Rust de alta performance seguindo as regras MDC:

Objective: API REST ultra-rápida com segurança máxima
Specification:
- Actix-Web 4.x com middleware customizado
- SQLx para PostgreSQL com compile-time checks
- Redis para cache distribuído
- JWT com validação rigorosa
- Logging estruturado com tracing
- Métricas Prometheus integradas

Context: @rust.mdc @monitoring.mdc @security.mdc
Acceptance:
- ✅ Arquitetura modular (handlers, services, models)
- ✅ Error handling com thiserror
- ✅ Validação de input com validator
- ✅ Testes unitários e integração ≥90%
- ✅ Benchmarks de performance
- ✅ Docker otimizado para produção

References:
- https://actix.rs/docs/
- https://docs.rs/sqlx/latest/sqlx/
```

## 🤖 Integração N8N AI Workflows

### Setup N8N Local (Opcional)

```bash
# 1. Docker Compose para N8N
cat > docker-compose.n8n.yml << EOF
version: '3.8'
services:
  n8n:
    image: n8nio/n8n:latest
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=admin123
      - N8N_HOST=localhost
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
    volumes:
      - n8n_data:/home/node/.n8n
    restart: unless-stopped

volumes:
  n8n_data:
EOF

# 2. Iniciar N8N
docker-compose -f docker-compose.n8n.yml up -d

# 3. Acesse http://localhost:5678
```

### Workflows Pré-configurados

#### 1. Code Review Automation
```json
{
  "name": "Cursor Code Review Agent",
  "description": "Automated code review with quality gates",
  "workflow": {
    "trigger": "GitHub Webhook",
    "steps": [
      "Extract PR files",
      "Run MDC rules validation", 
      "Generate review comments",
      "Post to GitHub PR"
    ]
  }
}
```

#### 2. Documentation Generator
```json
{
  "name": "Auto Documentation Generator",
  "description": "Generate docs from code changes",
  "workflow": {
    "trigger": "File changes",
    "steps": [
      "Analyze code structure",
      "Generate API docs",
      "Update README",
      "Commit documentation"
    ]
  }
}
```

#### 3. Test Generation Agent
```json
{
  "name": "Intelligent Test Generator",
  "description": "Generate tests based on code changes",
  "workflow": {
    "trigger": "New function/class",
    "steps": [
      "Analyze function signature",
      "Generate test cases",
      "Create mock data",
      "Validate test coverage"
    ]
  }
}
```

## 🔧 Configurações Avançadas

### Context Optimization

#### .cursorignore (Exclusão Completa)
```gitignore
# Build artifacts
**/node_modules/
**/dist/
**/build/
**/.next/
**/target/
**/__pycache__/
**/venv/
**/.venv/

# Logs e temporários
**/*.log
**/.cache/
**/.tmp/
**/tmp/

# Dados grandes
**/*.csv
**/*.json
data/
uploads/
**/*.pdf
**/*.zip
**/*.tar.gz

# Media files
**/*.jpg
**/*.jpeg
**/*.png
**/*.gif
**/*.mp4
**/*.avi
**/*.mov

# Secrets
**/.env
**/.env.*
!**/.env.example
**/*.key
**/*.pem
**/*.p12
**/secrets/

# Database
**/*.db
**/*.sqlite
**/*.sqlite3
**/migrations/
```

#### .cursorindexignore (Acesso Sob Demanda)
```gitignore
# Documentation (use @docs/file.md when needed)
docs/
design/
specs/
*.md
!README.md
!CHANGELOG.md

# Legacy code
legacy/
archived/
deprecated/
old/

# Large config files
**/webpack.config.js
**/rollup.config.js
**/vite.config.ts
config/large_config.json

# Generated files
**/*.generated.ts
**/*.generated.js
**/schema.prisma
**/schema.sql

# Test fixtures
**/fixtures/
**/mocks/
**/__fixtures__/
**/test-data/
```

### Model Selection Strategy

#### Por Tipo de Tarefa
```yaml
# Desenvolvimento diário
daily_tasks:
  model: "claude-4-sonnet"
  reason: "Melhor custo-benefício, boa qualidade"
  use_cases: ["refactoring", "bug fixes", "feature implementation"]

# Tarefas complexas
complex_tasks:
  model: "openai-o3"
  reason: "Raciocínio avançado, problemas complexos"
  use_cases: ["architecture design", "algorithm optimization", "debugging complex issues"]

# Projetos grandes
large_projects:
  model: "gemini-2.5-pro"
  reason: "1M tokens context, análise de codebase completa"
  use_cases: ["codebase analysis", "large refactoring", "migration projects"]

# Tarefas específicas
specialized_tasks:
  code_generation: "claude-4-sonnet"
  documentation: "gemini-2.5-pro"
  testing: "claude-4-sonnet"
  security_review: "openai-o3"
```

### @ References Best Practices

#### Estratégias por Contexto
```typescript
// 1. Feature Implementation
`
@File:PRD.md @File:src/types/user.ts @File:src/components/UserProfile.tsx

Implemente a funcionalidade de edição de perfil seguindo:
- Interface User já definida
- Componente UserProfile existente  
- Requisitos do PRD seção 3.2

OSCAR Framework aplicado com contexto específico.
`

// 2. Bug Investigation
`
@Terminal:npm run test @Git:git log --oneline -10 @File:src/utils/validation.ts

Investigue o bug de validação reportado:
- Logs de teste mostram falha
- Commits recentes podem ter introduzido
- Função de validação suspeita

Analise e proponha correção.
`

// 3. Code Review
`
@Code:src/api/users.ts:getUserById @File:tests/api/users.test.ts

Revise esta função considerando:
- Testes existentes cobrem casos edge?
- Error handling está adequado?
- Performance pode ser otimizada?

Sugira melhorias específicas.
`
```

## 🚨 Troubleshooting

### Problemas Comuns

#### 1. Regras não estão sendo aplicadas
```bash
# Verificar estrutura
ls -la .cursor/rules/

# Verificar sintaxe dos arquivos .mdc
head -20 .cursor/rules/*.mdc

# Reiniciar Cursor
# Ctrl+Shift+P → "Developer: Reload Window"
```

#### 2. Context muito grande
```bash
# Otimizar .cursorignore
echo "node_modules/" >> .cursorignore
echo "dist/" >> .cursorignore

# Usar .cursorindexignore para arquivos grandes
echo "docs/" >> .cursorindexignore
```

#### 3. Respostas inconsistentes
```bash
# Verificar User Rules
# Cursor → Settings → Rules
# Confirmar se OSCAR Framework está configurado

# Usar prompts mais específicos
# Sempre incluir Context e Acceptance criteria
```

### Logs e Debugging

#### Cursor Logs
```bash
# macOS
~/Library/Logs/Cursor/

# Windows  
%APPDATA%\Cursor\logs\

# Linux
~/.config/Cursor/logs/
```

#### Validação de Regras
```typescript
// Teste de regra específica
`
@typescript.mdc

Valide se esta função segue as regras TypeScript configuradas:

function processUser(data: any): any {
  return data.user?.name || "Unknown";
}

Identifique violações e sugira correções.
`
```

## 📊 Métricas e Monitoramento

### KPIs de Desenvolvimento

#### Velocidade
- **Lines of Code/Day**: Meta +200% vs baseline
- **Features Completed/Sprint**: Meta +150% vs baseline  
- **Bug Resolution Time**: Meta -60% vs baseline

#### Qualidade
- **Test Coverage**: Meta ≥80% em todos módulos
- **Code Review Time**: Meta -50% vs baseline
- **Production Bugs**: Meta -70% vs baseline

#### Satisfação
- **Developer Experience Score**: Meta ≥4.5/5
- **AI Assistance Effectiveness**: Meta ≥90% helpful responses
- **Time to First Success**: Meta <5 minutos para novos devs

### Dashboard de Métricas

```typescript
// Exemplo de coleta de métricas
interface DevelopmentMetrics {
  velocity: {
    linesPerDay: number;
    featuresPerSprint: number;
    bugResolutionHours: number;
  };
  quality: {
    testCoverage: number;
    codeReviewHours: number;
    productionBugs: number;
  };
  satisfaction: {
    developerScore: number;
    aiEffectiveness: number;
    timeToFirstSuccess: number;
  };
}
```

## 🎯 Próximos Passos

### Após Deploy Básico

1. **Semana 1**: Familiarização com regras e workflows
2. **Semana 2**: Customização para seu domínio específico
3. **Semana 3**: Integração com N8N workflows
4. **Semana 4**: Otimização baseada em métricas

### Evolução Contínua

1. **Mês 1**: Coleta de métricas baseline
2. **Mês 2**: Refinamento de regras baseado no uso
3. **Mês 3**: Implementação de workflows N8N avançados
4. **Mês 6**: Análise de ROI e expansão para outros projetos

---

## 🔗 Links de Referência

- **[CURSOR_USAGE_GUIDE.md](CURSOR_USAGE_GUIDE.md)** - Como usar cada regra específica
- **[docs/migration-guide.md](docs/migration-guide.md)** - Migração de projetos existentes
- **[docs/cursor-best-practices-integration.md](docs/cursor-best-practices-integration.md)** - Best practices detalhadas

---

> **🎉 Parabéns!** Você agora tem um ambiente de desenvolvimento assistido por IA de classe mundial. Para suporte, abra uma issue no repositório ou consulte a documentação completa.

**Tempo total de setup**: ~15 minutos  
**ROI esperado**: +300% velocidade, +31% qualidade  
**Próximo passo**: [CURSOR_USAGE_GUIDE.md](CURSOR_USAGE_GUIDE.md)
