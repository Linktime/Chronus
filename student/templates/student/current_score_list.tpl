{% extends 'base.tpl' %}
{% block title %}本学期课程成绩列表{% endblock %}
{% block score_tag %}active{% endblock %}
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

        {% include 'student/score_table.tpl' %}

        <div class="row">
            <div class="col-md-2">平均成绩：{{avg_score}}</div>
        </div>

{% endblock %}