{% extends 'base.tpl' %}
{% block title %}课程列表{% endblock %}
{% block body %}
        {% if messages %}
        {% for message in messages %}
            <div class="alert fade in alert-block alert-{{ message.tags }}">
            <button type="button" class="close" data-dismiss="alert">×</button>
                {{ message }}
            </div>
        {% endfor %}
        {% endif %}

        <form action="{% url 'cancel_elected' %}" method="post">
        {% csrf_token %}
        {% include 'student/elected_course_table.tpl' %}
        <button type="submit" class="btn btn-danger">退课</button>
        </form>

        {% include 'student/elected_course_grid.tpl' %}
{% endblock %}