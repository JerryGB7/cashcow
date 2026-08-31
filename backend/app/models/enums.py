from enum import Enum

class ATMStatus(str, Enum):
    OPERATIONAL= "Operational"
    LOW_CASH = "Low-Cash"
    MAINTENANCE = "Maintenance"
    OFFLINE = "Offline"

class Service_Call_Status(str, Enum):
    PENDING="Pending"
    IN_PROGRESS="In-Progress"
    COMPLETED="Completed"
    FAILED="Failed"

class Service_Call_Priority(str, Enum):
    LOW="Low"
    MEDIUM="Medium"
    CRITICAL="Critical"

class Technician_RBAC(str, Enum):
    OPERATION_MANAGER = "Operation-Manager"
    FIELD_TECHNICIAN = "Field-Technician"
    AUDITOR = "Auditor"    