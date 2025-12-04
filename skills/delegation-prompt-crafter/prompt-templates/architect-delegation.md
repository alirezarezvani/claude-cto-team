# Architect Delegation Template

Use this template when delegating design work to **cto-architect**.

## Template

```markdown
## CONTEXT

### Business Goal
[What business outcome does this system/feature enable?]
[How does success here translate to business value?]

### Current State
**Existing Architecture:**
- [Current tech stack]
- [Relevant existing systems]
- [Integration points]

**Pain Points:**
- [What's broken or missing?]
- [Why now?]

**Previous Decisions:**
- [Relevant past decisions that constrain options]

### Key Constraints
- **Budget**: [Infrastructure budget range, development budget if relevant]
- **Timeline**: [Hard deadlines, soft targets, flexibility]
- **Team**: [Size, skills, availability, learning curve tolerance]
- **Technical**: [Must-use technologies, compliance, existing commitments]

### Scale Parameters
- **Current**: [Users, requests/sec, data volume today]
- **Target (12 months)**: [Realistic growth expectations]
- **Peak vs Average**: [Traffic patterns, spiky or steady]

---

## TASK

### Primary Deliverable
Design a comprehensive system architecture for [specific system/feature]

### Format Requirements
Provide the standard 7-section architecture document:
1. **Executive Summary**: Business value, approach, timeline, budget, risks (1-2 pages)
2. **System Architecture**: Component diagram, data flow, integration points, scalability mechanisms
3. **Technology Stack Justification**: Each choice with explicit trade-offs, 10x growth considerations
4. **Implementation Roadmap**: MVP → Scale → Advanced phases with validation checkpoints
5. **Risk Assessment**: Technical debt, bottlenecks, dependencies, team gaps
6. **Code Examples**: API contracts, integration patterns, error handling
7. **Deployment Strategy**: Infrastructure as code, CI/CD, monitoring, DR

### Scope Boundaries
**In Scope:**
- [Specific components to design]
- [Specific decisions to make]

**Out of Scope:**
- [What other agents will handle]
- [What's deferred to future phases]
- [What's already decided]

---

## REQUIREMENTS

### Must-Haves
- [ ] [Critical requirement 1 - solution fails without this]
- [ ] [Critical requirement 2]
- [ ] [Critical requirement 3]

### Nice-to-Haves
- [ ] [Enhancement 1 - can defer if needed]
- [ ] [Enhancement 2]

### Quality Criteria
- **Performance**: [Latency SLA, throughput requirements]
- **Scalability**: [Growth factor, scaling mechanism]
- **Cost**: [Target infrastructure cost at launch and at scale]
- **Reliability**: [Uptime target, failure handling]

### Non-Functional Requirements
- **Security**: [Auth, encryption, compliance requirements]
- **Observability**: [Logging, monitoring, alerting needs]
- **Maintainability**: [Complexity constraints, team capabilities]

---

## INTEGRATION POINTS

### Upstream
- [What triggers this system? What data comes in?]

### Downstream
- [What consumes outputs? What depends on this?]

### Workflow Context
- [What happens after your design is complete?]
- [Will this be validated by strategic-cto-mentor?]
- [Who implements from this design?]

---

## ADDITIONAL CONTEXT

### Relevant Documentation
- [Links to existing docs, ADRs, diagrams]

### Stakeholder Preferences
- [Known preferences or constraints from leadership]

### Previous Attempts
- [What was tried before? Why did it fail?]

### Open Questions
- [Decisions that are still open for architect input]
```

## Example: E-commerce Notification System

```markdown
## CONTEXT

### Business Goal
Enable customers to receive real-time order status notifications, reducing "where's my order" support tickets by 60% and improving customer satisfaction scores.

### Current State
**Existing Architecture:**
- Node.js monolith with Express
- PostgreSQL for orders, users, products
- React web app, React Native mobile apps
- AWS (EC2, RDS, S3)
- Email via SendGrid (batch hourly)

**Pain Points:**
- Customers don't know order status until they check manually
- Support team overwhelmed with status inquiries
- Email notifications are delayed and often ignored

**Previous Decisions:**
- Staying on AWS (no multi-cloud)
- Keeping PostgreSQL as primary database
- Mobile apps must support offline mode

### Key Constraints
- **Budget**: < $3K/month additional infrastructure
- **Timeline**: MVP in 6 weeks (before holiday season)
- **Team**: 2 backend engineers (strong Node.js), 1 mobile dev
- **Technical**: Must use existing auth system, no new databases

### Scale Parameters
- **Current**: 50K users, 10K orders/day, 100 req/sec peak
- **Target (12 months)**: 200K users, 40K orders/day
- **Peak vs Average**: 5x spikes during sales events

---

## TASK

### Primary Deliverable
Design a real-time notification system architecture for order status updates

### Format Requirements
Standard 7-section document with emphasis on:
- WebSocket vs Server-Sent Events decision
- Push notification integration (iOS/Android)
- Failure handling and retry logic
- Cost breakdown at current and target scale

### Scope Boundaries
**In Scope:**
- Real-time push notifications (mobile)
- WebSocket/SSE for web real-time updates
- Notification delivery infrastructure
- Order status event pipeline

**Out of Scope:**
- Marketing notifications (separate project)
- SMS notifications (Phase 2)
- Email system changes (keep existing)

---

## REQUIREMENTS

### Must-Haves
- [ ] Real-time delivery (< 5 sec from status change to notification)
- [ ] Push notifications on iOS and Android
- [ ] Fallback mechanism if push fails
- [ ] Works offline (queue and deliver when back online)

### Nice-to-Haves
- [ ] User notification preferences (per channel)
- [ ] Rich notifications with order images
- [ ] Delivery/read receipts

### Quality Criteria
- **Performance**: p95 < 5 seconds end-to-end
- **Scalability**: Handle 200K users, 40K events/day
- **Cost**: < $3K/month at target scale
- **Reliability**: 99.9% delivery success rate

---

## INTEGRATION POINTS

### Upstream
- Order service emits status change events
- User service provides notification preferences

### Downstream
- Mobile apps consume push notifications
- Web app connects via WebSocket/SSE
- Analytics tracks delivery metrics

### Workflow Context
- Design will be validated by strategic-cto-mentor before implementation
- Backend team implements server-side, mobile team implements client-side
- QA team will need test environment with notification simulation

---

## ADDITIONAL CONTEXT

### Previous Attempts
Firebase was evaluated last year but rejected due to vendor lock-in concerns. Team prefers AWS-native solutions.

### Stakeholder Preferences
VP of Product wants "instant" notifications. CTO wants to avoid complex infrastructure.

### Open Questions
- Should we build notification preferences UI now or defer?
- What's acceptable behavior when user has notifications disabled?
```
