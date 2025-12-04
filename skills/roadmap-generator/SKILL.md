---
name: roadmap-generator
description: Generate phased implementation roadmaps with Epic/Story/Task breakdown, effort estimates, and validation checkpoints. Use when cto-architect needs to create actionable technical roadmaps from architecture designs.
---

# Roadmap Generator

Creates structured implementation roadmaps that transform architecture designs into actionable plans with clear phases, milestones, and validation gates.

## When to Use

- After architecture design is complete
- When translating strategic goals into execution plans
- Creating project timelines with realistic effort estimates
- Breaking down large initiatives into manageable phases

## Roadmap Structure

### Three-Phase Framework

Every roadmap follows MVP → Scale → Advanced phases:

```
Phase 1: MVP (Foundation)
├── Goal: Prove core value proposition
├── Duration: Typically 6-12 weeks
├── Success Criteria: Core functionality working
└── Exit Gate: User validation / metrics threshold

Phase 2: Scale (Growth)
├── Goal: Handle production load, improve reliability
├── Duration: Typically 8-16 weeks
├── Success Criteria: Performance SLAs met
└── Exit Gate: Load testing passed / uptime targets

Phase 3: Advanced (Optimization)
├── Goal: Competitive features, optimization
├── Duration: Ongoing
├── Success Criteria: Feature parity / differentiation
└── Exit Gate: Business metrics achieved
```

## Epic/Story/Task Hierarchy

### Epic
High-level capability that delivers business value.
- **Duration**: 2-6 weeks
- **Format**: "Enable [user] to [capability]"
- **Example**: "Enable customers to receive real-time order notifications"

### Story
User-facing functionality within an epic.
- **Duration**: 2-5 days
- **Format**: "As a [user], I want to [action] so that [benefit]"
- **Example**: "As a customer, I want push notifications so I know when my order ships"

### Task
Technical work to complete a story.
- **Duration**: 2-8 hours
- **Format**: "[Verb] [object] [context]"
- **Example**: "Implement WebSocket connection handler for notification service"

---

## Effort Estimation Framework

### T-Shirt Sizing

| Size | Story Points | Typical Duration | Characteristics |
|------|-------------|------------------|-----------------|
| XS | 1 | 2-4 hours | Trivial change, no unknowns |
| S | 2 | 0.5-1 day | Simple, well-understood |
| M | 3 | 1-2 days | Some complexity, minor unknowns |
| L | 5 | 3-5 days | Complex, some research needed |
| XL | 8 | 1-2 weeks | Very complex, significant unknowns |
| XXL | 13+ | > 2 weeks | Should be broken down |

### Estimation Guidelines

1. **Include buffer**: Add 20-30% for unknowns
2. **Account for context switching**: Multiply by 1.3 for teams juggling priorities
3. **New technology penalty**: Add 50% for unfamiliar tech
4. **Integration tax**: Add 20% for each external system integration

### Team Velocity Calculation

```
Effective Capacity = Team Size × Working Days × Focus Factor × Skill Factor

Focus Factor:
- Dedicated team: 0.8
- 50% allocated: 0.4
- Ad-hoc: 0.2

Skill Factor:
- Expert team: 1.0
- Experienced: 0.8
- Learning curve: 0.5
```

---

## Validation Checkpoints

### Phase Gate Reviews

Each phase ends with a validation gate:

```markdown
## Phase 1 Exit Gate

### Go Criteria
- [ ] Core features functional in staging
- [ ] Unit test coverage > 70%
- [ ] Integration tests passing
- [ ] Performance baseline established
- [ ] Security review completed

### No-Go Signals
- Critical bugs unresolved
- Core functionality missing
- Team capacity insufficient for Phase 2
- Business requirements changed significantly

### Decision
[ ] GO - Proceed to Phase 2
[ ] CONDITIONAL GO - Proceed with identified risks
[ ] NO-GO - Address blockers first
```

### Mid-Phase Checkpoints

