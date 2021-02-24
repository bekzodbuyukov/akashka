from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Engine:
    ''' Engine Class for Player '''

    def __init__(self, video_url) -> None:
        ''' Class Initialization '''
        # needed video url
        self.video_url = video_url

        # setting Chrome Driver
        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        
        # launching chrome in new windows with tab where given url opened
        self.driver.get(video_url)
        
        # getting movie player of youtube to make actions with it
        self.video = self.driver.find_element_by_id('movie_player')
        
        # auto starting video
        self.video.send_keys(Keys.SPACE)
        
        # video paused status
        self.paused = False
    
    def play(self):
        ''' Function for Playing Video '''
        if self.paused:
            self.video.send_keys(Keys.SPACE)
            self.paused = False

    def pause(self):
        ''' Function for Pausing Video '''
        if not self.paused:
            self.video.send_keys(Keys.SPACE)
            self.paused = True
    
    def stop(self):
        '''
        Function for Stopping Video
        P.S.: Closes opened Chrome in New window
        '''
        self.driver.quit()
    
    def next(self):
        ''' Function for Switching to Next Video '''
        next_video_element = self.driver.find_element_by_css_selector(
            'a.ytp-next-button.ytp-button'
        )
        
        next_video_url = next_video_element.get_attribute('href')

        self.driver.get(next_video_url)

        self.video = self.driver.find_element_by_id('movie_player')
        self.video.send_keys(Keys.SPACE)


        # for video in next_video:
        #     print(video.get_attribute('href'))
        #     if video.get_attribute('title') == 'Next (SHIFT+n)':
        #         next_video_url = video.get_attribute('href')

        # action = ActionChains(self.driver)
        # action.click(on_element=next_video)
        # self.driver.send_keys(Keys.END)
    
    def replay(self):
        ''' Function for Replying Video '''
        self.video.send_keys(Keys.END)
        self.video.send_keys(Keys.SPACE)

    def increase_volume(self):
        ''' Function for Increasing Video's Volume '''
        self.video.send_keys(Keys.UP)
    
    def decrease_volume(self):
        ''' Function for Decreasing Video's Volume '''
        self.video.send_keys(Keys.DOWN)
