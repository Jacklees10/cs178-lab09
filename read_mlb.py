import boto3
from boto3.dynamodb.conditions import Attr

REGION = "us-east-1"
TABLE_NAME = "MLB_Players"

def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_movie(player):
    """Print a single movie's details in a readable format."""
    name = player.get("Name", "Unknown Name")
    hr = player.get("HR", "Unknown HRs")
    rbi = player.get("RBI", "Unknown RBIs")
    # rating_str = ", ".join(f"{k}: {v}" for k, v in ratings.items()) if ratings else "No ratings"

    print(f"  Name : {name}")
    print(f"  HRs  : {hr}")
    print(f"  rbi: {rbi}")



def print_all_players():
    """Scan the entire Movies table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No players found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} player(s):\n")
    for player in items:
        print_movie(player)


def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_()


if __name__ == "__main__":
    main()