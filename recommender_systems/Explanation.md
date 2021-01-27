## Explanation for user recommendation
This is a short explanation of the functions in user_recommender.py

First the data is gotten from as json from tables of user data and stores in the file json_data

The data is first collected and merged using foreign keys into one dataframe

- get_combined_feature:
    This function gets combined features for users speciifed and requires user_id

-  get_index:
    This function gets the index of a user from the tables given

- get_actions
    This function gets the total actions count for a user's posts and requires user_id

- return_the_sender_id:
    This function checks for your user id among the sender id column to know the total number of people you've sent notifications to

- get_name_from_user_id:
    This function get the username of the user and requires user_id and requires user_id

- user_recommendation_base:
    This function recommends posts due to user preferences or suggest if it's a new user and requires user_id

- user_recommed:
    This function analyses a user and recommend posts to user and reuqires user_id

## Explanation for article recommender
his is a short explanation of the functions in article_recommender.py

First the data is gotten from as json from tables of user data and stores in the file json_data

Then the relevant data is merge and new columns are derived from gotten columns

- get_title_from_id
 This function return the title of an article and requires the id of the article

- get_title_from_index
    This function gets the title of an article based on the index of the article and require the index number

- check_action
 This funtion gets the entire actions on an article and requires the article id

- content_recommender
    This the main function that predicts the article similar to the ones inputted and requires title of the article and dataframe which is not compulsory.

- action recommender
    We also have action recommender function to suggest articles based on the most popular ones

