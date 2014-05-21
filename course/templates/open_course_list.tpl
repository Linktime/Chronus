{% extends "base.tpl" %}
{% block title %}本学期已开课程{% endblock %}
{% block body %}

        {% if messages %}
        {% for message in messages %}
            <div class="alert fade in alert-block alert-{{ message.tags }}">
            <button type="button" class="close" data-dismiss="alert">×</button>
                {{ message }}
            </div>
        {% endfor %}
        {% endif %}

        <form action="{% url 'elected_course' %}" method="post">
            {% csrf_token %}
            {% include 'open_course_table.tpl' %}
            <button type="submit" class="btn btn-success">选课</button>
        </form>

        {% if is_paginated %}
        <div>
            <ul class="pagination pagination-centered">
                {% if page_obj.has_previous %}
                <li><a href="?page={{ page_obj.previous_page_number }}">«</a></li>
                {% endif %}
                {% for page in page_obj.paginator.page_range %}
                <li><a href="?page={{page}}">{{page}}</a></li>
                {% endfor %}
                {% if page_obj.has_next %}
                <li><a href="?page={{ page_obj.next_page_number }}">»</a></li>
                {% endif %}
                <li><a>第{{ page_obj.number }} 页/ 共{{ page_obj.paginator.num_pages }}页</a></li>
            </ul>
        </div>
        {% endif %}
{% endblock %}