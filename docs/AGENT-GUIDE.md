# Agent Guide

## What a gate is
A gate is a file that tells a coding assistant which documents to read before making changes. It is not a source of behavior by itself.

## What authority means
Authoritative documents define the real contract: ownership, lifecycle, interface, schema, or architecture boundaries. Navigation and index documents only point to those sources.

## How to work safely
- Read the authoritative owner docs for the subsystem you are changing.
- Do not infer behavior from short summary docs.
- Do not expand scope beyond what the owner docs define.
- If a contract is missing or ambiguous, stop and ask for clarification.

## Why this matters
These rules prevent coding agents from inventing behaviors that are not written down. That keeps implementation aligned with the repository’s actual contracts.
