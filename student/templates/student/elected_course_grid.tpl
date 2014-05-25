        <table class="table table-bordered">
            <thead>
                <tr>
                    <th class="col-md-1 warning">节次</th>
                    <th class="col-md-2 warning">一</th>
                    <th class="col-md-2 warning">二</th>
                    <th class="col-md-2 warning">三</th>
                    <th class="col-md-2 warning">四</th>
                    <th class="col-md-2 warning">五</th>
                </tr>
            </thead>
            <tbody>
            {% for hour in week %}
                <tr>
                    <td class="warning">{{forloop.counter}}</td>
                    <td class="{% if hour.一 %}success{% endif %}">{{hour.一}}</td>
                    <td class="{% if hour.二 %}success{% endif %}">{{hour.二}}</td>
                    <td class="{% if hour.三 %}success{% endif %}">{{hour.三}}</td>
                    <td class="{% if hour.四 %}success{% endif %}">{{hour.四}}</td>
                    <td class="{% if hour.五 %}success{% endif %}">{{hour.五}}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>