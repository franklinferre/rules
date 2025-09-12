
# Cursor Rules v2 - Comprehensive Development Guidelines

Este repositório contém regras abrangentes para desenvolvimento moderno usando o formato Cursor Rules v2 (.mdc), organizadas por linguagens, DevOps, e exemplos práticos.

## 📁 Estrutura do Repositório

### 🔤 Languages/
Regras específicas por linguagem de programação:
- **typescript.mdc** - TypeScript com strict typing e patterns modernos
- **python.mdc** - Python com FastAPI/Django e async patterns
- **javascript.mdc** - JavaScript ES2023+ com functional programming
- **go.mdc** - Go para microservices e clean architecture
- **rust.mdc** - Rust com safety, performance e async patterns
- **php.mdc** - PHP moderno com Laravel/Symfony
- **java.mdc** - Java enterprise com Spring Boot

### ⚙️ DevOps/
Regras de infraestrutura e operações:
- **cicd.mdc** - CI/CD pipelines (GitHub Actions, GitLab, Jenkins, Azure)
- **containers.mdc** - Docker, Kubernetes, Helm best practices
- **monitoring.mdc** - Prometheus, Grafana, ELK, Jaeger observability
- **security.mdc** - Framework R.A.I.L.G.U.A.R.D para security
- **cloud.mdc** - AWS, GCP, Azure infrastructure as code

### 📋 Examples/
Casos práticos e templates:
- **fullstack.mdc** - Aplicações full-stack completas
- **supabase-integration.mdc** - Integrações Supabase + frontend

## 🚀 Como Usar

1. **Instale as regras no Cursor:**
   ```bash
   # Clone o repositório
   git clone https://github.com/franklinferre/rules.git
   
   # Copie as regras para seu projeto
   cp -r rules/.cursor/rules/ seu-projeto/.cursor/
   ```

2. **Use regras específicas:**
   - Para TypeScript: Copie `languages/typescript.mdc`
   - Para DevOps: Copie regras de `devops/`
   - Para exemplos: Consulte `examples/`

## 🔧 Formato Cursor Rules v2

Todas as regras seguem o formato .mdc com metadados YAML:

```yaml
---
description: "Descrição da regra"
globs: ["**/*.ts", "**/*.tsx"]
alwaysApply: false
---

# Conteúdo da regra em Markdown
```

## 🛡️ Framework R.A.I.L.G.U.A.R.D

Implementamos o framework de segurança R.A.I.L.G.U.A.R.D:
- **R**isk-First Reasoning
- **A**ccess Control  
- **I**nput Validation
- **L**ogging & Monitoring
- **G**uard Rails
- **U**ser Permissions
- **A**udit Trails
- **R**isk Assessment
- **D**ata Protection

## 🔄 Sincronização

Todas as regras são sincronizadas para manter consistência entre:
- Supabase ↔ PostgreSQL
- Frontend ↔ Backend
- Development ↔ Production

## 📖 Documentação

Cada regra inclui:
- ✅ Exemplos de boas práticas
- ❌ Padrões a evitar
- 🔧 Configurações recomendadas
- 📚 Links para documentação

## 🤝 Contribuição

1. Fork o repositório
2. Crie uma branch para sua feature
3. Siga o formato .mdc estabelecido
4. Teste as regras em projetos reais
5. Abra um Pull Request

## 📄 Licença

MIT License - veja [LICENSE](LICENSE) para detalhes.

---

**Desenvolvido para maximizar produtividade e manter código consistente e seguro.**
