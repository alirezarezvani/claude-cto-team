---
name: tech-stack-recommender
description: Recommend technology stacks based on project requirements, team expertise, and constraints. Use when selecting frameworks, languages, databases, and infrastructure for new projects.
---

# Tech Stack Recommender

Provides structured recommendations for technology stack selection based on project requirements, team constraints, and business goals.

## When to Use

- Starting a new project and need stack recommendations
- Evaluating technology options for specific use cases
- Comparing frameworks or languages for a project
- Assessing team readiness for a technology choice
- Planning technology migrations

## Stack Selection Framework

### Decision Inputs

```
┌───────────────────────────────────────────────────────────────────┐
│                    STACK SELECTION INPUTS                         │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Project Requirements     Team Factors        Business Constraints│
│  ────────────────────     ────────────        ──────────────────  │
│  • Scale expectations     • Current skills    • Time to market    │
│  • Performance needs      • Learning capacity • Budget            │
│  • Integration points     • Team size         • Hiring market     │
│  • Compliance/Security    • Experience level  • Long-term support │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │ RECOMMENDATION  │
                    │   Framework     │
                    └─────────────────┘
```

---

## Quick Stack Recommendations

### By Project Type

| Project Type | Frontend | Backend | Database | Why |
|--------------|----------|---------|----------|-----|
| **SaaS MVP** | Next.js | Node.js/Express | PostgreSQL | Fast iteration, full-stack JS |
| **E-commerce** | Next.js | Node.js or Python | PostgreSQL + Redis | SEO, caching, transactions |
| **Mobile App** | React Native | Node.js/Python | PostgreSQL | Cross-platform, shared logic |
| **Real-time App** | React | Node.js + WebSocket | PostgreSQL + Redis | Event-driven, low latency |
| **Data Platform** | React | Python/FastAPI | PostgreSQL + ClickHouse | Data processing, analytics |
| **Enterprise** | React | Java/Spring or .NET | PostgreSQL/Oracle | Stability, enterprise support |
| **ML Product** | React | Python/FastAPI | PostgreSQL + Vector DB | ML ecosystem, inference |

### By Team Profile

| Team Profile | Recommended Stack | Avoid |
|--------------|-------------------|-------|
| **Full-stack JS** | Next.js, Node.js, PostgreSQL | Go, Rust (learning curve) |
| **Python Background** | FastAPI, React, PostgreSQL | Heavy frontend frameworks |
| **Enterprise Java** | Spring Boot, React, PostgreSQL | Bleeding-edge tech |
| **Startup (Speed)** | Next.js, Supabase/Firebase | Complex microservices |
| **Scale-Up** | React, Go/Node, PostgreSQL | Monolithic frameworks |

---

## Technology Comparison Tables

### Frontend Frameworks

| Framework | Best For | Learning Curve | Ecosystem | Hiring |
|-----------|----------|----------------|-----------|--------|
| **React** | Complex UIs, SPAs | Medium | Excellent | Easy |
| **Next.js** | Full-stack, SSR, SEO | Medium | Excellent | Easy |
| **Vue.js** | Simpler apps, gradual adoption | Easy | Good | Medium |
| **Svelte** | Performance-critical | Easy | Growing | Hard |
| **Angular** | Enterprise, large teams | Hard | Good | Medium |

#### React vs Vue vs Angular

```
                Speed to MVP    Long-term Maint    Enterprise Ready
React           ████████░░      ████████░░         █████████░
Vue             █████████░      ███████░░          ██████░░░░
Angular         ██████░░░░      █████████░         ██████████
```

### Backend Frameworks

