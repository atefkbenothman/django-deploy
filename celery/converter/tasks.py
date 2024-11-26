from .celery import app


@app.task(name="add_numbers")
def add(x, y):
    print("-------")
    print(f"adding numbers: {x} and {y}")
    print("-------")
    return x + y
