from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
import os

dataviz = Flask(__name__)


@dataviz.route('/')
def home():
    return render_template('index.html')


# if __name__ == '__main__':
#     dataviz.run()

