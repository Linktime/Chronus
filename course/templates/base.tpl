<html>
<head>
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{{STATIC_URL}}css/bootstrap.min.css">
    {% block css_head %}{% endblock %}



</head>
<body>


    <nav class="navbar navbar-default" role="navigation">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="{% url 'index' %}">上海大学选课系统</a>
      </div>

      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
        {% if user.is_teacher %}
          <li><a href="">teacher</a></li>
        {% else %}
          <li class="{% block open_course_tag %}{% endblock %}"><a href="{% url 'open_course_list' %}">选课</a></li>
          <li class="{% block elected_course_tag %}{% endblock %}"><a href="{% url 'elected_course' %}">课表查询</a></li>
          <li class="dropdown {% block score_tag %}{% endblock %}"><a href="#" class="dropdown-toggle" data-toggle="dropdown">成绩<b class="caret"></b></a>
        {% endif %}
            <ul class="dropdown-menu">
                <li><a href="{% url 'current_score' %}">本学期成绩</a></li>
                <li><a href="{% url 'score' %}">成绩总表</a></li>
            </ul>
          </li>
        </ul>
        {% if user.is_student %}IntellijIdeaRulezzz
        <form class="navbar-form navbar-left" role="search" action="{% url 'open_course_list' %}">
          <div class="input-group">
            <input type="text" class="form-control" name="course_name" placeholder="课程名">
            <span class="input-group-btn"><button type="submit" class="btn btn-default">快速查询</button></span>
          </div>
        </form>
        {% endif %}
        <ul class="nav navbar-nav navbar-right">
          {% if user.is_authenticated %}
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">{{user.username}}<b class="caret"></b></a>
            <ul class="dropdown-menu">
              {% if user.is_teacher %}
              <li><a href="#">学院：{{user.teacherinfo.department.name}}</a></li>
              <li><a href="#">姓名：{{user.name}}</a></li>
              {% else %}
              <li><a href="#">学院：{{user.studentinfo.department.name}}</a></li>
              <li><a href="#">姓名：{{user.name}}</a></li>
              {% endif %}
            </ul>
          </li>
          <li>
            <a href="{% url 'logout' %}">注销</a>
          </li>
          {% else %}
          <li><a href="{% url 'login' %}">登陆</a></li>
          {% endif %}
        </ul>
      </div><!-- /.navbar-collapse -->
    </nav>

    <div class="container">
        {% block body %}{% endblock %}
    </div>
    <script type="text/javascript" src="{{STATIC_URL}}js/jquery.min.js"></script>
    <script type="text/javascript" src="{{STATIC_URL}}js/bootstrap.min.js"></script>
    {% block js_footer %}{% endblock %}
</body>
</html>