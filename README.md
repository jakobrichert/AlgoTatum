# ALGOTATUM
 Algorand NFT Marketplace using Tatum API 


**************************WARNING THIS CODE IS NOT MEANT FOR PRODUCTION USAGE AND IS STILL A WORK IN PROGRESS****************************************


# Known Issues 

Due to the holidays and time crunch I experienced while working on this, there is not much of the backend completed while most of the frontend is completed. 

While working on this I learned a lot about tatum API calls and blockchain development in general and hope I can finish this even after the bounty has expired. '

NFT BUY AND SELL FEATURES ARE NOT WORKING AS INTENDED

USER MODEL NEEDS UPDATING WITH WALLET ADDRESS AND BALANCE AS WELL AS NFT COLLECTION

NOT VERY SAFE TO STORE KEYS ON DJANGO ADMIN PAGE, COULD USE TATUM KMS SERVICE AS A SUGGESTION

SOME TEMPLATES NEED TO BE UPDATED FOR SCALING AS WELL AS PLACEHOLDERS REMOVED

SOME LOGO ICONS NEED UPDATING

NEED TO CALL SMART CONTRACT CREATION USING TATUM API
# Gitcoin Bounty Link

Link: https://gitcoin.co/issue/algorandfoundation/grow-algorand/121/100027179


# Usage

YOU MUST ADD YOUR OWN API KEY IN THE tatum.py file located in env/algorandtatum/algorand




. bin/activate  while in the env directory 

cd algorandtatum/

python manage.py runserver

then navigate to http://localhost:8000/ in your web browser 






