import pdb
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False, slow_mo=500) #slow_moはこのインスタンスを使うかくステップで0.5秒停止時間を入れている。
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(20000)

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.locator("button:has-text(\"Log In\")").click(timeout=5000) # timeout時間を設定できる。この要素だけ、デフォルトタイムアウトを上書きできる。



    ''' htmlの要素から抽出する手法。
    page.locator("text=shop").click()   # text=shop はshopがtextに含まれるものすべてを取得してくる。
    page.locator("text='shop'").click()   # text='shop' は完全にtextがshopと完全に一致している要素を取得してくる。
    page.locator("p")                                         # pタブを取得。複数ある場合は、最初に取得した要素が対象となる。
    page.locator("button:visible")                            # buttonタブの、css要素がvisibleのもの。
    page.locator(":nth-match(:text('shop'),1)").click()       # 1番目にマッチした要素を取得。
    page.locator(":nth-match(:text('shop'),2)").click()       # 2番目にマッチした要素を取得。
    '''

    ''' デザイン的な位置関係から抽出する手法 (所感: デバイスや画面サイズによって変化がありそうだし、あまり信用できない。)   
    page.locator("button:below(:text('Email'))")        # textがEmailの要素の下側に見えるボタン
    page.locator("button:above(:text('Email'))")        # textがEmailの要素の上側に見えるボタン
    page.locator("button:right-of(:text('Email'))")     # textがEmailの要素の右側に見えるボタン
    page.locator("button:left-of(:text('Email'))")      # textがEmailの要素の左側に見えるボタン
    page.locator("button:near(:text('Email'))")         # textがEmailの要素の近くに見えるボタン
    '''

    ''' DOM階層の用いた抽出手法  
    page.locator("[data-testid=\"switchToEmailLink\"] >> [data-testid=\"buttonElement\"]").click()　　#「>>」を使って子階層を指定できる。
    page.locator("[data-testid=\"switchToEmailLink\"] >> .. ).click()                                #「..」親の階層を指定できる。    
    '''
    
    # page.locator("button:has-text(\"Log In\")").click(timeout=5000)

    page.locator("text=\"Log In\"").click()
    pdb.set_trace()
    page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
    page.locator("[data-testid=\"switchToEmailLink\"] >> [data-testid=\"buttonElement\"]").click()
    page.locator("[data-testid=\"emailAuth\"] >> input[type=\"email\"]").click()
    page.locator("[data-testid=\"emailAuth\"] >> input[type=\"email\"]").fill("bhkbb0551@gmail.com")
    pdb.set_trace()
    page.locator("input[type=\"password\"]").click()
    page.locator("input[type=\"password\"]").fill("aaaaa")
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()
    page.locator("[aria-label=\"bhkbb0551 account menu\"]").click()

    #TODO: assertとexpectの違いは？
    assert page.is_visible("text=My Orders")
    pdb.set_trace()
    page.locator("a:has-text(\"My Orders\")").click()
    page.wait_for_url("https://symonstorozhenko.wixsite.com/website-1/account/my-orders")
    # ---------------------


    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
