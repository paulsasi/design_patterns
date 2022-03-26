import calculator
import time

def speed_test(service: calculator.CalculatorService):
    numbers = [10000, 20000, 30000, 40000, 50000]
    start = time.time()
    for i in range(100):
        number = numbers[i % 5]
        result = service.factorial(number)
    print(f"Took: {time.time()-start} seconds")

if __name__ == '__main__':

    compute_center = calculator.Calculator()
    compute_center_proxy = calculator.CalculatorProxy(service=compute_center)

    print("No cache test")
    speed_test(compute_center)

    print("Cache test")
    speed_test(compute_center_proxy)
