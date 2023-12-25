from tkinter import *
from tkinter import ttk # ttk --> themed ใน TK


def ClickButton(event):
    if Export.get() == "Export":

        """print(float(textCurrency_01.get())*float(Currency_01.get())/float(Currency_02.get()))
        label_convert.configure()"""

        if Currency_01.get() == "USD" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 34.9175 / 34.9175)
            label_convert.configure(text=float(textCurrency_01.get()) * 34.9175 / 34.9175)
        elif Currency_01.get() == "USD" and Currency_02.get() == "EUR":
            print(float(textCurrency_01.get()) * 34.9175 / 37.8893)
            label_convert.configure(text=float(textCurrency_01.get()) * 34.9175 / 37.8893)
        elif Currency_01.get() == "USD" and Currency_02.get() == "JPY":
            print(float(textCurrency_01.get()) * 34.9175 / 23.1813)
            label_convert.configure(text=float(textCurrency_01.get()) * 34.9175 / 23.1813)
        elif Currency_01.get() == "USD" and Currency_02.get() == "HKD":
            print(float(textCurrency_01.get()) * 34.9175 / 4.4580)
            label_convert.configure(text=float(textCurrency_01.get()) * 34.9175 / 4.4580)
        elif Currency_01.get() == "USD" and Currency_02.get() == "MYR":
            print(float(textCurrency_01.get()) * 34.9175 / 7.3884)
            label_convert.configure(text=float(textCurrency_01.get()) * 34.9175 / 7.3884)
        elif Currency_01.get() == "USD" and Currency_02.get() == "SGD":
            print(float(textCurrency_01.get()) * 34.9175 / 25.8733)
            label_convert.configure(text=float(textCurrency_01.get()) * 34.9175 / 25.8733)
        elif Currency_01.get() == "USD" and Currency_02.get() == "AUD":
            print(float(textCurrency_01.get()) * 34.9175 / 22.5136)
            label_convert.configure(text=float(textCurrency_01.get()) * 34.9175 / 22.5136)
        elif Currency_01.get() == "USD" and Currency_02.get() == "CNY":
            print(float(textCurrency_01.get()) * 34.9175 / 4.8133)
            label_convert.configure(text=float(textCurrency_01.get()) * 34.9175 / 4.8133)
        elif Currency_01.get() == "USD" and Currency_02.get() == "RUB":
            print(float(textCurrency_01.get()) * 34.9175 / 0.3939)
            label_convert.configure(text=float(textCurrency_01.get()) * 34.9175 / 0.3939)
        elif Currency_01.get() == "USD" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 34.9175 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 34.9175 / 1)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 37.8893 / 34.9175)
            label_convert.configure(text=float(textCurrency_01.get()) * 37.8893 / 34.9175)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "EUR":
            print(float(textCurrency_01.get()) * 37.8893 / 37.8893)
            label_convert.configure(text=float(textCurrency_01.get()) * 37.8893 / 37.8893)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "JPY":
            print(float(textCurrency_01.get()) * 37.8893 / 23.1813)
            label_convert.configure(text=float(textCurrency_01.get()) * 37.8893 / 23.1813)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "HKD":
            print(float(textCurrency_01.get()) * 37.8893 / 4.4580)
            label_convert.configure(text=float(textCurrency_01.get()) * 37.8893 / 4.4580)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "MYR":
            print(float(textCurrency_01.get()) * 37.8893 / 7.3884)
            label_convert.configure(text=float(textCurrency_01.get()) * 37.8893 / 7.3884)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "SGD":
            print(float(textCurrency_01.get()) * 37.8893 / 25.8733)
            label_convert.configure(text=float(textCurrency_01.get()) * 37.8893 / 25.8733)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "AUD":
            print(float(textCurrency_01.get()) * 37.8893 / 22.5136)
            label_convert.configure(text=float(textCurrency_01.get()) * 37.8893 / 22.5136)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "CNY":
            print(float(textCurrency_01.get()) * 37.8893 / 4.8133)
            label_convert.configure(text=float(textCurrency_01.get()) * 37.8893 / 4.8133)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "RUB":
            print(float(textCurrency_01.get()) * 37.8893 / 0.3939)
            label_convert.configure(text=float(textCurrency_01.get()) * 37.8893 / 0.3939)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 37.8893 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 37.8893 / 1)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 23.1813 / 34.9175)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.1813 / 34.9175)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "EUR":
            print(float(textCurrency_01.get()) * 23.1813 / 37.8893)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.1813 / 37.8893)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "JPY":
            print(float(textCurrency_01.get()) * 23.1813 / 23.1813)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.1813 / 23.1813)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "HKD":
            print(float(textCurrency_01.get()) * 23.1813 / 4.4580)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.1813 / 4.4580)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "MYR":
            print(float(textCurrency_01.get()) * 23.1813 / 7.3884)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.1813 / 7.3884)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "SGD":
            print(float(textCurrency_01.get()) * 23.1813 / 25.8733)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.1813 / 25.8733)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "AUD":
            print(float(textCurrency_01.get()) * 23.1813 / 22.5136)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.1813 / 22.5136)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "CNY":
            print(float(textCurrency_01.get()) * 23.1813 / 4.8133)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.1813 / 4.8133)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "RUB":
            print(float(textCurrency_01.get()) * 23.1813 / 0.3939)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.1813 / 0.3939)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 23.1813 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.1813 / 1)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 4.4580 / 34.9175)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.4580 / 34.9175)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "EUR":
            print(float(textCurrency_01.get()) * 4.4580 / 37.8893)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.4580 / 37.8893)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "JPY":
            print(float(textCurrency_01.get()) * 4.4580 / 23.1813)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.4580 / 23.1813)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "HKD":
            print(float(textCurrency_01.get()) * 4.4580 / 4.4580)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.4580 / 4.4580)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "MYR":
            print(float(textCurrency_01.get()) * 4.4580 / 7.3884)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.4580 / 7.3884)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "SGD":
            print(float(textCurrency_01.get()) * 4.4580 / 25.8733)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.4580 / 25.8733)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "AUD":
            print(float(textCurrency_01.get()) * 4.4580 / 22.5136)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.4580 / 22.5136)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "CNY":
            print(float(textCurrency_01.get()) * 4.4580 / 4.8133)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.4580 / 4.8133)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "RUB":
            print(float(textCurrency_01.get()) * 4.4580 / 0.3939)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.4580 / 0.3939)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 4.4580 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.4580 / 1)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 7.3884 / 34.9175)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.3884 / 34.9175)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "EUR":
            print(float(textCurrency_01.get()) * 7.3884 / 37.8893)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.3884 / 37.8893)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "JPY":
            print(float(textCurrency_01.get()) * 7.3884 / 23.1813)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.3884 / 23.1813)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "HKD":
            print(float(textCurrency_01.get()) * 7.3884 / 4.4580)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.3884 / 4.4580)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "MYR":
            print(float(textCurrency_01.get()) * 7.3884 / 7.3884)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.3884 / 7.3884)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "SGD":
            print(float(textCurrency_01.get()) * 7.3884 / 25.8733)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.3884 / 25.8733)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "AUD":
            print(float(textCurrency_01.get()) * 7.3884 / 22.5136)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.3884 / 22.5136)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "CNY":
            print(float(textCurrency_01.get()) * 7.3884 / 4.8133)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.3884 / 4.8133)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "RUB":
            print(float(textCurrency_01.get()) * 7.3884 / 0.3939)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.3884 / 0.3939)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 7.3884 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.3884 / 1)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 25.8733 / 34.9175)
            label_convert.configure(text=float(textCurrency_01.get()) * 25.8733 / 34.9175)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "EUR":
            print(float(textCurrency_01.get()) * 25.8733 / 37.8893)
            label_convert.configure(text=float(textCurrency_01.get()) * 25.8733 / 37.8893)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "JPY":
            print(float(textCurrency_01.get()) * 25.8733 / 23.1813)
            label_convert.configure(text=float(textCurrency_01.get()) * 25.8733 / 23.1813)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "HKD":
            print(float(textCurrency_01.get()) * 25.8733 / 4.4580)
            label_convert.configure(text=float(textCurrency_01.get()) * 25.8733 / 4.4580)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "MYR":
            print(float(textCurrency_01.get()) * 25.8733 / 7.3884)
            label_convert.configure(text=float(textCurrency_01.get()) * 25.8733 / 7.3884)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "SGD":
            print(float(textCurrency_01.get()) * 25.8733 / 25.8733)
            label_convert.configure(text=float(textCurrency_01.get()) * 25.8733 / 25.8733)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "AUD":
            print(float(textCurrency_01.get()) * 25.8733 / 22.5136)
            label_convert.configure(text=float(textCurrency_01.get()) * 25.8733 / 22.5136)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "CNY":
            print(float(textCurrency_01.get()) * 25.8733 / 4.8133)
            label_convert.configure(text=float(textCurrency_01.get()) * 25.8733 / 4.8133)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "RUB":
            print(float(textCurrency_01.get()) * 25.8733 / 0.3939)
            label_convert.configure(text=float(textCurrency_01.get()) * 25.8733 / 0.3939)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 25.8733 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 25.8733 / 1)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 22.5136 / 34.9175)
            label_convert.configure(text=float(textCurrency_01.get()) * 22.5136 / 34.9175)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "EUR":
            print(float(textCurrency_01.get()) * 22.5136 / 37.8893)
            label_convert.configure(text=float(textCurrency_01.get()) * 22.5136 / 37.8893)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "JPY":
            print(float(textCurrency_01.get()) * 22.5136 / 23.1813)
            label_convert.configure(text=float(textCurrency_01.get()) * 22.5136 / 23.1813)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "HKD":
            print(float(textCurrency_01.get()) * 22.5136 / 4.4580)
            label_convert.configure(text=float(textCurrency_01.get()) * 22.5136 / 4.4580)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "MYR":
            print(float(textCurrency_01.get()) * 22.5136 / 7.3884)
            label_convert.configure(text=float(textCurrency_01.get()) * 22.5136 / 7.3884)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "SGD":
            print(float(textCurrency_01.get()) * 22.5136 / 25.8733)
            label_convert.configure(text=float(textCurrency_01.get()) * 22.5136 / 25.8733)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "AUD":
            print(float(textCurrency_01.get()) * 22.5136 / 22.5136)
            label_convert.configure(text=float(textCurrency_01.get()) * 22.5136 / 22.5136)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "CNY":
            print(float(textCurrency_01.get()) * 22.5136 / 4.8133)
            label_convert.configure(text=float(textCurrency_01.get()) * 22.5136 / 4.8133)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "RUB":
            print(float(textCurrency_01.get()) * 22.5136 / 0.3939)
            label_convert.configure(text=float(textCurrency_01.get()) * 22.5136 / 0.3939)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 22.5136 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 22.5136 / 1)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 4.8133 / 34.9175)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.8133 / 34.9175)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "EUR":
            print(float(textCurrency_01.get()) * 4.8133 / 37.8893)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.8133 / 37.8893)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "JPY":
            print(float(textCurrency_01.get()) * 4.8133 / 23.1813)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.8133 / 23.1813)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "HKD":
            print(float(textCurrency_01.get()) * 4.8133 / 4.4580)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.8133 / 4.4580)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "MYR":
            print(float(textCurrency_01.get()) * 4.8133 / 7.3884)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.8133 / 7.3884)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "SGD":
            print(float(textCurrency_01.get()) * 4.8133 / 25.8733)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.8133 / 25.8733)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "AUD":
            print(float(textCurrency_01.get()) * 4.8133 / 22.5136)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.8133 / 22.5136)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "CNY":
            print(float(textCurrency_01.get()) * 4.8133 / 4.8133)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.8133 / 4.8133)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "RUB":
            print(float(textCurrency_01.get()) * 4.8133 / 0.3939)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.8133 / 0.3939)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 4.8133 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.8133 / 1)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 0.3939 / 34.9175)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3939 / 34.9175)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "EUR":
            print(float(textCurrency_01.get()) * 0.3939 / 37.8893)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3939 / 37.8893)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "JPY":
            print(float(textCurrency_01.get()) * 0.3939 / 23.1813)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3939 / 23.1813)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "HKD":
            print(float(textCurrency_01.get()) * 0.3939 / 4.4580)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3939 / 4.4580)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "MYR":
            print(float(textCurrency_01.get()) * 0.3939 / 7.3884)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3939 / 7.3884)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "SGD":
            print(float(textCurrency_01.get()) * 0.3939 / 25.8733)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3939 / 25.8733)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "AUD":
            print(float(textCurrency_01.get()) * 0.3939 / 22.5136)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3939 / 22.5136)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "CNY":
            print(float(textCurrency_01.get()) * 0.3939 / 4.8133)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3939 / 4.8133)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "RUB":
            print(float(textCurrency_01.get()) * 0.3939 / 0.3939)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3939 / 0.3939)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 0.3939 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3939 / 1)
        elif Currency_01.get() == "THB" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 1 / 34.9175)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 34.9175)
        elif Currency_01.get() == "THB" and Currency_02.get() == "EUR":
            print(float(textCurrency_01.get()) * 1 / 37.8893)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 37.8893)
        elif Currency_01.get() == "THB" and Currency_02.get() == "JPY":
            print(float(textCurrency_01.get()) * 1 / 23.1813)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 23.1813)
        elif Currency_01.get() == "THB" and Currency_02.get() == "HKD":
            print(float(textCurrency_01.get()) * 1 / 4.4580)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 4.4580)
        elif Currency_01.get() == "THB" and Currency_02.get() == "MYR":
            print(float(textCurrency_01.get()) * 1 / 7.3884)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 7.3884)
        elif Currency_01.get() == "THB" and Currency_02.get() == "SGD":
            print(float(textCurrency_01.get()) * 1 / 25.8733)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 25.8733)
        elif Currency_01.get() == "THB" and Currency_02.get() == "AUD":
            print(float(textCurrency_01.get()) * 1 / 22.5136)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 22.5136)
        elif Currency_01.get() == "THB" and Currency_02.get() == "CNY":
            print(float(textCurrency_01.get()) * 1 / 4.8133)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 4.8133)
        elif Currency_01.get() == "THB" and Currency_02.get() == "RUB":
            print(float(textCurrency_01.get()) * 1 / 0.3939)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 0.3939)
        elif Currency_01.get() == "THB" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 1 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 1)

        Currency_01.values = {'USD':34.9175,'EUR':37.8893,'JPY':23.1813,'HKD':4.4580,'MYR':7.3884,'SGD':25.8733,'AUD':22.5136,'CNY':4.8133,'RUB':0.3939,'THB':1}
        Currency_02.values = [34.9175,37.8893,23.1813,4.4580,7.3884,25.8733,22.5136,4.8133,0.3939,1]


    else:
        if Currency_01.get() == "USD" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 35.3284 / 35.3284)
            label_convert.configure(text=float(textCurrency_01.get()) * 35.3284 / 35.3284)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 38.7002 / 35.3284)
            label_convert.configure(text=float(textCurrency_01.get()) * 38.7002 / 35.3284)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 23.9481 / 35.3284)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.9481 / 35.3284)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 4.5502 / 35.3284)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.5502 / 35.3284)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 7.6335 / 35.3284)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.6335 / 35.3284)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 26.5117 / 35.3284)
            label_convert.configure(text=float(textCurrency_01.get()) * 26.5117 / 35.3284)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 23.3739 / 35.3284)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.3739 / 35.3284)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 4.9661 / 35.3284)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.9661 / 35.3284)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 0.3976 / 35.3284)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3976 / 35.3284)
        elif Currency_01.get() == "THB" and Currency_02.get() == "USD":
            print(float(textCurrency_01.get()) * 1 / 35.3284)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 35.3284)
        elif Currency_01.get() == "USD" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 35.3284 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 35.3284 / 1)
        elif Currency_01.get() == "EUR" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 38.7002 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 38.7002 / 1)
        elif Currency_01.get() == "JPY" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 23.9481 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.9481 / 1)
        elif Currency_01.get() == "HKD" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 4.5502 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.5502 / 1)
        elif Currency_01.get() == "MYR" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 7.6335 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 7.6335 / 1)
        elif Currency_01.get() == "SGD" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 26.5117 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 26.5117 / 1)
        elif Currency_01.get() == "AUD" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 23.3739 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 23.3739 / 1)
        elif Currency_01.get() == "CNY" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 4.9661 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 4.9661 / 1)
        elif Currency_01.get() == "RUB" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 0.3976 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 0.3976 / 1)
        elif Currency_01.get() == "THB" and Currency_02.get() == "THB":
            print(float(textCurrency_01.get()) * 1 / 1)
            label_convert.configure(text=float(textCurrency_01.get()) * 1 / 1)


