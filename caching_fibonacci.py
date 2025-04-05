
def caching_fibonacci():
  def fibonacci(n):
    cache = {} #Создать пустой словарь cache
    if n <= 0:
       return 0 
    if n == 1:
       return 1 
    if n in cache:
      return cache[n]

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]
  return fibonacci

fib = caching_fibonacci()

# Используем функцию fibonacci для вычисления чисел Фибоначчи 
print(fib(10)) # Выведет 55 
print(fib(15)) # Выведет 610