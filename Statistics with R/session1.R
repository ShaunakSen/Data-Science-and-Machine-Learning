subject_name <- c("Jon Doe", "Jane Doe", "Markus")
temperature <- c(37.0,37.4,40.0) 
flu_status <- c(FALSE,FALSE,TRUE) 

# Print all subject names except the first
subject_name[-1]

# Print all subject names except the first and second
subject_name[c(-1,-2)]

# FACTORS


food <- factor(c("low", "high", "medium", "high", "low", "medium", "high"))

# levels are by default in alphabetic order

levels(food)

# explicitly assigning the levels

food <- factor(food, levels = c("low", "medium", "high"))

levels(food)

min(food) # doesn't work 

# order the elements acc to levels

food <- factor(food, levels = c("low", "medium", "high"), ordered = TRUE)

# once we order we can compare elements

food[1] < food[2]

min(food)


symptoms <- factor (c("SEVERE", "MILD", "MODERATE"), levels = c("MILD", "MODERATE", "SEVERE"),
                    ordered=TRUE) 

# returns a vector of TRUE and FALSE values
symptoms > "MILD"

# display 1st and 3rd elems
symptoms[c(TRUE, FALSE, TRUE)]


# Print all subject names who have more than MILD symptoms
subject_name[symptoms>"MILD"]

# -------------------------------------------------------------------------------

# LISTS

# As vectors, a collection of elements, but not every element needs to be of the same type. 
# Entries in lists can be addressed using a name for each field (or by number as in vectors).
# A list in R is like a dict in python


subject1 <- list(fullname = "Markus", temperature = 40.0, symptoms = symptoms[1])

subject1

# We can access fields in a list via the "$" separator

subject1$fullname

# accessing several elems

subject1[c("fullname", "temperature")]

# -------------------------------------------------------------------------------

# DATAFRAMES

# A data frame is used for storing data tables. 
# It is a collection of vectors or factors of equal length

patient_data <- data.frame(subject_name, temperature, flu_status, symptoms, stringsAsFactors = FALSE)

# accessing the df

patient_data$symptoms


patient_data[c("subject_name", "temperature")]


# Individual entries can also be referenced by specifying rows and columns

patient_data[2,2]

# first and 3rd rows
patient_data[c(1,3),]

# first and 3rd rows, 1st and 4th cols

patient_data[c(1,3), c(1,4)]

# We can add rows to data frames using the function rbind (). Let's add an entry for a new patient:

new_patient <- c("Mike", 40.5, TRUE, "SEVERE")

patient_data <- rbind(patient_data, new_patient)

# adding a new col: marital_status

patient_data$married <- c(TRUE, TRUE, FALSE, FALSE)

patient_data

# -------------------------------------------------------------------------------

# MATRIX

# R also provides another data structure to store values in tabular form
# Entries in a matrix must be homogeneous

m <- matrix(c(1,2,3,"ok"), nrow = 2)
m

# all entries got converted to string to preserve same data type

class(m[1,1])

m <- matrix ( c(1, 2, 3, 4), nrow = 2) 
m

# -------------------------------------------------------------------------------

# EXERCISE 1

# 1: Calculate the square root of 719

sqrt(719)

# 2: Create a new variable "b" and assign it the value 178.0. Print b.

b <- 178.0

b

# 3: Convert the data type of "b" from the previous exercise to character. Print b.

b <- as.character(b)
b

# 4: Create a vector of numbers from 1 to 6. Find out its class. Create a vector with the "mixed" elements 1,2, "a" and "b". Find out its class.

vec1 <- c(1:6)
class(vec1)

# class becomes class of the highest casted elem 

vec2 <- c(1,2,"a","b")
class(vec2)

# 5: Initialize a character vector of size 30 and assign "a" to the first element of the vector.

vec3 <- vector(mode = "character", length = 30)

vec3

vec3[1] <- "a"

vec3

# 6: Create a vector with some of your friends names. Determine the length of that vector. 
# Get the second and third friends of that vector. 
# Sort that vector (explore the use of the "sort" and "order" functions). 
# sSort that vector in reverse order.

friends <- c("mini", "paddy", "bhagu", "saurav", "suraj")
friends[2]
friends[3]

sort(friends)
# rank gives rank of each elem 
rank(friends)

# order is more complicated. order(friends) = 3 1 2 4 5 
# => 1st rank elem is in 3rd pos, 2nd is in 1st.. so on
order(friends)

sort(friends, decreasing = TRUE)

# 7: Explore the use of "rep" and "seq" to initialize vectors and generate the vector 
# ('a','a',1,2,3,4,5,7,9,11) using these commands.

vec4 <- rep('a', 2)
vec4e
vec5 <- seq(1, 4)
vec6 <- seq(5, 11, by = 2)

vec7 <- c(vec4, vec5, vec6)

vec7
