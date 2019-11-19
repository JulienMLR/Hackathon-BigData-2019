library(rpart)

chemin <-"E:\\Telecom Nancy\\Cours 3A\\Hackathon2019\\Hackathon-BigData-2019\\ressources\\Traité\\Finished\\InfoVis2017.csv"

df <- read.csv(chemin)
df$DATE <- NULL
df$CODE <- NULL
df$LOCALITE <- NULL
df$MIN <-NULL

comTree <- rpart(COMMENT_NOUS_AVEZ_VOUS_DECOUVERT~.,data=df)
comTreeOptimal <- prune(comTree,cp=comTree$cptable[which.min(comTree$cptable[,4]),1])
prp(comOptimal,extra=1)