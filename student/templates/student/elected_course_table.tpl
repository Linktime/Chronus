        <table class="table table-hover">
            <thead>
                <tr><th></th><th>课程号</th><th>课程名</th><th>任课教师</th><th>地点</th><th>上课时间</th><th>容量</th></tr>
            </thead>
            <tbody>
                {% for elected_course in elected_course_list %}
                {% with open_course=elected_course.course %}
                <tr>
                    <td><input type="checkbox" name="open_course" value="{{open_course.id}}"></td>
                    <td>{{open_course.course.course_num}}</td>
                    <td>{{open_course.course.name}}</td>
                    <td>
                        {% for teacher in open_course.teacher.all %}
                            {{teacher.name}}&nbsp;
                        {% endfor %}
                    </td>
                    <td>{{open_course.place}}</td>
                    <td>{{open_course.time}}</td>
                    <td>{{open_course.elected_count}}/{{open_course.capacity}}</td>
                </tr>
                {% endwith %}
                {% endfor %}
            </tbody>
        </table>