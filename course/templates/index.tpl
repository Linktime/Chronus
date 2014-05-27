{% extends 'base.tpl' %}
{% block title %}选课须知{% endblock %}
{% block body %}
{% if user.is_teacher %}
        <pre>
            Balabala teacher
        </pre>
 {% else %}
        <pre>
             Balabala student
        </pre>
{% endif %}
{% endblock %}