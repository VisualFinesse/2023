from japplr import Japplr

my_searches = [
    {"keywords": "Software Engineer"},
    {"keywords": "test automation engineer"},
    {"keywords": "Full Stack Engineer"},
    {"keywords": "React Engineer"},
    {"keywords": "automation developer"},
    {"keywords": "python developer"},
    {"keywords": "Jr. Software Engineer"},
    {"keywords": "python programmer"},
    {"keywords": "database developer"},
    {"keywords": "sql programmer"},
    {"keywords": "Machine Learning Engineer"},
    {"keywords": ".NET developer"},
]

accounts = {
    "ziprecruiter": {
        "email": "foster@visualfinesse.com",
        "password": "P7SgJ@*njE$sM7&tl",
        "enabled": True,
    },
    "monster": {
        "email": "foster@visualfinesse.com",
        "password": "%lN2Z856FytpZ$E*",
        "enabled": True,
    },
}

j = Japplr(
    accounts=accounts,
    searches=my_searches,
    global_filters={"type": "full_time", "posteddaysago": 7},
)
j.login()
j.run(quantity_per_search=10, schedule_every_mins=15)
