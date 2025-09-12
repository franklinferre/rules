
# Project Rules Guide

## O que são Project Rules

Project Rules são regras **específicas do projeto** que ficam no diretório `.cursor/rules/` do seu projeto. Elas usam o formato `.mdc` (Markdown with front-matter) e são ativadas baseado em contexto, padrões de arquivos, ou manualmente.

## Formato das Project Rules

### Estrutura Básica
```markdown
---
description: Descrição clara da regra
globs:
  - "**/*.tsx"
  - "**/components/**"
alwaysApply: false
---

# Conteúdo da Regra

Instruções específicas para o agente...
```

### Front-matter Obrigatório

#### description
- **Propósito**: Descreve o que a regra faz
- **Formato**: String concisa e clara
- **Exemplo**: `"Frontend standards for TypeScript, React, Next.js"`

#### globs
- **Propósito**: Padrões de arquivos que ativam a regra automaticamente
- **Formato**: Array de strings com padrões glob
- **Exemplos**:
  ```yaml
  globs:
    - "**/*.tsx"           # Todos arquivos .tsx
    - "**/components/**"   # Arquivos na pasta components
    - "Dockerfile*"        # Arquivos que começam com Dockerfile
  ```

#### alwaysApply
- **Propósito**: Se a regra deve estar sempre ativa
- **Valores**: `true` ou `false`
- **Uso**: `true` para regras fundamentais, `false` para contextuais

## Tipos de Ativação

### Always Apply (`alwaysApply: true`)
Regras sempre ativas, independente do contexto:

```markdown
---
description: Core guardrails and fundamental controls
globs:
alwaysApply: true
---

# Core Guardrails
- Execute apenas o próximo passo
- Máximo 5 arquivos por ciclo
- RISK_ALERT para operações sensíveis
```

**Quando usar**:
- Controles de segurança fundamentais
- Limites operacionais básicos
- Padrões que se aplicam a todo o projeto

### Auto Attached (`alwaysApply: false` + `globs`)
Regras ativadas automaticamente por padrões de arquivos:

```markdown
---
description: TypeScript and React standards
globs:
  - "**/*.tsx"
  - "**/*.ts"
  - "**/components/**"
alwaysApply: false
---

# TypeScript/React Standards
- Sempre usar interfaces para props
- PascalCase para componentes
- camelCase para funções
```

**Quando usar**:
- Padrões específicos de linguagem/framework
- Regras que só fazem sentido para certos tipos de arquivo
- Configurações específicas de ferramentas

### Agent Requested (sem `globs`, `alwaysApply: false`)
Regras incluídas quando o agente detecta contexto relevante:

```markdown
---
description: Gates system for quality control
globs:
alwaysApply: false
---

# Gates System
Sistema de controle de qualidade G1-G5...
```

**Quando usar**:
- Processos complexos (gates, workflows)
- Regras de arquitetura e design
- Padrões de observabilidade

### Manual (`@rule-name`)
Regras ativadas explicitamente pelo usuário:

```markdown
---
description: I/O contracts for structured operations
globs:
alwaysApply: false
---

# I/O Contracts
Contratos REQUEST/RESPONSE obrigatórios...
```

**Ativação**: Use `@io-contracts` no chat para ativar

**Quando usar**:
- Regras especializadas
- Processos que nem sempre são necessários
- Troubleshooting e debugging

## Organização de Arquivos

### Convenção de Nomenclatura
```
.cursor/rules/
├── 00-core-guardrails.mdc      # Always apply
├── 10-gates-system.mdc         # Agent requested
├── 20-io-contracts.mdc         # Manual
├── 30-testing.mdc              # Auto attached (tests)
├── 40-security.mdc             # Always apply
├── 50-frontend-standards.mdc   # Auto attached (frontend)
├── 51-python-fastapi.mdc       # Auto attached (Python)
├── 60-docker-compose.mdc       # Auto attached (Docker)
└── 90-troubleshooting.mdc      # Manual
```

### Prefixos Numéricos
- **00-09**: Regras fundamentais (always apply)
- **10-19**: Processos e workflows (agent requested)
- **20-29**: Contratos e protocolos (manual)
- **30-39**: Testing e qualidade (auto attached)
- **40-49**: Segurança (always apply)
- **50-59**: Frontend/linguagens (auto attached)
- **60-69**: DevOps/infraestrutura (auto attached)
- **70-89**: Ferramentas específicas (auto attached)
- **90-99**: Troubleshooting e debug (manual)

## Padrões Glob Comuns

### Por Linguagem
```yaml
# TypeScript/JavaScript
globs:
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.js"
  - "**/*.jsx"

# Python
globs:
  - "**/*.py"
  - "**/requirements*.txt"
  - "**/pyproject.toml"

# Go
globs:
  - "**/*.go"
  - "**/go.mod"
  - "**/go.sum"
```