| Framework | Language | Best For | Performance | Ecosystem |
|-----------|----------|----------|-------------|-----------|
| **Express** | Node.js | APIs, real-time | Good | Excellent |
| **Fastify** | Node.js | High-performance APIs | Excellent | Good |
| **FastAPI** | Python | ML APIs, async | Excellent | Good |
| **Django** | Python | Full-featured apps | Good | Excellent |
| **Spring Boot** | Java | Enterprise | Good | Excellent |
| **Go (Gin/Echo)** | Go | High performance | Excellent | Good |
| **Rails** | Ruby | Rapid prototyping | Moderate | Good |
| **NestJS** | TypeScript | Structured Node apps | Good | Good |

#### When to Use What

```markdown
## Node.js (Express/Fastify/NestJS)
✅ Real-time applications (WebSocket)
✅ I/O-heavy workloads
✅ Full-stack JavaScript teams
✅ Microservices
❌ CPU-intensive tasks
❌ Heavy computation

## Python (FastAPI/Django)
✅ ML/Data Science integration
✅ Rapid prototyping
✅ Data processing pipelines
✅ Scientific computing
❌ High-concurrency I/O
❌ Real-time systems

## Go
✅ High-performance services
✅ System programming
✅ Concurrent workloads
✅ Microservices at scale
❌ Rapid prototyping
❌ Complex ORM needs

## Java (Spring Boot)
✅ Enterprise applications
✅ Complex business logic
✅ Transaction-heavy systems
✅ Large teams
❌ Quick MVPs
❌ Small projects
```

### Databases

| Database | Type | Best For | Scale | Complexity |
|----------|------|----------|-------|------------|
| **PostgreSQL** | Relational | General purpose, ACID | High | Medium |
| **MySQL** | Relational | Web apps, read-heavy | High | Low |
| **MongoDB** | Document | Flexible schemas, JSON | High | Low |
| **Redis** | Key-Value | Caching, sessions | Very High | Low |
| **Elasticsearch** | Search | Full-text search | High | Medium |
| **ClickHouse** | Columnar | Analytics, time-series | Very High | Medium |
| **DynamoDB** | Key-Value | Serverless, AWS | Very High | Medium |
| **Cassandra** | Wide-column | Write-heavy, distributed | Very High | High |

#### Database Selection Guide

```
Need ACID transactions?
├── YES → PostgreSQL
│
└── NO → What's your primary use case?
    ├── General purpose → PostgreSQL (still!)
    ├── Document storage → MongoDB
    ├── Caching → Redis
    ├── Search → Elasticsearch
    ├── Analytics → ClickHouse/BigQuery
    ├── Time-series → TimescaleDB/InfluxDB
    └── Key-value at scale → DynamoDB/Cassandra
```

### Infrastructure

| Platform | Best For | Complexity | Cost |
|----------|----------|------------|------|
| **Vercel** | Next.js, frontend | Very Low | $ - $$ |
| **Railway** | Simple deployments | Low | $ - $$ |
| **Render** | General apps | Low | $ - $$ |
| **AWS** | Everything, scale | High | $ - $$$$ |
| **GCP** | ML/Data, Kubernetes | High | $ - $$$$ |
| **Azure** | Enterprise, .NET | High | $ - $$$$ |
| **DigitalOcean** | Simple, affordable | Low | $ |
| **Fly.io** | Edge, global | Medium | $ - $$ |

---

## Stack Templates

### Template 1: Modern SaaS Startup

```
┌──────────────────────────────────────────────────────────────────┐
│                     MODERN SAAS STACK                            │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  FRONTEND          BACKEND            DATABASE                   │
│  ─────────         ───────            ────────                   │
│  Next.js 14        Node.js/Express    PostgreSQL                 │
│  TypeScript        TypeScript         Prisma ORM                 │
│  Tailwind CSS      REST/GraphQL       Redis (cache)              │
│                                                                  │
│  INFRASTRUCTURE    AUTH               PAYMENTS                   │
│  ──────────────    ────               ────────                   │
│  Vercel            Clerk/Auth0        Stripe                     │
│  AWS S3            NextAuth           Stripe Billing             │
│  Cloudflare CDN                                                  │
│                                                                  │
│  MONITORING        CI/CD              ANALYTICS                  │
│  ──────────        ─────              ─────────                  │
│  Sentry            GitHub Actions     PostHog/Amplitude          │
│  Datadog           Vercel Preview     Mixpanel                   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

Best for: B2B SaaS, 0-1M users
Team size: 2-10 engineers
Time to MVP: 4-8 weeks
```

