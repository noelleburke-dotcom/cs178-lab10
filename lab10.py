# name: Noelle Burke
# date:3/10/26
# description: Implementation of CRUD operations with DynamoDB — CS178 Lab 10
# proposed score: 0 (out of 5) -- if I don't change this, I agree to get 0 points.

import boto3

# boto3 uses the credentials configured via `aws configure` on EC2
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Playlist')

def create_song():
    title= (input("Please enter a song title"))
    artist= (input("Who sang the song?"))
    table.put_item(
        Item={
            'Title': title,
            'Artist': artist
        }
    )
    print("Bam song created!")
 
 
 
def print_all_songs():
    """Scan the entire Movies table and print each item."""
    table = dynamodb.Table('Playlist')
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No song found. Make sure your DynamoDB table has data.")
        return
    for song in items:
        print(song)




def delete_song():
    title = input("What is the song title? ")
    table.delete_item(
        Key={
            'Title':title,
        }
    )
    print("deleting song")
         

def print_menu():
    print("----------------------------")
    print("Press C: to CREATE a new song")
    print("Press R: to READ all songs")
    print("Press D: to DELETE a song")
    print("Press X: to EXIT application")
    print("----------------------------")

def main():
    input_char = ""
    while input_char.upper() != "X":
        print_menu()
        input_char = input("Choice: ")
        if input_char.upper() == "C":
            create_song()
        elif input_char.upper() == "R":
            print_all_songs()
        elif input_char.upper() == "D":
            delete_song()
        elif input_char.upper() == "X":
            print("exiting...")
        else:
            print("Not a valid option. Try again.")

main()