### Por Framework
```yaml
# React/Next.js
globs:
  - "**/components/**"
  - "**/pages/**"
  - "**/app/**"
  - "**/*.tsx"

# FastAPI
globs:
  - "**/api/**"
  - "**/routers/**"
  - "**/models/**"
  - "**/*.py"
```

### Por Ferramenta
```yaml
# Docker
globs:
  - "Dockerfile*"
  - "**/docker/**"
  - "**/docker-compose*.yml"

# Kubernetes
globs:
  - "**/k8s/**"
  - "**/kubernetes/**"
  - "**/*.yaml"
  - "**/*.yml"

# Testing
globs:
  - "**/tests/**"
  - "**/*.test.*"
  - "**/*.spec.*"
```

## Boas Práticas

### Tamanho e Foco
- **Máximo 500 linhas** por arquivo de regra
- **Uma responsabilidade** por arquivo
- **Foco específico** em um domínio/tecnologia

### Estrutura do Conteúdo
```markdown
---
description: Clear description
globs: [patterns]
alwaysApply: false
---

# Title

## Category 1
- Rule 1
- Rule 2

## Category 2
- Rule 1
- Rule 2

## Anti-Patterns (Forbidden)
- ❌ Bad pattern: Why and alternative
- ❌ Bad pattern: Why and alternative

## Examples
```good-language
// Good example
```

```bad-language
// Bad example
```

## References
- @ref:other-rule#section
- @docs:https://official-docs.com
```

### Referências Cruzadas
```markdown
# Dentro do conteúdo
@ref:core-guardrails#patch-only
@ref:testing#unit-tests
@ref:security#input-validation

# Links externos
@docs:https://docs.cursor.com/en/context/rules
@docs:https://reactjs.org/docs/getting-started.html

# Templates
@template:language-template.mdc
```

## Exemplos Práticos

### Regra Always Apply
```markdown
---
description: Security requirements that apply to all code
globs:
alwaysApply: true
---

# Security Fundamentals

## Input Validation
- Always validate user input
- Use whitelist approach
- Sanitize output

## Secrets Management
- Never hardcode secrets
- Use environment variables
- Rotate secrets regularly

@ref:core-guardrails#risk-alerts
```

### Regra Auto Attached
```markdown
---
description: React component standards and patterns
globs:
  - "**/*.tsx"
  - "**/components/**"
alwaysApply: false
---

# React Component Standards

## Component Structure
- Use functional components
- Props interface required
- Default exports preferred

## Naming Conventions
- PascalCase for components
- camelCase for props
- kebab-case for files

@ref:testing#unit-tests
```

### Regra Manual
```markdown
---
description: Troubleshooting guide and debugging procedures
globs:
alwaysApply: false
---

# Troubleshooting Guide

Use `@troubleshooting` to activate this rule.

## Common Issues
1. Build failures
2. Test failures
3. Deployment issues

## Debug Procedures
- Check logs first
- Verify configuration
- Test in isolation

@ref:core-guardrails
```

## Integração com User Rules

### Hierarquia de Precedência
1. **User Rules**: Sempre aplicadas, preferências globais
2. **Always Apply Project Rules**: Regras fundamentais do projeto
3. **Auto Attached Project Rules**: Regras contextuais
4. **Agent Requested Project Rules**: Regras por demanda
5. **Manual Project Rules**: Regras explicitamente solicitadas

### Evitando Conflitos
- **User Rules**: Mantenha genéricas e focadas em estilo
- **Project Rules**: Sejam específicas e técnicas
- **Não duplique**: Evite repetir regras entre User e Project
- **Teste integração**: Verifique se funcionam bem juntas

## Troubleshooting

### Regras Não Ativam
**Possíveis causas**:
- Padrões glob incorretos
- Front-matter malformado
- Arquivo não salvo em `.cursor/rules/`

**Soluções**:
- Verifique sintaxe do front-matter
- Teste padrões glob com arquivos reais
- Reinicie o Cursor IDE

### Conflitos entre Regras
**Sintomas**:
- Comportamento inconsistente
- Agente confuso
- Regras contradizendo umas às outras

**Soluções**:
- Revise hierarquia de regras
- Remova duplicações
- Torne regras mais específicas

### Performance Degradada
**Causas**:
- Muitas regras always apply
- Regras muito longas
- Padrões glob muito amplos

**Soluções**:
- Mova regras para auto attached
- Divida regras grandes
- Torne globs mais específicos

## Referências

- [User Rules Guide](user-rules-guide.md)
- [Migration Guide](migration-guide.md)
- [Templates](../templates/)
- [Cursor Rules Documentation](https://docs.cursor.com/en/context/rules)
