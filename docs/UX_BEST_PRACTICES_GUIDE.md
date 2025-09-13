---
description: "Guia de melhores práticas de UX para desenvolvimento de software, com foco em usabilidade, acessibilidade e design centrado no usuário, otimizado para o Cursor."
globs: ["docs/UX_BEST_PRACTICES_GUIDE.md"]
alwaysApply: true
---

# Guia de Melhores Práticas de UX para Desenvolvimento de Software

Este guia, elaborado com a perspectiva de um especialista em UX, visa fornecer diretrizes e melhores práticas para a criação de software com uma experiência de usuário excepcional. A integração desses princípios desde o início do ciclo de desenvolvimento é fundamental para o sucesso do produto.

## Princípios Fundamentais de UX

1.  **Design Centrado no Usuário (UCD):** O usuário está no centro de todas as decisões de design e desenvolvimento. Entenda suas necessidades, objetivos e frustrações.
2.  **Usabilidade:** O software deve ser fácil de usar, aprender e lembrar. A interface deve ser intuitiva e eficiente.
3.  **Acessibilidade (A11y):** O software deve ser acessível a todos, incluindo pessoas com deficiências. Siga as diretrizes WCAG (Web Content Accessibility Guidelines).
4.  **Consistência:** A interface e a interação devem ser consistentes em todo o produto, seguindo padrões de design estabelecidos.
5.  **Feedback:** O sistema deve fornecer feedback claro e imediato ao usuário sobre suas ações e o estado atual.
6.  **Simplicidade:** Evite complexidade desnecessária. A interface deve ser limpa, organizada e focada nas tarefas essenciais.

## Processo de UX no Desenvolvimento

### 1. Pesquisa e Descoberta

*   **Pesquisa com Usuários:** Realize entrevistas, pesquisas e observações para entender o público-alvo.
*   **Análise de Concorrentes:** Analise produtos concorrentes para identificar pontos fortes, fracos e oportunidades.
*   **Criação de Personas:** Desenvolva personas que representem os diferentes tipos de usuários do seu produto.
*   **Jornadas do Usuário:** Mapeie as jornadas do usuário para visualizar como eles interagem com o produto para atingir seus objetivos.

### 2. Design e Prototipação

*   **Arquitetura da Informação:** Organize e estruture o conteúdo de forma lógica e intuitiva.
*   **Wireframes:** Crie wireframes de baixa fidelidade para esboçar a estrutura e o layout das telas.
*   **Protótipos Interativos:** Desenvolva protótipos de alta fidelidade para simular a interação do usuário e testar fluxos.
*   **Design System:** Crie ou utilize um design system para garantir consistência visual e de componentes.

### 3. Testes e Validação

*   **Testes de Usabilidade:** Realize testes com usuários reais para identificar problemas de usabilidade e obter feedback.
*   **Testes A/B:** Compare diferentes versões de um design para determinar qual tem melhor desempenho.
*   **Análise de Métricas:** Utilize ferramentas de análise para coletar dados sobre o comportamento do usuário e identificar áreas de melhoria.

## Melhores Práticas de UI (User Interface)

*   **Hierarquia Visual:** Utilize tamanho, cor, contraste e espaçamento para criar uma hierarquia visual clara e guiar a atenção do usuário.
*   **Tipografia:** Escolha fontes legíveis e utilize uma escala tipográfica consistente.
*   **Cores:** Utilize uma paleta de cores coesa e que reforce a identidade da marca. Garanta que o contraste de cores atenda aos padrões de acessibilidade.
*   **Ícones e Imagens:** Utilize ícones e imagens de forma significativa para complementar o conteúdo e melhorar a compreensão.
*   **Formulários:** Projete formulários fáceis de preencher, com rótulos claros, validação em tempo real e mensagens de erro úteis.
*   **Navegação:** Crie uma navegação clara e consistente que permita ao usuário se orientar facilmente no produto.

## Acessibilidade (A11y)

*   **Contraste de Cores:** Garanta que o contraste entre o texto e o fundo atenda aos requisitos mínimos da WCAG.
*   **Texto Alternativo para Imagens:** Forneça texto alternativo descritivo para todas as imagens.
*   **Navegação por Teclado:** Garanta que todos os elementos interativos possam ser acessados e operados via teclado.
*   **Legendas e Transcrições:** Forneça legendas para vídeos e transcrições para conteúdo de áudio.
*   **ARIA (Accessible Rich Internet Applications):** Utilize atributos ARIA para melhorar a acessibilidade de componentes dinâmicos e complexos.

## Ferramentas e Recursos

*   **Figma, Sketch, Adobe XD:** Ferramentas de design e prototipação.
*   **Maze, UserTesting:** Plataformas para testes de usabilidade remotos.
*   **Google Analytics, Hotjar:** Ferramentas de análise de comportamento do usuário.
*   **WCAG (Web Content Accessibility Guidelines):** Diretrizes para acessibilidade na web.
*   **Material Design, Human Interface Guidelines:** Guias de design para Android e iOS.

## Integração com Cursor IDE e Agentes de IA para UX

Para maximizar a eficiência e a qualidade do UX Design no desenvolvimento assistido por IA, o Cursor IDE e seus agentes podem ser utilizados de forma estratégica:

*   **Pesquisa de Usuários Aprimorada por IA:**
    *   **Análise de Transcrições:** Utilize o Cursor para analisar transcrições de entrevistas ou sessões de feedback, identificando padrões, sentimentos e pontos de dor comuns.
    *   **Geração de Perguntas:** Agentes de IA podem sugerir perguntas para questionários ou roteiros de entrevistas com base em personas e objetivos do projeto.
    *   **Síntese de Dados:** O Cursor pode ajudar a sintetizar grandes volumes de dados de pesquisa, gerando resumos e insights acionáveis.

*   **Prototipagem e Testes Assistidos por IA:**
    *   **Geração de Trechos de Código para UI:** Agentes podem gerar componentes de UI (HTML/CSS/JS) a partir de descrições de wireframes ou protótipos, acelerando a criação de protótipos funcionais.
    *   **Simulação de Interações:** Agentes de IA podem simular interações de usuário em protótipos, identificando fluxos quebrados ou pontos de confusão antes dos testes com usuários reais.
    *   **Feedback Automatizado:** O Cursor pode analisar o código de protótipos e sugerir melhorias de usabilidade ou acessibilidade com base nas `Project Rules` de UX.

*   **Verificação de Acessibilidade Automatizada:**
    *   **Análise Estática de Código:** Integre o Cursor com ferramentas de análise estática para identificar automaticamente problemas de acessibilidade no código (e.g., falta de `alt` tags, contraste insuficiente, estrutura semântica inadequada).
    *   **Sugestões de Correção:** O Cursor pode propor correções para problemas de acessibilidade, aplicando as diretrizes WCAG diretamente no código.

## UX para Ferramentas de IA e Desenvolvedores

Ao projetar ferramentas de desenvolvimento assistidas por IA, como o Cursor, é crucial aplicar os princípios de UX para garantir que a experiência do desenvolvedor seja eficiente e agradável:

*   **Clareza na Interação com IA:**
    *   **Prompts e Respostas:** As interações com a IA devem ser claras, concisas e diretas. As respostas devem ser úteis e acionáveis, evitando ambiguidades.
    *   **Feedback Visual:** O IDE deve fornecer feedback visual claro sobre o que a IA está fazendo (e.g., 

