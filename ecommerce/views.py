from django.shortcuts import render
from store.models import Product, ReviewRating
from django.shortcuts import render, redirect


def home(request):
    products = Product.objects.all().filter(
        is_available=True).order_by('created_date')

    for product in products:
        reviews = ReviewRating.objects.filter(
            product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }

    return render(request, 'home.html', context)


def contact_view(request):
    return render(request, 'contact.html')


def send_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Enviar correo
        send_mail(
            subject=f"Nuevo mensaje de {name}",
            message=message,
            from_email=email,
            recipient_list=['admin@example.com'],  # Cambia por tu correo
        )

        messages.success(request, 'Tu mensaje ha sido enviado con éxito.')
        return redirect('contact')
    return redirect('contact')
