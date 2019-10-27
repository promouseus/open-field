#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   titlePanel("Counter Dash"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
      sidebarPanel(

        selectInput("rack", 'Rack:',
                    unique(recordList$data_namespace$data_source$rack)
        ),
        
        uiOutput("serverSelection"),
        
        uiOutput("vmSelection"),
        
        uiOutput("dateSelection"),
        
        downloadButton("downloadData", "Export dataset")
      ),
      
      # Show a plot of the generated distribution
      mainPanel(
         plotOutput("distPlot")
      )
   )
)

# Define server logic required to draw a histogram
server <- function(input, output) {

  output$serverSelection <- renderUI({
    selectInput("server", "Server:", choices = unique(subset(recordList$data_namespace$data_source$server, recordList$data_namespace$data_source$rack == input$rack)))
  })
  
  output$vmSelection <- renderUI({
    selectInput("vm", "Vm:", choices = unique(subset(recordList$data_namespace$data_source$vm, recordList$data_namespace$data_source$rack == input$rack & recordList$data_namespace$data_source$server == input$server )))
  })
  
  output$downloadData <- downloadHandler(
    filename = function() {
      paste("download.csv", sep = "")
    },
    content = function(file) {
      write.csv(recordList, file)
    }
  )
  
  output$dateSelection <- renderUI({
    #subrange rack, server, vm here for correct date scope
    con <- mongo(collection = "collector", db = "infra", url = "mongodb://localhost",
                 verbose = TRUE, options = ssl_options())
    recordList <- con$find(query = " {}")
    recordList <- subset(recordList,
                         recordList$data_namespace$data_source$vm == input$vm
                         & recordList$data_namespace$data_source$rack == input$rack
                         & recordList$data_namespace$data_source$server == input$server
    )
    
    dateRangeInput("dates", 
                   "Date range",
                   #start = "2010-01-01", 
                   start = min(recordList$data_namespace$date),
                   #end = as.character(Sys.Date()),
                   end = max(recordList$data_namespace$date),
                   language = "en")
  })
  
   output$distPlot <- renderPlot({
  # Make reactive: now you get GUI red error texts while the select options are rebuilding
     
     library("mongolite")
     con <- mongo(collection = "collector", db = "infra", url = "mongodb://localhost",
                  verbose = TRUE, options = ssl_options())
     recordList <- con$find(query = " {}")
      recordList <- subset(recordList, recordList$data_namespace$date >= as.POSIXct(input$dates[1]) & recordList$data_namespace$date <= as.POSIXct(input$dates[2]+1) #dates[2] add 1 day for hours until next day or you will miss the last day as select converst date to 0 hour and +1 ads the 'to', better fix is to set end time of selected date at 23:59:59 then adding a day
                            & recordList$data_namespace$data_source$vm == input$vm
                            & recordList$data_namespace$data_source$rack == input$rack
                            & recordList$data_namespace$data_source$server == input$server
                           )
      
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
      
   })
}
# Run the application

# Get all records from server
shinyApp(ui = ui, server = server)