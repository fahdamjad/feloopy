'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-06-02
 # @ Modified: 2023-06-02
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''
import rsome as rso
from rsome import dro

def generate_model(features):

    return dro.Model(name=features['model_name'],scens=features['scens'])


