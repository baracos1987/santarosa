from django import forms # importamos biblioteca forms *7


#creamos una clase llamada OpcionForm *7

class RequisitosForm(forms.Form):
    OPCIONES = (
        ('opcion1', 'Matricula Inicial'),
        ('opcion2', 'Traspaso'),
        ('opcion3', 'Rematricula'),
    )
    opcion = forms.ChoiceField(choices=OPCIONES, label='Seleccione el Trámite')