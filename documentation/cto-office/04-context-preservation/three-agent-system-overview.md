# Three-Agent System Overview

**Last Updated**: December 4, 2025
**Maintainer**: Claude Code / Technical Writer Agent
**Version**: 1.0

## Overview

The **CTO Office Three-Agent System** is a comprehensive framework for strategic technical leadership that combines coordination, design, and validation capabilities. This document explains the philosophy, design principles, and architecture of the system.

## System Philosophy

### The Problem: Vague Requirements → Weak Strategies → Failed Implementations

Traditional approaches to technical strategy often fail because:
- **Vague requirements** are accepted without challenge
- **Designs are created** without sufficient validation
- **Plans are implemented** without stress-testing assumptions
- **Failures happen** in production, not during planning

### The Solution: Checks and Balances

The three-agent system implements a checks-and-balances mechanism:

1. **cto-orchestrator** ensures requirements are clear before design begins
2. **cto-architect** creates comprehensive, well-thought-out designs
3. **strategic-cto-mentor** provides ruthless validation before resource commitment

This prevents:
- ❌ Implementing vague requirements (orchestrator catches this)
- ❌ Weak architectures reaching production (architect designs robustly)
- ❌ Wishful thinking driving decisions (mentor challenges assumptions)

## System Design Principles

### Principle 1: Role Separation

Each agent has a distinct, non-overlapping role:

| Role | Agent | Responsibility |
|------|-------|----------------|
| **Coordination** | cto-orchestrator | Clarify vague requests, route to specialists, manage multi-agent workflows |
| **Design** | cto-architect | Create architecture, select technologies, plan implementation |
| **Validation** | strategic-cto-mentor | Challenge assumptions, stress-test plans, identify risks |

**Why this matters**: Prevents role confusion and ensures each agent excels at its specialty.

### Principle 2: Sequential Validation

Design and validation happen sequentially, not simultaneously:

```
Requirements Clarification (orchestrator)
    ↓
Design Creation (architect)
    ↓
Design Validation (mentor)
    ↓
Design Refinement (architect)
    ↓
Implementation
```

**Why this matters**: Separating design from critique ensures:
- Designer focuses on comprehensive solutions
- Validator provides unbiased assessment
- Feedback loop improves quality

### Principle 3: Context Preservation

Information flows seamlessly between agents:

- Orchestrator → Architect: Structured requirements
- Architect → Mentor: Complete design with rationale
- Mentor → Architect: Specific feedback with concerns
- All agents: Maintain conversation context

**Why this matters**: Prevents information loss and redundant questions.

### Principle 4: Strategic Rigor

Every agent challenges wishful thinking:

- **Orchestrator**: Challenges vague buzzwords
- **Architect**: Designs with explicit trade-offs
- **Mentor**: Stress-tests all assumptions

**Why this matters**: Prevents fantasy timelines and unrealistic plans.

## System Architecture

### Information Flow

```
┌─────────────────────────────────────────────────────────┐
│                         USER                            │
└──────────────────┬──────────────────────────────────────┘
                   │ Request (may be vague)
                   ↓
┌──────────────────────────────────────────────────────────┐
│              cto-orchestrator                            │
│  • Clarifies requirements                                │
│  • Challenges vague buzzwords                            │
│  • Routes to appropriate specialist                      │
└───┬────────────────────────┬─────────────────────────────┘
    │                        │
    │ Design Request         │ Validation Request
    ↓                        ↓
┌─────────────────┐    ┌──────────────────────┐
│ cto-architect   │    │ strategic-cto-mentor │
│ • System design │    │ • Challenge          │
│ • Tech stack    │    │ • Validate           │
│ • Roadmap       │────┤ • Stress-test        │
└─────────────────┘    └──────────────────────┘
    ↑  Feedback              │
    └────────────────────────┘
```

### Agent Interactions

#### Interaction 1: Orchestrator → Architect (Design Request)
**When**: User needs architecture, technology decisions, or roadmap
**Flow**:
1. Orchestrator clarifies requirements
2. Orchestrator provides structured context to architect
3. Architect creates comprehensive design
4. Architect may recommend validation checkpoint

