from django import forms # importamos biblioteca forms *7


#creamos una clase llamada OpcionForm *7

class RequisitosForm(forms.Form):
    OPCIONES = (
        ('opcion1', 'Matricula Inicial'),
        ('opcion2', 'Matricula Inician Con Prenda'),
        ('opcion3', 'Traspaso'),
        ('opcion4', 'Traspaso Con Prenda'),
        ('opcion5', 'Radicado'),
        ('opcion6', 'Traslado De Cuenta'),
        ('opcion7', 'Cancelacion Licencia Deterioro'),
        ('opcion8', 'Duplicado Licencia'),
        ('opcion9', 'Inscripcion o Levanta Prenda'),
        ('opcion10', 'Cambio de Color'),
        ('opcion11', 'Cambio de Servicio'),
        ('opcion12', 'Duplicado de Placa'),
        ('opcion13', 'Cambio de Motor - Regrabación'),
        ('opcion14', 'Cambio de Motor'),
        ('opcion15', 'Cambio de carroceria otro'),
        ('opcion16', 'Cambio de carroceria'),
        ('opcion17', 'Repotenciación'),
        ('opcion18', 'Rematricula'),
        ('opcion20', 'Traspaso y Remate'),
        ('opcion19', 'Transformación'),
        ('opcion21', 'Traspaso Indeterminado'),
        ('opcion22', 'Blindaje'),
        ('opcion23', 'Modificación Alerta Propietario'),
        ('opcion24', 'Modificación Alerta Acreedor'),
        ('opcion25', 'Cancelacion Licencia'),
        ('opcion26', 'Polarizado'),
        ('opcion27', 'Cambio Conjunto'),
        ('opcion28', 'Historial Vehiculo'),
        ('opcion29', 'Inscripcion al RUNT'),
        ('opcion30', 'Actualizacion RUNT'),
        ('opcion31', 'Expedicion Licencia Conducción'),
        ('opcion32', 'Actualizar Licencia Conduccion TI a CC - Diferente Número'),
        ('opcion33', 'Actualizar Licencia Conduccion TI a CC - El mismo número'),

    )
    # le colocamos estilo al campo de texto con widget=forms.Select(attrs={'class': 'form-control'})
    opcion = forms.ChoiceField(choices=OPCIONES, label='Seleccione el Trámite', widget=forms.Select(attrs={'class': 'form-control'}))



class RequisitosFormMoto(forms.Form):
    OPCIONES = (
        ('opcion1', 'Matricula Inicial'),
        ('opcion2', 'Matricula Inician Con Prenda'),
        ('opcion3', 'Traspaso'),
        ('opcion4', 'Traspaso Con Prenda'),
        ('opcion5', 'Radicado'),
        ('opcion6', 'Traslado De Cuenta'),
        ('opcion7', 'Cancelacion Licencia Deterioro'),
        ('opcion8', 'Duplicado Licencia'),
        ('opcion9', 'Inscripcion o Levanta Prenda'),
        ('opcion10', 'Cambio de Color'),
        ('opcion11', 'Duplicado de Placa'),
        ('opcion12', 'Cambio de Motor - Regrabación'),
        ('opcion13', 'Cambio de Motor'),
        ('opcion14', 'Rematricula'),
        ('opcion15', 'Transformación'),
        ('opcion16', 'Traspaso Indeterminado'),
        ('opcion17', 'Modificación Alerta Propietario'),
        ('opcion18', 'Modificación Alerta Acreedor'),
        ('opcion19', 'Cancelacion Licencia'),
        ('opcion20', 'Historial Vehiculo'),
       

    )
    # le colocamos estilo al campo de texto con widget=forms.Select(attrs={'class': 'form-control'})
    opcion = forms.ChoiceField(choices=OPCIONES, label='Seleccione el Trámite', widget=forms.Select(attrs={'class': 'form-control'}))