- **Week 2**: Architecture validation
- **Week 4**: Integration milestone
- **Week 6**: Feature complete checkpoint
- **Weekly**: Sprint review and course correction

---

## Dependency Management

### Dependency Types

| Type | Description | Mitigation |
|------|-------------|------------|
| **Technical** | Service A needs Service B | Start B early, use mocks |
| **Team** | Need DevOps for deployment | Reserve capacity early |
| **External** | Third-party API integration | Validate early, have fallback |
| **Data** | Need production data for testing | Create synthetic data |

### Critical Path Identification

1. List all dependencies
2. Identify longest chain
3. Mark critical path items
4. Add buffer to critical path (25%)
5. Parallelize non-critical work

---

## Output Format

### Roadmap Document Structure

```markdown
# Implementation Roadmap: [Project Name]

**Created**: [Date]
**Owner**: [Team/Person]
**Architecture Reference**: [Link to architecture doc]

## Executive Summary
[2-3 sentences on approach and timeline]

## Timeline Overview
[Visual timeline or Gantt representation]

## Phase 1: MVP (Weeks 1-8)

### Phase Goals
- [Goal 1]
- [Goal 2]

### Epics

#### Epic 1.1: [Name]
**Duration**: [X weeks]
**Dependencies**: [List]

| Story | Points | Owner | Dependencies |
|-------|--------|-------|--------------|
| [Story 1] | M | [Team] | None |
| [Story 2] | L | [Team] | Story 1 |

**Tasks for Story 1**:
- [ ] [Task 1] (S)
- [ ] [Task 2] (M)

### Phase 1 Exit Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

### Phase 1 Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | High/Med/Low | High/Med/Low | [Action] |

---

## Phase 2: Scale (Weeks 9-16)
[Same structure as Phase 1]

---

## Phase 3: Advanced (Weeks 17+)
[Same structure as Phase 1]

---

## Resource Requirements

### Team Composition
| Role | Phase 1 | Phase 2 | Phase 3 |
|------|---------|---------|---------|
| Backend | 2 FTE | 3 FTE | 2 FTE |
| Frontend | 1 FTE | 2 FTE | 1 FTE |
| DevOps | 0.5 FTE | 1 FTE | 0.5 FTE |

### Infrastructure Costs
| Phase | Monthly Cost | Notes |
|-------|-------------|-------|
| Phase 1 | $X | Development environment |
| Phase 2 | $Y | Staging + production |
| Phase 3 | $Z | Full scale |

---

## Success Metrics

| Metric | Phase 1 Target | Phase 2 Target | Phase 3 Target |
|--------|---------------|----------------|----------------|
| [Metric 1] | [Value] | [Value] | [Value] |
| [Metric 2] | [Value] | [Value] | [Value] |

---

## Appendix

### Assumptions
- [Assumption 1]
- [Assumption 2]

### Open Questions
- [Question 1]
- [Question 2]
```

---

## Anti-Patterns to Avoid

### The Big Bang
Planning everything in detail upfront without iteration.
**Fix**: Plan Phase 1 in detail, Phase 2 at epic level, Phase 3 at theme level.

### The Feature Factory
Listing features without connecting to business outcomes.
**Fix**: Every epic must connect to a measurable business goal.

### The Happy Path
No buffer, no risk mitigation, assumes everything goes perfectly.
**Fix**: Add 25-30% buffer, identify top 5 risks with mitigations.

### The Kitchen Sink
Including every possible feature in MVP.
**Fix**: Ruthlessly cut to core value proposition only.

---

## Python Utilities

This skill includes Python utilities for roadmap generation:

- `generator.py` - Core roadmap generation logic
- `templates/` - Output templates (markdown, JSON)

See [generator.py](generator.py) for programmatic roadmap generation.

---

## References

- [Roadmap Templates](templates/) - Standard output formats
- [Estimation Guide](estimation-guide.md) - Detailed estimation techniques
