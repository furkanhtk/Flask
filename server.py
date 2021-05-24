from flask import Flask,render_template
import views



# <meta http-equiv="refresh" content="1" >

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/Measurement", view_func=views.Measurement_page)
    app.add_url_rule("/parameters", view_func=views.parameters_page, methods=["GET", "POST"])
    app.add_url_rule("/parameters/<int:parameter_id>", view_func=views.parameter_page)
    app.add_url_rule("/test", view_func=views.test, methods=["GET", "POST"])
    app.add_url_rule("/data", view_func=views.data, methods=["GET", "POST"])
    return app




if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port, use_reloader=False)
    #app.run(host="0.0.0.0")
