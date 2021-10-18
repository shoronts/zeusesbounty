from django.shortcuts import render


class ZeusesBountyUsers:

    def login(self):
        return render(self, 'login.html')

    def register(self):
        return render(self, 'register.html')
