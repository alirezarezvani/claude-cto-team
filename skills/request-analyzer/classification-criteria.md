# Classification Criteria

Detailed routing logic for request classification.

## Routing Decision Tree

```
START
  │
  ├─ Contains "is this solid?" / "thoughts on" / "review my plan" / "validate"
  │   └─► Type: VALIDATE → strategic-cto-mentor
  │
  ├─ Contains "how should I build" / "design" / "architect" / "what stack"
  │   └─► Type: DESIGN → cto-architect
  │
  ├─ Contains "fix" / "broken" / "error" / "not working" / "slow"
  │   └─► Type: DEBUG → debug-helper (via cto-orchestrator coordination)
  │
  ├─ Contains "document" / "explain" / "write docs" / "API reference"
  │   └─► Type: DOCUMENT → docs-writer
  │
  ├─ Contains "review code" / "check for issues" / "code quality"
  │   └─► Type: REVIEW → code-reviewer
  │
  ├─ Contains vague buzzwords (see buzzword-dictionary.md)
  │   └─► CLARIFY FIRST → clarification-protocol
  │
  └─ Complex / multi-domain
      └─► ORCHESTRATE → cto-orchestrator coordinates multiple agents
```

## Agent Routing Matrix

| Request Pattern | Primary Agent | Secondary Agents |
|-----------------|---------------|------------------|
| New system architecture | cto-architect | - |
| Technology selection | cto-architect | - |
| Implementation roadmap | cto-architect | strategic-cto-mentor (validation) |
| Plan validation | strategic-cto-mentor | cto-architect (if redesign needed) |
| Build vs buy decision | strategic-cto-mentor | cto-architect (if build selected) |
| Timeline stress-test | strategic-cto-mentor | - |
| ML/AI specific design | cv-ml-architect | cto-architect (integration) |
| Code review | code-reviewer | - |
| Test strategy | test-writer | - |
| Bug investigation | debug-helper | code-reviewer |
| Documentation | docs-writer | - |

## Complexity Assessment Criteria

### Single Agent (Simple)

- Clear, focused scope
- One domain (backend, frontend, ML, etc.)
- Obvious routing
- No dependencies on other agent outputs

**Examples:**
- "Design a REST API for user management"
- "Review this authentication code"
- "Is my database schema solid?"

### Sequential (Medium)

- Multiple phases that depend on each other
- Output from one agent feeds into another
- Clear order of operations

**Pattern:** Agent A → Agent B → [Optional: Agent C]

**Examples:**
- "Design and then validate our new architecture"
- "Create roadmap, then stress-test the timeline"
- "Build test strategy after reviewing the code"

### Parallel (Complex)

- Multiple independent domains
- Can execute simultaneously
- Requires synthesis of multiple outputs

**Pattern:** [Agent A, Agent B, Agent C] → Synthesize

**Examples:**
- "Full system design: backend, ML pipeline, and mobile app"
- "Review security, performance, and maintainability"

## Intent Classification Details

### Strategic Intent

**Indicators:**
- Future-focused language
- Resource allocation discussions
- Prioritization questions
- Long-term planning

**Key phrases:**
- "Our roadmap for..."
- "Should we prioritize..."
- "What's the strategy for..."
- "How should we approach..."

### Implementation Intent

**Indicators:**
- Building something new
- Technical specifications
- Architecture questions
- Stack selection

**Key phrases:**
- "How do we build..."
- "What's the best way to implement..."
- "Design a system that..."
- "Which technology should we use for..."

### Debugging Intent

**Indicators:**
- Something is broken
- Performance issues
- Unexpected behavior
- Error messages

**Key phrases:**
- "Why is X not working..."
- "How do I fix..."
- "Getting this error..."
- "Performance is degraded..."

### Documentation Intent

**Indicators:**
- Explaining existing systems
- Creating references
- Onboarding materials
- API documentation

**Key phrases:**
- "Document how X works..."
- "Write a guide for..."
- "Explain the architecture of..."
- "Create API docs for..."
