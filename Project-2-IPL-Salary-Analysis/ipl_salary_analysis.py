###################----------Data----------##############################
# Seasons - IPL years displayed on the X-axis
seasons = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]

# Players - Names of the 10 cricketers
players = ["Sachin", "Rahul", "Smith", "Sami", "Pollard", "Morris", "Samson", "Dhoni", "Kohli", "Sky"]

# Salaries - Each player's salary for the corresponding IPL season
sachin_salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
rahul_salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
smith_salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
sami_salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
pollard_salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
morris_salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
samson_salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
dhoni_salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
kohli_salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
sky_salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]

###################----------Data----------##############################

# Import the Matplotlib library to create graphs and charts
import matplotlib.pyplot as plt


# Create a figure (graph window) with 14 inches width and 6 inches height
plt.figure(figsize=(14, 6))

# Set the title displayed at the top of the graph
plt.title('IPL Members Salary Comparison')


# Create a list containing all 10 players' salary lists.
# Each salary list contains 10 salary values, one for each season.
cricketers_salary_list = [ sachin_salary, rahul_salary, smith_salary, sami_salary, pollard_salary, morris_salary, samson_salary, dhoni_salary, kohli_salary, sky_salary]

# Assign a different colour to each player's line in the graph
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'yellow', 'cyan', 'black']


# Loop through the 10 players using their index positions (0 to 9)
for i in range(0, 10):

    # Get the salary list of the current player using the index position
    cricketer_name = cricketers_salary_list[i]

    # Plot the player's salary values as a line on the same graph
    
    plt.plot(
        cricketer_name,   # Retrieves the salary values of the current cricketer(values) using the index position name.
        label=players[i], #label: Displays the player's name in the legend
        color=colors[i],  # color: Assigns a different colour to each player's line
        ls="--",          # ls: Uses a dashed line style
        marker="s",       # marker: Displays a square marker at each salary data point
        ms=6              # ms: Sets the marker size to 6
    )

    # Set the X-axis positions (0 to 9) to display the IPL seasons
    # rotation='vertical' displays the season names vertically
    plt.xticks(range(0, 10), seasons, rotation='vertical')

    # Display the player names with their matching colours in a legend
        plt.legend(
        loc='lower right',
        bbox_to_anchor=(1.25, 0.25) # bbox_to_anchor positions the legend outside the graph area
    )

# Automatically adjust spacing so graph elements fit properly
plt.tight_layout()

# Display the final graph containing all 10 players
plt.show()
