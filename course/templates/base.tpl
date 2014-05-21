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
        <a class="navbar-brand" href="#">上海大学选课系统</a>
      </div>

      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <li><a href="#">选课</a></li>
          <li><a href="#">课表查询</a></li>
        </ul>
        <form class="navbar-form navbar-left" role="search">
          <div class="input-group">
            <input type="text" class="form-control" placeholder="课程名">
            <span class="input-group-btn"><button type="submit" class="btn btn-default">查询</button></span>
          </div>

        </form>
        <ul class="nav navbar-nav navbar-right">
          <li><a href="#">{{user.identifier}}</a></li>
          <li>
            <a href="#">注销</a>
          </li>
        </ul>
      </div><!-- /.navbar-collapse -->
    </nav>


    {% block body %}{% endblock %}
    <script type="text/javascript" src="{{STATIC_URL}}js/jquery.min.js"></script>
    <script type="text/javascript" src="{{STATIC_URL}}js/bootstrap.min.js"></script>
    {% block js_footer %}{% endblock %}
</body>
</html>