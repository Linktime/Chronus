{% extends "base.tpl" %}
{% block title %}课程信息{% endblock %}
{% block body %}
        {% for course in courses %}
        <p>{{course.name}}</p>
        {% endfor %}
{% endblock %}