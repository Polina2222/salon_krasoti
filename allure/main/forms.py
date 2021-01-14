from django import forms

from .models import Order


class CallbackForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)

    def save(self, *args, **kwargs):
        cd = self.cleaned_data
        client_name = cd["name"]
        client_phone = cd["phone"]
        client_email = cd["email"]
        client_comment = cd["comment"]

        Order.objects.create(
            client_name=client_name,
            client_phone=client_phone,
            client_email=client_email,
            client_comment=client_comment
        )
