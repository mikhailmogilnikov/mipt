import structlog

def configure_logging():
    structlog.configure(
        processors=[
            structlog.processors.JSONRenderer()
        ]
    )
