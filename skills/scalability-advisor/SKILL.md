---
name: scalability-advisor
description: Guidance for scaling systems from startup to enterprise scale. Use when planning for growth, diagnosing bottlenecks, or designing systems that need to handle 10x-1000x current load.
---

# Scalability Advisor

Provides systematic guidance for scaling systems at different growth stages, identifying bottlenecks, and designing for horizontal scalability.

## When to Use

- Planning for 10x, 100x, or 1000x growth
- Diagnosing current performance bottlenecks
- Designing new systems for scale
- Evaluating scaling strategies (vertical vs. horizontal)
- Capacity planning and infrastructure sizing

## Scaling Stages Framework

### Stage Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SCALING JOURNEY                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Stage 1        Stage 2         Stage 3         Stage 4             │
│  Startup        Growth          Scale           Enterprise          │
│  0-10K users    10K-100K        100K-1M         1M+ users           │
│                                                                     │
│  Single         Add caching,    Horizontal      Global,             │
│  server         read replicas   scaling         multi-region        │
│                                                                     │
│  $100/mo        $1K/mo          $10K/mo         $100K+/mo           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Stage 1: Startup (0-10K Users)

### Architecture

```
┌────────────────────────────────────────┐
│           Single Server                │
│  ┌──────────────────────────────────┐  │
│  │  App Server (Node/Python/etc)    │  │
│  │  + Database (PostgreSQL)         │  │
│  │  + File Storage (local/S3)       │  │
│  └──────────────────────────────────┘  │
└────────────────────────────────────────┘
```

### Key Metrics

| Metric | Target | Warning |
|--------|--------|---------|
| Response time (P95) | < 500ms | > 1s |
| Database queries/request | < 10 | > 20 |
| Server CPU | < 70% | > 85% |
| Database connections | < 50% pool | > 80% pool |

### What to Focus On

**DO**:
- Write clean, maintainable code
- Use database indexes on frequently queried columns
- Implement basic monitoring (uptime, errors)
- Keep architecture simple (monolith is fine)

**DON'T**:
- Over-engineer for scale you don't have
- Add caching before you need it
- Split into microservices prematurely
- Worry about multi-region yet

### When to Move to Stage 2

- Database CPU consistently > 70%
- Response times degrading
- Single queries taking > 100ms
- Server resources maxed

---

## Stage 2: Growth (10K-100K Users)

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│    ┌─────────┐      ┌─────────────────────────────────┐     │
│    │   CDN   │      │      Load Balancer              │     │
│    └────┬────┘      └──────────────┬──────────────────┘     │
│         │                          │                        │
│         │           ┌──────────────┼──────────────┐         │
│         │           │              │              │         │
│         ▼           ▼              ▼              ▼         │
│    ┌─────────┐ ┌─────────┐   ┌─────────┐   ┌─────────┐      │
│    │ Static  │ │ App 1   │   │ App 2   │   │ App 3   │      │
│    │ Assets  │ └────┬────┘   └────┬────┘   └────┬────┘      │
│    └─────────┘      │             │             │           │
│                     └──────────────┼────────────┘           │
│                                    │                        │
│                     ┌──────────────┼──────────────┐         │
│                     │              │              │         │
│                     ▼              ▼              ▼         │
│               ┌─────────┐   ┌─────────┐   ┌─────────┐       │
│               │ Primary │   │  Read   │   │  Redis  │       │
│               │   DB    │───│ Replica │   │  Cache  │       │
│               └─────────┘   └─────────┘   └─────────┘       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Key Additions

| Component | Purpose | When to Add |
|-----------|---------|-------------|
| **CDN** | Static asset caching | Images, JS, CSS taking > 20% bandwidth |
| **Load Balancer** | Distribute traffic | Single server CPU > 70% |
| **Read Replicas** | Offload reads | > 80% database ops are reads |
| **Redis Cache** | Application caching | Same queries repeated frequently |
| **Job Queue** | Async processing | Background tasks blocking requests |

### Caching Strategy

```
Request Flow with Caching:

1. Check CDN (static assets)         ─► HIT: Return cached
                                           │
2. Check Application Cache (Redis)   ─► HIT: Return cached
                                           │
3. Check Database                    ─► Return + Cache result
```

