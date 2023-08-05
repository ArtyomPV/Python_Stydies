
** **
>from fastfood.models import *

>cap = Product(name='Капучино 0.3', price = 0.99) 

>cap.save()

>Product.objects.create(name= "Капучино 0.4", price = 109.0) 

>Product.objects.create(name = 'Картофель фри (станд.)', price = 93) 

>Product.objects.create(name='Картофель фри (бол.)', price = 106) 

>cashier1 = Staff.objects.create(full_name = 'Иванов Иван Иванович', position = Staff.CASHIER, labor_contract=1234)

>cashier2 = Staff.objects.create(position = Staff.CASHIER, full_name = 'Максимов Максим Максимович', labor_contract = 1235) 

>director = Staff.objects.create(labor_contract = 1111, full_name = 'Петров Петр Петрович', position = Staff.MANAGER) 

Произведём поиск, по номеру трудового договора. Для этого воспользуемся методом get() менеджера модели
>person = Staff.objects.get(labor_contract=1235)

>print(person) 
 
// Staff #2 - Position: CSHR 

>person.get_position_display() 

// 'Cashier'

поле position определили как  **СhoiceField** — поле с возможностью выбора. 
Знакомимся ещё с одной классной фишкой Django.
Он автоматически добавляет метод вида **get_FOO_display()**, 
где **FOO** — это название поля. Здесь мы и можем видеть, 
зачем нам нужно было задавать кортеж. 
Первое значение фактически хранится в базе данных, 
а с помощью второго метода можно получить любую другую строку, 
связанную с этим объектом!
** **
метод filter(). Согласно своему названию он фильтрует объекты в базе данных по заданным условиям. А условия задаются точно также — с помощью именованных аргументов.

Попробуем всё же получить наших сотрудников:
>cashiers = Staff.objects.filter(position=Staff.CASHIER)


> cashiers.values("full_name", "labor_contract")

// <QuerySet [{'full_name': 'Иванов Иван Иванович', 'labor_contract': 1234}, {'full_name': 'Максимов Максим Максимович', 'labor_contract': 1235}]>

** **
Фильтрация имеет огромное количество вспомогательных инструментов. 
Например, дописав к названию поля __gt в аргументе метода, 
можно найти все значения, которые больше (greater than) заданного числа.
> Product.objects.filter(price__gt=90)

    <QuerySet [<Product: Product #2 - Name: Капучино 0.4>,

    <Product: Product #3 - Name: Картофель фри (станд.)>,

    <Product: Product #4 - Name: Картофель фри (бол.)>]>

>Product.objects.filter(price__gt=90).values('name') 

     <QuerySet 

    [{'name': 'Капучино 0.4'}, 

    {'name': 'Картофель фри (станд.)'}, 

    {'name': 'Картофель фри (бол.)'}]>

Метод фильтрации по связанным объектам. Добавим несколько объектов в модель Order.

> Order.objects.create(staff = cashier1, take_away=False)

    // <Order: Order #1 - Total: 0>

> Order.objects.create(staff=cashier2, take_away=True) 

    //<Order: Order #2 - Total: 0>
>Order.objects.create(staff=cashier1, take_away=True)

    //<Order: Order #3 - Total: 0>

Мы имеем всего 3 заказа, два из которых принадлежат одному сотруднику 
и третий (в порядке добавления — второй) — другому сотруднику. 
Но, например, мы хотим получить все заказы сотрудника с labor_contract = 1234.
> Order.objects.filter(staff__labor_contract=1234).values('staff__full_name', 'take_away')

    //<QuerySet

    [{'staff__full_name': 'Иванов Иван Иванович', 'take_away': False},

    {'staff__full_name': 'Иванов Иван Иванович', 'take_away': True}]>

Мы применили фильтр, но не по самому полю текущей модели, 
а по полям связанной модели. Для этого использовали также 
двойное подчеркивание и сразу за ним — поле, по которому будем фильтровать. 
Аналогично мы можем поступать и со значениями! 
Используя двойное подчёркивание мы можем выводить поле связанного объекта модели, 
а не сам объект.

>Product.objects.all() 
    
выведет:

    //<QuerySet [<Product: Product #1 - Name: Капучино 0.3>, 
    
    <Product: Product #2 - Name: Капучино 0.4>, 

    <Product: Product #3 - Name: Картофель фри (станд.)>, 

    <Product: Product #4 - Name: Картофель фри (бол.)>]>

Проверка наличия, есть ли объект:
>ProductOrder.objects.all().exists()

выведет:

    False
метод сортировки order_by, по умолчанию в порядке возрастания
>Product.objects.all().order_by('name').values('name', 'price')

если использовать знак "-" минус, то сортировка будет по убыванию
>Product.objects.all().order_by('-price').values('name', 'price')
 
>
 
>
 
>
 
>
 
>
 
>
 
>
 
>
 
>
 
>
 