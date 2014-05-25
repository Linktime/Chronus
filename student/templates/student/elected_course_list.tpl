{% extends 'base.tpl' %}
{% block title %}课程列表{% endblock %}
{% block elected_course_tag %}active{% endblock %}
{% block body %}
        {% if messages %}
        {% for message in messages %}
            <div class="alert fade in alert-block alert-{{ message.tags }}">
            <button type="button" class="close" data-dismiss="alert">×</button>
                {{ message }}
            </div>
        {% endfor %}
        {% endif %}

        <div class="row">
            <div class="col-md-2">已选科目：{{user.studentinfo.get_course_count}}门</div>
            <div class="col-md-2">已选学分：{{user.studentinfo.get_credit}}分</div>
        </div>
        <form action="{% url 'student_cancel_elected' %}" method="post">
        {% csrf_token %}
        {% include 'student/elected_course_table.tpl' %}
        <button type="submit" class="btn btn-danger">退课</button>
        </form>

        {% include 'student/elected_course_grid.tpl' %}
{% endblock %}