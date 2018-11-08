# -*- coding:utf-8 -*-

from flask import flash, redirect, url_for, render_template

from SayHello import db, app
from SayHello.models import Message
from SayHello.forms import HelloForm


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body) # 实例化模型
        db.session.add(message)
        db.session.commit()
        flash('Your message have sent to the world!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)