{% extends 'base.tpl' %}
{% block title %}课程列表{% endblock %}
{% block body %}
        {% for course in elected_course_list %}
        <p>{{course.course.course.name}}</p>
        {% endfor %}
{% endblock %}