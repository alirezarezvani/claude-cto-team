# Anti-Pattern Catalog

Detailed examples and remediation for each anti-pattern.

---

## Architecture Anti-Patterns

### Big Ball of Mud

**What It Looks Like**:
```
┌─────────────────────────────────────┐
│  Everything calls everything else   │
│  ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐    │
│  │ A ├─┤ B ├─┤ C ├─┤ D ├─┤ E │    │
│  └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘    │
│    │     │     │     │     │       │
│    └─────┴─────┴─────┴─────┘       │
│         (all interconnected)        │
└─────────────────────────────────────┘
```

**Red Flags**:
- "We need to deploy everything together"
- "Changing the user model breaks notifications"
- "I'm not sure where this logic should go"
- Circular dependencies between modules
- 1000+ line files with mixed concerns

**Consequences**:
- Changes are risky and time-consuming
- Testing requires full system
- New developers take months to onboard
- Bugs cascade unpredictably

**Remediation**:
1. Draw actual dependency graph
2. Identify natural boundaries
3. Gradually extract modules with clear interfaces
4. Add integration tests at boundaries

---

### Golden Hammer

**What It Looks Like**:
- "We'll use Kubernetes for the static website"
- "PostgreSQL for the cache, PostgreSQL for the queue, PostgreSQL for everything"
- "React for the CLI tool"

**Red Flags**:
- Same technology for very different use cases
- Team only knows one stack
- Resistance to considering alternatives
- Justifications like "we already know it"

**Consequences**:
- Square peg, round hole implementations
- Unnecessary complexity
- Performance issues from wrong tool
- Team skill stagnation

**Remediation**:
1. Evaluate each problem independently
2. Create decision criteria matrix
3. Accept some technology diversity is healthy
4. Budget time for learning appropriate tools

---

### Premature Microservices

**What It Looks Like**:
```
Team size: 4 developers
Services: 15+ microservices
Result: Each dev responsible for 4 services
```

**Red Flags**:
- Starting with microservices for a new product
- More services than team members
- "We need to be ready to scale"
- No clear service boundaries, just "small services"

**Consequences**:
- Massive operational overhead
- Distributed system complexity (network failures, consistency)
- Slower development than monolith would be
- Deployment complexity

**Remediation**:
1. Merge back to modular monolith
2. Only split when you have clear bounded contexts
3. Rule of thumb: 1 service per 2-3 developers minimum
4. Split based on team boundaries, not technical layers

---

### Distributed Monolith

**What It Looks Like**:
```
"Microservices" that must be:
- Deployed together
- Versioned together
- Tested together
- Released together
```

**Red Flags**:
- Shared database between services
- Synchronous calls everywhere
- Breaking changes require coordinated deploys
- "We need to update all services for this change"

**Consequences**:
- All downsides of microservices (complexity, network)
- None of the benefits (independent deployment, scaling)
- Worse than a monolith

**Remediation**:
1. Acknowledge you have a distributed monolith
2. Either: separate properly OR merge back
3. Define clear API contracts
4. Move to async communication where possible

---

### Resume-Driven Development

**What It Looks Like**:
- "Let's rewrite in Rust" (for a CRUD app)
- "We should use GraphQL" (for 2 API endpoints)
- "Kubernetes would be perfect" (for a single container)

**Red Flags**:
- Technology choice can't be justified by requirements
- Justification focuses on "learning" not "solving"
- CV-worthy tech for boring problems
- Senior devs pushing tech they want experience in

**Consequences**:
- Wrong tool for the job
- Extended timeline for learning curve
- Team may not maintain after advocate leaves
- Technical debt from inexperience

**Remediation**:
1. Require explicit problem-solution mapping
2. Ask "what would we use if resumes didn't exist?"
3. Separate exploration projects from production
4. Budget for learning in side projects

---

## Timeline Anti-Patterns

### Timeline Fantasy

**What It Looks Like**:
```
Estimate: "6 weeks"
Basis: "Feels about right"
Buffer: 0%
Risks considered: 0
```

