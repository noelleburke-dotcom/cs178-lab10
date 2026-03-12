# name: Noelle Burke
# date:3/10/26
# description: Implementation of CRUD operations with DynamoDB — CS178 Lab 10
# proposed score: 0 (out of 5) -- if I don't change this, I agree to get 0 points.

import boto3
REGION = "us-east-1"
TABLE_NAME = "Movies"
# boto3 uses the credentials configured via `aws configure` on EC2
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Movies')

def create_movie():
    print("Please enter a movie title")
    print("What year did the movie release?")
    print("What are the ratings of the movie?")
    title= (input("Please enter a movie title"))
    year= int(input("What year did the movie release?"))
    rating= int(input("What are the ratings of the movie?"))
    table.put_item(
        Item={
            'Title': title,
            'Year': year,
            'Ratings':[rating]
        }
    )
    print("Bam movie created!")
 
def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)   
 
def print_all_movies():
    """Scan the entire Movies table and print each item."""
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No movies found. Make sure your DynamoDB table has data.")
        return


def update_rating():
    print("What is the movie title? What is the rating (integer):")
    try:
        title = (input("What is the movie title? "))
        rating = int(input("What is the rating (integer): "))
        if not isinstance(title,str) or not isinstance(rating, int):
            raise ValueError("wrong entry types")
    
        table.update_item(
            Key={"Title": title},
            UpdateExpression="SET Ratings = list_append(Ratings, :r)",
            ExpressionAttributeValues={':r': [rating]}
        )
        print("updating rating")
    except ValueError :
        print("error in updating the rating")   
    

def delete_movie():
    print("What is the movie title?")
    title = print(input("What is the movie title? "))
    table.delete_item(
        Key={
            'Title':title,
        }
    )
    print("deleting movie")

def query_movie():
    title = print(input("What is the movie title? "))
    title=table.get_item(
         Key={
             'Title':title,
         }
     )
     
    movie= response.get("Item")

    if not movie:
        print("not found")
        return
    ratings=movie.get("Ratings",[])
    if ratings: #get average of rating
        average= sum(ratings)/len(ratings)
        print("Average rating is ", average)
    else:
        print("No ratings were entered")

         



def print_menu():
    print("----------------------------")
    print("Press C: to CREATE a new movie")
    print("Press R: to READ all movies")
    print("Press U: to UPDATE a movie (add a review)")
    print("Press D: to DELETE a movie")
    print("Press Q: to QUERY a movie's average rating")
    print("Press X: to EXIT application")
    print("----------------------------")

def main():
    input_char = ""
    while input_char.upper() != "X":
        print_menu()
        input_char = input("Choice: ")
        if input_char.upper() == "C":
            create_movie()
        elif input_char.upper() == "R":
            print_all_movies()
        elif input_char.upper() == "U":
            update_rating()
        elif input_char.upper() == "D":
            delete_movie()
        elif input_char.upper() == "Q":
            query_movie()
        elif input_char.upper() == "X":
            print("exiting...")
        else:
            print("Not a valid option. Try again.")

main()
