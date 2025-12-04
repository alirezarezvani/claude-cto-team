# Buzzword Dictionary

Common vague terms that require clarification before proceeding.

## High-Priority Buzzwords (Always Challenge)

### Technology Buzzwords

| Buzzword | Challenge Question | What We Need |
|----------|-------------------|--------------|
| **"AI-powered"** | What specific AI capability? Classification, generation, prediction, recommendation? | Specific ML/AI task and success criteria |
| **"machine learning"** | What are you trying to predict or classify? What training data exists? | Problem type, data availability, accuracy requirements |
| **"real-time"** | What latency is acceptable? < 100ms? < 1s? < 10s? | Specific latency SLA |
| **"scalable"** | Scale from what to what? 1K to 10K users? 10K to 1M? | Current scale, target scale, timeline |
| **"modern"** | What specific technologies? What are you moving away from? | Technology constraints, migration needs |
| **"cloud-native"** | Kubernetes? Serverless? Managed services? Which cloud? | Deployment target, existing infrastructure |
| **"microservices"** | How many services? What boundaries? | Service decomposition strategy |
| **"secure"** | What compliance requirements? What threat model? | Security requirements, compliance (HIPAA, SOC2, GDPR) |

### Scope Buzzwords

| Buzzword | Challenge Question | What We Need |
|----------|-------------------|--------------|
| **"simple"** | Simple for whom? Users? Developers? Ops team? | Complexity constraints, target audience |
| **"basic"** | What features are in scope? What's explicitly out? | Feature list, MVP definition |
| **"just"** | "Just a small change" - what's the blast radius? | Impact assessment |
| **"quick"** | How quick? Hours? Days? Weeks? | Timeline with buffer |
| **"minimal"** | What's the minimum viable feature set? | MVP criteria |
| **"flexible"** | Flexible in what dimension? Extensible? Configurable? | Flexibility requirements |

### Timeline Buzzwords

| Buzzword | Challenge Question | What We Need |
|----------|-------------------|--------------|
| **"soon"** | When exactly? This week? This month? This quarter? | Specific deadline |
| **"fast"** | What's the timeline? What can be cut to hit it? | Deadline + scope flexibility |
| **"ASAP"** | What's driving the urgency? What's the real deadline? | Business driver, actual constraints |
| **"when we have time"** | When will that be? Is this actually prioritized? | Priority ranking, realistic timeline |
| **"eventually"** | Is this actually planned? What triggers it? | Commitment level, trigger conditions |

### Quality Buzzwords

| Buzzword | Challenge Question | What We Need |
|----------|-------------------|--------------|
| **"high-quality"** | What metrics define quality? Test coverage? Performance? | Quality metrics and thresholds |
| **"production-ready"** | What's your production readiness checklist? | Deployment criteria |
| **"enterprise-grade"** | What enterprise requirements? SLA? Compliance? Support? | Enterprise feature list |
| **"robust"** | Robust against what failures? | Failure scenarios, resilience requirements |
| **"reliable"** | What uptime target? 99%? 99.9%? 99.99%? | SLA requirements |

### Business Buzzwords

| Buzzword | Challenge Question | What We Need |
|----------|-------------------|--------------|
| **"leverage"** | Use what specifically? How does it help? | Concrete integration points |
| **"synergy"** | What specific benefit? Cost savings? Feature parity? | Measurable outcome |
| **"optimize"** | Optimize for what? Speed? Cost? Quality? | Optimization target and metric |
| **"streamline"** | What's currently inefficient? What's the target state? | Current pain points, success criteria |
| **"innovative"** | What's novel? What problem does novelty solve? | Innovation justification |

## Medium-Priority Buzzwords (Clarify if Ambiguous)

### Architecture Terms

| Term | When to Clarify |
|------|-----------------|
| **"API"** | REST? GraphQL? gRPC? WebSocket? |
| **"database"** | SQL? NoSQL? What query patterns? |
| **"cache"** | What to cache? TTL requirements? |
| **"queue"** | What message patterns? Ordering requirements? |
| **"service"** | Boundaries? Communication patterns? |

### Team Terms

| Term | When to Clarify |
|------|-----------------|
| **"team"** | How many people? What skills? |
| **"resources"** | People? Budget? Infrastructure? |
| **"capacity"** | Current workload? Availability? |
| **"expertise"** | Specific skills? Learning curve acceptable? |

## Red Flag Combinations

These combinations almost always indicate unclear requirements:

1. **"Simple AI solution"** - AI is rarely simple
2. **"Quick microservices migration"** - Microservices migrations are not quick
3. **"Basic real-time features"** - Real-time adds significant complexity
4. **"Just add machine learning"** - ML requires data, training, monitoring
5. **"Scalable MVP"** - MVP and scalability are often at odds
6. **"Enterprise-grade in 2 weeks"** - Enterprise features take time

## How to Challenge

When you detect a buzzword:

1. **Acknowledge the intent**: "I understand you want [buzzword capability]..."
2. **Ask for specifics**: "To design this effectively, I need to understand..."
3. **Provide options**: "Do you mean [option A] or [option B]?"
4. **Give examples**: "For example, real-time could mean < 100ms for gaming or < 5s for analytics..."

**Example challenge:**

> User: "We need an AI-powered solution"
>
> Challenge: "I want to make sure I design the right AI capability. Are you looking for:
> - **Classification**: Categorizing items (spam detection, sentiment analysis)
> - **Recommendation**: Suggesting items to users (product recommendations)
> - **Generation**: Creating content (text, images)
> - **Prediction**: Forecasting outcomes (churn prediction, demand forecasting)
>
> What specific problem are you trying to solve with AI?"
