import time
class TimeExecute:
    def __init__(self):
        pass

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        exec_time_msec = 1000 * (time.time() - self.start_time)
        print(f"{exec_time_msec:,.3f} [msec]")
    
