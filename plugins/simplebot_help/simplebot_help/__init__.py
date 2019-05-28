# -*- coding: utf-8 -*-
import os

from simplebot import Plugin
from jinja2 import Environment, PackageLoader, select_autoescape
import htmlmin


class Helper(Plugin):

    name = 'Help'
    description = 'Provides this help page.'
    long_description = 'To learn more about a plugin press the <strong>"More"</strong> button, to use them press the <strong>"Use"</strong> button, you will be prompted to use an app, select to always open with Delta Chat, a command will be autocompleted for you, send it to process your request.'
    version = '0.2.0'
    author = 'adbenitez'
    author_email = 'adbenitez@nauta.cu'
    cmd = '!help'

    NOSCRIPT = 'You need a browser with JavaScript support for this page to work correctly.'
    MORE = 'More'
    LESS = 'Less'
    USE = 'Use'

    @classmethod
    def activate(cls, ctx):
        super().activate(ctx)
        cls.TEMP_FILE = os.path.join(cls.ctx.basedir, cls.name+'.html')
        env = Environment(
            loader=PackageLoader(__name__, 'templates'),
            #autoescape=select_autoescape(['html', 'xml'])
        )
        cls.template = env.get_template('index.html')
        if ctx.locale == 'es':
            cls.description = 'Provee esta página de ayuda.'
            cls.long_description = 'Para saber más acerca de un plugin presiona el botón <strong>"Más"</strong>, para usarlos presiona el botón <strong>"Usar"</strong>, selecciona abrir siempre con Delta Chat, un comando será autocompletado para ti, envíalo para procesar tu petición.'
            cls.NOSCRIPT = 'Necesitas un navegador que soporte JavaScript para poder usar esta funcionalidad.'
            cls.MORE = 'Más'
            cls.LESS = 'Menos'
            cls.USE = 'Usar'

    @classmethod
    def process(cls, msg):
        if cls.get_args(cls.cmd, msg.text) is not None:
            plugins = sorted(cls.ctx.plugins, key=lambda p: p.name)
            plugins.remove(cls)
            plugins.insert(0, cls)
            bot_addr = cls.ctx.acc.get_self_contact().addr
            html = cls.template.render(plugin=cls, plugins=plugins, bot_addr=bot_addr)
            html = htmlmin.minify(html, remove_comments=True)
            with open(cls.TEMP_FILE, 'w') as fd:
                fd.write(html)
            chat = cls.ctx.acc.create_chat_by_message(msg)
            chat.send_file(cls.TEMP_FILE, mime_type='text/html')
            return True
        return False
