## Repository: {{repo}}

{% if page is not none %}   
Pull Request Page {{ page }}
{% else %}
List All Pull Requests
{% endif %}

| Num | Title | URL |
|-----|-------|-----|
{% for p in pulls -%}
|{{p.number}}|{{p.title|truncate(50, True) }}|{{p.url}}|
{% endfor -%}
