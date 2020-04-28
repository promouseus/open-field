#install.packages("mongolite")
# https://cran.r-project.org/web/packages/mongolite/mongolite.pdf
# Build upon jsonlite

# install.packages("shiny")
# install.packages("maps") # World map
# install.packages("mapproj") # Long/Lat to map

library("mongolite")
library("jsonlite")

con <- mongo(db = "collector", collection = "infra", url = "mongodb://localhost",
      verbose = TRUE, options = ssl_options())

recordList <- con$find(query = " {}")
#recordCount <- con$count(query = " {}")

#summary(recordList)

# Basic time on X (hor) and value on Y (ver)
# plot(recordList$data_namespace$sample$counterA, recordList$data_namespace$date)

# Plot 3 counters in 1 plot
#plot(recordList$data_namespace$date, recordList$data_namespace$sample$counterA,
#     type = "b", xlab = "Date", ylab = "Count", col='black', ylim=c(0,700)) # Max height 700 to auto detect
#lines(recordList$data_namespace$date, recordList$data_namespace$sample$counterB, type='b', col='red')
#lines(recordList$data_namespace$date, recordList$data_namespace$sample$counterC, type='b', col='blue')
#legend('bottomright', names(recordList$data_namespace$sample), # Location based on graph lines, top l/r or? 
#       lty=1, col=c('black','red', 'blue'), bty='n', cex=.75)

# Date selection on recordList (overwrite)
##recordList <- subset(recordList, recordList$data_namespace$date> "2014-12-03" & recordList$data_namespace$date < "2018-12-05")

# Write to CSV
## write.csv(recordList, file = "Rcsv.txt")

# Plot all counterd with different color
colorCounter <- 50
plot(recordList$data_namespace$date, recordList$data_namespace$sample$counterA,
     type = "n", xlab = "Date", ylab = "Count", col='black', ylim=c(0,700))
for(i in names(recordList$data_namespace$sample)) {
  #print(i)
  lines(recordList$data_namespace$date, recordList$data_namespace$sample[[i]], type='b', col=colors()[colorCounter])
  colorCounter <- colorCounter + 1
}
legend('bottomright', names(recordList$data_namespace$sample), # Location based on graph lines, top l/r or? 
       lty=1, col=colors()[50:600], bty='n', cex=.75)

# R maps with data coloring
# install.packages(c("maps", "mapproj"))
#helpers.R is an R script that can help you make choropleth maps,

# Shiny examples
#runExample("01_hello")      # a histogram
#runExample("02_text")       # tables and data frames
#runExample("03_reactivity") # a reactive expression
#runExample("04_mpg")        # global variables
#runExample("05_sliders")    # slider bars
#runExample("06_tabsets")    # tabbed panels
#runExample("07_widgets")    # help text and submit buttons
#runExample("08_html")       # Shiny app built from HTML
#runExample("09_upload")     # file upload wizard
#runExample("10_download")   # file download wizard
#runExample("11_timer")      # an automated timer

# Connections to Docker socket

