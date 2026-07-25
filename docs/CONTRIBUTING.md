# APEX Contributing Guide

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Audience:** Contributors — code, docs, skills, agents, integrations.

---

## 1. Welcome

Thanks for considering contributing to APEX. This guide covers code, docs,
skills, agents, DEX/chain adapters, and security disclosures.

---

## 2. Code of Conduct

This project follows a standard Code of Conduct:
- Be respectful, professional, and welcoming
- Disagree on ideas, not on people
- No harassment, discrimination, or trolling
- Violations → report to maintainers (see `SECURITY.md` for contact)

---

## 3. Ways to Contribute

You can contribute in many ways, ordered by impact:

1. **Bug reports** — well-written issues save everyone time
2. **Documentation** — typos, clarifications, examples, translations
3. **Skills & Agents** — new built-in capabilities
4. **DEX adapters** — support more exchanges
5. **Chain adapters** — support more networks
6. **Bug fixes** — small, focused PRs are best
7. **Refactors** — only with a clear justification
8. **Features** — propose in an issue first, get sign-off

---

## 4. Getting Started

### 4.1 Fork & Clone
```bash
git clone https://github.com/<your-username>/Apex-Arbitrage-Multichain-bot-for-windows.git
cd Apex-Arbitrage-Multichain-bot-for-windows
```

### 4.2 Install
```bash
npm ci
```

### 4.3 Run Dev Mode
```bash
npm run dev
```
This launches the Electron app with hot reload. The renderer and main process
both watch and rebuild.

### 4.4 Run Tests
```bash
npm test                 # all
npm run test:unit        # unit only
npm run test:integration # integration only
npm run test:contracts   # smart contract tests
```

### 4.5 Lint & Typecheck
```bash
npm run lint
npm run typecheck
```

---

## 5. Branch & Commit Conventions

### 5.1 Branches
- `main` — always deployable, protected
- `feat/<short-desc>` — new feature
- `fix/<short-desc>` — bug fix
- `docs/<short-desc>` — docs only
- `refactor/<short-desc>` — no behavior change
- `chore/<short-desc>` — tooling, deps, etc.

### 5.2 Commits
Use [Conventional Commits](https://www.conventionalcommits.org/):
```
feat(skills): add cross-chain-arb skill with bridge advisor
fix(ai-pipeline): handle 429 with Retry-After header
docs(readme): clarify local vs cloud AI setup
refactor(chains): extract multicall helper
test(dex): add Uniswap V3 quote test
chore(deps): bump electron to 31.7.0
```

### 5.3 Sign-off
Sign off your commits (`git commit -s`) to certify the DCO (Developer
Certificate of Origin). Add a `Signed-off-by:` line to each commit.

---

## 6. Pull Requests

### 6.1 Before Opening
- Search existing PRs and issues
- For new features: open an issue first to discuss
- For large changes: write a design doc (in `docs/proposals/`)
- Run lint, typecheck, tests locally
- Update relevant docs

### 6.2 Opening
- Use the PR template
- Reference the issue it closes (`Closes #123`)
- Add screenshots / recordings for UI changes
- Tag relevant reviewers (CODEOWNERS file)
- Keep PRs focused — one feature/fix per PR

### 6.3 Review
- Respond to feedback constructively
- Don't force-push after review starts (it hides comments)
- Mark conversations as resolved when addressed
- Be patient; reviewers are volunteers

### 6.4 Merging
- Squash-merge by default (keeps history clean)
- Maintainers handle merge; you'll be credited in release notes

---

## 7. Documentation Contributions

Docs are first-class. To contribute:

### 7.1 Format
- Markdown, CommonMark + GFM
- Headers: `#`, `##`, `###` (don't skip levels)
- Code blocks: fenced with language
- Links: relative within `docs/`
- Tables for structured data
- Lists for sequences

### 7.2 Style
- Active voice
- Specific (no "etc.")
- Code examples that actually work
- Screenshots when UI is described
- Every doc has a header block:
  ```markdown
  > **Version:** X.Y.Z | **Last Updated:** YYYY-MM-DD
  > **Scope:** One-sentence description.
  ```

### 7.3 Bumping Versions
When changing a doc, update its version header AND the changelog if it's a
user-visible change. Patch version for typos, minor for content changes.

---

## 8. Adding a Skill

See `SKILLS.md` §12 for the full checklist. Quick summary:

1. Create `packages/skills/src/<skill-id>/`
   - `index.ts` — exports `Skill` class
   - `schema.ts` — Zod schemas for input/output
   - `prompts.ts` — system prompts
   - `README.md` — short skill doc
2. Register in `packages/skills/src/registry.ts`
3. Add docs entry in `docs/SKILLS.md`
4. Add ≥3 tests in `packages/skills/test/<skill-id>.test.ts`
5. Update `CHANGELOG.md`

---

## 9. Adding an Agent

See `AGENTS.md` §8 for the full checklist. Quick summary:

1. Create `packages/agents/src/<agent-id>/`
   - `index.ts` — agent definition
   - `prompts.ts` — system prompt following `AGENTS.md` §5 template
   - `schema.ts` — Zod schemas
   - `tools.ts` — required tool definitions
2. Register in `packages/agents/src/registry.ts`
3. Add docs entry in `docs/AGENTS.md`
4. Add tests
5. Update `CHANGELOG.md`

---

## 10. Adding a DEX Adapter

See `DEX-INTEGRATION.md` for the full guide.

---

## 11. Adding a Chain Adapter

See `CHAIN-INTEGRATION.md` for the full guide.

---

## 12. Reporting Bugs

Use the issue template. Include:
- APEX version
- Windows version
- Steps to reproduce (minimum)
- Expected vs actual
- Logs (sanitize keys/addresses)
- Diagnostics export (no keys)

Search first; close as duplicate if it's been reported.

---

## 13. Security Issues

**Do not file public issues for security vulnerabilities.**

See `SECURITY.md` for responsible disclosure. We aim to acknowledge within
48 hours and patch within 7 days for high-severity issues.

---

## 14. License

By contributing, you agree that your contributions are licensed under the
project's license (see `LICENSE` file).

---

## 15. Recognition

Contributors are listed in:
- `CONTRIBUTORS.md`
- Release notes
- The About dialog (planned v3.1)

---

*Thanks for making APEX better. Every doc fix, every bug report, every PR matters.*
