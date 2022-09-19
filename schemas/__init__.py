from voluptuous import Schema, ALLOW_EXTRA

user_8 = Schema({
                "id": 8,
                "email": "lindsay.ferguson@reqres.in",
                "first_name": "Lindsay",
                "last_name": "Ferguson",
                "avatar": "https://reqres.in/img/faces/8-image.jpg"
            })

single_user = Schema({
    "data": user_8,
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
})

user1 = Schema({
    'name': 'Eugeny',
    'job': 'smetchik'
},
    extra=ALLOW_EXTRA,
    required=True
)

users_list = Schema({
    "page": 8,
    "per_page": 1,
    "total": 12,
    "total_pages": 12,
    "data": [user_8],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
})

