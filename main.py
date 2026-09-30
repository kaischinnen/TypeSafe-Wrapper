import json
import os 


class JevLib:
    def __init__(self): 
            try:
                typesafe_api_key = os.environ['TYPESAFE_API_KEY']
            except KeyError:
                raise RuntimeError("Missing required environment variable: $TYPESAFE_API_KEY") from None
            else:
                self.TYPESAFE_API_KEY = typesafe_api_key



def main():
    jevlib = JevLib()
    
     
if __name__ == "__main__":
    main()
                 