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
          <li><a href="{% url 'open_course_list' %}">选课</a></li>
          <li><a href="{% url 'student_elected_course' %}">课表查询</a></li>
        </ul>
        <form class="navbar-form navbar-left" role="search" action="{% url 'open_course_list' %}">
          <div class="input-group">
            <input type="text" class="form-control" name="course_name" placeholder="课程名">
            <span class="input-group-btn"><button type="submit" class="btn btn-default">查询</button></span>
          </div>

        </form>
        {% if user.is_authenticated %}
        <ul class="nav navbar-nav navbar-right">
          <li><a href="#">{{user.username}}</a></li>
          <li>
            <a href="{% url 'logout' %}">注销</a>
          </li>
        </ul>
        {% endif %}
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