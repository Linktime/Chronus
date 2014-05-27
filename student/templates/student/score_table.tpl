        <table class="table table-hover">
            <thead>
                <tr><th>课程号</th><th>课程名</th><th>任课教师</th><th>平时成绩</th><th>考试成绩</th><th>总成绩</th></tr>
            </thead>
            <tbody>
                {% for elected_course in courses %}
                {% with open_course=elected_course.course %}
                <tr>
                    <td>{{open_course.course.course_num}}</td>
                    <td>{{open_course.course.name}}</td>
                    <td>
                        {% for teacher in open_course.teacher.all %}
                            {{teacher.name}}&nbsp;
                        {% endfor %}
                    </td>
                    <td>{{elected_course.usual_score}}</td>
                    <td>{{elected_course.exam_score}}</td>
                    <td>{{elected_course.score}}</td>
                </tr>
                {% endwith %}
                {% endfor %}
            </tbody>
        </table>