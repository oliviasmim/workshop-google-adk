from google.adk.agents import LlmAgent, SequentialAgent

GEMINI_MODEL = "gemini-2.0-flash"

# ─── 1. React Code Writer ────────────────────────────────────
react_writer_agent = LlmAgent(
    name="ReactCodeWriterAgent",
    model=GEMINI_MODEL,
    instruction="""You are a React (TypeScript) Code Generator.
Based *only* on the user's request, write React code (using TypeScript and functional components) that fulfills the requirement.
Output *only* the complete code block, enclosed in triple backticks (```tsx ... ```).
Do not add any other text before or after the code block.
""",
    description="Creates initial React/TSX code from a specification.",
    output_key="generated_code",
)

# ─── 2. React Code Reviewer ──────────────────────────────────
react_reviewer_agent = LlmAgent(
    name="ReactCodeReviewerAgent",
    model=GEMINI_MODEL,
    instruction="""You are an expert React (TypeScript) Code Reviewer.
Review the code below and provide constructive feedback.

**Code to Review:**
```tsx
{generated_code}
```

**Review Criteria**
1. **Correctness:** Component renders / functions as intended?  
2. **Accessibility:** ARIA usage, semantics, keyboard support.  
3. **Code Quality:** Readability, hooks usage, state management, typing, lint rules.  
4. **Performance:** Avoids unnecessary re‑renders, memoization where needed.  
5. **Best Practices:** Folder structure, separation of concerns, testability.

**Output**
Return a concise, bulleted list of issues & suggestions.  
If the code is excellent and needs no changes, output: `No major issues found.`  
Return *only* the review comments or that single sentence.
""",
    description="Reviews React code and lists improvements.",
    output_key="review_comments",
)

# ─── 3. React Code Refactorer ────────────────────────────────
react_refactorer_agent = LlmAgent(
    name="ReactCodeRefactorerAgent",
    model=GEMINI_MODEL,
    instruction="""You are a React (TypeScript) Code Refactoring AI.
Refactor the code based on the review comments provided.

**Original Code**
```tsx
{generated_code}
```

**Review Comments**
{review_comments}

**Task**
Apply the suggestions.  
If comments state `No major issues found.`, return the original code unchanged.  
Ensure final code is complete, typed, and includes helpful comments if necessary.

**Output**
Output *only* the final code block wrapped in triple backticks (```tsx ... ```).  
Do not add any other text before or after the code block.
""",
    description="Refactors React code according to review.",
    output_key="refactored_code",
)

# ─── 4. Sequential Pipeline Agent ────────────────────────────
code_pipeline_agent = SequentialAgent(
    name="ReactCodePipelineAgent",
    description="Pipeline: generate → review → refactor React/TS code.",
    sub_agents=[
        react_writer_agent,
        react_reviewer_agent,
        react_refactorer_agent,
    ],
)

# ADK root agent
root_agent = code_pipeline_agent