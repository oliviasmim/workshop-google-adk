from google.adk.agents import Agent, SequentialAgent

MODEL = "gemini-2.0-flash"

# ─── 1. Specialized review agents ────────────────────────────
code_quality_agent = Agent(
    name="CodeQualityAgent",
    model=MODEL,
    description="Avalia duplicação, complexidade e oportunidades de otimização.",
    instruction="""
Você é um Especialista em Qualidade de Código.
Analise o conteúdo fornecido pelo usuário procurando:
• duplicações
• alta complexidade ciclomática
• problemas de abstração
• oportunidades de otimização

**Saída:**
Forneça um relatório priorizado em Markdown.
""",
    output_key="quality_report",
)

security_agent = Agent(
    name="SecurityAgent",
    model=MODEL,
    description="Investiga vulnerabilidades de segurança.",
    instruction="""
Você é um Especialista em Segurança.
Examine o conteúdo fornecido pelo usuário procurando:
• XSS
• injeções (SQL/NoSQL/Command)
• vazamento de dados
• falhas de autenticação/autorização
• outras vulnerabilidades OWASP Top 10

**Saída:**
Liste problemas por severidade e proponha correções (Markdown).
""",
    output_key="security_report",
)

style_agent = Agent(
    name="StyleAgent",
    model=MODEL,
    description="Verifica aderência a padrões de estilo.",
    instruction="""
Você é um Especialista em Padrões de Código.
Avalie o conteúdo fornecido pelo usuário considerando:
• nomenclatura
• formatação / PEP 8
• organização de imports
• boas práticas de framework / linguagem

**Saída:**
Enumere desvios e mostre como corrigi‑los (Markdown).
""",
    output_key="style_report",
)

# ─── 2. Consolidador final ───────────────────────────────────
final_reviewer = Agent(
    name="FinalReviewerAgent",
    model=MODEL,
    description="Consolida todos os relatórios em um parecer final.",
    instruction="""
Você é o Líder da Equipe de Revisão de Código.

Recebeu os relatórios:
• Qualidade ↓
{quality_report}

• Segurança ↓
{security_report}

• Estilo ↓
{style_report}

Sua tarefa:
1. Analise, remova duplicações e agrupe pontos similares.
2. Produza **um único parecer final** em Markdown seguindo a estrutura:

### 1 . Resumo Executivo
Máx. 4 linhas destacando riscos e pontos fortes.

### 2 . Tabela de Problemas
| Categoria | Severidade | Arquivo/Linha | Descrição | Agente |
|-----------|------------|---------------|-----------|--------|
| …         | …          | …             | …         | …      |

### 3 . Recomendações de Curto Prazo (≤ 1 dia)
- …

### 4 . Recomendações de Médio Prazo (≤ 1 sprint)
- …

### 5 . Decisão Final
**Go / No‑Go** para merge, com justificativa.

Regras
- Cite sempre arquivo e linha, se possível.
- Use tom profissional, direto, em Português.
- Não inclua o código completo; apenas trechos relevantes.
""",
)

# ─── 3. Pipeline sequencial ─────────────────────────────────
root_agent = SequentialAgent(
    name="CodeReviewPipeline",
    description="Pipeline de revisão: qualidade → segurança → estilo → consolidação.",
    sub_agents=[
        code_quality_agent,
        security_agent,
        style_agent,
        final_reviewer,
    ],
)