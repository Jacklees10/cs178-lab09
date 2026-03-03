import boto3
from boto3.dynamodb.conditions import Attr

REGION = "us-east-1"
TABLE_NAME = "MLB_Players"

def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_movie(player):
    name = player.get("Name", "Unknown Name")
    hr = player.get("HR", "Unknown HRs")
    rbi = player.get("RBI", "Unknown RBIs")
    print(f"  Name : {name}")
    print(f"  HRs  : {hr}")
    print(f"  RBI  : {rbi}")

def print_all_players():
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])
    if not items:
        print("No players found.")
        return
    print(f"Found {len(items)} player(s):\n")
    for player in items:
        print_movie(player)

def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_players()

if __name__ == "__main__":
    main()