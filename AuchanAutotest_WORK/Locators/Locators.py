#!/usr/bin/python
# -*- coding: utf-8 -*-

class Locators:
    """Локаторы"""


    """Локаторы страницы авторизации"""
    authorization_tab_xpath = "//section[2]/div/section/header/div[1]"
    registration_tab_xpath = "//section/header/div[2]"
    wrong_password_message = "li[class='error-msg'] span"
    wrong_password_message_text = "Неверный логин или пароль. Проверьте, пожалуйста."
    mail_input_wrong_password_name = 'email'
    subscribe_input_name = "subscribe"
    subscribe_btn_id = "news-subscribe-btn"
    subscribe_modal_id = "news-subscribe-modal"
    modal_subsbribe_overlay_id = "auchan-modal-overlay"
    login_email_id = "login-email"
    login_password_id = "login-password"
    submit_button = "div[class='logreg__btns'] button[type='submit']"
    forgot_password_link = "div[class='logreg__forget'] a"
    modal_window_send_password_id = "auchan-modal-container"
    submit_button_forgot_password_xpath = '//*[@id="form-forgot-password"]/div[2]/button'

    """Локаторы страницы регистрации"""
    first_name_id = "firstname"
    email_registration_id = "email"
    password_id = "password"
    password_confirmation_id = "confirm_password"
    agry_checkbox_xpath = '//*[@id="register-form"]/fieldset[6]/div/label'
    registration_button_xpath = '//*[@id="register-form"]/div/button'
    captcha_xpath = '//*[@id="recaptcha3"]'

    """Локаторы страницы личного кабинета"""
    mail_in_account = "tr[class='d']"
    logo =  "strong[class='logo']" #препрод "span[class='header__logo']"
    log_out_xpath = "//ul/li[2]/a/span"
    mail_after_registration_xpath = '//*[@id="main"]//tbody/tr[3]/th'

    """Локаторы главной страницы"""
    city_current_xpath = '//*[@id="product_region_name_container"]/span/span/span'
    city_list_xpath = '//*[@id="city_popup_container"]//fieldset[3]/div/label'
    city_search_xpath = '//*[@id="city_swap"]/div[2]/div/input[1]'
    city_search_list_element_xpath = '//*[@id="search_autocomplete"]/li'
    input_city_name_name = 'typecity1'
    logout_main_page = "div[class='header__logged-name']"
    account_page_link = 'div[class="header__logged-name"]'
    login_button = 'div[class="account-popup__login"] button[class="btn.btn--red.js-account-login-trigger"]'
    search_name = 'q'
    cart_xpath = '//*[@id="header_cart_widget_block"]/div/section[1]/div/a'
    main_menu_list_xpath ='/html/body/div[1]/div/section[1]/div/section/nav/ul/li'
    main_menu_element_xpath = '/html/body/div[1]/div/section[1]/div/section/nav/ul/li/div[1]/a/span[2]'#'/html/body/div[1]/div/section[1]/div/section/nav/ul/li'
    price_mainpage = "span[class='price-val']"
    price_rr = 'span[class="retailrocket-item-price-value"]'
    footer_links = 'footer[class="footer"] li[class="footer-col__submenu_item"] a'

    """Локаторы виджета корзины"""
    price_product_in_vidget = '#header_cart_widget_block > div > section.cart-popup-section > div:nth-child(2) > div > div > section > ul > li > div > div.cart-popup__price > div.price > span.cart-popup__price-val.price-val'
    price_total_in_v_cart = "#header_cart_widget_block > div > section.cart-popup-section > div:nth-child(2) > div > div > header > div.cart-popup__total > span.cart-popup__total-price.cart-total-price"
    price_close_vidget = "#header_cart_widget_block > div > section.header_cart_icon_wrapper > div > a"

    """Локаторы страницы корзины"""
    button_continue_xpath = '//*[@id="cart_widget_block"]//button'
    loader = "div[id='ajaxloader_container']"
    price_product_in_cart = "div[class='current-price'] span[class='price-val']"
    price_total_in_cart ='div[class="basket__summup-col1"] span[class="price-val"]'

    """Локаторы страницы чекаута"""
    delivery_to_home_tab_xpath = '//*[@id="delivery_details_block"]/ul/li[1]'
    delivery_to_shop_tab_xpath = '//*[@id="delivery_details_block"]/ul/li[2]'
    express_delivery_checkbox_xpath = '//*[@id="delivery_details_block"]/div/div[1]/div[1]/div[2]/div[3]/div/label'
    shop_xpath = '//*[@id="delivery_details_block"]/div/div[2]/div/div[1]/div[2]/div/div[1]/ul/li/h6/em'
    to_2th_level_checkout_button_xpath = '//*[@id="checkout_widget_block"]//button'
    text_area_xpath = '//*[@id="checkout_widget_block"]/div[2]/div[2]/div/ul/li[3]/div/textarea'
    payment_on_receipt = '//*[@id="checkout-pay-list"]/div[2]/ul/li[3]/div/div[1]'
    payment_on_receipt2 = 'div[class="checkout__pay-item-title"]'
    confirm_pay_button_xpath = '//*[@id="checkout-pay-list"]/div[2]/div[2]/button'
    address_checkbox = 'label[for="address_1"]'
    price_on_checkout = "div[class='current-price'] span[class='price-val']"
    price_promocode = '#checkout_widget_block > div.checkout__order.checkout__order--promocode.checkout__promocode > div.checkout__order-body > div.checkout__promocode-col.checkout__promocode-col--total > ul > li.content_list__item.checkout__promocode-content_list-item3 > div.content_list__item-rt > div > span.price-val'

    """Локаторы страницы каталога"""
    catalog2_level = 'div[class="category__item-title"] a'
    #body > div.page > div > section.main-content > div > section > ul > li:nth-child(1) > div > div > div.category__item-title > a
    product_item_list = 'article[class="products__item"]'

    """Локаторы страницы товара"""
    add_to_cart_button_xpath = '//*[@id="product_addtocart_form"]//button[1]'
    no_stock_massage = 'div[class="ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-draggable.ui-resizable"]'
    subscribe_product_massage = 'span[class="btn--subscribe-to-item__before.btn-txt__before"]'
    self_delivery_blok_xpath = '//*[@id="product_view_block_container"]/article/section[1]/div[2]/div[2]/div/div[3]/div[2]'
    price_product_cart = 'div[class="prcard-current-price current-price"] span[class="price-val"]'

    """Локаторы success page"""
    thank_block_header = 'h2[class="thank-block__header"]'
    order_id_xpath = '//strong/a'
    logout_link_xpath = '//*[@id="header_login_widget_block"]/section[2]/div/div/a'
                        #'//*[@id="header"]/div[1]/div[3]/div[1]/div[4]/ul/li[2]/a' #логаут из ЛК
    logout_link_fail_xpath = '//*[@id="header_login_widget_block"]/section[2]/div/div/a'

    """Локаторы страницы онлайн оплаты"""
    order_price ='body > div.po-wrapper > div > div > div.po-order-summary > table > tbody > tr:nth-child(2) > td:nth-child(2)'
    delivery_price = 'span[id="shipping_total_price"]'
    grand_total_price = 'span[id="grand_total_price"]'
