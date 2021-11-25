def sum_factorial(start, stop):
  # 递归求阶乘
  def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

  # 生成器解析式生成各个数的阶乘，然后再求和
  return sum(factorial(i) for i in range(start, stop+1))

# 调用函数，测试代码
print(sum_factorial(1, 20))