#### Interaction 2: Architect → Mentor (Validation Request)
**When**: High-stakes decision, aggressive timeline, or significant resources
**Flow**:
1. Architect completes design
2. Architect recommends validation (if appropriate)
3. Mentor validates design with ruthless honesty
4. Mentor provides specific feedback

#### Interaction 3: Mentor → Architect (Feedback Loop)
**When**: Mentor identifies flaws or concerns
**Flow**:
1. Mentor provides critical feedback
2. Architect receives feedback non-defensively
3. Architect refines design addressing concerns
4. Updated design ready for implementation (or re-validation)

#### Interaction 4: Orchestrator → Mentor (Direct Validation)
**When**: User presents existing plan for validation
**Flow**:
1. Orchestrator recognizes validation request
2. Orchestrator routes to mentor
3. Mentor validates plan
4. If major issues, orchestrator may coordinate architect for redesign

### Multi-Agent Orchestration

For complex, multi-domain projects:

```
User Request (complex)
    ↓
cto-orchestrator
    ├→ cto-architect (overall system)
    ├→ cv-ml-architect (ML specifics)
    ├→ test-writer (testing strategy)
    └→ docs-writer (documentation)
    ↓
cto-orchestrator (synthesizes)
    ↓
strategic-cto-mentor (validates complete plan)
    ↓
Implementation
```

## Role Distribution

### The Friendly Gatekeeper: cto-orchestrator

**Personality**: Conversational but strategically rigorous
**Job**: Keep things moving efficiently while recognizing when validation is needed

**Key behaviors**:
- Challenges vague requests: "What do you mean by 'AI-powered'?"
- Routes intelligently: Design → architect, Validation → mentor
- Maintains velocity: Fast clarification, efficient coordination
- Recognizes risk: "That timeline looks tight - let's validate with mentor"

**Not**: Ruthless critic, deep technical designer

### The Professional Designer: cto-architect

**Personality**: Professional, comprehensive, systematic
**Job**: Create bulletproof architecture designs and implementation roadmaps

**Key behaviors**:
- Designs comprehensively: System architecture, tech stack, roadmap
- Balances trade-offs: Explicit pros/cons for every decision
- Plans phased delivery: MVP → Scale → Advanced with validation checkpoints
- Recommends validation: Proactively suggests mentor review for high-stakes decisions

**Not**: Validator/critic, coordinator

### The Ruthless Critic: strategic-cto-mentor

**Personality**: Brutally honest, direct, confrontational
**Job**: Tear apart weak plans and prevent disasters

**Key behaviors**:
- Never sugarcoats: "This timeline is fantasy"
- Challenges everything: Questions every assumption
- Identifies patterns: Recognizes Premature Optimization, Shiny Object Syndrome, etc.
- Provides alternatives: After criticism, offers concrete improvements

**Not**: Designer, coordinator

## Validation Checkpoints

The architect proactively includes validation checkpoints in roadmaps:

### Checkpoint 1: Before MVP Implementation
**Questions**:
- Is architecture appropriate for scale?
- Is technology stack realistic for team?
- Is timeline achievable?
- Is team capacity sufficient?

### Checkpoint 2: Before Scaling Effort
**Questions**:
- Did Phase 1 deliver as expected?
- Is scaling strategy sound?
- Are cost projections realistic?
- Does team have bandwidth?

### Checkpoint 3: Before Advanced Features
**Questions**:
- Is Phase 3 needed or is optimization better?
- Are priorities correct?
- Is business case solid?

## Success Patterns

### Pattern 1: Full Design-Validate-Refine (High-Stakes)
**Use for**: Major projects, significant resource commitment

**Flow**:
1. User request → Orchestrator clarifies
2. Architect designs comprehensively
3. Mentor validates ruthlessly
4. Architect refines based on feedback
5. Implementation begins

**Result**: Robust, validated strategy minimizing risk

### Pattern 2: Design-Only (Low-Stakes)
**Use for**: Straightforward projects, well-understood patterns

**Flow**:
1. User request (clear) → Orchestrator routes
2. Architect designs
3. Implementation begins

