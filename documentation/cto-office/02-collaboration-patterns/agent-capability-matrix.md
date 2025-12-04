# Agent Capability Matrix

**Last Updated**: December 4, 2025
**Maintainer**: Claude Code / Technical Writer Agent
**Version**: 1.0

## Overview

This matrix provides a quick-reference comparison of the three CTO Office agents. Use this to determine which agent to engage for specific needs.

## Quick Decision Guide

| User Says | Route To |
|-----------|----------|
| "I want to add [vague feature]" | cto-orchestrator (will clarify then route) |
| "How should I build X?" | cto-architect (design work) |
| "Is this plan solid?" | strategic-cto-mentor (validation work) |
| "Thoughts on my roadmap?" | strategic-cto-mentor (validation work) |
| "Our app is getting slow" (vague) | cto-orchestrator (will clarify scope) |
| "Design architecture for Y" | cto-architect (clear design request) |
| Complex multi-domain project | cto-orchestrator (coordinates multiple agents) |

## Comprehensive Capability Matrix

### Core Attributes

| Attribute | cto-orchestrator | strategic-cto-mentor | cto-architect |
|-----------|------------------|---------------------|---------------|
| **Primary Role** | Coordinator & Router | Validator & Critic | Designer & Builder |
| **Personality** | Friendly but rigorous | Brutally honest | Professional & systematic |
| **Model** | Sonnet (fast coordination) | Opus (deep analysis) | Opus (complex design) |
| **Color** | Green | Orange | Green |
| **Experience** | 10+ years startup operator | Decades across multiple industries | 10+ years scalable systems |

### When to Use

| Scenario | cto-orchestrator | strategic-cto-mentor | cto-architect |
|----------|------------------|---------------------|---------------|
| **Vague request** | ✅ PRIMARY | ❌ No | ❌ No |
| **Multi-domain project** | ✅ PRIMARY | ❌ No | ❌ No |
| **Design new system** | ⚠️ Routes to architect | ❌ No | ✅ PRIMARY |
| **Validate existing plan** | ⚠️ Routes to mentor | ✅ PRIMARY | ❌ No |
| **Technology selection** | ⚠️ Routes to architect | ❌ No | ✅ PRIMARY |
| **Build vs buy decision** | ⚠️ Routes to mentor | ✅ PRIMARY | ❌ No |
| **Roadmap stress-testing** | ⚠️ Routes to mentor | ✅ PRIMARY | ❌ No |
| **Implementation roadmap** | ⚠️ Routes to architect | ❌ No | ✅ PRIMARY |
| **Timeline validation** | ⚠️ Routes to mentor | ✅ PRIMARY | ❌ No |
| **Performance issues** | ✅ Clarifies & coordinates | ⚠️ If systemic issues | ⚠️ If needs redesign |

### Input Requirements

| Input Needed | cto-orchestrator | strategic-cto-mentor | cto-architect |
|--------------|------------------|---------------------|---------------|
| **Clarity required** | No - will clarify | Moderate - needs plan to validate | High - needs structured requirements |
| **Business context** | Will ask if missing | Required for validation | Required for design |
| **Technical details** | Optional initially | Helpful but not required | Ideally provided |
| **Constraints** | Will clarify | Critical for assessment | Critical for design |
| **Timeline info** | Will ask | Required for validation | Required for roadmap |

### Output Format

| Output Type | cto-orchestrator | strategic-cto-mentor | cto-architect |
|-------------|------------------|---------------------|---------------|
| **Primary deliverable** | Clarified requirements + routing plan | Validation report with verdict | Comprehensive architecture design |
| **Structure** | 1. Questions<br>2. Task decomposition<br>3. Delegation plan<br>4. Synthesis | 1. Verdict<br>2. Strengths<br>3. Critical flaws<br>4. Path forward | 1. Executive summary<br>2. System architecture<br>3. Tech stack<br>4. Roadmap<br>5. Risk assessment<br>6. Code examples<br>7. Deployment |
| **Length** | Brief (1-2 pages) | Medium (3-5 pages) | Comprehensive (10-20 pages) |
| **Tone** | Friendly but direct | Brutally honest | Professional & thorough |

### Communication Style

| Style Element | cto-orchestrator | strategic-cto-mentor | cto-architect |
|---------------|------------------|---------------------|---------------|
| **Approach** | "Let me clarify..." | "This timeline is fantasy..." | "Based on your requirements..." |
| **Questions** | 2-3 focused questions | Pointed challenging questions | Clarifying technical questions |
| **Criticism** | Gentle challenge | Ruthless critique | Balanced assessment |
| **Recommendations** | Routing decisions | Alternatives after criticism | Trade-off analysis |
| **Buzzwords** | Challenges immediately | Calls out directly | Translates to specifics |

### Collaboration Patterns

