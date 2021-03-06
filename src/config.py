class Spbx(object):
    spbx_timer = "spbx_timer"


class Ledt(object):
    ledt_amount = "ledt_amount"
    ledt_less_than = "ledt_less_than"
    ledt_operator = "ledt_operator"
    ledt_item_num = "ledt_item_num"
    ledt_decimal = "ledt_decimal"
    ledt_score = "ledt_score"
    ledt_correct_rate = "ledt_correct_rate"
    ledt_score_all = "ledt_score_all"
    ledt_correct_rate_all = "ledt_correct_rate_all"


class Chkb(object):
    chkb_decimal = "chkb_decimal"


class Btn(object):
    btn_generate = "btn_generate"


class Others(object):
    main_window_title = "不知道起啥名字"
    config_args = {
        Chkb.chkb_decimal: False,
        Ledt.ledt_decimal: 0,
        Ledt.ledt_amount: 10,
        Ledt.ledt_less_than: 20,
        Ledt.ledt_item_num: 2,
        Spbx.spbx_timer: 0,
        Ledt.ledt_operator: ['+', '-']

    }


class Txe(object):
    txe_about = "txe_about"
    about = '''
        <p>---{}---</p>
        <p align:center >‘不知道叫什么名字’ 小组特别出品</p>
        <p>作者：刘彦龙、何婧源、白汝冰</p>
        <p>编程：刘彦龙</p>
        <p>界面设计：何婧源、白汝冰</p>
        <p>专业：2016级水文与水资源工程</p>
        <p>Github: <a href='https://github.com/rainyl'>https://github.com/rainyl</p>
    '''.format(Others.main_window_title)


