{% extends "base.tpl" %}
{% block body %}
<table class="table">
{% for course in courses %}
<tr>
    <td>{{course.course.course_num}}</td>
    <td><a href="{{course.get_url}}" target="_blank">{{course.course.name}}</a></td>
    <td>{{course.time}}</td>
    <td>{{course.place}}</td>
    <td>{{course.semester.semester}}</td>
    <td>{{course.elected_count}}/{{course.capacity}}</td>

    <td>
    {% if course.is_current %}
    <a href="{{course.get_modify_url}}">登分</a>
    {% endif %}
    </td>
</tr>
{% endfor %}
</table>
{% endblock %}