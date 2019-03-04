# test celery

from celery import Celery

app = Celery('tasks',
             backend='redis://localhost:6379/0',
             broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    print("ok")
    app.worker_main()