### Template 2: E-Commerce Platform

```
┌──────────────────────────────────────────────────────────────────┐
│                   E-COMMERCE STACK                               │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  FRONTEND          BACKEND            DATABASE                   │
│  ─────────         ───────            ────────                   │
│  Next.js (SSR)     Node.js/Python     PostgreSQL                 │
│  TypeScript        GraphQL/REST       Redis                      │
│  Tailwind/Styled   Medusa/Custom      Elasticsearch              │
│                                                                  │
│  PAYMENTS          SHIPPING           INVENTORY                  │
│  ────────          ────────           ─────────                  │
│  Stripe            ShipStation        Custom/ERP                 │
│  PayPal            EasyPost           Webhook sync               │
│                                                                  │
│  CDN               SEARCH             QUEUE                      │
│  ───               ──────             ─────                      │
│  CloudFront        Algolia/Elastic    SQS/BullMQ                 │
│  Cloudflare        Typesense          Redis                      │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

Best for: D2C, Marketplace
Team size: 5-20 engineers
Time to MVP: 8-16 weeks
```

### Template 3: ML-Powered Product

```
┌──────────────────────────────────────────────────────────────────┐
│                    ML PRODUCT STACK                              │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  FRONTEND          API                ML SERVING                 │
│  ─────────         ───                ──────────                 │
│  React/Next.js     FastAPI            TorchServe/Triton          │
│  TypeScript        Python             Docker/K8s                 │
│                    Pydantic           ONNX Runtime               │
│                                                                  │
│  DATABASE          VECTOR DB          FEATURE STORE              │
│  ────────          ─────────          ─────────────              │
│  PostgreSQL        Pinecone           Feast                      │
│  Redis             Weaviate           Redis                      │
│                    pgvector                                      │
│                                                                  │
│  ML OPS            TRAINING           MONITORING                 │
│  ─────             ────────           ──────────                 │
│  MLflow            SageMaker          Weights & Biases           │
│  Airflow           Vertex AI          Prometheus/Grafana         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

Best for: AI products, recommendation systems
Team size: 5-15 engineers + ML team
Time to MVP: 12-24 weeks
```

### Template 4: Real-Time Application

```
┌──────────────────────────────────────────────────────────────────┐
│                   REAL-TIME STACK                                │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  FRONTEND          BACKEND            REAL-TIME                  │
│  ─────────         ───────            ─────────                  │
│  React             Node.js            Socket.io                  │
│  TypeScript        Express/Fastify    WebSocket                  │
│                    TypeScript         Redis Pub/Sub              │
│                                                                  │
│  DATABASE          CACHE              MESSAGE QUEUE              │
│  ────────          ─────              ─────────────              │
│  PostgreSQL        Redis              Redis Streams              │
│  Prisma            In-memory          Kafka (scale)              │
│                                                                  │
│  PRESENCE          STATE SYNC         CONFLICT RESOLUTION        │
│  ────────          ──────────         ───────────────────        │
│  Redis             CRDT/OT            Yjs/Automerge              │
│  Custom            LiveBlocks         Custom                     │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

Best for: Chat, collaboration, gaming
Team size: 5-15 engineers
Time to MVP: 8-16 weeks
```

---

## Technology Trade-off Analysis

### Language Selection Matrix

