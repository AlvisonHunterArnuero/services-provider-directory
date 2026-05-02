from main import app
from models import db, Provider, Review

def seed_data():
    with app.app_context():
        # Clear existing data just in case
        db.drop_all()
        db.create_all()

        # Add dummy providers
        providers_data = [
    {
        "name": "Alvison Hunter",
        "trade": "Senior Web Developer",
        "phone": "+505 8863 8751",
        "email": "alvison@gmail.com",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653422/starwars/ccl%20team/alvison_p3gvwd.png",  # generic dev portrait
        "location": "Carazo, Nicaragua",
        "experience_years": 16,
        "is_verified": True,
        "starting_rate": 25.0,
        "bio": "Senior Frontend Engineer specializing in React, Next.js, TypeScript, and Python. Experienced in headless CMS, API integrations, and building scalable web applications for global brands."
    },
    {
        "name": "Alexander Ruiz",
        "trade": "Software Engineer",
        "phone": "",  # not public; could leave empty or omit
        "email": "",  # not public; could leave empty or omit
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653419/starwars/ccl%20team/alex_jfz85j.png",  # generic engineer
        "location": "Carazo, Nicaragua",
        "experience_years": 9,
        "is_verified": True,
        "starting_rate": 22.0,
        "bio": "Software engineer with experience in industrial electronics, maintenance, and electrical installations. Works with complex systems and third‑party service coordination."
    },
    {
        "name": "Ernesto Gutierrez",
        "trade": "CTU Manager",
        "phone": "",
        "email": "",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653423/starwars/ccl%20team/tito_ksrqmh.png",  # generic manager
        "location": "Granada, Nicaragua",
        "experience_years": 12,
        "is_verified": True,
        "starting_rate":30.0,
        "bio": "CTU Manager focused on organizational transformation and infrastructure projects. Experienced in leading teams and partnerships that build large‑scale infrastructure with long‑term social impact."
    },
    {
        "name": "Patrick Cairolli",
        "trade": "Software Engineer",
        "phone": "",
        "email": "",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653421/starwars/ccl%20team/pat_sjcz9z.png",  # generic lawyer
        "location": "Managua, Nicaragua",
        "experience_years": 6,
        "is_verified": True,
        "starting_rate": 15.0,
        "bio": "Software Engineer working across Nicaragua and U.S. cases. Experienced in case coordination, documentation, and supporting clients through complex legal processes."
    },
    {
        "name": "Jean Cairolli",
        "trade": "Frontend Developer",
        "phone": "",
        "email": "",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653421/starwars/ccl%20team/papu_p7srlu.png",  # generic Frontend Developer
        "location": "Managua,Nicaragua",
        "experience_years": 7,
        "is_verified": True,
        "starting_rate": 15.0,
        "bio": "Fro helping institutions and students navigate academic pathways, curriculum development, and learning strategies through personalized consulting."
    },
    {
        "name": "Jorge Cruz",
        "trade": "Software Engineer",
        "phone": "",
        "email": "",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653421/starwars/ccl%20team/jorge_zs2rn9.png",  # generic dev
        "location": "Managua, Nicaragua",
        "experience_years": 7,
        "is_verified": True,
        "starting_rate": 15.0,
        "bio": "Software Engineer specializing in backend development with Java and related technologies. Passionate about building reliable and maintainable applications."
    },
    {
        "name": "Krystopher Rivera",
        "trade": "Software Developer",
        "phone": "",
        "email": "",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653420/starwars/ccl%20team/Krys_Ruiz_01_ykfjls.png",  # generic dev
        "location": "Carazo, Nicaragua",
        "experience_years": 4,
        "is_verified": True,
        "starting_rate": 12.0,
        "bio": "Software developer experienced with Angular, .NET, React, and Spring Boot. Builds scalable, user‑focused web and backend systems for diverse industries."
    },
    {
        "name": "Carlos Mondragon",
        "trade": "Full‑Stack Developer",
        "phone": "",
        "email": "",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653420/starwars/ccl%20team/carlos_ctpsut.png",  # generic coder
        "location": "Managua, Nicaragua",
        "experience_years": 3,
        "is_verified": True,
        "starting_rate": 13.0,
        "bio": "Full‑stack developer with strong experience in PHP, Laravel, MySQL, React, TypeScript, and Node.js. Builds end‑to‑end applications and modern web platforms."
    },
    {
        "name": "Bosco Granizo",
        "trade": "Engineering & Sourcing Leader",
        "phone": "",
        "email": "",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653420/starwars/ccl%20team/Juan_bosco_ddxyai.png",  # generic engineer leader
        "location": "Asuncion, Paraguay",
        "experience_years": 22,
        "is_verified": True,
        "starting_rate": 120.0,
        "bio": "Executive engineering and strategic sourcing leader with over 20+ years in the household appliances industry. Focuses on P&L leadership and cost‑impact initiatives."
    },
    {
        "name": "Jared Vilchez",
        "trade": "Software Engineer",
        "phone": "",
        "email": "",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653418/starwars/ccl%20team/jared_m9b6ma.png",  # generic coder
        "location": "Carazo, Nicaragua",
        "experience_years": 2,
        "is_verified": True,
        "starting_rate": 10.0,
        "bio": "Software engineer and mobile‑focused developer building web and mobile platforms that connect users with local service providers and home‑solutions marketplaces."
    }
]

        pro_objects = []
        for data in providers_data:
            pro = Provider(**data)
            db.session.add(pro)
            pro_objects.append(pro)

        db.session.commit()

        # Add some reviews
        reviews_data = [
    {"pro_id": pro_objects[0].id, "rating": 5, "comment": "Alvison was amazing! Super fast turnaround.", "ip_address": "127.0.0.1"},
    {"pro_id": pro_objects[0].id, "rating": 4, "comment": "Very professional, though a bit pricey.", "ip_address": "127.0.0.2"},
    {"pro_id": pro_objects[1].id, "rating": 5, "comment": "Alexander Ruiz delivered exactly what we needed. Highly recommend!", "ip_address": "127.0.0.3"},
    {"pro_id": pro_objects[2].id, "rating": 3, "comment": "Ernesto Gutierrez did the job, but communication could be better.", "ip_address": "127.0.0.4"},
    {"pro_id": pro_objects[3].id, "rating": 4, "comment": "Solid work by Patrick. He clearly knows his stuff.", "ip_address": "127.0.0.5"},
    {"pro_id": pro_objects[4].id, "rating": 5, "comment": "Jean Cairolli went above and beyond. Extremely satisfied!", "ip_address": "127.0.0.6"},
    {"pro_id": pro_objects[5].id, "rating": 2, "comment": "Jorge Cruz was late and the quality wasn't what I expected.", "ip_address": "127.0.0.7"},
    {"pro_id": pro_objects[6].id, "rating": 4, "comment": "Krystopher is very talented. Will definitely hire again.", "ip_address": "127.0.0.8"},
    {"pro_id": pro_objects[7].id, "rating": 5, "comment": "Best experience yet. Carlos Mondragon is a true professional.", "ip_address": "127.0.0.9"},
    {"pro_id": pro_objects[8].id, "rating": 4, "comment": "Bosco Granizo was great, just took a little longer than planned.", "ip_address": "127.0.0.10"},
    {"pro_id": pro_objects[9].id, "rating": 5, "comment": "Great attention to detail by Jared Vilchez. Five stars!", "ip_address": "127.0.0.11"}
        ]

        for r_data in reviews_data:
            review = Review(**r_data)
            db.session.add(review)

        db.session.commit()
        print("Successfully seeded the database with providers and reviews!")

if __name__ == "__main__":
    seed_data()
