from django import forms

from web_app.models import SATELLITE_STATUS, Satellite


class SatelliteForm(forms.ModelForm):
    identifier = forms.CharField(
        label="Идентификатор",
        help_text="Уникальный идентификатор спутника",
    )
    name = forms.CharField(
        label="Название",
        help_text="Название спутника",
    )
    purpose = forms.CharField(
        label="Назначение",
        help_text="Назначение спутника",
    )
    image_url = forms.URLField(
        label="Ссылка на изображение",
        help_text="Ссылка на изображение спутника",
        required=False,
    )
    status = forms.ChoiceField(
        label="Статус",
        choices=SATELLITE_STATUS,
        help_text="Статус спутника",
    )
    is_frequency_violator = forms.BooleanField(
        label="Нарушитель частот",
        help_text="Является ли спутник нарушителем частот",
        required=False,
    )
    country = forms.CharField(
        label="Страна",
        help_text="Страна, в которой спутник был запущен",
        required=False,
    )
    launch_date = forms.DateField(
        label="Дата запуска",
        help_text="Дата запуска спутника",
        required=False,
    )

    class Meta:
        model = Satellite
        fields = [
            "identifier",
            "name",
            "purpose",
            "image_url",
            "status",
            "is_frequency_violator",
            "country",
            "launch_date",
        ]
