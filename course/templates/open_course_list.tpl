{% extends "base.tpl" %}
{% block title %}本学期已开课程{% endblock %}
{% block body %}
        {% for open_course in open_courses %}
        <p>{{open_course.course.name}}</p>
        {% endfor %}
{% endblock %}