**Result**: Fast execution with acceptable risk

### Pattern 3: Validation-First (Existing Plan)
**Use for**: User already has plan, needs validation

**Flow**:
1. User presents plan → Orchestrator recognizes validation need
2. Mentor validates
3. If major issues: Architect redesigns
4. Implementation begins

**Result**: Existing plans stress-tested before resource commitment

## Failure Modes and Prevention

### Failure Mode 1: Vague Requirements Implemented
**Without system**: Vague request → Developer guesses → Wrong implementation
**With system**: Orchestrator challenges vagueness → Clear requirements → Correct implementation

### Failure Mode 2: Weak Architecture Deployed
**Without system**: Quick design → Implementation → Production failure
**With system**: Architect designs → Mentor validates → Robust architecture → Stable production

### Failure Mode 3: Fantasy Timeline Committed
**Without system**: Optimistic estimate → Team burns out → Deadline missed
**With system**: Architect estimates → Mentor stress-tests → Realistic timeline → Deadline met

### Failure Mode 4: Wrong Technology Chosen
**Without system**: Trendy tech selected → Team struggles → Project fails
**With system**: Architect evaluates → Mentor challenges assumptions → Right tech → Success

## Integration with Other Agents

### cv-ml-architect (ML Specialist)
**Relationship**: Architect delegates ML-specific decisions to cv-ml-architect
**Flow**: Architect (overall system) → cv-ml-architect (ML specifics) → Architect (integrates)

### Native Agents (Implementation Specialists)
**Relationship**: Architect requests help from native agents for specific tasks
**Examples**:
- test-writer: Design testing strategy
- docs-writer: Create architectural documentation
- code-reviewer: Review architecture decision records

## Context Preservation Across Projects

### Project Documentation (This Directory)
**Location**: `documentation/cto-office/`
**Purpose**: Reference implementation, patterns, and guidelines
**Use**: Template for all projects using CTO Team agents

### Per-Project Adaptation
**Location**: `[your-project]/documentation/cto-office/`
**Purpose**: Project-specific context, decisions, and adaptations
**Use**: Maintain project history and decisions

**Example**:
- Clone this repo's `documentation/cto-office/` to your project
- Customize for your project-specific context and decisions

## Benefits of the System

### For CTOs and Technical Leaders
- ✅ Validated strategies before resource commitment
- ✅ Comprehensive architectures with trade-off analysis
- ✅ Stress-tested assumptions and realistic timelines
- ✅ Clear collaboration patterns for complex projects

### For Product Owners and Product Managers
- ✅ Clear routing decisions (which agent for what)
- ✅ Predictable outputs and timelines
- ✅ Validated roadmaps for stakeholder presentation
- ✅ Traceable decision-making process

### For Engineering Teams
- ✅ Clear, well-defined requirements
- ✅ Comprehensive technical strategies
- ✅ Realistic timelines with proper planning
- ✅ Validation checkpoints preventing wasted effort

## Getting Started

### For Your First Project

1. **Start with orchestrator** if request is vague or multi-domain
2. **Review agent specifications** to understand capabilities
3. **Follow workflow patterns** documented in capability matrix
4. **Include validation checkpoints** for high-stakes decisions
5. **Create project-specific documentation** to preserve context

### For Roadmap Planning

1. **Engage architect** to design roadmap with phased approach
2. **Include validation checkpoints** at critical decision points
3. **Validate with mentor** before presenting to stakeholders
4. **Refine based on feedback** incorporating mentor's critique
5. **Present validated roadmap** to Human CTO with confidence

## Version History

| Version | Date | Changes | Maintainer |
|---------|------|---------|------------|
| 1.0 | 2025-12-04 | Initial system overview | Claude Code |

## Related Documentation

- [Agent Capability Matrix](../02-collaboration-patterns/agent-capability-matrix.md)
- [cto-orchestrator Specification](../01-agent-specifications/cto-orchestrator-spec.md)
- [strategic-cto-mentor Specification](../01-agent-specifications/strategic-cto-mentor-spec.md)
- [cto-architect Specification](../01-agent-specifications/cto-architect-spec.md)
- [README](../README.md)
