{% extends 'base.tpl' %}
{% block title %}登陆{% endblock %}
{% block css_head %}

    <style type="text/css">
			.center {
  				width: auto;

  				margin-left: 300;
  				margin-right: auto;
  				margin-top: 50;
				}

		    body{ background-color:#FFE; }

		    .bg{ background-color:#FFF;}
	</style>


{% endblock %}
{% block body %}
        <div style="border:1" class="bg">
        <div class="center">
        <form action="{% url 'django.contrib.auth.views.login' %}" method="post" class="form-horizontal" role="form">
            {% csrf_token %}

        <div class="form-group">
            <label for="username" class="col-sm-2 control-label">username</label>
            <div class="col-sm-4">
            <input type="text" class="form-control" id="inputusername" placeholder="Username">
            </div>
         </div>

        <div class="form-group">
            <label for="inputPassword3" class="col-sm-2 control-label">Password</label>
            <div class="col-sm-4">
             <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
            </div>
         </div>


         <div class="form-group">
            <div class="col-sm-offset-2 col-sm-6">
            <div class="checkbox">
              <label>
                 <input type="checkbox"> Remember me
                 </label>
             </div>
            </div>
        </div>

         <div class="form-group">
            <div class="col-sm-offset-2 col-sm-4">
             <button type="submit" class="btn btn-primary">Sign in</button>
            </div>
         </div>

         </div>
         <div>
</form>



{% endblock %}