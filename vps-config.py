import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "5162572062:AAEvGeB0qoU7y7E7Jei6Ow6Pw4Eq7RsunKs"
    APP_ID = 9844066
    API_HASH = "0d3f74056f1e60388d3317548799ee17"
    TG_USER_SESSION = "BQCASQT-Cd6Mku-9UzfinQCP7O5X36Sa7Fr-DImTFV7iXhFY1feE0Jjc84_VEzDpDzaDdQRfB-__KQbSJb2i7lQN3g13bwHbSe0PbmXToPv7SU1x0xUdQWEfUtGtZ-BR9zkCevyNEsjAkEy-6Xe8F9_tW2TeODApQ4RruVv4IuPLUwUCVqmbMUTUVihuGgGyuwXCRxoG2fCFpvkV-9ItypSjp-YEXNdJ_M9MLNV53D4exTNPjuaNjsXr3HY7jJ2nU1_AB7mvL4aD76Dix2YvXG5Cyo3HQ_4fB_Zgx0kX_LhAT-2D2ciNczgW61OMoVeD_DZ0HxpXeMdr7M7bloNOVB-iaYcCeAA"
    DB_URI = "postgresql://unverjl7agp8zwk8uxwi:5HHgyhQrZMjsIoif8vagcGIFpe0j3V@b1611fc2iiqr8f5lt4kc-postgresql.services.clever-cloud.com:5432/b1611fc2iiqr8f5lt4kc"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
