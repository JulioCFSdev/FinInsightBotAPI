from django.shortcuts import render
import django.http
from .models import User


def user(response, pk):
    try:
        user_obj = User.objects.get(id=pk)
        context = {'user': user_obj}
        return django.http.HttpResponse('User founded!', context)
    except Exception as exception:
        print(f'response: {response}\nexception: {exception}')
        return django.http.HttpResponseNotFound('User not founded!')
    
def users(response):
    try:
        users_obj = User.objects.all()
        context = {'users': users_obj}
        return django.http.JsonResponse('Users founded!', context)
    except Exception as exception:
        print(f'response: {response}\nexception: {exception}')
        return django.http.HttpResponseNotFound('Has a internal problem in Users getter')

def add_user(response):
    try:
        return django.http.HttpResponse('User created with sucess!')
    except Exception as exception:
        print(f'response: {response}\nexception: {exception}')
        return django.http.HttpResponseBadRequest("User not created with sucess!")
    
def update_user(response, pk):
    try:
        return django.http.HttpResponse('User has updated with sucess!')
    except Exception as exception:
        print(f'response: {response}\nexception: {exception}')
        return django.http.HttpResponseNotModified('User hasnt updated with sucess!')
    
def delete_user(response, pk):
    try:
        return django.http.HttpResponse('User deleted with sucess!')
    except Exception as exception:
        print(f'response: {response}\nexception: {exception}')
        return django.http.HttpResponseForbidden("Operação de exclusão cancelada. Você não tem permissão para excluir este item.")