**What to Cache**:
- Session data (TTL: session duration)
- User profile data (TTL: 5-15 minutes)
- API responses (TTL: varies by freshness needs)
- Database query results (TTL: 1-5 minutes)
- Computed values (TTL: based on computation cost)

### Database Optimization

```sql
-- Find slow queries
SELECT query, calls, mean_time, total_time
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 20;

-- Find missing indexes
SELECT schemaname, tablename, indexrelname, idx_scan, seq_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0 AND seq_scan > 1000;
```

### When to Move to Stage 3

- Write traffic overwhelming single primary
- Cache hit rate plateauing despite optimization
- Read replicas can't keep up with replication lag
- Need independent scaling of components

---

## Stage 3: Scale (100K-1M Users)

### Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                           CDN / Edge                                 │
└──────────────────────────────────────────────────────────────────────┘
                                    │
┌──────────────────────────────────────────────────────────────────────┐
│                        API Gateway                                   │
│              (Rate limiting, Auth, Routing)                          │
└──────────────────────────────────────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│   Service A   │          │   Service B   │          │   Service C   │
│   (Users)     │          │   (Orders)    │          │   (Search)    │
│   Auto-scale  │          │   Auto-scale  │          │   Auto-scale  │
└───────┬───────┘          └───────┬───────┘          └───────┬───────┘
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│   User DB     │          │   Order DB    │          │ Elasticsearch │
│   (Sharded)   │          │   (Sharded)   │          │   (Cluster)   │
└───────────────┘          └───────────────┘          └───────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────┐
                    │     Message Queue         │
                    │     (Kafka / SQS)         │
                    └───────────────────────────┘
```

### Key Patterns

#### Database Sharding

```
Sharding Strategies:

1. Hash-based (user_id % num_shards)
   PRO: Even distribution
   CON: Hard to add shards

2. Range-based (user_id 1-1M → shard 1)
   PRO: Easy to add shards
   CON: Hotspots possible

3. Directory-based (lookup table)
   PRO: Flexible
   CON: Lookup overhead
```

#### Event-Driven Architecture

```
Synchronous → Asynchronous

Before:
  API → Service A → Service B → Service C → Response (slow)

After:
  API → Service A → Queue → Response (fast)
                      ↓
              Service B, C process async
```

### Scaling Checklist

- [ ] Stateless application servers (no local state)
- [ ] Database read/write separation
- [ ] Asynchronous processing for non-critical paths
- [ ] Circuit breakers between services
- [ ] Distributed tracing implemented
- [ ] Auto-scaling configured with proper metrics
- [ ] Database connection pooling (PgBouncer, ProxySQL)

### When to Move to Stage 4

- Need geographic distribution for latency
- Regulatory requirements (data residency)
- Single region can't handle failover
- Global user base with latency requirements

---

## Stage 4: Enterprise (1M+ Users)

### Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          Global Load Balancer                           │
│                       (GeoDNS, Anycast, Route53)                        │
└─────────────────────────────────────────────────────────────────────────┘
                    │                                │
           ┌────────┴────────┐              ┌───────┴────────┐
           │                 │              │                │
           ▼                 ▼              ▼                ▼
    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │  US-East     │  │  US-West     │  │  EU-West     │  │  AP-South    │
    │  Region      │  │  Region      │  │  Region      │  │  Region      │
    │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │
    │  │Services│  │  │  │Services│  │  │  │Services│  │  │  │Services│  │
    │  └────────┘  │  │  └────────┘  │  │  └────────┘  │  │  └────────┘  │
    │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │
    │  │Database│  │  │  │Database│  │  │  │Database│  │  │  │Database│  │
    │  │(Primary)│ │  │  │(Replica)│ │  │  │(Primary)│ │  │  │(Replica)│ │
    │  └────────┘  │  │  └────────┘  │  │  └────────┘  │  │  └────────┘  │
    └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
                              │                   │
                              └─────────┬─────────┘
                                        │
                              Cross-Region Replication
```

### Multi-Region Patterns

| Pattern | Consistency | Latency | Complexity |
|---------|-------------|---------|------------|
| **Active-Passive** | Strong | High failover | Low |
| **Active-Active** | Eventual | Low | High |
| **Follow-the-Sun** | Strong per region | Medium | Medium |

### Data Consistency Strategies

