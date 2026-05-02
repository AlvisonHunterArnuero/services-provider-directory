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
        "trade": "Senior Product Engineer",
        "phone": "+505 8863 8751",
        "email": "alvison@gmail.com",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653422/starwars/ccl%20team/alvison_p3gvwd.png",
        "location": "Carazo, Nicaragua",
        "experience_years": 16,
        "is_verified": True,
        "starting_rate": 25.0,
        "bio": "Senior Product Engineer specializing in Next.js, AI-powered SaaS platforms, and scalable workflow systems. Experienced with React, TypeScript, Node.js, PostgreSQL, Python, and Go."
    },
    {
        "name": "Alexander Ruiz",
        "trade": "Full-Stack Developer",
        "phone": "",
        "email": "ralexs.acu@gmail.com",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653419/starwars/ccl%20team/alex_jfz85j.png",
        "location": "Carazo, Nicaragua",
        "experience_years": 9,
        "is_verified": True,
        "starting_rate": 18.0,
        "bio": "Full-Stack Developer focused on JavaScript, TypeScript, React, and Node.js applications. Experienced in database design, custom software, and modern web development."
    },
    {
        "name": "Ernesto Gutierrez",
        "trade": "Full-Stack Developer",
        "phone": "50581886845",
        "email": "eblind39@hotmail.com",
        "linkedIn_url":"https://www.linkedin.com/in/ernesto-gutierrez-ergchrvs/",
        "github_url": "https://github.com/",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653423/starwars/ccl%20team/tito_ksrqmh.png",
        "location": "Granada, Nicaragua",
        "experience_years": 12,
        "is_verified": True,
        "starting_rate": 20.0,
        "bio": "Full-Stack Developer experienced with React, TypeScript, C#/.NET, Java, and JavaScript ecosystems. Builds scalable web applications and enterprise software solutions."
    },
    {
        "name": "Patrick Cairoli",
        "trade": "Full-Stack JavaScript Developer",
        "phone": "",
        "email": "patrick.cairoli@gmail.com",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653421/starwars/ccl%20team/pat_sjcz9z.png",
        "location": "Managua, Nicaragua",
        "experience_years": 6,
        "is_verified": True,
        "starting_rate": 15.0,
        "bio": "Full-Stack JavaScript Developer working with React, Express, and PostgreSQL applications. Passionate about building efficient web platforms and learning new technologies."
    },
    {
        "name": "Jean Cairoli",
        "trade": "Full-Stack Web Developer",
        "phone": "",
        "email": "jcairoli1993@gmail.com",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653421/starwars/ccl%20team/papu_p7srlu.png",
        "location": "Managua,Nicaragua",
        "experience_years": 7,
        "is_verified": True,
        "starting_rate": 15.0,
        "bio": "Full-Stack Web Developer experienced with React, Next.js, Vue, Node.js, Gatsby, and micro-frontends. Focused on creating innovative, scalable, and user-centered digital solutions."
    },
    {
        "name": "Jorge Cruz",
        "trade": "Backend Web Developer",
        "phone": "",
        "email": "jorcrus2@gmail.com",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653421/starwars/ccl%20team/jorge_zs2rn9.png",
        "location": "Managua, Nicaragua",
        "experience_years": 7,
        "is_verified": True,
        "starting_rate": 10.0,
        "bio": "Backend Web Developer specializing in Laravel, Symfony, PHP, and JavaScript applications. Experienced in HubSpot HubL modules, themes customization, and scalable web systems."
    },
    {
        "name": "Krysthopher Rivera",
        "trade": "Full-Stack Developer",
        "phone": "",
        "email": "krysthopher@gmail.com",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653420/starwars/ccl%20team/Krys_Ruiz_01_ykfjls.png",
        "location": "Carazo, Nicaragua",
        "experience_years": 4,
        "is_verified": True,
        "starting_rate": 12.0,
        "bio": "Full-Stack Developer experienced in React, Next.js, Node.js, GraphQL, MongoDB, and TypeScript. Passionate about web development, mentorship, and delivering high-quality solutions."
    },
    {
        "name": "Carlos Mondragon",
        "trade": "Full-Stack Developer",
        "phone": "",
        "email": "cema962002@gmail.com",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653420/starwars/ccl%20team/carlos_ctpsut.png",
        "location": "Managua, Nicaragua",
        "experience_years": 3,
        "is_verified": True,
        "starting_rate": 13.0,
        "bio": "Full-Stack Developer specializing in React, Next.js, TypeScript, NestJS, and FastAPI applications. Builds modern, accessible, and scalable web platforms with clean UI architecture."
    },
    {
        "name": "Bosco Granizo",
        "trade": "Senior PHP & Ecommerce Developer",
        "phone": "",
        "email": "mayorgagranizo@gmail.com",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653420/starwars/ccl%20team/Juan_bosco_ddxyai.png",
        "location": "Asuncion, Paraguay",
        "experience_years": 22,
        "is_verified": True,
        "starting_rate": 40.0,
        "bio": "Senior PHP & Ecommerce Developer experienced with Laravel, Symfony, WordPress, Shopify, and Prestashop. Specialized in ecommerce platforms, web scraping, and custom web solutions."
    },
    {
        "name": "Jared Vilchez",
        "trade": "Frontend Web Developer",
        "phone": "",
        "email": "jared.zvo@gmail.com",
        "photo_url": "https://res.cloudinary.com/alvison-hunter/image/upload/v1777653418/starwars/ccl%20team/jared_m9b6ma.png",
        "location": "Carazo, Nicaragua",
        "experience_years": 2,
        "is_verified": True,
        "starting_rate": 10.0,
        "bio": "Frontend Web Developer skilled in React.js, TypeScript, GraphQL, and Material UI. Builds responsive interfaces with modern frontend technologies and clean user experiences."
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
