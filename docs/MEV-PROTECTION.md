# MEV Protection

## Purpose
Defines MEV avoidance, mitigation, and execution safeguards.

## Ownership
- Owns MEV visibility assessment, protection mode selection, and blocking policy.
- Feeds routing and execution.

## Responsibilities
- Detect high-risk visibility conditions.
- Choose private or protected submission when policy permits.
- Apply sandwich, backrun, and replay safeguards.
- Block submissions when protection policy cannot be satisfied.

## Inputs
- Route fingerprint.
- Venue visibility.
- Mempool exposure.
- Chain conditions.
- Submission mode policy.

## Outputs
- MEV risk label.
- Protection mode.
- Reject reason.
- Submission recommendation.

## Validation
- Reject if policy demands protection and no safe protection path exists.
- Reject if a route cannot be protected under the current chain or venue.

## Persistence
- Persist MEV risk class, selected protection, reject reason, and route fingerprint.

## Monitoring
- Protected submission rate.
- MEV rejection count.
- Visibility risk count.

## Cross-references
- `EXECUTION-ENGINE.md`
- `ROUTING-ENGINE.md`
- `TRANSACTION-LIFECYCLE.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Protection detail
- Must define private relay behavior and simulation checks.

## Required details
- Define private routing and sandbox protections.
