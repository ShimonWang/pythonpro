import cal_pi
import time
import cal_pi_compile


def main():
    start_time = time.time()
    print(cal_pi.calculate_pi(20_000_000))
    print(f"time {time.time() - start_time}")

    start_time = time.time()
    print(cal_pi_compile.calculate_pi(20_000_000))
    print(f"time {time.time() - start_time}")

    start_time = time.time()
    print(cal_pi_compile.calculate_pi_anotated(20_000_000))
    print(f"time {time.time() - start_time}")


if __name__ == "__main__":
    main()