---
description: "Guia de melhores práticas para configurar projetos no Cursor IDE, incluindo settings.json, ESLint, TypeScript e outras ferramentas, para otimizar o desenvolvimento assistido por IA."
globs: ["docs/project_configuration_best_practices.md"]
alwaysApply: true
---

# Guia de Melhores Práticas para Configuração de Projetos no Cursor IDE

Este guia detalha as melhores práticas para configurar projetos no Cursor IDE, garantindo um ambiente de desenvolvimento otimizado para a colaboração com a IA. Uma configuração robusta e consistente é fundamental para maximizar a eficiência, a qualidade do código e a experiência do desenvolvedor.

## Princípios Essenciais para Configuração de Projetos

*   **Consistência:** Manter configurações uniformes em toda a equipe e entre projetos.
*   **Otimização para IA:** Configurar ferramentas para fornecer o melhor contexto possível à IA e aproveitar suas capacidades.
*   **Automação:** Reduzir a intervenção manual através de configurações que automatizam tarefas repetitivas.
*   **Clareza e Documentação:** Configurações devem ser claras, bem documentadas e fáceis de entender.

## 1. `settings.json` do Cursor

O arquivo `settings.json` é o coração da configuração do seu ambiente de desenvolvimento no Cursor. Ele deve ser configurado para otimizar a interação com a IA e o fluxo de trabalho.

### 1.1. Configurações Gerais do Cursor

*   **`editor.formatOnSave`:** `true` - Garante que o código seja formatado automaticamente ao salvar, mantendo a consistência.
*   **`editor.codeActionsOnSave`:**
    ```json
    {
        "source.fixAll.eslint": "explicit",
        "source.organizeImports": "explicit"
    }
    ```
    *   Permite que o ESLint corrija automaticamente problemas e organize imports ao salvar.
*   **`files.eol`:** `"\n"` - Garante consistência nas quebras de linha (LF) entre diferentes sistemas operacionais.
*   **`files.trimTrailingWhitespace`:** `true` - Remove espaços em branco desnecessários no final das linhas.
*   **`files.insertFinalNewline`:** `true` - Garante que todos os arquivos terminem com uma nova linha.

### 1.2. Configurações Específicas para IA

*   **`cursor.model`:** Defina o modelo de IA padrão a ser usado. Pode ser sobrescrito por regras MDC ou prompts específicos.
    ```json
    "cursor.model": "Claude-4 Sonnet" // Ou "Gemini 2.5 Pro", "OpenAI o3"
    ```
*   **`cursor.context.maxTokens`:** Ajuste o tamanho máximo do contexto que a IA pode receber. Um valor maior pode melhorar a compreensão, mas pode aumentar o custo e o tempo de resposta.
    ```json
    "cursor.context.maxTokens": 128000 // Exemplo para Gemini 2.5 Pro
    ```
*   **`cursor.context.exclude`:** Use para excluir arquivos ou diretórios que não devem ser enviados para a IA, reduzindo o ruído e otimizando o uso de tokens. Complementa o `.cursorignore`.
    ```json
    "cursor.context.exclude": [
        "**/node_modules/**",
        "**/dist/**",
        "**/*.log",
        "**/*.min.js"
    ]
    ```
*   **`cursor.agent.autoCommit`:** `false` - Recomenda-se desabilitar o auto-commit para que o desenvolvedor tenha controle total sobre as alterações antes de comitar.

### 1.3. Integração com Outras Ferramentas

*   **`terminal.integrated.defaultProfile.linux`:** Configure o terminal padrão para um shell que você prefere (e.g., `bash`, `zsh`).
*   **`git.autofetch`:** `true` - Mantém o repositório local atualizado com as mudanças remotas.

## 2. ESLint e Prettier

ESLint e Prettier são essenciais para manter a qualidade e a consistência do código, o que é vital para a IA entender e gerar código que se encaixe nos padrões do projeto.

### 2.1. Configuração do ESLint (`.eslintrc.js` ou `.eslintrc.json`)