**Red Flags**:
- "If everything goes well"
- No comparison to past projects
- No buffer for unknowns
- Estimate unchanged despite scope growth

**Consequences**:
- Missed deadlines (100% certain)
- Crunch time and burnout
- Quality sacrificed
- Trust erosion

**Remediation**:
1. Compare to actual past durations
2. Add 30-50% buffer for unknowns
3. Use three-point estimation (optimistic, realistic, pessimistic)
4. Track actuals vs estimates to improve

---

### Scope Creep Blindness

**What It Looks Like**:
```
Week 1: "Build user auth"
Week 2: "...and SSO"
Week 3: "...and 2FA"
Week 4: "...and admin impersonation"
Week 5: "Why aren't we done yet?"
```

**Red Flags**:
- "While we're at it..."
- "It's just a small addition"
- Deadline stays fixed as scope grows
- No formal change process

**Consequences**:
- Deadline impossible to meet
- Team demoralized
- Quality suffers
- Original scope not delivered

**Remediation**:
1. Document original scope clearly
2. Every addition requires trade-off discussion
3. Re-estimate when scope changes
4. Make scope changes visible to stakeholders

---

### MVP Maximalism

**What It Looks Like**:
```
"MVP" feature list:
- Core functionality ✓
- Admin dashboard
- Analytics
- Multi-tenant support
- API for partners
- White-labeling
- 3 language support
- Mobile apps
```

**Red Flags**:
- MVP takes 6+ months
- "We can't launch without [nice-to-have]"
- Features that don't validate core hypothesis
- Enterprise features in v0.1

**Consequences**:
- Never launches
- Builds wrong thing for too long
- Burns runway before validation
- Team exhausted before real feedback

**Remediation**:
1. Define what hypothesis you're testing
2. Minimum = smallest thing to test hypothesis
3. Everything else is v2
4. Set hard deadline and cut ruthlessly

---

## Team Anti-Patterns

### Hero Culture

**What It Looks Like**:
```
Org chart says: 5 engineers
Reality: 1 engineer who matters + 4 others
```

**Red Flags**:
- "Only [person] can fix that"
- One person in every critical meeting
- Others defer instead of learning
- Hero works nights/weekends

**Consequences**:
- Single point of failure (human)
- Hero burns out or leaves
- Others don't grow
- Resentment builds

**Remediation**:
1. Document what hero knows
2. Pair hero with others on critical systems
3. Rotate ownership deliberately
4. Celebrate team wins, not hero saves

---

### Knowledge Silos

**What It Looks Like**:
```
"How does billing work?"
"Ask Sarah"

"How do we deploy?"
"Ask Marcus"

"What's the database schema?"
"That's in Tom's head"
```

**Red Flags**:
- Questions always go to same person
- No documentation for critical systems
- Bus factor of 1
- "Tribal knowledge"

**Consequences**:
- Single points of failure
- Slow onboarding
- Key person leaving is catastrophic
- Bottlenecks on individuals

**Remediation**:
1. Document as you go
2. Rotate on-call and support
3. Pair programming on critical systems
4. Record architecture decisions

---

### Understaffed Ambition

**What It Looks Like**:
```
Plan: "Build the platform"
Team: 2 engineers
Timeline: "Q3"
Reality: Needs 8 engineers for 18 months
```

**Red Flags**:
- "Small but mighty team"
- Comparing to well-funded competitors
- Plans assume 100% productivity
- "We'll hire as we grow"

**Consequences**:
- Burnout guaranteed
- Corners cut everywhere
- Technical debt explosion
- Missed deadlines

**Remediation**:
1. Right-size scope to team
2. Sequence instead of parallelize
3. Have hiring complete before plan starts
4. Build less, but build it well

---

## Process Anti-Patterns

### Cargo Cult Agile

**What It Looks Like**:
```
Has: Daily standups, sprints, story points
Missing: Working software, customer feedback, adaptation
```

**Red Flags**:
- Ceremonies without outcomes
- Sprint planning but no sprint goals
- Retrospectives with no changes
- Story points without velocity tracking

