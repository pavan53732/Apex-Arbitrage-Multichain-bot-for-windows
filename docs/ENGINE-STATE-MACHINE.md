# Engine State Machine

## Document type
Document type: [REFERENCE]

## Purpose
Defines core engine lifecycle states.

## State machine
- Initialising, Ready, Running, Degraded, Recovering, Stopped.

## Transitions
- Initialising -> Ready -> Running.
- Running -> Degraded -> Recovering -> Running.
- Running -> Stopped.

