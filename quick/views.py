import dateutil.parser
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import traceback
from datetime import *

class TwitterApi(APIView):
    #Getting a user data using twitter username
    def get(self, request, id):
        
        try:
            #profile data counts
            profile_score = 0
            
            url = "https://api.twitter.com/2/users/by/username/"+id+"?user.fields=created_at,description,id,location,name,profile_image_url,public_metrics"

            payload={}
            headers = {
            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFgufgEAAAAAA5spA0KzLrUJtHnOE94bwA9HUm4%3DJCERp6jG9FxY1ltSwg2GmdZLvriiEjjkhgtMoq0JlloeMTk9qV',
            'Cookie': 'guest_id=v1%3A166859839150441292; guest_id_ads=v1%3A166859839150441292; guest_id_marketing=v1%3A166859839150441292; personalization_id="v1_4EA2POUUWCvMY/J41wErYA=="'
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            json_response = (response.json())
            print(json_response)
            #using len because of its dynamics content 
            '''example : some profile not have a description or profile_pic'''
            print(json_response)
            if len(json_response['data']['description']) !=0:
                profile_score += 10
            if len(json_response['data']['profile_image_url']) !=0:
                profile_score += 10
            location = (json_response['data']['location'])
            # if location == True:
            #     profile_score += 10
            if len(location) != 0 :
                profile_score += 10
            else:
                profile_score += 0
                
            followers =(json_response['data']['public_metrics']['followers_count'])
            if followers >= 3000:
                profile_score += 20
            elif followers >= 1000:
                profile_score += 10

            user_join=(json_response['data']['created_at'])
            b = dateutil.parser.isoparse(user_join)
            date_joined = b.strftime("%Y-%m-%d")
            a = datetime.today() - datetime.strptime(date_joined, "%Y-%m-%d")
            joined = a.days / 365
            if joined >= 5 :
                profile_score += 20
            elif joined >= 1:
                profile_score += 10

            tweets = (json_response['data']['public_metrics']['tweet_count'])
            total = a.days * 2400
            print(total)
            if (total/4) <= tweets:
                profile_score += 30
            elif (total/10) <= tweets:
                profile_score += 20
            elif ((total/10)/2) <= tweets:
                profile_score += 10
            return Response({"YOUR PROFILE SCORE ", profile_score})

        except Exception:
            return Response(traceback.format_exc(), status = status.HTTP_400_BAD_REQUEST)
