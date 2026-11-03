import uvicorn

# Log levels: trace, debug, info, warning, error, critical


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="debug",
        workers=1,
    )
