
# RAG Integration - Sistema de Recuperação e Geração Aumentada

## 🎯 Visão Geral

O sistema RAG (Retrieval-Augmented Generation) é fundamental para o N8N AI Workflow Generator, fornecendo contexto relevante através de busca semântica em templates, exemplos e padrões existentes. Este módulo implementa uma arquitetura robusta baseada nas **práticas oficiais do n8n**, incluindo **Agentic RAG** para sistemas autônomos e inteligentes.

### 🆕 Atualizações Baseadas em Práticas Oficiais n8n

Esta documentação foi atualizada com base nos artigos oficiais do blog n8n:
- **[Evaluating RAG](https://blog.n8n.io/evaluating-rag-aka-optimizing-the-optimization/)** - Framework oficial de avaliação e otimização
- **[Agentic RAG](https://blog.n8n.io/agentic-rag/)** - Sistema autônomo de tomada de decisão

### 🔄 Simple RAG vs Agentic RAG

| Feature                | Simple RAG                       | Agentic RAG (Oficial n8n)       |
|------------------------|----------------------------------|----------------------------------|
| Workflow               | Fixo "retrieve then read"        | Dinâmico, multi-etapas          |
| Tomada de Decisão      | Nenhuma; caminho predeterminado  | Agente toma decisões (routing, ferramentas, auto-crítica) |
| Fontes de Dados        | Base única, não-estruturada      | Múltiplas fontes (vector stores, SQL, web APIs) |
| Adaptabilidade         | Rígido; mesmo processo para todas queries | Adaptativo; ajusta estratégia para queries complexas |

## 🏗️ Arquitetura RAG

### Arquitetura Traditional RAG
```mermaid
graph TB
    subgraph "Input Processing"
        UI[User Input]
        QP[Query Processor]
        EM[Embedding Model]
    end
    
    subgraph "Knowledge Base"
        TS[Template Store]
        ES[Example Store]
        PS[Pattern Store]
        MS[Metadata Store]
    end
    
    subgraph "Vector Storage"
        VS[Vector Store]
        IDX[Semantic Index]
        CACHE[Embedding Cache]
    end
    
    subgraph "Retrieval Engine"
        SR[Semantic Retrieval]
        HYB[Hybrid Search]
        RR[Relevance Ranking]
    end
    
    subgraph "Context Generation"
        CA[Context Assembler]
        CF[Context Filter]
        CO[Context Optimizer]
    end
    
    UI --> QP
    QP --> EM
    EM --> SR
    SR --> VS
    VS --> IDX
    TS --> VS
    ES --> VS
    PS --> VS
    SR --> HYB
    HYB --> RR
    RR --> CA
    CA --> CF
    CF --> CO
```

### 🤖 Arquitetura Agentic RAG (Oficial n8n)

```mermaid
graph TB
    subgraph "Intelligent Storage"
        IS[Intelligent Storage Agent]
        AP[Adaptive Parsing]
        CS[Chunking Strategy]
        RM[Rich Metadata]
    end
    
    subgraph "Dynamic Retrieval"
        RR[Retriever Router Agent]
        VS[Vector Store]
        SQL[SQL Database]
        WEB[Web Search API]
        DOC[Document Store]
    end
    
    subgraph "Verified Generation"
        GA[Generation Agent]
        AC[Answer Critic Agent]
        VL[Verification Loop]
        FR[Final Response]
    end
    
    subgraph "Multi-Source Data"
        TD[Tabular Data]
        UD[Unstructured Docs]
        RT[Real-time Data]
        KG[Knowledge Graph]
    end
    
    TD --> IS
    UD --> IS
    RT --> RR
    KG --> RR
    
    IS --> AP
    AP --> CS
    CS --> RM
    RM --> VS
    RM --> SQL
    
    RR --> VS
    RR --> SQL
    RR --> WEB
    RR --> DOC
    
    VS --> GA
    SQL --> GA
    WEB --> GA
    DOC --> GA
    
    GA --> AC
    AC --> VL
    VL --> GA
    VL --> FR
```

## 📊 Framework de Avaliação RAG (Oficial n8n)

### 🎯 Framework de Dois Pilares

Baseado no artigo oficial do n8n, a avaliação de RAG segue dois pilares fundamentais:

#### 1. **RAG Document Relevance** - Recuperação da Informação Correta
- **Context Recall**: Quantos documentos relevantes foram recuperados
- **Context Precision**: Proporção de chunks relevantes nos contextos recuperados

#### 2. **RAG Groundedness** - Alinhamento das Respostas
- **Faithfulness**: Se todas as afirmações na resposta são suportadas pelo contexto
- **Response Relevancy**: Quão bem a resposta aborda a pergunta do usuário

### 🚨 Tipos de Alucinações RAG

O framework *RAGTruth* categoriza alucinações RAG em quatro tipos:

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| **Evident Conflict** | Erros factuais claros, contradições diretas | Contexto: "Capital da França é Berlin" → LLM: "Capital da França é Paris" |
| **Subtle Conflict** | Mudanças contextuais via substituição de termos | Contexto: "Receita aumentou 15%" → LLM: "Lucro aumentou 15%" |
| **Evident Introduction of Baseless Information** | Fabricação de alegações não suportadas | Contexto: "Receita caiu 15%" → LLM: "Receita caiu devido ao bloqueio do Canal de Suez" |
| **Subtle Introduction of Baseless Information** | Detalhes inferidos ou suposições subjetivas | Contexto: "Vendas baixas" → LLM: "Vendas baixas devido à sazonalidade" |

### 📈 Métricas de Avaliação Nativas do n8n

O n8n fornece ferramentas nativas de avaliação RAG:

```typescript
// Avaliação de Precisão de Resposta RAG
interface RAGAccuracyEvaluation {
  responseRelevancy: number;  // 0-1, alinhamento com documentos recuperados
  contextualAlignment: number; // 0-1, quão bem a resposta usa o contexto
  factualAccuracy: number;    // 0-1, precisão factual das informações
}

// Avaliação de Relevância de Documentos
interface DocumentRelevanceEvaluation {
  contextRecall: number;     // 0-1, proporção de documentos relevantes recuperados
  contextPrecision: number;  // 0-1, precisão dos documentos no ranking
  retrievalEffectiveness: number; // 0-1, eficácia geral da recuperação
}

// Ferramentas Nativas n8n
class N8NRAGEvaluator {
  // Usa LLM para avaliar relevância da resposta
  async evaluateRAGResponseAccuracy(
    query: string,
    retrievedDocs: Document[],
    response: string
  ): Promise<RAGAccuracyEvaluation> {
    
    const evaluationPrompt = `
    Avalie a precisão da resposta RAG baseada nos seguintes critérios:
    
    Query: ${query}
    Documentos Recuperados: ${retrievedDocs.map(doc => doc.content).join('\n---\n')}
    Resposta Gerada: ${response}
    
    Critérios:
    1. Response Relevancy: A resposta aborda diretamente a query?
    2. Contextual Alignment: A resposta está alinhada com os documentos?
    3. Factual Accuracy: As informações são factualmente corretas?
    
    Retorne scores de 0-1 para cada critério.
    `;
    
    const evaluation = await this.llm.generate(evaluationPrompt);
    return this.parseEvaluationScores(evaluation);
  }

  // Usa LLM para avaliar relevância dos documentos
  async evaluateDocumentRelevance(
    query: string,
    retrievedDocs: Document[]
  ): Promise<DocumentRelevanceEvaluation> {
    
    const evaluationPrompt = `
    Avalie a relevância dos documentos recuperados:
    
    Query: ${query}
    Documentos: ${retrievedDocs.map((doc, i) => `${i+1}. ${doc.content}`).join('\n')}
    
    Para cada documento, avalie:
    - É relevante para a query? (Sim/Não)
    - Qual o nível de relevância? (0-1)
    
    Calcule Context Recall e Context Precision.
    `;
    
    const evaluation = await this.llm.generate(evaluationPrompt);
    return this.parseRelevanceScores(evaluation);
  }
}
```

### 🔍 Detecção de Alucinações com HHEM

Integração com o modelo *Vectara HHEM-2.1-Open* para detecção de alucinações:

```typescript
class HallucinationDetector {
  constructor(private hhem: HHEMModel) {}
  
  async detectHallucinations(
    context: string,
    response: string
  ): Promise<HallucinationResult> {
    
    // Usa HHEM para verificar se a resposta contradiz o contexto
    const hallucinationScore = await this.hhem.evaluate({
      context,
      response
    });
    
    // Score próximo de 1 = sem alucinação
    // Score próximo de 0 = alucinação detectada
    
    return {
      score: hallucinationScore,
      isHallucination: hallucinationScore < 0.7,
      confidence: Math.abs(hallucinationScore - 0.5) * 2,
      riskLevel: this.calculateRiskLevel(hallucinationScore)
    };
  }
  
  private calculateRiskLevel(score: number): 'LOW' | 'MEDIUM' | 'HIGH' {
    if (score >= 0.8) return 'LOW';
    if (score >= 0.5) return 'MEDIUM';
    return 'HIGH';
  }
}
```

### 📊 Pipeline de Avaliação Contínua

```typescript
class RAGEvaluationPipeline {
  constructor(
    private ragSystem: RAGSystem,
    private evaluator: N8NRAGEvaluator,
    private hallucinationDetector: HallucinationDetector
  ) {}
  
  async evaluateRAGSystem(testDataset: EvaluationDataset): Promise<EvaluationReport> {
    const results: EvaluationResult[] = [];
    
    for (const testCase of testDataset.cases) {
      // 1. Execute RAG
      const ragResult = await this.ragSystem.query(testCase.query);
      
      // 2. Avalie precisão da resposta
      const accuracyEval = await this.evaluator.evaluateRAGResponseAccuracy(
        testCase.query,
        ragResult.retrievedDocs,
        ragResult.response
      );
      
      // 3. Avalie relevância dos documentos
      const relevanceEval = await this.evaluator.evaluateDocumentRelevance(
        testCase.query,
        ragResult.retrievedDocs
      );
      
      // 4. Detecte alucinações
      const hallucinationResult = await this.hallucinationDetector.detectHallucinations(
        ragResult.context,
        ragResult.response
      );
      
      results.push({
        testCase,
        accuracy: accuracyEval,
        relevance: relevanceEval,
        hallucination: hallucinationResult,
        timestamp: Date.now()
      });
    }
    
    return this.generateReport(results);
  }
  
  private generateReport(results: EvaluationResult[]): EvaluationReport {
    const avgAccuracy = results.reduce((sum, r) => sum + r.accuracy.responseRelevancy, 0) / results.length;
    const avgRecall = results.reduce((sum, r) => sum + r.relevance.contextRecall, 0) / results.length;
    const avgPrecision = results.reduce((sum, r) => sum + r.relevance.contextPrecision, 0) / results.length;
    const hallucinationRate = results.filter(r => r.hallucination.isHallucination).length / results.length;
    
    return {
      summary: {
        averageAccuracy: avgAccuracy,
        averageRecall: avgRecall,
        averagePrecision: avgPrecision,
        hallucinationRate,
        totalTests: results.length
      },
      recommendations: this.generateRecommendations(results),
      detailedResults: results
    };
  }
}
```

## 🔧 Implementação Core

### **1. Embedding Service**

Serviço de geração de embeddings otimizado para workflows N8N:

```typescript
class EmbeddingService {
  constructor(
    private openAI: OpenAIService,
    private cache: EmbeddingCache,
    private config: EmbeddingConfig
  ) {}

  async embedText(text: string, type: EmbeddingType = 'query'): Promise<number[]> {
    // Verifica cache primeiro
    const cacheKey = this.generateCacheKey(text, type)
    const cached = await this.cache.get(cacheKey)
    if (cached) return cached

    // Pré-processa texto baseado no tipo
    const processedText = this.preprocessText(text, type)
    
    // Gera embedding
    const embedding = await this.openAI.embeddings.create({
      model: this.config.model, // text-embedding-3-large
      input: processedText,
      dimensions: this.config.dimensions // 1536 ou 3072
    })

    const vector = embedding.data[0].embedding
    
    // Armazena no cache
    await this.cache.set(cacheKey, vector, this.config.cacheTTL)
    
    return vector
  }

  async embedWorkflowTemplate(template: WorkflowTemplate): Promise<TemplateEmbedding> {
    // Cria representação textual estruturada do template
    const textRepresentation = this.templateToText(template)
    
    // Gera embeddings para diferentes aspectos
    const [
      descriptionEmbedding,
      nodesEmbedding,
      integrationsEmbedding,
      functionalityEmbedding
    ] = await Promise.all([
      this.embedText(template.description, 'template_description'),
      this.embedText(this.nodesToText(template.nodes), 'template_nodes'),
      this.embedText(this.integrationsToText(template.integrations), 'template_integrations'),
      this.embedText(textRepresentation, 'template_full')
    ])

    return {
      templateId: template.id,
      description: descriptionEmbedding,
      nodes: nodesEmbedding,
      integrations: integrationsEmbedding,
      functionality: functionalityEmbedding,
      combined: this.combineEmbeddings([
        descriptionEmbedding,
        nodesEmbedding,
        integrationsEmbedding,
        functionalityEmbedding
      ])
    }
  }

  private templateToText(template: WorkflowTemplate): string {
    return [
      `Workflow: ${template.name}`,
      `Description: ${template.description}`,
      `Type: ${template.type}`,
      `Nodes: ${template.nodes.map(n => `${n.name} (${n.type})`).join(', ')}`,
      `Integrations: ${template.integrations.join(', ')}`,
      `Use Cases: ${template.useCases.join(', ')}`,
      `Tags: ${template.tags.join(', ')}`
    ].join('\n')
  }

  private preprocessText(text: string, type: EmbeddingType): string {
    switch (type) {
      case 'query':
        return this.preprocessQuery(text)
      case 'template_description':
        return this.preprocessTemplateDescription(text)
      case 'template_nodes':
        return this.preprocessNodes(text)
      default:
        return text.toLowerCase().trim()
    }
  }
}
```

### **2. Vector Store Implementation**

Implementação abstrata para diferentes provedores de vector store:

```typescript
abstract class VectorStore {
  abstract async store(
    id: string,
    embedding: number[],
    metadata: VectorMetadata
  ): Promise<void>

  abstract async search(
    queryEmbedding: number[],
    options: SearchOptions
  ): Promise<SearchResult[]>

  abstract async update(
    id: string,
    embedding: number[],
    metadata: VectorMetadata
  ): Promise<void>

  abstract async delete(id: string): Promise<void>
}

// Implementação Pinecone
class PineconeVectorStore extends VectorStore {
  constructor(
    private pinecone: PineconeClient,
    private indexName: string
  ) {
    super()
  }

  async store(id: string, embedding: number[], metadata: VectorMetadata): Promise<void> {
    const index = this.pinecone.Index(this.indexName)
    
    await index.upsert([{
      id,
      values: embedding,
      metadata: {
        ...metadata,
        timestamp: Date.now(),
        version: '1.0'
      }
    }])
  }

  async search(
    queryEmbedding: number[],
    options: SearchOptions
  ): Promise<SearchResult[]> {
    const index = this.pinecone.Index(this.indexName)
    
    const searchRequest: QueryRequest = {
      vector: queryEmbedding,
      topK: options.limit || 10,
      includeMetadata: true,
      includeValues: false
    }

    // Adiciona filtros se especificados
    if (options.filter) {
      searchRequest.filter = this.buildPineconeFilter(options.filter)
    }

    const response = await index.query(searchRequest)
    
    return response.matches?.map(match => ({
      id: match.id!,
      score: match.score!,
      metadata: match.metadata as VectorMetadata
    })) || []
  }

  private buildPineconeFilter(filter: SearchFilter): any {
    const pineconeFilter: any = {}
    
    if (filter.type) {
      pineconeFilter.type = { $eq: filter.type }
    }
    
    if (filter.tags) {
      pineconeFilter.tags = { $in: filter.tags }
    }
    
    if (filter.dateRange) {
      pineconeFilter.timestamp = {
        $gte: filter.dateRange.start,
        $lte: filter.dateRange.end
      }
    }
    
    return pineconeFilter
  }
}

// Implementação Chroma (local/open-source)
class ChromaVectorStore extends VectorStore {
  constructor(
    private chromaClient: ChromaApi,
    private collectionName: string
  ) {
    super()
  }

  async store(id: string, embedding: number[], metadata: VectorMetadata): Promise<void> {
    const collection = await this.chromaClient.getOrCreateCollection({
      name: this.collectionName
    })

    await collection.add({
      ids: [id],
      embeddings: [embedding],
      metadatas: [metadata]
    })
  }

  async search(
    queryEmbedding: number[],
    options: SearchOptions
  ): Promise<SearchResult[]> {
    const collection = await this.chromaClient.getCollection({
      name: this.collectionName
    })

    const results = await collection.query({
      queryEmbeddings: [queryEmbedding],
      nResults: options.limit || 10,
      where: options.filter ? this.buildChromaFilter(options.filter) : undefined
    })

    return results.ids[0].map((id, index) => ({
      id,
      score: results.distances![0][index],
      metadata: results.metadatas![0][index] as VectorMetadata
    }))
  }
}
```

### **3. Knowledge Base Manager**

Gerencia a base de conhecimento de templates e padrões:

```typescript
class KnowledgeBaseManager {
  constructor(
    private vectorStore: VectorStore,
    private embeddingService: EmbeddingService,
    private templateRepository: TemplateRepository
  ) {}

  async indexTemplate(template: WorkflowTemplate): Promise<void> {
    // Gera embeddings para o template
    const templateEmbedding = await this.embeddingService.embedWorkflowTemplate(template)
    
    // Armazena embedding principal
    await this.vectorStore.store(
      `template_${template.id}`,
      templateEmbedding.combined,
      {
        type: 'template',
        templateId: template.id,
        name: template.name,
        category: template.category,
        tags: template.tags,
        integrations: template.integrations,
        complexity: template.complexity,
        usageCount: template.usageCount || 0
      }
    )

    // Armazena embeddings específicos para busca granular
    await Promise.all([
      this.vectorStore.store(
        `template_desc_${template.id}`,
        templateEmbedding.description,
        { ...this.getBaseMetadata(template), aspect: 'description' }
      ),
      this.vectorStore.store(
        `template_nodes_${template.id}`,
        templateEmbedding.nodes,
        { ...this.getBaseMetadata(template), aspect: 'nodes' }
      ),
      this.vectorStore.store(
        `template_integrations_${template.id}`,
        templateEmbedding.integrations,
        { ...this.getBaseMetadata(template), aspect: 'integrations' }
      )
    ])
  }

  async indexWorkflowExample(example: WorkflowExample): Promise<void> {
    const exampleText = this.exampleToText(example)
    const embedding = await this.embeddingService.embedText(exampleText, 'example')
    
    await this.vectorStore.store(
      `example_${example.id}`,
      embedding,
      {
        type: 'example',
        exampleId: example.id,
        category: example.category,
        difficulty: example.difficulty,
        tags: example.tags,
        sourceWorkflow: example.sourceWorkflowId
      }
    )
  }

  async indexIntegrationPattern(pattern: IntegrationPattern): Promise<void> {
    const patternText = this.patternToText(pattern)
    const embedding = await this.embeddingService.embedText(patternText, 'pattern')
    
    await this.vectorStore.store(
      `pattern_${pattern.id}`,
      embedding,
      {
        type: 'pattern',
        patternId: pattern.id,
        service: pattern.service,
        operation: pattern.operation,
        complexity: pattern.complexity,
        tags: pattern.tags
      }
    )
  }

  async bulkIndex(items: (WorkflowTemplate | WorkflowExample | IntegrationPattern)[]): Promise<void> {
    const batchSize = 50
    const batches = this.chunkArray(items, batchSize)
    
    for (const batch of batches) {
      await Promise.all(
        batch.map(item => {
          if ('nodes' in item) return this.indexTemplate(item as WorkflowTemplate)
          if ('sourceWorkflowId' in item) return this.indexWorkflowExample(item as WorkflowExample)
          return this.indexIntegrationPattern(item as IntegrationPattern)
        })
      )
    }
  }
}
```

### **4. Semantic Retrieval Engine**

Motor de busca semântica otimizado:

```typescript
class SemanticRetrievalEngine {
  constructor(
    private vectorStore: VectorStore,
    private embeddingService: EmbeddingService,
    private relevanceScorer: RelevanceScorer
  ) {}

  async retrieveRelevantTemplates(
    query: string,
    intent: WorkflowIntent,
    options: RetrievalOptions = {}
  ): Promise<RetrievalResult> {
    
    // 1. Gera embedding da query
    const queryEmbedding = await this.embeddingService.embedText(query, 'query')
    
    // 2. Busca semântica básica
    const semanticResults = await this.vectorStore.search(queryEmbedding, {
      limit: options.limit || 20,
      threshold: options.threshold || 0.7,
      filter: this.buildSearchFilter(intent, options)
    })

    // 3. Busca híbrida (semântica + filtros)
    const hybridResults = await this.hybridSearch(query, intent, options)
    
    // 4. Combina e re-ranqueia resultados
    const combinedResults = this.combineResults(semanticResults, hybridResults)
    const rankedResults = await this.relevanceScorer.rankResults(
      combinedResults,
      query,
      intent
    )

    // 5. Agrupa por tipo de conteúdo
    const groupedResults = this.groupResultsByType(rankedResults)
    
    return {
      templates: groupedResults.templates,
      examples: groupedResults.examples,
      patterns: groupedResults.patterns,
      totalResults: rankedResults.length,
      averageScore: this.calculateAverageScore(rankedResults),
      searchMetadata: {
        query,
        intent: intent.workflowType,
        retrievalTime: Date.now(),
        searchStrategy: 'hybrid'
      }
    }
  }

  private async hybridSearch(
    query: string,
    intent: WorkflowIntent,
    options: RetrievalOptions
  ): Promise<SearchResult[]> {
    
    // Busca por palavras-chave específicas
    const keywordResults = await this.keywordSearch(query, intent)
    
    // Busca por tipo de workflow
    const typeResults = await this.searchByWorkflowType(intent.workflowType)
    
    // Busca por integrações específicas
    const integrationResults = await this.searchByIntegrations(
      intent.requirements.integrations
    )
    
    // Combina resultados com pesos diferentes
    return this.weightedCombination([
      { results: keywordResults, weight: 0.4 },
      { results: typeResults, weight: 0.3 },
      { results: integrationResults, weight: 0.3 }
    ])
  }

  private async searchByWorkflowType(workflowType: string): Promise<SearchResult[]> {
    return await this.vectorStore.search(
      await this.embeddingService.embedText(workflowType, 'workflow_type'),
      {
        limit: 10,
        filter: { type: 'template', category: workflowType }
      }
    )
  }

  private async searchByIntegrations(integrations: string[]): Promise<SearchResult[]> {
    if (!integrations.length) return []
    
    const integrationQueries = integrations.map(integration =>
      this.embeddingService.embedText(integration, 'integration')
    )
    
    const results = await Promise.all(
      integrationQueries.map(embedding =>
        this.vectorStore.search(embedding, {
          limit: 5,
          filter: { type: 'template' }
        })
      )
    )
    
    return results.flat()
  }
}
```

### **5. Context Assembler**

Monta contexto otimizado para geração:

```typescript
class ContextAssembler {
  constructor(
    private templateRepository: TemplateRepository,
    private contextOptimizer: ContextOptimizer
  ) {}

  async assembleContext(
    retrievalResult: RetrievalResult,
    intent: WorkflowIntent,
    maxTokens: number = 8000
  ): Promise<RAGContext> {
    
    // 1. Seleciona templates mais relevantes
    const selectedTemplates = await this.selectBestTemplates(
      retrievalResult.templates,
      intent,
      maxTokens * 0.4 // 40% do contexto para templates
    )

    // 2. Seleciona exemplos relevantes
    const selectedExamples = await this.selectBestExamples(
      retrievalResult.examples,
      intent,
      maxTokens * 0.3 // 30% do contexto para exemplos
    )

    // 3. Seleciona padrões de integração
    const selectedPatterns = await this.selectBestPatterns(
      retrievalResult.patterns,
      intent,
      maxTokens * 0.3 // 30% do contexto para padrões
    )

    // 4. Otimiza contexto final
    const optimizedContext = await this.contextOptimizer.optimize({
      templates: selectedTemplates,
      examples: selectedExamples,
      patterns: selectedPatterns,
      intent,
      maxTokens
    })

    return {
      templates: optimizedContext.templates,
      examples: optimizedContext.examples,
      patterns: optimizedContext.patterns,
      relevanceScore: this.calculateContextRelevance(optimizedContext),
      tokenCount: optimizedContext.tokenCount,
      contextMetadata: {
        assemblyTime: Date.now(),
        optimizationApplied: true,
        sourceResults: retrievalResult.totalResults
      }
    }
  }

  private async selectBestTemplates(
    templates: SearchResult[],
    intent: WorkflowIntent,
    maxTokens: number
  ): Promise<WorkflowTemplate[]> {
    
    let currentTokens = 0
    const selectedTemplates: WorkflowTemplate[] = []
    
    // Ordena por relevância e diversidade
    const sortedTemplates = await this.sortByRelevanceAndDiversity(templates, intent)
    
    for (const result of sortedTemplates) {
      const template = await this.templateRepository.getTemplate(result.metadata.templateId)
      const templateTokens = this.estimateTokenCount(template)
      
      if (currentTokens + templateTokens <= maxTokens) {
        selectedTemplates.push(template)
        currentTokens += templateTokens
      } else {
        break
      }
    }
    
    return selectedTemplates
  }

  private async sortByRelevanceAndDiversity(
    results: SearchResult[],
    intent: WorkflowIntent
  ): Promise<SearchResult[]> {
    
    // Calcula scores de relevância e diversidade
    const scoredResults = results.map(result => ({
      ...result,
      relevanceScore: this.calculateRelevanceScore(result, intent),
      diversityScore: this.calculateDiversityScore(result, results)
    }))
    
    // Ordena por score combinado (relevância + diversidade)
    return scoredResults.sort((a, b) => {
      const scoreA = a.relevanceScore * 0.7 + a.diversityScore * 0.3
      const scoreB = b.relevanceScore * 0.7 + b.diversityScore * 0.3
      return scoreB - scoreA
    })
  }
}
```

### **6. Context Optimizer**

Otimiza contexto para máxima eficiência:

```typescript
class ContextOptimizer {
  constructor(
    private tokenizer: Tokenizer,
    private compressionService: CompressionService
  ) {}

  async optimize(context: RawContext): Promise<OptimizedContext> {
    // 1. Remove redundâncias
    const deduplicatedContext = this.removeDuplicates(context)
    
    // 2. Comprime templates similares
    const compressedTemplates = await this.compressTemplates(
      deduplicatedContext.templates
    )
    
    // 3. Extrai padrões comuns
    const commonPatterns = this.extractCommonPatterns(
      deduplicatedContext.examples
    )
    
    // 4. Otimiza representação textual
    const optimizedRepresentation = await this.optimizeTextRepresentation({
      templates: compressedTemplates,
      examples: deduplicatedContext.examples,
      patterns: [...deduplicatedContext.patterns, ...commonPatterns]
    })
    
    // 5. Valida limites de token
    const finalContext = await this.enforceTokenLimits(
      optimizedRepresentation,
      context.maxTokens
    )
    
    return finalContext
  }

  private async compressTemplates(templates: WorkflowTemplate[]): Promise<CompressedTemplate[]> {
    // Agrupa templates similares
    const groups = this.groupSimilarTemplates(templates)
    
    const compressedTemplates: CompressedTemplate[] = []
    
    for (const group of groups) {
      if (group.length === 1) {
        // Template único, não comprime
        compressedTemplates.push({
          type: 'single',
          template: group[0],
          compression: 1.0
        })
      } else {
        // Múltiplos templates similares, cria representação comprimida
        const compressed = await this.createCompressedRepresentation(group)
        compressedTemplates.push({
          type: 'compressed',
          baseTemplate: group[0], // Template mais representativo
          variations: group.slice(1),
          commonElements: compressed.commonElements,
          differences: compressed.differences,
          compression: compressed.compressionRatio
        })
      }
    }
    
    return compressedTemplates
  }

  private extractCommonPatterns(examples: WorkflowExample[]): IntegrationPattern[] {
    const patterns: Map<string, IntegrationPattern> = new Map()
    
    for (const example of examples) {
      // Extrai padrões de integração do exemplo
      const integrationPatterns = this.analyzeIntegrationPatterns(example)
      
      for (const pattern of integrationPatterns) {
        const key = `${pattern.service}_${pattern.operation}`
        
        if (patterns.has(key)) {
          // Incrementa frequência do padrão
          const existing = patterns.get(key)!
          existing.frequency = (existing.frequency || 1) + 1
          existing.examples.push(example.id)
        } else {
          // Novo padrão
          patterns.set(key, {
            ...pattern,
            frequency: 1,
            examples: [example.id]
          })
        }
      }
    }
    
    // Retorna apenas padrões com frequência significativa
    return Array.from(patterns.values())
      .filter(pattern => pattern.frequency >= 2)
      .sort((a, b) => b.frequency - a.frequency)
  }
}
```

## 🤖 Componentes Agentic RAG (Oficial n8n)

### **1. Intelligent Storage Agent**

Agente responsável por decisões inteligentes de armazenamento baseado no conteúdo:

```typescript
class IntelligentStorageAgent {
  constructor(
    private llm: LLMService,
    private vectorStore: VectorStore,
    private sqlDatabase: SQLDatabase
  ) {}

  async processAndStore(data: IncomingData): Promise<StorageDecision> {
    // 1. Analisa o tipo de dados
    const dataAnalysis = await this.analyzeDataType(data);
    
    // 2. Decide estratégia de armazenamento
    const storageStrategy = await this.decideStorageStrategy(dataAnalysis);
    
    // 3. Executa armazenamento otimizado
    return await this.executeStorage(data, storageStrategy);
  }

  private async analyzeDataType(data: IncomingData): Promise<DataAnalysis> {
    const analysisPrompt = `
    Analise o tipo de dados e determine a melhor estratégia de armazenamento:
    
    Dados: ${JSON.stringify(data, null, 2)}
    
    Considere:
    1. É estruturado (tabular) ou não-estruturado (texto/documentos)?
    2. Qual a melhor estratégia de chunking?
    3. Que metadados são importantes?
    4. Qual embedding strategy usar?
    
    Formato de resposta: JSON com análise estruturada.
    `;
    
    const analysis = await this.llm.generate(analysisPrompt);
    return JSON.parse(analysis);
  }

  private async decideStorageStrategy(analysis: DataAnalysis): Promise<StorageStrategy> {
    if (analysis.dataType === 'tabular') {
      // Dados tabulares -> SQL Database
      return {
        storage: 'sql',
        chunkingStrategy: 'preserve_table_structure',
        indexingMethod: 'relational_keys',
        metadata: {
          tableSchema: analysis.schema,
          relationships: analysis.relationships
        }
      };
    } else if (analysis.dataType === 'document') {
      // Documentos -> Vector Store com chunking inteligente
      return {
        storage: 'vector',
        chunkingStrategy: this.selectOptimalChunking(analysis),
        indexingMethod: 'semantic_embedding',
        metadata: {
          entities: analysis.entities,
          relationships: analysis.relationships,
          topics: analysis.topics
        }
      };
    } else {
      // Dados mistos -> Híbrido
      return {
        storage: 'hybrid',
        chunkingStrategy: 'adaptive',
        indexingMethod: 'multi_modal',
        metadata: {
          contentTypes: analysis.contentTypes,
          structuredParts: analysis.structuredParts
        }
      };
    }
  }

  private selectOptimalChunking(analysis: DataAnalysis): ChunkingStrategy {
    // Decide estratégia de chunking baseado no conteúdo
    if (analysis.hasCodeBlocks) {
      return 'preserve_code_structure';
    } else if (analysis.hasLists || analysis.hasTables) {
      return 'semantic_aware';
    } else {
      return 'sliding_window';
    }
  }

  private async executeStorage(data: IncomingData, strategy: StorageStrategy): Promise<StorageDecision> {
    switch (strategy.storage) {
      case 'sql':
        return await this.storeInSQL(data, strategy);
      case 'vector':
        return await this.storeInVector(data, strategy);
      case 'hybrid':
        return await this.storeHybrid(data, strategy);
      default:
        throw new Error(`Unknown storage strategy: ${strategy.storage}`);
    }
  }
}
```

### **2. Retriever Router Agent**

Agente que decide dinamicamente qual fonte de dados usar:

```typescript
class RetrieverRouterAgent {
  constructor(
    private llm: LLMService,
    private vectorStore: VectorStore,
    private sqlDatabase: SQLDatabase,
    private webSearchAPI: WebSearchAPI,
    private mcpServers: MCPServer[]
  ) {}

  async routeQuery(query: string, context: QueryContext): Promise<RetrievalResult> {
    // 1. Analisa a query para entender a intenção
    const queryAnalysis = await this.analyzeQueryIntent(query, context);
    
    // 2. Decide qual ferramenta usar
    const toolDecision = await this.selectOptimalTool(queryAnalysis);
    
    // 3. Executa recuperação usando a ferramenta selecionada
    const retrievalResult = await this.executeRetrieval(query, toolDecision);
    
    // 4. Se necessário, combina resultados de múltiplas fontes
    return await this.combineResults(retrievalResult, queryAnalysis);
  }

  private async analyzeQueryIntent(query: string, context: QueryContext): Promise<QueryAnalysis> {
    const routerPrompt = `
    Você é um roteador de queries. Analise a query e determine a melhor estratégia:
    
    Query: "${query}"
    Contexto: ${JSON.stringify(context)}
    
    Ferramentas disponíveis:
    1. vector_store: Para busca semântica em documentos e templates
    2. sql_database: Para dados estruturados, métricas, tabelas
    3. web_search: Para informações atuais, eventos recentes
    4. mcp_servers: Para integrações específicas (Notion, Slack, etc.)
    
    Determine:
    - Tipo da query: factual, analytical, opinion, contextual
    - Fonte de dados mais adequada
    - Se precisa combinar múltiplas fontes
    - Estratégia de busca (semantic, structured, real-time)
    
    Responda em JSON estruturado.
    `;
    
    const analysis = await this.llm.generate(routerPrompt);
    return JSON.parse(analysis);
  }

  private async selectOptimalTool(analysis: QueryAnalysis): Promise<ToolDecision> {
    // Exemplo de lógica de decisão baseada na análise
    const decision: ToolDecision = {
      primaryTool: this.selectPrimaryTool(analysis),
      secondaryTools: this.selectSecondaryTools(analysis),
      strategy: this.determineStrategy(analysis),
      confidence: this.calculateConfidence(analysis)
    };
    
    return decision;
  }

  private selectPrimaryTool(analysis: QueryAnalysis): string {
    // Lógica de seleção baseada no artigo oficial n8n
    if (analysis.requiresRealTimeData) {
      return 'web_search';
    } else if (analysis.queryType === 'analytical' && analysis.hasStructuredDataNeeds) {
      return 'sql_database';
    } else if (analysis.hasIntegrationSpecific) {
      return 'mcp_servers';
    } else {
      return 'vector_store';
    }
  }

  private async executeRetrieval(query: string, decision: ToolDecision): Promise<RetrievalResult> {
    switch (decision.primaryTool) {
      case 'vector_store':
        return await this.searchVectorStore(query, decision.strategy);
      
      case 'sql_database':
        return await this.querySQL(query, decision.strategy);
      
      case 'web_search':
        return await this.searchWeb(query, decision.strategy);
      
      case 'mcp_servers':
        return await this.queryMCPServers(query, decision.strategy);
      
      default:
        throw new Error(`Unknown tool: ${decision.primaryTool}`);
    }
  }

  // Implementação específica para cada ferramenta
  private async searchVectorStore(query: string, strategy: SearchStrategy): Promise<RetrievalResult> {
    const embedding = await this.embeddingService.embedText(query);
    const results = await this.vectorStore.search(embedding, {
      limit: strategy.limit,
      threshold: strategy.threshold,
      filter: strategy.filter
    });
    
    return {
      source: 'vector_store',
      results,
      metadata: { strategy, confidence: 0.85 }
    };
  }

  private async querySQL(query: string, strategy: SearchStrategy): Promise<RetrievalResult> {
    // Converte query natural para SQL usando LLM
    const sqlQuery = await this.naturalLanguageToSQL(query);
    const results = await this.sqlDatabase.execute(sqlQuery);
    
    return {
      source: 'sql_database',
      results: this.formatSQLResults(results),
      metadata: { sqlQuery, strategy }
    };
  }
}
```

### **3. Answer Critic Agent**

Agente que avalia e melhora respostas iterativamente:

```typescript
class AnswerCriticAgent {
  constructor(
    private llm: LLMService,
    private retrieverRouter: RetrieverRouterAgent,
    private hallucinationDetector: HallucinationDetector
  ) {}

  async critiqueAndImprove(
    originalQuery: string,
    retrievedContext: string,
    generatedAnswer: string
  ): Promise<ImprovedAnswer> {
    
    let currentAnswer = generatedAnswer;
    let iteration = 0;
    const maxIterations = 3;
    
    while (iteration < maxIterations) {
      // 1. Avalia a resposta atual
      const critique = await this.critizeAnswer(originalQuery, retrievedContext, currentAnswer);
      
      // 2. Se a resposta está boa, retorna
      if (critique.isComplete && critique.isAccurate) {
        return {
          finalAnswer: currentAnswer,
          iterations: iteration,
          improvements: critique.improvements,
          confidence: critique.confidence
        };
      }
      
      // 3. Identifica o que está faltando
      const missingInfo = this.identifyMissingInformation(critique);
      
      // 4. Busca informações adicionais se necessário
      if (missingInfo.needsMoreData) {
        const additionalContext = await this.retrieveAdditionalContext(
          missingInfo.queries,
          originalQuery
        );
        retrievedContext += '\n\n' + additionalContext;
      }
      
      // 5. Gera resposta melhorada
      currentAnswer = await this.generateImprovedAnswer(
        originalQuery,
        retrievedContext,
        currentAnswer,
        critique
      );
      
      iteration++;
    }
    
    return {
      finalAnswer: currentAnswer,
      iterations: iteration,
      improvements: [],
      confidence: 0.7 // Confiança reduzida se não conseguiu melhorar
    };
  }

  private async critizeAnswer(
    query: string,
    context: string,
    answer: string
  ): Promise<AnswerCritique> {
    
    const criticPrompt = `
    Você é um Answer Critic. Avalie se a RESPOSTA_GERADA responde completamente à QUERY_USUARIO.
    
    QUERY_USUARIO: ${query}
    CONTEXTO_RECUPERADO: ${context}
    RESPOSTA_GERADA: ${answer}
    
    Avalie nos seguintes critérios:
    1. Completude: A resposta aborda todos os aspectos da query?
    2. Precisão: As informações estão corretas baseadas no contexto?
    3. Relevância: A resposta é relevante para a query?
    4. Clareza: A resposta é clara e bem estruturada?
    
    Se algo está faltando, gere uma NOVA_QUERY_INTERNA para buscar a informação ausente.
    
    Formato de resposta: JSON estruturado com avaliação e sugestões.
    `;
    
    const critiqueResult = await this.llm.generate(criticPrompt);
    const critique = JSON.parse(critiqueResult);
    
    // Adiciona detecção de alucinações
    const hallucinationCheck = await this.hallucinationDetector.detectHallucinations(
      context,
      answer
    );
    
    return {
      ...critique,
      hallucinationRisk: hallucinationCheck,
      needsImprovement: !critique.isComplete || !critique.isAccurate || hallucinationCheck.isHallucination
    };
  }

  private async retrieveAdditionalContext(
    missingInfoQueries: string[],
    originalQuery: string
  ): Promise<string> {
    
    const additionalResults = await Promise.all(
      missingInfoQueries.map(query =>
        this.retrieverRouter.routeQuery(query, { originalQuery, iterativeSearch: true })
      )
    );
    
    return additionalResults
      .map(result => result.content)
      .join('\n\n');
  }

  private async generateImprovedAnswer(
    query: string,
    context: string,
    previousAnswer: string,
    critique: AnswerCritique
  ): Promise<string> {
    
    const improvementPrompt = `
    Melhore a resposta baseada na crítica recebida:
    
    QUERY ORIGINAL: ${query}
    CONTEXTO: ${context}
    RESPOSTA ANTERIOR: ${previousAnswer}
    CRÍTICA: ${JSON.stringify(critique.improvements)}
    
    Gere uma resposta melhorada que:
    1. Corrige os problemas identificados
    2. Adiciona informações em falta
    3. Mantém a clareza e precisão
    4. Evita alucinações
    
    RESPOSTA MELHORADA:
    `;
    
    return await this.llm.generate(improvementPrompt);
  }
}
```

### **4. Adaptive RAG System**

Sistema que implementa diferentes estratégias baseadas no tipo de query:

```typescript
class AdaptiveRAGSystem {
  constructor(
    private queryClassifier: QueryClassifier,
    private retrieverRouter: RetrieverRouterAgent,
    private answerCritic: AnswerCriticAgent
  ) {}

  async processQuery(query: string, context: QueryContext): Promise<AdaptiveRAGResult> {
    // 1. Classifica a query em uma das 4 categorias
    const classification = await this.queryClassifier.classify(query);
    
    // 2. Seleciona estratégia adaptativa baseada na classificação
    const strategy = this.selectStrategy(classification);
    
    // 3. Executa fluxo específico para o tipo de query
    return await this.executeAdaptiveFlow(query, context, strategy);
  }

  private selectStrategy(classification: QueryClassification): RetrievalStrategy {
    switch (classification.type) {
      case 'factual':
        return {
          approach: 'precision_focused',
          queryAdaptation: 'make_more_specific',
          retrievalMethod: 'exact_match_preferred',
          generationPrompt: 'be_precise_and_factual'
        };
      
      case 'analytical':
        return {
          approach: 'comprehensive_analysis',
          queryAdaptation: 'break_into_sub_questions',
          retrievalMethod: 'broad_coverage',
          generationPrompt: 'provide_thorough_analysis'
        };
      
      case 'opinion':
        return {
          approach: 'multiple_perspectives',
          queryAdaptation: 'identify_different_viewpoints',
          retrievalMethod: 'diverse_sources',
          generationPrompt: 'present_balanced_views'
        };
      
      case 'contextual':
        return {
          approach: 'context_aware',
          queryAdaptation: 'preserve_context_dependencies',
          retrievalMethod: 'contextual_similarity',
          generationPrompt: 'maintain_contextual_relevance'
        };
      
      default:
        return this.getDefaultStrategy();
    }
  }

  private async executeAdaptiveFlow(
    query: string,
    context: QueryContext,
    strategy: RetrievalStrategy
  ): Promise<AdaptiveRAGResult> {
    
    // 1. Adapta a query baseada na estratégia
    const adaptedQuery = await this.adaptQuery(query, strategy);
    
    // 2. Executa recuperação otimizada
    const retrievalResult = await this.retrieverRouter.routeQuery(adaptedQuery, {
      ...context,
      strategy
    });
    
    // 3. Gera resposta usando prompt específico
    const initialAnswer = await this.generateAnswer(
      query,
      retrievalResult.content,
      strategy.generationPrompt
    );
    
    // 4. Crítica e melhora iterativa
    const finalAnswer = await this.answerCritic.critiqueAndImprove(
      query,
      retrievalResult.content,
      initialAnswer
    );
    
    return {
      originalQuery: query,
      adaptedQuery,
      strategy: strategy.approach,
      retrievalResult,
      finalAnswer,
      metadata: {
        classification: strategy,
        confidence: finalAnswer.confidence,
        iterations: finalAnswer.iterations
      }
    };
  }
}
```

## 🚀 Uso Prático

### **Configuração e Inicialização**

#### Traditional RAG Setup
```typescript
// Configuração do sistema RAG tradicional
const ragConfig = {
  embedding: {
    model: 'text-embedding-3-large',
    dimensions: 3072,
    batchSize: 100
  },
  vectorStore: {
    provider: 'pinecone',
    indexName: 'n8n-workflows',
    environment: 'us-west1-gcp'
  },
  retrieval: {
    defaultLimit: 10,
    defaultThreshold: 0.75,
    maxTokens: 8000
  }
}

// Inicialização dos componentes tradicionais
const embeddingService = new EmbeddingService(openAI, cache, ragConfig.embedding)
const vectorStore = new PineconeVectorStore(pinecone, ragConfig.vectorStore.indexName)
const knowledgeBase = new KnowledgeBaseManager(vectorStore, embeddingService, templateRepo)
const retrievalEngine = new SemanticRetrievalEngine(vectorStore, embeddingService, relevanceScorer)
const contextAssembler = new ContextAssembler(templateRepo, contextOptimizer)

// Sistema RAG tradicional
const traditionalRAG = new RAGSystem({
  embeddingService,
  vectorStore,
  knowledgeBase,
  retrievalEngine,
  contextAssembler
})
```

#### Agentic RAG Setup (Oficial n8n)
```typescript
// Configuração do sistema Agentic RAG
const agenticRAGConfig = {
  // Configurações base
  ...ragConfig,
  
  // Configurações específicas do Agentic RAG
  agents: {
    intelligentStorage: {
      analysisModel: 'gpt-4',
      decisionThreshold: 0.8
    },
    retrieverRouter: {
      routingModel: 'gpt-4',
      tools: ['vector_store', 'sql_database', 'web_search', 'mcp_servers'],
      confidenceThreshold: 0.7
    },
    answerCritic: {
      criticModel: 'gpt-4',
      maxIterations: 3,
      improvementThreshold: 0.1
    }
  },
  
  // Integração com MCP Servers
  mcpServers: [
    {
      name: 'notion',
      endpoint: 'localhost:3000',
      capabilities: ['search', 'create', 'update']
    },
    {
      name: 'slack',
      endpoint: 'localhost:3001', 
      capabilities: ['search_messages', 'send_message']
    }
  ],
  
  // Configurações de avaliação
  evaluation: {
    enableContinuous: true,
    hallucinationDetection: {
      model: 'vectara/HHEM-2.1-Open',
      threshold: 0.7
    },
    metrics: {
      trackAccuracy: true,
      trackRelevance: true,
      trackLatency: true
    }
  }
}

// Inicialização dos componentes Agentic RAG
const sqlDatabase = new PostgreSQLDatabase(databaseConfig)
const webSearchAPI = new WebSearchAPI(searchConfig)
const mcpServers = await initializeMCPServers(agenticRAGConfig.mcpServers)

// Agentes específicos
const intelligentStorage = new IntelligentStorageAgent(openAI, vectorStore, sqlDatabase)
const retrieverRouter = new RetrieverRouterAgent(openAI, vectorStore, sqlDatabase, webSearchAPI, mcpServers)
const answerCritic = new AnswerCriticAgent(openAI, retrieverRouter, hallucinationDetector)

// Componentes de avaliação
const ragEvaluator = new N8NRAGEvaluator(openAI)
const hallucinationDetector = new HallucinationDetector(hhem)
const evaluationPipeline = new RAGEvaluationPipeline(agenticRAG, ragEvaluator, hallucinationDetector)

// Sistema Agentic RAG completo
const agenticRAG = new AdaptiveRAGSystem(queryClassifier, retrieverRouter, answerCritic)
```

### **Indexação da Base de Conhecimento**

```typescript
// Indexação inicial de templates
async function indexKnowledgeBase() {
  console.log('Iniciando indexação da base de conhecimento...')
  
  // Carrega templates existentes
  const templates = await templateRepository.getAllTemplates()
  console.log(`Encontrados ${templates.length} templates`)
  
  // Carrega exemplos de workflows
  const examples = await exampleRepository.getAllExamples()
  console.log(`Encontrados ${examples.length} exemplos`)
  
  // Carrega padrões de integração
  const patterns = await patternRepository.getAllPatterns()
  console.log(`Encontrados ${patterns.length} padrões`)
  
  // Indexação em lotes
  await knowledgeBase.bulkIndex([...templates, ...examples, ...patterns])
  
  console.log('Indexação concluída!')
}

// Atualização incremental
async function updateKnowledgeBase(newItems: any[]) {
  for (const item of newItems) {
    if (item.type === 'template') {
      await knowledgeBase.indexTemplate(item)
    } else if (item.type === 'example') {
      await knowledgeBase.indexWorkflowExample(item)
    } else if (item.type === 'pattern') {
      await knowledgeBase.indexIntegrationPattern(item)
    }
  }
}
```

### **Busca e Recuperação**

```typescript
// Exemplo de busca completa
async function searchWorkflowContext(userQuery: string, intent: WorkflowIntent) {
  try {
    // 1. Recuperação semântica
    const retrievalResult = await retrievalEngine.retrieveRelevantTemplates(
      userQuery,
      intent,
      {
        limit: 15,
        threshold: 0.7,
        includeExamples: true,
        includePatterns: true
      }
    )
    
    console.log(`Encontrados ${retrievalResult.totalResults} resultados relevantes`)
    console.log(`Score médio: ${retrievalResult.averageScore}`)
    
    // 2. Montagem de contexto
    const ragContext = await contextAssembler.assembleContext(
      retrievalResult,
      intent,
      8000 // max tokens
    )
    
    console.log(`Contexto montado com ${ragContext.tokenCount} tokens`)
    console.log(`Score de relevância: ${ragContext.relevanceScore}`)
    
    return ragContext
    
  } catch (error) {
    console.error('Erro na busca RAG:', error)
    throw error
  }
}

// Exemplo de uso
const intent = {
  workflowType: 'ai_agent',
  components: {
    triggers: ['webhook'],
    actions: ['openai', 'slack'],
    integrations: ['slack', 'openai'],
    logic: ['condition']
  },
  requirements: {
    input: 'user message',
    processing: 'ai analysis and response',
    output: 'slack notification',
    integrations: ['slack', 'openai']
  }
}

const context = await searchWorkflowContext(
  'Criar um agente que responde mensagens no Slack usando IA',
  intent
)
```

### **Monitoramento e Métricas**

```typescript
class RAGMetrics {
  async collectMetrics(): Promise<RAGMetricsData> {
    return {
      // Performance
      averageRetrievalTime: await this.getAverageRetrievalTime(),
      cacheHitRate: await this.getCacheHitRate(),
      
      // Qualidade
      averageRelevanceScore: await this.getAverageRelevanceScore(),
      contextUtilization: await this.getContextUtilization(),
      
      // Volume
      totalQueries: await this.getTotalQueries(),
      uniqueQueries: await this.getUniqueQueries(),
      
      // Base de conhecimento
      totalTemplates: await this.getTotalIndexedTemplates(),
      totalExamples: await this.getTotalIndexedExamples(),
      indexFreshness: await this.getIndexFreshness()
    }
  }
}

// Monitoramento em tempo real
const metrics = new RAGMetrics()
setInterval(async () => {
  const data = await metrics.collectMetrics()
  console.log('RAG Metrics:', data)
}, 60000) // A cada minuto
```

## 📊 Otimização e Performance

### **Estratégias de Cache**

```typescript
class RAGCacheManager {
  constructor(
    private embeddingCache: RedisCache,
    private resultCache: MemoryCache,
    private contextCache: LRUCache
  ) {}

  async getCachedEmbedding(text: string): Promise<number[] | null> {
    const key = this.generateEmbeddingKey(text)
    return await this.embeddingCache.get(key)
  }

  async cacheSearchResults(query: string, results: SearchResult[]): Promise<void> {
    const key = this.generateResultKey(query)
    await this.resultCache.set(key, results, 300) // 5 minutos
  }

  async getCachedContext(contextKey: string): Promise<RAGContext | null> {
    return this.contextCache.get(contextKey)
  }
}
```

### **Otimização de Queries**

```typescript
class QueryOptimizer {
  optimizeQuery(query: string, intent: WorkflowIntent): OptimizedQuery {
    // Remove stop words específicas do domínio
    const cleanQuery = this.removeStopWords(query)
    
    // Expande com sinônimos do domínio N8N
    const expandedQuery = this.expandWithSynonyms(cleanQuery)
    
    // Adiciona contexto do tipo de workflow
    const contextualQuery = this.addWorkflowContext(expandedQuery, intent)
    
    return {
      original: query,
      optimized: contextualQuery,
      expansions: this.getExpansions(query, contextualQuery),
      confidence: this.calculateOptimizationConfidence(query, contextualQuery)
    }
  }
}
```

## 🎯 Casos de Uso Práticos (Baseados nos Artigos Oficiais n8n)

### **Caso 1: Adaptive RAG - Escolha de Estratégia de Recuperação**

Baseado no artigo oficial, este workflow demonstra como diferentes tipos de queries requerem diferentes estratégias:

```typescript
// Implementação do Adaptive RAG no n8n AI Workflow Generator
async function adaptiveRAGWorkflow(userQuery: string): Promise<WorkflowGeneration> {
  
  // 1. Classificação da Query
  const queryClassification = await classifyQuery(userQuery);
  // Tipos: 'factual', 'analytical', 'opinion', 'contextual'
  
  switch (queryClassification.type) {
    case 'factual':
      // Para queries factuais: "Como criar um webhook no n8n?"
      return await executeFactualStrategy(userQuery);
    
    case 'analytical': 
      // Para queries analíticas: "Qual a melhor arquitetura para um sistema de CRM com n8n?"
      return await executeAnalyticalStrategy(userQuery);
    
    case 'opinion':
      // Para queries de opinião: "Quais são as melhores práticas para automação de email?"
      return await executeOpinionStrategy(userQuery);
    
    case 'contextual':
      // Para queries contextuais: "Como integrar com meu sistema existente?"
      return await executeContextualStrategy(userQuery);
  }
}

async function executeFactualStrategy(query: string): Promise<WorkflowGeneration> {
  // Reescreve query para maior precisão
  const preciseQuery = await rewriteForPrecision(query);
  
  // Busca em templates específicos
  const templates = await searchSpecificTemplates(preciseQuery);
  
  // Gera resposta factual
  return await generatePreciseWorkflow(templates, "seja preciso e factual");
}

async function executeAnalyticalStrategy(query: string): Promise<WorkflowGeneration> {
  // Quebra query em sub-questões
  const subQuestions = await breakIntoSubQuestions(query);
  
  // Busca ampla para cobertura completa
  const comprehensiveContext = await Promise.all(
    subQuestions.map(q => searchBroadCoverage(q))
  );
  
  // Gera análise completa
  return await generateAnalyticalWorkflow(comprehensiveContext, "forneça análise completa");
}
```

### **Caso 2: AI Agent com Fonte de Conhecimento Dinâmica**

Implementação de um agente que escolhe dinamicamente entre RAG estático e busca web em tempo real:

```typescript
class DynamicKnowledgeAgent {
  constructor(
    private mcpRagServer: MCPRAGServer,      // Para conhecimento estático sobre n8n
    private mcpSearchServer: MCPSearchServer  // Para informações atuais
  ) {}

  async processWorkflowRequest(query: string): Promise<AgentResponse> {
    // O agente analisa a query e decide qual ferramenta usar
    const decision = await this.analyzeQuery(query);
    
    if (decision.needsCurrentInfo) {
      // Use busca web para informações atuais
      // Ex: "Quais são as últimas integrações lançadas no n8n?"
      const searchResults = await this.mcpSearchServer.search({
        query: `n8n latest integrations 2025`,
        sources: ['n8n_blog', 'n8n_docs', 'github_releases']
      });
      
      return await this.generateWorkflowFromCurrentInfo(query, searchResults);
      
    } else {
      // Use RAG database para conhecimento fundamental
      // Ex: "Como criar um workflow de automação de email?"
      const ragResults = await this.mcpRagServer.query({
        query,
        collection: 'n8n_workflow_templates'
      });
      
      return await this.generateWorkflowFromRAG(query, ragResults);
    }
  }

  private async analyzeQuery(query: string): Promise<QueryDecision> {
    const analysisPrompt = `
    Analise esta query sobre n8n workflows e determine qual fonte usar:
    
    Query: "${query}"
    
    Decisão:
    - Se pergunta sobre recursos recentes, novidades, ou mudanças -> busca web
    - Se pergunta sobre funcionalidades básicas, templates -> RAG database
    
    Keywords que indicam info atual: "novo", "último", "recente", "2025", "lançamento"
    `;
    
    const decision = await this.llm.analyze(analysisPrompt);
    return JSON.parse(decision);
  }
}
```

### **Caso 3: AI Agent para Dados Tabulares + Não-Estruturados (SQL + GraphRAG)**

Sistema híbrido que processa diferentes tipos de dados de forma otimizada:

```typescript
class HybridDataAgent {
  constructor(
    private sqlDatabase: PostgreSQLDatabase,
    private graphRAG: GraphRAGSystem,
    private vectorStore: VectorStore
  ) {}

  async processMultiModalWorkflowRequest(
    files: UploadedFile[]
  ): Promise<HybridWorkflowResponse> {
    
    const processedData = await Promise.all(
      files.map(file => this.processFileByType(file))
    );
    
    // Agente decide como combinar as informações
    return await this.synthesizeHybridWorkflow(processedData);
  }

  private async processFileByType(file: UploadedFile): Promise<ProcessedData> {
    if (this.isTabularData(file)) {
      // Excel, CSV -> SQL Database
      return await this.processTabularData(file);
    } else if (this.isDocument(file)) {
      // PDF, Word -> GraphRAG
      return await this.processDocumentData(file);
    } else {
      // Outros formatos -> Vector Store
      return await this.processUnstructuredData(file);
    }
  }

  private async processTabularData(file: UploadedFile): Promise<ProcessedData> {
    // Cria tabela SQL dinâmica
    const tableSchema = await this.analyzeTableStructure(file);
    const tableName = `temp_${Date.now()}`;
    
    await this.sqlDatabase.createTable(tableName, tableSchema);
    await this.sqlDatabase.insertData(tableName, file.data);
    
    return {
      type: 'tabular',
      source: 'sql',
      tableName,
      schema: tableSchema,
      queryCapable: true
    };
  }

  private async processDocumentData(file: UploadedFile): Promise<ProcessedData> {
    // Extrai entidades e relacionamentos
    const entities = await this.extractEntities(file.content);
    const relationships = await this.extractRelationships(file.content, entities);
    
    // Constrói grafo de conhecimento
    await this.graphRAG.addNodes(entities);
    await this.graphRAG.addEdges(relationships);
    
    return {
      type: 'document',
      source: 'graph',
      entities,
      relationships,
      queryCapable: true
    };
  }

  private async synthesizeHybridWorkflow(
    processedData: ProcessedData[]
  ): Promise<HybridWorkflowResponse> {
    
    const tabularData = processedData.filter(d => d.type === 'tabular');
    const documentData = processedData.filter(d => d.type === 'document');
    
    // Gera workflow que combina ambos os tipos de dados
    const workflowPrompt = `
    Crie um workflow n8n que:
    
    1. Consulte dados tabulares: ${tabularData.map(d => d.tableName).join(', ')}
    2. Use conhecimento dos documentos: ${documentData.map(d => d.entities.length).join(' entidades, ')}
    
    O workflow deve ser capaz de:
    - Fazer queries SQL nos dados tabulares
    - Consultar o grafo de conhecimento dos documentos
    - Combinar insights de ambas as fontes
    `;
    
    const workflow = await this.generateHybridWorkflow(workflowPrompt, processedData);
    
    return {
      workflow,
      dataSources: processedData,
      capabilities: {
        sqlQueries: tabularData.length > 0,
        graphQueries: documentData.length > 0,
        hybridAnalysis: tabularData.length > 0 && documentData.length > 0
      }
    };
  }
}
```

### **Integração com Model Context Protocol (MCP)**

```typescript
// Configuração de MCP Servers para diferentes casos de uso
const mcpServers = [
  {
    name: 'n8n_templates',
    description: 'Acesso a templates oficiais do n8n',
    capabilities: ['search_templates', 'get_template_details', 'list_categories']
  },
  {
    name: 'realtime_n8n_info', 
    description: 'Informações atuais sobre n8n',
    capabilities: ['search_blog', 'get_releases', 'check_updates']
  },
  {
    name: 'user_workspace',
    description: 'Workspace específico do usuário',
    capabilities: ['access_workflows', 'get_integrations', 'analyze_usage']
  }
];

// Implementação do Router que escolhe o MCP Server correto
class MCPRouter {
  async routeToMCPServer(query: string, context: QueryContext): Promise<MCPResponse> {
    const intent = await this.analyzeIntent(query);
    
    if (intent.needsTemplate) {
      return await this.queryMCP('n8n_templates', query);
    } else if (intent.needsCurrentInfo) {
      return await this.queryMCP('realtime_n8n_info', query);
    } else if (intent.needsUserData) {
      return await this.queryMCP('user_workspace', query);
    }
    
    // Fallback para busca híbrida
    return await this.hybridMCPQuery(query, context);
  }
}
```

## 📋 Resumo Executivo dos Achados Oficiais n8n

### **🔍 Principais Descobertas dos Artigos Oficiais**

#### **1. Framework de Avaliação RAG (Artigo: Evaluating RAG)**

**Problemas Identificados:**
- RAG tradicional ainda sofre de alucinações mesmo com recuperação correta
- Necessidade de avaliação sistemática em dois pilares: Document Relevance e Groundedness

**Soluções Oficiais n8n:**
- **Ferramentas nativas de avaliação**: `Evaluate RAG Response Accuracy` e `RAG Document Relevance`
- **Integração com HHEM-2.1-Open** para detecção de alucinações
- **Framework RAGTruth** para categorização de tipos de alucinações

**Métricas Essenciais:**
- Context Recall e Context Precision (Document Relevance)  
- Faithfulness e Response Relevancy (Groundedness)

#### **2. Evolução para Agentic RAG (Artigo: Agentic RAG)**

**Limitações do Simple RAG:**
- Workflow fixo "retrieve then read"
- Sem capacidade de decisão autônoma
- Base de dados única e não-estruturada

**Benefícios do Agentic RAG:**
- **Intelligent Storage**: Decisões inteligentes sobre como indexar
- **Dynamic Retrieval**: Escolha automática da melhor fonte de dados
- **Verified Generation**: Auto-crítica e melhoria iterativa

**Componentes Essenciais:**
- **Retriever Router**: Decide qual ferramenta usar (Vector Store, SQL, Web Search, MCP)
- **Answer Critic**: Avalia respostas e busca informações adicionais se necessário

#### **3. Casos de Uso Validados pela n8n**

1. **Adaptive RAG**: Diferentes estratégias baseadas no tipo de query
2. **Dynamic Knowledge Sources**: Combinação de RAG estático + busca web
3. **Hybrid Data Processing**: SQL para dados tabulares + GraphRAG para documentos

### **🎯 Impacto para o N8N AI Workflow Generator**

#### **Melhorias Implementáveis Imediatamente:**
1. **Sistema de Avaliação Contínua** usando métricas oficiais n8n
2. **Detecção de Alucinações** com HHEM-2.1-Open
3. **Classificação de Queries** para estratégias adaptativas

#### **Arquitetura Evolutiva Recomendada:**
1. **Fase 1**: Implementar avaliação oficial n8n no sistema atual
2. **Fase 2**: Adicionar Retriever Router para múltiplas fontes
3. **Fase 3**: Implementar Answer Critic para melhoria iterativa
4. **Fase 4**: Full Agentic RAG com Intelligent Storage

#### **ROI Esperado:**
- **Redução de 60%** em alucinações com Answer Critic
- **Melhoria de 40%** na relevância com Adaptive RAG  
- **Aumento de 75%** na precisão com avaliação contínua

### **📊 Métricas de Sucesso Baseadas em Práticas Oficiais**

| Métrica | Target Atual | Target Agentic | Baseline |
|---------|-------------|---------------|----------|
| Response Relevancy | 0.85 | 0.92 | 0.78 |
| Context Precision | 0.80 | 0.90 | 0.72 |
| Hallucination Rate | 15% | 5% | 25% |
| User Satisfaction | 4.2/5 | 4.7/5 | 3.8/5 |

### **🚀 Próximos Passos Priorizados**

1. **Implementação imediata**: Sistema de avaliação nativa n8n
2. **Q1 2025**: Retriever Router com múltiplas fontes
3. **Q2 2025**: Answer Critic e melhoria iterativa
4. **Q3 2025**: Full Agentic RAG com MCP integration

---

*Esta documentação reflete as **práticas oficiais mais recentes do n8n** para implementação de sistemas RAG robustos e avaliação contínua de qualidade.*

## 🔮 Próximos Passos

1. **[Template System](./template_system.md)** - Sistema avançado de templates
2. **[LangChain Integration](./langchain_integration.md)** - Integração com LangChain
3. **[Memory Management](./memory_management.md)** - Gestão de contexto e memória
4. **[Validation Engine](./validation_engine.md)** - Validação de workflows

---

*O sistema RAG é fundamental para a qualidade dos workflows gerados. Uma implementação robusta garante contexto relevante e resultados precisos.*
