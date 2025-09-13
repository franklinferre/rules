
# 📖 Cursor Usage Guide - Como Usar Cada Regra MDC

> **Guia completo de uso das regras Model-Driven Code com exemplos práticos e workflows N8N**

## 🎯 Visão Geral

Este guia detalha como usar efetivamente cada regra MDC disponível no repositório, incluindo exemplos práticos, prompts otimizados e integração com workflows N8N.

## 📋 Índice de Regras

### 🔤 Languages (7 linguagens)
- [TypeScript](#-typescript-mdc) - Web moderno + React/Next.js
- [JavaScript](#-javascript-mdc) - JavaScript ES2024+
- [Python](#-python-mdc) - FastAPI/Django/Flask
- [Go](#-go-mdc) - Gin/Echo/Fiber
- [Rust](#-rust-mdc) - Actix/Axum/Warp
- [Java](#-java-mdc) - Spring Boot 3.x
- [PHP](#-php-mdc) - Laravel/Symfony

### ⚙️ DevOps (5 áreas)
- [Containers](#-containers-mdc) - Docker + Kubernetes
- [CI/CD](#-cicd-mdc) - GitHub Actions + GitLab
- [Cloud](#-cloud-mdc) - AWS/GCP/Azure
- [Monitoring](#-monitoring-mdc) - Observabilidade
- [Security](#-security-mdc) - DevSecOps

### 🎯 Examples (2 padrões)
- [Full-Stack](#-fullstack-mdc) - Arquiteturas modernas
- [Supabase Integration](#-supabase-integration-mdc) - Integração oficial

## 🔤 Languages Rules

### 📘 TypeScript MDC

**Arquivo**: `languages/typescript.mdc`  
**Quando usar**: Projetos TypeScript, React, Next.js, Node.js  
**Auto-ativação**: `**/*.ts`, `**/*.tsx`, `**/*.d.ts`

#### Recursos Principais
- ✅ Strict mode obrigatório
- ✅ Tipos explícitos e interfaces claras
- ✅ Functional programming patterns
- ✅ Error handling robusto
- ✅ Performance optimization

#### Exemplo de Uso

```typescript
// ❌ Antes (sem regras)
function processUser(data: any): any {
  return data.user?.name || "Unknown";
}

// ✅ Depois (com typescript.mdc)
interface UserData {
  readonly user: {
    readonly id: string;
    readonly name: string;
    readonly email: string;
  } | null;
}

interface ProcessedUser {
  readonly name: string;
  readonly isValid: boolean;
}

function processUser(data: UserData): ProcessedUser {
  if (!data.user?.name) {
    return { name: "Unknown", isValid: false };
  }
  
  return { 
    name: data.user.name, 
    isValid: true 
  };
}
```

#### Prompts Otimizados

```typescript
// 1. Feature Implementation
`
@typescript.mdc @File:src/types/user.ts

Implemente um hook React para gerenciamento de estado de usuário:

Objective: Hook customizado para autenticação e perfil
Specification:
- useUser() hook com TypeScript strict
- Estado: loading, user, error
- Métodos: login, logout, updateProfile
- Integração com Context API

Context: Interface User já definida
Acceptance:
- ✅ Tipos explícitos para todos estados
- ✅ Error handling com Result<T, E> pattern
- ✅ Testes unitários com React Testing Library
- ✅ Documentação JSDoc completa

References: https://react.dev/reference/react/hooks
`

// 2. Code Review
`
@typescript.mdc @Code:src/utils/validation.ts

Revise esta função de validação seguindo as regras TypeScript:

function validateEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

Identifique melhorias em:
- Type safety
- Error handling  
- Performance
- Testability
`

// 3. Refactoring
`
@typescript.mdc @File:src/components/UserList.tsx

Refatore este componente para seguir as regras MDC:
- Extrair interfaces para props
- Implementar error boundaries
- Otimizar re-renders com useMemo
- Adicionar loading states apropriados
`
```

#### Integração N8N

```json
{
  "name": "TypeScript Code Quality Gate",
  "trigger": "File change *.ts, *.tsx",
  "workflow": [
    {
      "step": "Extract changed files",
      "action": "git diff --name-only"
    },
    {
      "step": "Validate TypeScript rules",
      "action": "Apply @typescript.mdc validation"
    },
    {
      "step": "Generate improvements",
      "action": "AI analysis with OSCAR framework"
    },
    {
      "step": "Create PR comment",
      "action": "Post suggestions to GitHub"
    }
  ]
}
```

### 🐍 Python MDC

**Arquivo**: `languages/python.mdc`  
**Quando usar**: APIs Python, FastAPI, Django, Flask, ML  
**Auto-ativação**: `**/*.py`

#### Recursos Principais
- ✅ Python 3.12+ features
- ✅ Type hints obrigatórios
- ✅ Pydantic para validação
- ✅ Async/await patterns
- ✅ Error handling estruturado

#### Exemplo de Uso

```python
# ❌ Antes (sem regras)
def create_user(data):
    user = User()
    user.name = data.get('name')
    user.email = data.get('email')
    return user

# ✅ Depois (com python.mdc)
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from result import Result, Ok, Err

class CreateUserRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, le=120)

class User(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: Optional[int] = None
    created_at: datetime

async def create_user(
    request: CreateUserRequest
) -> Result[User, str]:
    """
    Create a new user with validation.
    
    Args:
        request: Validated user creation data
        
    Returns:
        Result containing User or error message
    """
    try:
        # Business logic here
        user = User(
            id=generate_id(),
            name=request.name,
            email=request.email,
            age=request.age,
            created_at=datetime.utcnow()
        )
        
        return Ok(user)
        
    except Exception as e:
        logger.error(f"Failed to create user: {e}")
        return Err(f"User creation failed: {str(e)}")
```

#### Prompts Otimizados

```python
# 1. API Endpoint
`
@python.mdc @File:app/models/user.py

Crie um endpoint FastAPI para atualização de usuário:

Objective: PATCH /users/{user_id} com validação completa
Specification:
- Pydantic models para request/response
- Validação de permissões
- Error handling estruturado
- Logging para auditoria
- Testes unitários e integração

Context: Model User já definido
Acceptance:
- ✅ Type hints em todas funções
- ✅ Validação Pydantic v2
- ✅ Result<T, E> pattern para errors
- ✅ OpenAPI documentation
- ✅ Testes pytest ≥80% coverage

References: https://fastapi.tiangolo.com/tutorial/
`

# 2. Data Processing
`
@python.mdc @File:src/processors/data_pipeline.py

Otimize este pipeline de dados seguindo as regras Python:

def process_data(data):
    results = []
    for item in data:
        if item.get('valid'):
            results.append(transform(item))
    return results

Melhorias necessárias:
- Type annotations
- Async processing
- Error handling
- Memory optimization
`
```

### 🦀 Rust MDC

**Arquivo**: `languages/rust.mdc`  
**Quando usar**: APIs high-performance, sistemas, CLI tools  
**Auto-ativação**: `**/*.rs`, `**/Cargo.toml`

#### Recursos Principais
- ✅ Rust 2021 edition
- ✅ Error handling com Result<T, E>
- ✅ Memory safety patterns
- ✅ Performance optimization
- ✅ Async/await com Tokio

#### Exemplo de Uso

```rust
// ❌ Antes (sem regras)
fn get_user(id: String) -> String {
    // Unsafe operations, poor error handling
    let user = database.find(id).unwrap();
    user.name
}

// ✅ Depois (com rust.mdc)
use anyhow::{Context, Result};
use serde::{Deserialize, Serialize};
use uuid::Uuid;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct User {
    pub id: Uuid,
    pub name: String,
    pub email: String,
    pub created_at: chrono::DateTime<chrono::Utc>,
}

#[derive(Debug, thiserror::Error)]
pub enum UserError {
    #[error("User not found: {id}")]
    NotFound { id: Uuid },
    #[error("Database error: {0}")]
    Database(#[from] sqlx::Error),
    #[error("Validation error: {0}")]
    Validation(String),
}

pub async fn get_user(
    pool: &sqlx::PgPool,
    id: Uuid,
) -> Result<User, UserError> {
    let user = sqlx::query_as!(
        User,
        "SELECT id, name, email, created_at FROM users WHERE id = $1",
        id
    )
    .fetch_optional(pool)
    .await
    .context("Failed to query database")?
    .ok_or(UserError::NotFound { id })?;

    Ok(user)
}
```

## ⚙️ DevOps Rules

### 🐳 Containers MDC

**Arquivo**: `devops/containers.mdc`  
**Quando usar**: Docker, Kubernetes, containerização  
**Auto-ativação**: `Dockerfile*`, `docker-compose*.yml`, `k8s/*.yaml`

#### Recursos Principais
- ✅ Multi-stage builds
- ✅ Security best practices
- ✅ Optimization patterns
- ✅ Health checks
- ✅ Resource limits

#### Exemplo de Uso

```dockerfile
# ❌ Antes (sem regras)
FROM node:latest
COPY . .
RUN npm install
CMD ["npm", "start"]

# ✅ Depois (com containers.mdc)
# Multi-stage build for Node.js app
FROM node:18-alpine AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine AS runtime
# Security: non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001

WORKDIR /app
COPY --from=base /app/node_modules ./node_modules
COPY --from=build --chown=nextjs:nodejs /app/.next ./.next
COPY --from=build /app/public ./public
COPY --from=build /app/package.json ./package.json

USER nextjs

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/api/health || exit 1

EXPOSE 3000
CMD ["npm", "start"]
```

#### Prompts Otimizados

```dockerfile
# 1. Dockerfile Optimization
`
@containers.mdc @File:Dockerfile

Otimize este Dockerfile seguindo as regras de containers:

FROM python:3.11
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

Objective: Dockerfile production-ready
Specification:
- Multi-stage build
- Security hardening
- Size optimization
- Health checks
- Non-root user

Acceptance:
- ✅ Image size <100MB
- ✅ Security scan clean
- ✅ Health check functional
- ✅ Build time <2min
`

# 2. Kubernetes Deployment
`
@containers.mdc @File:k8s/deployment.yaml

Crie manifesto Kubernetes seguindo as regras:

Objective: Deployment resiliente para produção
Specification:
- Resource limits apropriados
- Liveness/readiness probes
- Rolling update strategy
- Security context
- ConfigMap/Secret integration

Context: App FastAPI com PostgreSQL
Acceptance:
- ✅ Zero-downtime deployments
- ✅ Auto-scaling configurado
- ✅ Monitoring labels
- ✅ Security policies
`
```

### 📊 Monitoring MDC

**Arquivo**: `devops/monitoring.mdc`  
**Quando usar**: Observabilidade, métricas, logs, alertas  
**Auto-ativação**: `prometheus.yml`, `grafana/`, `**/monitoring/**`

#### Recursos Principais
- ✅ Structured logging
- ✅ Metrics collection
- ✅ Distributed tracing
- ✅ Alerting rules
- ✅ Dashboard templates

#### Exemplo de Uso

```python
# ❌ Antes (sem regras)
def process_order(order_id):
    print(f"Processing order {order_id}")
    # Process order
    print("Order processed")

# ✅ Depois (com monitoring.mdc)
import logging
import time
from prometheus_client import Counter, Histogram, start_http_server
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Metrics
ORDER_COUNTER = Counter('orders_processed_total', 'Total processed orders')
ORDER_DURATION = Histogram('order_processing_seconds', 'Order processing time')

# Structured logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Tracing setup
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

@ORDER_DURATION.time()
def process_order(order_id: str) -> None:
    """Process an order with full observability."""
    
    with tracer.start_as_current_span("process_order") as span:
        span.set_attribute("order.id", order_id)
        
        logger.info(
            "Processing order",
            extra={
                "order_id": order_id,
                "operation": "process_order",
                "timestamp": time.time()
            }
        )
        
        try:
            # Business logic here
            time.sleep(0.1)  # Simulate processing
            
            ORDER_COUNTER.inc()
            span.set_attribute("order.status", "completed")
            
            logger.info(
                "Order processed successfully",
                extra={
                    "order_id": order_id,
                    "status": "completed",
                    "duration": 0.1
                }
            )
            
        except Exception as e:
            span.set_attribute("order.status", "failed")
            span.record_exception(e)
            
            logger.error(
                "Order processing failed",
                extra={
                    "order_id": order_id,
                    "error": str(e),
                    "status": "failed"
                },
                exc_info=True
            )
            raise
```

## 🎯 Examples Rules

### 🌐 Full-Stack MDC

**Arquivo**: `examples/fullstack.mdc`  
**Quando usar**: Aplicações web completas, SPAs, PWAs  
**Auto-ativação**: `**/app/**`, `**/pages/**`, `next.config.js`

#### Recursos Principais
- ✅ Arquitetura em camadas
- ✅ State management
- ✅ API integration
- ✅ Authentication patterns
- ✅ Performance optimization

#### Exemplo de Uso

```typescript
// ❌ Antes (sem regras)
function UserProfile() {
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    fetch('/api/user').then(res => res.json()).then(setUser);
  }, []);
  
  return <div>{user?.name}</div>;
}

// ✅ Depois (com fullstack.mdc)
import { useQuery } from '@tanstack/react-query';
import { z } from 'zod';

// Schema validation
const UserSchema = z.object({
  id: z.string().uuid(),
  name: z.string().min(1),
  email: z.string().email(),
  avatar: z.string().url().optional(),
});

type User = z.infer<typeof UserSchema>;

// API layer
class UserService {
  static async getUser(id: string): Promise<User> {
    const response = await fetch(`/api/users/${id}`, {
      headers: {
        'Authorization': `Bearer ${getAuthToken()}`,
        'Content-Type': 'application/json',
      },
    });
    
    if (!response.ok) {
      throw new Error(`Failed to fetch user: ${response.statusText}`);
    }
    
    const data = await response.json();
    return UserSchema.parse(data);
  }
}

// Component with proper error handling
interface UserProfileProps {
  userId: string;
}

export function UserProfile({ userId }: UserProfileProps) {
  const {
    data: user,
    isLoading,
    error,
    refetch
  } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => UserService.getUser(userId),
    staleTime: 5 * 60 * 1000, // 5 minutes
    retry: 3,
  });

  if (isLoading) {
    return <UserProfileSkeleton />;
  }

  if (error) {
    return (
      <ErrorBoundary
        error={error}
        onRetry={refetch}
        fallback="Failed to load user profile"
      />
    );
  }

  if (!user) {
    return <EmptyState message="User not found" />;
  }

  return (
    <div className="user-profile">
      <Avatar src={user.avatar} alt={user.name} />
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}
```

### 🗄️ Supabase Integration MDC

**Arquivo**: `examples/supabase-integration.mdc`  
**Quando usar**: Projetos com Supabase, PostgreSQL, Auth  
**Auto-ativação**: `supabase/`, `**/*supabase*`

#### Recursos Principais
- ✅ Official Supabase patterns
- ✅ Row Level Security (RLS)
- ✅ Edge Functions
- ✅ Realtime subscriptions
- ✅ Type-safe database access

#### Exemplo de Uso

```typescript
// ❌ Antes (sem regras)
const { data } = await supabase
  .from('users')
  .select('*')
  .eq('id', userId);

// ✅ Depois (com supabase-integration.mdc)
import { createClient } from '@supabase/supabase-js';
import { Database } from './types/database';

// Type-safe client
const supabase = createClient<Database>(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

// Database types
type User = Database['public']['Tables']['users']['Row'];
type UserInsert = Database['public']['Tables']['users']['Insert'];
type UserUpdate = Database['public']['Tables']['users']['Update'];

// Service layer with error handling
export class UserService {
  static async getUser(id: string): Promise<User | null> {
    const { data, error } = await supabase
      .from('users')
      .select(`
        id,
        name,
        email,
        avatar_url,
        created_at,
        profiles (
          bio,
          website
        )
      `)
      .eq('id', id)
      .single();

    if (error) {
      console.error('Error fetching user:', error);
      throw new Error(`Failed to fetch user: ${error.message}`);
    }

    return data;
  }

  static async updateUser(
    id: string, 
    updates: UserUpdate
  ): Promise<User> {
    const { data, error } = await supabase
      .from('users')
      .update(updates)
      .eq('id', id)
      .select()
      .single();

    if (error) {
      console.error('Error updating user:', error);
      throw new Error(`Failed to update user: ${error.message}`);
    }

    return data;
  }
}

// RLS Policy (SQL)
/*
-- Enable RLS
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Users can only see their own data
CREATE POLICY "Users can view own profile" ON users
  FOR SELECT USING (auth.uid() = id);

-- Users can only update their own data  
CREATE POLICY "Users can update own profile" ON users
  FOR UPDATE USING (auth.uid() = id);
*/

// Realtime subscription
export function useUserSubscription(userId: string) {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const subscription = supabase
      .channel(`user:${userId}`)
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table: 'users',
          filter: `id=eq.${userId}`,
        },
        (payload) => {
          if (payload.eventType === 'UPDATE') {
            setUser(payload.new as User);
          }
        }
      )
      .subscribe();

    return () => {
      subscription.unsubscribe();
    };
  }, [userId]);

  return user;
}
```

## 🤖 Integração com N8N Workflows

### Workflow Templates

#### 1. Code Quality Gate
```json
{
  "name": "Automated Code Quality Gate",
  "description": "Validates code changes against MDC rules",
  "trigger": {
    "type": "webhook",
    "event": "github.pull_request"
  },
  "nodes": [
    {
      "name": "Extract PR Files",
      "type": "GitHub",
      "operation": "getPullRequestFiles"
    },
    {
      "name": "Apply MDC Rules",
      "type": "AI Agent",
      "prompt": "@{rule_name}.mdc Analyze these files and identify violations"
    },
    {
      "name": "Generate Report",
      "type": "Template",
      "template": "code_quality_report.md"
    },
    {
      "name": "Post PR Comment",
      "type": "GitHub",
      "operation": "createComment"
    }
  ]
}
```

#### 2. Documentation Generator
```json
{
  "name": "Auto Documentation Generator",
  "description": "Generates docs from code changes",
  "trigger": {
    "type": "file_change",
    "pattern": "src/**/*.{ts,tsx,py,rs}"
  },
  "nodes": [
    {
      "name": "Analyze Code Structure",
      "type": "AI Agent",
      "prompt": "@{language}.mdc Extract API documentation from this code"
    },
    {
      "name": "Generate Markdown",
      "type": "Template",
      "template": "api_documentation.md"
    },
    {
      "name": "Update README",
      "type": "File Operation",
      "operation": "append"
    },
    {
      "name": "Commit Changes",
      "type": "Git",
      "operation": "commit"
    }
  ]
}
```

#### 3. Test Generation Agent
```json
{
  "name": "Intelligent Test Generator",
  "description": "Generates tests for new functions",
  "trigger": {
    "type": "code_analysis",
    "event": "new_function_detected"
  },
  "nodes": [
    {
      "name": "Analyze Function",
      "type": "AI Agent",
      "prompt": "@{language}.mdc Generate comprehensive tests for this function"
    },
    {
      "name": "Create Test File",
      "type": "File Operation",
      "operation": "create"
    },
    {
      "name": "Run Tests",
      "type": "Shell",
      "command": "npm test"
    },
    {
      "name": "Validate Coverage",
      "type": "Coverage Analysis",
      "threshold": 80
    }
  ]
}
```

## 🎯 Prompts Avançados com OSCAR

### Feature Implementation

```typescript
`
@{language}.mdc @File:PRD.md @File:src/types/

OSCAR Framework:

Objective: Implementar sistema de notificações em tempo real
Specification:
- WebSocket connection com auto-reconnect
- Queue de notificações offline
- Tipos TypeScript para todas mensagens
- Persistência local com IndexedDB
- UI components com Tailwind CSS

Context: 
- @File:src/types/notification.ts (tipos existentes)
- @File:src/hooks/useWebSocket.ts (hook base)
- @PRD.md seção 4.3 (requisitos de notificação)

Acceptance:
- ✅ Connection resiliente a falhas de rede
- ✅ Queue persiste durante offline
- ✅ Tipos explícitos para todos payloads
- ✅ Testes unitários ≥85% coverage
- ✅ Performance: <100ms para mostrar notificação
- ✅ Acessibilidade: ARIA labels e keyboard navigation

References:
- https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
- https://web.dev/notification-best-practices/
- https://tailwindcss.com/docs/accessibility
`
```

### Code Review

```typescript
`
@{language}.mdc @Code:src/utils/auth.ts:validateToken

OSCAR Framework:

Objective: Revisar função de validação de token JWT
Specification:
- Verificar implementação de segurança
- Validar error handling
- Analisar performance
- Checar type safety

Context:
- @File:src/types/auth.ts (tipos de auth)
- @File:tests/utils/auth.test.ts (testes existentes)
- Função atual usa jsonwebtoken library

Acceptance:
- ✅ Sem vulnerabilidades de segurança
- ✅ Error handling completo
- ✅ Tipos explícitos
- ✅ Performance otimizada
- ✅ Testes cobrem edge cases

References:
- https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/
- https://owasp.org/www-project-web-security-testing-guide/
`
```

### Refactoring

```typescript
`
@{language}.mdc @File:src/components/UserDashboard.tsx

OSCAR Framework:

Objective: Refatorar componente para melhor performance e manutenibilidade
Specification:
- Extrair sub-componentes reutilizáveis
- Implementar lazy loading para seções
- Otimizar re-renders com React.memo
- Adicionar error boundaries
- Melhorar acessibilidade

Context:
- Componente atual tem 300+ linhas
- Performance issues reportados
- @File:src/hooks/useUser.ts (hook de usuário)
- @File:src/components/ui/ (componentes base)

Acceptance:
- ✅ Componente principal <100 linhas
- ✅ Sub-componentes reutilizáveis
- ✅ Lazy loading implementado
- ✅ Performance melhorada >50%
- ✅ Acessibilidade score >95%
- ✅ Testes mantidos e expandidos

References:
- https://react.dev/reference/react/memo
- https://web.dev/code-splitting-suspense/
- https://www.w3.org/WAI/WCAG21/quickref/
`
```

## 📊 Métricas e Monitoramento

### KPIs por Regra

#### TypeScript MDC
- **Type Coverage**: Meta ≥95%
- **Build Time**: Meta <30s
- **Bundle Size**: Meta <500KB
- **Runtime Errors**: Meta <0.1%

#### Python MDC  
- **Type Hints Coverage**: Meta ≥90%
- **Test Coverage**: Meta ≥85%
- **API Response Time**: Meta <200ms
- **Memory Usage**: Meta <512MB

#### Containers MDC
- **Image Size**: Meta <100MB
- **Build Time**: Meta <5min
- **Security Vulnerabilities**: Meta 0
- **Startup Time**: Meta <10s

### Dashboard de Qualidade

```typescript
interface QualityMetrics {
  rules: {
    [ruleName: string]: {
      compliance: number; // 0-100%
      violations: number;
      lastCheck: Date;
      trend: 'improving' | 'stable' | 'declining';
    };
  };
  overall: {
    score: number; // 0-100
    grade: 'A' | 'B' | 'C' | 'D' | 'F';
    recommendations: string[];
  };
}
```

## 🚨 Troubleshooting

### Problemas Comuns

#### 1. Regra não está sendo aplicada
```bash
# Verificar se arquivo está no glob pattern
ls -la .cursor/rules/
head -10 .cursor/rules/typescript.mdc

# Verificar sintaxe do front-matter
---
description: "..."
globs: ["**/*.ts", "**/*.tsx"]
alwaysApply: false
---
```

#### 2. Conflitos entre regras
```typescript
// Use @ref: para referenciar outras regras
`
@typescript.mdc @fullstack.mdc

Há conflito entre as regras TypeScript e Full-Stack para:
- Error handling patterns
- State management approach

Resolva priorizando @typescript.mdc para tipos e @fullstack.mdc para arquitetura.
`
```

#### 3. Performance issues
```bash
# Otimizar .cursorignore
echo "node_modules/" >> .cursorignore
echo "dist/" >> .cursorignore
echo "*.log" >> .cursorignore

# Usar .cursorindexignore para arquivos grandes
echo "docs/" >> .cursorindexignore
echo "*.md" >> .cursorindexignore
```

## 🎯 Melhores Práticas

### 1. Combinação de Regras
```typescript
// ✅ Boa combinação
typescript.mdc + fullstack.mdc + containers.mdc

// ❌ Evitar conflitos
python.mdc + typescript.mdc (para mesmo arquivo)
```

### 2. Prompts Estruturados
```typescript
// ✅ Sempre use OSCAR Framework
Objective: Claro e específico
Specification: Requisitos técnicos detalhados
Context: @files relevantes
Acceptance: Critérios mensuráveis
References: Links oficiais

// ❌ Prompts vagos
"Melhore este código"
"Adicione testes"
```

### 3. Iteração Contínua
```typescript
// Ciclo de melhoria
1. Implementar → 2. Medir → 3. Analisar → 4. Otimizar → Repetir

// Métricas por ciclo
- Code quality score
- Development velocity  
- Bug reduction rate
- Developer satisfaction
```

---

## 🔗 Próximos Passos

1. **[CURSOR_DEPLOY_GUIDE.md](CURSOR_DEPLOY_GUIDE.md)** - Setup inicial completo
2. **[docs/migration-guide.md](docs/migration-guide.md)** - Migração de projetos existentes
3. **[docs/cursor-best-practices-integration.md](docs/cursor-best-practices-integration.md)** - Best practices avançadas

---

> **💡 Dica**: Comece com uma regra por vez, meça o impacto, e expanda gradualmente. O objetivo é melhorar a qualidade e velocidade de desenvolvimento de forma sustentável.

**Tempo de domínio**: ~2 semanas de uso ativo  
**ROI esperado**: +200% velocidade, +40% qualidade  
**Suporte**: Issues no GitHub ou documentação oficial
