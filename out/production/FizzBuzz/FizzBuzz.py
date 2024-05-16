class FizzBuzz:
    def main(self) -> None:
        for i in range(1, 101):
            divisibleBy3, divisibleBy5= (i%3)==0, (i%5)==0
            if divisibleBy3 and divisibleBy5:
                print("Fizz Buzz")
            elif divisibleBy3:
                print("Fizz")
            elif divisibleBy5:
                print("Buzz")
            else:
                print(i)
if __name__ == '__main__':
    FizzBuzz().main()