from django import forms

from web_app.models import (
    SATELLITE_STATUS,
    TRANSMITTER_STATUS,
    TRANSMITTER_TYPES,
    Satellite,
    Tle,
    Transmitter,
)


class SatelliteForm(forms.ModelForm):
    identifier = forms.CharField(
        label="Идентификатор",
        help_text="Уникальный идентификатор спутника",
    )
    name = forms.CharField(
        label="Название",
        help_text="Уникальное название спутника",
    )
    purpose = forms.CharField(
        label="Назначение",
        help_text="Назначение спутника",
    )
    image = forms.ImageField(
        label="Изображение",
        help_text="Изображение спутника",
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
            "image",
            "status",
            "is_frequency_violator",
            "country",
            "launch_date",
        ]


class TransmitterForm(forms.ModelForm):
    satellite = forms.ModelChoiceField(
        queryset=Satellite.objects.all(),
        label="Спутник",
        help_text="Спутник, к которому относится передатчик",
    )
    description = forms.CharField(
        label="Описание",
        help_text="Описание передатчика",
    )
    type = forms.ChoiceField(
        label="Тип", help_text="Тип передатчика", choices=TRANSMITTER_TYPES
    )
    status = forms.ChoiceField(
        label="Статус",
        help_text="Статус передатчика",
        choices=TRANSMITTER_STATUS,
    )
    modulation = forms.CharField(
        label="Модуляция",
        help_text="Модуляция передатчика",
    )
    upper_frequency_up = forms.FloatField(
        label="Верхняя частота наверх",
        help_text="Верхняя частота наверх передатчика",
        required=False,
    )
    lower_frequency_up = forms.FloatField(
        label="Нижняя частота наверх",
        help_text="Нижняя частота наверх передатчика",
        required=False,
    )
    upper_frequency_down = forms.FloatField(
        label="Верхняя частота вниз",
        help_text="Верхняя частота вниз передатчика",
        required=False,
    )
    lower_frequency_down = forms.FloatField(
        label="Нижняя частота вниз",
        help_text="Нижняя частота вниз передатчика",
        required=False,
    )
    baud_rate = forms.FloatField(
        label="Скорость передачи",
        help_text="Скорость передачи передатчика",
    )
    is_inverted = forms.BooleanField(
        label="Инверсия",
        help_text="Инверсия передатчика",
        required=False,
    )

    class Meta:
        model = Transmitter
        fields = [
            "satellite",
            "description",
            "status",
            "type",
            "modulation",
            "upper_frequency_up",
            "lower_frequency_up",
            "upper_frequency_down",
            "lower_frequency_down",
            "baud_rate",
            "is_inverted",
        ]


class TleForm(forms.ModelForm):
    satellite = forms.ModelChoiceField(
        queryset=Satellite.objects.all(),
        label="Спутник",
        help_text="Спутник, к которому относится TLE",
    )
    tle_0 = forms.CharField(
        label="TLE_0",
        help_text="Первая строка TLE",
    )
    tle_1 = forms.CharField(
        label="TLE_1",
        help_text="Вторая строка TLE",
    )
    tle_2 = forms.CharField(
        label="TLE_2",
        help_text="Третья строка TLE",
    )

    class Meta:
        model = Tle
        fields = ["satellite", "tle_0", "tle_1", "tle_2"]
