from django.shortcuts import render
# from django.core.email import send_email


def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message= request.POST['message']

        #send email
        # send_email(
        #     message_name, #subject
        #     message, #message
        #     message_email, #from_email
        #     'anhtuanbk1994@gmail.com', #to_email
        #     fail_silently=False

        # )

        return render(request, 'contact.html', {'message_name':message_name , 'message_email':message_email , 'message': message})
    else:
        return render(request, 'contact.html', {})
