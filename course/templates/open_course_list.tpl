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

        <form action="{% url 'elected_course' %}" method="post" role="form">
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

        <form class="form-horizontal" method="get" action="{% url 'open_course_advanced_search' %}" role="form">
            <fieldset>
                <legend>高级查询</legend>
            <div class="form-group">
                <label class="control-label col-md-2" for="id_course_num">课程号</label>
                <div class="col-md-3">
                    <input id="id_course_num" name="course_num" class="form-control" placeholder="课程号">
                </div>
            </div>
            <div class="form-group">
                <label class="control-label col-md-2" for="id_course_name">课程名</label>
                <div class="col-md-3">
                    <input id="id_course_name" name="course_name" class="form-control" placeholder="课程名">
                </div>
            </div>
            <div class="form-group">
                <label class="control-label col-md-2" for="id_course_teacher">教师名</label>
                <div class="col-md-3">
                    <input id="id_course_teacher" name="course_teacher" class="form-control" placeholder="教师名">
                </div>
            </div>
            <div class="form-group">
                <label class="control-label col-md-2" for="id_course_time">上课时间</label>
                <div class="col-md-3">
                    <input id="id_course_time" name="course_time" class="form-control" placeholder="例如：一11-12">
                </div>
            </div>
                <button class="btn btn-default">查询</button>
            </fieldset>
        </form>
{% endblock %}