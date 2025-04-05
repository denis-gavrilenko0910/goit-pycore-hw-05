from typing import Callable
import re

def generator_numbers(text: str):
  regxp_pattern = r'\d+\.\d+'
  for num in re.findall(regxp_pattern, text):
    yield float(num)
   
def sum_profit(text: str, func: Callable):
  total = 0
  for num in func(text):
    total +=num
  
  return total
  
text = "Общий доход работника состоит из нескольких частей: 1000.01 как основной доход, дополненный дополнительными поступлениями 27.45 и 324.00 долларов." 

total_income = sum_profit(text, generator_numbers)

print(f"Общий доход: {total_income}")