# Pull Request Submission Guide

## Target: claude-code-plugins-plus Marketplace

This guide will help you submit the CTO Team plugin to the most popular Claude Code community marketplace.

---

## Step 1: Fork and Clone

1. Go to: https://github.com/jeremylongshore/claude-code-plugins-plus
2. Click "Fork" (top right)
3. Clone your fork:
```bash
git clone https://github.com/YOUR-USERNAME/claude-code-plugins-plus.git
cd claude-code-plugins-plus
```

---

## Step 2: Add Plugin Entry to Marketplace

Edit `.claude-plugin/marketplace.extended.json` and add this entry to the `plugins` array:

```json
{
  "name": "cto-team",
  "source": {
    "source": "github",
    "repo": "alirezarezvani/claude-cto-team"
  },
  "description": "Strategic CTO advisory team with specialized agents for architecture design, plan validation, and technology decisions. Includes cto-orchestrator (coordinator), cto-architect (system designer), and strategic-cto-mentor (ruthless validator) with 12 specialized skills.",
  "version": "1.0.0",
  "category": "productivity",
  "keywords": [
    "cto",
    "architecture",
    "strategic-planning",
    "tech-decisions",
    "validation",
    "roadmap",
    "build-vs-buy",
    "system-design",
    "ml-architecture",
    "agents"
  ],
  "author": {
    "name": "Alireza Rezvani",
    "email": "contact@alirezarezvani.com",
    "url": "https://github.com/alirezarezvani"
  },
  "homepage": "https://github.com/alirezarezvani/claude-cto-team",
  "repository": "https://github.com/alirezarezvani/claude-cto-team",
  "license": "MIT",
  "components": {
    "agents": 3,
    "commands": 4,
    "skills": 12,
    "total": 19
  },
  "featured": false
}
```

**Important:** Add this entry alphabetically by plugin name in the plugins array.

---

## Step 3: Sync Marketplace

Run the marketplace sync script to regenerate `marketplace.json`:

```bash
# Install dependencies if needed
pnpm install
# or
npm install

# Sync marketplace
pnpm run sync-marketplace
# or
npm run sync-marketplace
```

---

## Step 4: Commit Changes

```bash
git add .claude-plugin/marketplace.extended.json .claude-plugin/marketplace.json
git commit -m "Add cto-team plugin - Strategic CTO advisory agents"
git push origin main
```

---

## Step 5: Create Pull Request

1. Go to your fork on GitHub
2. Click "Contribute" → "Open pull request"
3. Use this PR title:

```
Add cto-team plugin - Strategic CTO advisory agents
```

4. Use this PR description:

```markdown
## Plugin Submission: cto-team

### Overview
Strategic CTO advisory team with three specialized AI agents that provide:
- Architecture design and system planning
- Ruthless validation of technical decisions
- Technology stack recommendations
- Build vs buy analysis

### Components
- **3 Agents**: cto-orchestrator, cto-architect, strategic-cto-mentor
- **4 Slash Commands**: /validate, /design, /decide, /cto
- **12 Specialized Skills**: Architecture patterns, roadmap generation, cost estimation, validation reports, and more

### Category
Productivity

### Key Features
- 🎯 Strategic technical guidance at CTO level
- 🏗️ Comprehensive system architecture design
- ✅ Ruthless plan validation with 7-dimension framework
- 📊 Technology stack recommendations with trade-off analysis
- 💰 Cost estimation and TCO analysis
- 🗺️ Phased implementation roadmaps

### Plugin Quality Checklist
- [x] Valid `.claude-plugin/plugin.json` with all required fields
- [x] Comprehensive README.md with usage examples
- [x] MIT License included
- [x] All functionality tested locally
- [x] No hardcoded credentials
- [x] Security best practices followed
- [x] Semantic versioning (1.0.0)
- [x] Well-documented with 3 agents, 4 commands, 12 skills

### Repository
https://github.com/alirezarezvani/claude-cto-team

### Installation
```bash
claude /plugin install alirezarezvani/claude-cto-team
```

### Author
Alireza Rezvani ([@alirezarezvani](https://github.com/alirezarezvani))

---

This plugin has been thoroughly tested and follows all contribution guidelines. Ready for review!
```

5. Click "Create pull request"

---

## Step 6: Wait for Review

- **Initial review**: Within 7 days
- **Feedback**: Within 14 days
- **Merge**: 1-3 days after approval

---

## Submission Checklist

- [ ] Forked claude-code-plugins-plus repository
- [ ] Added plugin entry to `.claude-plugin/marketplace.extended.json`
- [ ] Added entry alphabetically by name
- [ ] Ran `pnpm run sync-marketplace` successfully
- [ ] Committed and pushed changes
- [ ] Created pull request with proper title and description
- [ ] Linked to this repository in PR description

---

## Alternative: Manual GitHub PR Creation

If you prefer to do this entirely in the GitHub UI:

1. Fork the repository
2. Navigate to `.claude-plugin/marketplace.extended.json` in your fork
3. Click "Edit" (pencil icon)
4. Add the plugin entry JSON (from Step 2 above) to the plugins array
5. Commit directly to main branch with message: "Add cto-team plugin"
6. Create pull request from your fork

GitHub will automatically offer to create the PR after you commit.

---

## Questions?

If you encounter issues:
- Check their CONTRIBUTING.md: https://github.com/jeremylongshore/claude-code-plugins-plus/blob/main/CONTRIBUTING.md
- Review their example plugins in `plugins/` directory
- Open an issue in their repo if you need help

---

**Last Updated**: December 17, 2025
