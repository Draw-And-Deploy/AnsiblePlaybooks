from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/api/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/api/access_log'
errorlog =  '/api/error_log'