Mainwindow = Tk()
label_Custom = Label(Mainwindow,text="Thai Customs",width=20,bg="green",font=("Helvetica",38))
label_Custom.grid(row=0)
label_Date = Label(Mainwindow,text="December, 2023",width=80,anchor=E)
label_Date.grid(row=1)

Export = ttk.Combobox(Mainwindow, values=['Export','Import'],width=6,font=("Helvetica",18))
Export.current(0)
Export.grid(row=2)

label_From = Label(Mainwindow,text="From")
label_From.place(x=100,y=120)

Currency_01 = ttk.Combobox(Mainwindow, values=['USD','EUR','JPY','HKD','MYR','SGD','AUD','CNY','RUB','THB'],width=4)
Currency_01.current(0)
Currency_01.place(x=100,y=160)
textCurrency_01 = Entry(Mainwindow)
textCurrency_01.place(x=200,y=160)

label_To = Label(Mainwindow,text="To")
label_To.place(x=100,y=200)

Calculate = Button(Mainwindow,text="Calculate")
Calculate.place(x=200,y=200)
Calculate.bind('<Button-1>',ClickButton)
Currency_02 = ttk.Combobox(Mainwindow, values=['USD','EUR','JPY','HKD','MYR','SGD','AUD','CNY','RUB','THB'],width=4)
Currency_02.current(0)
Currency_02.place(x=100,y=240)

label_convert = Label(Mainwindow,text="Result")
label_convert.place(x=200,y=240)
Mainwindow.mainloop()

