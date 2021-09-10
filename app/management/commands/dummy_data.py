import logging
import random
import string

import requests
from datetime import datetime, timedelta

from django.conf import settings
from django.core.management.base import BaseCommand

from app.models import *
from app.constants import *

logger = logging.getLogger(__name__)

from random import randint

import names

class Command(BaseCommand):
    help = """This script adds QA users to non production environments. It is part of VIKI-4371."""

    def handle(self, *args, **options):
        tags=["html","css","java", "aws", "azure", "tech", "career"]
        company = ["amazon", "tcs", "cts", "tsteps", "groupon","orderofn", "google"]
        job_title = ["intern", "software developer", "manager", "SDM", "CTO", "Vice president", "Director Of Engg"]
        interests = ["cricket", "football", "table tennis", "hacking", "browsing", "tv", "netflix"]
        # goal_list = ["Learning", "Train", "Catchup", "Review"]
        # for i in range(0,25):
        #     user = TUser.objects.create_user(
        #         username=f"random@{i}.com",
        #         email=f"random@{i}.com",
        #         first_name=f"User {i}",
        #         last_name="Doe",
        #     )
        #
        #     mentor = Mentor.objects.create(
        #         position=list(POSITIONS._db_values)[i%5],
        #         tags= [ tags[randint(0,6)], tags[randint(0,6)], tags[randint(0,6)] ],
        #     )
        #     user.mentor = mentor
        #
        #     mentee =  Mentee.objects.create(
        #         tags=[tags[randint(0, 6)], tags[randint(0, 6)], tags[randint(0, 6)]],
        #         about_you = "John Doe John Doe"
        #     )
        #     user.mentee = mentee
        #     user.set_password("ash")
        #     user.save()
        #
        #     for i in range(1, 4):
        #         goal = Goal.objects.create(
        #             text = f"{tags[randint(0,6)]} {goal_list[randint(0,3)]}",
        #             description = f"{tags[randint(0,6)]} {goal_list[randint(0,3)]}",
        #             mentee = mentee,
        #             tags=[tags[randint(0, 6)], tags[randint(0, 6)], tags[randint(0, 6)]],
        #         )
        #
        #     mentors = Mentor.objects.all()
        #     goals = Goal.objects.filter(mentee = mentee)
        #     now = datetime.now()
        #
        #     for i in range(1, 4):
        #         start_time = now + timedelta(hours=randint(1,100))
        #         end_time = start_time + timedelta(minutes=30)
        #         meeting = Meeting.objects.create(
        #             mentee = mentee,
        #             mentor = random.choice(mentors),
        #             goal=random.choice(goals),
        #             start_time = start_time,
        #             end_time = end_time,
        #             meeting_link = f"http://zoomus.com?join={randint(99999,99999999)}"
        #         )

        for i in range(0,10):
            name = names.get_full_name().lower()
            input = {
                "basic": {
                    "displayName": name,
                    "firstName": name.split(" ")[0],
                    "lastName": name.split(" ")[1],
                    "photoUrl": "https://picsum.photos/200",
                    "public": True,
                    "phoneNumber": f"{randint(91912345678, 91999999999)}",
                    "countryCode": "+91",
                    "phoneNumberVerified": False,
                    "address": "chennai",
                    "description": f"{name} description",
                    "latestCompany": company[ randint(0,6)] ,
                    "latestJobtitle":job_title[ randint(0,6)] ,
                    "currentlyEmployed": False,
                    "hasExperience": False,
                    "email": f"{name.split(' ')[0]}@orderofn.com",
                    "firebaseUid": ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
                    "emailVerified": False,
                    "disabled": False,
                    "createdAt": "2021-05-25T14:25:59.006Z",
                    "updatedAt": "2021-05-25T14:25:59.006Z"
                },
                "education": [
                    {
                        "description": "college",
                        "currentlyStudying": False,
                        "grade": "string",
                        "degree": "B Tech",
                        "specialization": "Computer Science",
                        "school": "Anna University",
                    }
                ],
                "experience": [
                    {
                        "description": "string",
                        "company": company[ randint(0,6)] ,
                        "jobtitle": job_title[ randint(0,6)] ,
                        "jobtype": "full-time",
                        "startDate": "2021-05-25",
                        "endDate": "2021-05-25",
                        "currentlyWorking": True
                    },
                    {
                        "description": "string",
                        "company": company[randint(0, 6)],
                        "jobtitle": job_title[randint(0, 6)],
                        "jobtype": "full-time",
                        "startDate": "2021-05-25",
                        "endDate": "2021-05-25",
                        "currentlyWorking": True
                    },
                    {
                        "description": "string",
                        "id": 0,
                        "company": company[randint(0, 6)],
                        "jobtitle": job_title[randint(0, 6)],
                        "jobtype": "full-time",
                        "startDate": "2021-05-25",
                        "endDate": "2021-05-25",
                        "currentlyWorking": True
                    }
                ],
                "languages": [
                    {
                        "level": "beginner",
                        "language": "English"
                    },
                    {
                        "level": "advanced",
                        "language": "Hindi"
                    }
                ],
                "interests": [ interests[randint(0, 6)], interests[randint(0, 6)], interests[randint(0, 6)],   ],
                "skills": [ tags[randint(0, 6)], tags[randint(0, 6)], tags[randint(0, 6)],  ],
                "certificates": [
                    {
                        "credentialId": "string",
                        "credentialUrl": "string",
                        "issuedDate": "2021-05-25",
                        "expiryDate": "2021-05-25",
                        "canExpire": True,
                        "id": 0,
                        "certificate": {
                            "name": "string",
                            "id": 0,
                            "organization": {
                                "name": "string",
                                "id": 0
                            }
                        }
                    }
                ],
                "projects": [
                    {
                        "name": "string",
                        "description": "string",
                        "company": {
                            "name": "string",
                            "id": 0
                        },
                        "coverImage": {
                            "url": "string",
                            "title": "string",
                            "type": "string",
                            "id": 0
                        },
                        "skills": [
                            {
                                "name": "string",
                                "id": 0
                            }
                        ],
                        "links": [
                            {
                                "url": "string",
                                "title": "string",
                                "id": 0
                            }
                        ],
                        "id": 0
                    }
                ],
                }
            print(input['basic']['email'])
            result = requests.post("http://127.0.0.1:8000/tsprings/", json=input)