*   **Extensões:** Utilize extensões recomendadas para a sua stack (e.g., `eslint-config-airbnb`, `plugin:react/recommended`, `plugin:@typescript-eslint/recommended`).
*   **Regras Personalizadas:** Defina regras específicas do projeto para garantir a conformidade com os padrões internos.
*   **Integração com TypeScript:** Se estiver usando TypeScript, configure o `@typescript-eslint/parser` e os plugins relevantes.

### 2.2. Configuração do Prettier (`.prettierrc.js` ou `.prettierrc.json`)

*   **Formatação Consistente:** Defina regras de formatação (e.g., `tabWidth`, `singleQuote`, `semi`) para garantir que todo o código seja formatado de maneira uniforme.
*   **Integração com ESLint:** Use `eslint-config-prettier` e `eslint-plugin-prettier` para desabilitar regras do ESLint que conflitam com o Prettier e para rodar o Prettier como uma regra do ESLint.

## 3. `tsconfig.json` (para Projetos TypeScript)

Uma configuração robusta do `tsconfig.json` é crucial para a IA entender a estrutura do seu projeto TypeScript, tipos e módulos.

*   **`strict`:** `true` - Habilita todas as opções de verificação de tipo estritas, melhorando a qualidade do código e a capacidade da IA de inferir tipos.
*   **`forceConsistentCasingInFileNames`:** `true` - Garante que os nomes dos arquivos sejam consistentes, evitando problemas em diferentes sistemas operacionais.
*   **`noUnusedLocals` e `noUnusedParameters`:** `true` - Ajuda a identificar código morto, o que a IA pode auxiliar a remover.
*   **`paths` e `baseUrl`:** Configure aliases de caminho para facilitar a importação de módulos, o que ajuda a IA a navegar pela base de código.

## 4. Arquivos de Ignorar (`.cursorignore`, `.gitignore`, `.eslintignore`)

Gerenciar o que é ignorado é tão importante quanto gerenciar o que é incluído. Isso reduz o ruído para a IA e para o controle de versão.

*   **`.cursorignore`:** Exclui arquivos e diretórios do contexto que o Cursor envia para a IA. Use para arquivos de build, logs, node_modules, etc.
*   **`.gitignore`:** Exclui arquivos do controle de versão Git.
*   **`.eslintignore`:** Exclui arquivos da análise do ESLint.

## 5. Outras Ferramentas e Configurações

*   **`package.json` (scripts):** Defina scripts úteis (e.g., `start`, `build`, `test`, `lint`) que a IA pode invocar via `@Terminal`.
*   **Variáveis de Ambiente:** Utilize arquivos `.env` ou gerenciadores de segredos para credenciais e configurações sensíveis, nunca as codifique diretamente.
*   **Docker (`Dockerfile`, `docker-compose.yml`):** Se o projeto usa Docker, garanta que os arquivos de configuração estejam otimizados para desenvolvimento e produção, e que a IA possa entendê-los para auxiliar na conteinerização.

## Implementation Notes

[Use esta seção para registrar decisões específicas de configuração do projeto, desafios encontrados ao integrar ferramentas e quaisquer adaptações necessárias para o ambiente do Cursor.]

## MDC Compliance Checklist

- [ ] **`settings.json` Otimizado:** Configurações gerais e de IA ajustadas para o Cursor.
- [ ] **ESLint Configurado:** Regras de linting e formatação consistentes.
- [ ] **Prettier Configurado:** Formatação automática e consistente.
- [ ] **`tsconfig.json` Robusto:** Configurações TypeScript estritas e claras.
- [ ] **Arquivos de Ignorar:** `.cursorignore`, `.gitignore`, `.eslintignore` configurados corretamente.
- [ ] **Scripts Úteis:** `package.json` com scripts de automação.
- [ ] **Segurança de Credenciais:** Variáveis de ambiente ou gerenciadores de segredos para dados sensíveis.
- [ ] **Documentação:** Todas as configurações importantes documentadas.


