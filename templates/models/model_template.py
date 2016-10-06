# -*- coding: utf-8 -*-
# Copyright {{ year }} {{ autor }} <{{ email_autor }}>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

# Imports habituales
{# Pongo v8 pero la condición puede ser otra #}
{% if v8 %}
from openerp import import api, fields, models
{% endif %}

{% for model in models %}
    {# Bucle para crear los modelos de la api v8#}
{% endfor %}

{% for modelv7 in modelsv7 %}
    {# Bucle para crear los modelos de la api v7 #}
{% endfor %}

{% for wizard in wizards %}
    {# Bucle para crear los wizards de la api v8#}
{% endfor %}
{% for memory in wizardsv7 %}
    {# Bucle para crear los wizards de la api v7, que son un asco#}
{% endfor %}
