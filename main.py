from googleapiclient.discovery import build

class checker_api:
    def __init__(self):
        self.api_key = ""
        self.youtube_connector = build('youtube','v3',developerKey=self.api_key)
        self.query = input("Enter your query:")
        self.maxResults = 5
        self.response_count = 1

    
    def searching_video(self):
        request = self.youtube_connector.search().list(part='id', type='video', q=self.query, maxResults=self.maxResults)
        response = request.execute()
        return response
    
    def getting_video_details(self,video_id):
        request = self.youtube_connector.videos().list(part='snippet,contentDetails', id=video_id)
        details = request.execute()
        if(details['items'][0]['contentDetails']['licensedContent']):
            print(f"{self.response_count}. Title: {details['items'][0]['snippet']['title']} | ChannelName: {details['items'][0]['snippet']['channelTitle']} | Copyright: YES | URL: https://www.youtube.com/watch?v={details['items'][0]['id']}")

        else:
            print(f"{self.response_count}. Title: {details['items'][0]['snippet']['title']} | ChannelName: {details['items'][0]['snippet']['channelTitle']} | Copyright: NO | URL: https://www.youtube.com/watch?v={details['items'][0]['id']}")

    def main(self):
        results = self.searching_video()
        video_list=results['items']
        for i in range(len(video_list)):
            video_id=video_list[i]['id']['videoId']
            self.getting_video_details(video_id)
            self.response_count += 1
            print()
        

check = checker_api()
check.main()
