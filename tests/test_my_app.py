from app import app

def test_app_is_up_and_running():
    with app.test_client() as c:
        request = c.post('/predict', json={"CHAS":{  
          "0":0.0
       },
       "RM":{  
          "0":6.575
       },
       "TAX":{  
          "0":296.0
       },
       "PTRATIO":{  
          "0":15.3
       },
       "B":{  
          "0":396.9
       },
       "LSTAT":{  
          "0":4.98
       }})

        status = request.status_code
        
        assert status == 200


def test_prediction():
    with app.test_client() as c:
        request = c.post('/predict', json={"CHAS":{  
          "0":0.0
       },
       "RM":{  
          "0":6.575
       },
       "TAX":{  
          "0":296.0
       },
       "PTRATIO":{  
          "0":15.3
       },
       "B":{  
          "0":396.9
       },
       "LSTAT":{  
          "0":4.98
       }})
    
        prediction = request.get_json()['prediction'][0]

        assert prediction == 20.35373177134412


