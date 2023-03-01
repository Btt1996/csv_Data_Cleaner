library(ggplot2)
library(readr)

data <- read_csv("cleaned_data.csv")

# Create a histogram of a column called "column1"
ggplot(data, aes(x = column1)) + 
  geom_histogram(fill = "steelblue", color = "white") + 
  labs(title = "Histogram of Column 1", x = "Column 1 Values", y = "Frequency")

# Create a scatter plot of two columns called "column1" and "column2"
ggplot(data, aes(x = column1, y = column2)) + 
  geom_point(color = "steelblue") + 
  labs(title = "Scatter Plot of Column 1 and Column 2", x = "Column 1 Values", y = "Column 2 Values")

# Create a bar chart of a column called "column3"
ggplot(data, aes(x = column3)) + 
  geom_bar(fill = "steelblue", color = "white") + 
  labs(title = "Bar Chart of Column 3", x = "Column 3 Values", y = "Frequency")
