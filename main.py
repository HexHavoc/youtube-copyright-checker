from googleapiclient.discovery import build


class checker_api:
    def __init__(self):
        self.api_key = ""
        self.youtube_connector = build('youtube','v3',developerKey=self.api_key)
        self.url_input = input("Enter the url of the song:")
        self.maxResults = 50
        self.url_video_id = ''
        self.reference_video_title = ''
        self.url_video_tags = []

    def fetching_videoId_from_url(self):
        seperated_url = self.url_input.split('=')
        self.url_video_id = seperated_url[1]

    
    def searching_reference_video(self):
        request = self.youtube_connector.search().list(part='id', type='video', q=self.reference_video_title, maxResults=self.maxResults)
        response = request.execute()
        return response

    def url_copyright_checker(self):
        print()
        self.fetching_videoId_from_url()
        request = self.youtube_connector.videos().list(part='snippet,contentDetails', id=self.url_video_id)

        url_video_details = request.execute()

        self.reference_video_title = url_video_details['items'][0]['snippet']['title']

        self.url_video_tags = url_video_details['items'][0]['snippet']['tags']

        if(url_video_details['items'][0]['contentDetails']['licensedContent']):
            print(f"Title: {url_video_details['items'][0]['snippet']['title']} | ChannelName: {url_video_details['items'][0]['snippet']['channelTitle']} | Copyright: YES")

            print(f"The song {url_video_details['items'][0]['snippet']['title']} is copyrighted on youtube")
            print()
            
            print("***Since the given song is copyrighted on youtube we have some recommendations for the same song but which does not have any copyright issues***")
            print("\v")
            self.reccomendation_video_displayer()


        else:
            print(f"Title: {url_video_details['items'][0]['snippet']['title']} | ChannelName: {url_video_details['items'][0]['snippet']['channelTitle']} | Copyright: NO")

            print(f"The song {url_video_details['items'][0]['snippet']['title']} is copyright free on youtube")



    
    def getting_reference_video_details(self,video_id):
        request = self.youtube_connector.videos().list(part='snippet,contentDetails', id=video_id)
        details = request.execute()

        try:
            if(details['items'][0]['contentDetails']['licensedContent'] == False and self.reference_video_title in details['items'][0]['snippet']['title'] and self.url_video_tags in details['items'][0]['snippet']['tags']):
                print(f"* Title: {details['items'][0]['snippet']['title']} | ChannelName: {details['items'][0]['snippet']['channelTitle']} | Copyright: NO | URL: https://www.youtube.com/watch?v={details['items'][0]['id']}")
                print()

        except KeyError:
            print("OOPS SORRY NO TAGS FOUND FOR THIS ONE")


    def reccomendation_video_displayer(self):
        results = self.searching_reference_video()
        video_list=results['items']
        for i in range(len(video_list)):
            video_id=video_list[i]['id']['videoId']
            self.getting_reference_video_details(video_id)

    def main(self):
        self.url_copyright_checker()

        

check = checker_api()
check.main()
