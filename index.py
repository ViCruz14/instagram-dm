from time import sleep

from instapy import InstaPy, smart_run
from instapy.commenters_util import users_liked
from instapy.util import explicit_wait, web_address_navigator
from selenium.webdriver.common.by import By
from utilidade import mandar_dm, pegar_seguidores

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')
mensagem = input('Digite a mensagem que desenha enviar: ')

session = InstaPy(username=usuario,
                  password=senha, want_check_browser=False)

with smart_run(session):
    seguidores = pegar_seguidores(usuario, senha)

    confirmacao = input(
        f'Encontramos {len(seguidores)} perfis. Deseja continuar para o disparo? [s/n] ')

    if confirmacao == 's':
        for seguidor in seguidores:
            mandar_dm(session.browser, session.logger, seguidor, mensagem)
