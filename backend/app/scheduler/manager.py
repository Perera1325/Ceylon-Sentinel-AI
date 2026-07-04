import logging

from ..config.settings import settings
from .jobs import (run_finance_collector, run_news_collector,
                   run_weather_collector)
from .scheduler import scheduler

logger = logging.getLogger(__name__)


def start_scheduler():
    """Start the scheduler and register all default jobs."""
    if not scheduler.running:
        scheduler.start()
        logger.info("APScheduler started successfully.")

        # Register News Collector Job
        scheduler.add_job(
            run_news_collector,
            "interval",
            minutes=settings.NEWS_INTERVAL_MINUTES,
            id="job_news_collector",
            replace_existing=True,
        )

        # Register Weather Collector Job
        scheduler.add_job(
            run_weather_collector,
            "interval",
            minutes=settings.WEATHER_INTERVAL_MINUTES,
            id="job_weather_collector",
            replace_existing=True,
        )

        # Register Finance Collector Job
        scheduler.add_job(
            run_finance_collector,
            "interval",
            minutes=settings.FINANCE_INTERVAL_MINUTES,
            id="job_finance_collector",
            replace_existing=True,
        )
        logger.info("All default collector jobs registered.")


def shutdown_scheduler():
    """Gracefully shutdown the scheduler."""
    if scheduler.running:
        scheduler.shutdown()
        logger.info("APScheduler shut down successfully.")


def pause_job(job_id: str):
    scheduler.pause_job(job_id)


def resume_job(job_id: str):
    scheduler.resume_job(job_id)


def stop_job(job_id: str):
    scheduler.remove_job(job_id)


def get_jobs():
    return scheduler.get_jobs()