| Factor | JavaScript/TS | Python | Go | Java | Rust |
|--------|--------------|--------|-----|------|------|
| **Learning Curve** | Low | Low | Medium | Medium | High |
| **Ecosystem** | Excellent | Excellent | Good | Excellent | Growing |
| **Performance** | Good | Moderate | Excellent | Good | Excellent |
| **Hiring Pool** | Large | Large | Medium | Large | Small |
| **Type Safety** | TS: Good | Optional | Excellent | Excellent | Excellent |
| **Memory Safety** | GC | GC | GC | GC | Compile-time |

### Framework Selection Criteria

```markdown
## Evaluation Checklist

1. **Team Expertise** (Weight: 30%)
   - Current skills alignment?
   - Learning curve acceptable?
   - Training resources available?

2. **Project Requirements** (Weight: 30%)
   - Performance requirements met?
   - Feature set complete?
   - Scalability path clear?

3. **Ecosystem** (Weight: 20%)
   - Package availability?
   - Community size?
   - Third-party integrations?

4. **Long-term Viability** (Weight: 20%)
   - Active maintenance?
   - Corporate backing?
   - Future roadmap?
```

---

## Anti-Patterns to Avoid

### Technology Selection Red Flags

| Anti-Pattern | Why It's Bad | Better Approach |
|--------------|--------------|-----------------|
| **Resume-Driven** | Choosing tech for career, not project | Match to requirements |
| **Hype-Driven** | Picking latest without evaluation | Proven over trendy |
| **Comfort-Only** | Only familiar tech even when unsuitable | Evaluate objectively |
| **Over-Engineering** | Complex stack for simple needs | Start simple |
| **Under-Engineering** | Simple tools for complex needs | Plan for growth |

### Common Mistakes

```markdown
❌ "Let's use microservices from day one"
   → Start monolith, extract later

❌ "We need Kubernetes for our 3-person startup"
   → Use managed platforms (Vercel, Railway)

❌ "MongoDB because NoSQL is modern"
   → PostgreSQL handles 95% of use cases better

❌ "GraphQL for everything"
   → REST is simpler for most APIs

❌ "Let's build our own auth"
   → Use Auth0, Clerk, or established solutions
```

---

## Migration Considerations

### When to Consider Migration

| Trigger | Action |
|---------|--------|
| Performance bottlenecks | Profile first, then consider |
| Team expertise mismatch | Train or hire before migrating |
| End of life/support | Plan 6-12 months ahead |
| Scale limitations | Validate limits with benchmarks |
| Security vulnerabilities | Patch if possible, migrate if not |

### Migration Risk Assessment

```
LOW RISK:
- Library/package updates
- Minor version upgrades
- Adding new services

MEDIUM RISK:
- Database version upgrades
- Framework major versions
- New deployment platform

HIGH RISK:
- Language/framework rewrites
- Database technology changes
- Monolith to microservices
```

---

## Quick Reference

### "I'm building a..."

| Project | Recommended Stack |
|---------|-------------------|
| Blog/CMS | Next.js + Headless CMS (Sanity/Contentful) |
| SaaS Dashboard | Next.js + Node.js + PostgreSQL |
| Mobile App | React Native + Node.js + PostgreSQL |
| E-commerce | Next.js + Medusa/Custom + PostgreSQL |
| Real-time Chat | React + Node.js + Socket.io + Redis |
| Data Dashboard | React + Python/FastAPI + PostgreSQL |
| ML Product | React + Python/FastAPI + PostgreSQL + Vector DB |
| API Service | Node.js or Python + PostgreSQL |

### Stack Complexity Levels

| Complexity | Description | Example Stack |
|------------|-------------|---------------|
| **Minimal** | Single deployment, managed services | Vercel + Supabase |
| **Simple** | Separate frontend/backend | Vercel + Railway + PostgreSQL |
| **Standard** | Multiple services, caching | AWS ECS + RDS + Redis |
| **Complex** | Microservices, event-driven | K8s + Multiple DBs + Kafka |

---

## References

- [Framework Comparison](framework-comparison.md) - Detailed feature comparisons
- [Migration Playbooks](migration-playbooks.md) - Step-by-step migration guides
