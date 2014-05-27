{% extends 'base.tpl' %}
{% block title %}成绩总表{% endblock %}
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


        {% regroup courses by course.semester.begin_year as course_by_year %}
        {% for year_course in course_by_year %}
            {% regroup year_course.list by course.semester.get_season_display as course_by_semester %}
            {% for semester_course in course_by_semester %}
            <div class="row">
                <div class="col-md-2">{{year_course.grouper}}学年{{semester_course.grouper}}</div>
            </div>
            {% with courses=semester_course.list %}
                {% include "student/score_table.tpl" %}
            {% endwith %}
            {% endfor %}
        {% endfor %}

{% endblock %}