```
CAP Theorem Trade-offs:

Strong Consistency (CP):
- All regions see same data
- Higher latency for writes
- Use for: Financial transactions, inventory

Eventual Consistency (AP):
- Regions may have stale data briefly
- Low latency always
- Use for: Social feeds, analytics, non-critical

Causal Consistency:
- Related operations ordered correctly
- Balance of latency and correctness
- Use for: Messaging, collaboration
```

### Enterprise Checklist

- [ ] Multi-region deployment
- [ ] Cross-region data replication
- [ ] Global CDN with edge caching
- [ ] Disaster recovery tested
- [ ] Compliance (SOC 2, GDPR, data residency)
- [ ] 99.99% SLA architecture
- [ ] Zero-downtime deployments
- [ ] Chaos engineering practice

---

## Bottleneck Diagnosis Guide

### Finding the Bottleneck

```
Systematic Diagnosis:

1. Where is time spent?
   └─► Distributed tracing (Jaeger, Datadog)

2. Is it the database?
   └─► Check slow query logs, connection pool

3. Is it the application?
   └─► CPU profiling, memory analysis

4. Is it the network?
   └─► Latency between services, DNS resolution

5. Is it external services?
   └─► Third-party API latency, rate limits
```

### Common Bottlenecks by Layer

| Layer | Symptoms | Solutions |
|-------|----------|-----------|
| **Database** | Slow queries, high CPU | Indexing, read replicas, caching |
| **Application** | High CPU, memory | Optimize code, scale horizontally |
| **Network** | High latency, timeouts | CDN, edge caching, connection pooling |
| **Storage** | Slow I/O, high wait | SSD, object storage, caching |
| **External APIs** | Timeouts, rate limits | Circuit breakers, caching, fallbacks |

### Database Bottleneck Checklist

```markdown
## Quick Database Health Check

1. Connection Pool
   - Current connections vs max?
   - Connection wait time?
   - Pool exhaustion events?

2. Query Performance
   - Slowest queries (pg_stat_statements)?
   - Missing indexes (seq scans > 10K)?
   - Lock contention?

3. Replication
   - Replica lag?
   - Write throughput?
   - Read distribution?

4. Storage
   - Disk I/O wait?
   - Table/index bloat?
   - WAL write latency?
```

---

## Scaling Calculations

### Capacity Planning Formula

```
Required Capacity = Peak Traffic × Growth Factor × Safety Margin

Example:
- Current peak: 1,000 req/sec
- Expected growth: 3x in 12 months
- Safety margin: 1.5x

Required: 1,000 × 3 × 1.5 = 4,500 req/sec capacity
```

### Database Sizing

```
Connection Pool Size:
  connections = (num_cores × 2) + effective_spindle_count

  Example: 8 cores, SSD
  connections = (8 × 2) + 1 = 17 connections per instance

Read Replica Sizing:
  replicas = ceiling(read_traffic / single_replica_capacity)

  Example: 10,000 reads/sec, 3,000/replica capacity
  replicas = ceiling(10,000 / 3,000) = 4 replicas
```

### Cache Sizing

```
Cache Size:
  memory = working_set_size × (1 + overhead_factor)

  Working set = frequently accessed data (usually 10-20% of total)
  Overhead = ~1.5x for Redis data structures

  Example: 10GB working set
  Redis memory = 10GB × 1.5 = 15GB
```

---

## Quick Reference

### Scaling Decision Matrix

| Symptom | First Try | Then Try | Finally |
|---------|-----------|----------|---------|
| Slow page loads | Add caching | CDN | Edge compute |
| Database slow | Add indexes | Read replicas | Sharding |
| API timeouts | Async processing | Circuit breakers | Event-driven |
| High server CPU | Vertical scale | Horizontal scale | Optimize code |
| High memory | Increase RAM | Fix memory leaks | Redesign data structures |

### Infrastructure Cost at Scale

| Users | Architecture | Monthly Cost |
|-------|-------------|--------------|
| 10K | Single server | $100-300 |
| 100K | Load balanced + cache | $1,000-3,000 |
| 1M | Microservices + sharding | $10,000-30,000 |
| 10M | Multi-region | $100,000+ |

---

## References

- [Bottleneck Diagnosis Guide](bottleneck-diagnosis.md) - Detailed troubleshooting
- [Capacity Planning Calculator](capacity-calculator.md) - Sizing formulas