| Pattern | cto-orchestrator | strategic-cto-mentor | cto-architect |
|---------|------------------|---------------------|---------------|
| **Works with User** | Always (first contact) | When validation needed | When design needed |
| **Works with Orchestrator** | N/A (is orchestrator) | Receives validation requests | Receives design requests |
| **Works with Architect** | Routes to architect | Validates architect's designs | N/A (is architect) |
| **Works with Mentor** | Routes for validation | N/A (is mentor) | Receives mentor feedback |
| **Delegates work** | Yes (to all specialists) | Rarely (focused role) | Sometimes (to cv-ml-architect, native agents) |

### Strengths & Limitations

| Aspect | cto-orchestrator | strategic-cto-mentor | cto-architect |
|--------|------------------|---------------------|---------------|
| **Best at** | - Clarifying vague requests<br>- Multi-agent coordination<br>- Context management<br>- Efficient routing | - Stress-testing assumptions<br>- Identifying risks<br>- Calling out bad ideas<br>- Pattern recognition | - Comprehensive design<br>- Technology selection<br>- Phased roadmaps<br>- Trade-off analysis |
| **Not suitable for** | - Deep technical design<br>- Ruthless validation<br>- Implementation details | - Creating designs<br>- Coordination work<br>- Being diplomatic | - Validation/critique<br>- Coordination<br>- Being ruthless |
| **Time investment** | Fast (minutes to clarify) | Medium (30-60 min validation) | High (hours for comprehensive design) |

## Common Workflows

### Workflow 1: Full Design-Validate-Refine
```
User Request (vague)
    ↓
cto-orchestrator (clarifies requirements)
    ↓
cto-architect (designs architecture)
    ↓
strategic-cto-mentor (validates design)
    ↓
cto-architect (refines based on feedback)
    ↓
Implementation
```

**Use when**: High-stakes project, significant resource commitment, aggressive timeline

### Workflow 2: Design Only
```
User Request (clear)
    ↓
cto-orchestrator (optional, if multi-domain)
    ↓
cto-architect (designs architecture)
    ↓
Implementation
```

**Use when**: Low-stakes, straightforward, well-understood patterns

### Workflow 3: Validation Only
```
User presents plan
    ↓
cto-orchestrator (recognizes validation need)
    ↓
strategic-cto-mentor (validates plan)
    ↓
User refines OR cto-architect helps refine
    ↓
Implementation
```

**Use when**: User already has plan, needs stress-testing before proceeding

### Workflow 4: Multi-Agent Orchestration
```
User Request (complex, multi-domain)
    ↓
cto-orchestrator (breaks down, coordinates)
    ├→ cto-architect (system design)
    ├→ cv-ml-architect (ML specifics)
    ├→ test-writer (testing strategy)
    └→ docs-writer (documentation)
    ↓
cto-orchestrator (synthesizes outputs)
    ↓
strategic-cto-mentor (validates complete plan)
    ↓
Implementation
```

**Use when**: Complex project spanning multiple technical domains

## Tips for Product Owners & Product Managers

### Choosing the Right Agent

1. **Start with orchestrator if**:
   - Request is vague or spans multiple domains
   - You're not sure which agent to use
   - Need help structuring the problem

2. **Go directly to architect if**:
   - Need clear architecture design
   - Asking "How should I build X?"
   - Requirements are well-defined

3. **Go directly to mentor if**:
   - Have existing plan to validate
   - Asking "Is this solid?" or "Thoughts?"
   - Need assumptions challenged

### Setting Expectations

| Agent | Typical Time | Output Length | Follow-up Likely? |
|-------|--------------|---------------|-------------------|
| cto-orchestrator | 5-15 minutes | 1-2 pages | Yes (routes to specialists) |
| strategic-cto-mentor | 30-60 minutes | 3-5 pages | Maybe (if major flaws found) |
| cto-architect | 2-4 hours | 10-20 pages | Possibly (if validation recommended) |

### Creating Effective Roadmaps

**For roadmap creation**:
1. Start with cto-architect (design the roadmap)
2. Validate with strategic-cto-mentor (stress-test assumptions)
3. Refine based on feedback

**For roadmap validation**:
1. Start with strategic-cto-mentor (validate existing roadmap)
2. If major issues, engage cto-architect to redesign
3. Re-validate after redesign

## Version History

| Version | Date | Changes | Maintainer |
|---------|------|---------|------------|
| 1.0 | 2025-12-04 | Initial capability matrix | Claude Code |

## Related Documentation

- [cto-orchestrator Specification](../01-agent-specifications/cto-orchestrator-spec.md)
- [strategic-cto-mentor Specification](../01-agent-specifications/strategic-cto-mentor-spec.md)
- [cto-architect Specification](../01-agent-specifications/cto-architect-spec.md)
- [Three-Agent System Overview](../04-context-preservation/three-agent-system-overview.md)
