from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game

# Create your views here.
def main(request):
    return render(request, 'fourth_task/main.html')

def shop(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'fourth_task/shop.html', context)

def cart(request):
    cart_items = request.session.get('cart', [])
    return render(request, 'fourth_task/cart.html', {'cart_items': cart_items})


users = ['Danil', 'Pavel', 'Anton']

def sign_up_by_django(request):
    info = {}
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            existing_users = Buyer.objects.values_list('name', flat=True)

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18 лет'
            else:
                Buyer.objects.create(name=username, balance=0.00, age=age)
                return render(request, 'fifth_task/registration_page.html',
                              {'message': f'Приветствуем, {username}!'})
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        existing_users = Buyer.objects.values_list('name', flat=True)

        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
        else:
            Buyer.objects.create(name=username, balance=0.00, age=age)
            info['message'] = f'Приветствуем, {username}!'
            users.append(username)
    return render(request, 'fifth_task/registration_page.html', info)