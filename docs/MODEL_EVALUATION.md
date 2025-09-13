---
description: "Análise e recomendações de modelos de IA para o Cursor IDE, baseadas em critérios de aderência MDC, gerenciamento de contexto, qualidade da saída, colaboração e performance."
globs: ["docs/MODEL_EVALUATION.md"]
alwaysApply: true
---

# Avaliação e Recomendações de Modelos de IA para o Cursor IDE

Este documento estabelece os critérios e o processo para avaliar e recomendar modelos de IA a serem utilizados no Cursor IDE, garantindo que eles se alinhem com a metodologia de Desenvolvimento de Software Disciplinado por IA e as `Project Rules` do projeto `rules`.

## Critérios de Avaliação de Modelos de IA

Os modelos de IA serão avaliados com base nos seguintes critérios:

1.  **Aderência às `Project Rules` (MDC Compliance):**
    *   Capacidade do modelo de entender e aplicar as regras definidas nos arquivos `.mdc`.
    *   Precisão na aplicação de `globs`, `alwaysApply` e `description` para o contexto.
    *   Habilidade de seguir as diretrizes de `Architectural Compliance & Quality Gates` e `MDC Compliance Checklist`.

2.  **Gerenciamento de Contexto e Memória:**
    *   Eficácia na utilização do contexto fornecido (código, documentação, `Project Rules`, `User Rules`).
    *   Capacidade de manter a coerência e a relevância ao longo de interações mais longas (memória de conversação).
    *   Habilidade de referenciar e integrar informações de `Memories` e `Codebase Indexing` do Cursor.

3.  **Qualidade da Saída (Código, Texto, Sugestões):**
    *   Precisão e correção do código gerado ou sugerido.
    *   Qualidade da linguagem natural (clareza, concisão, gramática).
    *   Relevância e utilidade das sugestões e refatorações.
    *   Conformidade com as `User Rules` (e.g., sinalização de incerteza, tom profissional).

4.  **Colaboração e Interatividade:**
    *   Facilidade de interação com o modelo (clareza nas perguntas, capacidade de seguir instruções complexas).
    *   Habilidade de pedir esclarecimentos ou informações adicionais quando o contexto é insuficiente.
    *   Capacidade de se adaptar ao feedback do usuário e aprender com as correções.

5.  **Performance e Latência:**
    *   Velocidade de resposta do modelo para diferentes tipos de tarefas (geração de código, refatoração, explicação).
    *   Eficiência no uso de recursos computacionais.

## Processo de Avaliação

1.  **Definição de Cenários de Teste:** Criar um conjunto de cenários de teste que cubram diferentes aspectos do desenvolvimento (e.g., geração de nova funcionalidade, refatoração de código existente, depuração, escrita de testes, documentação).
2.  **Execução dos Testes:** Executar cada modelo de IA através dos cenários de teste, registrando as interações e os resultados.
3.  **Análise e Pontuação:** Avaliar a saída de cada modelo com base nos critérios definidos, atribuindo pontuações e comentários detalhados.
4.  **Recomendações:** Formular recomendações sobre quais modelos são mais adequados para diferentes tipos de tarefas ou fases do desenvolvimento, e identificar áreas para melhoria.

## Recomendações Atuais

[Esta seção será preenchida com as recomendações específicas após a execução do processo de avaliação. Exemplo:

*   **Modelo A (e.g., GPT-4o):** Recomendado para tarefas de geração de código complexas e refatoração, devido à sua alta qualidade de saída e aderência às `Project Rules`.
*   **Modelo B (e.g., Claude 3 Opus):** Recomendado para análise de código e depuração, devido à sua capacidade superior de gerenciamento de contexto e explicação.
*   **Modelo C (e.g., Gemini 1.5 Pro):** Recomendado para tarefas de documentação e geração de testes, devido à sua eficiência e boa qualidade de texto.]

## Implementation Notes

[Use esta seção para registrar decisões sobre a escolha de modelos, desafios encontrados na avaliação e planos para reavaliações futuras.]

## MDC Compliance Checklist

- [ ] **Critérios Definidos:** Critérios de avaliação de modelos claros e abrangentes.
- [ ] **Processo de Avaliação:** Processo de avaliação estruturado e replicável.
- [ ] **Recomendações Baseadas em Dados:** Recomendações fundamentadas em evidências.
- [ ] **Aderência às Rules:** Modelos avaliados pela capacidade de seguir as `Project Rules`.
- [ ] **Gerenciamento de Contexto:** Modelos avaliados pela eficácia no uso do contexto do Cursor.


