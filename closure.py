def outer_func():
    message = 'Hi'

    def inner_func():
        # message는 inner_func 안에서 선언되지는 않았지만
        # inner_func 함수 내에서 사용되기 때문에 자유 변수(free variable)
        print(message)

    return inner_func()

outer_func()


def outer_function(tag):
    text = 'Some text'
    tag = tag

    def inner_function(text=text):
        print('<{0}>{1}<{0}>'.format(tag, text))

    return inner_function

h1_func = outer_function('h1')
p_func = outer_function('p')

h1_func('This is text from h1_func')
p_func('p_func text')
h1_func()