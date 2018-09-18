def sum(a, b):
    return a + b

print(sum(2, 3))
# 변수나 데이터 구조안에 담을 수 있다.
# func_add 변수에 sum 함수를 저장할 수 있다
func_add = sum

# 두 출력 결과가 동일한 함수를 가리키고 있다.
print(func_add)
print(sum)

print(func_add(3, 4))


# 인자(parameter), 인수(argument)
# x는 인자
def square(x):
    return x * x

t = 5   # t 는 인수
square(t)
square(5)   # 인수 5를 집접 전달


# 함수의 인자로 전달할 수 있다.
def my_map(func, arg_list1):
    result = []
    for arg in arg_list1:
        result.append(func(arg, arg))

    return result

arg_list = [1, 2, 3, 4, 5]
print(arg_list)
print(my_map(sum, arg_list))

# 기존 함수나 모듈을 수정할 필요 없이 편리하게 쓸 수 있는
# 기능?? 예제 실용적인 예제가 뭐가 있을까?


# 함수의 결과값으로 함수 리턴하기
def logger(msg):

    # 클로저(closure)
    # logger()가 종료된 후에도 msg 지역 변수를 참조할 수 있음
    def log_message():
        print('Log: ', msg)

    return log_message

log_hi = logger('hi')
print(log_hi)
log_hi()
print(logger)

del logger  # 글로벌 네임스페이스에서 logger 오브젝트를 지웁니다.

try:
    print(logger)
except NameError:
    print('NameError: logger는 존재하지 않습니다.')

log_hi()

# 파이썬의 네임스페이스 구성은 어떻게 되어 있을까?
# 파이썬의 실행 모델은 어떻게 구성되어 있고 어떻게 동작할까?
