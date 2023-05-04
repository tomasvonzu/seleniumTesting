Feature: Sort By
    As a customer, I want to manage the service types
    to do that i will go to the web app
    and use the plattaform in order to create or edit or even delete agencies
    
    Scenario: Sort items by ascendent price
        Given the user wants to search an item
        When the user sort by ascendent price
        Then the item with the lower price should appear first
    
    Scenario: Sort items by descendent price
        Given the user wants to search an item
        When the user sort by descendent price
        Then the item with the higher price should appear first