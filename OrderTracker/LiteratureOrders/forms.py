from django import forms

from .models import *


class SpecialOrderForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = SpecialOrder

        # Constrain the UserForm to just these fields.
        fields = ("ordered_by", "item", "quantity", "order_date", "received_date", "fulfilled_date")


class CreateSpecialOrderForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = SpecialOrder

        # Constrain the UserForm to just these fields.
        fields = ("ordered_by", "item", "quantity", "order_date",)

class BulkOrderForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = BulkOrder

        # Constrain the UserForm to just these fields.
        fields = ("ordered_by", "item", "quantity", "order_date", "received_date", "fulfilled_date")


class CreateBulkOrderForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = BulkOrder

        # Constrain the UserForm to just these fields.
        fields = ("ordered_by", "item", "quantity", "order_date",)