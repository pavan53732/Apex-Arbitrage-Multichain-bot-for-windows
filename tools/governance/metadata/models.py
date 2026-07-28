from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field

class DocumentMetadata(BaseModel):
    path: str
    type: Optional[str] = None
    owner: Optional[str] = None
    status: Optional[str] = None
    version: Optional[str] = None
    purpose: Optional[str] = None
    scope: Optional[str] = None
    responsibilities: list[str] = Field(default_factory=list)
    owns: list[str] = Field(default_factory=list)
    does_not_own: list[str] = Field(default_factory=list)
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    depends_on: list[str] = Field(default_factory=list)
    required_by: list[str] = Field(default_factory=list)
    interfaces: list[str] = Field(default_factory=list)
    events_produced: list[str] = Field(default_factory=list)
    events_consumed: list[str] = Field(default_factory=list)
    configuration: list[str] = Field(default_factory=list)
    schemas: list[str] = Field(default_factory=list)
    state_machines: list[str] = Field(default_factory=list)
    security: list[str] = Field(default_factory=list)
    recovery: list[str] = Field(default_factory=list)
    failure_behaviour: list[str] = Field(default_factory=list)
    performance: list[str] = Field(default_factory=list)
    validation: list[str] = Field(default_factory=list)
    testing: list[str] = Field(default_factory=list)
    cross_references: list[str] = Field(default_factory=list)
    version_history: list[str] = Field(default_factory=list)
    canonical_source: Optional[str] = None
    last_updated: Optional[str] = None
    raw_text: str = ""

class BehaviouralRoot(BaseModel):
    path: str
    signals: list[str]
    reason: str

class GovernanceProgress(BaseModel):
    programme: str
    phase: str
    completed: bool = False
    last_commit: Optional[str] = None
    notes: list[str] = Field(default_factory=list)
