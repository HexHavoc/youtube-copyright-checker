
from googleapiclient.discovery import build



class checker_api:
    def __init__(self):
        self.api_key = ""
        self.youtube_connector = build('youtube','v3',developerKey=self.api_key)
        self.query = input("Enter your query:")
        self.maxResults = 5

    
    def searching_video(self):
        request = self.youtube_connector.search().list(part='id', type='video', q=self.query, maxResults=self.maxResults)
        response = request.execute()
        print(response)
        return response
    
    def getting_video_details(self,video_id):
        request = self.youtube_connector.videos().list(part='contentDetails', id=video_id)
        details = request.execute()
        print(details['items'][0]['contentDetails']['licensedContent'])

    def main(self):
        results = self.searching_video()
        video_list=results['items']
        for i in range(len(video_list)):
            video_id=video_list[i]['id']['videoId']
            self.getting_video_details(video_id)
        

check = checker_api()
check.main()
