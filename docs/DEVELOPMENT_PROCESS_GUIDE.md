---
description: "Guia de processo de desenvolvimento em fases, incluindo a Fase 0 para infraestrutura e automação, alinhado com as práticas do Cursor."
globs: ["docs/DEVELOPMENT_PROCESS_GUIDE.md"]
alwaysApply: true
---

# Guia de Processo de Desenvolvimento em Fases

Este documento descreve um processo de desenvolvimento de software em fases, com foco na integração de metodologias disciplinadas e o uso de ferramentas de IA como o Cursor. A estrutura é inspirada na necessidade de garantir qualidade, conformidade e eficiência desde o início do projeto.

## Visão Geral do Processo

O processo é dividido em fases distintas, cada uma com objetivos claros, entregáveis e portões de qualidade. A progressão entre as fases é condicionada à aprovação dos portões de qualidade, garantindo que o trabalho esteja sempre alinhado com os padrões definidos.

## Fase 0: Preparação e Infraestrutura (A Base Sólida)

A Fase 0 é crucial e precede qualquer desenvolvimento de funcionalidade. Seu objetivo é estabelecer uma base sólida de infraestrutura, ferramentas e automação que garantirá a qualidade e a eficiência das fases subsequentes.

### Objetivos da Fase 0

*   **Definição de Infraestrutura:** Estabelecer a infraestrutura de nuvem (AWS, GCP, Azure) e os serviços de suporte (bancos de dados, filas, caches).
*   **Configuração de CI/CD:** Implementar pipelines de Integração Contínua e Entrega Contínua (CI/CD) para automação de builds, testes e deployments.
*   **Ferramentas de Qualidade:** Configurar ferramentas de linting, formatação de código, análise estática e dinâmica de segurança (SAST/DAST).
*   **Ambientes de Desenvolvimento:** Padronizar e automatizar a criação de ambientes de desenvolvimento e teste.
*   **Monitoramento e Observabilidade:** Implementar soluções de monitoramento, logging e tracing para garantir a visibilidade da aplicação e infraestrutura.
*   **Documentação Inicial:** Criar a documentação essencial do projeto, incluindo ADRs (Architectural Decision Records) e guias de setup.
*   **Benchmarking e Performance:** Definir e configurar ferramentas para benchmarking de desempenho e testes de carga.

### Entregáveis da Fase 0

*   Infraestrutura como Código (IaC) versionada e funcional.
*   Pipelines de CI/CD automatizados e testados.
*   Configurações de ferramentas de qualidade de código e segurança.
*   Ambientes de desenvolvimento provisionados.
*   Dashboards de monitoramento e alertas configurados.
*   ADRs e documentação de setup.

### Portões de Qualidade da Fase 0

*   **100% de Automação de Infraestrutura:** Toda a infraestrutura deve ser provisionada via código.
*   **Zero Vulnerabilidades Críticas:** Scans de segurança devem passar sem vulnerabilidades críticas na infraestrutura base.
*   **Pipelines Verdes:** Todos os pipelines de CI/CD devem estar funcionando e passando em todos os testes.
*   **Cobertura de Monitoramento:** Métricas e logs essenciais devem estar sendo coletados e visualizados.

## Fases de Desenvolvimento (Iterativas)

Após a conclusão da Fase 0, o desenvolvimento de funcionalidades segue um ciclo iterativo, onde cada fase foca em um conjunto específico de funcionalidades ou componentes.

### Estrutura de uma Fase de Desenvolvimento

Cada fase de desenvolvimento deve ser definida utilizando um template `.mdc` (ver `templates/development_process/phase_template.mdc`) e incluir:

*   **Objetivos:** O que será alcançado nesta fase.
*   **Escopo:** As funcionalidades e componentes envolvidos.
*   **Dependências:** Pré-requisitos para iniciar a fase.
*   **Entregáveis:** Os resultados esperados (código, testes, documentação).
*   **Portões de Qualidade:** Critérios de aceitação para a conclusão da fase.

## Ferramentas de IA e a Metodologia

O Cursor e outros agentes de IA são integrados em todas as fases para auxiliar no desenvolvimento, revisão de código, geração de testes e documentação. As `Project Rules` (`.cursor/rules/*.mdc`) e `User Rules` são fundamentais para guiar o comportamento da IA, garantindo que ela siga as melhores práticas e padrões do projeto.

## Ciclo de Feedback e Melhoria Contínua

O processo é iterativo e promove um ciclo contínuo de feedback e melhoria. As `Implementation Notes` em cada `.mdc` e os ADRs são utilizados para registrar aprendizados e ajustar o processo conforme necessário.


