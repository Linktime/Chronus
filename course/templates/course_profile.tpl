{% extends 'base.tpl' %}
{% block body %}
{% if ocourse %}
<table class="table">
    <tr>
        <td>课程号</td>
        <td>{{ ocourse.course.course_num }}</td>
        <td>学分</td>
        <td>{{ ocourse.course.credit }}</td>
    </tr>
    <tr>
        <td>学期</td>
        <td>{{ ocourse.course.semester.semester }}</td>
        <td>学院</td>
        <td>{{ ocourse.course.department.name }}</td>
    </tr>
    <tr>
        <td>教师</td>
        <td>{{ ocourse.teacher.name }}</td>
        <td>容量</td>
        <td>{{ ocourse.elected_count }}/{{ ocourse.capacity }}</td>
    </tr>

    <tr>
        <td colspan="4">上课地点与时间</td>
    </tr>
    <tr>
        <td colspan="4">{{ ocourse.place }}&nbsp;&nbsp;{{ ocourse.time }}</td>
    </tr>

    <tr>
        <td colspan="4">简介</td>
    </tr>
    <tr>
        <td colspan="4">{{ ocourse.course.course_intro }}</td>
    </tr>

    <tr>
        <td colspan="4">详情</td>
    </tr>
    <tr>
        <td colspan="4">{{ ocourse.course.course_detail }}</td>
    </tr>


    <tr>
        <td colspan="4">教学信息</td>
    </tr>
    <tr>
        <td colspan="4">{{ ocourse.information }}</td>
    </tr>
</table>
{% else %}
    <h3>此课不存在</h3>
{% endif %}
{% endblock %}