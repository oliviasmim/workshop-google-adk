from google.adk.agents import Agent

MODEL = "gemini-2.0-flash"           


# ─── LLM agents ─────────────────────
code_quality_agent = Agent(
    name="code_quality_agent",
    model=MODEL,
    instruction=(
        "Você é um Especialista em Qualidade de Código.\n"
        "Analise o conteúdo em conteúdo enviado pelo usario  procurando duplicações, alta complexidade, "
        "problemas de abstração e oportunidades de otimização. "
        "Retorne um relatório detalhado e priorizado."
    ),
    description="Analisa a qualidade geral do código.",
    output_key="quality_report",
)

security_agent = Agent(
    name="security_agent",
    model=MODEL,
    instruction=(
        "Você é um Especialista em Segurança.\n"
        "Examine conteúdo enviado pelo usario  em busca de XSS, injeções, vazamento de dados, "
        "falhas de autenticação/autorização e outras vulnerabilidades. "
        "Classifique por severidade e proponha correções."
    ),
    description="Revisa vulnerabilidades de segurança.",
    output_key="security_report",
)

style_agent = Agent(
    name="style_agent",
    model=MODEL,
    instruction=(
        "Você é um Especialista em Padrões de Código.\n"
        "Avalie conteúdo enviado pelo usario  quanto a nomenclatura, formatação, organização de imports "
        "e boas práticas React/TypeScript. Liste desvios e mostre como corrigi-los."
    ),
    description="Avalia aderência a padrões de estilo.",
    output_key="style_report",
)

# ─── Compose them into an ADK “agent team” (Sequential) ─────
root_agent = Agent(
    name="code_review_team",
    model=MODEL,
    description="Executa análise de qualidade, segurança e estilo em sequência.",
    instruction="""
Você é o Líder da Equipe de Revisão de Código.

Fluxo de trabalho
1. Encaminhe o conteúdo enviado pelo usario aos especialistas na ordem:
   a) code_quality_agent  
   b) security_agent  
   c) style_agent  
2. Aguarde os relatórios (`quality_report`, `security_report`, `style_report`).
3. Consolide tudo em **um único parecer final** no formato Markdown:

Regras
- Agrupe observações idênticas; evite duplicação.
- Cite sempre o arquivo e linha, se possível.
- Use tom profissional e direto, em Português.
- Não inclua código-fonte completo no relatório, apenas trechos relevantes.
""",
    sub_agents=[code_quality_agent, security_agent, style_agent],
)