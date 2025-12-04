# Mentor Delegation Template

Use this template when delegating validation work to **strategic-cto-mentor**.

## Template

```markdown
## CONTEXT

### What's Being Validated
[Brief description of the plan/proposal/decision being reviewed]

### Business Context
- **Company Stage**: [Startup/Growth/Enterprise]
- **Primary Goal**: [What success looks like]
- **Timeline Pressure**: [Why this timeline?]
- **Resource Situation**: [Team capacity, budget reality]

### The Proposal/Plan
[Attach or summarize the plan being validated]

Key points:
- [Point 1]
- [Point 2]
- [Point 3]

### Known Risks and Concerns
[What the proposer already knows might be weak]
- [Concern 1]
- [Concern 2]

---

## TASK

### Primary Deliverable
Provide ruthless validation of [plan/proposal/decision] with a clear verdict

### Format Requirements
Use the standard 8-section validation report:
1. **Verdict**: GOOD / BAD / NEEDS MAJOR WORK
2. **What You Got Right**: 2-3 specific strengths
3. **Critical Flaws**: Major weaknesses (Flaw → Why It Matters → Consequence)
4. **What You're Not Considering**: Blindspots and hidden assumptions
5. **The Real Question**: Reframe if solving wrong problem
6. **What Bulletproof Looks Like**: Criteria for success
7. **Recommended Path Forward**: Concrete next steps
8. **Questions You Need to Answer First**: Information gaps

### Focus Areas
Specifically stress-test:
- [ ] [Area 1: e.g., "Timeline feasibility"]
- [ ] [Area 2: e.g., "Team capacity to execute"]
- [ ] [Area 3: e.g., "Technical assumptions"]

### Validation Dimensions
Evaluate against the 7 dimensions:
1. Business Impact
2. Technical Risk
3. Operational Risk
4. Financial Risk
5. Timeline Risk
6. Team Risk
7. Market Risk

---

## REQUIREMENTS

### Must Evaluate
- [ ] Are the core assumptions valid?
- [ ] Is the timeline realistic given the team?
- [ ] Are the costs accurately estimated?
- [ ] What happens when things go wrong?

### Must Identify
- [ ] Hidden assumptions not explicitly stated
- [ ] Anti-patterns (Premature Optimization, Shiny Object, Timeline Fantasy, etc.)
- [ ] Missing contingency plans
- [ ] Resource conflicts with other initiatives

### Honesty Level
Be ruthlessly honest. Better to hear hard truths now than learn them in production. This is not a rubber stamp exercise.

---

## ADDITIONAL CONTEXT

### Stakeholder Dynamics
- [Who proposed this? Their track record?]
- [Who needs to approve? What do they care about?]
- [Political considerations?]

### Previous Related Decisions
- [What was tried before?]
- [What constraints exist from past choices?]

### What Success Looks Like
- [How will we know this validation was valuable?]
- [What decisions will this inform?]

---

## AFTER VALIDATION

### If Verdict is GOOD
- Proceed to implementation planning
- Document key assumptions that were validated

### If Verdict is NEEDS MAJOR WORK
- Route feedback to cto-architect for revision
- Identify specific areas to address
- Plan re-validation after changes

### If Verdict is BAD
- Stop before committing resources
- Identify if problem should be reframed entirely
- Consider alternative approaches
```

## Example: Q2 Roadmap Validation

```markdown
## CONTEXT

### What's Being Validated
Q2 2025 Technical Roadmap for the engineering team

### Business Context
- **Company Stage**: Series A startup, 18 months runway
- **Primary Goal**: Hit growth targets to raise Series B
- **Timeline Pressure**: Board expects 3x user growth by Q4
- **Resource Situation**: 12 engineers, hiring 4 more in Q2

### The Proposal/Plan
**Q2 Roadmap:**
1. Migrate monolith to microservices (8 weeks)
2. Implement real-time features (4 weeks)
3. Refactor payment system (3 weeks)
4. Launch mobile app v2 (6 weeks)

Key points:
- All items marked as "must-do" by product team
- Timeline assumes 4 new hires are productive by week 3
- No buffer allocated for unexpected issues
- Engineering lead confident it's "aggressive but achievable"

### Known Risks and Concerns
- New hires might take longer to onboard
- Microservices migration has never been done before
- Payment refactor requires coordination with finance team

---

## TASK

### Primary Deliverable
Validate the Q2 roadmap with focus on feasibility and risk

### Format Requirements
Standard 8-section validation report with emphasis on:
- Timeline reality check
- Team capacity analysis
- Dependency and sequencing issues

### Focus Areas
Specifically stress-test:
- [ ] Microservices migration timeline (8 weeks realistic?)
- [ ] Assumption that new hires productive in week 3
- [ ] Parallel execution of 4 major initiatives
- [ ] Zero buffer in the plan

### Validation Dimensions
Pay special attention to:
- **Timeline Risk**: Is this achievable?
- **Team Risk**: Can the team execute this?
- **Operational Risk**: What can go wrong?

---

## REQUIREMENTS

### Must Evaluate
- [ ] Is 8 weeks realistic for microservices migration with this team?
- [ ] What's the blast radius if one initiative slips?
- [ ] Are there hidden dependencies between the 4 items?
- [ ] What happens if new hires don't start or ramp slowly?

### Must Identify
- [ ] Timeline Fantasy indicators
- [ ] Hero Culture dependencies (who must not quit?)
- [ ] Missing contingency plans
- [ ] Optimistic assumptions stated as facts

### Honesty Level
The engineering lead is emotionally invested in this plan. Challenge it anyway. Better to have a hard conversation now than miss Q2 targets.

---

## ADDITIONAL CONTEXT

### Stakeholder Dynamics
- Engineering lead proposed this (first time leading roadmap)
- CEO is pushing for aggressive growth
- CTO is on sabbatical until March
- Board meeting in May (will review Q2 progress)

### Previous Related Decisions
- Last quarter's roadmap was 60% delivered
- Microservices discussion started 6 months ago, no progress yet
- Mobile app v1 launch took 50% longer than planned

### What Success Looks Like
- Clear understanding of what's achievable
- Prioritized list if something must be cut
- Risk mitigation strategies for likely failure points

---

## AFTER VALIDATION

### If Verdict is GOOD
- Present to leadership with confidence
- Document assumptions being accepted

### If Verdict is NEEDS MAJOR WORK
- Work with engineering lead to revise scope
- Identify which items can be deferred to Q3
- Add realistic buffers

### If Verdict is BAD
- Escalate to leadership before committing
- Propose alternative scoping
- Prevent team burnout from impossible plan
```
