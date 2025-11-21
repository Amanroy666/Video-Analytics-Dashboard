"""Dashboard API endpoints"""
from fastapi import FastAPI
from datetime import date

app = FastAPI()

@app.get("/videos/{video_id}/metrics")
async def get_video_metrics(video_id: str):
    return {
        'video_id': video_id,
        'total_views': 15234,
        'avg_watch_time': 125.5,
        'completion_rate': 68.5,
        'likes': 1523,
        'comments': 234
    }

@app.get("/analytics/trends")
async def get_trends(start_date: date, end_date: date):
    return {
        'period': f"{start_date} to {end_date}",
        'trending_categories': ['tech', 'education', 'entertainment'],
        'top_videos': []
    }
