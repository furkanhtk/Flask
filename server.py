from flask import Flask,render_template
import views
from database import Database
from parameter import Parameter




def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/Measurement", view_func=views.Measurement_page)
    app.add_url_rule("/parameters", view_func=views.parameters_page, methods=["GET", "POST"])
    app.add_url_rule("/parameters/<int:parameter_key>", view_func=views.parameter_page)
    app.add_url_rule("/new-parameter", view_func=views.parameter_add_page, methods=["GET", "POST"])

    db = Database(r"C:\Users\Furkan\Desktop\Flask\parameters.sqlite")
    app.config["db"] = db


    return app




if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
    #app.run(host="0.0.0.0")
