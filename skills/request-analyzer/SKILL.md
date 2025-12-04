---
name: request-analyzer
description: Analyze incoming user requests to detect intent, request type (design/validate/debug/document), complexity level, and identify vague requirements or buzzwords that need clarification. Use when cto-orchestrator receives new requests that need classification before routing to specialist agents.
---

# Request Analyzer

Classifies incoming requests to enable intelligent routing and identify clarification needs before delegating to specialist agents.

## When to Use

- When receiving a new user request that needs classification
- When determining which specialist agent should handle a request
- When identifying if requirements are too vague to proceed
- When detecting buzzwords that need to be challenged

## Analysis Framework

### Step 1: Detect Intent

Classify the primary intent:

| Intent | Indicators | Route |
|--------|------------|-------|
| **Strategic** | "roadmap", "strategy", "plan", "prioritize", "decide" | May need validation |
| **Implementation** | "build", "create", "implement", "design", "architect" | Design work |
| **Debugging** | "fix", "broken", "error", "slow", "not working" | Debug/investigate |
| **Documentation** | "document", "explain", "describe", "write docs" | Documentation |

### Step 2: Classify Request Type

| Type | Key Phrases | Primary Agent |
|------|-------------|---------------|
| **Design** | "How should I build...", "What architecture...", "Design a system..." | cto-architect |
| **Validate** | "Is this plan solid?", "Thoughts on...", "Review my roadmap..." | strategic-cto-mentor |
| **Debug** | "Why is X slow?", "Fix this error...", "Troubleshoot..." | debug-helper |
| **Document** | "Write documentation for...", "Explain how..." | docs-writer |
| **Review** | "Review this code...", "Check for issues..." | code-reviewer |

### Step 3: Assess Complexity

| Complexity | Characteristics | Execution Pattern |
|------------|-----------------|-------------------|
| **Single** | Clear scope, one domain, obvious routing | Direct to one agent |
| **Sequential** | Multiple phases, depends on previous output | Agent chain |
| **Parallel** | Independent domains, can run simultaneously | Multiple agents in parallel |

### Step 4: Identify Vague Terms

Scan for buzzwords that require clarification. See [buzzword-dictionary.md](buzzword-dictionary.md) for the complete list.

**Common red flags:**
- "AI-powered" - What specific AI capability?
- "scale" - What numbers? From what to what?
- "fast" / "soon" - What timeline exactly?
- "simple" - Simple for whom? What constraints?
- "modern" - What specific technologies?

### Step 5: Detect Missing Context

Check for required context based on request type:

**For Design Requests:**
- [ ] Expected user/traffic scale
- [ ] Budget constraints
- [ ] Timeline requirements
- [ ] Team size and expertise
- [ ] Existing infrastructure

**For Validation Requests:**
- [ ] Current state or existing plan
- [ ] Business goals and constraints
- [ ] Timeline and resources
- [ ] Success criteria

## Output Format

Provide analysis in this structure:

```
## Request Analysis

**Intent**: [strategic | implementation | debugging | documentation]
**Type**: [design | validate | debug | document | review]
**Complexity**: [single | sequential | parallel]

### Vague Terms Detected
- "[term]" - needs clarification: [what to ask]

### Missing Context
- [missing information item]

### Suggested Routing
**Primary Agent**: [agent name]
**Rationale**: [why this agent]

### Clarification Needed
[yes/no] - [brief explanation]

### Recommended Next Step
[what to do next - clarify or delegate]
```

## Examples

### Example 1: Vague Request

**User**: "I want to add AI capabilities to my app"

**Analysis**:
- **Intent**: Implementation
- **Type**: Design
- **Complexity**: Unknown (needs clarification)
- **Vague Terms**: "AI capabilities" - What specific problem are we solving?
- **Missing Context**: Scale, budget, timeline, team, existing stack
- **Clarification Needed**: Yes
- **Next Step**: Use clarification-protocol before routing

### Example 2: Clear Design Request

**User**: "Design a real-time notification system for 100K users, using our existing PostgreSQL database and Node.js backend"

**Analysis**:
- **Intent**: Implementation
- **Type**: Design
- **Complexity**: Single
- **Vague Terms**: None
- **Missing Context**: Timeline, budget (nice to have but not blocking)
- **Suggested Routing**: cto-architect
- **Clarification Needed**: No (can proceed with optional clarification)

### Example 3: Validation Request

**User**: "Here's my Q2 roadmap - migrate to microservices, add real-time features, and launch mobile app. Thoughts?"

**Analysis**:
- **Intent**: Strategic
- **Type**: Validate
- **Complexity**: Single
- **Vague Terms**: None
- **Missing Context**: Team size, current architecture state
- **Suggested Routing**: strategic-cto-mentor
- **Clarification Needed**: Mild (some context helpful but not blocking)

## References

- [Classification Criteria](classification-criteria.md) - Detailed routing logic
- [Buzzword Dictionary](buzzword-dictionary.md) - Common vague terms to challenge
