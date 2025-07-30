from dataclasses import dataclass, field
from typing import Any, Dict, Optional

@dataclass
class InputData:
    text: Optional[str] = None
    image: Optional[bytes] = None  # Raw image bytes
    audio: Optional[bytes] = None  # Raw audio bytes
    video: Optional[bytes] = None  # Raw video bytes
    document: Optional[bytes] = None # Raw document bytes (PDF, DOC, etc.)
    table: Optional[Any] = None    # Structured table data (e.g., pandas DataFrame, list of dicts)
    sensor_data: Optional[Dict[str, Any]] = None # Real-time sensor data
    logs: Optional[str] = None     # Interaction logs
    
    # Metadados
    origin: Optional[str] = None
    timestamp: Optional[str] = None # Using str for simplicity, can be datetime object
    user_authentication: Optional[Dict[str, Any]] = None

    def __post_init__(self):
        # Ensure at least one content type is provided
        if not any([self.text, self.image, self.audio, self.video, self.document, self.table, self.sensor_data, self.logs]):
            raise ValueError("At least one content type (text, image, audio, video, document, table, sensor_data, logs) must be provided.")
