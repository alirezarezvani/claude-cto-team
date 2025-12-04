# Challenge Questions by Category

Ready-to-use questions for challenging assumptions in proposals and plans.

## Timeline Assumptions

### Duration Estimates
- What's this estimate based on? Past projects or intuition?
- What similar work has the team done before? How long did it actually take?
- Does this estimate include testing, documentation, and deployment?
- What's the buffer for unexpected issues? (Every project has them)
- If this takes 2x longer, what's the impact on the overall plan?

### Deadline Commitments
- What's driving this deadline? Is it real or arbitrary?
- What happens if we miss this deadline by 2 weeks? 4 weeks?
- Who committed to this timeline and on what basis?
- What scope can be cut if we can't hit the deadline?
- Has the team agreed this timeline is achievable?

### Parallel Work
- You're planning X, Y, and Z in parallel. Do you have the staff for that?
- What happens when these parallel tracks need to integrate?
- Who's the point person for each track? Do they have capacity?
- What's the critical path? What delays everything if it slips?

---

## Resource Assumptions

### Hiring
- What's your time-to-hire for this role? (Industry average is 3-6 months for senior)
- What's your offer acceptance rate? What if candidates decline?
- Where will these candidates come from? Do you have a pipeline?
- What happens to the project if you only fill 50% of planned hires?
- How long until new hires are productive? (Usually 2-3 months)

### Team Capacity
- What's the team's current utilization? Where does time for this come from?
- Is anyone on this team also committed to other projects?
- What happens during vacations, sick days, or turnover?
- Who's the backup if the key technical lead is unavailable?
- Have you accounted for support and maintenance of existing systems?

### Skills
- Does the team have experience with this technology?
- What's the learning curve? Is that factored into the timeline?
- Who's the expert? What if they leave?
- Do you need external help? Is that budgeted?

---

## Technical Assumptions

### Performance
- Has this been tested at the required scale?
- What's the current performance baseline? What's the target?
- What happens when you hit 2x, 5x, 10x the expected load?
- What's the failure mode? Graceful degradation or crash?
- Have you identified the bottleneck? Is it CPU, memory, network, database?

### Integration
- Have you talked to the team that owns this API/service?
- What's the API's documented rate limit? What happens when you hit it?
- Is there a staging environment you can test against?
- What's the API's uptime SLA? What's your fallback when it's down?
- Has anyone on the team done this integration before?

### Architecture
- Does the current architecture support this use case?
- What changes are required to existing systems?
- Have you considered backward compatibility?
- What's the rollback plan if this doesn't work?
- Is this introducing new single points of failure?

### Data
- Do you have the data you need? In the format you need?
- What's the data quality? Have you validated it?
- Are there privacy/compliance implications?
- What's the data volume? Is your system designed for that?
- Who owns this data? Can you use it for this purpose?

---

## Business Assumptions

### User Behavior
- What evidence shows users want this feature?
- Have you talked to actual users? How many?
- What's the expected adoption rate? Based on what?
- What if users don't adopt this? What's the fallback?
- How will you measure success? What's the threshold?

### Market
- What's the competitive landscape? What are others doing?
- What's the time-to-market pressure? What happens if you're late?
- Is the market stable or changing? How will that affect this?
- What's your differentiation? Why will customers choose you?

### Revenue/Cost
- What's the expected ROI? What's that based on?
- What if costs are 2x higher than projected?
- What if revenue is 50% of projected?
- What's the break-even point? When do you expect to hit it?
- What's the opportunity cost of doing this vs. other initiatives?

---

## External Dependencies

### Vendors
- What's the vendor's track record on delivery commitments?
- Do you have a contract? What are the SLAs?
- What's the cost at scale? Is there a ceiling?
- What's the lock-in risk? How hard is it to switch?
- Who's the backup vendor if this one fails?

### Partners
- What's the partner's incentive to deliver on time?
- What do they get from this partnership?
- What's the escalation path if they're slow?
- Have you worked with them before? How did it go?

### Regulatory
- What regulations apply? Are you sure you're compliant?
- What happens if regulations change?
- Have you talked to legal/compliance?
- What's the cost of getting this wrong?

---

## Meta Questions

### Evidence Quality
- What evidence supports this assumption?
- Is this assumption stated explicitly or implied?
- Who made this assumption? What's their expertise?
- When was this last validated? Is it still true?

### Consequence Analysis
- If this assumption is wrong, what's the blast radius?
- Can we continue if this assumption fails?
- What early warning signs would indicate this is wrong?
- What's the cost of validating this assumption now vs. finding out later?

### Alternative Scenarios
- What's the best case? What's the worst case? What's most likely?
- What would have to be true for the worst case to happen?
- What's Plan B if this assumption proves wrong?
- Can we design the project to be less dependent on this assumption?

---

## Challenge Intensity Levels

### Level 1: Gentle Probe
Use when: Initial exploration, building rapport
> "Help me understand the thinking behind this assumption..."
> "What led you to this conclusion?"

### Level 2: Direct Challenge
Use when: Significant concerns, need clarity
> "I'm not seeing evidence for this. What are we basing it on?"
> "This seems optimistic. What's the realistic scenario?"

### Level 3: Stress Test
Use when: High-stakes decisions, pattern of optimism
> "Walk me through the failure scenario. What happens when this is wrong?"
> "I've seen this assumption fail in 3 other projects. What's different here?"

### Level 4: Hard Stop
Use when: Critical flaws, must address before proceeding
> "I can't validate this plan while this assumption is unverified. We need to test this first."
> "This assumption is the foundation of the entire plan. If it's wrong, everything falls apart."

---

## Question Selection Guide

| Situation | Recommended Questions |
|-----------|----------------------|
| First review | Start with evidence quality questions |
| Technical proposal | Focus on technical and performance questions |
| Business case | Focus on market and ROI questions |
| Timeline-driven | Focus on timeline and resource questions |
| External dependencies | Focus on vendor and partner questions |
| High uncertainty | Use meta questions liberally |
