install.packages("syuzhet")
install.packages("openNLPdata")
install.packages("rJava")
# Load
library(ggplot2)
library(tm)
library(wordcloud)
library(syuzhet)

texts <- readLines("test2.txt")
# Read the text file from desktop
#filePath <- "/home/manoj/test2.txt"


docs <- Corpus(VectorSource(text))
# clean data 
trans <- content_transformer(function (x , pattern ) gsub(pattern, " ", x))
docs <- tm_map(docs, toSpace, "/")
docs <- tm_map(docs, toSpace, "@")
docs <- tm_map(docs, toSpace, "\\|")
docs <- tm_map(docs, content_transformer(tolower))
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, stripWhitespace)
docs <- tm_map(docs, stemDocument)

#create the document
dtm <- TermDocumentMatrix(docs)
mat <- as.matrix(dtm)
v <- sort(rowSums(mat),decreasing=TRUE)

#data frame
d <- data.frame(word = names(v),freq=v)
head(d, 10)

#generate wordcloud
set.seed(1056)
wordcloud(words = d$word, freq = d$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

#fetch sentiment words fron texts
sentiment <-get_nrc_sentiment(texts)
text <- cbind(texts,sentiment)

#count the sentiment words by category
totalsentiment <- data.frame(col_sums(text[,c(2:11)]))
names(totalsentiment) <- "count"
totalsentiment <- cbind("sentiment" =rownames(totalsentiment),totalsentiment)
rownames(totalsentiment) <- NULL

#total sentiment score of all texts
ggplot(data = totalsentiment, aes(x = sentiment,y = count)) +
  geom_bar(aes(fill = sentiment), stat = "identify") +
  theme(legend.position = "none") +
  xlab("sentiment") + ylab("total count") +ggtitle("total sentiment score")

