---
description: "Guia de melhores práticas para o uso eficaz do Model Context Protocol (MCP) no Cursor IDE, otimizando o desenvolvimento assistido por IA."
globs: ["docs/mcp_best_practices_guide.md"]
alwaysApply: true
---

# Guia de Melhores Práticas para o Model Context Protocol (MCP) no Cursor IDE

Este guia detalha as melhores práticas para utilizar o Model Context Protocol (MCP) no Cursor IDE, maximizando a eficiência e a inteligência do desenvolvimento assistido por IA. O MCP é uma ferramenta poderosa que conecta o Cursor a sistemas externos e fontes de dados, fornecendo contexto rico e permitindo a automação de tarefas complexas.

## O que é o Model Context Protocol (MCP)?

O Model Context Protocol (MCP) é um padrão aberto que permite que modelos de IA (como os utilizados no Cursor) interajam com dados e serviços externos. Em vez de depender apenas do contexto fornecido diretamente no prompt, o MCP permite que o Cursor:

*   **Acesse informações em tempo real:** De bancos de dados, APIs, sistemas de gerenciamento de projetos (como o Linear), etc.
*   **Execute ações:** Como criar issues, buscar documentação na web, interagir com o sistema de arquivos ou executar comandos no terminal.
*   **Mantenha o contexto:** De forma persistente e estruturada, evitando a necessidade de repetir informações.

## Por que usar o MCP?

O uso do MCP oferece diversos benefícios que transformam o fluxo de trabalho de desenvolvimento:

1.  **Contexto Aprimorado:** Fornece à IA acesso a informações relevantes e atualizadas de sistemas externos, resultando em respostas mais precisas e úteis.
2.  **Automação Poderosa:** Permite que a IA execute ações diretamente em outras ferramentas, automatizando tarefas repetitivas e complexas (e.g., criar uma issue no Linear, buscar uma dependência).
3.  **Redução de Alucinações:** Com acesso a fontes de dados autoritativas, a IA tem menos probabilidade de "alucinar" ou gerar informações incorretas.
4.  **Segurança e Controle:** O MCP impõe um modelo de permissões, garantindo que a IA só acesse e manipule dados com a autorização do usuário e dentro de limites definidos.
5.  **Reusabilidade:** Servidores MCP podem ser desenvolvidos e reutilizados em diferentes projetos e contextos, padronizando a interação da IA com ferramentas comuns.
6.  **Eficiência no Desenvolvimento:** Reduz a necessidade de copiar e colar informações, alternar entre aplicativos e realizar tarefas manuais, acelerando o ciclo de desenvolvimento.

## Tipos de MCPs e Quando Usá-los

O Cursor suporta diferentes tipos de MCPs, cada um otimizado para um tipo específico de interação:

### 1. MCPs de Sistema de Arquivos (`@File`, `@Files`, `@Code`)

*   **O que são:** Permitem que a IA acesse e manipule arquivos e trechos de código no seu projeto.
*   **Quando usar:**
    *   Para fornecer à IA o conteúdo de um arquivo específico (`@File <caminho/do/arquivo>`).
    *   Para incluir múltiplos arquivos ou diretórios (`@Files <caminho/do/diretorio>`).
    *   Para referenciar um trecho de código específico (`@Code <linha_inicial>-<linha_final>`).
    *   Ao pedir para a IA refatorar, depurar, documentar ou gerar testes para um código existente.
*   **Por que usar:** Essencial para qualquer tarefa de codificação, garante que a IA tenha o contexto exato do seu codebase.

### 2. MCPs de Web (`@Web`)

*   **O que são:** Permitem que a IA realize buscas na web e acesse o conteúdo de páginas web.
*   **Quando usar:**
    *   Para pesquisar documentação, exemplos, soluções para erros ou informações sobre APIs externas.
    *   Para obter informações atualizadas que não estão no seu codebase ou base de conhecimento local.
*   **Por que usar:** Mantém a IA informada com os dados mais recentes da internet, útil para resolver problemas novos ou complexos.

### 3. MCPs de Terminal (`@Terminal`)

*   **O que são:** Permitem que a IA execute comandos no terminal e capture seus outputs.
*   **Quando usar:**
    *   Para executar testes, compilar código, instalar dependências, verificar o status de serviços ou interagir com ferramentas de linha de comando.
    *   Para depurar problemas que exigem a execução de comandos específicos.
*   **Por que usar:** Habilita a IA a interagir com o ambiente de desenvolvimento de forma dinâmica, automatizando tarefas operacionais.

### 4. MCPs de Git (`@Git`)

*   **O que são:** Permitem que a IA interaja com o seu repositório Git, acessando histórico de commits, branches, diffs, etc.
*   **Quando usar:**
    *   Para entender o histórico de mudanças de um arquivo ou funcionalidade.
    *   Para gerar mensagens de commit, revisar pull requests ou auxiliar em merges.
*   **Por que usar:** Fornece à IA uma compreensão profunda da evolução do projeto e das práticas de controle de versão.

### 5. MCPs de Integração (Customizados, e.g., Linear, Notion, Slack)

