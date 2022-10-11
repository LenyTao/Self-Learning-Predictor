from app.adder import adder
from app.extractor import cassandra_bd
from app.utils import conf_reader

from flask import Flask, render_template, request


def main():
    config = conf_reader.get_config_info(".")
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    @app.route('/', methods=['GET'])
    def index():
        return render_template("main_page.html")

    @app.route('/add_page', methods=['GET'])
    def show_add_page():
        return render_template("add_page.html")

    @app.route('/results_page', methods=['GET', 'POST'])
    def show_result():
        all_records = cassandra_bd.get_all_record_from(config)
        return render_template("result_page.html", records=all_records)

    @app.route('/sender_for_prediction', methods=['POST'])
    def send_kafka_for_prediction():
        adder.add_event_to_kafka(request, config, "input_event")
        return render_template("main_page.html")

    @app.route('/sender_for_learning', methods=['POST'])
    def remove_data_cassandra():
        adder.add_event_to_kafka(request, config, "learning_event")
        cassandra_bd.del_record_by_id(request.form["id_event"], config)
        return render_template("main_page.html")

    app.run(debug=False,host='0.0.0.0')
