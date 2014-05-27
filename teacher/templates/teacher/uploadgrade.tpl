{% extends "base.tpl" %}
{% block body %}
<h3><a href="{{ ocourse.get_url}}" target="_blank">{{ ocourse.course.name }}</a> 成绩登记表</h3>
<form method="post" action="{% url "uploadgrade" ocourse.id %}">
{% csrf_token %}
{{ formset.management_form }}
<table class="table">
<tr>
    <td>学号</td>
    <td>学生姓名</td>
    <td>平时成绩</td>
    <td>考试成绩</td>
    <td>总评成绩</td>
</tr>
{% for form in formset %}
    <tr>
    {% for field in form %}
        {% if field.is_hidden %}
        {{ field }}
        {% else %}
        <td>{{ field }} <span style="color: red">{{ field.error }}</span></td>
        {% endif %}
    {% endfor %}
    </tr>
{% endfor %}
</table>
<br />
<table>
{{ ratioform }}
</table>

<br />
<button class="btn btn-primary">submit</button>
</form>
{% endblock %}