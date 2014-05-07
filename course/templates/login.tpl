{% extends 'base.tpl' %}
{% block title %}登陆{% endblock %}
{% block body %}
        <form action="{% url 'django.contrib.auth.views.login' %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Login">
        </form>
{% endblock %}