**Consequences**:
- Process overhead without benefits
- Team cynicism about "agile"
- Predictability still poor
- Customer needs ignored

**Remediation**:
1. Start with outcomes, not ceremonies
2. Measure working software delivered
3. Actually change based on retros
4. Talk to customers regularly

---

### Analysis Paralysis

**What It Looks Like**:
```
Month 1: Requirements gathering
Month 2: Requirements review
Month 3: Architecture discussions
Month 4: More requirements
Month 5: "We need more stakeholder input"
Month 6: Still no code
```

**Red Flags**:
- Requirements doc over 50 pages
- Multiple architecture reviews
- "We need to think about this more"
- Perfect is enemy of good

**Consequences**:
- Nothing ships
- Market moves on
- Team loses momentum
- Stakeholders lose confidence

**Remediation**:
1. Set hard deadline for first delivery
2. Limit planning phase explicitly
3. Accept iteration beats perfection
4. Build to learn, not learn to build

---

## Technology Anti-Patterns

### Shiny Object Syndrome

**What It Looks Like**:
```
2023: "We should use [Framework X]"
2024: "We should use [Framework Y]"
2025: "We should use [Framework Z]"
(Original project still on Framework W)
```

**Red Flags**:
- New tech proposed every quarter
- "This would solve our problems"
- Grass is greener mentality
- Ignoring switching costs

**Consequences**:
- Constant context switching
- Nothing gets deep investment
- Technical debt from half-migrations
- Team churn from instability

**Remediation**:
1. Define adoption criteria upfront
2. Require proof-of-concept before proposal
3. Calculate total cost of switching
4. Commit to choices for defined period

---

### Not Invented Here

**What It Looks Like**:
```
Custom built:
- Logging framework
- Authentication system
- Job queue
- ORM
- Testing framework
- Deployment system
```

**Red Flags**:
- "We can build it better"
- Custom solutions for solved problems
- Maintenance burden ignored
- Team proud of infrastructure

**Consequences**:
- Maintaining commodities instead of differentiators
- Security vulnerabilities from non-expert implementations
- Documentation and support burden
- Hiring harder (custom stack)

**Remediation**:
1. Only build what differentiates
2. Calculate true cost (build + maintain + document + support)
3. Use off-the-shelf for commodities
4. Focus engineering on business value

---

### Vendor Lock-in Denial

**What It Looks Like**:
```
"We can always migrate later"
(3 years later)
"Migration would take 18 months and $2M"
```

**Red Flags**:
- Deep integration with single vendor
- Proprietary APIs used extensively
- No abstraction layer
- Switching costs never calculated

**Consequences**:
- Pricing leverage lost
- Feature roadmap dependency
- Migration costs compound over time
- Vendor changes break everything

**Remediation**:
1. Calculate exit costs before commitment
2. Abstract vendor-specific code
3. Use open standards where possible
4. Maintain backup vendor relationship

---

## Quick Reference Card

### Immediate Red Flags
- [ ] "Only [person] knows..."
- [ ] "If everything goes well..."
- [ ] "We'll figure it out later..."
- [ ] "We need to hire..."
- [ ] "It's just a small addition..."
- [ ] "We can always migrate..."
- [ ] "Let's use [new tech] because..."

### Questions to Ask
1. What happens if the key person leaves?
2. What's this estimate based on?
3. What's the Plan B?
4. What similar things have we done? How long did they take?
5. What's the switching cost?
6. Who owns this?
7. Where is this documented?

### Pattern → Severity Quick Guide

| If you see... | It's probably... | Severity |
|---------------|------------------|----------|
| Single point of human failure | Hero Culture | Critical |
| Optimistic estimate, no buffer | Timeline Fantasy | Critical |
| More services than devs | Premature Microservices | High |
| Custom auth, logging, etc. | Not Invented Here | High |
| MVP with 20+ features | MVP Maximalism | High |
| "Agile" but nothing ships | Cargo Cult Agile | Medium |
| Latest framework every year | Shiny Object Syndrome | Medium |
