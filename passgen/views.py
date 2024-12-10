import secrets
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import PasswordGeneratorForm

# main page
def index(request):
    return render(request, 'main.html')

# gen pass view
def password_generator_view(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            use_uppercase = form.cleaned_data['use_uppercase']
            use_numbers = form.cleaned_data['use_numbers']

            # gen password
            characters = 'abcdefghijklmnopqrstuvwxyz'
            if use_uppercase:
                characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if use_numbers:
                characters += '0123456789'

            password = ''.join(secrets.choice(characters) for _ in range(length))

            # gen unique id 
            password_id = secrets.token_hex(16)

            # save password to session
            request.session[f'generated_password_{password_id}'] = password
            messages.success(request, f"Сгенерирован пароль: {password}")
	    # redirect to detail page
            return redirect(f'/generate/{password_id}')
    else:
        form = PasswordGeneratorForm()

    return render(request, 'generate.html', {'form': form})

def password_detail_view(request, password_id):
    generated_password = request.session.get(f'generated_password_{password_id}')

    if not generated_password:
        messages.error(request, "Пароль не найден")
        return redirect('home')

    return render(request, 'password_detail.html', {'generated_password': generated_password})
