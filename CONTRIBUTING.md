# Contributing

Thanks for helping keep this list accurate. Corrections are as valuable as additions — a wrong
star count or a dead link costs a reader more than a missing entry does.

## Conflict of interest

**This list is maintained by [Valmera](https://valmera.io), which is itself listed in it** (under
Agentic video editors, with its hosted connector under Video MCP servers). That is a conflict,
so it is stated plainly rather than buried.

The rules that follow from it:

- Valmera follows the same entry format, description length and disclosure rules as every other tool.
- A product may appear once per relevant section when each entry describes a distinct workflow
  or integration. This applies equally to every company; repeating the same pitch does not qualify.
- Affiliation earns no preferred position, bold type or promotional links. Entries are alphabetical.
- Competing tools are listed on identical terms. **Pull requests adding a Valmera competitor are
  welcome and will be reviewed on the same bar as anything else** — being a competitor is not a
  reason for rejection, and it will never be one.
- If you think an entry here reads like marketing, open an issue. Rewriting a puffed-up
  description is a valid PR, including for Valmera's own entry.

## The inclusion bar

An entry must be **a real, usable tool** — something a reader can install, run, or sign up for
today.

Accepted:

- A hosted product with a working sign-up or a public demo.
- A publicly available hosted connector with setup documentation and stated access requirements.
  Label it as hosted; an open licence on its documentation does not make the service open source.
- A repository with code, a README that explains how to run it, and a commit history.
- A model with released weights, or a paper with a public PDF.
- A dataset with a real download or request process.

Rejected:

- Landing pages, waitlists, "coming soon", and closed betas with no public access.
- Repositories presented as runnable implementations without working code. A documentation-only
  repository may support a hosted-service entry, but is not an open-source implementation.
- Products that have shut down. If a widely-listed tool is dead, a PR that says so in a note is
  more useful than one that removes it silently.
- Affiliate or referral links of any kind. Plain canonical URLs only.
- Reposts, mirrors and SEO clones of a tool already listed.

Low star counts are not a reason for rejection — several genuinely useful MCP servers here have
fewer than fifty. Check usability and access requirements, not popularity alone.

## How to propose an entry

1. Check it is not already listed, including under a different name (several tools have rebranded).
2. Open a pull request editing `README.md` directly.
3. Add the entry to the correct section, **in alphabetical order** within that section.
4. Use the standard format:

   ```markdown
   - [Name](https://example.com) - What it does, in one sentence under 140 characters. *(marker)*
   ```

   - Sentence case. End the description with a period.
   - Say what the tool *does*, not how good it is. No "powerful", "revolutionary", "best-in-class".
   - Markers, where useful: licence and star count for repositories
     (`*(MIT · 4.7k★)*`), or `*(hosted)*` / `*(hosted · free tier)*` / `*(paid)*` for products.
     Add `· last commit YYYY-MM` when a repo has been quiet for over a year.

5. In the PR description, include:
   - a link that proves the tool works (docs, a demo, a release, or the repo);
   - for repositories, the output of `curl -s https://api.github.com/repos/OWNER/NAME | grep -E '"(stargazers_count|spdx_id|pushed_at)"'`;
   - a note if you are affiliated with the tool. Affiliation is fine and does not disqualify
     anything — undisclosed affiliation does.

## Picking the right section

The three editing sections are easy to confuse, so:

- **Agentic video editors** — you state a goal in words and an agent plans and performs the edit on
  footage you supply. If a human still has to make every cut, it belongs in AI-assisted.
- **AI-assisted editors** — a human drives a timeline and AI does specific chores.
- **Generative video** — a model creates or transforms visual material from a prompt, reference
  media or both. This includes generative transformations of supplied footage; describe the
  supported task and source limits instead of assuming full-project editing capabilities.

Products may combine these workflows, including generation inside an agentic editor. Classify
a tool by its main use and mention another verified capability in its description; avoid universal
claims that an editing category can never generate media or that generation never accepts sources.

## Removals

Open an issue (or a PR) if a tool has shut down, a repo has been archived, or a link 404s. The
weekly [lychee](https://github.com/lycheeverse/lychee) run catches broken links but cannot catch a
product that still serves a page while no longer working.

## Verification dates

The README records scoped verification dates. When updating entries, state which sources and
claims you checked and when. Distinguish a documentation check from a hands-on product test;
neither establishes a quality ranking. Do not advance the whole directory's date for a partial
update. Re-check any star counts you touch — they change quickly.
