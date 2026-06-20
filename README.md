# eazyfit — model-aware compiler

A FastAPI service that compiles raw user prompts and optional document attachments into structured, model-aware markdown. The goal: give LLMs signal, not noise.

## What it does

Raw prompts are often ambiguous, verbose, or poorly structured for LLM consumption. eazyfit parses your intent and any attached documents, then compiles them into a clean `.md` file with explicit context, task, constraints, and an optimised prompt — reducing computational waste and improving response quality.

## Pipeline

```
User prompt + attachments (PDF, DOCX, images)
        |
  [LlamaParse]  →  extracts structured content from documents
        |
  [GPTCache]    →  semantic cache check (similarity threshold)
        |              hit → return cached compiled output
  [LangChain]   →  orchestrates the pipeline
        |
    [DSPy]      →  compiles raw prompt + doc context into structured output
        |
  [LangSmith]   →  traces every step (latency, tokens, prompt versions)
        |
  Markdown .md output:
    ## Context         ← distilled from documents
    ## Task            ← clear, unambiguous instruction
    ## Constraints     ← model hints (format, scope, tone)
    ## Compiled Prompt ← final optimised prompt
```

## Stack

| Layer | Tool | Purpose |
|---|---|---|
| API | FastAPI | Request ingestion |
| Document parsing | LlamaParse | PDF, DOCX, images → structured text |
| Orchestration | LangChain | Pipeline composition |
| Prompt compilation | DSPy | Raw prompt → model-aware prompt |
| Semantic caching | GPTCache | Reproducibility + cost reduction |
| Observability | LangSmith | Tracing, prompt tracking, token usage |

## Project structure

```
eazyfit-model-aware-compiler/
├── main.py                          # FastAPI entry point
├── project.toml                     # Project metadata and dependencies
├── .env.example                     # Environment variable template
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── compiler.py          # /compile endpoint
│   ├── core/
│   │   ├── parser/
│   │   │   └── document_parser.py   # LlamaParse integration
│   │   ├── compiler/
│   │   │   └── prompt_compiler.py   # DSPy signatures + compilation
│   │   ├── cache/
│   │   │   └── semantic_cache.py    # GPTCache integration
│   │   └── pipeline/
│   │       └── chain.py             # LangChain orchestration
│   ├── models/
│   │   ├── request.py               # Pydantic request models
│   │   └── response.py              # Pydantic response models
│   ├── utils/
│   │   └── markdown.py              # Markdown output renderer
│   └── settings/
│       └── config.py                # Environment config
```

## Setup

**1. Clone and create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
# or with uv:
uv pip install -r requirements.txt
```

**3. Configure environment**
```bash
cp .env.example .env
# fill in your API keys
```

**4. Run**
```bash
uvicorn main:app --reload
```

## API

### `POST /compiler/compile`

Accepts a prompt and optional file attachments. Returns a compiled, model-aware markdown output.

**Request** (multipart/form-data):

| Field | Type | Required | Description |
|---|---|---|---|
| `prompt` | string | yes | Raw user prompt |
| `files` | file[] | no | Documents to parse (PDF, DOCX, images) |

**Response**:
```json
{
  "compiled_prompt": "...",
  "markdown": "...",
  "context": "...",
  "task": "...",
  "constraints": "..."
}
```

### `GET /`

Health check.

## Environment variables

See `.env.example` for the full list.
