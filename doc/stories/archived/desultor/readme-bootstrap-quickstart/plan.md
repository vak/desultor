---
kind: story
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: local-evidence
tags: [story, docs, readme, bootstrap, quickstart, desultor]
session_signature:
  harness: codex
  model_family: gpt-5
  model_exact: not_exposed_in_session
  reasoning_effort: not_exposed_in_session
session_signature_sources:
  harness:
    source: direct_context
    raw_evidence: "You are Codex, a coding agent based on GPT-5."
  model_family:
    source: direct_context
    raw_evidence: "You are Codex, a coding agent based on GPT-5."
  model_exact:
    source: not_exposed_in_session
    raw_evidence: not_exposed_in_session
  reasoning_effort:
    source: not_exposed_in_session
    raw_evidence: not_exposed_in_session
---
# Plan

## Goal

Make the root `README.md` understandable as a public entrypoint for people who
want to start a brand-new project with Desultor, without turning it into the
host project's own README.

## Plan

1. Add a short quickstart section for brand-new projects near the top of the
   root `README.md`.
2. Make both `Codex-first` and `Claude Code-first` entrypaths explicit.
3. State clearly which files are imported, which project docs must be authored
   immediately, and that the starter's root `README.md` must not become the
   host project's root README.
4. Keep the existing import contract and repository map intact while making the
   public-facing path easier to scan.
