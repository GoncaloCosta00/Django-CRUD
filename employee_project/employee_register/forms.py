from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('nome','telefone','emp_codigo','cargo')
        labels = {
            'emp_codigo':'Código Empregado'
        }
#para em vez de aparecer -------, aparecer select
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['cargo'].empty_label = "Select"
        #para o código de empregado não ser de preenchimento obrigatório
        self.fields['emp_codigo'].required = False
