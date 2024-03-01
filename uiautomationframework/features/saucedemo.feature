Feature:
  
  Scenario Outline: Login to Application
	Given Application URL
	When login with valid <user> and <password>
	Then sauce demo home page should be displayed
	Examples:
	  | user            | password     |
	  | standard_user   | secret_sauce |
	  | locked_out_user | secret_sauce |