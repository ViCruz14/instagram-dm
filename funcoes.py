from time import sleep

from instagrapi import Client
from instapy.util import explicit_wait, web_address_navigator
from selenium.webdriver.common.by import By


def mandar_dm(browser,  logger,  conta, mensagem):
    web_address_navigator(browser, f"https://www.instagram.com/{conta}/")
    try:
        botao_seguir = browser.find_element(
            By.CSS_SELECTOR, '._acan._acap._acaq._acas')
        botao_seguir.click()

        botao_de_mensagem = explicit_wait(
            browser, 'VOEL', ['._acan._acap._acat', 'CSS'], logger, timeout=5)

        if botao_de_mensagem.get_attribute('innerText') != 'Requested':
            botao_de_mensagem.click()
            caixa_de_mensagem = explicit_wait(browser, 'VOEL', [
                '._abbh > textarea:nth-child(1)', 'CSS'], logger, timeout=5)
            caixa_de_mensagem.send_keys(mensagem)
            sleep(0.5)
            botao_enviar = browser.find_element(
                By.CSS_SELECTOR, 'div._abbi:nth-child(2) > button:nth-child(1)')
            botao_enviar.click()
            sleep(0.5)

    except:
        try:
            botao_de_mensagem = explicit_wait(
                browser, 'VOEL', ['._acan._acap._acat', 'CSS'], logger, timeout=5)
            if botao_de_mensagem.get_attribute('innerText') != 'Requested':
                botao_de_mensagem.click()
                caixa_de_mensagem = explicit_wait(browser, 'VOEL', [
                    '._abbh > textarea:nth-child(1)', 'CSS'],
                    logger, timeout=5)

                caixa_de_mensagem.send_keys(mensagem)
                sleep(0.5)
                botao_enviar = browser.find_element(
                    By.CSS_SELECTOR, 'div._abbi:nth-child(2) > button:nth-child(1)')
                botao_enviar.click()
                sleep(0.5)
        except:
            pass


def pegar_seguidores(usuario, senha):
    perfis = []
    cl = Client()
    cl.login(usuario, senha)

    user_id = cl.user_id_from_username(usuario)
    seguidores = cl.user_followers(user_id)

    for seguidor in seguidores.values():
        perfis.append(seguidor.username)

    return perfis