*   **O que são:** Servidores MCP personalizados que conectam o Cursor a ferramentas de terceiros (como o Linear, Notion, Slack, etc.) via suas APIs.
*   **Quando usar:**
    *   Para criar, atualizar ou consultar issues em sistemas de gerenciamento de projetos (como o Linear).
    *   Para buscar informações em bases de conhecimento (como o Notion).
    *   Para enviar notificações ou interagir em canais de comunicação (como o Slack).
    *   Sempre que precisar que a IA interaja com dados ou funcionalidades de um sistema externo específico.
*   **Por que usar:** Estende as capacidades do Cursor para além do código, integrando-o ao ecossistema completo de ferramentas da equipe, automatizando workflows de ponta a ponta.

## Como Usar o MCP no Cursor

1.  **Configuração:**
    *   Certifique-se de que os servidores MCP necessários estejam configurados no seu Cursor IDE (geralmente em `Settings -> Model Context Protocol`).
    *   Para MCPs customizados (como o Linear), pode ser necessário instalar um servidor MCP local ou remoto e configurá-lo no Cursor.
    *   Garanta que as credenciais (e.g., PATs) estejam configuradas de forma segura.

2.  **Referência em Prompts:**
    *   Utilize a sintaxe `@` para referenciar MCPs diretamente nos seus prompts. O Cursor irá automaticamente buscar o contexto ou executar a ação associada.
    *   Exemplo: `"@Linear create issue: 'Bug: Falha na autenticação ao usar OAuth' com descrição 'Ocorre ao tentar login com Google, erro 500 no backend.' e prioridade 'High'"`
    *   Exemplo: `"@File src/services/auth.ts: Refatore esta função para usar async/await e adicione tratamento de erros." `

3.  **Combinação de MCPs:**
    *   Combine diferentes MCPs no mesmo prompt para fornecer um contexto ainda mais rico e permitir ações complexas.
    *   Exemplo: `"@File src/components/UserAuth.tsx @Web 'React OAuth best practices': Revise este componente de autenticação e sugira melhorias de segurança e UX com base nas melhores práticas encontradas na web." `

## Melhores Práticas para Prompt Engineering com MCPs

*   **Seja Específico:** Quanto mais específico você for ao referenciar um MCP, melhor será o contexto fornecido à IA.
*   **Priorize o Contexto:** Coloque os MCPs mais relevantes no início do prompt para garantir que a IA os processe com prioridade.
*   **Valide as Saídas:** Sempre revise as ações e o código gerado pela IA, especialmente quando ela interage com sistemas externos ou modifica arquivos.
*   **Use `alwaysApply: true` com Cautela:** Para regras MDC que usam MCPs, `alwaysApply: true` pode ser útil para garantir que o contexto esteja sempre disponível, mas use com cautela para evitar sobrecarga de contexto desnecessária.
*   **Documente Suas Regras:** Mantenha seus arquivos `.mdc` bem documentados, explicando o propósito de cada regra e como ela utiliza os MCPs.

## Implementation Notes

[Use esta seção para registrar detalhes sobre a configuração de MCPs específicos, desafios de integração, estratégias de otimização e quaisquer adaptações necessárias para o ambiente do Cursor.]

## MDC Compliance Checklist

- [ ] **MCPs Essenciais Configurados:** Todos os MCPs necessários para o projeto estão configurados no Cursor.
- [ ] **Uso Contextualizado:** MCPs são utilizados de forma relevante para o contexto da tarefa.
- [ ] **Prompts Otimizados:** Prompts utilizam a sintaxe `@` de forma eficaz para referenciar MCPs.
- [ ] **Segurança na Autenticação:** Credenciais para MCPs externos (e.g., PATs) são armazenadas de forma segura.
- [ ] **Feedback de Operação:** O Cursor fornece feedback claro sobre as ações do MCP.
- [ ] **Documentação de MCPs Customizados:** MCPs personalizados são bem documentados (e.g., `linear_mcp_rules.mdc`).
- [ ] **Validação de Saídas:** Ações e código gerado via MCP são revisados e validados.




## Sugestões de Projetos de MCPs Mais Usados na Fase de Desenvolvimento

Para otimizar o fluxo de trabalho de desenvolvimento, alguns MCPs se destacam pela sua utilidade e frequência de uso. A seguir, uma lista dos mais relevantes e seus casos de uso:

### 1. MCP para Gerenciamento de Projetos (e.g., Linear, Jira, Trello)

*   **Propósito:** Conectar o Cursor a ferramentas de gerenciamento de projetos para automatizar a criação, atualização e consulta de issues, tarefas e projetos.
*   **Casos de Uso:**
    *   **Criação de Issues:** Gerar automaticamente issues de bug ou feature a partir de trechos de código ou descrições de problemas no IDE.
    *   **Atualização de Status:** Mudar o status de uma tarefa no Linear quando um commit relacionado é feito ou uma feature é concluída.
    *   **Contexto de Tarefa:** Recuperar a descrição completa de uma issue do Linear para que a IA possa entender o objetivo da tarefa antes de gerar código.
    *   **Vinculação de Commits:** Garantir que cada commit esteja associado a uma issue, melhorando a rastreabilidade.
