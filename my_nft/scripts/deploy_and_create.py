from scripts.helpful_scripts import get_account, SimpleCollectible 
sample_token_uri = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"

def main():
   account=get_account() 
   simple_collectible =SimpleCollectible.deploy({"from":account})
   tx = simple_collectible.createCollectible(sample_token_uri,{"from:account"})
   tx.wait(1)
   print(
      f"awesome,you can now veiw at{OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() -1)}"
      )
   print("please wait up tp 20 mins, and hit the refresh metadata button")