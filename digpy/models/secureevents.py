from typing import List, Dict, Union, Optional
from datetime import datetime


# class Datum:
#     def __init__(self, id: str, actions: Optional[dict], agentId: Optional[int],cursor: str, timestamp: datetime, customer_id: int, originator: dict, category: dict, source: dict, name: str, description: str, severity: int, content: dict, labels: dict, agent_id: Optional[int], machine_id: Optional[str]) -> None:
#         self.id = id
#         self.actions = actions
#         self.agentId = agentId
#         self.cursor = cursor
#         self.timestamp = timestamp
#         self.customer_id = customer_id
#         self.originator = originator
#         self.category = category
#         self.source = source
#         self.name = name
#         self.description = description
#         self.severity = severity
#         self.content = content
#         self.labels = labels
#         self.agent_id = agent_id
#         self.machine_id = machine_id

class SecureEvents:
    def __init__(self, actions: Optional[dict], agentId: Optional[int], category: str, containerId: Optional[str], content: dict, cursor: str, customer_id: Optional[int], description: str, id: str, label: Optional[dict], machineId: Optional[str], name: str, originator: str, severity: int, source: str, timestamp: datetime, **kwargs) -> None:
    # def __init__(self, actions: Optional[dict], agentId: Optional[int], category: str, containerId: Optional[str], content: dict, cursor: str, customer_id: Optional[int], description: str, id: str, label: Optional[dict], machineId: Optional[str], name: str, originator: str, severity: int, source: str, timestamp: datetime, **kwargs) -> None:
    # def __init__(self, id: str, **kwargs) -> None:
        self.actions = actions
        self.agentId = agentId
        self.category = category
        self.containerId = containerId
        self.content = content
        self.cursor = cursor
        self.customer_id = customer_id
        self.description = description
        self.id = id
        self.label = label
        self.machineId = machineId
        self.name = name
        self.originator = originator
        self.severity = severity
        self.source = source
        self.timestamp = timestamp
        self.__dict__.update(kwargs)


# class Content:
#     def __init__(self, false_positive: bool, fields: Fields, internal_rule_name: str, matched_on_default: bool, origin: str, output: str, policy_id: int, rule_name: str, rule_sub_type: int, rule_tags: List[str], rule_type: int) -> None:
#         self.false_positive = false_positive
#         self.fields = fields
#         self.internal_rule_name = internal_rule_name
#         self.matched_on_default = matched_on_default
#         self.origin = origin
#         self.output = output
#         self.policy_id = policy_id
#         self.rule_name = rule_name
#         self.rule_sub_type = rule_sub_type
#         self.rule_tags = rule_tags
#         self.rule_type = rule_type


# class Labels:
#     def __init__(self, kubernetes_cluster_name: str, kubernetes_ingresse_name: str, kubernetes_namespace_name: str) -> None:
#         self.kubernetes_cluster_name = kubernetes_cluster_name
#         self.kubernetes_ingresse_name = kubernetes_ingresse_name
#         self.kubernetes_namespace_name = kubernetes_namespace_name


