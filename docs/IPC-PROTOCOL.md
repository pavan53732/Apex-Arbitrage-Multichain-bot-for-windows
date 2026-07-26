# IPC Protocol

## Purpose
Defines the application IPC contract between desktop UI and backend services.

## Transport
- Must define a Windows-friendly transport such as named pipes or equivalent brokered IPC.
- Must define message envelopes, correlation IDs, and versioning.

## Contract
- Every message needs a producer, consumer, type, and payload schema.
- Messages must define error response behavior and compatibility rules.

## Required details
- Define Windows transport, schema, and version compatibility.
