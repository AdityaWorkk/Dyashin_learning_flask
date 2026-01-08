from flask import Flask, render_template,redirect,url_for
import requests

# Flask automatically looks for a "templates" folder, 
# so 'template_folder="templates"' is correct but usually optional.
app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    # 1. Re-activate your variables
    var_a = 10
    lis = [10, 20, 30, 40, 50]
    
    # 2. You MUST pass the variables into the render_template function
    # Syntax: template_variable_name = local_python_variable
    return render_template("template.html", var_a = var_a, lis=lis)    #html_variable_name = flask_variable_name 


#extends and {% block content%} {% endblock %}
@app.route("/greet")
def greet():
    return render_template("2_greetings.html")



#Filters
@app.route("/filters")
def filters():
    filter_var = "Hello world"
    return render_template("3_filters.html", filter_var = filter_var)  

@app.template_filter("reverse_sting")     #Custom filter
def reveres_sting(filter_var):
    return filter_var[::-1]

@app.template_filter("repeat")
def repeat(filter_var, times = 2):         #If the html didn't return any element we will use default times as 2
    repeated = filter_var * times
    return repeated + " "

@app.template_filter("alternate_letters")
def alternate_filter(filter_var):
    return "".join([c.upper() if i%2==0 else c.lower() for i,c in enumerate(filter_var)])


#Redirecting with dynamic urls
@app.route("/redirect_to_filters")
def redirect_to_filters():
    return redirect(url_for("filters"))   #We directly pass in the function name insted of the URL



if __name__ == "__main__":
    # 3. Added port=5000 explicitly for clarity
    app.run(host="0.0.0.0", port=5000, debug=True)

