"""Video event collector"""
from kafka import KafkaProducer
import json
from datetime import datetime

class VideoEventCollector:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    
    def track_event(self, event_type, video_id, user_id, metadata):
        event = {
            'event_type': event_type,
            'video_id': video_id,
            'user_id': user_id,
            'timestamp': datetime.now().isoformat(),
            'metadata': metadata
        }
        self.producer.send('video-events', value=event)
