from django import forms


class StockForm(forms.Form):
    ticker = forms.CharField(label="Enter Ticker", max_length=10)
