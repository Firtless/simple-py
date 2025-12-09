import time


class Timer:
    def __enter__(self):
        self._enter_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._exit_time = time.time()


def main():
    with Timer() as timer:

        print("Starting timed operation...")
        time.sleep(5.23)  # Simulate a task
        print("Timed operation finished.")

    print(f"{timer._exit_time - timer._enter_time:.2f} seconds elapsed")


if __name__ == "__main__":
    main()
