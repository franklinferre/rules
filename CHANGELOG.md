

# Changelog

All notable changes to the Cursor MDC Rules repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-09-12

### Added - Supabase Official Integration

#### New Rule Files
- **`75-supabase-official.mdc`** - Official Supabase development standards based on official documentation:
  - Official function templates with mandatory security configurations
  - SECURITY INVOKER and search_path = '' requirements
  - Performance classification (IMMUTABLE/STABLE/VOLATILE) with examples
  - Row Level Security (RLS) policy patterns
  - Edge Functions development templates
  - Realtime subscription patterns
  - Migration and rollback templates
  - Comprehensive error handling patterns
  - Official naming conventions and project structure

#### Enhanced Files
- **`70-database-standards.mdc`** - Integrated official Supabase practices:
  - Added mandatory function template with security configurations
  - Integrated performance classification guidelines
  - Enhanced trigger function patterns
  - Added official Supabase rules structure reference
  - Included links to official rule installation command

#### Updated Documentation
- **`README.md`** - Updated to reflect Supabase integration:
  - Added reference to new rule 75-supabase-official.mdc
  - Updated rule count to 75 (16 total rules)
  - Enhanced database standards description with Supabase integration

### Enhanced Features

#### Official Supabase Compliance
- **Security-First Approach**: Mandatory SECURITY INVOKER and empty search_path
- **Performance Optimization**: Proper function classification for PostgreSQL optimization
- **Official Templates**: Based on Supabase's official AI editor rules documentation
- **Best Practices Integration**: Seamless integration with existing database standards

#### Comprehensive Coverage
- **Database Functions**: Complete templates for all function types
- **Security Policies**: RLS patterns for user-based and role-based access
- **Edge Functions**: TypeScript templates with proper CORS and authentication
- **Realtime Features**: Client-side subscription and presence patterns
- **Migration Patterns**: Safe migration and rollback templates

#### Developer Experience
- **Copy-Paste Ready**: All templates are production-ready
- **Error Handling**: Comprehensive error handling patterns
- **Type Safety**: Explicit typing requirements and examples
- **Documentation**: Inline comments and usage examples

### Integration Benefits

#### Enhanced Security
- **Mandatory Security Settings**: Prevents common security vulnerabilities
- **Fully Qualified Names**: Eliminates schema injection risks
- **Explicit Permissions**: Clear permission model with SECURITY INVOKER default

#### Improved Performance
- **Function Classification**: Proper IMMUTABLE/STABLE/VOLATILE usage
- **Query Optimization**: Templates optimized for PostgreSQL query planner
- **Connection Efficiency**: Built-in connection pooling best practices

#### Official Compliance
- **Supabase Standards**: Aligned with official Supabase documentation
- **AI Editor Rules**: Compatible with official Supabase AI editor rules
- **Future-Proof**: Based on official templates and patterns

### Source Attribution
Based on official Supabase documentation and AI editor rules available at:
- https://supabase.com/ui/docs/ai-editors-rules/prompts
- https://supabase.com/ui/r/ai-editor-rules.json

---

## [1.1.0] - 2025-09-12

### Added - Cursor Best Practices Integration

#### New Rule Files
- **`05-cursor-best-practices.mdc`** - Core Cursor IDE best practices including:
  - PRD-first development methodology
  - Agent vs ASK mode selection strategy
  - Model selection guidelines (Claude-4 Sonnet, OpenAI o3, Gemini 2.5 Pro)
  - @ References mastery (@File, @Code, @Web, @Terminal, @Git)
  - Quality triad: Logging + Tests + Documentation
  - Iterative improvement workflows
  - MCP servers integration for advanced users

- **`15-prompt-engineering.mdc`** - Advanced prompt engineering techniques:
  - OSCAR Framework (Objective-Specification-Context-Acceptance-References)
  - Prompt patterns library (feature implementation, bug fixing, refactoring)
  - Context management strategies and layering techniques
  - 3-Pass refinement method (Structure → Quality → Polish)
  - Quality metrics and anti-patterns
  - Progressive disclosure and constraint-based prompting

- **`25-context-optimization.mdc`** - Context and indexing optimization:
  - Comprehensive `.cursorignore` patterns for different project types
  - Strategic `.cursorindexignore` for on-demand file access
  - Smart file referencing strategies and context layering
  - Token budget allocation and management
  - Performance optimization techniques
  - Context validation and troubleshooting

