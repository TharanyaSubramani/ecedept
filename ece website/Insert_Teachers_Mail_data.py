from pymongo import MongoClient

# Replace the connection string with your MongoDB instance's connection string
client = MongoClient("mongodb://localhost:27017/")

# Access the 'ECE_DPT' database
db = client["ECE_DPT"]

# Access the 'teachers' collection
teachers_collection = db['teacher_mail_pass']

# Data to insert
teachers_data = [
    {
        "name": "Dr.N.Kasthuri",
        "email": "kasthuri@kongu.ac.in",
        "password": "kasthuri@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.T.Meeradevi",
        "email": "meeradevi@kongu.ac.in",
        "password": "meeradevi@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.P.Nirmala devi",
        "email": "nirmaladevi@kongu.ac.in",
        "password": "nirmaladevi@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.D.Malathi",
        "email": "malathy@kongu.ac.in",
        "password": "malathi@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.P.SivaRanjani",
        "email": "sivaranjani@kongu.ac.in",
        "password": "sivaranjani@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.S.Maheswaran",
        "email": "mmaheswaran_eie@kongu.ac.in",
        "password": "maheswaran@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.S.Sasikala",
        "email": "sasikalas@kongu.ac.in",
        "password": "sasikala@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.M. Joseph Auxilius Jude",
        "email": "jude@kongu.ac.in",
        "password": "josephauxiliusjude@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.J.Vijayalakshmi",
        "email": "vijayalakshmi@kongu.ac.in",
        "password": "vijayalakshmi@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.K.Senthil Kumar",
        "email": "ksenthilkumar@kongu.ac.in",
        "password": "senthilkumar@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.A.Arulmurugan",
        "email": "arul@kongu.ac.in",
        "password": "arulmurugan@ece",
        "usertype": "teacher"
    },
    {
        "name": "G.Deepa",
        "email": "g.deepa@kongu.ac.in",
        "password": "deepa@ece",
        "usertype": "teacher"
    },
    {
        "name": "N.S.Kavitha",
        "email": "nskavitha@kongu.ac.in",
        "password": "kavitha@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.K.ManojSenthil",
        "email": "kmanojsenthil@kongu.ac.in",
        "password": "manojsenthil@ece",
        "usertype": "teacher"
    },
    {
        "name": "A.Chandrasekaran",
        "email": "chandru@kongu.ac.in",
        "password": "chandrasekaran@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.K.KavinKumar",
        "email": "kavinkumar.ece@kongu.edu",
        "password": "kavinkumar@ece",
        "usertype": "teacher"
    },
    {
        "name": "Dr.V.C.Diniesh",
        "email": "vcdiniesh@kongu.ac.in",
        "password": "dinesh@ece",
        "usertype": "teacher"
    },
    {
        "name": "Vibin Mammen Vinod",
        "email": "vibin@kongu.ac.in",
        "password": "vibinmammenvinod@ece",
        "usertype": "teacher"
    },
    {
        "name": "V.Mekala",
        "email": "mekalav@kongu.ac.in",
        "password": "mekala@ece",
        "usertype": "teacher"
    },
    {
        "name": "B.Vivek",
        "email": "vivek.ece@kongu.ac.in",
        "password": "vivek@ece",
        "usertype": "teacher"
    },
    {
        "name": "V.Anbumani",
        "email": "anbumani.ece@kongu.ac.in",
        "password": "anbumani@ece",
        "usertype": "teacher"
    },
    {
        "name": "S.Preethi",
        "email": "preethi.s@kongu.ac.in",
        "password": "preethi@ece",
        "usertype": "teacher"
    },
    {
        "name": "A.Vennila",
        "email": "vennila.ece@kongu.ac.in",
        "password": "vennila@ece",
        "usertype": "teacher"
    },
    {
        "name": "S.Sathesh",
        "email": "sathesh.ece@kongu.ac.in",
        "password": "sathesh@ece",
        "usertype": "teacher"
    },
    {
        "name": "R.Ramyea",
        "email": "ramyea.ece@kongu.ac.in",
        "password": "ramyea@ece",
        "usertype": "teacher"
    },
    {
        "name": "S.Suthagar",
        "email": "suthagar.ece@kongu.ac.in",
        "password": "suthagar@ece",
        "usertype": "teacher"
    },
    {
        "name": "R.P.Karthik",
        "email": "rpkarthik.ece@kongu.ac.in",
        "password": "karthik@ece",
        "usertype": "teacher"
    },
    {
        "name": "G.Thirunavukkarasu",
        "email": "gthiru.ece@kongu.ac.in",
        "password": "thirunavukkarasu@ece",
        "usertype": "teacher"
    },
    {
        "name": "M.Pavithra",
        "email": "mpavithra.ece@kongu.ac.in",
        "password": "pavithra@ece",
        "usertype": "teacher"
    },
    {
        "name": "P.Pavithara",
        "email": "ppavithara.ece@kongu.ac.in",
        "password": "pavithara@ece",
        "usertype": "teacher"
    },
    {
        "name": "P.Gowri",
        "email": "gowri.ece@kongu.ac.in",
        "password": "gowri@ece",
        "usertype": "teacher"
    },
    {
        "name": "N.Indhumathi",
        "email": "indhumathi.ece@kongu.ac.in",
        "password": "indhumathi@ece",
        "usertype": "teacher"
    },
    {
        "name": "G.Sivapriya",
        "email": "sivapriya.ece@kongu.ac.in",
        "password": "sivapriya@ece",
        "usertype": "teacher"
    },
    {
        "name": "B.Swathi",
        "email": "swathi.ece@kongu.ac.in",
        "password": "swathi@ece",
        "usertype": "teacher"
    },
    {
        "name": "B.Banumithra",
        "email": "banumithra.ece@kongu.ac.in",
        "password": "banumithra@ece",
        "usertype": "teacher"
    },
    {
        "name": "M.Ramesh",
        "email": "ramesh.ece@kongu.ac.in",
        "password": "ramesh@ece",
        "usertype": "teacher"
    },
    {
        "name": "M. Ponkarthika",
        "email": "Ponkarthika.ece@kongu.ac.in",
        "password": "ponkarthika@ece",
        "usertype": "teacher"
    },
    {
        "name": "B.Abinaya",
        "email": "abinaya.ece@kongu.ac.in",
        "password": "abinaya@ece",
        "usertype": "teacher"
    }
]

# Insert data into the collection
teachers_collection.insert_many(teachers_data)

print("Data inserted successfully")