*   **Por que é crucial:** Mantém o time alinhado, automatiza a burocracia e garante que o desenvolvimento esteja sempre ligado aos objetivos do projeto.

### 2. MCP para Documentação e Base de Conhecimento (e.g., Notion, Confluence, Wiki Interna)

*   **Propósito:** Fornecer à IA acesso a documentação interna, especificações de design, FAQs e bases de conhecimento para um contexto rico e preciso.
*   **Casos de Uso:**
    *   **Geração de Código:** A IA pode consultar a documentação de arquitetura para garantir que o código gerado esteja em conformidade com os padrões internos.
    *   **Resolução de Dúvidas:** Responder a perguntas sobre o sistema, APIs internas ou processos de desenvolvimento consultando a base de conhecimento.
    *   **Atualização de Documentação:** Sugerir ou gerar atualizações para a documentação técnica com base em novas funcionalidades ou refatorações.
*   **Por que é crucial:** Reduz a dependência de conhecimento tribal, acelera o onboarding e garante que a IA e os desenvolvedores tenham acesso à 


informação mais precisa.

### 3. MCP para Sistemas de Controle de Versão (e.g., GitHub, GitLab, Bitbucket)

*   **Propósito:** Estender as capacidades do `@Git` nativo do Cursor, permitindo interações mais complexas com o repositório remoto, como gerenciamento de Pull Requests, revisões de código e automação de workflows.
*   **Casos de Uso:**
    *   **Revisão de Código Assistida por IA:** A IA pode analisar um Pull Request, identificar potenciais bugs, sugerir melhorias de estilo ou performance e até mesmo gerar comentários para a revisão.
    *   **Automação de PRs:** Criar Pull Requests automaticamente após a conclusão de uma feature branch, preenchendo a descrição com base nos commits e na issue relacionada.
    *   **Análise de Histórico:** Consultar o histórico de commits de um arquivo ou módulo para entender a evolução e as decisões de design.
*   **Por que é crucial:** Otimiza o processo de revisão de código, melhora a qualidade do software e acelera a integração contínua.

### 4. MCP para Ferramentas de CI/CD (e.g., GitHub Actions, GitLab CI, Jenkins)

*   **Propósito:** Permitir que a IA interaja com pipelines de CI/CD para acionar builds, verificar status de testes, analisar logs de deploy e automatizar a resolução de falhas.
*   **Casos de Uso:**
    *   **Acionamento de Builds:** Iniciar um pipeline de CI/CD diretamente do IDE após uma mudança significativa no código.
    *   **Análise de Falhas:** Quando um teste falha, a IA pode analisar os logs do CI/CD, identificar a causa raiz e sugerir uma correção.
    *   **Monitoramento de Deploy:** Verificar o status de um deploy e notificar o desenvolvedor sobre o sucesso ou falha.
*   **Por que é crucial:** Acelera o ciclo de feedback do desenvolvimento, reduz o tempo de inatividade e melhora a confiabilidade das entregas.

### 5. MCP para Ferramentas de Monitoramento e Observabilidade (e.g., Prometheus, Grafana, Sentry)

*   **Propósito:** Conectar o Cursor a sistemas de monitoramento para que a IA possa diagnosticar problemas em produção, analisar métricas de performance e identificar anomalias.
*   **Casos de Uso:**
    *   **Diagnóstico de Incidentes:** Quando um alerta de produção é acionado, a IA pode consultar logs e métricas para identificar a causa do problema e sugerir soluções.
    *   **Otimização de Performance:** Analisar dados de performance de uma aplicação e sugerir otimizações de código ou infraestrutura.
    *   **Análise de Erros:** Recuperar detalhes de erros de ferramentas como Sentry e ajudar a depurar o problema diretamente no IDE.
*   **Por que é crucial:** Permite uma resposta mais rápida a incidentes, melhora a estabilidade das aplicações e otimiza o uso de recursos.

### 6. MCP para Ferramentas de Segurança (e.g., SAST/DAST, Gerenciadores de Vulnerabilidades)

*   **Propósito:** Integrar o Cursor com ferramentas de segurança para que a IA possa identificar, analisar e sugerir correções para vulnerabilidades de segurança no código.
*   **Casos de Uso:**
    *   **Análise de Código Seguro:** A IA pode usar um MCP de SAST para verificar o código em busca de padrões de vulnerabilidade e sugerir correções antes mesmo do commit.
    *   **Gerenciamento de Vulnerabilidades:** Consultar um gerenciador de vulnerabilidades para obter detalhes sobre falhas conhecidas e ajudar a priorizar e resolver problemas de segurança.
*   **Por que é crucial:** Fortalece a postura de segurança do software, integrando práticas de DevSecOps diretamente no fluxo de trabalho do desenvolvedor.

Ao integrar esses tipos de MCPs, o Cursor se torna uma ferramenta ainda mais poderosa, capaz de automatizar e otimizar diversas facetas do ciclo de vida do desenvolvimento de software.

