# Contributing

Thanks for helping keep this list accurate. Corrections are as valuable as additions — a wrong
star count or a dead link costs a reader more than a missing entry does.

## Conflict of interest

**This list is maintained by [Valmera](https://valmera.io), which is itself listed in it** (under
Agentic video editors). That is a conflict, so it is stated plainly rather than buried.

The rules that follow from it:

- Valmera gets one entry, in the same format, with the same length, and with its limits stated —
  exactly like every other tool.
- It is not placed first, bolded, given extra links, or repeated in a second section.
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
- A repository with code, a README that explains how to run it, and a commit history.
- A model with released weights, or a paper with a public PDF.
- A dataset with a real download or request process.

Rejected:

- Landing pages, waitlists, "coming soon", and closed betas with no public access.
- Repositories that are a README and nothing else, or a thin wrapper with no working code.
- Products that have shut down. If a widely-listed tool is dead, a PR that says so in a note is
  more useful than one that removes it silently.
- Affiliate or referral links of any kind. Plain canonical URLs only.
- Reposts, mirrors and SEO clones of a tool already listed.

Low star counts are not a reason for rejection — several genuinely useful MCP servers here have
fewer than fifty. An empty repo is.

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
- **Generative video** — the model synthesises new frames. It does not edit your footage, and it
  goes in this section however the marketing describes it.

A tool that does two of these gets one entry, in the section matching what it is mainly used for,
with the other capability mentioned in the description.

## Removals

Open an issue (or a PR) if a tool has shut down, a repo has been archived, or a link 404s. The
weekly [lychee](https://github.com/lycheeverse/lychee) run catches broken links but cannot catch a
product that still serves a page while no longer working.

## Verification dates

The README states the date every entry was last checked. If you make a bulk update, update that
date and re-check the star counts you touched — a star count without a date is a fact with a short
shelf life.
