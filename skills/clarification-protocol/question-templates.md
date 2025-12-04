# Question Templates

Ready-to-use question templates organized by category.

## Scope Questions

### For Vague Features

```
When you say "[vague term]", I want to make sure I understand the scope:

**Question**: Are you looking for [Option A] or [Option B]?

**Context**: [Option A] typically involves [scope/effort], while [Option B] is [different scope/effort].
```

### For "AI/ML" Requests

```
"AI" covers a lot of ground. Let me narrow this down:

**Question**: What specific task should the AI perform?
- **Classification**: Sorting items into categories (spam detection, sentiment)
- **Recommendation**: Suggesting items to users (products, content)
- **Generation**: Creating new content (text, images, summaries)
- **Prediction**: Forecasting outcomes (churn, demand, pricing)

**Follow-up**: What training data do you have available?
```

### For "Modern/Updated" Requests

```
"Modern" means different things in different contexts:

**Question**: What specifically feels outdated about the current system?
- UI/UX feels dated?
- Technology stack is hard to maintain?
- Performance doesn't meet current needs?
- Missing features competitors have?

**This helps me focus on what actually needs to change vs. what's working fine.**
```

## Scale Questions

### For Unknown User Scale

```
Scale requirements drive architecture decisions:

**Question**: What's your user base like?
- **Today**: Approximately how many [users/requests/transactions]?
- **12 months**: What's a realistic target (not aspirational)?
- **Peak vs Average**: Is traffic spiky (events, campaigns) or steady?

**Example**: "We have 5K monthly users today, hoping for 50K in 12 months, with 10x spikes during sales events."
```

### For Data Scale

```
Data volume affects storage, processing, and cost:

**Question**: How much data are we dealing with?
- **Volume**: How much data per day/month? (GB, TB?)
- **Velocity**: How fast does it come in? (batch vs. streaming)
- **Variety**: What formats? (structured, unstructured, mixed)

**This determines whether we need a simple database or a data platform.**
```

### For Performance Requirements

```
"Fast" means different things in different contexts:

**Question**: What performance is acceptable?
- **Response time**: What's the max acceptable latency? (100ms? 1s? 10s?)
- **Throughput**: How many requests per second at peak?
- **Availability**: What uptime is required? (99%? 99.9%? 99.99%?)

**Example**: "API responses under 200ms, handling 1000 req/s, 99.9% uptime."
```

## Timeline Questions

### For Vague Deadlines

```
Understanding timeline helps me recommend the right scope:

**Question**: What's driving the timeline?
- **Hard deadline**: Is there an event, launch, or commitment we must hit?
- **Soft deadline**: Is this a target that has some flexibility?
- **No deadline**: Is this "when it's ready" work?

**Follow-up**: If we can't hit the timeline with full scope, what can be cut or phased?
```

### For "ASAP" Requests

```
"ASAP" usually means there's a business driver:

**Question**: What's creating the urgency?
- Customer commitment?
- Competitive pressure?
- Technical issue causing pain?
- Internal goal/OKR?

**Understanding the "why" helps me prioritize what actually needs to be fast vs. what just feels urgent.**
```

## Constraint Questions

### For Unknown Budget

```
Budget affects build vs. buy decisions and infrastructure choices:

**Question**: What's the budget range for this initiative?
- **< $5K/month**: Optimize for cost, use managed services
- **$5K-$50K/month**: Balance features and cost
- **$50K+/month**: Can invest in performance and scalability

**This isn't about cutting corners—it's about not over-engineering.**
```

### For Unknown Team

```
Team capacity shapes what's realistic:

**Question**: Who will build and maintain this?
- **Team size**: How many engineers available?
- **Skills**: What's the team's expertise? (languages, frameworks, cloud)
- **Availability**: Is this the team's focus or a side project?

**Example**: "3 senior engineers, strong in Python/React, 50% dedicated."
```

### For Unknown Constraints

```
Hidden constraints cause projects to fail:

**Question**: Are there any constraints I should know about?
- **Technical**: Must integrate with specific systems? Technology mandates?
- **Compliance**: HIPAA, GDPR, SOC2, industry regulations?
- **Political**: Stakeholders who must approve? Past decisions we can't change?
- **Timeline**: Competing priorities? Upcoming events?

**Better to surface these now than discover them mid-project.**
```

## Success Questions

### For Unclear Goals

```
Without clear success criteria, we can't measure progress:

**Question**: How will we know this succeeded?
- **Metric**: What specific number will change?
- **Target**: What value makes this a success?
- **Timeline**: By when should we see results?

**Example**: "Reduce page load time from 5s to < 2s within 3 months."
```

### For Business Impact

```
Understanding business impact helps prioritize:

**Question**: What business outcome does this enable?
- Revenue impact?
- Cost reduction?
- User satisfaction?
- Competitive advantage?

**This helps me understand how much complexity is justified.**
```

## Context Questions

### For Unknown Current State

```
Knowing where you are helps me design where you're going:

**Question**: What's the current state?
- **Architecture**: What does the system look like today?
- **Pain points**: What's broken or frustrating?
- **Strengths**: What's working well that we should preserve?

**Share any diagrams, docs, or code pointers that help me understand.**
```

### For Migration/Upgrade Requests

```
Migrations need careful planning:

**Question**: What's driving the migration?
- **End of life**: Current system being deprecated?
- **Cost**: Current solution too expensive?
- **Features**: Need capabilities current system doesn't have?
- **Performance**: Current system can't keep up?

**Follow-up**: What's the acceptable downtime or transition period?
```