#### Enhanced Documentation
- **`docs/cursor-best-practices-integration.md`** - Complete integration guide covering:
  - Detailed explanation of all 10 integrated best practices
  - Implementation workflows and project setup checklists
  - Migration guide for existing and new projects
  - Success metrics and compatibility notes

#### Updated Files
- **`.cursorignore`** - Enhanced with comprehensive exclusion patterns:
  - Build artifacts and dependencies (node_modules, venv, dist, build)
  - Logs and temporary files (*.log, .cache, .tmp)
  - Large data files (*.csv, *.json, data/, uploads/)
  - Media files (images, videos, PDFs, archives)
  - Secrets and sensitive data (.env, *.key, *.pem)
  - Database and binary files

- **`README.md`** - Updated with:
  - Integration of best practices methodology
  - Enhanced project setup instructions
  - New workflow integration examples
  - Updated compatibility information

### Enhanced Features

#### Prompt Engineering Excellence
- **OSCAR Framework**: Structured approach to prompt construction
- **Pattern Library**: Reusable templates for common development tasks
- **Quality Metrics**: Measurable standards for prompt effectiveness
- **Iterative Refinement**: Systematic approach to improving AI responses

#### Context Management
- **Progressive Context Building**: Layer-by-layer context construction
- **Smart Referencing**: Optimized @ reference usage patterns
- **Token Optimization**: Strategic budget allocation for maximum efficiency
- **Performance Monitoring**: Tools and techniques for context validation

#### Quality Assurance
- **Definition of Done**: Feature + Tests + Logs + Documentation
- **3-Pass Method**: Systematic code review and refinement process
- **Quality Triad**: Integrated approach to logging, testing, and documentation
- **Proactive Testing**: Test generation before feature completion

### Integration Benefits

#### Improved Development Workflow
- **PRD-First Approach**: Clear requirements and alignment before coding
- **Mode Selection Strategy**: Appropriate use of AGENT vs ASK modes
- **Model Optimization**: Right AI model for each task complexity
- **Iterative Excellence**: Systematic improvement through refinement cycles

#### Enhanced Code Quality
- **Comprehensive Testing**: Unit tests with ≥80% coverage targets
- **Observability**: Logging standards for debugging and monitoring
- **Documentation**: Complete project documentation from PRD to API docs
- **Consistency**: Standardized patterns and practices across projects

#### Optimized Performance
- **Context Efficiency**: >80% relevance in referenced content
- **Response Speed**: Optimized indexing for faster AI responses
- **Token Management**: Strategic context allocation and budget control
- **Accuracy**: >90% first-pass accuracy through better prompting

### Compatibility
- **Cursor Rules v2**: Full compatibility with latest `.mdc` format
- **Existing Rules**: No breaking changes to current rule structure
- **Cross-References**: Proper `@ref:` syntax for rule interconnection
- **Modular Adoption**: Incremental integration of new practices

### Source Attribution
Based on "Mastering Cursor IDE: 10 Best Practices (Building a Daily Task Manager App)" by Roberto Infante, with adaptations for the MDC repository structure and Cursor Rules v2 compatibility.

---

## [1.0.0] - 2025-09-12

### Added
- Initial repository structure with Cursor Rules v2 support
- Core guardrails and gates system
- Language-specific rules (Python FastAPI, TypeScript React)
- Testing and security standards
- DevOps and Docker Compose rules
- Template system for new rules
- Comprehensive documentation


## [2024-09-12] - New MDC Rules 70-74

### Added
- **70-database-standards.mdc**: Comprehensive database standards for PostgreSQL, MySQL, SQLite, MongoDB, and Supabase with performance optimization
- **71-traefik-proxy.mdc**: Traefik reverse proxy setup with Docker, SSL termination, and load balancing best practices  
- **72-memory-optimization.mdc**: Memory management, caching strategies, and performance optimization techniques across languages
- **73-rule-authoring.mdc**: Meta-practices and standards for creating effective Cursor MDC rules and documentation
- **74-fullstack-patterns.mdc**: Modern full-stack architectures, SOLID principles, and CI/CD pipeline best practices

### Enhanced
- Extended rule coverage to 16 total MDC rules (00-74)
- Added cross-references between related rules using @ref: system
- Improved documentation structure and consistency

