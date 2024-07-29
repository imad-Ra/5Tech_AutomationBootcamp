from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium.pom.herokuapp.infra.basepage import BasePage


class BasePageApp(BasePage):
    ELEMENTAL_SELENIUM = '//div[@style="text-align: center;"]'
    FORK_IN_GITHUB = '//img[@alt="Fork me on GitHub"]'
    ADD_REMOVE_ELEMENTS = '//a[text()="Add/Remove Elements"]'
    BASIC_AUTH = '//a[text()="Basic Auth"]'
    BROKEN_IMAGES = '//a[text()="Broken Images"]'
    CHALLENGING_DOM = '//a[text()="Challenging DOM"]'
    CHECKBOXES = '//a[text()="Checkboxes"]'
    CONTEXT_MENU = '//a[text()="Context Menu"]'
    DIGEST_AUTHENTICATION = '//a[text()="Digest Authentication"]'
    DISAPPEARING_ELEMENTS = '//a[text()="Disappearing Elements"]'
    DRAG_AND_DROP = '//a[text()="Drag and Drop"]'
    DROPDOWN = '//a[text()="Dropdown"]'
    DYNAMIC_CONTENT = '//a[text()="Dynamic Content"]'
    DYNAMIC_CONTROLS = '//a[text()="Dynamic Controls"]'
    DYNAMIC_LOADING = '//a[text()="Dynamic Loading"]'
    ENTRY_AD = '//a[text()="Entry Ad"]'
    EXIT_INTENT = '//a[text()="Exit Intent"]'
    FILE_DOWNLOAD = '//a[text()="File Download"]'
    FILE_UPLOAD = '//a[text()="File Upload"]'
    FLOATING_MENU = '//a[text()="Floating Menu"]'
    FORGOT_PASSWORD = '//a[text()="Forgot Password"]'
    FORM_AUTHENTICATION = '//a[text()="Form Authentication"]'
    FRAMES = '//a[text()="Frames"]'
    GEOLOCATION = '//a[text()="Geolocation"]'
    HORIZONTAL_SLIDER = '//a[text()="Horizontal Slider"]'
    HOVERS = '//a[text()="Hovers"]'
    INFINITE_SCROLL = '//a[text()="Infinite Scroll"]'
    INPUTS = '//a[text()="Inputs"]'
    JQUERY_UI_MENUS = '//a[text()="JQuery UI Menus"]'
    JAVASCRIPT_ALERTS = '//a[text()="JavaScript Alerts"]'
    JAVASCRIPT_ONLOAD_EVENT_ERROR = '//a[text()="JavaScript onload event error"]'
    KEY_PRESSES = '//a[text()="Key Presses"]'
    LARGE_AND_DEEP_DOM = '//a[text()="Large & Deep DOM"]'
    MULTIPLE_WINDOWS = '//a[text()="Multiple Windows"]'
    NESTED_FRAMES = '//a[text()="Nested Frames"]'
    NOTIFICATION_MESSAGES = '//a[text()="Notification Messages"]'
    REDIRECT_LINK = '//a[text()="Redirect Link"]'
    SECURE_FILE_DOWNLOAD = '//a[text()="Secure File Download"]'
    SHADOW_DOM = '//a[text()="Shadow DOM"]'
    SHIFTING_CONTENT = '//a[text()="Shifting Content"]'
    SLOW_RESOURCES = '//a[text()="Slow Resources"]'
    SORTABLE_DATA_TABLES = '//a[text()="Sortable Data Tables"]'
    STATUS_CODES = '//a[text()="Status Codes"]'
    TYPOS = '//a[text()="Typos"]'
    WYSIWYG_EDITOR = '//a[text()="WYSIWYG Editor"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)

    def fork_in_github(self):
        return self._click_element(self.FORK_IN_GITHUB)

    def add_remove_elements(self):
        return self._click_element(self.ADD_REMOVE_ELEMENTS)

    def basic_auth(self):
        return self._click_element(self.BASIC_AUTH)

    def broken_images(self):
        return self._click_element(self.BROKEN_IMAGES)

    def challenging_dom(self):
        return self._click_element(self.CHALLENGING_DOM)

    def checkboxes(self):
        return self._click_element(self.CHECKBOXES)

    def context_menu(self):
        return self._click_element(self.CONTEXT_MENU)

    def digest_authentication(self):
        return self._click_element(self.DIGEST_AUTHENTICATION)

    def disappearing_elements(self):
        return self._click_element(self.DISAPPEARING_ELEMENTS)

    def drag_and_drop(self):
        return self._click_element(self.DRAG_AND_DROP)

    def dropdown(self):
        return self._click_element(self.DROPDOWN)

    def dynamic_content(self):
        return self._click_element(self.DYNAMIC_CONTENT)

    def dynamic_controls(self):
        return self._click_element(self.DYNAMIC_CONTROLS)

    def dynamic_loading(self):
        return self._click_element(self.DYNAMIC_LOADING)

    def entry_ad(self):
        return self._click_element(self.ENTRY_AD)

    def exit_intent(self):
        return self._click_element(self.EXIT_INTENT)

    def file_download(self):
        return self._click_element(self.FILE_DOWNLOAD)

    def file_upload(self):
        return self._click_element(self.FILE_UPLOAD)

    def floating_menu(self):
        return self._click_element(self.FLOATING_MENU)

    def forgot_password(self):
        return self._click_element(self.FORGOT_PASSWORD)

    def form_authentication(self):
        return self._click_element(self.FORM_AUTHENTICATION)

    def frames(self):
        return self._click_element(self.FRAMES)

    def geolocation(self):
        return self._click_element(self.GEOLOCATION)

    def horizontal_slider(self):
        return self._click_element(self.HORIZONTAL_SLIDER)

    def hovers(self):
        return self._click_element(self.HOVERS)

    def infinite_scroll(self):
        return self._click_element(self.INFINITE_SCROLL)

    def inputs(self):
        return self._click_element(self.INPUTS)

    def jquery_ui_menus(self):
        return self._click_element(self.JQUERY_UI_MENUS)

    def javascript_alerts(self):
        return self._click_element(self.JAVASCRIPT_ALERTS)

    def javascript_onload_event_error(self):
        return self._click_element(self.JAVASCRIPT_ONLOAD_EVENT_ERROR)

    def key_presses(self):
        return self._click_element(self.KEY_PRESSES)

    def large_and_deep_dom(self):
        return self._click_element(self.LARGE_AND_DEEP_DOM)

    def multiple_windows(self):
        return self._click_element(self.MULTIPLE_WINDOWS)

    def nested_frames(self):
        return self._click_element(self.NESTED_FRAMES)

    def notification_messages(self):
        return self._click_element(self.NOTIFICATION_MESSAGES)

    def redirect_link(self):
        return self._click_element(self.REDIRECT_LINK)

    def secure_file_download(self):
        return self._click_element(self.SECURE_FILE_DOWNLOAD)

    def shadow_dom(self):
        return self._click_element(self.SHADOW_DOM)

    def shifting_content(self):
        return self._click_element(self.SHIFTING_CONTENT)

    def slow_resources(self):
        return self._click_element(self.SLOW_RESOURCES)

    def sortable_data_tables(self):
        return self._click_element(self.SORTABLE_DATA_TABLES)

    def status_codes(self):
        return self._click_element(self.STATUS_CODES)

    def typos(self):
        return self._click_element(self.TYPOS)

    def wysiwyg_editor(self):
        return self._click_element(self.WYSIWYG_EDITOR)

    def _click_element(self, xpath):
        element = self._wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()