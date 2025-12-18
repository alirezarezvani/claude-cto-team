# Marketplace Submission Guide

This document tracks the CTO Team plugin's presence across Claude Code marketplaces.

## Current Status

- ✅ **GitHub Installation**: Available at `alirezarezvani/claude-cto-team`
- ✅ **Marketplace File**: `.claude-plugin/marketplace.json` configured
- ⏳ **Community Marketplaces**: Pending submission

## Submission Checklist

### 1. claude-code-plugins-plus (Recommended)
**Repository**: https://github.com/jeremylongshore/claude-code-plugins-plus
**Status**: Not yet submitted

**Steps to submit:**
1. Fork the repository
2. Add entry to their marketplace.json following their schema
3. Submit pull request with:
   - Plugin name: `cto-team`
   - Source: `alirezarezvani/claude-cto-team`
   - Description, keywords, category
4. Reference their CONTRIBUTING.md guidelines

### 2. ccplugins/marketplace
**Repository**: https://github.com/ccplugins/marketplace
**Status**: Not yet submitted

**Steps to submit:**
1. Fork the repository
2. Add plugin entry to their curated list
3. Submit pull request following their quality guidelines

### 3. ananddtyagi/claude-code-marketplace
**Website**: https://claudecodecommands.directory/submit
**Status**: Not yet submitted

**Steps to submit:**
1. Visit submission form
2. Provide plugin details:
   - GitHub URL: https://github.com/alirezarezvani/claude-cto-team
   - Description: Strategic CTO advisory team with specialized agents
   - Category: Productivity / Development Tools
3. Submit for review

### 4. Other Community Marketplaces
- claude-plugins.dev
- claudemarketplaces.com
- claudecodemarketplace.com

## Plugin Metadata

Use this information when submitting:

```json
{
  "name": "cto-team",
  "description": "Strategic CTO advisory team with specialized agents for architecture design, plan validation, and technology decisions",
  "version": "1.0.0",
  "author": "Alireza Rezvani",
  "homepage": "https://github.com/alirezarezvani/claude-cto-team",
  "keywords": ["cto", "architecture", "strategic-planning", "validation", "roadmap", "system-design"],
  "license": "MIT",
  "agents": 3,
  "commands": 4,
  "skills": 12
}
```

## Installation Methods

After marketplace submissions are approved, users can install via:

**Direct GitHub:**
```bash
claude /plugin install alirezarezvani/claude-cto-team
```

**From Marketplace:**
```bash
claude /plugin marketplace add jeremylongshore/claude-code-plugins-plus
claude /plugin install cto-team
```

**From Our Marketplace:**
```bash
claude /plugin marketplace add alirezarezvani/claude-cto-team
```

## Promotion Strategy

1. ✅ GitHub repository with comprehensive README
2. ⏳ Submit to major community marketplaces
3. ⏳ Share on social media (LinkedIn, Twitter/X, Dev.to)
4. ⏳ Write blog post about the CTO Team agents
5. ⏳ Engage with Claude Code community

## Resources

- [Official Plugin Marketplace Docs](https://code.claude.com/docs/en/plugin-marketplaces)
- [Plugin Development Guide](https://www.anthropic.com/news/claude-code-plugins)
- [Community Guidelines](https://github.com/jeremylongshore/claude-code-plugins-plus/blob/main/CONTRIBUTING.md)

---

**Note**: Claude Code uses a decentralized marketplace model. There is no single "official" Anthropic marketplace. Plugin discovery happens through community-curated marketplaces and direct GitHub installations.

Last Updated: December 17, 2025
