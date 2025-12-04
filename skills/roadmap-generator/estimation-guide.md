# Estimation Guide

Detailed techniques for accurate effort estimation in technical roadmaps.

## The Estimation Problem

Humans are notoriously bad at estimation, especially for:
- Novel work (never done before)
- Complex work (many unknowns)
- Long-duration work (> 2 weeks)

This guide provides techniques to improve accuracy.

---

## T-Shirt Sizing Deep Dive

### Size Definitions

| Size | Points | Duration | Characteristics | Example |
|------|--------|----------|-----------------|---------|
| **XS** | 1 | 2-4 hours | Config change, copy update, trivial fix | Change environment variable |
| **S** | 2 | 0.5-1 day | Simple, well-understood, no dependencies | Add new API field |
| **M** | 3 | 1-2 days | Some complexity, minor unknowns | Build CRUD endpoint |
| **L** | 5 | 3-5 days | Complex, research needed | Implement authentication |
| **XL** | 8 | 1-2 weeks | Very complex, significant unknowns | Build recommendation engine |
| **XXL** | 13+ | > 2 weeks | Must be broken down | Full microservice |

### When to Use Each Size

**XS - Trivial**
- You've done this exact thing before
- No code review concerns
- Can be done and deployed in one sitting

**S - Simple**
- Clear implementation path
- Single component affected
- Standard patterns apply

**M - Standard**
- Normal feature work
- May need some research
- Touches 2-3 files/components

**L - Complex**
- Multiple components affected
- Integration work required
- Some architectural decisions

**XL - Very Complex**
- Significant unknowns
- New technology/patterns
- Cross-team coordination
- Should consider breaking down

**XXL - Epic-level**
- Too large for single story
- Must be decomposed
- Red flag if assigned to single item

---

## Estimation Techniques

### 1. Reference-Based Estimation

Compare to similar past work:

```
Previous similar feature: 3 weeks
Complexity adjustment: 1.2x (slightly more complex)
Team familiarity: 0.9x (more familiar now)
Estimate: 3 × 1.2 × 0.9 = 3.2 weeks
```

### 2. Task Decomposition

Break down until tasks are < 1 day:

```
Feature: User Dashboard

Tasks:
├── Design API schema (S: 4h)
├── Implement backend endpoint (M: 8h)
├── Create React components (M: 12h)
├── Write unit tests (S: 4h)
├── Integration tests (S: 4h)
├── Documentation (XS: 2h)
└── Code review + fixes (S: 4h)

Total: 38 hours ≈ 5 days
Add 25% buffer: 6.25 days
Estimate: L (3-5 days) → round up to 1.5 weeks
```

### 3. Three-Point Estimation

Estimate optimistic, most likely, and pessimistic:

```
Optimistic (O): Everything goes perfectly = 3 days
Most Likely (M): Normal development = 5 days
Pessimistic (P): Everything goes wrong = 12 days

PERT Estimate = (O + 4M + P) / 6
             = (3 + 20 + 12) / 6
             = 5.8 days
```

### 4. Planning Poker

Team-based estimation:
1. Present story to team
2. Everyone estimates privately
3. Reveal estimates simultaneously
4. Discuss outliers
5. Re-estimate until consensus

---

## Adjustment Factors

### Multipliers to Apply

| Factor | Multiplier | When to Apply |
|--------|------------|---------------|
| **New technology** | 1.5x | Team hasn't used tech before |
| **New team member** | 1.3x | < 3 months on project |
| **External dependency** | 1.2x | Per external team/service |
| **Legacy code** | 1.4x | Poorly documented old code |
| **Compliance requirements** | 1.3x | Security/audit requirements |
| **Cross-timezone** | 1.2x | Team spans > 6 hour difference |

### Velocity Adjustments

```
Theoretical capacity:
  5 engineers × 40 hours = 200 hours/week

Realistic capacity (apply factors):
  - Meetings/admin: 0.8x
  - Context switching: 0.85x
  - Interruptions: 0.9x
  - Learning/research: 0.9x

Effective capacity:
  200 × 0.8 × 0.85 × 0.9 × 0.9 = 110 hours/week

That's 55% of theoretical!
```

---

## Common Estimation Mistakes

### 1. The 90% Done Trap
**Mistake**: "We're 90% done" for weeks.
**Fix**: Track tasks to completion, not percentage.

### 2. Ignoring Integration
**Mistake**: Estimate components in isolation.
**Fix**: Add explicit integration tasks and testing.

### 3. Happy Path Only
**Mistake**: Estimate assumes no bugs, no blockers.
**Fix**: Always add 20-30% buffer.

### 4. Scope Creep Blindness
**Mistake**: Estimate original scope, deliver expanded scope.
**Fix**: Re-estimate when scope changes.

### 5. Anchoring
**Mistake**: First estimate biases all subsequent estimates.
**Fix**: Use planning poker, estimate independently first.

### 6. Planning Fallacy
**Mistake**: Optimism despite past evidence.
**Fix**: Compare to actual duration of past similar work.

---

## Estimation for Different Phases

### Phase 1: MVP
- Estimate in detail (story/task level)
- Add 25% buffer
- Expect 20% scope change

### Phase 2: Scale
- Estimate at epic level
- Add 30% buffer
- Expect 30% scope change

### Phase 3: Advanced
- Estimate at theme level only
- Add 40% buffer
- Expect 50% scope change

---

## Team Velocity

### Calculating Historical Velocity

```
Sprint 1: 34 points completed
Sprint 2: 28 points completed
Sprint 3: 31 points completed
Sprint 4: 35 points completed

Average velocity: 32 points/sprint
Standard deviation: 2.9 points

Conservative estimate: 29 points/sprint (avg - 1 std dev)
```

### Using Velocity for Planning

```
Total backlog: 180 points
Conservative velocity: 29 points/sprint
Sprints needed: 180 / 29 = 6.2 sprints

Add buffer (20%): 7.5 sprints
Estimate: 8 sprints (4 months with 2-week sprints)
```

---

## Estimation Checklist

Before finalizing estimates, verify:

- [ ] Broke down items to < 1 week
- [ ] Considered integration time
- [ ] Accounted for testing
- [ ] Included documentation
- [ ] Added code review time
- [ ] Applied technology multipliers
- [ ] Compared to past similar work
- [ ] Added 20-30% buffer
- [ ] Team agreed on estimates
- [ ] Identified dependencies

---

## Templates

### Story Estimation Template

```markdown
## Story: [Title]

### Decomposition
| Task | Estimate | Confidence |
|------|----------|------------|
| [Task 1] | 4h | High |
| [Task 2] | 8h | Medium |
| [Task 3] | 4h | Low |

### Base Estimate
Sum of tasks: 16 hours

### Adjustments
- New technology: +50% (8h)
- Integration: +20% (3h)

### Final Estimate
27 hours ≈ 3.5 days → Size: L

### Risks to Estimate
- [Risk 1]: Could add 1-2 days
- [Risk 2]: Could add 0.5 days
```

### Project Estimation Summary

```markdown
## Project: [Name]

### Estimated Duration
| Phase | Points | Weeks | Confidence |
|-------|--------|-------|------------|
| MVP | 89 | 8 | High |
| Scale | 120 | 12 | Medium |
| Advanced | 80 | 10 | Low |

### Buffer Applied
- MVP: +25% → 10 weeks
- Scale: +30% → 15.6 weeks
- Advanced: +40% → 14 weeks

### Total: 39.6 weeks (~10 months)

### Key Assumptions
1. Team of 5 engineers
2. 30 points/sprint velocity
3. No major scope changes
```
