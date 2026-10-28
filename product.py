def get_input(prompt, cast=str):
    while True:
        value = input(prompt).strip()
        if not value:
            print('این مقدار نباید خالی باشد!\n')
            continue
        try:
            return cast(value)
        except ValueError:
            print('لطفاً عدد معتبر وارد کنید!\n')


FIELDS = {
    'name':     ('نام کالا : ', str),
    'quantity': ('تعداد کالا : ', int),
    'time':     ('زمان ورود کالا : ', str),
    'user':     ('یوزر تان را وارد کنید : ', str),
    'buy':      ('قیمت خرید را وارد کنید : ', float),
    'sell':     ('قیمت فروش را وارد کنید : ', float),
}

products = []


def add_product():
    product = {key: get_input(text, cast) for key, (text, cast) in FIELDS.items()}
    products.append(product)


add_product()
print(products)