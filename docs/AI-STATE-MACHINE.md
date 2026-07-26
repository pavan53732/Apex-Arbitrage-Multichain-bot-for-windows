# AI State Machine

## Document type
Document type: [REFERENCE]

## Purpose
Defines AI orchestration states and transitions.

## State machine
- Draft, Ready, Running, Waiting, Failed, Retrying, Completed.

## Transitions
- Draft -> Ready -> Running -> Completed.
- Running -> Waiting -> Running.
- Running -> Failed -> Retrying -> Running.
- Failed -> Completed is forbidden.

