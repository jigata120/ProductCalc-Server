import uuid
from django.utils.dateparse import parse_datetime

import uuid


def populate_users():
    data = {
        "35c62d76-8152-4626-8712-eeb96381bea8": {
            "name": "Pesho",
            "email": "peter@abv.bg",
            "password": "pesho123",
            "profile_url": "https://i.discogs.com/JiKwA9mIcucKXN_eKFaLPeJW8niDHkk4Pg-saH6r2nw/rs:fit/g:sm/q:40/h:300/w:300/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTYxMTI5/MC0xMzY4MjA3NzE5/LTkwMDYuanBlZw.jpeg",
            "role": "worker"
        },
        "847ec027-f659-4086-8032-5173e2f9c93a": {
            "name": "Gosho",
            "email": "george@abv.bg",
            "password": "sasasasa",
            "role": "worker"
        },
        "60f0cf0b-34b0-4abd-9769-8c42f830dffc": {
            "name": "Admin",
            "email": "admin@abv.bg",
            "password": "dadadada",
            "profile_url": "https://0.academia-photos.com/54504255/15234528/58504073/s200_luigi.finocchiaro.jpg",
            "role": "worker"
        },
        "60f0adw3-34b0-4abd-9769-8c42f830eeec": {
            "name": "Katia",
            "email": "katia@abv.bg",
            "password": "katia123",
            "profile_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2Yyb8V7OuCdcAjhRWIUKYYmgvH-ZFaOEdUw&s",
            "role": "admin"
        }
    }

    for user_id, user_data in data.items():
        try:
            # Validate and convert UUID
            user_uuid = uuid.UUID(user_id)
        except ValueError:
            print(f"Invalid UUID format: {user_id}")
            continue

        UserProfile.objects.update_or_create(
            id=user_uuid,
            defaults={
                'name': user_data.get('name'),
                'email': user_data.get('email'),
                'password': user_data.get('password'),  # Hash passwords in production
                'profile_url': user_data.get('profile_url'),
                'role': user_data.get('role')
            }
        )
    print('Successfully populated the UserProfile model')

if __name__ == "__main__":
    import django
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "React_Server.settings")
    django.setup()
from projects_data.models import Project, UserProfile

user = UserProfile.objects.first()
project = Project.objects.create(
    title="Test5 Project",
    final_product="Soap5",
    owner=user,
    table={
            "Values":{
                "Calcium":"mg",
                "Magnecium":"mg",
                "Celen":"mg",
                "Vitamin-B6":"mg",
                "Vitamin-B12":"mg",
            },
            "Products":{
                 "Carrot":{
                    "Calcium":101,
                    "Magnecium":23,
                    "Celen":15,
                    "Vitamin-B6":41,
                    "Vitamin-B12":55,
                },
                "Broccoli":{
                    "Calcium":51,
                    "Magnecium":0,
                    "Celen":200,
                    "Vitamin-B6":1,
                    "Vitamin-B12":55,
                },
                "Garlic":{
                    "Calcium":101,
                    "Magnecium":123,
                    "Celen":200,
                    "Vitamin-B6":761,
                    "Vitamin-B12":0,
                },
                "Carrot2":{
                    "Calcium":100,
                    "Magnecium":23,
                    "Celen":15,
                    "Vitamin-B6":41,
                    "Vitamin-B12":55,
                },

            }
        },
    picture_url="https://example.com/project-image.jpg"
)
# print(project)
from projects_data.models import UserProfile
UserProfile.objects.get(id='32fd8a5e-2735-425b-abf2-c137ecc856a4')
