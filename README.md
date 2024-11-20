<h1> Python Project 15: Coffee Machine </h1>
<h2>Summary</h2>
<p>This project is for day 15 of the 100 Days of Code challenge that I'm completing as part of the Complete Python Pro Bootcamp with Dr. Angela Yu from the London App Brewery. Each project in this challenge will be using Python so that I can grow my skills in software development.</p>
<p>This project is a coffee vending machine, where the user can order an espresso, latte, or cappuccino. The machine will check if the machine has sufficient resources (i.e., check levels of water, milk, and coffee), and if so, it will accept quarters, dimes, nickels, and pennies. The machine calculates the total coins inserted and will advise if the amount is acceptable before making the coffee. If the amount is too little, it advises the user and issues a refund, and if the amount is too much, it will issue change before making the coffee. The coffee machine also has the ability to issue a report upon request, which provides the user will a status on it's coffee, water, and milk levels as well as how much profit it has made. The program will also end when the machine is told to turn off.</p>
<p>
The coffee machine uses the following learnings:
  <ul>
    <li>
      functions
    </li>
    <li>
      dictionaries and lists
    </li>
    <li>
      for and while loops
    </li>
    <li>
      if/elif/else statements
    </li>
  </ul>
</p>
<h3>Learnings</h3>
<ul>
  <li>
   This project really tested me, as I knew how I wanted to break down the steps needed to complete this project and how I wanted sections of the code to be written; however, I struggle with the layout of the code within the file. For example, I initially kept trying to make the coffee order as another elif statement to the one shown starting on line 89 and then trying to make it another if statement entirely. After reviewing a few of my other projects, I figured out to list it as the else statement.
  </li>
  <li>
    It also took me some time to figure out how I wanted the functions of the coffee-making process to run in the else statement. I spent some time writing out the functions to check resources, accept payment in the coins listed in the requirements, then make the coffee (deducting the resources and adding to the profit), but struggled a little to figure out that nested if statements were needed in the initial else statement (on line 98).
  </li>
  <li>
    I also could have made my code simpler and would like to redo this project again in the near future. For example, on line 62, I wrote "change = abs(round(drink_cost - money_received, 2))". This could be rewritten as "change = round(money_received - drink_cost, 2)". However, one positive from this is that it made me curious about whether there was a way to turn a negative number into a positive number in Python, and after some Googling, I discovered some documentation about the abs() function. Although, it may not always be necessary to use, I think this is a valuable function to be aware of.
  </li>
</ul>
<h2>Tech stack</h2>
<ul>
  <li>Python</li>
  <li>VS Code</li>
  <li>PyCharm</li>
  <li>ASCII</li>
