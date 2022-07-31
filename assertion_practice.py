from playwright.sync_api import Playwright, sync_playwright,expect
import pdb




def assertion_practice(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    ''' assertとexpectの違い
    assert: 期待値に対しての結果をすぐに返す。　※ 画面遷移時間などを考慮できない。
    expect: 期待値に対しての結果をタイムアウトまで待つことができる。 (タイムアウトまで繰り返し、結果を探し続ける。)
    '''

    assert page.is_visible("text='Celebrating Beauty and Style'")    # assertは、期待したものと外れた場合に例外を発生させてくれる。
    expect(page.locator("text='Celebrating Beauty and Style'")).to_be_visible()   # timeout時間も設定できる。

    page.wait_for_timeout(5000)
    page.locator("button:has-text(\"Log In\")").click() # timeout時間を設定できる。この要素だけ、デフォルトタイムアウトを上書きできる。
    page.locator("[data-testid='signUp.switchToSignUp']:has-text('Log In')").click() # timeout時間を設定できる。この要素だけ、デフォルトタイムアウトを上書きできる。

    page.locator("text='Log in with Email'").click()
    page.locator("[data-testid=\"emailAuth\"] >> input[type=\"email\"]").click()
    page.locator("[data-testid=\"emailAuth\"] >> input[type=\"email\"]").fill("bar@gmail.com")
    page.locator("input[type=\"password\"]").click()
    page.locator("input[type=\"password\"]").fill("bar")
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()

    page.wait_for_selector("[aria-label='foo account menu']")
    assert page.is_visible("[aria-label=\"foo account menu\"]")
    page.locator("[aria-label=\"foo account menu\"]").click()


    #pdb.set_trace()




with sync_playwright() as playwright:
    assertion_practice(playwright)